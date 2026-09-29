#!/usr/bin/env python3
"""Single source of truth for all gates (CI, release, health).

Every blocking check lives in GATES exactly once. CI, release.yml and
build-health.py all consume this list, so they cannot drift apart again.

Usage:
  python scripts/run-gates.py            # blocking gates, exit 2 on failure
  python scripts/run-gates.py --advisory # advisory gates too (exit 0 always)
  python scripts/run-gates.py --list     # print the gate table, run nothing
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PY = sys.executable

# (name, argv, blocking). Advisory gates never fail the build.
GATES = [
    ("validate", [PY, "scripts/validate.py"], True),
    ("security", [PY, "scripts/security-check.py"], True),
    ("json", [PY, "-c",
      "import json;json.load(open('catalog/skills.json',encoding='utf-8'));"
      "json.load(open('.claude-plugin/plugin.json',encoding='utf-8'));print('JSON OK')"], True),
    ("indexes", [PY, "scripts/check-indexes.py"], True),
    ("catalog", [PY, "scripts/build-catalog.py", "--check"], True),
    ("golden", [PY, "scripts/eval-golden.py"], True),
    ("oracles", [PY, "scripts/check-oracles.py"], True),
    ("invariants", [PY, "scripts/check-invariants.py"], True),
    ("behavior", [PY, "scripts/eval-behavior.py"], True),
    ("freshness", [PY, "scripts/check-freshness.py", "--check"], True),
    ("sources", [PY, "scripts/check-sources.py", "--check"], True),
    ("plugins-sync", [PY, "-c",
      "import subprocess,sys;subprocess.run([sys.executable,'scripts/build-plugins.py'],cwd=r'%s',check=True);"
      "sys.exit(subprocess.run(['git','diff','--exit-code','.codex-plugin','.cursor-plugin','gemini-extension.json'],cwd=r'%s').returncode)" % (REPO, REPO)], True),
    ("install-dryrun", [PY, "scripts/install.py", "--all", "--dest", "./tmp-test", "--dry-run"], True),
    ("installer-attack", [PY, "scripts/check-installer.py"], True),
    ("vendors-verify", [PY, "scripts/sync-vendors.py", "--verify-local"], True),
    ("risk-matrix", [PY, "scripts/build-risk-matrix.py", "--check"], True),
    ("links", [PY, "scripts/check-sources.py", "--check-links"], False),
    ("spec", [PY, "scripts/check-spec.py"], False),
    ("vendors-drift", [PY, "scripts/sync-vendors.py", "--check"], False),
]


def run_one(name, argv):
    try:
        r = subprocess.run(argv, capture_output=True, text=True, timeout=900,
                           cwd=REPO)
    except Exception as e:  # noqa: BLE001
        return 2, f"runner error: {e}"
    tail = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()]
    return r.returncode, (tail[-1] if tail else "(no output)")[:160]


def main():
    args = sys.argv[1:]
    if "--list" in args:
        for name, _, blocking in GATES:
            print(f"{'BLOCK' if blocking else 'advisory':8} {name}")
        return 0
    advisory_only = "--advisory" in args
    failed = []
    for name, argv, blocking in GATES:
        if advisory_only and blocking:
            continue
        rc, summary = run_one(name, argv)
        if rc == 0:
            print(f"[ok] {name}: {summary}")
        elif not blocking:
            print(f"[advisory-FAIL] {name}: {summary}")
        else:
            print(f"[FAIL] {name}: {summary}")
            failed.append(name)
    if failed:
        print(f"gates: {len(GATES) - len(failed)}/{len(GATES)} green, FAILED: {', '.join(failed)}")
        return 2
    print(f"gates: all blocking green ({sum(1 for _, _, b in GATES if b)} gates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
