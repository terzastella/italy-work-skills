---
name: morosita-condominiale
description: Handle condo arrears with recovery paths. Use when asked morosità condominiali, condo arrears Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Morosità Condominiale

Arrears recovered in order: reminder, formal notice, injunction — no shortcuts.

## When to use

- "morosità condominiali", "condo arrears Italy".
- Do not use for legal strategy (lawyer referral for court).

## Workflow

1. Friendly reminder with statement first (errors happen).
2. Formal notice (diffida-style, tracked) + payment plan option where sensible.
3. Decreto ingiuntivo path: documents + costs + timelines overview.
4. Buyer of a debtor flat: solidarity rules + pre-purchase checks (see compravendita-casa).

## Rules

- Service cuts as pressure: limits stated (essential services protected).
- No shaming lists: privacy + dignity, stated plainly.
- Amounts from statements only, never estimated debts.

## Examples

See `examples/morosita-cases.md`. Escalation in `references/scala.md`.

## Edge cases

- Owner bankrupt/deceased → claim in procedure + referral, no DIY.
- Tenant vs owner debt → who owes whom mapped (see affitto-check logic).
- New admin inheriting arrears → handover audit first, stated as step one.
