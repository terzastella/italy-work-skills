---
name: mensa-scolastica
description: Explain school meal fees with ISEE bands. Use when asked mensa scolastica, school meals Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[city]"
user-invocable: true
disable-model-invocation: false
---

# Mensa Scolastica

Meal fees decoded: ISEE bands, enrollment, diets, arrears.

## When to use

- "mensa scolastica", "school meals Italy".
- Do not use for school choice (see `scuola-iscrizioni`).

## Workflow

1. Tariffs by ISEE band (comune tables, year-stated) + full-price default.
2. Enrollment: school/comune portal + deadlines ( Missed = full price, stated).
3. Special diets (health/religious): certificates needed, paths.
4. Output: band math + steps + arrears warning.

## Rules

- Tariffs per comune + year; never national figures as law.
- Arrears block service in many comuni: pay-first advice, stated plainly.
- Sibling discounts where due, verified locally.

## Examples

See `examples/mensa-cases.md`. Band logic in `references/fasce.md`.

## Edge cases

- Mid-year ISEE change → re-band timing explained.
- Separated parents billing → who pays rules + referral for disputes.
- Unpaid past year → new-year enrollment blocked risk, stated first.
