"""Read-only ZIP audit. Does not extract, import or execute submitted programs."""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import zipfile


PERSONAL_PATH = re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+|/(?:Users|home)/[^/\s]+/", re.I)
TEXT_SUFFIXES = {".py", ".json", ".md", ".txt", ".yaml", ".yml", ".csv"}


def all_values_equal(values, target):
    if isinstance(values, list):
        return bool(values) and all(all_values_equal(item, target) for item in values)
    return isinstance(values, (int, float)) and not isinstance(values, bool) and values == target


def audit_package(path, required=(), compile_python=False, max_uncompressed_mb=512):
    path = Path(path)
    report = {"file": path.name, "size_bytes": path.stat().st_size,
              "sha256": sha256(path.read_bytes()).hexdigest(), "findings": [], "members": []}

    def finding(code, severity, member, message):
        report["findings"].append({"code": code, "severity": severity, "member": member, "message": message})

    try:
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
            names = [i.filename for i in infos]
            files = [i for i in infos if not i.is_dir()]
            report["file_count"] = len(files)
            report["members"] = names
            if sum(i.file_size for i in infos) > max_uncompressed_mb * 1024 * 1024:
                finding("size-limit", "high", "", "Uncompressed size exceeds the configured audit budget; contents not read.")
                return report
            for name, count in Counter(n.casefold() for n in names).items():
                if count > 1:
                    finding("duplicate-member", "high", name, "Duplicate or case-colliding archive member.")
            for needed in required:
                matches = [i for i in files if PurePosixPath(i.filename).name == needed]
                if not matches:
                    finding("required-missing", "high", needed, "Required basename is absent.")
                elif len(matches) > 1:
                    finding("required-ambiguous", "high", needed, "Several files have the required basename; choose the canonical result.")
            for info in infos:
                name = info.filename
                parts = PurePosixPath(name.replace("\\", "/")).parts
                if name.startswith(("/", "\\")) or ".." in parts or re.match(r"^[A-Za-z]:", name):
                    finding("unsafe-member-path", "high", name, "Archive member is not a safe relative path.")
                if any(c in name for c in ('?', '*', '<', '>', '|', ':', '"')) or any(ord(c) < 32 for c in name):
                    finding("invalid-member-name", "high", name, "Name cannot be represented safely in Windows Explorer; check filename encoding.")
                if stat.S_ISLNK(info.external_attr >> 16):
                    finding("symlink", "high", name, "Symbolic link in a submission archive requires manual review.")
                if info.is_dir():
                    continue
                if "__pycache__" in parts or name.endswith((".pyc", ".pyo")):
                    finding("temporary-file", "medium", name, "Remove interpreter cache from the final submission.")
                if not info.file_size:
                    finding("empty-file", "medium", name, "Empty file; verify whether intentional.")
                suffix = PurePosixPath(name).suffix.lower()
                if suffix not in TEXT_SUFFIXES:
                    continue
                raw = archive.read(info)
                try:
                    text = raw.decode("utf-8-sig")
                except UnicodeDecodeError:
                    finding("text-encoding", "medium", name, "Text is not UTF-8; inspect its encoding manually.")
                    text = None
                if text is not None and PERSONAL_PATH.search(text):
                    finding("personal-path", "high", name, "Personal absolute path detected; use a package-relative path.")
                if compile_python and suffix == ".py":
                    try:
                        compile(raw, name, "exec")
                    except (SyntaxError, ValueError, UnicodeError) as error:
                        finding("python-syntax", "high", name, f"Syntax/encoding failure at line {getattr(error, 'lineno', '?')}: {getattr(error, 'msg', type(error).__name__)}")
                if suffix == ".json" and text is not None:
                    try:
                        data = json.loads(text)
                    except json.JSONDecodeError as error:
                        finding("json-invalid", "high", name, f"Invalid JSON at line {error.lineno}.")
                    else:
                        if isinstance(data, dict) and all_values_equal(data.get("temperature"), 0) and all_values_equal(data.get("moisture"), 0) and all_values_equal(data.get("minimum_properties"), 1) and all_values_equal(data.get("maximum_properties"), 1):
                            finding("mock-summary", "high", name, "Zero temperature/moisture and unit properties match a mocked-result contamination pattern; verify against a real run.")
            bad = archive.testzip()
            if bad:
                finding("crc-failed", "high", bad, "CRC check failed.")
    except (zipfile.BadZipFile, RuntimeError, OSError, NotImplementedError) as error:
        finding("archive-invalid", "high", "", f"Archive cannot be fully read: {type(error).__name__}.")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--required", action="append", default=[], help="Exact required basename; repeat per deliverable.")
    parser.add_argument("--compile-python", action="store_true", help="Compile source for syntax only; never execute it.")
    parser.add_argument("--max-uncompressed-mb", type=int, default=512)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        report = audit_package(args.source, args.required, args.compile_python, args.max_uncompressed_mb)
    except OSError as error:
        parser.exit(2, f"Cannot open archive: {error.__class__.__name__}\n")
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"{report['file']}: {report['size_bytes']} bytes, {report.get('file_count', 0)} files")
        print("SHA-256:", report["sha256"])
        for item in report["findings"]:
            print(f"[{item['severity']}] {item['code']} {item['member']}: {item['message']}")
        if not report["findings"]:
            print("No static package findings. Numerical correctness and actual execution were not checked.")
    return int(any(f["severity"] == "high" for f in report["findings"]))


if __name__ == "__main__":
    raise SystemExit(main())
