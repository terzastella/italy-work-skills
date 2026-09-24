---
name: contributi-inps
description: Explain INPS contributions by track with minimal rates. Use when asked contributi INPS, gestione separata, minimal contributions Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[activity]"
user-invocable: true
disable-model-invocation: false
---

# Contributi INPS

Which INPS track, what it costs: Gestione Separata vs artigiani/commercianti.

## When to use

- "contributi INPS", "gestione separata", "minimal contributions", "aliquote INPS".
- Do not use for pension computation (rates and method only).

## Workflow

1. Route by activity: professional without albo → Gestione Separata;
   artigiani/commercianti → dedicated gestione with minimal fixed + percentage.
2. Show: rate (year-stated), minimal fixed where due, payment instalments, deductibility.
3. Forfettari note: contributions deductible from forfait income (see regime-forfettario).
4. Close with accountant/INPS check (rates move yearly).

## Rules

- Rates always with year; minimal fixed amounts with year.
- Reduced rates (e.g. co.co.co nuances, new activities) flagged as verify-items, never asserted.
- Never compute a full pension position here.

## Examples

See `examples/contributi-cases.md`. Track table in `references/gestioni.md`.

## Edge cases

- Mixed activities → each track separate, flag double-position costs.
- Employee + freelance → cumulo rules mention + referral.
- Arrears discovered → ravvedimento path mention, professional referral.
