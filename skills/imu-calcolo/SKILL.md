---
name: imu-calcolo
description: Explain IMU property tax with base and rate method. Use when asked IMU, property tax Italy, seconda casa tax.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.5", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[property data]"
user-invocable: true
disable-model-invocation: false
---

# IMU Calcolo

IMU without surprises: who pays, on what base, at which rate, when — with a
neutral calculator for the math. Flagship skill: deep method, dated tables,
verified fixtures, special cases mapped.

## When to use

- "IMU", "property tax Italy", "seconda casa", "quanto pago di IMU".
- Do not use for income taxes (see `irpef-scaglioni`), registration taxes,
  or TARI waste tax (see `tari-tassa`).

## Workflow (tappe with formal in/out)

### Tappa 1 — Qualify the property

Input: free-text description. Output: one of main-home / seconda-casa /
agricultural-land / buildable-area / pertinenza (+ category letter).
Main home (non-luxury) → exempt, stop here with the rule cited.
Land → agricultural vs edificabile fork (see `references/casi-particolari.md`).

### Tappa 2 — Collect inputs (never compute from thin air)

Required: rendita catastale, categoria, comune, tax year, months of possession.
Rate comes from the comune delibera for the year — ask the user for it or state
it as given, never from memory. Missing any item → ask, do not proceed with gaps.

### Tappa 3 — Run the math (script preferred, reproducible)

`python skills/imu-calcolo/scripts/imu.py --rendita 850 --moltiplicatore 160 --aliquota-per-mille 10.6 --year 2026`
Fallback by hand: rendita × 1.05 × multiplier → base; base × rate − deductions.
Multiplier from `references/tabelle.md` by categoria (never guessed).

### Tappa 4 — Output the statement

Base + annual tax + June advance + December balance (F24 codes noted)
+ "verify rate on comune delibera YEAR before paying" + accountant/comune check.

### Tappa 5 — Special cases sweep

Run the checklist in `references/casi-particolari.md` (inagibile, comodato,
terreni, pertinenze oltre una, ex-pat, comproprietà). Any hit → mapped path,
never silent.

## Multi-turn protocol

Turn 1 (qualify): one question max — "prima o seconda casa?" Turn 2 (inputs):
ask missing items in one batch, with examples of where to find them
(visura: rendita + categoria). Turn 3 (verify): read back rate + year +
comune for confirmation before computing. Never compute on turn 1.

## Rules

- Rates are municipal: never state a rate without naming comune + year.
  The script takes rates as input — it bundles no rates, ever.
- Main home exempt except luxury A/1, A/8, A/9 (200€ annual deduction, year-stated).
- Luxury deduction and possession months are pro-rated together in the script.
- Mid-year sale: month-split by possession months (15-day rule noted, verify yearly).
- Inagibile/collabente 50% base cut: conditions + comune proof required, flag it.
- Comodato to first-degree relatives: reductions under strict conditions — verify current rules, never promise.
- Agricultural land: exemptions by farmer status and mountain/hill lists — map only, referral to CAF/accountant.

## Scripts

- `scripts/imu.py` — pure math: base, annual tax, advance/balance split.
  Fixtures with expected outputs in `examples/fixtures/` (5 cases). Run:
  `python skills/imu-calcolo/scripts/imu.py --help`

## Examples

Good and bad cases in `examples/imu-cases.md`. Method in `references/metodo.md`.
Tables (multipliers, deductions) in `references/tabelle.md`.
Special cases in `references/casi-particolari.md`.
Payment notes (F24, deadlines, late paths) in `references/versamento.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Sold mid-year | `--mesi` split; paid acconto → conguaglio math, stated |
| 2 | Co-owned | split by share first, then run per share |
| 3 | Rate changed mid-year | recompute with new delibera, never average silently |
| 4 | Inagibile 50% | conditions + comune proof, flag (see casi-particolari) |
| 5 | Pertinenze oltre una | taxable as separate units, flagged |
| 6 | Ex-pat owner | same math + payment-from-abroad paths + referral |
| 7 | Comodato relatives | reductions map, verify current, never promise |
| 8 | Agricultural land | farmer/mountain lists map only + referral |
