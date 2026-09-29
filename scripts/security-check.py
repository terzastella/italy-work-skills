#!/usr/bin/env python3
"""Repo-wide security check: secrets, PII and personal paths.

Usage:
  python scripts/security-check.py
  python scripts/security-check.py --include-vendors
Read-only, exit 2 on hits, 0 when clean.

Scans skills/, templates/, archive/, docs/, catalog/, scripts/ and root
config/docs files. vendors/ is excluded by default: those are byte-identical
upstream copies reviewed at pin time (see scripts/sync-vendors.py).
Use --include-vendors for a manual (noisy: documentation examples trigger it)
review.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

PATTERNS = [
    (r"(?i)aws_(secret_)?access_key_id\s*[:=]\s*AKIA[0-9A-Z]{16}", "aws-key"),
    (r"(?i)gh[pousr]_[A-Za-z0-9_]{20,}", "github-token"),
    (r"github_pat_[A-Za-z0-9_]{20,}", "github-fine-grained-pat"),
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
SKIP_DIRS = {".git", "__pycache__", "tmp-test", "tmp-test-install",
             "node_modules", ".venv", "outputs"}

# Known-safe hits: (path prefix, label or None for any label). Tight by
# default: whole-file allows exist only where the file MUST contain
# pattern-like strings (scanner definitions, security docs). Reviewed
# 2026-09-28 — every entry below maps to a verified false positive.
ALLOW = [
    ("docs/TEST-PLAN", "localhost-ref"),      # local Ollama endpoint logs
    ("docs/COMPATIBILITY.md", "localhost-ref"),
    ("docs/BATCHES.md", "localhost-ref"),
    ("docs/TEST-PLAN-LOCAL-MATRIX.md", "localhost-ref"),
    ("scripts/security-check.py", "win-user-path"),    # own pattern defs
    ("scripts/security-check.py", "linux-home-path"),
    ("scripts/security-check.py", "mac-home-path"),
    ("scripts/security-check.py", "localhost-ref"),    # allow-listed log paths
    ("scripts/security-check.py", "email-pii"),        # fake-sample comment
    ("scripts/validate.py", "win-user-path"),          # own pattern def
    ("scripts/validate.py", "linux-home-path"),
    ("scripts/validate.py", "mac-home-path"),
    ("docs/SECURITY.md", "win-user-path"),             # documents the pattern
    ("docs/SECURITY.md", "linux-home-path"),
    ("SECURITY.md", "win-user-path"),
    ("SECURITY.md", "linux-home-path"),
    ("press-release-it/examples/press-cases.md", "email-pii"),  # john@example.com [sample data]
    ("catalog/vendors-manifest.json", "xai-key"),  # vendor skill name false hit, not a key
]

# Generated install copies (gitignored, byte-copies of skills/ or vendors/).
# Scanned sources already cover their content; hits here would double-report.
ADAPTER_SKILL_DIRS = {".agents/skills", ".opencode/skills", ".claude/skills",
                      ".grok/skills", ".cursor/skills", ".github/skills",
                      ".gemini/skills", ".windsurf/skills"}


def allowed(rel, label):
    return any(rel.startswith(p) if lbl is None else (rel.startswith(p) and label == lbl)
               for p, lbl in ALLOW)


def scan_roots(include_vendors=False):
    roots = [REPO / "skills", REPO / "templates", REPO / "archive",
             REPO / "docs", REPO / "catalog", REPO / "scripts"]
    roots += [REPO / f for f in ("llms.txt", "README.md", "README-IT.md",
                                 "CONTRIBUTING.md", "SECURITY.md", "AGENTS.md",
                                 "CHANGELOG.md", "RELEASE-NOTES.md")
              if (REPO / f).exists()]
    roots += [p for p in REPO.glob(".*.json*") if p.is_file()]
    for sub in (".github", "hooks", ".claude-plugin", ".codex-plugin",
                ".cursor-plugin", ".agents", ".claude", ".grok", ".opencode",
                ".windsurf", ".cursor", ".gemini"):
        if (REPO / sub).exists():
            roots.append(REPO / sub)
    if include_vendors and (REPO / "vendors").exists():
        roots += [p for p in (REPO / "vendors").iterdir()
                  if p.is_dir() and p.name != "third-party"]
    files = []
    for root in roots:
        if not root.exists():
            continue
        if root.is_file():
            files.append(root)
            continue
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            rel = p.relative_to(REPO).as_posix()
            if any(rel == d or rel.startswith(d + "/") for d in ADAPTER_SKILL_DIRS):
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
            hits.append((str(f.relative_to(REPO)), 0, "unreadable",
                         "file could not be read: treated as failure"))
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for pat, label in PATTERNS:
                if re.search(pat, line):
                    # Reduce false positives on docs citing patterns as examples
                    low = line.lower()
                    if ("esempio" in low or "sample" in low or "example" in low) and label in {"email-pii"}:
                        continue
                    rel = f.relative_to(REPO)
                    if allowed(str(rel).replace("\\", "/"), label):
                        continue
                    hits.append((str(rel), i, label, line.strip()[:140]))
    scope = "repo-wide" + (" + vendors/" if args.include_vendors else " (vendors excluded)")
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
