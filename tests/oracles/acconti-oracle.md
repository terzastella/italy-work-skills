# Oracle: acconti-calcolo (hand-computed, 2026-09-28)

Case: prior-year imposta 10000, historic split 100 (single payment).

Hand derivation: base = 10000, dovuto = true, rate = [10000.00].

```json oracle-input
{"imposta": 10000, "split": "100", "year": 2026}
```

```json oracle-expected
{"metodo": "storico", "base": 10000, "acconto_dovuto": true, "rate": [10000.0]}
```
