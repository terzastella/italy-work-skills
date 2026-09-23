---
name: acconti-calcolo
description: Compute Italian advance payments with historic method. Use when asked acconto imposte, advance payment, how acconti work Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[prior year tax]"
user-invocable: true
disable-model-invocation: false
---

# Acconti (Advance Payments)

Saldo + acconti without surprises: historic method, thresholds, previsional option.

## When to use

- "acconto imposte", "advance payment", "how acconti work".
- Do not use for deadline calendar (see `scadenze-fiscali`).

## Workflow

1. Take prior-year due tax (from return, e.g. LM42 line for forfettari).
2. Rule: if above 52€ threshold → advance due. Determine split from current rules
   (IRPEF-style instalments vs single sostitutiva advance — check AdE for the year,
   rules changed in the past). Never assert the split from memory.
3. Show math line by line + previsional alternative (lower expected income) with its risks.
4. Close with payment dates pointer (see `scadenze-fiscali`) + accountant check.

## Rules

- Numbers only from user data or return lines cited.
- Previsional method: explain penalties if underpaid, never recommend blindly.
- Thresholds with year. Forfettario vs ordinary kept distinct.

## Examples

See `examples/acconti-cases.md`. Method table in `references/metodo.md`.

## Edge cases

- First year (no history) → usually no advance, explain why.
- Sharp income drop → previsional path + risk note + professional referral.
- Mixed incomes → advances per tax type, do not merge.
