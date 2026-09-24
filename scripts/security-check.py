#!/usr/bin/env python3
"""Local security check: secrets, PII and personal paths in skills/ and templates/.

Usage:
  python scripts/security-check.py
  python scripts/security-check.py --include-vendors
Read-only, exit 2 on hits, 0 when clean.

vendors/ is excluded by default: those are byte-identical upstream copies
reviewed at pin time (see scripts/sync-vendors.py). Use --include-vendors
for a manual (noisy: documentation examples trigger it) review.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

PATTERNS = [
    (r"(?i)aws_(secret_)?access_key_id\s*[:=]\s*AKIA[0-9A-Z]{16}", "aws-key"),
    (r"(?i)gh[pousr]_[A-Za-z0-9_]{20,}", "github-token"),
    (r"xai-[A-Za-z0-9-]{10,}", "xai-key"),
    (r"sk-(proj-)?[A-Za-z0-9-]{10,}", "openai-key"),
    (r"(?i)(password|passwd|secret)\s*[:=]\s*.+", "password-assign"),
    (r"(?i)[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", "email-pii"),
    (r"C:\\Users\\[^\\/\s]+", "win-user-path"),
    (r"/home/[^/\s]+", "linux-home-path"),
    (r"/Users/[^/\s]+", "mac-home-path"),
    (r"(?i)\b(192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[01])\.)\d+\.\d+", "private-ip"),
    (r"(?i)localhost(:\d+)?", "localhost-ref"),
]

SKIP_DIRS = {".git", "__pycache__", "tmp-test"}
SKIP_FILES = {"security-check.py", "check-diff.py"}

def scan_roots(include_vendors=False):
    roots = [REPO / "skills", REPO / "templates"]
    if include_vendors and (REPO / "vendors").exists():
        roots += [p for p in (REPO / "vendors").iterdir()
                  if p.is_dir() and p.name != "third-party"]
    files = []
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            if any(part in SKIP_DIRS for part in p.parts):
                continue
            if p.suffix.lower() not in {".md", ".py", ".json", ".txt", ".yaml", ".yml"}:
                continue
            files.append(p)
    return sorted(files)

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-vendors", action="store_true")
    args = ap.parse_args()
    hits = []
    files = scan_roots(args.include_vendors)
    if not files:
        print("No files to scan.")
        return 0
    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"WARN: {f.relative_to(REPO)} unreadable: {e}")
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for pat, label in PATTERNS:
                if re.search(pat, line):
                    # Reduce false positives on docs citing patterns as examples
                    low = line.lower()
                    if ("esempio" in low or "sample" in low or "example" in low) and label in {"email-pii"}:
                        continue
                    rel = f.relative_to(REPO)
                    hits.append((str(rel), i, label, line.strip()[:140]))
    scope = "skills/ + templates/" + (" + vendors/" if args.include_vendors else "")
    print(f"Scanned {len(files)} files in {scope}.")
    if hits:
        print(f"\nHITS ({len(hits)}): review before sharing.")
        for rel, lineno, label, preview in hits[:50]:
            print(f" - {rel}:{lineno} [{label}] {preview}")
        if len(hits) > 50:
            print(f" ... and {len(hits) - 50} more")
        return 2
    print("OK: no obvious secrets/PII/personal paths.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
