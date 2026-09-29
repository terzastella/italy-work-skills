#!/usr/bin/env python3
"""Generate docs/HEALTH.md: one dated snapshot of every gate (never hand-edit).

Runs the deterministic gates as subprocesses and records their summary
lines. Slow (~minutes); run before releases, not per commit.

Usage:
  python scripts/build-health.py
"""
import datetime as dt
import importlib.util
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "docs" / "HEALTH.md"


def _load_gates():
    spec = importlib.util.spec_from_file_location(
        "run_gates", REPO / "scripts" / "run-gates.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return [(n, c) for n, c, b in mod.GATES if b]


GATES = _load_gates()


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
        status = "green" if rc == 0 else ("SKIPPED" if rc == 3 else "RED")
        rows.append((name, status, summary))
        print(f"[{status}] {name}: {summary}")
    ok = sum(1 for _, s, _ in rows if s == "green")
    skipped = sum(1 for _, s, _ in rows if s == "SKIPPED")
    lines = ["# Health snapshot — generated, do not hand-edit",
             "",
             f"Date: {today}. Regenerate with `python scripts/build-health.py`.",
             "",
             f"Gates green: {ok}/{len(rows)}" + (f", {skipped} skipped." if skipped else "."),
             "",
             "| Gate | Status | Summary |",
             "|---|---|---|"]
    lines += [f"| {n} | {s} | {sm} |" for n, s, sm in rows]
    lines += ["",
              "Green here means the deterministic gates pass. SKIPPED means the",
              "environment cannot run that gate (it runs on CI Linux instead).",
              "It does not mean normative content is current (see freshness",
              "column) or that every skill was agent-tested",
              "(`docs/COMPATIBILITY.md`).",
              ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote docs/HEALTH.md: {ok}/{len(rows)} green"
          + (f", {skipped} skipped" if skipped else ""))
    return 0 if ok + skipped == len(rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
