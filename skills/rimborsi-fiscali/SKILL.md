---
name: rimborsi-fiscali
description: Guide tax refund claims with timelines. Use when asked rimborso fiscale, tax refund Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[tax]"
user-invocable: true
disable-model-invocation: false
---

# Rimborsi Fiscali

Claim back overpaid taxes: instance, timelines, nudges that work.

## When to use

- "rimborso fiscale", "tax refund Italy".
- Do not use for compensation alternative without comparing (see `compensazioni-f24`).

## Workflow

1. Route: return-claimed (automatic processing) vs separate istanza (model + documents).
2. Timelines: statutory processing + silence-assent where due (year-stated) + sollecito paths.
3. Interest on late refunds where provided.
4. Output: path + documents + timeline + follow-up calendar.

## Rules

- Timelines with year; offices vary on speed — ranges, never promises.
- Istanza content: exact tax/period/amount + proofs, no vague claims.
- Prescription terms for old credits stated first (don't file dead claims).

## Examples

See `examples/rimborsi-cases.md`. Path map in `references/percorsi.md`.

## Edge cases

- Refund stuck for years → sollecito + ricorso paths escalated, referral.
- Deceased taxpayer credit → heir claim track with documents.
- Offset instead → comparison table vs waiting, decided on cash needs.
