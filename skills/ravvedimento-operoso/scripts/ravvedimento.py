#!/usr/bin/env python3
"""Late-payment fix neutral calculator (ravvedimento-operoso skill).

Pure math only: penalty band % and legal rate are explicit year-stated
inputs (bands move — verify live). Spontaneous fix only; if an audit
started, this script does not apply.

Usage:
  python scripts/ravvedimento.py --imposta 2000 --giorni 40 --sanzione-pct 1.5 --tasso-legale 2.0 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Ravvedimento math (band % and legal rate are inputs).")
    ap.add_argument("--imposta", type=float, required=True)
    ap.add_argument("--giorni", type=int, required=True)
    ap.add_argument("--sanzione-pct", type=float, required=True, help="reduced penalty % for the timing band (year-stated)")
    ap.add_argument("--tasso-legale", type=float, required=True, help="legal yearly rate % (year-stated)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.imposta < 0 or args.giorni < 0 or args.sanzione_pct < 0 or args.tasso_legale < 0:
        print("error: all figures must be >= 0", file=sys.stderr)
        return 2

    sanzione = round(args.imposta * args.sanzione_pct / 100.0, 2)
    interessi = round(args.imposta * args.tasso_legale / 100.0 * args.giorni / 365.0, 2)
    totale = round(args.imposta + sanzione + interessi, 2)

    if args.json:
        print(json.dumps({"year": args.year, "sanzione": sanzione,
                          "interessi": interessi, "totale": totale}, indent=2))
    else:
        print(f"Imposta {args.imposta:,.2f} + sanzione {args.sanzione_pct:g}% = {sanzione:,.2f} + interessi {args.giorni}gg = {interessi:,.2f} -> TOTALE {totale:,.2f} ({args.year})")
        print("Pay now — each day costs. F24: tax + penalty + interest on separate lines. Verify band % live.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
