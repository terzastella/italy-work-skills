# Profile calendars (scadenze-fiscali) — patterns, years always attached

These are STRUCTURES with 2026 examples. Every date below is an example for
its year — verify on agenziaentrate.gov.it before paying, every year.

## Forfettario (imposta sostitutiva)

- Saldo prior year + 1st advance: same summer date (e.g. 20/07/2026 per DL 89/2026,
  no surcharge) → late option +30 days +0.80% (e.g. 20/08).
- Split per current AdE rules (see `acconti-calcolo`) — stated, not assumed.
- Chain: `regime-forfettario` (5.820 pattern) → `acconti-calcolo` (split) → here (dates).

## Ordinary (IRPEF)

- Saldo + 1st acconto (40%) summer → 2nd acconto (60%) late autumn.
- Dates + surcharge windows year-stated; ravvedimento on miss (see `ravvedimento-operoso`).

## Employee-only

- No advances. CU (spring) → 730 precompilata → conguaglio in payslip.
- Different calendar entirely: route to `cu-730-guida`, never merge with business dates.

## IMU (separate track, see `imu-calcolo`)

- June 16 advance + December 16 balance. Never merged into income-tax rows.

## Reading a calendar row

`date | who | what | surcharge? | source` — source = decree number + AdE notice
date. A row without source is a rumor, not a deadline.
