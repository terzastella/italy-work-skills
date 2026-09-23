---
name: rateizzazione-debiti
description: Explain tax debt instalments with lapse rules. Use when asked rateizzare cartella, instalment plan AdER, dilazione debiti.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[debt]"
user-invocable: true
disable-model-invocation: false
---

# Rateizzazione Debiti

Pay over time without losing the plan: ordinary vs extraordinary, lapse rules.

## When to use

- "rateizzare cartella", "instalment plan AdER", "dilazione debiti".
- Do not use for disputing the debt (see `cartelle-ader`).

## Workflow

1. Amount → ordinary plan (up to threshold) vs extraordinary (above, documented hardship).
2. Missed-instalment lapse rule (count + year-stated): the plan-killer, stated first.
3. Request path: online/office + documents + first-instalment timing.
4. Output: plan math + lapse warning + calendar.

## Rules

- Lapse count with year; rules tightened/loosened over time — verify live.
- New debts during plan: compatibility rules flagged.
- Never advise strategic defaulting.

## Examples

See `examples/rateizzazione-cases.md`. Plan table in `references/piani.md`.

## Edge cases

- Lapsed plan → re-application limits (one-shot rules), professional now.
- Business in crisis → composizione paths mentioned + specialist referral.
- Parallel ravvedimento possible? Explain interaction, no double benefits assumed.
