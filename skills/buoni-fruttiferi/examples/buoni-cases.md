# buoni-fruttiferi cases

## Good: €10k parked (script)

Input: ordinary series, 2,5% gross, duty €10 (2026, given) [sample data].

Run: `python skills/buoni-fruttiferi/scripts/bpf.py --capitale 10000 --lordo 2.5 --bollo 10 --year 2026`

Output: netto €208,75 + early-exit rules +
`type identified first — old series differ. No endorsements.`

## Bad: series skipped

Input: "ho dei buoni vecchi, quanto rendono?" with no series [sample data].

Output: no number. `Series first — old series differ too much to guess. Identify, then compute.`
