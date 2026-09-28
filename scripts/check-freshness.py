#!/usr/bin/env python3
"""Report references/ files missing last-verified or older than 12 months.

Usage:
  python scripts/check-freshness.py           # report only, exit 0
  python scripts/check-freshness.py --check   # exit 2 on stale/missing

Advisory only (see docs/FRESHNESS.md). Pilot covers invoice-it,
imu-calcolo, regime-forfettario; full rollout is theme by theme.
"""
import datetime as dt
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PAT = re.compile(r"^last-verified:\s*(\d{4})-(\d{2})-(\d{2})", re.M)
STALE_DAYS = 365
PILOT = {"invoice-it", "imu-calcolo", "regime-forfettario"}


def main():
    check = "--check" in sys.argv
    today = dt.date.today()
    missing, stale = [], []
    for ref in sorted((REPO / "skills").glob("*/references/*.md")):
        skill = ref.parts[-3]
        m = PAT.search(ref.read_text(encoding="utf-8"))
        if not m:
            if skill in PILOT:
                missing.append(f"{skill}/{ref.name}")
            continue
        try:
            seen = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            missing.append(f"{skill}/{ref.name} (bad date)")
            continue
        if (today - seen).days > STALE_DAYS:
            stale.append(f"{skill}/{ref.name} ({m.group(0).split(': ', 1)[1]})")
    for m in missing:
        print(f"[MISSING] {m}")
    for s in stale:
        print(f"[STALE] {s}")
    pilot_refs = sum(1 for _ in (REPO / "skills").glob("*/references/*.md")
                     if _.parts[-3] in PILOT)
    print(f"freshness: {len(missing)} missing, {len(stale)} stale "
          f"(pilot: {len(PILOT)} skills, {pilot_refs} refs)")
    if check and (missing or stale):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
