# assicurazione-casa cases

## Good: post-burglary claim

Input: burglary, police report filed [sample data].

Output: claim steps (prompt notice + photos + list) + policy deductibles check +
`denied? read motivo + IVASS path mentioned.`

## Bad: late notice

Input: "denuncio tra qualche mese" [sample data].

Output: `Prompt notice is the duty — late claims risk denial. Photos + list now, motivo read if refused.`
