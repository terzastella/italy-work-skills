#!/usr/bin/env python3
"""Home-sale gain neutral calculator (plusvalenza-casa skill).

Pure math only: 5-year clock + both tax paths. Rates are explicit
year-stated inputs. Final tax is the notary's job, never this script's.

Usage:
  python scripts/pluscasa.py --acquisto 2023 --vendita 2026 --gain 40000 --sostitutiva 26 --marginale 35 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Plusvalenza casa math (rates are inputs).")
    ap.add_argument("--acquisto", type=int, required=True)
    ap.add_argument("--vendita", type=int, required=True)
    ap.add_argument("--gain", type=float, required=True, help="sale gain in euro")
    ap.add_argument("--sostitutiva", type=float, default=26.0, help="flat % at deed (year-stated)")
    ap.add_argument("--marginale", type=float, default=None, help="landlord marginal IRPEF % (asked, optional)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.vendita < args.acquisto or args.gain < 0:
        print("error: vendita >= acquisto, gain >= 0", file=sys.stderr)
        return 2

    anni = args.vendita - args.acquisto
    imponibile = anni < 5
    sost = round(args.gain * args.sostitutiva / 100.0, 2) if imponibile else 0.0
    irpef = round(args.gain * args.marginale / 100.0, 2) if (imponibile and args.marginale is not None) else None

    if args.json:
        print(json.dumps({"anni_possesso": anni, "imponibile": imponibile,
                          "sostitutiva": sost, "irpef_stimata": irpef}, indent=2))
    else:
        if not imponibile:
            print(f"Held {anni} years (>= 5): generally OUT — no gain tax. Notary confirms.")
        else:
            print(f"Held {anni} years (< 5): taxable. Sostitutiva {args.sostitutiva:g}% = {sost:,.2f}" +
                  (f" vs IRPEF ~{irpef:,.2f} (marginale asked, not assumed)" if irpef is not None else "") +
                  f" ({args.year})")
            print("Notary/commercialista computes final — method here, verdicts there.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
