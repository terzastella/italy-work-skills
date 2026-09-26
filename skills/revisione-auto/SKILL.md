---
name: revisione-auto
description: Explain vehicle inspections with timing and failures. Use when asked revisione auto, car inspection Italy, bollino blu.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[vehicle]"
user-invocable: true
disable-model-invocation: false
---

# Revisione Auto

Inspections on time: 4+2 rhythm, what they check, failed-test paths.

## When to use

- "revisione auto", "car inspection Italy".
- Do not use for fines appeals (see `multe-ricorso`).

## Workflow

1. Timing: first at 4 years, then every 2 (year-stated) + overdue math.
2. What is checked: brakes, lights, emissions, tires, chassis numbers.
3. Outcomes: pass · repeat (riparare + ripresentare) · suspended.
4. Output: due-date check + booking + cost range (year-stated).

## Rules

- Driving without revisione: sanctions + insurance issues — stated bluntly.
- Foreign/rehomed vehicles: separate tracks flagged.
- Never fake certificates: criminal matter, stated + refused.

## Examples

See `examples/revisione-cases.md`. Timing in `references/tempi.md`.

## Edge cases

- Bought used, revisione due soon → negotiate before purchase, flag it.
- Camper/motorcycles: same rhythm, specific centers noted.
- Missed by years → regularize now + sanction math, no minimization.
