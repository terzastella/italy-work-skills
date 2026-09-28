---
name: periodo-prova
description: Explain trial periods with duration and exit rules. Use when asked periodo di prova, trial period Italy, prova lavoro.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[contract]"
user-invocable: true
disable-model-invocation: false
---

# Periodo di Prova

Trial periods decoded: how long, who can exit, what happens after.

## When to use

- "periodo di prova", "trial period Italy".
- Do not use for dismissal disputes (see `licenziamento-info`).

## Workflow

1. Duration from CCNL + level (6 months legal max, year-stated; lower levels less) — cite contract.
2. During: either side exits freely, no notice (state it); duties must match hired mansioni.
3. After: automatic confirmation, seniority counts from day one.
4. Output: duration check + exit rules + mismatch flags.

## Rules

- Duration only with CCNL cited; never generic "3 months".
- Mismatched duties during prova → flag + referral.
- Sick leave during prova: rules differ, flag + verify.

## Examples

See `examples/prova-cases.md`. Duration logic in `references/durate.md`.

## Edge cases

- Repeated fixed-terms with prova each time → abuse pattern, flag + referral.
- Prova never written → legal default applies, explain + verify.
- Executives (dirigenti): different rules, do not generalize.
