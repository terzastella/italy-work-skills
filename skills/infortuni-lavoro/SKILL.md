---
name: infortuni-lavoro
description: Explain work injury reports with INAIL path. Use when asked infortunio lavoro, work injury Italy, denuncia INAIL.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Infortuni sul Lavoro

Work injuries handled fast: report, certificate, INAIL claim — information, union referral.

## When to use

- "infortunio lavoro", "work injury Italy", "denuncia INAIL".
- Do not use for disputes/compensation strategy (referral).

## Workflow

1. Immediate: medical care + tell employer promptly + keep everything (photos, witnesses, reports).
2. Denuncia: employer files to INAIL (terms), medical certificate chain.
3. Benefits overview: indennità temporanea + postumi tracks (year-stated), employer top-ups by CCNL.
4. Output: steps with timing + documents + referral.

## Rules

- Timing stressed: late reports complicate everything — stated first.
- Commuting accidents (in itinere) covered with conditions, explained.
- No blame narratives in outputs: facts + steps only.

## Examples

See `examples/infortuni-cases.md`. Steps in `references/passi.md`.

## Edge cases

- Employer minimizing ("no need to report") → report anyway, rights stated + referral.
- Serious injury → lawyer + union immediately, no checklists first.
- Autonomous/domestic workers → different tracks flagged, not mixed.
