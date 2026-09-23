---
name: sollecito-pagamento
description: Write 3-level payment reminders, polite to formal. Use when asked payment reminder, unpaid invoice, sollecito, chase payment Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[invoice data]"
user-invocable: true
disable-model-invocation: false
---

# Payment Reminders (Italy)

Three levels, escalating only if ignored: polite → firm → formal with interest.

## When to use

- "payment reminder", "unpaid invoice", "sollecito", "client doesn't pay".
- Do not use for legal injunctions (decreto ingiuntivo needs a lawyer).

## Workflow

1. Ask: invoice no., date, amount, days overdue, prior reminders sent.
2. Pick level: L1 <30 days polite · L2 30-60 firm · L3 60+ formal (late interest cited, rate from user).
3. Draft in Italian + English summary of tone. Facts only: number, date, amount.
4. Never threats, never penalties invented: interest only if contract/law cited by user.

## Rules

- Every reminder cites exact invoice data, never "your debt" generically.
- One escalation per ignored message; state next step calmly.
- Amounts/dates only as provided.

## Examples

See `examples/sollecito-cases.md`. Level templates in `references/livelli.md`.

## Edge cases

- Disputed invoice → pause reminders, propose clarification draft instead.
- PA debtor → longer statutory terms apply, flag them, stay formal.
- Partial payment → acknowledge received, restate residual with new deadline.
