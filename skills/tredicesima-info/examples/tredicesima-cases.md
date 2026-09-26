# tredicesima-info cases

## Good: mid-year hire (script)

Input: hired in May, monthly base €1.800 (CCNL items cited) [sample data].

Run: `python skills/tredicesima-info/scripts/tredicesima.py --retribuzione 1800 --mesi 8`

Output: 8/12 → rateo €150/mese, maturato €1.200 + advance note + `CCNL items cited — never generic lists as law.`

## Good: part-time pro-rata

Input: 50% part-time, full year [sample data].

Output: rateo €75/mese → €900. `Part-time math shown plainly.`

## Bad: generic pay items

Input: "quanto mi spetta?" with no CCNL [sample data].

Output: no figure. `Items included vary by CCNL: cite the contract first, compute after.`
