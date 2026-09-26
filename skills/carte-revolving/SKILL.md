---
name: carte-revolving
description: Explain revolving cards with real TAEG math. Use when asked carta revolving, revolving credit Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[offer]"
user-invocable: true
disable-model-invocation: false
---

# Carte Revolving

Revolving decoded: minimum-payment trap, real TAEG, exit math.

## When to use

- "carta revolving", "revolving credit Italy".
- Do not use for loan advice (comparison math only).

## Workflow

1. Mechanics: credit line refills as you repay minimums — why balances persist.
2. Real cost: TAEG (year-stated) on an example balance over 12 months, shown plainly.
3. Exit: fixed-instalment switch + payoff plan math from user figures.
4. Output: cost math + exit plan + questions for the bank.

## Rules

- TAEG with year; minimum-payment trap stated bluntly with numbers.
- No product endorsement; no "good debt" framing.
- Usury-threshold cross-check note (see `usura-tassi`).

## Scripts

- `scripts/revolving.py` — 12-month cost simulation + exit math (TAEG is an input).
  Fixtures with expected outputs in `examples/fixtures/`. Minimums shown as trap, with numbers.

## Examples

See `examples/revolving-cases.md`. Cost logic in `references/costo.md`.

## Edge cases

- Multiple revolvings stacked → total minimums vs income math, urgent tone.
- Pensioner targets → vulnerability flag + family involvement advice.
- Already deep → debt-plan order (highest TAEG first), general method only.
