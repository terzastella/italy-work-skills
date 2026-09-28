---
name: colf-badanti
description: Guide domestic work contracts with levels and contributions. Use when asked colf badante, domestic worker Italy, contratto domestico.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Colf e Badanti

Domestic work in order: contract level, pay, contributions, permits.
Flagship skill: profiling funnel, convivente logic, cost picture with tables.

## When to use

- "colf badante", "domestic worker Italy", "contratto domestico".
- Do not use for company employees (different CCNL).

## Workflow (tappe with formal in/out)

### Tappa 1 — Profile (no figures before this)

Mansioni: colf vs badante vs baby-sitter. Hours: convivente or not.
Level per CCNL domestico (year-stated tables — see `references/livelli.md`).
Non-EU worker → permits flag now (hiring-decree flows + referral, never DIY on quotas).

### Tappa 2 — Pay picture

Minimum tables (year-stated, CCNL cited) + 13a + TFR accrual + ferie.
Convivente: vitto/alloggio counting stated, never folded silently.
Badante nights: presence vs active-hours rules flagged.

### Tappa 3 — Contributions + permits

INPS quarterly via F24 (rates + minimal, year-stated) + INAIL for domestics.
Dismissal terms: preavviso + TFR + domestic-specific rules (no generic licenziamento mix).

### Tappa 4 — Close with links

Payslip reading (see `busta-paga-leggi`), holidays (see `ferie-permessi`),
linked benefits (e.g. asilo: amounts with year). Irregular work: risks stated
plainly for both sides + regularization path.

## Multi-turn protocol

Turn 1 (profile): mansioni + hours + convivente — figures wait.
Turn 2 (contract + pay): level + full cost picture. Turn 3 (admin):
contributions + permits + first-payslip verification.

## Rules

- Levels and minimums with year + CCNL cited; never generic pay figures.
- Convivente vs non-convivente rules differ: vitto/alloggio counting stated.
- Irregular work: risks stated plainly for both sides, regularization path.

## Examples

Good and bad cases in `examples/colf-cases.md`. Level table in `references/livelli.md`.
Night-shift rules in `references/notti.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Non-EU, no permit | hiring-decree referral, never DIY |
| 2 | Night shifts | presence vs active hours flagged |
| 3 | Dismissal | preavviso + TFR domestic terms |
| 4 | Irregular work | risks both sides + regularization |
| 5 | Bonus linked | cross-links, amounts with year |
