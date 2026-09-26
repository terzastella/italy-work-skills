#!/usr/bin/env python3
"""Invoice totals neutral calculator (invoice-it skill).

Pure arithmetic only: line totals, VAT grouped by rate, grand total.
Never invents VAT IDs, clients, or numbers — items are explicit inputs.

Usage:
  python scripts/totals.py --items examples/items-610.json
  python scripts/totals.py --items '[{"desc":"x","qty":2,"price":100.0,"iva":22.0}]'
"""
import argparse
import json
import sys


def load_items(spec):
    try:
        if spec.strip().startswith("["):
            return json.loads(spec)
        return json.load(open(spec, encoding="utf-8"))
    except (ValueError, OSError) as e:
        print(f"error: cannot read items: {e}", file=sys.stderr)
        return None


def compute(items):
    lines, iva_map, imponibile = [], {}, 0.0
    for it in items:
        tot = round(it["qty"] * it["price"], 2)
        iva = round(tot * it["iva"] / 100.0, 2)
        lines.append({"desc": it["desc"], "riga": tot, f"iva_{it['iva']:g}pct": iva})
        iva_map[it["iva"]] = round(iva_map.get(it["iva"], 0.0) + iva, 2)
        imponibile = round(imponibile + tot, 2)
    totale = round(imponibile + sum(iva_map.values()), 2)
    return {"righe": lines, "imponibile": imponibile, "iva_per_aliquota": iva_map, "totale": totale}


def main():
    ap = argparse.ArgumentParser(description="Invoice totals math (items are inputs).")
    ap.add_argument("--items", required=True, help="JSON file or inline JSON array")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    items = load_items(args.items)
    if items is None:
        return 2
    for it in items:
        if it["qty"] <= 0 or it["price"] < 0 or it["iva"] < 0:
            print("error: qty > 0, price/iva >= 0 required", file=sys.stderr)
            return 2

    out = compute(items)
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        for i, l in enumerate(out["righe"], 1):
            print(f"Item {i}: {l['desc']} — riga EUR {l['riga']:,.2f}")
        iva_str = " | ".join(f"VAT {k:g}%: EUR {v:,.2f}" for k, v in sorted(out["iva_per_aliquota"].items()))
        print(f"Taxable: EUR {out['imponibile']:,.2f} | {iva_str} | TOTAL: EUR {out['totale']:,.2f}")
        print("DRAFT — verify with accountant")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
