#!/usr/bin/env python3
"""F24 offset neutral calculator (compensazioni-f24 skill).

Pure math only: certain credits vs due taxes, visto threshold is an
explicit year-stated input. "Expected" credits do not compensate.

Usage:
  python scripts/compensa.py --crediti 2000 --debiti 1500 --soglia-visto 5000 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="F24 offset math (threshold is an input).")
    ap.add_argument("--crediti", type=float, required=True, help="certain existing credits")
    ap.add_argument("--debiti", type=float, required=True, help="taxes due")
    ap.add_argument("--soglia-visto", type=float, required=True, help="visto threshold (year-stated)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.crediti, args.debiti, args.soglia_visto) < 0:
        print("error: figures must be >= 0", file=sys.stderr)
        return 2

    compensato = round(min(args.crediti, args.debiti), 2)
    residuo_credito = round(args.crediti - compensato, 2)
    residuo_debito = round(args.debiti - compensato, 2)
    visto = args.crediti > args.soglia_visto

    if args.json:
        print(json.dumps({"year": args.year, "compensato": compensato,
                          "residuo_credito": residuo_credito, "residuo_debito": residuo_debito,
                          "visto_necessario": visto}, indent=2))
    else:
        print(f"Compensato: {compensato:,.2f} | residuo credito {residuo_credito:,.2f}, residuo debito {residuo_debito:,.2f} ({args.year})")
        print("Visto di conformità: " + ("NECESSARIO sopra soglia — no compensation without it." if visto else "non richiesto a questi importi (soglia year-stated)."))
        print("Credits must exist and be certain: expected credits do not compensate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
