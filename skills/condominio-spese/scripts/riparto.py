#!/usr/bin/env python3
"""Condo split neutral calculator (condominio-spese skill).

Pure math only: expected share vs charged, gap as a question for the
administrator — never an accusation.

Usage:
  python scripts/riparto.py --totale 48000 --millesimi 85 --addebitato 4500
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Condo split math (gap is a question).")
    ap.add_argument("--totale", type=float, required=True, help="rendiconto total")
    ap.add_argument("--millesimi", type=float, required=True)
    ap.add_argument("--addebitato", type=float, required=True, help="charged to the unit")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.totale, args.millesimi, args.addebitato) < 0:
        print("error: figures must be >= 0", file=sys.stderr)
        return 2

    atteso = round(args.totale * args.millesimi / 1000.0, 2)
    gap = round(args.addebitato - atteso, 2)

    if args.json:
        print(json.dumps({"atteso": atteso, "gap": gap}, indent=2))
    else:
        print(f"{args.millesimi:g}/1000 x {args.totale:,.2f} = {atteso:,.2f} attesi vs {args.addebitato:,.2f} addebitati -> gap {gap:+,.2f}")
        print("Math first, accusations never. Contest terms year-stated, if delibera confirmed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
