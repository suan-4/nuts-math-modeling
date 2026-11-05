from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


PLACEHOLDER_PATTERNS = (
    r"\bTODO\b",
    r"\bTBD\b",
    r"\[待填[^\]]*\]",
    r"待补充",
    r"待完善",
    r"作为(?:一个)?AI",
)
RESULT_MARKERS = (
    "得到",
    "求得",
    "求解得",
    "结果为",
    "结果表明",
    "结果显示",
    "结果发现",
    "最终为",
    "达到",
    "提升",
    "降低",
)
UNIT_PATTERN = re.compile(
    r"(?P<value>[-+]?\d+(?:\.\d+)?)\s*"
    r"(?P<unit>km/h|m/s|cm/s|mm/s|kg/m\^?2|kg/m²|μm|um|mm|cm|km|m|ms|s|%|元)"
)
QUESTION_PATTERN = re.compile(r"(?:针对|对于)?问题\s*([一二三四五六七八九十]+|\d+)")


def finding(code: str, severity: str, message: str, line: int) -> dict[str, object]:
    return {"code": code, "severity": severity, "message": message, "line": line}


def abstract_lines(lines: list[str]) -> list[tuple[int, str]]:
    start = None
    for index, line in enumerate(lines):
        if re.fullmatch(r"\s*#*\s*摘要\s*", line):
            start = index + 1
            break
    if start is None:
        return []

    selected: list[tuple[int, str]] = []
    for index in range(start, len(lines)):
        line = lines[index]
        if re.match(r"\s*关键词\s*[:：]", line):
            break
        if re.match(r"\s*#+\s+", line) and not re.fullmatch(r"\s*#*\s*摘要\s*", line):
            break
        selected.append((index + 1, line))
    return selected


def audit_text(text: str) -> list[dict[str, object]]:
    lines = text.splitlines()
    findings: list[dict[str, object]] = []

    for line_number, line in enumerate(lines, 1):
        if any(re.search(pattern, line, flags=re.IGNORECASE) for pattern in PLACEHOLDER_PATTERNS):
            findings.append(
                finding("placeholder", "high", "发现占位符或未清理的生成痕迹。", line_number)
            )

    selected_abstract_lines = abstract_lines(lines)
    abstract_blocks = []
    current = []
    for line_number, line in selected_abstract_lines:
        if QUESTION_PATTERN.search(line) and current:
            abstract_blocks.append(current)
            current = []
        current.append((line_number, line))
    if current:
        abstract_blocks.append(current)
    for block in abstract_blocks:
        line_number = block[0][0]
        line = " ".join(item[1] for item in block)
        if QUESTION_PATTERN.search(line) and not any(marker in line for marker in RESULT_MARKERS):
            findings.append(
                finding(
                    "abstract-result-missing",
                    "medium",
                    "摘要中的问题段检测到方法描述，但未检测到明确结果；请人工核对。",
                    line_number,
                )
            )

    abstract_line_numbers = {line_number for line_number, _ in selected_abstract_lines}
    abstract_questions = {
        match.group(1)
        for _, line in selected_abstract_lines
        for match in QUESTION_PATTERN.finditer(line)
    }
    body_questions: dict[str, int] = {}
    for line_number, line in enumerate(lines, 1):
        if line_number in abstract_line_numbers:
            continue
        for match in QUESTION_PATTERN.finditer(line):
            body_questions.setdefault(match.group(1), line_number)
    for question in sorted(set(body_questions) - abstract_questions):
        findings.append(
            finding(
                "abstract-question-missing",
                "medium",
                f"正文包含问题{question}，但摘要未检测到对应问题段。",
                body_questions[question],
            )
        )

    occurrences: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    for line_number, line in enumerate(lines, 1):
        for match in UNIT_PATTERN.finditer(line):
            context = line[max(0, match.start() - 18) : match.start()].strip()
            occurrences[match.group("value")].append(
                (match.group("unit"), line_number, context)
            )

    for value, records in occurrences.items():
        units = {record[0] for record in records}
        if len(units) < 2:
            continue
        contexts = [record[2] for record in records]
        shared_metric = any(
            left and right and (left in right or right in left or len(set(left) & set(right)) >= 4)
            for i, left in enumerate(contexts)
            for right in contexts[i + 1 :]
        )
        if shared_metric:
            line_number = min(record[1] for record in records)
            findings.append(
                finding(
                    "unit-conflict",
                    "medium",
                    f"数值 {value} 在相近指标语境中使用了不同单位：{', '.join(sorted(units))}。",
                    line_number,
                )
            )

    figure_refs = set(re.findall(r"(图|表)\s*(\d+)", text))
    figure_defs = set(re.findall(r"^\s*(图|表)\s*(\d+)(?:\s*[:：]|\s+)\S", text, re.M))
    for kind, missing in sorted(figure_refs - figure_defs, key=lambda item: (item[0], int(item[1]))):
        for line_number, line in enumerate(lines, 1):
            if re.search(rf"{kind}\s*{re.escape(missing)}(?!\d)", line):
                findings.append(
                    finding(
                        "unresolved-figure-table-reference",
                        "medium",
                        f"{kind}{missing} 被引用，但未检测到对应题注；请人工核对。",
                        line_number,
                    )
                )
                break

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a UTF-8 paper text export.")
    parser.add_argument("source", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    text = args.source.read_text(encoding="utf-8")
    findings = audit_text(text)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if args.format == "json":
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    else:
        if not findings:
            print("No deterministic surface findings.")
        for item in findings:
            print(
                f"[{item['severity']}] line {item['line']} "
                f"{item['code']}: {item['message']}"
            )
    return 1 if any(item["severity"] == "high" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
