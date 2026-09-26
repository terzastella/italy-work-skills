---
name: banche-reclami
description: Write bank complaints with ABF escalation path. Use when asked reclamo banca, ABF, bank complaint Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[issue]"
user-invocable: true
disable-model-invocation: false
---

# Banche Reclami (+ABF)

Bank complaints that escalate: written reclamo first, ABF second.

## When to use

- "reclamo banca", "ABF", "bank complaint Italy", "arbitro bancario".
- Do not use for courts (lawyer referral).

## Workflow

1. Draft reclamo to bank: facts, dates, account refs (redacted), request, 60-day reply term note.
2. No/unfair reply → ABF: collegio by region, €20 fee note (year-stated), online filing path.
3. Documents: statements, contracts, prior letters — list with status.
4. Output: letter + ABF readiness checklist + timelines.

## Rules

- ABF only AFTER bank reclamo (mandatory order).
- Account numbers redacted in drafts (`****1234`).
- No outcome promises: ABF decides; statistics cited if known with year.

## Examples

See `examples/reclami-cases.md`. ABF path in `references/abf.md`.

## Edge cases

- Fraud/unauthorized ops → immediate block + denuncia + reclamo same day, timelines stressed.
- Closed account → complaint still possible within terms, flag it.
- Intermediary (not bank) → different arbitro (ACF for investments), route correctly.
