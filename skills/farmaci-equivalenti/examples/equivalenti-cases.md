# farmaci-equivalenti cases

## Good: brand prescribed, generic offered

Input: brand on prescription [sample data].

Output: equivalence check + substitution rule + `doctor's non-substitution respected,
never bypassed. Ticket math included.`

## Bad: bypass non-substitution

Input: "tanto prendo il generico lo stesso" against doctor's note [sample data].

Output: `Doctor's non-substitution respected, never bypassed — pharmacist route explained, ticket math included.`
