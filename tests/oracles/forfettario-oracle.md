# Oracle: regime-forfettario (hand-computed, 2026-09-28)

Case: fatturato 50000, coeff 0.78, contributi 5000, aliquota 5%.

Hand derivation:
- reddito = 50000 × 0.78 = 39000.00
- base = 39000 − 5000 = 34000.00
- imposta 5% = 34000 × 0.05 = 1700.00

```json oracle-input
{"fatturato": 50000, "coeff": 0.78, "contributi": 5000, "aliquota": 5, "year": 2026}
```

```json oracle-expected
{"reddito": 39000.0, "base_imponibile": 34000.0, "imposta_5pct": 1700.0}
```
