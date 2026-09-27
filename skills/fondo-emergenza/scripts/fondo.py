#!/usr/bin/env python3
"""Emergency-fund size neutral calculator (fondo-emergenza skill).

Pure math only: 3-6 months essential expenses (6x/12x for freelancers),
plus months-to-target from surplus. Method, not personal advice.

Usage:
  python scripts/fondo.py --spese 2000 --profilo dipendente
  python scripts/fondo.py --spese 2000 --profilo freelance --surplus 750
"""
import argparse
import json
import math
import sys


def main():
    ap = argparse.ArgumentParser(description="Emergency fund sizing (profile is an input).")
    ap.add_argument("--spese", type=float, required=True, help="essential monthly expenses")
    ap.add_argument("--profilo", choices=("dipendente", "freelance"), default="dipendente")
    ap.add_argument("--surplus", type=float, default=None, help="monthly surplus for build-up")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.spese <= 0 or (args.surplus is not None and args.surplus <= 0):
        print("error: spese/surplus must be > 0", file=sys.stderr)
        return 2

    mult = (3, 6) if args.profilo == "dipendente" else (6, 12)
    low, high = round(args.spese * mult[0], 2), round(args.spese * mult[1], 2)
    out = {"profilo": args.profilo, "target_min": low, "target_max": high}
    if args.surplus is not None:
        mid = (low + high) / 2.0
        out["mesi_per_target_medio"] = math.ceil(mid / args.surplus)

    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"Profilo {args.profilo}: spese {args.spese:,.2f}/mese -> target {low:,.2f}-{high:,.2f}")
        if "mesi_per_target_medio" in out:
            print(f"Piano: surplus {args.surplus:,.2f}/mese -> target medio in {out['mesi_per_target_medio']} mesi")
        print("Liquid means liquid: no funds/ETFs/crypto for this money. Rebuild after use.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
