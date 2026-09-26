#!/usr/bin/env python3
"""Occasional-work net neutral calculator (collaborazioni-occasionali skill).

Pure math only: gross - 20% withholding, INPS franchise as explicit
year-stated input. Habituality verdict lives in the skill text, not here.

Usage:
  python scripts/occasionali.py --lordo 4000 --ritenuta 20 --franchigia-inps 5000 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Occasional net math (thresholds are inputs).")
    ap.add_argument("--lordo", type=float, required=True)
    ap.add_argument("--ritenuta", type=float, default=20.0, help="withholding % (year-stated)")
    ap.add_argument("--franchigia-inps", type=float, required=True, help="yearly INPS franchise (year-stated)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.lordo < 0 or not 0 <= args.ritenuta < 100 or args.franchigia_inps < 0:
        print("error: bad figures", file=sys.stderr)
        return 2

    rit = round(args.lordo * args.ritenuta / 100.0, 2)
    netto = round(args.lordo - rit, 2)
    inps_dovuta = args.lordo > args.franchigia_inps

    if args.json:
        print(json.dumps({"year": args.year, "ritenuta": rit, "netto": netto,
                          "inps_dovuta": inps_dovuta}, indent=2))
    else:
        print(f"Lordo {args.lordo:,.2f} - ritenuta {args.ritenuta:g}% = {rit:,.2f} -> netto {netto:,.2f} ({args.year})")
        print("INPS Gestione Separata: " + ("DOVUTA sopra franchigia — iscrizione + versamento." if inps_dovuta else "sotto franchigia — niente INPS su questi importi."))
        print("Habitual = VAT needed even under 5.000: the key test lives in the skill.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
