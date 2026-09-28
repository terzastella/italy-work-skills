---
name: corrispettivi-it
description: Explain Italian daily takings via telematic recorder or software. Use when asked corrispettivi, scontrino, registratore telematico, daily takings.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[activity]"
user-invocable: true
disable-model-invocation: false
---

# Corrispettivi

Daily takings the Italian way: telematic recorder vs software solution, invoice vs receipt.

## When to use

- "corrispettivi", "scontrino", "registratore telematico", "vending machine".
- Do not use for e-invoices (see `fattura-elettronica-it`).

## Workflow

1. Ask: activity type (retail, food, vending, fuel, services to consumers).
2. Route: RT (registratore telematico) vs software solution vs vending rules — see `references/strumenti.md`.
3. Explain: daily electronic transmission, invoice-vs-receipt choice, customer asking for invoice.
4. Close with AdE source link + "verify with accountant for your ATECO".

## Rules

- Invoice vs corrispettivo is the customer's right to choose: explain both.
- No hardware/brand recommendations beyond AdE-listed categories.
- Vending/fuel have special flows: flag them, do not generalize RT rules.

## Examples

See `examples/corrispettivi-cases.md`. Official sources in `references/fonti.md`.

## Edge cases

- Mixed B2B/B2C activity → both flows, kept separate.
- No internet at premises → RT offline buffer rules, cite AdE.
- Software house building integration → point to AdE technical specs, not DIY protocol guesses.
