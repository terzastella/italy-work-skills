#!/usr/bin/env python3
"""Monthly budget builder (xlsx-budget-it skill).

Stdlib only: writes Income.csv + Expenses.csv and prints the Summary
(balance + per-category share). CSVs open directly in Excel; the agent
converts to .xlsx with formulas when openpyxl is available.

Usage:
  python scripts/budget.py --month 2026-01 --income 2000 --spese affitto:800 spesa:350 trasporti:120 --out budget-2026-01
"""
import argparse
import csv
import json
import sys
from pathlib import Path


def parse_spese(specs):
    out = []
    for s in specs:
        if ":" not in s:
            return None
        cat, val = s.rsplit(":", 1)
        try:
            out.append((cat.strip(), round(float(val), 2)))
        except ValueError:
            return None
    return out


def main():
    ap = argparse.ArgumentParser(description="Monthly budget builder (CSV + summary).")
    ap.add_argument("--month", required=True, help="e.g. 2026-01")
    ap.add_argument("--income", type=float, required=True)
    ap.add_argument("--spese", nargs="*", default=[], help="CAT:amount ...")
    ap.add_argument("--out", required=True, help="output stem, e.g. budget-2026-01")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    spese = parse_spese(args.spese)
    if spese is None or args.income < 0 or any(v < 0 for _, v in spese):
        print("error: spese must be CAT:amount with amount >= 0", file=sys.stderr)
        return 2

    tot_spese = round(sum(v for _, v in spese), 2)
    saldo = round(args.income - tot_spese, 2)
    quote = {c: round(v / tot_spese * 100, 1) if tot_spese else 0.0 for c, v in spese}

    if not args.json:
        out = Path(args.out)
        out.mkdir(parents=True, exist_ok=True)
        with open(out / "Income.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["date", "source", "amount"])
            w.writerow([args.month + "-01", "stipendio", f"{args.income:.2f}"])
        with open(out / "Expenses.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["date", "category", "amount"])
            for c, v in spese:
                w.writerow([args.month + "-01", c, f"{v:.2f}"])
        print(f"Wrote {out}/Income.csv + Expenses.csv (open in Excel, add SUM formulas).")
    print(json.dumps({"month": args.month, "income": args.income, "spese": tot_spese,
                      "saldo": saldo, "quote_pct": quote}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
