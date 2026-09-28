# Oracle: mutuo-tassi (hand-computed, 2026-09-28)

Independent French-amortization implementation:
rata = P·r·(1+r)^n / ((1+r)^n − 1), r = annual/12, n = years·12,
rounded to cents; totale = rata × n.

Case: capitale 150000, 25 anni, offerta A TAEG 4.0, offerta B TAN 3.5,
shock B +2.0 → 5.5.

Hand derivation (rounded):
- A: r=0.003333, n=300 → rata 791.76, totale 237528.00
- B: r=0.002917, n=300 → rata 750.94, totale 225282.00
- shock: r=0.004583, n=300 → rata 921.13, totale 276339.00

```json oracle-input
{"capitale": 150000, "anni": 25, "taeg-a": 4.0, "tan-b": 3.5, "shock": 2.0}
```

```json oracle-expected
{"rata_a": 791.76, "totale_a": 237528.0, "rata_b": 750.94, "totale_b": 225282.0, "rata_b_shock": 921.13, "totale_b_shock": 276339.0}
```
