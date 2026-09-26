#!/usr/bin/env python3
"""GS contributions neutral calculator (contributi-inps skill).

Pure math only: income x rate, split into advance/balance. The rate and
the split are explicit year-stated inputs (rates move yearly).

Usage:
  python scripts/contributi.py --reddito 40000 --aliquota 26.07 --split 40,40,20 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="GS contributions math (rate and split are inputs).")
    ap.add_argument("--reddito", type=float, required=True)
    ap.add_argument("--aliquota", type=float, required=True, help="GS rate % (year-stated)")
    ap.add_argument("--split", default="40,40,20", help="instalment percents summing to 100")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        parts = [float(x) for x in args.split.split(",")]
    except ValueError:
        print("error: --split must be percents like '40,40,20'", file=sys.stderr)
        return 2
    if args.reddito < 0 or args.aliquota < 0 or not parts or abs(sum(parts) - 100.0) > 0.01:
        print("error: bad figures (reddito/aliquota >= 0, split sums to 100)", file=sys.stderr)
        return 2

    totale = round(args.reddito * args.aliquota / 100.0, 2)
    rate = [round(totale * p / 100.0, 2) for p in parts]

    if args.json:
        print(json.dumps({"year": args.year, "totale": totale, "rate": rate}, indent=2))
    else:
        print(f"Reddito {args.reddito:,.2f} x {args.aliquota:g}% = {totale:,.2f} ({args.year})")
        for i, r in enumerate(rate, 1):
            print(f"Rata {i}: {r:,.2f}")
        print("Deductible from forfait income (see regime-forfettario). Rates move yearly — verify current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
