---
name: telefonia-reclami
description: Write telecom complaints with conciliaweb path. Use when asked reclamo operatore, telefonia reclamo, conciliaweb AGCOM.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[issue]"
user-invocable: true
disable-model-invocation: false
---

# Telefonia Reclami (+Conciliaweb)

Phone/internet complaints that escalate: operator first, Conciliaweb second.

## When to use

- "reclamo operatore", "telefonia reclamo", "conciliaweb AGCOM".
- Do not use for courts (giudice di pace referral at most).

## Workflow

1. Draft reclamo to operator: line/account refs (redacted), facts, dates, request, 45-day reply note.
2. No/unfair reply → Conciliaweb (AGCOM/Corecom) online path + documents.
3. Indemnities (indennizzi automatici) for known faults: state where due.
4. Output: letter + escalation checklist + timelines.

## Rules

- Account/line numbers redacted in drafts.
- Conciliaweb only AFTER operator reclamo (mandatory order).
- No outcome promises.

## Examples

See `examples/telefonia-cases.md`. Path in `references/conciliaweb.md`.

## Edge cases

- Migration/portability blocked → fast-track angles flagged, urgency stated.
- Business lines → consumer-conciliazione may not apply, flag + referral.
- Debt collection threats → verify debt first, conciliaweb parallel where due.
