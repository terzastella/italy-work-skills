---
name: imu-calcolo
description: Explain IMU property tax with base and rate method. Use when asked IMU, property tax Italy, seconda casa tax.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[property data]"
user-invocable: true
disable-model-invocation: false
---

# IMU Calcolo

IMU without surprises: who pays, on what base, at which rate, when.

## When to use

- "IMU", "property tax Italy", "seconda casa".
- Do not use for income taxes or registration taxes.

## Workflow

1. Ask: property type (main home? seconda casa? land? buildable area?), cadastral data (rendita, categoria), municipality.
2. Rules: main home exempt (except luxury A/1-A/8-A/9) · second homes/land taxable.
3. Method: rivaluta rendita +5%, × multiplier by category, × municipal rate (check comune delibera, year).
4. Show math + June/December instalments + F24 note. Close with accountant/comune check.

## Rules

- Rates are municipal: never state a rate without naming comune + year.
- Luxury main homes (A/1, A/8, A/9) pay with 200€ deduction — flag the exception.
- Never compute from thin air: rendita + categoria + comune required.

## Examples

See `examples/imu-cases.md`. Method in `references/metodo.md`.

## Edge cases

- Inagibile/collabente 50% base → conditions + comune proof required, flag it.
- Comodato to relatives → reductions under conditions, verify current rules.
- Sold mid-year → months of possession split, count rules stated.
