# How to read AdE deadline notices (scadenze-fiscali)

last-verified: 2026-09-28

1. Who it covers (forfettari? ISA? companies?) — DL 89/2026 style extensions list categories.
2. What moves: saldo vs acconto, which year, with/without 0.40% or 0.80% surcharge.
3. New date + 30-day surcharge window (e.g. 2026: 20 July plain, 20 August +0.80%).
4. Source: decree number + AdE notice date. Never trust forwarded screenshots alone.
5. Calendar entry format: `date | who | what | surcharge? | source`.

## Worked chain (forfettario 2026, sample data)

Prior-year sostitutiva due 5.820€ (return line cited) → saldo by 20/07/2026 (DL 89/2026,
no surcharge) + 1st advance 50% historic same date (split per current rules, see
`acconti-calcolo`) → late option +30 days with +0.80% by 20/08 → VERIFY on
agenziaentrate.gov.it before paying. Amounts chain: `regime-forfettario` computes
the 5.820, `acconti-calcolo` splits it, this skill dates it — one figure, three skills.

## Anti-patterns

- Timeless deadlines ("si paga a giugno") → always refuse, ask the year.
- Extension assumed from social media → decree number or it didn't happen.
- Employee profile given business calendar → route to CU/730 path instead.
