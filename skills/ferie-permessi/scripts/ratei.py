#!/usr/bin/env python3
"""Holiday accrual neutral calculator (ferie-permessi skill).

Pure math only: annual entitlement comes from the CCNL (explicit input),
part-time scales it. Deadlines live in references, not here.

Usage:
  python scripts/ratei.py --spettanza 26 --mese 7 --fruiti 10
  python scripts/ratei.py --spettanza 26 --part-time 50 --mese 6
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Holiday accrual math (entitlement is an input, CCNL-cited).")
    ap.add_argument("--spettanza", type=float, required=True, help="annual holiday entitlement in days (CCNL-cited)")
    ap.add_argument("--part-time", type=float, default=100.0, help="work percentage (100 = full-time)")
    ap.add_argument("--mese", type=int, required=True, choices=range(1, 13), help="current month 1-12")
    ap.add_argument("--fruiti", type=float, default=0.0, help="days already taken")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.spettanza <= 0 or not 0 < args.part_time <= 100 or args.fruiti < 0:
        print("error: spettanza > 0, 0 < part-time <= 100, fruiti >= 0", file=sys.stderr)
        return 2

    rateo_exact = args.spettanza * args.part_time / 100.0 / 12.0
    rateo = round(rateo_exact, 2)
    maturato = round(rateo_exact * args.mese, 2)
    residuo = round(maturato - args.fruiti, 2)

    if args.json:
        print(json.dumps({"rateo_mensile": rateo, "maturato": maturato,
                          "fruiti": args.fruiti, "residuo": residuo}, indent=2))
    else:
        print(f"Rateo: {args.spettanza:g} x {args.part_time:g}% / 12 = {rateo} gg/mese")
        print(f"Maturato a mese {args.mese}: {maturato} - fruiti {args.fruiti:g} = residuo {residuo}")
        print("Day counts only with CCNL cited. Fruition deadlines: year-stated, see references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
