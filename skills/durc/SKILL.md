---
name: durc
description: Explain DURC compliance proof with validity and checks. Use when asked DURC, regolarità contributiva, DURC online.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[company]"
user-invocable: true
disable-model-invocation: false
---

# DURC (Regolarità Contributiva)

Proof of contribution compliance: what it is, how long it lasts, what breaks it.

## When to use

- "DURC", "regolarità contributiva", "DURC online".
- Do not use for fixing debts (repayment plans need professionals).

## Workflow

1. Explain: single document from INPS/INAIL/Casse proving contribution regularity;
   required for public contracts, incentives, some private clients.
2. Validity window (current rule + year) + verification portal path.
3. Irregularity causes: unpaid contributions, missing declarations — regularization
   path overview + professional referral.
4. Output: status reading + next steps, never a forged document.

## Rules

- Validity period with year; rules change — verify current.
- Never produce fake DURCs: reading + paths only.
- Incentives link: no DURC, no agevolazioni (see agevolazioni-assunzioni).

## Examples

See `examples/durc-cases.md`. Validity table in `references/validita.md`.

## Edge cases

- Subcontracting chains → each link needs its own, flag it.
- Just-opened firm → first-issuance timing explained.
- Disputed debt → contestation path mention + referral, no DIY.
