#!/usr/bin/env python3
"""Overtime pay neutral calculator (straordinari-info skill).

Pure math only: hours x hourly pay x (1 + CCNL-cited premium).
The premium is an explicit input, never a generic % as law.

Usage:
  python scripts/straord.py --ore 20 --paga-oraria 12 --maggiorazione 25
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Overtime pay math (premium is a CCNL-cited input).")
    ap.add_argument("--ore", type=float, required=True)
    ap.add_argument("--paga-oraria", type=float, required=True)
    ap.add_argument("--maggiorazione", type=float, required=True, help="premium % from CCNL table (cited)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.ore, args.paga_oraria, args.maggiorazione) < 0:
        print("error: figures must be >= 0", file=sys.stderr)
        return 2

    base = round(args.ore * args.paga_oraria, 2)
    extra = round(base * args.maggiorazione / 100.0, 2)
    totale = round(base + extra, 2)

    if args.json:
        print(json.dumps({"base": base, "maggiorazione": extra, "totale": totale}, indent=2))
    else:
        print(f"{args.ore:g}h x {args.paga_oraria:,.2f} = {base:,.2f} + {args.maggiorazione:g}% = {extra:,.2f} -> {totale:,.2f}")
        print("Premium CCNL-cited, never generic. Banca ore alternative: time instead of money.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
