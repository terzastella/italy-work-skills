---
name: agevolazioni-assunzioni
description: Map Italian hiring incentives with requirements checklist. Use when asked agevolazioni assunzioni, hiring incentives Italy, sgravi contributivi.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[hire profile]"
user-invocable: true
disable-model-invocation: false
---

# Agevolazioni Assunzioni

Hiring incentives without losing them: requirements first, paperwork second.

## When to use

- "agevolazioni assunzioni", "hiring incentives Italy", "sgravi contributivi".
- Do not use for payroll computation.

## Workflow

1. Profile: who is hired (young, women, over-50, disabled, NASpI recipients), contract type.
2. Match to current incentives (see `references/incentivi.md`, year-stated): rate, cap, duration.
3. Requirements checklist: DURC, CCNL applied, prior headcount, no dismissals in window.
4. Output: eligible incentives ranked + application steps + consultant referral.

## Rules

- Incentives expire/change yearly: every fact with year + "verify current call".
- De minimis cumulation flagged where relevant.
- Never promise an incentive: "likely eligible IF all gates pass".

## Examples

See `examples/agevolazioni-cases.md`.

## Edge cases

- Recent dismissals in company → exclusion windows, check first.
- Apprenticeship overlap → compare with apprendistato track (see tirocinio/apprendistato).
- Domestic/agri workers → special tracks, do not generalize.
