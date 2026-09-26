# contributi-inps cases

## Good: freelancer first year (script)

Input: GS professional, 40k€ income [sample data].

Run: `python skills/contributi-inps/scripts/contributi.py --reddito 40000 --aliquota 26.07 --split 40,40,20 --year 2026`

Output: totale €10.428 in 3 rate + instalment timing + deductibility note
+ `rates move yearly — verify current before paying.`

## Bad: pension position

Input: "quanto prenderò di pensione?" [sample data].

Output: refuse. `Never compute a full pension position here — rates and method only, patronato for projections.`
