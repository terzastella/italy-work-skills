# imu-calcolo cases

## Good: second home with given rate

Input: rendita €850, cat A/2, comune rate 1.06% (10.6 per mille, 2026, given) [sample data].

Run: `python skills/imu-calcolo/scripts/imu.py --rendita 850 --moltiplicatore 160 --aliquota-per-mille 10.6 --year 2026`

Output:
```text
Base: 850 × 1.05 = 892,50 × 160 = €142.800
Tax: 142.800 × 1,06% = €1.513,68 → June €756,84 + December €756,84 (F24)
Verify rate on comune delibera 2026 before paying.
```

## Good: luxury main home with deduction

Input: rendita €1.200, cat A/1, rate 10.6 per mille, 200€ deduction, 2026 [sample data].

Run: same script with `--rendita 1200 --detrazione 200 --year 2026`

Output: base €201.600 → tax €1.936,96 → June €968,48 + December €968,48 (F24).

## Good: mid-year sale (7 months)

Input: same as first case, sold end of July (7 months possession) [sample data].

Run: same script with `--mesi 7`

Output: dovuta €882,98 → June €441,49 + December €441,49. Acconto already paid: conguaglio math stated.

## Bad: rate from memory

Input: "seconda casa a Milano, quanto pago?" without rendita/categoria/rate [sample data].

Output: no number. Ask for rendita + categoria + comune + year rate first.
`Never compute from thin air: rendita + categoria + comune required.`

## Bad: main home assumed taxable

Input: "pago IMU sulla prima casa?" (non-luxury) [sample data].

Output: exempt — stated plainly, with the A/1-A/8-A/9 exception flagged.
