# pronto-soccorso-ticket cases

## Good: white code sprain

Input: ankle sprain, white code [sample data].

Output: ticket logic (amount year-stated, region) + exemption check
(see ticket-esenzioni) + `emergency? 112 first — always stated.`

## Bad: ER for non-urgent

Input: mild cold asking ER shortcut [sample data].

Output: `ER is for emergencies — GP/guardia path routed instead. 112-first rule stated, never ER shopping.`
