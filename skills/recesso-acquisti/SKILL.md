---
name: recesso-acquisti
description: Guide 14-day withdrawal for distance and off-premises purchases. Use when asked recesso, ripensamento, return online purchase Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[purchase]"
user-invocable: true
disable-model-invocation: false
---

# Recesso Acquisti (Withdrawal)

Change your mind right: 14 days, exceptions, refund path.

## When to use

- "recesso", "ripensamento", "return online purchase", "diritto di recesso".
- Do not use for in-store purchases (no general right — flag it).

## Workflow

1. Check scope: distance (online/phone) or off-premises = covered; in-store = generally NOT covered.
2. Exceptions list (see `references/eccezioni.md`): sealed hygiene, custom, perishable, digital-after-consent, etc.
3. 14 days from delivery (goods) or contract (services); notice + return steps.
4. Refund: 14 days from seller's knowledge, same means, return costs rule stated.

## Rules

- In-store regret ≠ right: say it first when relevant.
- Exceptions checked one by one against the purchase, never assumed.
- Custom/sealed-opened cases decided carefully with the list.

## Examples

See `examples/recesso-cases.md`.

## Edge cases

- Digital download started with consent → right lost, verify consent was asked.
- Partial returns → per-item logic, shipping cost split stated.
- Seller ignores → formal notice draft + ADR/authority paths mentioned.
