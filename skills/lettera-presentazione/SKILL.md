---
name: lettera-presentazione
description: Write Italian cover letters tied to the job ad. Use when asked cover letter, lettera di presentazione, lettera motivazionale.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[job ad]"
user-invocable: true
disable-model-invocation: false
---

# Lettera di Presentazione

Letters that get interviews: ad-specific, 4 paragraphs, 1 page.

## When to use

- "cover letter", "lettera di presentazione/motivazionale" (Italian context).
- Do not use for CVs (see `cv-europass`).

## Workflow

1. Ask: job ad (or link text), candidate's 2-3 matching proofs, contact.
2. Structure: hook on the ad (1 line) → why them (1) → why you with 2 proofs → call (availability + contact).
3. Body in Italian (formal `Lei`), notes around it in English.
4. Max 200 words. No CV repetition.

## Rules

- Every claim traceable to CV: never new jobs here.
- Company name + role spelled exactly as in the ad.
- No salary talk unless the ad asks.

## Examples

See `examples/lettera-cases.md`. Openings in `references/aperture.md`.

## Edge cases

- No ad (spontaneous) → target company + department + 1 reason, state it is spontaneous.
- Career change → transferable proof first, gap addressed in 1 line.
- Email body vs attachment → short body + attached letter, both provided.
