---
name: garanzie-consumo
description: Explain Italy's 2-year legal guarantee with burden rules. Use when asked garanzia, legal warranty Italy, prodotto difettoso.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[product/issue]"
user-invocable: true
disable-model-invocation: false
---

# Garanzie Consumo (Legal Warranty)

Defective product rights: 2-year seller warranty, burden flip, repair/replace/refund ladder.

## When to use

- "garanzia", "legal warranty Italy", "prodotto difettoso", "diritto di recesso" (no — see `recesso-acquisti`).
- Do not use for commercial (voluntary) warranties beyond legal terms.

## Workflow

1. Check: consumer purchase (not B2B), within 2 years of delivery, defect (not wear/misuse).
2. Ladder: repair or replace first (seller chooses, reasonable time) → price reduction or refund if impossible.
3. Burden: first year presumed pre-existing (seller proves otherwise); second year consumer proves — state it.
4. Output: complaint draft to seller + documents to attach (receipt, photos).

## Rules

- B2B purchases excluded: say it when relevant.
- Commercial warranty ≠ legal: both can coexist, legal never waivable.
- Deadlines denounced "within 2 months of discovery" — state the rule with year.

## Examples

See `examples/garanzia-cases.md`. Ladder in `references/scala.md`.

## Edge cases

- Second-hand from professional → 1-year minimum agreement possible, flag it.
- Software/digital content → specific directive rules, referral for edge cases.
- Seller gone → producer chain options briefly, no miracles promised.
