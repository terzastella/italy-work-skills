# IMU method (imu-calcolo)

last-verified: 2026-09-28

## Base

`base = rendita Ã— 1.05 (rivalutazione) Ã— moltiplicatore di categoria`.
Multiplier comes from the national table for the tax year â€” see `tabelle.md`.
Never invent it: ask for categoria (e.g. A/2) and look it up.

## Tax

`imposta annua = base Ã— aliquota comunale âˆ’ detrazioni`.
Aliquota is per-mille from the comune delibera for the year (e.g. 10.6).
Luxury main homes (A/1, A/8, A/9): 200â‚¬ annual deduction (year-stated).

## Possession

`dovuta = annua Ã— mesi/12`. Month counts if possession â‰¥ 15 days (verify yearly).
Split already-paid acconto vs ricalcolato as conguaglio, stated explicitly.

## Payment

June 16 advance + December 16 balance via F24 (codes per property type noted
on the form). Late payment: ravvedimento paths (see `ravvedimento-operoso`).

## Close

Every answer ends with: rate verified on comune delibera YEAR + accountant/comune
check. Rates are municipal â€” this skill bundles none.
