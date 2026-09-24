---
name: esami-intramoenia
description: Explain intramoenia exams with costs and waits. Use when asked intramoenia, private exams public hospital Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[exam]"
user-invocable: true
disable-model-invocation: false
---

# Esami in Intramoenia

Paying to skip the queue, decoded: costs, waits, receipts that count.

## When to use

- "intramoenia", "private exams public hospital Italy".
- Do not use for medical advice.

## Workflow

1. What: same public doctors, paid track, shorter waits — mechanics explained.
2. Costs: price lists per structure (no national tariff) + detrazione link (see spese-mediche-detrazioni).
3. When worth it: urgency vs cost trade-off framework, no verdicts.
4. Output: comparison (SSN wait vs intramoenia cost) + booking steps.

## Rules

- Prices per structure + year; never national figures as law.
- Receipts kept for detrazioni — stated as step, not tip.
- No doctor endorsements.

## Examples

See `examples/intramoenia-cases.md`. Trade-offs in `references/confronto.md`.

## Edge cases

- Urgent need → ER/urgent paths first (see pronto-soccorso-ticket), not intramoenia shopping.
- Exempt patients: intramoenia still paid — stated to avoid confusion.
- Second opinions: intramoenia as fast route, framed neutrally.
