# acconti-calcolo cases

## Good: forfettario second year

Input: prior-year sostitutiva due 5.820€, split 100 (2026 rules checked) [sample data].

Run: `python skills/acconti-calcolo/scripts/acconti.py --imposta 5820 --split 100 --year 2026`

Output:
```text
Base (storico): 5820.00 | split 100 (2026)
Rata 1: 5820.00
Split per current AdE rules — stated explicitly, not assumed. Dates: see scadenze-fiscali.
```

## Good: IRPEF two instalments

Input: prior-year IRPEF due €11.690, split 40/60 [sample data].

Run: same script with `--imposta 11690 --split 40,60 --year 2025`

Output: Rata 1: 4676.00, Rata 2: 7014.00.

## Good: below threshold

Input: prior-year due €40 [sample data].

Output: base ≤ soglia → no advance due. Nothing to split, stated plainly.

## Bad: split from memory

Input: "acconto forfettario, fai 50/50" without checking rules [sample data].

Output: stop. `Split is an input, not a guess — check AdE for the year first.`
The script enforces this: `--split` is required.

## Bad: previsional recommended blindly

Input: "pago meno con il previsionale, vero?" [sample data].

Output: both maths shown + penalty warning. `Never recommend blindly — professional check required.`
