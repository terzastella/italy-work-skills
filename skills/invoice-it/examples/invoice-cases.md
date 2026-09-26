# invoice-it cases

## Good: simple 22% invoice (script)

Input: given client, 1 item consulting 10h × €50.

Run: `python skills/invoice-it/scripts/totals.py --items skills/invoice-it/examples/items-610.json`

Verification:
```text
Item 1: consulting — 10 x €50 = €500
Taxable: €500 | VAT 22%: €110 | TOTAL: €610
Missing data: none
DRAFT — verify with accountant
```

## Good: mixed rates

Input: servizio A 2×€100 @22% + servizio B 1×€200 @10% [sample data].

Run: same script with `examples/items-miste.json`

Output: Taxable €400 | VAT 22% €44 | VAT 10% €20 | TOTAL €464.

## Bad: missing data invented

Input: items only, no client VAT ID.

Output: draft with `Client VAT ID: [TODO]`, totals computed anyway,
no invented VAT ID. `Never invent VAT IDs, tax codes, existing invoice numbers.`
