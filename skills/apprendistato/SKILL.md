---
name: apprendistato
description: Explain apprenticeships with types and protections. Use when asked apprendistato, apprenticeship Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Apprendistato

Real apprenticeships: types, training duty, pay path, protections.

## When to use

- "apprendistato", "apprenticeship Italy" (employment contract, not stage).
- Do not use for internships/tirocini (see `tirocinio-guida`).

## Workflow

1. Type: professionalizzante vs alta formazione/duale (age/goal differ, limits year-stated).
2. Must-haves: written training plan (PFI), tutor, progressive pay path.
3. Protections: same as employees + confirmation rules at the end.
4. Output: situation check + questions for employer + union referral if violated.

## Rules

- Training duty is the contract's soul: no training = abuse flag.
- Pay path by CCNL level progression — cite contract, never guess.
- Confirmation (conferma) rules stated; end-of-term options listed.

## Examples

See `examples/apprendistato-cases.md`. Types in `references/tipi.md`.

## Edge cases

- "Apprentice" doing senior work alone → mismatch flag + referral.
- Underpaid vs CCNL path → gap computed from contract tables, not memory.
- End of term → conferma, proroga, or exit options explained.
