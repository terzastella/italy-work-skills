# busta-paga-leggi cases

## Good: standard month check (script)

Input: base €1.800 + straordinari €150, INPS €175,50, IRPEF €280, detrazioni €125,50, netto €1.620 [sample data].

Run: `python skills/busta-paga-leggi/scripts/payslip_check.py --lordo 1950 --inps 175.5 --irpef 280 --detrazioni 125.5 --netto 1620`

Output: line walk + `net recomputed €1.620 = match` + `TFR accruing separately` + `cross-check with CU at year end.`

## Good: mismatch as question

Input: same lines, stated net €1.600 [sample data].

Output: recomputed €1.620 vs stated €1.600 → `€20 gap: ask payroll, possible conguaglio — not an accusation.`

## Good: part-time proportional

Input: 50% part-time, lordo €975, INPS €87,75, IRPEF €120, detrazioni €60, netto €827,25 [sample data].

Output: match. `Proportional checks flagged for part-time — verified here.`

## Bad: fraud claim

Input: any gap found [sample data].

Output: never "they steal". `Anomalies phrased as checks ("verify with payroll"), never fraud claims.`
