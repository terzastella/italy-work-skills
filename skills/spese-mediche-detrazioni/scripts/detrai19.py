#!/usr/bin/env python3
"""Medical 19% neutral calculator (spese-mediche-detrazioni skill).

Pure math only: (traceable expenses - franchise) x 19%. Franchise is an
explicit year-stated input. Eligibility lives in references/ammissibili.md.

Usage:
  python scripts/detrai19.py --spese 900 --franchigia 129.11 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Medical deduction math (franchise is an input).")
    ap.add_argument("--spese", type=float, required=True, help="eligible traceable expenses")
    ap.add_argument("--franchigia", type=float, required=True, help="franchise in euro (year-stated)")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.spese, args.franchigia) < 0:
        print("error: figures must be >= 0", file=sys.stderr)
        return 2

    base = round(max(0.0, args.spese - args.franchigia), 2)
    detrazione = round(base * 0.19, 2)

    if args.json:
        print(json.dumps({"year": args.year, "base": base, "detrazione": detrazione}, indent=2))
    else:
        print(f"Base: {args.spese:,.2f} - franchigia {args.franchigia:,.2f} = {base:,.2f} -> 19% = {detrazione:,.2f} ({args.year})")
        print("Eligible papers only (parlante + fiscal code). Tracciabilità: year-stated rules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
