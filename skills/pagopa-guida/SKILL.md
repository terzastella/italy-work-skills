---
name: pagopa-guida
description: Guide pagoPA payments with notice codes and receipts. Use when asked pagoPA, pay PA online, avviso pagamento, IUV code.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[notice]"
user-invocable: true
disable-model-invocation: false
---

# pagoPA Guide

Pay the PA without errors: notice codes, channels, receipts that prove payment.

## When to use

- "pagoPA", "pay PA online", "avviso pagamento", "IUV code", "bollettino PA".
- Do not use for tax computation (amounts come from the notice).

## Workflow

1. Take notice data: creditor entity, IUV/notice code, amount, deadline.
2. Channels: IO app, online banking (CBILL/pagoPA), tobacconist/ATM, entity counter.
3. Pay (user does it) → receipt (RT) kept: the ONLY proof. Note fees per channel.
4. Missed deadline: ravvedimento-like paths differ per tax — flag + referral, never "pay late same way".

## Rules

- Amounts from the notice only, never recomputed.
- Receipt (RT) kept as file + print for important matters.
- Never handle payment credentials: guide the clicks, user pays.

## Examples

See `examples/pagopa-cases.md`. Channel notes in `references/canali.md`.

## Edge cases

- Lost notice → retrieve from creditor/IO app, do not pay blind amounts.
- Double payment → refund path via creditor, keep both receipts.
- Scam avviso → verify creditor + IUV on official channels before paying.
