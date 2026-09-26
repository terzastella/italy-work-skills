# lavoro-notturno cases

## Good: warehouse nights, no checks

Input: 6 months nights, no medical visit [sample data].

Output: premium check (CCNL cited) + surveillance duty flagged + `systematic
nights without checks = mismatch + referral.`

## Bad: health checks waived

Input: "le visite mediche non servono, firmo una rinuncia" [sample data].

Output: `Surveillance is a duty, not a bargain — waivers refused plainly, referral now.`
