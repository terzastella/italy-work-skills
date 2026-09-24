---
name: domanda-bando
description: Draft grant applications with attachments checklist. Use when asked domanda bando, application, candidatura contributo.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[call + company data]"
user-invocable: true
disable-model-invocation: false
---

# Domanda Bando

Applications that survive evaluation: complete, consistent, on time.

## When to use

- "domanda bando", "application", "candidatura contributo".
- Do not use for reading the call (see `bandi-pmi`).

## Workflow

1. Take: call text + company data (all given, nothing invented).
2. Draft per required sections, mirroring evaluation criteria order.
3. Attachments checklist with status (have/missing/[TODO]) + formats required.
4. Consistency pass: numbers identical everywhere (budget = narrative = forms).
5. Output draft + "before sending" checklist + deadline countdown.

## Rules

- Zero invented data: balance sheets, employees, costs only as provided.
- Amounts identical across all sections (top exclusion cause).
- Submit via official portal only: never fake submissions.
- Signatures/digital identity noted where required (SPID/CIE/firma digitale).

## Examples

See `examples/domanda-cases.md`. Exclusion errors in `references/errori.md`.

## Edge cases

- Missing mandatory doc → draft with `[TODO]` + how to get it, never skip silently.
- Deadline <7 days → triage: viable minimum vs advise next edition.
- Partnership applications → roles + letters per partner, consistency across all.
