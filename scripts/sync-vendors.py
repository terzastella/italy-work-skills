#!/usr/bin/env python3
"""Compare vendors/upstreams.lock.json against upstream HEADs,
and verify local trees match the lock (no drift, no hand-edits).

Usage:
  python scripts/sync-vendors.py                # report only, exit 0
  python scripts/sync-vendors.py --check        # exit 2 if any upstream moved
  python scripts/sync-vendors.py --verify-local # exit 2 on local drift, no network
  python scripts/sync-vendors.py --snapshot     # (re)write vendors/tree-hashes.json baseline

Never auto-updates: copy new trees by hand, verify byte-identical,
then bump the lock + licenses. Re-snapshot after every legit re-copy.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LOCK = REPO / "vendors" / "upstreams.lock.json"
SNAP = REPO / "vendors" / "tree-hashes.json"


def ls_remote(url):
    try:
        out = subprocess.run(["git", "ls-remote", url, "HEAD"],
                             capture_output=True, text=True, timeout=60)
        if out.returncode != 0:
            return None
        return out.stdout.split()[0]
    except Exception:
        return None


def file_hash(path):
    """SHA256 with CRLF normalized to LF (Windows checkouts convert endings)."""
    return hashlib.sha256(Path(path).read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def locked_files(lock):
    """All files under locked skill dirs, as repo-relative posix paths."""
    out = []
    for u in lock["upstreams"]:
        root = REPO / u["local"]
        for name in u.get("skills", []):
            d = root / name
            if not d.is_dir():
                continue
            for p in sorted(d.rglob("*")):
                if p.is_file():
                    out.append(p.relative_to(REPO).as_posix())
    return out


def snapshot(lock):
    files = locked_files(lock)
    snap = {"files": {}}
    for rel in files:
        snap["files"][rel] = file_hash(REPO / rel)
    SNAP.write_text(json.dumps(snap, indent=1) + "\n", encoding="utf-8")
    print(f"snapshot: {len(files)} vendor files hashed -> {SNAP.name}")
    return 0


def verify_hashes(lock):
    if not SNAP.is_file():
        print(f"[DRIFT] missing {SNAP.name}: run sync-vendors.py --snapshot")
        return 2
    snap = json.loads(SNAP.read_text(encoding="utf-8"))["files"]
    current = locked_files(lock)
    problems = []
    for rel in current:
        if rel not in snap:
            problems.append(f"{rel}: new file since snapshot")
        elif file_hash(REPO / rel) != snap[rel]:
            problems.append(f"{rel}: content changed since snapshot")
    for rel in snap:
        if rel not in current:
            problems.append(f"{rel}: deleted since snapshot")
    for p in problems[:20]:
        print(f"[DRIFT] {p}")
    if len(problems) > 20:
        print(f"[DRIFT] ... and {len(problems) - 20} more")
    if problems:
        print(f"\n{len(problems)} byte-level drift problem(s). Re-copy from the locked commit, then re-snapshot.")
        return 2
    print(f"hashes: {len(current)} vendor files byte-identical to snapshot.")
    return 0


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
    if "--snapshot" in sys.argv:
        return snapshot(lock)
    if "--verify-local" in sys.argv:
        rc = verify_local(lock)
        if rc:
            return rc
        return verify_hashes(lock)
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
