---
name: leasing-finanziamento
description: Compare leasing vs loans with total cost. Use when asked leasing, finanziamento auto, lease vs loan Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[offers]"
user-invocable: true
disable-model-invocation: false
---

# Leasing vs Finanziamento

Lease or loan, decided on total cost: TAN/TAEG, maxi-rata, riscatto.

## When to use

- "leasing", "finanziamento auto", "lease vs loan Italy".
- Do not use for investment advice.

## Workflow

1. Take offers: TAN/TAEG, duration, anticipo, maxi-rata/riscatto, fees, insurance tied.
2. Total-cost math both + riscatto scenarios (keep vs return).
3. Business use: deductibility notes (year-stated) + accountant flag.
4. Output: table + winner by math + questions for dealer/bank.

## Rules

- TAEG-equivalent comparison always; TAN alone never decides.
- Riscatto math shown (return = sunk cost framing, honest).
- No dealer/bank endorsement.

## Examples

See `examples/leasing-cases.md`. Cost anatomy in `references/anatomia.md`.

## Edge cases

- VAT holders: deductibility differences flagged + accountant.
- Early termination → penalties read from contract, stated plainly.
- Used-car leasing → residual risks flagged extra.
