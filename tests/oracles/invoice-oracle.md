# Oracle: invoice-it (hand-computed, 2026-09-28)

Case: 10h consulting × 50 euro, VAT 22% (reuses `examples/items-610.json`).

Hand derivation:
- imponibile = 10 × 50 = 500.00
- IVA 22% = 500 × 0.22 = 110.00
- totale = 610.00

```json oracle-input
"examples/items-610.json"
```

```json oracle-expected
{"imponibile": 500.0, "iva_per_aliquota": {"22.0": 110.0}, "totale": 610.0}
```
