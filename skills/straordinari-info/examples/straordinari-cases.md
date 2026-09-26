# straordinari-info cases

## Good: 20 extra hours month (script)

Input: metalmeccanico, 20h overtime, €12/h, 25% premium (CCNL cited) [sample data].

Run: `python skills/straordinari-info/scripts/straord.py --ore 20 --paga-oraria 12 --maggiorazione 25`

Output: base €240 + premium €60 = €300 + cap check (year-stated) + banca ore option +
`unpaid systematics flagged + referral. No generic percentages as law.`

## Bad: generic premium

Input: "quanto mi pagano gli straordinari?" with no CCNL [sample data].

Output: no figure. `Premiums only with CCNL cited; never generic percentages as law — contract first.`
