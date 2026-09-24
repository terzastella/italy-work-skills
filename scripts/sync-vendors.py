#!/usr/bin/env python3
"""Compare vendors/upstreams.lock.json against upstream HEADs.

Usage:
  python scripts/sync-vendors.py          # report only, exit 0
  python scripts/sync-vendors.py --check  # exit 2 if any upstream moved

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


def main():
    check = "--check" in sys.argv
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
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
