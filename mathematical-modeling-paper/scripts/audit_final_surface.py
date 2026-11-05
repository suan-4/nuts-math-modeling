from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


GENERIC_HEADINGS = {"约束条件", "模型求解与过程", "结果分析"}


def audit(text: str) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    lines = text.splitlines()
    has_gap = bool(re.search(r"(?:MIP\s*gap|MIP间隙|对偶间隙)", text, re.I))

    for line_number, raw in enumerate(lines, 1):
        line = raw.strip()
        heading = re.sub(r"^(?:[一二三四五六七八九十]+、|\d+(?:\.\d+)*\s*)", "", line)
        if heading in GENERIC_HEADINGS:
            findings.append({"code": "generic-heading", "line": line_number,
                             "message": "Use a title that names the actual model, operation, or evidence."})
        if has_gap and re.search(r"(?:全局最优|最优解|最优方案)", line):
            findings.append({"code": "optimality-language", "line": line_number,
                             "message": "Check whether solver proof/status supports this optimality claim."})
        if re.search(r"固定.{0,12}方案", line) and re.search(r"(?:稳健|鲁棒)", line):
            findings.append({"code": "fixed-sensitivity-robustness", "line": line_number,
                             "message": "A fixed-solution sensitivity study is post-evaluation, not proof of overall robustness."})
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Chinese modeling-paper text for high-risk surface claims.")
    parser.add_argument("source", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    findings = audit(args.source.read_text(encoding="utf-8"))
    if args.format == "json":
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f"[lead] line {item['line']} {item['code']}: {item['message']}")
        if not findings:
            print("No high-risk surface leads.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
