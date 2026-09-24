---
name: canone-rai
description: Explain TV licence fee with exemptions and opt-out. Use when asked canone Rai, TV licence Italy, canone bolletta.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Canone Rai

TV fee in the electricity bill: who pays, who is exempt, how to opt out.

## When to use

- "canone Rai", "TV licence Italy", "canone in bolletta".
- Do not use for other utility fees.

## Workflow

1. Rule: one fee per household with a TV (AdE presumption), charged via electricity bill.
2. Exemptions: over-75 with income limit, diplomats, (year-stated) — declaration to AdE by deadline.
3. No-TV opt-out: dichiarazione di non detenzione (yearly, deadline) — exact path.
4. Double charges (two bills): refund request path.

## Rules

- Amount with year (it changed over years — never timeless).
- Exemption income limits with year; verify current.
- Second homes do not double-pay: state the single-household rule.

## Examples

See `examples/canone-cases.md`. Exemption table in `references/esenioni.md`.

## Edge cases

- Deceased holder → voltura/exemption steps for heirs, flag it.
- Missed opt-out deadline → pay + next-year declaration, no retro miracles.
- Rented home → holder is the resident, landlord/tenant split explained.
