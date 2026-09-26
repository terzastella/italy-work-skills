#!/usr/bin/env python3
"""Advance payments neutral calculator (acconti-calcolo skill).

Pure math only: the instalment SPLIT is an explicit input, never assumed
(AdE rules changed in the past — check for the year and state it).

Usage:
  python scripts/acconti.py --imposta 5820 --split 100 --year 2026
  python scripts/acconti.py --imposta 11690 --split 40,60 --year 2025
  python scripts/acconti.py --imposta 5820 --split 100 --previsione 3000 --year 2026
"""
import argparse
import json
import sys


def parse_split(spec):
    try:
        parts = [float(x) for x in spec.split(",")]
    except ValueError:
        return None
    if not parts or any(p <= 0 for p in parts) or abs(sum(parts) - 100.0) > 0.01:
        return None
    return parts


def main():
    ap = argparse.ArgumentParser(description="Advance payments math (split is an input, never assumed).")
    ap.add_argument("--imposta", type=float, required=True, help="prior-year due tax (return line cited)")
    ap.add_argument("--split", required=True, help="instalment split in percent, e.g. '100' or '40,60'")
    ap.add_argument("--soglia", type=float, default=52.0, help="no-advance threshold (verify year)")
    ap.add_argument("--previsione", type=float, default=None, help="previsionale base (lower expected income)")
    ap.add_argument("--year", type=int, required=True, help="tax year (rules valid only for this year)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.imposta < 0:
        print("error: imposta must be >= 0", file=sys.stderr)
        return 2
    parts = parse_split(args.split)
    if parts is None:
        print("error: --split must be positive percents summing to 100 (e.g. '100' or '40,60')", file=sys.stderr)
        return 2

    base = args.previsione if args.previsione is not None else args.imposta
    metodo = "previsionale" if args.previsione is not None else "storico"
    dovuto = base > args.soglia
    rate = [round(base * p / 100.0, 2) for p in parts] if dovuto else []

    out = {"year": args.year, "metodo": metodo, "base": base,
           "soglia": args.soglia, "acconto_dovuto": dovuto, "rate": rate,
           "warning": "previsionale: penalties apply if underpaid — professional check required" if metodo == "previsionale" else ""}
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        if not dovuto:
            print(f"Base {base:,.2f} <= soglia {args.soglia:,.2f} ({args.year}): no advance due.")
        else:
            print(f"Base ({metodo}): {base:,.2f} | split {args.split} ({args.year})")
            for i, r in enumerate(rate, 1):
                print(f"Rata {i}: {r:,.2f}")
            if out["warning"]:
                print("WARNING: " + out["warning"])
        print("Split per current AdE rules — stated explicitly, not assumed. Dates: see scadenze-fiscali.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
