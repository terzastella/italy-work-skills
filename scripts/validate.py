#!/usr/bin/env python3
"""Validate SKILL.md against the agentskills.io spec (pragmatic subset).

Usage:
  python scripts/validate.py
  python scripts/validate.py --skill invoice-it
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

def vendor_roots():
    v = REPO / "vendors"
    if not v.exists():
        return []
    return sorted([p for p in v.iterdir() if p.is_dir() and p.name != "third-party"])

def find_skill(name):
    direct = REPO / "skills" / name
    if (direct / "SKILL.md").exists():
        return direct
    for root in vendor_roots():
        cand = root / name
        if (cand / "SKILL.md").exists():
            return cand
    return None

def all_skill_dirs():
    dirs = sorted([p for p in (REPO / "skills").iterdir() if p.is_dir()])
    for root in vendor_roots():
        dirs += sorted([p for p in root.iterdir() if p.is_dir()])
    return dirs

def validate_skill(skill_dir):
    errors = []
    warnings = []
    # Vendor copies are byte-identical upstream files: structural rules that
    # would require editing (e.g. >500-line bodies) are warnings, not errors.
    strict = "vendors" not in Path(skill_dir).parts
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
    if not fm.get("license", ""):
        (errors if strict else warnings).append(
            "frontmatter.license missing" if strict else "WARN: frontmatter.license missing (vendor file)")
    compat = fm.get("compatibility", "")
    if compat and len(compat) > 500:
        (errors if strict else warnings).append(
            f"compatibility too long ({len(compat)} > 500)" if strict else "WARN: compatibility too long (vendor file)")
    meta = fm.get("metadata", "")
    if not meta:
        (errors if strict else warnings).append(
            "frontmatter.metadata missing (author, version, lang)" if strict else "WARN: frontmatter.metadata missing (vendor file)")
    if not fm.get("allowed-tools", ""):
        (errors if strict else warnings).append(
            "frontmatter.allowed-tools missing" if strict else "WARN: frontmatter.allowed-tools missing (vendor file)")
    for section in ("## Workflow", "## Rules", "## Edge cases"):
        if section.lower() not in body.lower():
            (errors if strict else warnings).append(
                f"body missing {section} section" if strict else f"WARN: body missing {section} (vendor file)")
    if strict and Path(skill_dir).name not in ("hello-agent", "skill-starter"):
        refs = [p for p in Path(skill_dir).glob("references/*") if p.is_file()]
        exs = [p for p in Path(skill_dir).glob("examples/*") if p.is_file()]
        if not refs:
            errors.append("references/ empty or missing, add domain details")
        if not exs:
            errors.append("examples/ empty or missing, add good/bad cases")
    if len(body.strip()) < 20:
        errors.append("body too short, add instructions and examples")
    if len(body.splitlines()) > 500:
        if strict:
            errors.append("body >500 lines, move details to references/")
        else:
            warnings.append("WARN: body >500 lines (vendor file, not editable)")
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
    if args.skill:
        found = find_skill(args.skill)
        if found is None:
            print(f"Unknown skill: {args.skill}")
            return 1
        targets = [found]
    else:
        targets = all_skill_dirs()
    # also validate template
    if not args.skill and (REPO / "templates" / "skill-starter").exists():
        targets.append(REPO / "templates" / "skill-starter")
    failed = False
    for t in targets:
        errs, warns = validate_skill(t)
        label = str(t.relative_to(REPO))
        if errs:
            failed = True
            print(f"[FAIL] {label}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"[OK] {label}")
        for w in warns:
            print(f"  ! {w}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
