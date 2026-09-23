---
name: cu-730-guida
description: Explain CU and 730 paths for employees and freelancers. Use when asked CU, 730, precompilata, dichiarazione redditi.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[profile]"
user-invocable: true
disable-model-invocation: false
---

# CU & 730 Guide

Which return for whom: CU received, 730 filed, precompilata accepted or edited.

## When to use

- "CU", "730", "precompilata", "dichiarazione redditi".
- Do not use for forfettari returns (Redditi PF, different path — flag it).

## Workflow

1. Profile: employee (CU, 730 possible) vs freelancer ordinary (Redditi PF) vs forfettario (Redditi PF LM).
2. CU: what it certifies (income + withholding), check figures vs payslips.
3. 730: precompilata via AdE (SPID/CIE) → accept as-is or edit → CAF/professional vs DIY trade-offs.
4. Deductions/detrazioni: common ones listed, documents to keep.

## Rules

- Never file anything: guidance + checklist only.
- Deadlines with year; extensions happen — verify current.
- Forfettario + 730 confusion → 730 is NOT their return, redirect clearly.

## Examples

See `examples/cu730-cases.md`. Document checklist in `references/documenti.md`.

## Edge cases

- Two CUs (job change) → both in 730, conguaglio logic explained.
- Foreign income → quadro RW mention + professional referral, never DIY.
- Mistakes in precompilata → edit path + integrativa mention.
