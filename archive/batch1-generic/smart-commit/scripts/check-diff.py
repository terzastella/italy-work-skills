#!/usr/bin/env python3
"""Flags possible secrets and suspicious files in git diff --staged. Read-only, never commits."""
import re
import subprocess
import sys

PATTERNS = [
    (r"(?i)aws_(secret_)?access_key_id\s*[:=]\s*AKIA[0-9A-Z]{16}", "aws-key"),
    (r"(?i)gh[pousr]_[A-Za-z0-9_]{20,}", "github-token"),
    (r"xai-[A-Za-z0-9-]{10,}", "xai-key"),
    (r"sk-(proj-)?[A-Za-z0-9-]{10,}", "openai-key"),
    (r"(?i)(password|passwd|secret)\s*[:=]\s*.+", "password-assign"),
]

def run(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return out.stdout if out.returncode == 0 else ""
    except Exception as e:
        print(f"WARN: {' '.join(cmd)} failed: {e}", file=sys.stderr)
        return ""

def main():
    diff = run(["git", "diff", "--staged", "--unified=0"])
    if not diff.strip():
        diff = run(["git", "diff", "--unified=0"])
    if not diff.strip():
        print("OK: empty diff, nothing to check.")
        return 0
    hits = []
    for i, line in enumerate(diff.splitlines(), 1):
        if not line.startswith("+") or line.startswith("+++"):
            continue
        for pat, label in PATTERNS:
            if re.search(pat, line):
                hits.append((i, label, line[:160]))
    stat = run(["git", "diff", "--staged", "--stat"])
    print(stat or "(no staged stat)")
    if hits:
        print("\nSUSPICIOUS (verify before committing):")
        for lineno, label, preview in hits:
            print(f" - line~{lineno} [{label}] {preview}")
        return 2
    print("\nOK: no obvious secrets. Remember: check files >1MB and TODOs.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
