#!/usr/bin/env python3
"""Generate docs/HEALTH.md: one dated snapshot of every gate (never hand-edit).

Runs the deterministic gates as subprocesses and records their summary
lines. Slow (~minutes); run before releases, not per commit.

Usage:
  python scripts/build-health.py
"""
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "docs" / "HEALTH.md"

GATES = [
    ("validate", [sys.executable, "scripts/validate.py"]),
    ("security", [sys.executable, "scripts/security-check.py"]),
    ("indexes", [sys.executable, "scripts/check-indexes.py"]),
    ("catalog", [sys.executable, "scripts/build-catalog.py", "--check"]),
    ("golden", [sys.executable, "scripts/eval-golden.py"]),
    ("oracles", [sys.executable, "scripts/check-oracles.py"]),
    ("invariants", [sys.executable, "scripts/check-invariants.py"]),
    ("behavior", [sys.executable, "scripts/eval-behavior.py"]),
    ("freshness", [sys.executable, "scripts/check-freshness.py"]),
    ("vendors", [sys.executable, "scripts/sync-vendors.py", "--verify-local"]),
    ("risk-matrix", [sys.executable, "scripts/build-risk-matrix.py", "--check"]),
]


def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600,
                           cwd=REPO)
    except Exception as e:  # noqa: BLE001
        return 2, f"runner error: {e}"
    tail = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()]
    summary = tail[-1] if tail else "(no output)"
    return r.returncode, summary[:160]


def main():
    today = dt.date.today().isoformat()
    rows = []
    for name, cmd in GATES:
        rc, summary = run(cmd)
        status = "green" if rc == 0 else "RED"
        rows.append((name, status, summary))
        print(f"[{status}] {name}: {summary}")
    ok = sum(1 for _, s, _ in rows if s == "green")
    lines = ["# Health snapshot — generated, do not hand-edit",
             "",
             f"Date: {today}. Regenerate with `python scripts/build-health.py`.",
             "",
             f"Gates green: {ok}/{len(rows)}.",
             "",
             "| Gate | Status | Summary |",
             "|---|---|---|"]
    lines += [f"| {n} | {s} | {sm} |" for n, s, sm in rows]
    lines += ["",
              "Green here means the deterministic gates pass. It does not mean",
              "normative content is current (see freshness column) or that every",
              "skill was agent-tested (see `docs/COMPATIBILITY.md`).",
              ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote docs/HEALTH.md: {ok}/{len(rows)} green")
    return 0 if ok == len(rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
