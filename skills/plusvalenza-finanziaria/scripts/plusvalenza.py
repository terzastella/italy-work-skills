#!/usr/bin/env python3
"""Financial gains neutral calculator (plusvalenza-finanziaria skill).

Pure math only: (gain - loss residue) x rate. Rate is an explicit
year-stated input. Regime choice stays textual + commercialista.

Usage:
  python scripts/plusvalenza.py --gain 5000 --minus 0 --aliquota 26 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Capital gains math (rate is an input).")
    ap.add_argument("--gain", type=float, required=True)
    ap.add_argument("--minus", type=float, default=0.0, help="compensable loss residue")
    ap.add_argument("--aliquota", type=float, required=True, help="rate % (year-stated)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.gain, args.minus) < 0 or not 0 <= args.aliquota < 100:
        print("error: bad figures", file=sys.stderr)
        return 2

    base = round(max(0.0, args.gain - args.minus), 2)
    imposta = round(base * args.aliquota / 100.0, 2)

    if args.json:
        print(json.dumps({"year": args.year, "base": base, "imposta": imposta}, indent=2))
    else:
        print(f"Base: {args.gain:,.2f} - minus {args.minus:,.2f} = {base:,.2f} x {args.aliquota:g}% = {imposta:,.2f} ({args.year})")
        print("Regime choice explained, no trade advice. Old minus expiring: use-or-lose timing stated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
