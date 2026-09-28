---
name: ferie-permessi
description: Explain holidays and permits with accrual rules. Use when asked ferie permessi, holidays permits Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
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

1. Accrual with the bundled script (preferred, reproducible): entitlement comes from
   the CCNL (explicit input, never generic) + part-time pro-rata on user figures:
   `python skills/ferie-permessi/scripts/ratei.py --spettanza 26 --mese 7 --fruiti 10`
2. Use: yearly fruition deadlines (year-stated) + employer scheduling vs worker choice balance.
3. Permits: ROL/ex-festivita overview + 104 permits mentioned only (dedicated paths elsewhere).
4. Output: balance math + deadlines + request steps.

## Rules

- Day counts only with CCNL cited; never generic "you get N days".
- Unused holidays: no cash-out during employment (exceptions stated), stated plainly.
- Sickness during holidays: suspension path + certificate rule (see `malattia-certificato`).

## Scripts

- `scripts/ratei.py` — monthly accrual + balance math (entitlement is a CCNL-cited input).
  Fixtures with expected outputs in `examples/fixtures/`.

## Examples

See `examples/ferie-cases.md`. Accrual logic in `references/ratei.md`.

## Edge cases

- Resignation with leftover holidays: payout vs notice interplay + referral.
- Denied holidays repeatedly: written trail + union referral.
- 104 permits interplay: separate track, briefly mapped, no detail here.
