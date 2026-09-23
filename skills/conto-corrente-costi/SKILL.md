---
name: conto-corrente-costi
description: Read bank fee statements with total yearly cost. Use when asked conto corrente costi, bank fees Italy, estratto conto costi.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[statement]"
user-invocable: true
disable-model-invocation: false
---

# Conto Corrente Costi

Bank costs decoded: canone, operations, ISC, what to compare.

## When to use

- "conto corrente costi", "bank fees Italy".
- Do not use for investment advice.

## Workflow

1. Take fee statement (user-provided, redacted): canone, operation fees, card costs, overdraft terms.
2. Compute total yearly cost + ISC indicator explained (what it means).
3. Compare: 2-3 profiles (basic/online/premium) on total cost, not headline "zero fees".
4. Output: verdict + switch checklist (direct debits, salary, notice).

## Rules

- Account numbers redacted in drafts (`****1234`).
- "Zero fees" claims tested against conditions (giacenza minima etc.).
- No bank endorsement; math only.

## Examples

See `examples/conto-cases.md`. Fee anatomy in `references/voci.md`.

## Edge cases

- ISEE-linked free accounts (base accounts) → eligibility note.
- Overdraft used → tassi debitori + CMS-style costs explained plainly.
- Closing account → pending debits + notice + document retention.
