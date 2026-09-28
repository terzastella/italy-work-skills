# Oracle: imu-calcolo (hand-computed, 2026-09-28)

Independent of `examples/fixtures/`: values derived by hand below, then
checked against the calculator. Catches formula+fixture both-wrong.

Case: seconda casa, rendita 850, categoria A/2 (moltiplicatore 160),
aliquota 10.6 per mille, full year, no detrazione.

Hand derivation:
- rivalutazione 5%: 850 × 1.05 = 892.50
- base: 892.50 × 160 = 142800.00
- imposta annua: 142800 × 10.6/1000 = 142800 × 0.0106 = 1513.68
- acconto giugno = saldo dicembre = 1513.68 / 2 = 756.84

```json oracle-input
{"rendita": 850, "moltiplicatore": 160, "aliquota-per-mille": 10.6, "detrazione": 0, "mesi": 12, "year": 2026}
```

```json oracle-expected
{"base_imponibile": 142800.0, "imposta_dovuta": 1513.68, "acconto_giugno": 756.84, "saldo_dicembre": 756.84}
```
