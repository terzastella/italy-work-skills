#!/usr/bin/env python3
"""IMU neutral calculator (imu-calcolo skill).

Pure math only: no rates are bundled (municipal rates change yearly and per
comune). The caller passes rendita, multiplier, rate and year explicitly.

Usage:
  python scripts/imu.py --rendita 850 --moltiplicatore 160 --aliquota-per-mille 10.6 --year 2026
  python scripts/imu.py --rendita 850 --moltiplicatore 160 --aliquota-per-mille 10.6 --detrazione 200 --mesi 6 --year 2026
"""
import argparse
import json
import sys

RIVALUTAZIONE = 1.05


def base_imponibile(rendita, moltiplicatore):
    return round(rendita * RIVALUTAZIONE * moltiplicatore, 2)


def imposta_annua(base, aliquota_per_mille, detrazione=0.0):
    return round(base * aliquota_per_mille / 1000.0 - detrazione, 2)


def rate(imposta):
    # Acconto (giugno) = metà arrotondata per eccesso al centesimo, saldo = resto.
    acconto = round(imposta / 2.0, 2)
    return acconto, round(imposta - acconto, 2)


def main():
    ap = argparse.ArgumentParser(description="IMU neutral calculator (math only, rates are inputs).")
    ap.add_argument("--rendita", type=float, required=True, help="rendita catastale in euro")
    ap.add_argument("--moltiplicatore", type=float, required=True, help="moltiplicatore per categoria catastale")
    ap.add_argument("--aliquota-per-mille", type=float, required=True, help="municipal rate, e.g. 10.6")
    ap.add_argument("--detrazione", type=float, default=0.0, help="annual deduction in euro (e.g. 200 luxury homes)")
    ap.add_argument("--mesi", type=int, default=12, choices=range(1, 13), help="months of possession")
    ap.add_argument("--year", type=int, required=True, help="tax year (figures valid only for this year)")
    ap.add_argument("--json", action="store_true", help="output JSON instead of text")
    args = ap.parse_args()

    if args.rendita <= 0 or args.moltiplicatore <= 0 or args.aliquota_per_mille < 0:
        print("error: rendita/moltiplicatore must be > 0, aliquota >= 0", file=sys.stderr)
        return 2

    base = base_imponibile(args.rendita, args.moltiplicatore)
    annua_intera = imposta_annua(base, args.aliquota_per_mille, args.detrazione)
    fattore = args.mesi / 12.0
    dovuta = round(annua_intera * fattore, 2)
    acconto, saldo = rate(dovuta)

    out = {
        "year": args.year,
        "base_imponibile": base,
        "imposta_annua_intera": annua_intera,
        "mesi_possesso": args.mesi,
        "imposta_dovuta": dovuta,
        "acconto_giugno": acconto,
        "saldo_dicembre": saldo,
    }
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"Base: {args.rendita} x 1.05 x {args.moltiplicatore:g} = EUR {base:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"Imposta dovuta ({args.year}, {args.mesi} mesi): EUR {dovuta:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"Acconto giugno: EUR {acconto:,.2f} + Saldo dicembre: EUR {saldo:,.2f} (F24)".replace(",", "X").replace(".", ",").replace("X", "."))
        print("Verify the municipal rate on the comune delibera before paying.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
