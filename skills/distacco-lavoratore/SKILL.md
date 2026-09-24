---
name: distacco-lavoratore
description: Explain secondments with A1 and allowance rules. Use when asked distacco lavoratore, secondment Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Distacco Lavoratore

Secondments decoded: genuine requirements, A1 abroad, allowances.

## When to use

- "distacco lavoratore", "secondment Italy".
- Do not use for transfers (see `trasferimento-sede`) or trips (see trasferte skills).

## Workflow

1. Genuine test: distaccante interest + temporaneità + cost reimbursement only (no profit).
2. Abroad (UE): A1 certificate path + host-country basics flagged.
3. Allowances/indennità during distacco + CCNL applied (origin vs host logic).
4. Output: genuineness check + documents + referral.

## Rules

- Fake secondment (somministrazione mascherata) flagged + referral, plainly.
- A1 before departure: stated as must, not tip.
- No "paper-only" arrangements advised, ever.

## Examples

See `examples/distacco-cases.md`. Genuineness in `references/test.md`.

## Edge cases

- Intra-group frequent shuttling → abuse patterns named + referral.
- Extra-EU postings → bilateral agreements check, specialist referral.
- Remote-work "distacco" claims → usually not distacco, reclassified + explained.
