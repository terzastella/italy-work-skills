---
name: salute-mentale-info
description: Explain mental-health access paths without diagnosis. Use when asked salute mentale, supporto psicologico Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Salute Mentale (Info Only, Delicate)

Access paths mapped: CSM, helplines, emergencies — information, never diagnosis.

## When to use

- "salute mentale", "supporto psicologico Italy".
- NEVER diagnosis, therapy advice, or crisis counseling (professionals only).

## Workflow

1. Access: GP referral → CSM/consultori + helplines (numbers, year-stated) + private paths.
2. Urgency ladder: distress → helpline now; danger → 118 immediately (stated first when relevant).
3. Costs: SSN coverage vs private fees overview.
4. Output: paths + numbers + referral. Plain, warm, non-alarmist tone.

## Rules

- Delicate skill: helpline numbers + 118 in every relevant answer.
- No diagnosis, no therapy content, no medication talk — ever.
- Minors: parental involvement rules noted + school counselor paths.

## Examples

See `examples/mentale-cases.md`. Access map in `references/accessi.md`.

## Edge cases

- Immediate danger stated → 118 now, no checklists first.
- Workplace mobbing link: paths + union referral, documented everything.
- Postpartum distress: dedicated paths flagged with extra care.
