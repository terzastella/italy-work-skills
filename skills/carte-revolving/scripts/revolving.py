#!/usr/bin/env python3
"""Revolving-card cost neutral calculator (carte-revolving skill).

Simulates 12 months of fixed payments on a balance at TAEG.
Minimums trap shown with numbers, exit plan with fixed instalments.

Usage:
  python scripts/revolving.py --saldo 3000 --taeg 16 --rata 200
"""
import argparse
import json
import sys


def simulate(saldo, taeg, rata, mesi=12):
    r = taeg / 100.0 / 12.0
    bal, interessi = saldo, 0.0
    for _ in range(mesi):
        if bal <= 0:
            break
        i = round(bal * r, 2)
        interessi = round(interessi + i, 2)
        bal = round(bal + i - min(rata, bal + i), 2)
    return interessi, bal


def main():
    ap = argparse.ArgumentParser(description="Revolving cost math (TAEG is an input).")
    ap.add_argument("--saldo", type=float, required=True)
    ap.add_argument("--taeg", type=float, required=True, help="TAEG % (year-stated)")
    ap.add_argument("--rata", type=float, required=True, help="fixed monthly payment")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.saldo, args.taeg, args.rata) <= 0:
        print("error: figures must be > 0", file=sys.stderr)
        return 2

    interessi, residuo = simulate(args.saldo, args.taeg, args.rata)

    if args.json:
        print(json.dumps({"interessi_12m": interessi, "residuo": residuo}, indent=2))
    else:
        print(f"Saldo {args.saldo:,.2f} al {args.taeg:g}% TAEG, rata {args.rata:,.2f}: interessi 12m {interessi:,.2f}, residuo {residuo:,.2f}")
        print("Minimums = trap with numbers, stated bluntly. Exit: fixed instalments above minimum.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
