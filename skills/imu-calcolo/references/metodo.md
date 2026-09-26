# IMU method (imu-calcolo)

## Base

`base = rendita × 1.05 (rivalutazione) × moltiplicatore di categoria`.
Multiplier comes from the national table for the tax year — see `tabelle.md`.
Never invent it: ask for categoria (e.g. A/2) and look it up.

## Tax

`imposta annua = base × aliquota comunale − detrazioni`.
Aliquota is per-mille from the comune delibera for the year (e.g. 10.6).
Luxury main homes (A/1, A/8, A/9): 200€ annual deduction (year-stated).

## Possession

`dovuta = annua × mesi/12`. Month counts if possession ≥ 15 days (verify yearly).
Split already-paid acconto vs ricalcolato as conguaglio, stated explicitly.

## Payment

June 16 advance + December 16 balance via F24 (codes per property type noted
on the form). Late payment: ravvedimento paths (see `ravvedimento-operoso`).

## Close

Every answer ends with: rate verified on comune delibera YEAR + accountant/comune
check. Rates are municipal — this skill bundles none.
