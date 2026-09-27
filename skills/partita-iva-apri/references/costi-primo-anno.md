# First-year costs preview (partita-iva-apri)

Patterns with user figures only — never price lists as law. Amounts year-stated.

## Freelance forfettario sketch (60k pattern)

- Tax: `forfettario.py --fatturato 60000 --coeff 0.78 --contributi 8000 --year 2026` → 5.820.
- Contributions: `contributi.py --reddito 46800 --aliquota 26.07 --year 2026` → GS math.
- Advances: `acconti.py` split on the sostitutiva (see `acconti-calcolo`).
- Total first-year cash need = tax + contributions + advances + accountant fee.
  Show the sum, call it a sketch, accountant confirms.

## Artigiano/commerciante sketch

- Minimal fixed (year-stated) + percentage over minimal — both explicit inputs.
- Chamber (diritto camerale) yearly, year-stated.
- Same close: sketch, not promise.

## What never goes here

No regime verdicts, no filing steps executed, no "you will pay X" promises.
The preview exists to prevent surprise #1 of new freelancers: contributions
from month one.
