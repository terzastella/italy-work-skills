---
name: ticket-esenzioni
description: Explain health copay exemptions with codes. Use when asked ticket sanitario, esenzione ticket, copay exemption Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Ticket Esenzioni

Copay exemptions mapped: income, chronic, disability, pregnancy — codes and validity.

## When to use

- "ticket sanitario", "esenzione ticket", "copay exemption Italy".
- Do not use for medical advice.

## Workflow

1. Profile: income (ISEE-linked codes), chronic disease (pathology list), disability %, pregnancy.
2. Match to exemption codes (see `references/codici.md`, region + year).
3. Validity/renewal per code + where registered (ASL/doctor).
4. Output: matching codes + how to activate + expiry note.

## Rules

- Codes with region + year; lists move — verify current.
- Never invent a code: unmatched cases get the application path, not a guess.
- Pregnancy/invalidità paths flagged with dedicated rules.

## Examples

See `examples/ticket-cases.md`.

## Edge cases

- Expired exemption used at booking → renewal before the visit, flag costs otherwise.
- Cross-region care → exemption recognition notes, verify.
- Changed income → re-check yearly, auto-renewal not assumed.
