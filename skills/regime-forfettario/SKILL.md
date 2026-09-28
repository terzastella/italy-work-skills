---
name: regime-forfettario
description: Explain Italy's flat-rate scheme with thresholds and calculations. Use when asked forfettario, flat rate, 85.000, 5 percent, coefficiente.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.5", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Regime Forfettario (2026 rules)

Italy's flat-rate scheme explained with current thresholds: who qualifies,
what changes at 85k/100k. Flagship skill: gates checklist, threshold machine,
tax math — never an eligibility verdict.

## When to use

- "forfettario", "flat rate Italy", "85.000", "5%", "coefficiente di redditività".
- Do not use for tax advice or filing: information + calculation method only.

## Workflow (tappe with formal in/out)

### Tappa 1 — Gates first (no math before gates)

Run the checklist in `references/requisiti.md` against user facts:
prior-year revenue, employee costs, employee/pension income, exclusion causes
(see `references/esclusioni.md`). One unchecked gate → name it + what changes it.
Never declare eligibility: all-checked still ends with "accountant confirms".

### Tappa 2 — Threshold machine

≤85.000€ stay · 85.001–100.000€ exit next year · >100.000€ immediate exit
with VAT from the breaching invoice. Professionals: takings; firms: accrual —
say which applies. Run `--soglia-check` for the figure at hand.

### Tappa 3 — Tax math (script preferred, reproducible)

`python skills/regime-forfettario/scripts/forfettario.py --fatturato 60000 --coeff 0.78 --contributi 8000 --aliquota 15 --year 2026`
revenue × coefficient − social contributions = base × 15% (or 5% startup
with all L.190/2014 conditions).

### Tappa 4 — Close with the two sentences

Verify with accountant; rules change yearly (checked 2026-09-23).
Contributions stay deductible from forfait income (see `contributi-inps`).

## Multi-turn protocol

Turn 1 (gates): collect the four gate facts in one batch — revenue, costs,
employee income, exclusions. Turn 2 (math OR threshold): run ONE of them,
whichever the user asked. Turn 3 (what's next): INPS track, acconti calendar,
or first invoice — routed, never all at once.

## Rules

- Amounts always with year ("85.000€, 2026"). Never present 2026 rules as timeless.
- Professionals: threshold on takings; firms: on accrual — say which applies.
- Never declare eligibility ("you qualify"): list gates, let the accountant decide.
- 5% startup: only with all L.190/2014 art.1 c.65 conditions (new activity, prior 3 years, no continuity).
- Ex-employee continuity: the silent killer — flag at tappa 1, never as an afterthought.

## Scripts

- `scripts/forfettario.py` — tax math + threshold status (coefficient, thresholds, rate are inputs).
  Fixtures with expected outputs in `examples/fixtures/` (5 cases). The script never declares eligibility.

## Examples

Good and bad cases in `examples/forfettario-cases.md`. Gates in `references/requisiti.md`.
Exclusions in `references/esclusioni.md`. Official sources in `references/fonti.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Near-threshold year (80-100k) | monitoring plan + what happens at each line |
| 2 | Ex-employee continuity | exclusion risk flagged at tappa 1, strongly |
| 3 | Employee income alongside | yearly limit check (35.000€ 2026 → 30.000€ 2027 per current law) |
| 4 | Prior ordinary year, late takings | taxed ordinary, not forfait (see worked case) |
| 5 | Over 100k mid-year | immediate exit + VAT from breaching invoice, urgent tone |
| 6 | 5% startup doubt | all c.65 conditions listed, no shortcuts |
