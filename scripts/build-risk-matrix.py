#!/usr/bin/env python3
"""Generate docs/RISK-MATRIX.md from repo sources (never hand-edit output).

Levels: L3 delicate (eval-behavior DELICATE), L2 calculator (ships scripts/),
L1 operative workflow (in GUIDED, no scripts, not delicate), L0 informative
(everything else). Freshness/review columns read live from the tree.

Usage:
  python scripts/build-risk-matrix.py
  python scripts/build-risk-matrix.py --check   # exit 2 if output differs
"""
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "docs" / "RISK-MATRIX.md"
MATRIX_TESTED = {"hello-agent", "invoice-it", "frontend-design", "tdd",
                 "brainstorming", "imu-calcolo", "irpef-scaglioni",
                 "acconti-calcolo", "regime-forfettario", "busta-paga-leggi"}


def _load_behavior():
    spec = importlib.util.spec_from_file_location(
        "eval_behavior", REPO / "scripts" / "eval-behavior.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return set(mod.DELICATE), set(mod.GUIDED)


def level(name, delicate, guided, skills_root):
    if name in delicate:
        return "L3", "delicate: law/health/tax/family, info-only + referral"
    if (skills_root / name / "scripts").is_dir():
        return "L2", "calculator: wrong math costs money"
    if name in guided:
        return "L1", "operative workflow: drafts and procedures"
    return "L0", "informative: explain and map"


def main():
    check = "--check" in sys.argv
    delicate, guided = _load_behavior()
    skills_root = REPO / "skills"
    names = sorted(p.name for p in skills_root.iterdir()
                   if p.is_dir() and (p / "SKILL.md").is_file())
    rows = []
    for name in names:
        lv, reason = level(name, delicate, guided, skills_root)
        front = (skills_root / name / "SKILL.md").read_text(encoding="utf-8")[:2000]
        fresh = "yes" if re.search(r'last_verified: "\d{4}-\d{2}-\d{2}"', front) else "no"
        review = "matrix" if name in MATRIX_TESTED else "—"
        rows.append((lv, name, reason, fresh, review))
    order = {"L3": 0, "L2": 1, "L1": 2, "L0": 3}
    rows.sort(key=lambda r: (order[r[0]], r[1]))
    counts = {lv: sum(1 for r in rows if r[0] == lv) for lv in "L3 L2 L1 L0".split()}
    lines = ["# Risk matrix — generated, do not hand-edit",
             "",
             f"Source: `eval-behavior.py` DELICATE/GUIDED + `scripts/` presence. "
             f"Regenerate with `python scripts/build-risk-matrix.py`.",
             "",
             f"Totals: {counts['L3']} L3 (delicate) · {counts['L2']} L2 (calculator) · "
             f"{counts['L1']} L1 (operative) · {counts['L0']} L0 (informative).",
             "",
             "| Skill | Level | Why | Freshness stamped | Agent-tested |",
             "|---|---|---|---|---|"]
    lines += [f"| {n} | {lv} | {rs} | {fr} | {rv} |" for lv, n, rs, fr, rv in rows]
    lines.append("")
    text = "\n".join(lines)
    if check:
        if not OUT.is_file() or OUT.read_text(encoding="utf-8") != text:
            print("RISK MATRIX CHECK FAILED: regenerate with build-risk-matrix.py")
            return 2
        print(f"risk matrix: OK ({len(rows)} skills)")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote docs/RISK-MATRIX.md: {len(rows)} skills "
          f"({counts['L3']}L3/{counts['L2']}L2/{counts['L1']}L1/{counts['L0']}L0)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
