---
name: cartelle-ader
description: Read AdER payment notices with 60-day options. Use when asked cartella esattoriale, AdER notice, payment notice Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[notice]"
user-invocable: true
disable-model-invocation: false
---

# Cartelle AdER

Payment notices decoded: what, how much, 60 days to act — never ignore.

## When to use

- "cartella esattoriale", "AdER notice".
- Do not use for disputes strategy (see options + referral).

## Workflow

1. Read: creditor entity, tax/period, tax vs penalties vs interest split, notification date.
2. 60-day clock from notification: pay · rateizzare (see rateizzazione-debiti) · impugn (terms + who).
3. Validity check basics: notification defects overview (flag, never verdicts).
4. Output: amount split + options ranked + deadline countdown.

## Rules

- 60 days from NOTIFICATION, not issue: stress it.
- Never "ignore it and wait": prescription is long and specific — referral.
- Amounts only from the notice.

## Examples

See `examples/cartelle-cases.md`. Reading keys in `references/chiavi.md`.

## Edge cases

- Never received (irreperibilità) → compiuta giacenza rules overview + check now.
- Already executive phase (pignoramento) → urgent professional, timelines stressed.
- Co-obligors → each notified separately, check all.
