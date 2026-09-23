---
name: isee-guida
description: Explain ISEE with DSU documents and common mistakes. Use when asked ISEE, DSU, indicator, bonus thresholds Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[household]"
user-invocable: true
disable-model-invocation: false
---

# ISEE Guide

ISEE without errors: household, DSU documents, current vs ordinary.

## When to use

- "ISEE", "DSU", "indicator", "bonus thresholds".
- Do not use for computing exact ISEE (INPS simulator/official calc only).

## Workflow

1. Household: who counts (residence + family status rules, see `references/nucleo.md`).
2. DSU documents checklist: incomes, assets (bank balances at 31/12!), properties, vehicles.
3. Ordinary vs corrente (current-year income drop cases).
4. Output: personalized checklist + where to file (INPS online, CAF, patronato) + validity.

## Rules

- Balances at 31/12 of year-2: the classic mistake — stress it.
- Never compute a final ISEE number: method + checklist, INPS calculates.
- Separated/divorced/special households → dedicated DSU paths, flag them.

## Examples

See `examples/isee-cases.md`.

## Edge cases

- Income drop this year → ISEE corrente path with conditions.
- Missing bank paper → exact giacenza media + saldo instructions per bank.
- Urgent bonus deadline → precompilata DSU route, timing noted.
