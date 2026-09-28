---
name: energia-reclami
description: Write energy complaints with ARERA desk path. Use when asked reclamo energia, luce gas complaint, sportello ARERA.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[issue]"
user-invocable: true
disable-model-invocation: false
---

# Energia Reclami (ARERA)

Energy complaints that move: supplier first, ARERA desk second.

## When to use

- "reclamo energia", "luce/gas complaint", "sportello ARERA".
- Do not use for offer comparison (see `bollette-energia`).

## Workflow

1. Draft reclamo to supplier (see `telefonia-reclami` pattern): POD/PDR, facts, request, reply term.
2. No/unfair reply → Sportello ARERA conciliation path + documents.
3. Wrong-bill cases: conguaglio verification first (see `bollette-energia`).
4. Output: letter + escalation checklist.

## Rules

- POD/PDR redacted in drafts where sensitive.
- Supplier-first order mandatory (terms year-stated).
- Disconnection threats (morosità): fast action + rules stated urgently.

## Examples

See `examples/energia-cases.md`. ARERA path in `references/sportello.md`.

## Edge cases

- Prescribed bills (old conguagli) → prescription rules flagged, do not pay blindly.
- New tenant, old debt → not yours: voltura + dispute in parallel.
- Vulnerable customers (bonus/disagio) → protections fast-tracked.
