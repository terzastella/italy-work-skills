---
name: fido-scoperto
description: Explain overdrafts with costs and revocation. Use when asked fido, scoperto conto Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Fido e Scoperto

Overdrafts decoded: agreed vs messy, costs, revocation shocks.

## When to use

- "fido", "scoperto conto Italy".
- Do not use for loan advice.

## Workflow

1. Fido accordato (rate, fees, duration) vs sconfinamento (higher costs, tolerance limits).
2. Cost math: rates + fees on user figures (year-stated).
3. Revocation: bank can pull back with notice — contingency plan stated.
4. Output: situation map + cost math + questions for bank.

## Rules

- Rates/fees with year; verify live.
- Chronic overdraft: debt-plan logic (see fondo-emergenza), no normalization.
- No bank endorsement.

## Examples

See `examples/fido-cases.md`. Cost logic in `references/costi.md`.

## Edge cases

- CRIF reporting from arrears: consequences + regularization urgency.
- Business overdraft mixing personal: separation advised plainly.
- Revoked suddenly: payment priorities + referral, urgent tone.
