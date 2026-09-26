# Payslip lines (busta-paga-leggi)

Gross side: paga base (CCNL level cited) · contingenza/EDR · superminimo ·
straordinari (hours × rate) · premi · una tantum.
Withholding side: INPS worker share (as stated, ~9% typical — verify CCNL) ·
IRPEF + detrazioni lavoro dipendente (as stated) · addizionali where present.
Result: netto + TFR accrual (separate line, not in net) + ferie/permessi balances.
13a/14a: separate months with their own accrual logic. Arretrati: tassazione
separata section, never merged with ordinary.
Verification: feed stated lines to `scripts/payslip_check.py`; gap > €1 (rounding
tolerance) → question for payroll. Anomalies = checks, never fraud claims.
Privacy first: redact name/fiscal code before sharing anything.
