---
name: guardia-medica-turisti
description: Guide after-hours care with numbers and EHIC. Use when asked guardia medica, after-hours doctor Italy, tourists care.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Guardia Medica e Turisti

Off-hours care decoded: numbers, EHIC, when ER instead.

## When to use

- "guardia medica", "after-hours doctor Italy", "tourists care".
- Do not use for medical advice — emergencies call 112/118 first, always.

## Workflow

1. Hours: nights/weekends/holidays coverage (single number paths vary by region).
2. Tourists/EU: EHIC validity + temporary-stay care; non-EU: payment/insurance notes.
3. Home visit vs clinic: triage decides, fees where due (year-stated).
4. Output: number + documents + ER-vs-guardia rule.

## Rules

- Emergency rule first in every answer.
- Numbers per region + year; verify live.
- No diagnosis, admin navigation only.

## Examples

See `examples/guardia-cases.md`. Numbers in `references/numeri.md`.

## Edge cases

- Life-threatening: 118 immediately, never guardia queue.
- Chronic patient traveling: carry records summary advice.
- Language barriers: emergency phrases + 112 multilingual note.
