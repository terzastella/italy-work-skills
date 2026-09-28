---
name: lavoro-notturno
description: Explain night work with premiums and limits. Use when asked lavoro notturno, night work Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[contract]"
user-invocable: true
disable-model-invocation: false
---

# Lavoro Notturno

Nights decoded: definition, premiums, health checks, bans.

## When to use

- "lavoro notturno", "night work Italy".
- Do not use for on-call (see `reperibilita-lavoro`).

## Workflow

1. Definition by law/CCNL (hours band, year-stated) + who counts as night worker.
2. Pay: premiums by CCNL cited + Sunday-night stacking logic.
3. Health: surveillance visits where due; protected categories (maternity/minors) bans.
4. Output: situation check + pay math + questions for employer.

## Rules

- Premiums only with CCNL cited; never generic percentages as law.
- Bans (maternity/minors) stated plainly with referral paths.
- Systematic nights without checks: mismatch flag + referral.

## Examples

See `examples/notturno-cases.md`. Bands in `references/fasce.md`.

## Edge cases

- Pregnant worker on nights → exemption path + medical cert, urgent tone.
- Rotating shifts and rest: 11h rule interplay (see orario-riposi).
- Smart-worker "night messages" → disconnection interplay flagged.
