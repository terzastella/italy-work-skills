# irpef-scaglioni cases

## Good: €35k employee (2025 table)

Input: €35.000 gross, 2025 [sample data].

Run: `python skills/irpef-scaglioni/scripts/irpef.py --reddito 35000 --scaglioni skills/irpef-scaglioni/examples/scaglioni-2025.json --year 2025`

Output:
```text
Slice 0-28000: 28000 x 23% = 6440.00
Slice 28000-50000: 7000 x 25% = 1750.00
Tax: 8190.00 | average 23.4% | marginal 25% (year 2025)
```

## Good: the fear killed with numbers

Input: "if I earn €51.000 instead of €49.000, do I lose money?" [sample data].

Output: run both figures. €49.000 → €11.690. €51.000 → €12.370 (only €1.000
at 43% = €430 extra). Net rises €1.570. `Only the slice above pays more — proved, not asserted.`

## Bad: timeless table

Input: "calcola IRPEF su €40.000" with no year [sample data].

Output: no number. Ask the year first, load that year's table, verify live.
`Never reuse last year's table silently.`

## Bad: forfettario mixed in

Input: forfettario asking for scaglioni math [sample data].

Output: stop. `Different world — see regime-forfettario. Slices do not apply.`
