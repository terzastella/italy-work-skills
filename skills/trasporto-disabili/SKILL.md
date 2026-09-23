---
name: trasporto-disabili
description: Explain disability transport permits and parking. Use when asked contrassegno disabili, disabled parking Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Trasporto Disabili

Permits and parking decoded: contrassegno, ZTL access, reserved stalls.

## When to use

- "contrassegno disabili", "disabled parking Italy".
- Do not use for benefit amounts (see `invalidita-104`).

## Workflow

1. Permit: medical certification + comune issuance + validity/renewal.
2. Rights: reserved stalls, ZTL transit (notify passages where required), free parking nuances.
3. Misuse: heavy sanctions + permit revocation — stated plainly.
4. Output: application steps + use rules + renewal calendar.

## Rules

- Personal permit (person, not car): transfer rules stated.
- ZTL with permit: many cities require passage notification — flag it.
- Abuse (lending the permit): sanctions stated bluntly.

## Examples

See `examples/trasporto-cases.md`. Rules in `references/regole.md`.

## Edge cases

- Temporary disability → temporary permits exist, flag + path.
- Traveling to another comune → recognition + local quirks noted.
- Expired permit in use → renew first, fines otherwise.
