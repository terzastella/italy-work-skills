# ritenuta-acconto cases

## Good: ordinary lordo to netto (script)

Input: professional invoice €1.000 gross, ordinary regime, 20% [sample data].

Run: `python skills/ritenuta-acconto/scripts/ritenuta.py --lordo 1000 --aliquota 20`

Output: ritenuta €200 → netto €800. `Direction stated: lordo→netto. Certified yearly in CU.`

## Good: netto to lordo (script)

Input: agreed net €800, ordinary, 20% [sample data].

Output: lordo €1.000, ritenuta €200. `Direction stated: netto→lordo.`

## Good: forfettario invoice to company

Input: forfettario dev invoices €2.000 to SRL [sample data].

Run: same script with `--lordo 2000 --forfettario`

Output: no withholding — invoice carries the exemption statement; company pays gross.
Reminder: statement text on every invoice.

## Good: year-end regime change

Output: December ordinary invoice paid in January as forfettario →
withholding applies (invoice-regime governs), usable against prior-year IRPEF.

## Bad: direction unstated

Input: "con 1000 euro quanto mi resta?" [sample data].

Output: no number first. `Never compute net/gross without stating which direction — ask lordo-or-netto, then compute.`

## Bad: treaty rate improvised

Input: Swiss client, "which withholding?" [sample data].

Output: `Cross-border: flag, do not improvise treaty rates — specialist check required.`
