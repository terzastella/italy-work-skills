# Oracle: tfr-fondo (hand-computed, 2026-09-28)

Law formula: tasso = 1.5 + 0.75 × inflazione.
Case: accantonato 20000, inflazione 4.0 → tasso 4.50, 20000 × 0.045 = 900.00.

```json oracle-input
{"accantonato": 20000, "inflazione": 4.0, "year": 2026}
```

```json oracle-expected
{"tasso_pct": 4.5, "rivalutazione": 900.0}
```
