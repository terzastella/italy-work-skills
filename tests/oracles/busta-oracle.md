# Oracle: busta-paga-leggi (hand-computed, 2026-09-28)

Case: lordo 1950, inps 180, irpef 120, detrazioni 30, stated netto 1620.

Hand derivation:
- ricalcolato = 1950 − 180 − 120 + 30 = 1680.00
- gap = 1680 − 1620 = +60.00 → over tolerance → ask payroll

```json oracle-input
{"lordo": 1950, "inps": 180, "irpef": 120, "detrazioni": 30, "netto": 1620}
```

```json oracle-expected
{"netto_ricalcolato": 1680.0, "gap": 60.0, "esito": "gap: ask payroll (possible conguaglio - not an accusation)"}
```
