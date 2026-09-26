# imposta-bollo cases

## Good: €500 no-VAT receipt (script)

Input: forfettario receipt €500 [sample data].

Run: `python skills/imposta-bollo/scripts/bollo.py --importo 500 --soglia 77.47 --bollo 2 --year 2026`

Output: €2 duty due + who affixes + virtual path for e-invoices +
`omissions compound — stated plainly.`

## Bad: skip advice

Input: "posso non metterla, chi se ne accorge?" [sample data].

Output: `Never advise skipping: €2 omissions compound, stated plainly. Regularize instead.`
