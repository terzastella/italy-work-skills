#!/usr/bin/env python3
"""Assegno unico band lookup (assegno-unico skill).

Table lookup only: amounts come from an explicit dated table file.
Tables move yearly — verify the current INPS circular. No-DSU = minimum.

Usage:
  python scripts/fasce.py --isee 25000 --minori 2 --tabella examples/importi-2025.json --year 2025
"""
import argparse
import json
import sys


def load_table(path):
    data = json.load(open(path, encoding="utf-8"))
    bands = []
    for b in data["fasce"]:
        top = float("inf") if b["isee_max"] == "inf" else float(b["isee_max"])
        bands.append((top, float(b["per_minore"])))
    return data.get("year"), bands


def main():
    ap = argparse.ArgumentParser(description="Assegno unico band lookup (tables are inputs).")
    ap.add_argument("--isee", type=float, required=True)
    ap.add_argument("--minori", type=int, required=True)
    ap.add_argument("--tabella", required=True, help="JSON band table with year")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.isee < 0 or args.minori < 0:
        print("error: isee/minori must be >= 0", file=sys.stderr)
        return 2
    tab_year, bands = load_table(args.tabella)
    if tab_year != args.year:
        print(f"error: table year {tab_year} != requested year {args.year} — verify live", file=sys.stderr)
        return 2

    per_minore = next(v for top, v in bands if args.isee <= top)
    mensile = round(per_minore * args.minori, 2)

    if args.json:
        print(json.dumps({"year": args.year, "isee": args.isee, "minori": args.minori,
                          "per_minore": per_minore, "mensile": mensile}, indent=2))
    else:
        print(f"Fascia ISEE {args.isee:,.0f} ({args.year}): EUR {per_minore:,.2f}/minore x {args.minori} = EUR {mensile:,.2f}/mese")
        print("VERIFY current INPS circular — tables move yearly. No-DSU = minimum. Disabled children: higher bands, see patronato.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
