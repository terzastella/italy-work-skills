# IMU payment notes (imu-calcolo)

last-verified: 2026-09-28

## Instalments

June 16 advance + December 16 balance (verify year â€” dates move rarely but check).
Acconto = half rounded, saldo = remainder (see script `rate()`).

## F24

Property taxes via F24, codes per property type noted on the form.
Keep quietanze: they are the proof of payment.

## Late payment

Ravvedimento paths apply (see `ravvedimento-operoso`): band % + daily interest.
Each day costs â€” pay now, compute exact with the band inputs.

## Mid-year changes

Sold â†’ conguaglio between paid acconto and recomputed due, stated explicitly.
Rate changed â†’ full recompute with the new delibera, never a silent average.
