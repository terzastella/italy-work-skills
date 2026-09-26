#!/usr/bin/env python3
"""Postal-bond net neutral calculator (buoni-fruttiferi skill).

Pure math only: gross x (1 - 12.5%) - duty. Series first (old series
differ), rate and duty are explicit year-stated inputs.

Usage:
  python scripts/bpf.py --capitale 10000 --lordo 2.5 --bollo 10 --year 2026
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="BPF net math (rate and duty are inputs).")
    ap.add_argument("--capitale", type=float, required=True)
    ap.add_argument("--lordo", type=float, required=True, help="gross % for the series (cited)")
    ap.add_argument("--bollo", type=float, default=0.0)
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if min(args.capitale, args.lordo, args.bollo) < 0:
        print("error: figures must be >= 0", file=sys.stderr)
        return 2

    netto = round(args.capitale * args.lordo / 100.0 * 0.875 - args.bollo, 2)

    if args.json:
        print(json.dumps({"year": args.year, "netto": netto}, indent=2))
    else:
        print(f"Lordo {args.capitale * args.lordo / 100.0:,.2f} x (1-12.5%) - bollo {args.bollo:,.2f} = netto {netto:,.2f} ({args.year})")
        print("Type identified first — old series differ. Early-exit rules stated. No endorsements.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
