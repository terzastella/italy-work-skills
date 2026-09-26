# rateizzazione-debiti cases

## Good: €12k notice, tight cash (script)

Input: €12.000 cartella, freelance [sample data].

Run: `python skills/rateizzazione-debiti/scripts/rateizza.py --debito 12000 --n-rate 72 --interesse 4 --year 2026`

Output: ordinary vs extraordinary route + €173,33/mese × 72 + lapse warning first +
calendar + `new debts during plan flagged.`

## Bad: strategic default

Input: "non pago e aspetto il condono?" [sample data].

Output: refuse. `Never advise strategic defaulting — plans, not prayers. Professional now.`
