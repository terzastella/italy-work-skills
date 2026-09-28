# Oracle: ritenuta-acconto (hand-computed, 2026-09-28)

Case: standard (non-forfettario) professional fee, lordo 2000, 20%.

Hand derivation: ritenuta = 2000 × 0.20 = 400.00, netto = 1600.00.

```json oracle-input
{"lordo": 2000}
```

```json oracle-expected
{"direzione": "lordo->netto", "lordo": 2000, "aliquota_pct": 20, "ritenuta": 400.0, "netto": 1600.0}
```
