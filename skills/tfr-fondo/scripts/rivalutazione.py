#!/usr/bin/env python3
"""TFR revaluation neutral calculator (tfr-fondo skill).

Pure math only: 1.5% fixed + 75% of inflation on the accrued stock.
Inflation is an explicit year-stated input. No fund recommendations.

Usage:
  python scripts/rivalutazione.py --accantonato 20000 --inflazione 2.0 --year 2025
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="TFR revaluation math (inflation is an input).")
    ap.add_argument("--accantonato", type=float, required=True, help="accrued TFR stock in euro")
    ap.add_argument("--inflazione", type=float, required=True, help="annual inflation % (year-stated)")
    ap.add_argument("--year", type=int, required=True, help="reference year")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.accantonato < 0:
        print("error: accantonato must be >= 0", file=sys.stderr)
        return 2

    tasso = round(1.5 + 0.75 * args.inflazione, 3)
    rivalutazione = round(args.accantonato * tasso / 100.0, 2)

    if args.json:
        print(json.dumps({"year": args.year, "tasso_pct": tasso,
                          "rivalutazione": rivalutazione}, indent=2))
    else:
        print(f"Tasso ({args.year}): 1.5% + 75% x {args.inflazione}% = {tasso}%")
        print(f"Rivalutazione: {args.accantonato:,.2f} x {tasso}% = {rivalutazione:,.2f}")
        print("Mechanics only — no fund recommendations. Exit taxation: year-stated, see references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
