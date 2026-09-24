---
name: volture-catastali
description: Guide cadastral transfers with documents and timing. Use when asked voltura catastale, cadastral transfer Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[case]"
user-invocable: true
disable-model-invocation: false
---

# Volture Catastali

Ownership records updated: succession, deeds, court orders — documents + timing.

## When to use

- "voltura catastale", "cadastral transfer Italy".
- Do not use for reading a visura (see `visura-leggimi`).

## Workflow

1. Trigger: succession (dichiarazione first) · deed (notaio files it) · court order · riunione usufrutto.
2. Documents per trigger + tributi catastali (fixed amounts, year-stated).
3. Timing: statutory terms + sanzioni for lateness.
4. Output: path + documents + costs + referral for tangled cases.

## Rules

- Who files what: notaio files deeds; heirs file succession-linked ones.
- Terms with year; late = sanctions, stated plainly.
- Never invent cadastral data: visura first (see visura-leggimi).

## Examples

See `examples/volture-cases.md`. Trigger table in `references/casi.md`.

## Edge cases

- Pre-1987 records chaos → historical search path + technician referral.
- Mismatched data (names/areas) → rettifica before voltura, order matters.
- Riunione usufrutto on death → automatic-ish but file it, explain.
