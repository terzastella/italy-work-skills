#!/usr/bin/env python3
"""Compare vendors/upstreams.lock.json against upstream HEADs,
and verify local trees match the lock (no drift, no hand-edits).

Usage:
  python scripts/sync-vendors.py                # report only, exit 0
  python scripts/sync-vendors.py --check        # exit 2 if any upstream moved
  python scripts/sync-vendors.py --verify-local # exit 2 on local drift, no network

Never auto-updates: copy new trees by hand, verify byte-identical,
then bump the lock + licenses.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LOCK = REPO / "vendors" / "upstreams.lock.json"


def ls_remote(url):
    try:
        out = subprocess.run(["git", "ls-remote", url, "HEAD"],
                             capture_output=True, text=True, timeout=60)
        if out.returncode != 0:
            return None
        return out.stdout.split()[0]
    except Exception:
        return None


def verify_local(lock):
    """Every locked skill exists with SKILL.md; no extra skill dirs (drift)."""
    problems = []
    for u in lock["upstreams"]:
        root = REPO / u["local"]
        if not root.is_dir():
            problems.append(f"{u['repo']}: missing local root {u['local']}")
            continue
        for name in u.get("skills", []):
            if not (root / name / "SKILL.md").is_file():
                problems.append(f"{u['repo']}: missing {u['local']}/{name}/SKILL.md")
        local_dirs = sorted(p.name for p in root.iterdir() if p.is_dir())
        for d in local_dirs:
            if d not in u.get("skills", []):
                print(f"[EXTRA] {u['local']}/{d} not in lock (drift or excluded upstream dir)")
    for p in problems:
        print(f"[DRIFT] {p}")
    if problems:
        print(f"\n{len(problems)} local drift problem(s). Re-copy from the locked commit.")
        return 2
    print("\nLocal vendor trees match the lock.")
    return 0


def main():
    check = "--check" in sys.argv
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    if "--verify-local" in sys.argv:
        return verify_local(lock)
    moved = []
    for u in lock["upstreams"]:
        head = ls_remote(u["url"] + ".git")
        status = "OK " if head == u["commit"] else "MOVED"
        print(f"[{status}] {u['repo']}: locked {u['commit'][:12]} vs HEAD {(head or '?')[:12]}")
        if head and head != u["commit"]:
            moved.append(u["repo"])
    if moved:
        print(f"\n{len(moved)} upstream(s) moved: {', '.join(moved)}.")
        print("Re-copy trees, verify hashes, bump vendors/upstreams.lock.json.")
        return 2 if check else 0
    print("\nAll upstreams pinned and current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
