# Advance method table (acconti-calcolo)

last-verified: 2026-09-28

- Base: prior-year due tax (return line, e.g. LM42 for forfettari). Previsionale:
  current-year estimate instead — allowed, but underpayment penalties apply.
- Threshold: no advance if ≤52€ (verify year).
- Split: explicit input to the script (`--split 100` or `--split 40,60`).
  Current AdE rules per tax decide it — IRPEF-style instalments vs single
  sostitutiva advance. Do not assert from memory; rules changed in the past.
- First year: usually no advance (no history to base it on).
- Mixed incomes: per-tax advances, never merged.
- Dates live in `scadenze-fiscali`; compensation of overpaid advances in `compensazioni-f24`.
