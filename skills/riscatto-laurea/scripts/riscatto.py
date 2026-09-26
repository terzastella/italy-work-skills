#!/usr/bin/env python3
"""Degree-buyback cost neutral calculator (riscatto-laurea skill).

Pure math only: years x annual tariff. The tariff comes from INPS tables
for the year (explicit input, never bundled) — ordinary vs agevolato differ.

Usage:
  python scripts/riscatto.py --anni 5 --tariffa 6000 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Riscatto cost math (tariff is a year-stated input).")
    ap.add_argument("--anni", type=int, required=True, help="uncovered degree years")
    ap.add_argument("--tariffa", type=float, required=True, help="annual tariff in euro (INPS table, year-stated)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.anni <= 0 or args.tariffa < 0:
        print("error: anni > 0, tariffa >= 0", file=sys.stderr)
        return 2

    costo = round(args.anni * args.tariffa, 2)
    if args.json:
        print(json.dumps({"year": args.year, "costo": costo}, indent=2))
    else:
        print(f"Costo ({args.year}): {args.anni} anni x {args.tariffa:,.2f} = {costo:,.2f}")
        print("Method choice with numbers, not advice as fact. Deductibility: current rules cited. INPS/patronato files it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
