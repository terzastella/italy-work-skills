---
name: regime-forfettario
description: Explain Italy's flat-rate scheme with thresholds and calculations. Use when asked forfettario, flat rate, 85.000, 5 percent, coefficiente.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Regime Forfettario (2026 rules)

Italy’s flat-rate scheme explained with current thresholds: who qualifies, what changes at 85k/100k.

## When to use

- "forfettario", "flat rate Italy", "85.000", "5%", "coefficiente di redditività".
- Do not use for tax advice or filing: information + calculation method only.

## Workflow

1. Check the 2026 gates (see `references/requisiti.md`): prior-year revenue ≤85.000€,
   employee costs ≤20.000€, employee/pension income within limit, no exclusion causes.
2. Two-threshold logic: ≤85.000€ stay · 85.001–100.000€ exit next year ·
   >100.000€ immediate exit with VAT from the breaching invoice.
3. Show the math: revenue × coefficient − social contributions = base × 15% (or 5% startup).
4. Always close with: verify with accountant; rules change yearly (checked 2026-09-23).

## Rules

- Amounts always with year ("85.000€, 2026"). Never present 2026 rules as timeless.
- Professionals: threshold on takings; firms: on accrual — say which applies.
- Never declare eligibility ("you qualify"): list gates, let the accountant decide.
- 5% startup: only with all L.190/2014 art.1 c.65 conditions (new activity, prior 3 years, no continuity).

## Examples

See `examples/forfettario-cases.md`. Official sources in `references/fonti.md`.

## Edge cases

- Near-threshold year (80-100k) → monitoring plan + what happens at each line.
- Employee income alongside → check the yearly limit (35.000€ for 2026, back to 30.000€ in 2027 per current law).
- Prior ordinary year with late takings → taxed under ordinary rules, not forfait (see worked case).
