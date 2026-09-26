# spese-mediche-detrazioni cases

## Good: pharmacy year total (script)

Input: €900 parlante receipts, fiscal code present [sample data].

Run: `python skills/spese-mediche-detrazioni/scripts/detrai19.py --spese 900 --franchigia 129.11 --year 2026`

Output: base €770,89 → 19% = €146,47 + `tracciabilità check (year-stated rules) + declaration line pointer.`

## Bad: estimates instead of receipts

Input: "circa 900 euro di farmacia, senza scontrini" [sample data].

Output: no math. `Lost receipts → pharmacy ristampa path, not estimates. Papers first, math after.`
