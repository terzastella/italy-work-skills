#!/usr/bin/env python3
"""Mortgage compare neutral calculator (mutuo-tassi skill).

Compares two offers on TAEG-based French amortization totals + a shock
scenario on the variable one. Rates are explicit inputs, never advice.

Usage:
  python scripts/mutuo.py --capitale 180000 --anni 20 --taeg-a 3.1 --tan-b 2.6 --shock 2.0
"""
import argparse
import json
import sys


def rata(capitale, annuo_pct, n):
    r = annuo_pct / 100.0 / 12.0
    if r == 0:
        return round(capitale / n, 2)
    return round(capitale * r / (1 - (1 + r) ** -n), 2)


def main():
    ap = argparse.ArgumentParser(description="Mortgage TAEG comparison (rates are inputs).")
    ap.add_argument("--capitale", type=float, required=True)
    ap.add_argument("--anni", type=int, required=True)
    ap.add_argument("--taeg-a", type=float, required=True, help="fixed offer TAEG %")
    ap.add_argument("--tan-b", type=float, required=True, help="variable offer current TAN %")
    ap.add_argument("--shock", type=float, default=2.0, help="variable shock scenario in points")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.capitale <= 0 or args.anni <= 0:
        print("error: capitale/anni must be > 0", file=sys.stderr)
        return 2

    n = args.anni * 12
    ra = rata(args.capitale, args.taeg_a, n)
    rb = rata(args.capitale, args.tan_b, n)
    rs = rata(args.capitale, args.tan_b + args.shock, n)
    out = {"rata_a": ra, "totale_a": round(ra * n, 2),
           "rata_b": rb, "totale_b": round(rb * n, 2),
           "rata_b_shock": rs, "totale_b_shock": round(rs * n, 2)}

    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"A fisso TAEG {args.taeg_a:g}%: rata {ra:,.2f} x {n} = {out['totale_a']:,.2f}")
        print(f"B variabile TAN {args.tan_b:g}%: rata {rb:,.2f} x {n} = {out['totale_b']:,.2f} (+shock {args.shock}pt: rata {rs:,.2f} = {out['totale_b_shock']:,.2f})")
        print("French amortization on TAEG/TAN inputs. No endorsement — your call with numbers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
