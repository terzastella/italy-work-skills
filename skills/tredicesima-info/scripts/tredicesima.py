#!/usr/bin/env python3
"""13th-salary accrual neutral calculator (tredicesima-info skill).

Pure math only: monthly pay items included come from the CCNL
(explicit input). Part-time scales it.

Usage:
  python scripts/tredicesima.py --retribuzione 1800 --mesi 8
  python scripts/tredicesima.py --retribuzione 1800 --mesi 12 --part-time 50
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Tredicesima accrual math (pay items are inputs).")
    ap.add_argument("--retribuzione", type=float, required=True, help="monthly pay base (CCNL items cited)")
    ap.add_argument("--mesi", type=int, required=True, choices=range(0, 13), help="worked months 0-12")
    ap.add_argument("--part-time", type=float, default=100.0)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.retribuzione < 0 or not 0 < args.part_time <= 100:
        print("error: retribuzione >= 0, 0 < part-time <= 100", file=sys.stderr)
        return 2

    exact = args.retribuzione * args.part_time / 100.0 / 12.0
    maturato = round(exact * args.mesi, 2)

    if args.json:
        print(json.dumps({"rateo_mensile": round(exact, 2), "maturato": maturato}, indent=2))
    else:
        print(f"Rateo: {args.retribuzione:,.2f} x {args.part_time:g}% / 12 = {round(exact, 2):,.2f}/mese")
        print(f"Maturato ({args.mesi} mesi): {maturato:,.2f}")
        print("Items included vary by CCNL — cite the contract. Resigned mid-year: share due.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
