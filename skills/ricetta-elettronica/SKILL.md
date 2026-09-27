---
name: ricetta-elettronica
description: Explain e-prescriptions with validity and use. Use when asked ricetta elettronica, e-prescription Italy, NRE.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Ricetta Elettronica

E-prescriptions decoded: NRE, validity, any-pharmacy use.

## When to use

- "ricetta elettronica", "e-prescription Italy", "NRE".
- Do not use for medical advice.

## Workflow

1. NRE + fiscal code: enough at any pharmacy (paper promemoria optional).
2. Validity windows by type (year-stated) + repeats (ripetibile/limitata) logic.
3. Out-of-region use: valid nationwide, stated plainly.
4. Output: steps + validity check + pharmacist questions.

## Rules

- No drug advice, admin paths only.
- Validity with year; rules update — verify live.
- Lost NRE: doctor reissue path, no panic.

## Examples

See `examples/ricetta-cases.md`. Validity in `references/validita.md`.

## Edge cases

- Narcotics/controlled: special forms, stricter rules flagged.
- Exempt patients: ticket link (see ticket-esenzioni), code on file.
- Tourist prescription: SSN vs private paths explained.
