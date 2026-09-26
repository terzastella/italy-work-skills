# collaborazioni-occasionali cases

## Good: designer side gigs (script)

Input: 3 invoices to 3 clients, €4.000 total [sample data].

Run: `python skills/collaborazioni-occasionali/scripts/occasionali.py --lordo 4000 --ritenuta 20 --franchigia-inps 5000 --year 2026`

Output: ritenuta €800 → netto €3.200, INPS sotto franchigia + occasional OK verdict + ricevuta path +
`if it becomes monthly with one client → VAT track (see partita-iva-apri).`

## Bad: habitual disguised

Input: monthly invoices to the same single client [sample data].

Output: `Habitual = VAT needed even under 5.000€: the key test, stated first. No blanket occasional cover.`
