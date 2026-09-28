---
name: ateco-scelta
description: Choose the right ATECO code and know why it matters. Use when asked codice ATECO, ATECO choice, which ATECO.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[activity]"
user-invocable: true
disable-model-invocation: false
---

# ATECO Choice

The right code drives coefficient, contributions, grants: choose from real activity.

## When to use

- "codice ATECO", "which ATECO", "ATECO for ...".
- Do not use for opening procedure (see `partita-iva-apri`).

## Workflow

1. Ask: describe a typical week (what you actually do/sell), not the dream.
2. Match to ATECO families + forfettario coefficient per candidate (see `references/coefficienti.md`).
3. Propose 1 primary + 1 secondary with reason; flag grant/bandi relevance.
4. Close with: confirm with accountant before filing; codes can be added/changed later.

## Rules

- Code from activity, never from desired coefficient (fraud flag).
- Multiple activities → primary + secondaries, revenue summed for the 85k gate.
- Never guarantee a coefficient: cite table + year (year-stated), accountant confirms.

## Examples

See `examples/ateco-cases.md`.

## Edge cases

- Regulated professions (avvocati, medici...) → albo + specific rules, referral.
- Digital nomad mixed income → split activities, flag each.
- Code change later → explain variazione path briefly.
