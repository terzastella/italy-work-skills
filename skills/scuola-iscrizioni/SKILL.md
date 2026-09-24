---
name: scuola-iscrizioni
description: Guide school enrollments with windows and criteria. Use when asked iscrizioni scuola, school enrollment Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[level]"
user-invocable: true
disable-model-invocation: false
---

# Scuola Iscrizioni

Enrollments on time: online windows, priority criteria, open days that matter.

## When to use

- "iscrizioni scuola", "school enrollment Italy".
- Do not use for university (see `universita-tasse`).

## Workflow

1. Level: infanzia/primaria/secondarie — online portal (MIUR) windows with year.
2. Criteria: residence proximity, siblings, parents' work — school-published rankings.
3. Documents: fiscal codes, vaccinations (mandatory checks), residency proof.
4. Output: timeline + documents + 3 school questions (mensa, tempo pieno, trasporti).

## Rules

- Windows with year; dates move — verify current ministerial circular.
- Vaccination obligations stated plainly (access rules).
- No school "ranking" claims: fit criteria, not league tables.

## Examples

See `examples/scuola-cases.md`. Windows in `references/finestre.md`.

## Edge cases

- Mid-year transfer → nulla osta path + timing, flag paperwork.
- Foreign records/vaccines → translation + ASL validation steps.
- Over-subscribed school → appeal/waitlist mechanics explained, no guarantees.
