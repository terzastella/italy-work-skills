# Oracle: cedolare-secca (hand-computed, 2026-09-28)

Case: canone 24000, cedolare 21%, marginal IRPEF 43%.

Hand derivation:
- cedolare = 24000 × 0.21 = 5040.00
- irpef stimata = 24000 × 0.43 = 10320.00 → vince cedolare

```json oracle-input
{"canone": 24000, "cedolare": 21, "marginale": 43}
```

```json oracle-expected
{"costo_cedolare": 5040.0, "costo_irpef_stimato": 10320.0, "vince": "cedolare"}
```
