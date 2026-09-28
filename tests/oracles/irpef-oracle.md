# Oracle: irpef-scaglioni (hand-computed, 2026-09-28)

Verifies the calculator implements the SKILL's dated table
(`examples/scaglioni-2025.json`: 23% to 28k, 25% to 50k, 43% above).
Whether that table matches live law is the freshness domain, not this file.

Case: reddito 35000, year 2025.

Hand derivation:
- slice 1: 28000 × 0.23 = 6440.00
- slice 2: (35000 − 28000) × 0.25 = 7000 × 0.25 = 1750.00
- imposta = 6440 + 1750 = 8190.00
- media = 8190/35000 = 23.40%, marginale = 25%

```json oracle-input
{"reddito": 35000, "scaglioni": "examples/scaglioni-2025.json", "year": 2025}
```

```json oracle-expected
{"imposta": 8190.0, "aliquota_media_pct": 23.4, "aliquota_marginale_pct": 25.0}
```
