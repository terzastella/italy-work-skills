---
name: ferie-permessi
description: Explain holidays and permits with accrual rules. Use when asked ferie permessi, holidays permits Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Ferie e Permessi

Holidays and permits decoded: accrual, use deadlines, permits overview.

## When to use

- "ferie", "permessi", "holidays permits Italy".
- Do not use for study permits detail (see `permessi-studio-150`).

## Workflow

1. Accrual: monthly ratei logic + part-time pro-rata math on user figures.
2. Use: yearly fruition deadlines (year-stated) + employer scheduling vs worker choice balance.
3. Permits: ROL/ex-festivita overview + 104 permits mentioned only (dedicated paths elsewhere).
4. Output: balance math + deadlines + request steps.

## Rules

- Day counts only with CCNL cited; never generic "you get N days".
- Unused holidays: no cash-out during employment (exceptions stated), stated plainly.
- Sickness during holidays: suspension path + certificate rule (see `malattia-certificato`).

## Examples

See `examples/ferie-cases.md`. Accrual logic in `references/ratei.md`.

## Edge cases

- Resignation with leftover holidays: payout vs notice interplay + referral.
- Denied holidays repeatedly: written trail + union referral.
- 104 permits interplay: separate track, briefly mapped, no detail here.
