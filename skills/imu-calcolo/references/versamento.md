# IMU payment notes (imu-calcolo)

## Instalments

June 16 advance + December 16 balance (verify year — dates move rarely but check).
Acconto = half rounded, saldo = remainder (see script `rate()`).

## F24

Property taxes via F24, codes per property type noted on the form.
Keep quietanze: they are the proof of payment.

## Late payment

Ravvedimento paths apply (see `ravvedimento-operoso`): band % + daily interest.
Each day costs — pay now, compute exact with the band inputs.

## Mid-year changes

Sold → conguaglio between paid acconto and recomputed due, stated explicitly.
Rate changed → full recompute with the new delibera, never a silent average.
