---
name: pensione-reversibilita
description: Explain survivor pensions with rates and limits. Use when asked reversibilità, survivor pension Italy, pensione vedova.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Pensione di Reversibilità (Info Only, Delicate)

Survivor pensions mapped: rates by household, income limits, application — information, patronato files.

## When to use

- "reversibilità", "survivor pension Italy", "pensione vedova".
- NEVER for benefit computation as verdict (patronato referral).

## Workflow

1. Rates by household composition (spouse alone/children rates, year-stated).
2. Income limits reducing/cutting the benefit (year-stated) + cumulo rules.
3. Application: INPS/patronato + documents + timing from death.
4. Output: rate map + limits + steps. No amount promises.

## Rules

- Delicate skill: plain tone, patronato closes every answer.
- Rates/limits with year; they move — verify live.
- Divorced with assegno: special case flagged + referral, never DIY.

## Examples

See `examples/reversibilita-cases.md`. Rate table in `references/aliquote.md`.

## Edge cases

- Remarriage → benefit loss rules stated plainly.
- Coexisting own pension → cumulo limits explained generally, INPS computes.
- Convivenza (not married) → no reversibilità as spouse: state + alternatives (see unioni-convivenze).
