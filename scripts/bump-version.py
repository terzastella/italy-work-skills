#!/usr/bin/env python3
"""SemVer bump for catalog + plugin manifests (superpowers-2 block).

Reads the version from catalog/skills.json, bumps it, writes it back to
all managed manifests (see .version-bump.json), and prints the follow-ups
(CHANGELOG entry, commit, tag). Never commits or tags by itself.

Usage:
  python scripts/bump-version.py --patch   # fixes, depth work, docs
  python scripts/bump-version.py --minor   # new skills
  python scripts/bump-version.py --major   # breaking layout
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CATALOG = REPO / "catalog" / "skills.json"


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--patch", action="store_true")
    g.add_argument("--minor", action="store_true")
    g.add_argument("--major", action="store_true")
    args = ap.parse_args()

    lock = json.loads((REPO / ".version-bump.json").read_text(encoding="utf-8"))
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    major, minor, patch = (int(x) for x in data["version"].split("."))
    if args.major:
        major, minor, patch = major + 1, 0, 0
    elif args.minor:
        minor, patch = minor + 1, 0
    else:
        patch += 1
    new = f"{major}.{minor}.{patch}"

    for rel in lock["managed_files"]:
        p = REPO / rel
        if not p.exists():
            print(f"skip (missing): {rel}")
            continue
        text = p.read_text(encoding="utf-8")
        obj = json.loads(text)
        obj["version"] = new
        p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"bumped {rel} -> {new}")

    # gemini-extension.json uses the same version key; build-plugins keeps
    # skill lists in sync — remind, don't second-guess:
    print("next: python scripts/build-plugins.py  # re-sync skill lists")
    print("next: CHANGELOG entry + commit + git tag -a v" + new)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
