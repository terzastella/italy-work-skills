---
name: mediazione-civile
description: Explain civil mediation with mandatory cases. Use when asked mediazione civile, mediation Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[dispute]"
user-invocable: true
disable-model-invocation: false
---

# Mediazione Civile (Info Only)

Mediation mapped: mandatory matters, first meeting, costs, outcomes.

## When to use

- "mediazione civile", "mediation Italy".
- Do not use for strategy (mediator/lawyer referral).

## Workflow

1. Mandatory matters list (condominio, diritti reali, successioni, medical liability, etc. — year-stated).
2. Flow: organism choice → first meeting (often free/low-cost) → negotiate → agreement (enforceable) or nothing.
3. Costs: fees by value bands (year-stated) + lawyer presence rules.
4. Output: path map + costs + referral.

## Rules

- Mandatory list with year; skipping it kills later court cases — stated first.
- No negotiation tactics here.
- Every answer ends with referral for real disputes.

## Examples

See `examples/mediazione-cases.md`. Matter list in `references/materie.md`.

## Edge cases

- Urgent measures needed → mediation too slow: court first, flag + referral.
- Failed mediation → court path unlocked, certificate kept.
- Cross-border party → practical hurdles flagged early.
