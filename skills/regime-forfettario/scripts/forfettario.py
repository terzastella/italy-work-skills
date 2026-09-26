#!/usr/bin/env python3
"""Forfettario neutral calculator (regime-forfettario skill).

Pure math only: coefficient, thresholds and rate are explicit inputs.
Eligibility gates live in references/requisiti.md — this script never
declares anyone eligible.

Usage:
  python scripts/forfettario.py --fatturato 60000 --coeff 0.78 --contributi 8000 --aliquota 15 --year 2026
  python scripts/forfettario.py --soglia-check 97000 --year 2026
"""
import argparse
import json
import sys


def imposta(fatturato, coeff, contributi, aliquota_pct):
    reddito = round(fatturato * coeff, 2)
    base = round(reddito - contributi, 2)
    return reddito, base, round(base * aliquota_pct / 100.0, 2)


def stato_soglie(fatturato, s1=85000.0, s2=100000.0):
    if fatturato <= s1:
        return "resta: entro soglia, regime confermato quest'anno e prossimo (verifica altri gate)"
    if fatturato <= s2:
        return "esci prossimo anno: oltre 85k, forfettario fino al 31/12, ordinario dal 1/1"
    return "esci subito: oltre 100k, IVA dalla fattura di sforamento + ordinario immediato"


def main():
    ap = argparse.ArgumentParser(description="Forfettario math (coefficient, thresholds, rate are inputs).")
    ap.add_argument("--fatturato", type=float, help="annual fees/revenue in euro")
    ap.add_argument("--coeff", type=float, help="profitability coefficient, e.g. 0.78")
    ap.add_argument("--contributi", type=float, default=0.0, help="deductible social contributions")
    ap.add_argument("--aliquota", type=float, choices=(5.0, 15.0), default=15.0, help="5 startup (gates!) or 15")
    ap.add_argument("--soglia-check", type=float, default=None, help="revenue figure to test against thresholds")
    ap.add_argument("--s1", type=float, default=85000.0)
    ap.add_argument("--s2", type=float, default=100000.0)
    ap.add_argument("--year", type=int, required=True, help="tax year (rules valid only for this year)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    out = {"year": args.year}
    if args.fatturato is not None:
        if args.coeff is None or not 0 < args.coeff <= 1:
            print("error: --coeff required, between 0 and 1", file=sys.stderr)
            return 2
        reddito, base, tax = imposta(args.fatturato, args.coeff, args.contributi, args.aliquota)
        out.update({"reddito": reddito, "base_imponibile": base,
                    f"imposta_{args.aliquota:g}pct": tax})
    check = args.soglia_check if args.soglia_check is not None else args.fatturato
    if check is not None:
        out["stato_soglie"] = stato_soglie(check, args.s1, args.s2)
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        if "reddito" in out:
            print(f"Reddito: {args.fatturato:,.2f} x {args.coeff} = {out['reddito']:,.2f} - {args.contributi:,.2f} = base {out['base_imponibile']:,.2f}")
            print(f"Imposta {args.aliquota:g}%: {out[f'imposta_{args.aliquota:g}pct']:,.2f} ({args.year})")
        if "stato_soglie" in out:
            print("Soglie: " + out["stato_soglie"])
        print("Math only — eligibility gates in references/requisiti.md, accountant confirms.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
