#!/usr/bin/env python3
"""Validate SKILL.md against the agentskills.io spec (pragmatic subset).

Usage:
  python scripts/validate.py
  python scripts/validate.py --skill smart-commit
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME = 64
MAX_DESC = 1024

def split_frontmatter(text):
    if not text.startswith("---"):
        return None, "missing opening --- frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "unclosed frontmatter"
    return parts[1], parts[2]

def parse_simple_yaml(fm):
    data = {}
    for line in fm.strip().splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"').strip("'")
    return data

def validate_skill(skill_dir):
    errors = []
    warnings = []
    sk = Path(skill_dir) / "SKILL.md"
    if not sk.exists():
        return [f"{skill_dir}: missing SKILL.md"], []
    text = sk.read_text(encoding="utf-8")
    fm_raw, body = split_frontmatter(text)
    if fm_raw is None:
        return [f"{sk}: {body}"], []
    fm = parse_simple_yaml(fm_raw)
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        errors.append("frontmatter.name missing (required)")
    elif len(name) > MAX_NAME or not NAME_RE.match(name):
        errors.append(f"name '{name}' invalid: hyphen-case, max {MAX_NAME}")
    if Path(skill_dir).name != name:
        errors.append(f"name '{name}' != folder name '{Path(skill_dir).name}'")
    if not desc:
        errors.append("frontmatter.description missing (required)")
    elif len(desc) > MAX_DESC:
        errors.append(f"description too long ({len(desc)} > {MAX_DESC})")
    if len(body.strip()) < 20:
        errors.append("body too short, add instructions and examples")
    if len(body.splitlines()) > 500:
        errors.append("body >500 lines, move details to references/")
    # Warning locali (non bloccanti): PII, path assoluti, code-block senza linguaggio
    if re.search(r"(?i)[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", body):
        warnings.append("WARN: possible email in body, check PII")
    if re.search(r"C:\\Users\\|/home/|/Users/", text):
        warnings.append("WARN: personal absolute path, use relative paths")
    in_code = False
    for i, line in enumerate(body.splitlines(), 1):
        s = line.strip()
        if not in_code and s.startswith("```"):
            if s == "```":
                warnings.append(f"WARN: code block without language ~line {i}")
            in_code = True
        elif in_code and s.startswith("```"):
            in_code = False
    return errors, warnings

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", default=None)
    args = ap.parse_args()
    targets = [REPO / "skills" / args.skill] if args.skill else sorted(
        [p for p in (REPO / "skills").iterdir() if p.is_dir()])
    # also validate template
    if not args.skill and (REPO / "templates" / "skill-starter").exists():
        targets.append(REPO / "templates" / "skill-starter")
    failed = False
    for t in targets:
        errs, warns = validate_skill(t)
        if errs:
            failed = True
            print(f"[FAIL] {t.name}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"[OK] {t.name}")
        for w in warns:
            print(f"  ! {w}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
