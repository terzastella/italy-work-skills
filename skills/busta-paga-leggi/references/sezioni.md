# Section walk (busta-paga-leggi)

Read top to bottom. For each: what it is → source of the figure → what to compare.

## Testata

Employer, employee (redacted), month/year, CCNL + level, hire date, INPS position.
Check: CCNL + level drive every number below — lock them first.

## Competenze (gross side)

Paga base (CCNL minimum for the level) · contingenza/EDR (fixed element) ·
superminimo (individual/company) · straordinari (hours × rate, see `straordinari-info`) ·
premi/una tantum · 13a/14a ratei where paid monthly · ferie/permessi balances (days, not money).
Check: base vs CCNL minimum (see `contratto-base-check`); overtime vs authorizations.

## Trattenute (withholding side)

INPS worker share (as stated, ~9% typical — verify CCNL) · IRPEF (as stated;
cross-check magnitude with `irpef-scaglioni` slices, never recompute brackets here) ·
detrazioni lavoro dipendente + carichi (as stated) · addizionali where present.
Check: INPS ≈ 9% of imponibile (rough); IRPEF plausible for the bracket.

## Netto + footer

Netto = competenze − trattenute (+ detrazioni). TFR accrual (separate line,
see `tfr-fondo`). Ferie/permessi residui (days). TFR + fondo choice note yearly.
Close: CU cross-check tip (year-end totals must reconcile).
