---
name: assegno-unico
description: Explain assegno unico with ISEE bands and application. Use when asked assegno unico, family allowance Italy, bonus bebè.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[household]"
user-invocable: true
disable-model-invocation: false
---

# Assegno Unico

Family allowance mapped: who gets it, how ISEE sets it, how to apply.

## When to use

- "assegno unico", "family allowance Italy", "bonus bebè".
- Do not use for computing exact entitlement (INPS tables only).

## Workflow

1. Who: dependent children (age/study/disability rules, year-stated).
2. ISEE link: bands set monthly amount (current tables with year).
3. Apply: INPS online/patronato + DSU link (see `isee-guida`) + timing (arrears rules).
4. Output: eligibility check + amount range + application steps.

## Rules

- Amounts with year; tables move — verify current INPS circular.
- No-DSU = minimum: state it (the classic loss).
- Separated parents/shared custody: split rules flagged, not assumed.

## Examples

See `examples/assegno-cases.md`. Band logic in `references/fasce.md`.

## Edge cases

- Late application → arrears limits stated plainly.
- Disabled children → higher bands + extra rules, flag + patronato.
- ISEE expired mid-year → renewal timing to avoid minimums.
