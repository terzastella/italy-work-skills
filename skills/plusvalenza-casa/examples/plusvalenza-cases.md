# plusvalenza-casa cases

## Good: second home sold year 3 (script)

Input: bought 2023, sold 2026, +€40k gain [sample data].

Run: `python skills/plusvalenza-casa/scripts/pluscasa.py --acquisto 2023 --vendita 2026 --gain 40000 --sostitutiva 26 --marginale 35 --year 2026`

Output: taxable (within 5y) + sostitutiva €10.400 vs IRPEF ~€14.000 (year-stated) +
`notary/commercialista computes final — method here, verdicts there.`

## Good: held 11 years (out)

Input: bought 2015, sold 2026 [sample data].

Output: generally OUT — no gain tax. `Clock first, math second.`

## Bad: donated property clock from donation

Input: donated 2024, selling 2026, "clock started at donation?" [sample data].

Output: `Donated property: 5-year clock from ORIGINAL purchase — stated (classic trap). Never restart the clock at donation.`
