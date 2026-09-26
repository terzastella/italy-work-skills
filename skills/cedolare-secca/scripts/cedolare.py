#!/usr/bin/env python3
"""Flat rental tax comparison (cedolare-secca skill).

Pure math only: flat rate and the landlord's marginal IRPEF rate are
explicit inputs (the marginal rate is asked, never assumed).

Usage:
  python scripts/cedolare.py --canone 12000 --cedolare 21 --marginale 35
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Cedolare vs IRPEF comparison (rates are inputs).")
    ap.add_argument("--canone", type=float, required=True, help="annual rent in euro")
    ap.add_argument("--cedolare", type=float, default=21.0, help="flat rate % (21, or 26 additional units, year-stated)")
    ap.add_argument("--marginale", type=float, required=True, help="landlord marginal IRPEF % (asked, not assumed)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.canone < 0 or not 0 <= args.cedolare < 100 or not 0 <= args.marginale < 100:
        print("error: canone >= 0, rates in [0, 100)", file=sys.stderr)
        return 2

    flat = round(args.canone * args.cedolare / 100.0, 2)
    irpef = round(args.canone * args.marginale / 100.0, 2)
    winner = "cedolare" if flat < irpef else ("irpef" if irpef < flat else "pari")

    if args.json:
        print(json.dumps({"canone": args.canone, "cedolare_pct": args.cedolare,
                          "costo_cedolare": flat, "marginale_pct": args.marginale,
                          "costo_irpef_stimato": irpef, "vince": winner}, indent=2))
    else:
        print(f"Canone {args.canone:,.2f}: cedolare {args.cedolare:g}% = {flat:,.2f} vs IRPEF {args.marginale:g}% ~ {irpef:,.2f} (+ addizionali) -> vince: {winner}")
        print("Marginal asked, not assumed. No ISTAT update under cedolare. Commercial use excluded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
