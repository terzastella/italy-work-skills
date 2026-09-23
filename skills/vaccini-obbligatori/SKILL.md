---
name: vaccini-obbligatori
description: Explain mandatory vaccines with schedule info. Use when asked vaccini obbligatori, mandatory vaccines Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[age]"
user-invocable: true
disable-model-invocation: false
---

# Vaccini Obbligatori (Info Only)

Schedules mapped: mandatory vs recommended, school links — information, pediatrician decides.

## When to use

- "vaccini obbligatori", "mandatory vaccines Italy".
- NEVER medical advice or anti-vaccine content (pediatrician referral).

## Workflow

1. Schedule by age (year-stated calendar): mandatory vs recommended split.
2. School link: documented requirements for enrollment (see `scuola-iscrizioni`).
3. Catch-up paths for missed doses + ASL booking.
4. Output: schedule map + booking steps. No medical opinions, ever.

## Rules

- Calendars with year; they update — verify live.
- No efficacy/safety debates here: schedule info only.
- Exemptions: medical only, certified — stated plainly.

## Examples

See `examples/vaccini-cases.md`. Schedule in `references/calendario.md`.

## Edge cases

- Foreign records → translation + ASL validation steps.
- Adult boosters (tetanus etc.) → schedules noted briefly.
- Hesitant parents → pediatrician conversation, never debates here.
