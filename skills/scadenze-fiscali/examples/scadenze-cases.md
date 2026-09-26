# scadenze-fiscali cases

## Good: forfettario 2026 payments (method)

Input: 2025 balance due 5.820€ (from return), profile forfettario.

Output:
```text
Saldo 2025: 5.820 by 20/07/2026 (DL 89/2026, no surcharge)
1st advance 2026: 50% historic (LM42 line) same date
Late option: +30 days with +0.80% (by 20/08)
VERIFY on agenziaentrate.gov.it before paying — extensions move.
```

## Good: employee profile routed

Input: employee, no business income [sample data].

Output: CU → 730 path, different calendar, no advance payments. `Ask profile first — wrong calendar is worse than none.`

## Bad: timeless deadline

Input: "quando si paga il saldo?" with no year [sample data].

Output: no date. `Never state a deadline without year — ask year + profile first.`

## Bad: screenshot extension

Input: forwarded message "proroga al 30/09!!!" [sample data].

Output: `Decree number + AdE notice date, or it didn't happen. Never trust forwarded screenshots alone.`
