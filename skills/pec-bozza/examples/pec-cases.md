# pec-bozza cases

## Good: unpaid invoice via PEC

Input: invoice 12/2026, €610, 45 days overdue, recipient PEC given [sample data].

Output: Italian draft (formal `Lei`, facts, 7-day request) + English tone summary
+ checklist: attachments named, receipts to keep, `send from PEC to PEC`.
+ Note: `Draft only — I did not send anything.`

## Good: no sender mailbox (blocked)

Input: user has no PEC, wants to send one [sample data].

Output: no draft. `Get an AgID-listed PEC mailbox first — ordinary email has no certified value.`

## Bad: invented PEC address

Input: recipient name only, no PEC address [sample data].

Output: draft with `To: [TODO — PEC address]` + stop. `Never invent PEC addresses.`
