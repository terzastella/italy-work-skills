# verbale-riunione-it cases

## Good: project sync

Input raw notes: "Marco finishes API by Friday, Anna tests, next sync Monday" [sample data].

Output: minutes with decisions (API scope frozen) + actions
(Marco — API done — 26/09/2026; Anna — tests — 29/09/2026)
+ English recap: `API frozen; 2 actions with dates; next 29/09.`

## Bad: ownerless actions

Input: notes with tasks but no owners [sample data].

Output: `Every action gets owner + date — ownerless actions refused as output. Asked back, never assigned silently.`
