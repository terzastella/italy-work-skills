#!/usr/bin/env python3
"""Withholding neutral calculator (ritenuta-acconto skill).

Pure math only: 20% ordinary rate is the standard input (explicit, year-stated).
Forfettari: no withholding at all. Direction always stated (gross->net or net->gross).

Usage:
  python scripts/ritenuta.py --lordo 1000 --aliquota 20
  python scripts/ritenuta.py --netto 800 --aliquota 20
  python scripts/ritenuta.py --lordo 1000 --forfettario
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Withholding math (rate is an input).")
    ap.add_argument("--lordo", type=float, default=None)
    ap.add_argument("--netto", type=float, default=None)
    ap.add_argument("--aliquota", type=float, default=20.0, help="withholding % (year-stated)")
    ap.add_argument("--forfettario", action="store_true", help="payee is forfettario: no withholding")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if (args.lordo is None) == (args.netto is None):
        print("error: pass exactly one of --lordo or --netto", file=sys.stderr)
        return 2
    if not 0 <= args.aliquota < 100:
        print("error: aliquota must be in [0, 100)", file=sys.stderr)
        return 2

    if args.forfettario:
        base = args.lordo if args.lordo is not None else args.netto
        out = {"regime": "forfettario", "ritenuta": 0.0, "netto": base,
               "nota": "Forfettari: NO withholding — state it on the invoice."}
    elif args.lordo is not None:
        rit = round(args.lordo * args.aliquota / 100.0, 2)
        out = {"direzione": "lordo->netto", "lordo": args.lordo, "aliquota_pct": args.aliquota,
               "ritenuta": rit, "netto": round(args.lordo - rit, 2)}
    else:
        lordo = round(args.netto / (1 - args.aliquota / 100.0), 2)
        out = {"direzione": "netto->lordo", "netto": args.netto, "aliquota_pct": args.aliquota,
               "lordo": lordo, "ritenuta": round(lordo - args.netto, 2)}

    if args.json:
        print(json.dumps(out, indent=2))
    else:
        if out.get("regime"):
            print(f"Forfettario: lordo {out['netto']:,.2f} = netto (no withholding). {out['nota']}")
        elif out["direzione"] == "lordo->netto":
            print(f"Lordo {out['lordo']:,.2f} x {out['aliquota_pct']:g}% = ritenuta {out['ritenuta']:,.2f} -> netto {out['netto']:,.2f}")
        else:
            print(f"Netto {out['netto']:,.2f} -> lordo {out['lordo']:,.2f} (ritenuta {out['ritenuta']:,.2f} at {out['aliquota_pct']:g}%)")
        print("Cross-border: flag, never improvise treaty rates. Certified yearly in CU.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
