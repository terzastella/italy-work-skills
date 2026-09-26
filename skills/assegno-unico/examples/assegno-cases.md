# assegno-unico cases

## Good: two kids, ISEE 25k (script)

Input: 2 minors, ISEE 25.000€ [sample data].

Run: `python skills/assegno-unico/scripts/fasce.py --isee 25000 --minori 2 --tabella skills/assegno-unico/examples/importi-2025.json --year 2025`

Output: band €150/minore → €300/mese + apply path (INPS/patronato, DSU link) + `verify current circular — tables move yearly.`

## Bad: timeless amount

Input: "quanto prendo?" with no year [sample data].

Output: no number. `Amounts with year; tables move — verify current INPS circular first.`

## Bad: no-DSU skipped

Input: household without DSU asking for the max [sample data].

Output: `No-DSU = minimum: state it (the classic loss).` Apply path via `isee-guida` first.
