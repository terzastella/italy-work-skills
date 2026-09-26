---
name: imu-calcolo
description: Explain IMU property tax with base and rate method. Use when asked IMU, property tax Italy, seconda casa tax.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[property data]"
user-invocable: true
disable-model-invocation: false
---

# IMU Calcolo

IMU without surprises: who pays, on what base, at which rate, when — with a
neutral calculator for the math.

## When to use

- "IMU", "property tax Italy", "seconda casa", "quanto pago di IMU".
- Do not use for income taxes (see `irpef-scaglioni`), registration taxes,
  or TARI waste tax (see `tari-tassa`).

## Workflow

1. Qualify the property: main home (abitazione principale)? Seconda casa?
   Land (agricolo/edificabile)? Pertinenze (C/2, C/6, C/7 — one per category)?
2. Collect inputs (never compute from thin air): rendita catastale, categoria,
   comune, months of possession. Rate comes from the comune delibera for the
   tax year — ask the user for it or state it as given, never from memory.
3. Run the math with the bundled script (preferred, reproducible):
   `python skills/imu-calcolo/scripts/imu.py --rendita 850 --moltiplicatore 160 --aliquota-per-mille 10.6 --year 2026`
   Fallback by hand: rendita × 1.05 × multiplier → base; base × rate − deductions.
4. Output: base + annual tax + June advance + December balance (F24 codes noted)
   + "verify rate on comune delibera YEAR before paying" + accountant/comune check.

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
  Fixtures with expected outputs in `examples/fixtures/`. Run:
  `python skills/imu-calcolo/scripts/imu.py --help`

## Examples

Good and bad cases in `examples/imu-cases.md`. Method in `references/metodo.md`.
Tables (multipliers, deductions) in `references/tabelle.md`.

## Edge cases

- Sold mid-year → `--mesi` split; acconto already paid needs conguaglio math, stated.
- Rate changed by comune mid-year → recompute with the new delibera, never average silently.
- Ex-pat owner of Italian property → same math, payment-from-abroad paths flagged + referral.
- Co-owned property → split by ownership share first, then run per share.
- Pertinenze beyond one-per-category → taxable as separate units, flagged.
