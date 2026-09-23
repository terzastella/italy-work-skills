# invoice-it cases

## Simple 22% invoice

Input: given client, 1 item consulting 10h × €50.

Verification:
```text
Item 1: consulting — 10 x €50 = €500
Taxable: €500 | VAT 22%: €110 | TOTAL: €610
Missing data: none
DRAFT — verify with accountant
```

## Missing data

Input: items only, no client VAT ID.

Output: draft with `Client VAT ID: [TODO]`, totals computed anyway,
no invented VAT ID.
