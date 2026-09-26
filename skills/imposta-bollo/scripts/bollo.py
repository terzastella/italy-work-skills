#!/usr/bin/env python3
"""Stamp-duty check neutral calculator (imposta-bollo skill).

Pure threshold math only: over threshold without VAT → duty due.
Threshold and amount are explicit year-stated inputs.

Usage:
  python scripts/bollo.py --importo 500 --soglia 77.47 --bollo 2 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Bollo threshold check (threshold is an input).")
    ap.add_argument("--importo", type=float, required=True)
    ap.add_argument("--soglia", type=float, required=True, help="threshold in euro (year-stated)")
    ap.add_argument("--bollo", type=float, default=2.0, help="duty amount (year-stated)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.importo, args.soglia, args.bollo) < 0:
        print("error: figures must be >= 0", file=sys.stderr)
        return 2

    dovuta = args.importo > args.soglia

    if args.json:
        print(json.dumps({"year": args.year, "dovuta": dovuta,
                          "importo_bollo": args.bollo if dovuta else 0.0}, indent=2))
    else:
        if dovuta:
            print(f"Importo {args.importo:,.2f} > soglia {args.soglia:,.2f}: bollo EUR {args.bollo:,.2f} dovuto ({args.year}). Omissions compound — stated plainly.")
        else:
            print(f"Importo {args.importo:,.2f} <= soglia {args.soglia:,.2f}: niente bollo ({args.year}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
