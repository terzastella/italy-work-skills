# Oracle: plusvalenza-casa (hand-computed, 2026-09-28)

Case: bought 2022, sold 2026 (4 years ≤ 5 → taxable), gain 50000,
26% substitute tax.

Hand derivation: anni = 4, imponibile = true, 50000 × 0.26 = 13000.00.

```json oracle-input
{"acquisto": 2022, "vendita": 2026, "gain": 50000, "sostitutiva": 26, "year": 2026}
```

```json oracle-expected
{"anni_possesso": 4, "imponibile": true, "sostitutiva": 13000.0}
```
