---
name: maternita-congedi
description: Explain maternity and parental leave with INPS paths. Use when asked maternità, congedi parentali, parental leave Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Maternità e Congedi (Info)

Leave rights mapped: mandatory, parental, fathers — information + patronato referral.

## When to use

- "maternità", "congedi parentali", "parental leave Italy", "paternità".
- Do not use for disputes or benefit computation (patronato referral).

## Workflow

1. Profile: employee vs autonomous (different tracks).
2. Map: mandatory maternity (5 months typical pattern) + parental leave shares +
   fathers' days (year-stated) + allowance % overview.
3. Application path: INPS online/patronato + documents + timing (before birth where due).
4. Close with: rules move yearly — verify current + patronato for the file.

## Rules

- Allowance figures with year only; no guaranteed amounts.
- Autonomous workers: separate track, state the difference plainly.
- Dismissal protection (dimissioni in gravidanza need validation) mentioned + referral.

## Examples

See `examples/maternita-cases.md`. Track table in `references/congedi.md`.

## Edge cases

- Adoption/fostering → dedicated rules, flag + referral.
- Premature birth → extensions exist, mention + verify.
- Employer pressure → rights stated + union/ispettorato paths.
