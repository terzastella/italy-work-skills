# regime-forfettario cases

## Good: startup 5% math (script)

Input: 2025 fees 60.000€, coefficient 78%, social contributions 8.000€ [sample data].

Run: `python skills/regime-forfettario/scripts/forfettario.py --fatturato 60000 --coeff 0.78 --contributi 8000 --aliquota 15 --year 2026`

Output:
```text
Taxable: 60.000 × 0.78 = 46.800 − 8.000 = 38.800
Tax 15%: 5.820 (5% startup if gates met: 1.940)
Gates: revenue ok · costs unknown [TODO] · employee income unknown [TODO]
Likely eligible IF all gates pass — accountant confirms.
```

## Good: near 100k (blocked planning)

Input: 97.000€ by October [sample data].

Run: same script with `--soglia-check 97000 --year 2026`

Output: stay forfait till 31/12, no VAT this year, ordinary from 1/1 + daily monitoring warning for the 100k line.

## Bad: eligibility verdict

Input: "posso entrare nel forfettario?" with revenue only [sample data].

Output: no verdict. `Gates checklist in references/requisiti.md — one unchecked gate stops the call. Accountant decides.`
