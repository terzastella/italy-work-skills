# conti-deposito cases

## Good: €30k parked (script)

Input: €30.000 for 1 year, 3,0% gross, duty €34,20 (2026, given) [sample data].

Run: `python skills/conti-deposito/scripts/deposito.py --capitale 30000 --lordo 3.0 --bollo 34.2 --year 2026`

Output: netto €631,80 + promo-duration check + FITD note +
`net as verdict number, never gross. No endorsement.`

## Bad: gross comparison

Input: "3% contro 2,8%, vinco col 3?" [sample data].

Output: no verdict on gross. `Net after 26% + duty decides — recompute both, then compare.`
