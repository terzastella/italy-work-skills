---
name: donazione-sangue
description: Guide blood donation with requirements and leave. Use when asked donazione sangue, blood donation Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Donazione Sangue

Donate right: requirements, centers, paid leave day.

## When to use

- "donazione sangue", "blood donation Italy".
- Do not use for medical advice.

## Workflow

1. Requirements: age/weight/health basics + temporary exclusions overview.
2. Where: AVIS/centri trasfusionali booking paths (no addresses invented).
3. Work leave: paid donation day rules (year-stated) + certificate to employer.
4. Output: eligibility check + booking steps + leave note.

## Rules

- Medical screening decides on site: never pre-clear anyone.
- Leave rules with year; CCNL specifics referred.
- No health claims beyond procedure.

## Examples

See `examples/donazione-cases.md`. Requirements in `references/requisiti.md`.

## Edge cases

- Recent travel/tattoo/piercing → temporary deferrals listed generally.
- Medication use → center decides case by case, flag + ask there.
- First-timer anxiety → process walkthrough, reassuring but honest.
