# utenze-voltura cases

## Good: new rental, active supply

Input: Milan rental, light on, prior tenant left [sample data].

Output: voltura path + documents + timing + `prior debts stay with prior holder —
verify POD has no morosità flag before filing.`

## Bad: prior debts accepted

Input: "mi accollo i debiti del vecchio inquilino per fare prima" [sample data].

Output: `Prior debts stay with prior holder — never accept them to speed up. Verify first, file after.`
