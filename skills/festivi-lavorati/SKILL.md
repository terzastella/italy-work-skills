---
name: festivi-lavorati
description: Explain holiday work pay with Sunday rules. Use when asked festivi lavorati, holiday work Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[contract]"
user-invocable: true
disable-model-invocation: false
---

# Festivi Lavorati

Holidays worked decoded: premiums, compensatory rest, Sunday logic.

## When to use

- "festivi lavorati", "holiday work Italy".
- Do not use for overtime (see `straordinari-info`).

## Workflow

1. Which holidays: national + Santo patrono + soppresse economics (who pays what).
2. Worked-holiday pay: premiums by CCNL cited + riposo compensativo option.
3. Sunday as weekly rest: working it triggers specific rules (flagged per CCNL).
4. Output: pay math + rest check + questions for employer.

## Rules

- Premiums only with CCNL cited; never generic percentages as law.
- Soppresse paid anyway: stated (common confusion).
- Retail/tourism openings: Sunday-work regimes flagged, not judged.

## Examples

See `examples/festivi-cases.md`. Premium logic in `references/maggiorazioni.md`.

## Edge cases

- Forced holiday work systematically → mismatch flag + referral.
- Part-time verticale on holidays → proportional logic flagged.
- Religious alternatives requested → accommodation paths, neutral tone.
