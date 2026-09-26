# canone-rai cases

## Good: over-75 exemption

Input: 78 years old, pension under limit [sample data].

Output: exemption path (declaration to AdE by deadline, year-stated limit) +
`verify current income limit — it moves.` No fee computed as owed.

## Bad: limit assumed

Input: "tanto sono over 75, non pago" with income unknown [sample data].

Output: `Age alone is not enough — income limit year-stated + declaration by deadline, or the fee stands.`
