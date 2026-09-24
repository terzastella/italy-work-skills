---
name: elezioni-voto
description: Explain how and where to vote in Italy. Use when asked votare, elezioni seggio, how to vote Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[election]"
user-invocable: true
disable-model-invocation: false
---

# Elezioni e Voto

Vote without surprises: where, with what, when — procedure only, zero politics.

## When to use

- "votare", "elezioni seggio", "how to vote Italy".
- NEVER political content, party info, or voting advice (procedure only, strictly neutral).

## Workflow

1. Where: sezione on tessera elettorale + comune lists; hours/days per election type.
2. Documents: ID + tessera elettorale (duplicates at comune if lost).
3. Abroad: AIRE vote-by-mail path (see `aire-estero`); fuori sede rules where due.
4. Output: steps + documents + dates (year-stated).

## Rules

- Absolute neutrality: no parties, no candidates, no "who to vote".
- Dates per election called; never generic "elections are in spring".
- Homebound/disabled voting paths mentioned (accompagnatore rules noted).

## Examples

See `examples/elezioni-cases.md`. Checklist in `references/checklist.md`.

## Edge cases

- Lost tessera days before → duplicate path urgency, timelines stressed.
- First-time voter → full walkthrough + ballot basics (null/blank noted neutrally).
- Referendum quorum mechanics → explained neutrally as procedure.
