#!/usr/bin/env python3
"""Independent-oracle check for neutral calculators.

Each tests/oracles/<skill>-oracle.md holds HAND-COMPUTED input/expected
pairs (```json oracle-input / oracle-expected blocks) reviewed by a human.
Unlike eval-golden fixtures, the expected values live in a prose document
with derivations — a formula bug shipped together with a wrong fixture
expected still fails here. Exit 2 on mismatch, 0 when all green. CI runs this.

Usage:
  python scripts/check-oracles.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import importlib.util

REPO = Path(__file__).resolve().parents[1]


def _load_golden():
    spec = importlib.util.spec_from_file_location(
        "eval_golden", REPO / "scripts" / "eval-golden.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.argv, mod.close_enough


argv, close_enough = _load_golden()

ORACLES = {
    "imu-oracle.md": ("imu-calcolo", "imu.py"),
    "irpef-oracle.md": ("irpef-scaglioni", "irpef.py"),
    "invoice-oracle.md": ("invoice-it", "totals.py"),
    "forfettario-oracle.md": ("regime-forfettario", "forfettario.py"),
    "acconti-oracle.md": ("acconti-calcolo", "acconti.py"),
}


def blocks(path):
    txt = path.read_text(encoding="utf-8")
    inp = re.search(r"```json oracle-input\n(.*?)```", txt, re.S)
    exp = re.search(r"```json oracle-expected\n(.*?)```", txt, re.S)
    if not inp or not exp:
        return None, None
    return json.loads(inp.group(1)), json.loads(exp.group(1))


def main():
    failed = total = 0
    for fname, (skill, script) in sorted(ORACLES.items()):
        skill_dir = REPO / "skills" / skill
        inp, want = blocks(REPO / "tests" / "oracles" / fname)
        if inp is None:
            print(f"[FAIL] {fname}: missing oracle blocks")
            failed += 1
            continue
        total += 1
        try:
            r = subprocess.run(argv(skill_dir, script, inp),
                               capture_output=True, text=True, timeout=60, cwd=REPO)
        except Exception as e:  # noqa: BLE001
            print(f"[FAIL] {fname}: runner error {e}")
            failed += 1
            continue
        if r.returncode != 0:
            print(f"[FAIL] {fname}: exit {r.returncode}: {r.stderr.strip()[:200]}")
            failed += 1
            continue
        try:
            out = json.loads(r.stdout)
        except ValueError:
            print(f"[FAIL] {fname}: not JSON output")
            failed += 1
            continue
        errs = close_enough(out, want)
        if errs:
            print(f"[FAIL] {fname}:")
            for e in errs:
                print(f"  - {e}")
            failed += 1
        else:
            print(f"[ok] {fname}")
    print(f"oracles: {total - failed}/{total} independent checks green")
    return 2 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
