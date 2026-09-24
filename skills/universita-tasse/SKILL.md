---
name: universita-tasse
description: Explain university fees with ISEE-U bands and aid. Use when asked tasse universitarie, ISEE-U, scholarships Italy, DSU diritto studio.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[ateneo]"
user-invocable: true
disable-model-invocation: false
---

# Università Tasse e Aiuti

Fees by ISEE-U bands + no-tax area + scholarships: pay right, miss nothing.

## When to use

- "tasse universitarie", "ISEE-U", "scholarships Italy", "DSU diritto studio".
- Do not use for school levels (see `scuola-iscrizioni`).

## Workflow

1. ISEE-U first (university ISEE variant — see `isee-guida` differences).
2. No-tax area + bands per ateneo (each university publishes tables — cite the ateneo).
3. DSU scholarships: call, deadlines, merit + income gates.
4. Output: fee estimate path + aid checklist + deadlines calendar.

## Rules

- Ateneo tables differ: always cite the specific university + year.
- No-tax thresholds with year; verify current.
- Out-of-course (fuori corso) surcharges flagged honestly.

## Examples

See `examples/universita-cases.md`. No-tax logic in `references/notax.md`.

## Edge cases

- Part-time student status → fee reductions where offered.
- International student → dedicated desks + ISEE-U parificato paths.
- Late ISEE-U → max band applied: file early, stated bluntly.
