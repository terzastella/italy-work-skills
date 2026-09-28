# Oracle: tredicesima-info (hand-computed, 2026-09-28)

Case: retribuzione 2000, 6 mesi.
Hand: rateo = 2000/12 = 166.67, maturato = 166.67 × 6 = 1000.00
(1000.02 with unrounded rateo — oracle expects the rounded convention).

```json oracle-input
{"retribuzione": 2000, "mesi": 6}
```

```json oracle-expected
{"rateo_mensile": 166.67, "maturato": 1000.0}
```
