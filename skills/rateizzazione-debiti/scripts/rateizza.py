#!/usr/bin/env python3
"""Instalment-plan neutral calculator (rateizzazione-debiti skill).

Pure math only: total with interest over N rates. Lapse counts and
thresholds live in references/piani.md (year-stated), never here.

Usage:
  python scripts/rateizza.py --debito 12000 --n-rate 72 --interesse 4 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Instalment math (interest is an input).")
    ap.add_argument("--debito", type=float, required=True)
    ap.add_argument("--n-rate", type=int, required=True, dest="n_rate")
    ap.add_argument("--interesse", type=float, required=True, help="total interest % (year-stated)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.debito < 0 or args.n_rate <= 0 or args.interesse < 0:
        print("error: debito/interesse >= 0, n-rate > 0", file=sys.stderr)
        return 2

    interessi = round(args.debito * args.interesse / 100.0, 2)
    totale = round(args.debito + interessi, 2)
    rata = round(totale / args.n_rate, 2)

    if args.json:
        print(json.dumps({"year": args.year, "interessi": interessi,
                          "totale": totale, "rata": rata}, indent=2))
    else:
        print(f"Debito {args.debito:,.2f} + interessi {args.interesse:g}% = {interessi:,.2f} -> totale {totale:,.2f} / {args.n_rate} rate = {rata:,.2f}/mese ({args.year})")
        print("Lapse rule kills lapsed plans — stated first, every time. New debts during plan: flagged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
