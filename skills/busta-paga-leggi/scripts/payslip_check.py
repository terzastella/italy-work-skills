#!/usr/bin/env python3
"""Payslip net verification (busta-paga-leggi skill).

Recomputes net pay from stated lines and reports the gap vs the stated net.
Pure arithmetic: every figure is an input. Gaps are questions for payroll,
never accusations.

Usage:
  python scripts/payslip_check.py --lordo 1950 --inps 175.5 --irpef 280 --detrazioni 125.5 --netto 1620
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Payslip net verification (recompute, don't accuse).")
    ap.add_argument("--lordo", type=float, required=True, help="gross: base + overtime + other items")
    ap.add_argument("--inps", type=float, required=True, help="INPS worker share as stated on the payslip")
    ap.add_argument("--irpef", type=float, required=True, help="IRPEF withholding as stated on the payslip")
    ap.add_argument("--detrazioni", type=float, default=0.0, help="applied tax credits / other additions")
    ap.add_argument("--netto", type=float, required=True, help="stated net pay to verify against")
    ap.add_argument("--tolleranza", type=float, default=1.0, help="match tolerance in euro (rounding)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.lordo, args.inps, args.irpef) < 0:
        print("error: lordo/inps/irpef must be >= 0", file=sys.stderr)
        return 2

    ricalcolato = round(args.lordo - args.inps - args.irpef + args.detrazioni, 2)
    gap = round(ricalcolato - args.netto, 2)
    esito = "match" if abs(gap) <= args.tolleranza else "gap: ask payroll (possible conguaglio — not an accusation)"

    if args.json:
        print(json.dumps({"lordo": args.lordo, "inps": args.inps, "irpef": args.irpef,
                          "detrazioni": args.detrazioni, "netto_dichiarato": args.netto,
                          "netto_ricalcolato": ricalcolato, "gap": gap, "esito": esito}, indent=2))
    else:
        print(f"Lordo {args.lordo:,.2f} - INPS {args.inps:,.2f} - IRPEF {args.irpef:,.2f} + detrazioni {args.detrazioni:,.2f} = {ricalcolato:,.2f}")
        print(f"Stated net: {args.netto:,.2f} | gap: {gap:+,.2f} -> {esito}")
        print("Privacy: redact name/fiscal code before sharing payslips.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
