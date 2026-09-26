# ferie-permessi cases

## Good: summer balance check (script)

Input: full-time, 26 days entitlement (CCNL cited), 10 days used by July [sample data].

Run: `python skills/ferie-permessi/scripts/ratei.py --spettanza 26 --mese 7 --fruiti 10`

Output: rateo 2,17/mese + maturato 15,17 − fruiti 10 = residuo 5,17 + fruition deadlines (year-stated) + request steps.
`Day counts only with CCNL cited — never generic.`

## Good: part-time pro-rata

Input: 50% part-time, same entitlement, June, nothing taken [sample data].

Run: same script with `--spettanza 26 --part-time 50 --mese 6`

Output: maturato 6,5 = residuo 6,5. `Pro-rata applied before accrual, stated explicitly.`

## Bad: generic entitlement

Input: "quante ferie ho?" with no CCNL [sample data].

Output: no number. `Entitlement is a CCNL-cited input — ask first, compute after.`
