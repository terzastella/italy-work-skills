---
name: trasferte-lavoro
description: Guide national work trips with diaria and receipts. Use when asked trasferta Italia, work trip allowance Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[trip]"
user-invocable: true
disable-model-invocation: false
---

# Trasferte Italia

National trips covered: diaria vs receipts, what to keep, what is taxed.

## When to use

- "trasferta Italia", "work trip allowance Italy".
- Do not use for abroad trips (see `trasferta-estero`).

## Workflow

1. Regime: diaria forfettaria vs piè di lista (company policy decides, ask).
2. Keep: invoices/receipts originals, trip authorization, times.
3. Tax frame: exempt quotas overview (year-stated) + beyond-quota treatment.
4. Output: checklist + cost table + policy questions.

## Rules

- Quotas with year; verify live.
- Receipts originals rule stressed (photos as backup, not replacement).
- Mixed business/personal days: split accounting stated.

## Examples

See `examples/trasferte-cases.md`. Quota logic in `references/quote.md`.

## Edge cases

- Same-day trips: meal-only rules flagged.
- Company car vs own: kilometric refunds (ACI tables cited, year) vs fuel receipts.
- Smart-worker "trips" to HQ: transfer vs trip boundary explained.
