#!/usr/bin/env python3
"""Deposit net neutral calculator (conti-deposito skill).

Pure math only: gross x (1 - 26%) - duty. Gross rate and duty are
explicit year-stated inputs. Net as verdict number, never gross.

Usage:
  python scripts/deposito.py --capitale 30000 --lordo 3.0 --bollo 34.2 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Deposit net math (rate and duty are inputs).")
    ap.add_argument("--capitale", type=float, required=True)
    ap.add_argument("--lordo", type=float, required=True, help="gross yearly % (promo cited)")
    ap.add_argument("--bollo", type=float, default=0.0, help="duty in euro (year-stated)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.capitale, args.lordo, args.bollo) < 0:
        print("error: figures must be >= 0", file=sys.stderr)
        return 2

    lordo_e = args.capitale * args.lordo / 100.0
    netto = round(lordo_e * 0.74 - args.bollo, 2)

    if args.json:
        print(json.dumps({"year": args.year, "netto": netto}, indent=2))
    else:
        print(f"Lordo {lordo_e:,.2f} x (1-26%) - bollo {args.bollo:,.2f} = netto {netto:,.2f} ({args.year})")
        print("Net as verdict number, never gross. Promo-duration check + FITD note. No endorsement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
