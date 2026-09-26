#!/usr/bin/env python3
"""IRPEF neutral calculator (irpef-scaglioni skill).

Pure slice math only: brackets come from an explicit dated table file.
No rates are bundled — pass --scaglioni with the table for the tax year
and verify it live (reforms move brackets).

Usage:
  python scripts/irpef.py --reddito 35000 --scaglioni examples/scaglioni-2025.json --year 2025
"""
import argparse
import json
import sys


def load_brackets(path):
    data = json.load(open(path, encoding="utf-8"))
    brackets = data["scaglioni"]
    out = []
    for b in brackets:
        limite = float("inf") if b["fino"] == "inf" else float(b["fino"])
        out.append((limite, float(b["aliquota"])))
    return data.get("year"), out


def slice_math(reddito, brackets):
    fette, base = [], 0.0
    for limite, aliquota in brackets:
        if reddito <= base:
            break
        quota = min(reddito, limite) - base
        fette.append({"da": base, "a": limite if limite != float("inf") else reddito,
                      "base": quota, "aliquota": aliquota, "imposta": round(quota * aliquota, 2)})
        base = limite
    return fette


def main():
    ap = argparse.ArgumentParser(description="IRPEF slice math (brackets are inputs, never bundled).")
    ap.add_argument("--reddito", type=float, required=True, help="gross income in euro")
    ap.add_argument("--scaglioni", required=True, help="JSON bracket table with year, e.g. examples/scaglioni-2025.json")
    ap.add_argument("--year", type=int, required=True, help="tax year (table valid only for this year)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.reddito < 0:
        print("error: reddito must be >= 0", file=sys.stderr)
        return 2
    tab_year, brackets = load_brackets(args.scaglioni)
    if tab_year != args.year:
        print(f"error: table year {tab_year} != requested year {args.year} — verify live", file=sys.stderr)
        return 2

    fette = slice_math(args.reddito, brackets)
    totale = round(sum(f["imposta"] for f in fette), 2)
    media = round(totale / args.reddito * 100, 2) if args.reddito else 0.0
    marginale = round(fette[-1]["aliquota"] * 100, 2) if fette else 0.0

    if args.json:
        print(json.dumps({"year": args.year, "reddito": args.reddito, "fette": fette,
                          "imposta": totale, "aliquota_media_pct": media,
                          "aliquota_marginale_pct": marginale}, indent=2))
    else:
        for f in fette:
            print(f"Slice {f['da']:,.0f}-{f['a']:,.0f}: {f['base']:,.0f} x {f['aliquota']*100:g}% = {f['imposta']:,.2f}")
        print(f"Tax: {totale:,.2f} | average {media}% | marginal {marginale}% (year {args.year})")
        print("Earning more never nets less: only the slice above the threshold pays the higher rate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
