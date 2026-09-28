---
name: medico-base
description: Guide GP choice and change with out-of-region rules. Use when asked medico di base, choose GP Italy, cambio medico.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Medico di Base

GP sorted: choice, change, temporary stays elsewhere.

## When to use

- "medico di base", "choose GP Italy", "cambio medico".
- Do not use for medical advice.

## Workflow

1. Choice/change: ASL online/counter with SPID + availability lists (massimali).
2. Out-of-region stays: temporary registration paths (domicilio sanitario) with durations.
3. Pediatrician switch at age limits noted.
4. Output: steps + documents + fallback counter path.

## Rules

- Massimali (patient caps) explain "no availability" answers.
- No medical content, admin navigation only.
- Region asked first (ASL portals differ, procedures year-stated).

## Examples

See `examples/medico-cases.md`. Paths in `references/percorsi.md`.

## Edge cases

- Moved recently → residenza + GP change order explained.
- Homebound patient → ADI/home-visit paths mentioned.
- Tourist/short stay → guardia medica + EHIC notes for EU visitors.
