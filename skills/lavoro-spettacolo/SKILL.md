---
name: lavoro-spettacolo
description: Explain entertainment work with ex-ENPALS rules. Use when asked lavoro spettacolo, entertainment workers Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Lavoro dello Spettacolo

Entertainment work decoded: ex-ENPALS contributions, intermittents, protections.

## When to use

- "lavoro spettacolo", "entertainment workers Italy".
- Do not use for generic fixed-term rules.

## Workflow

1. Registration: ex-ENPALS (now INPS gestione) positions for artists/technicians.
2. Intermittent gigs: contribution days logic + NASpI interplay (see `naspi-guida`).
3. Contracts: scritture, rehearsals pay, overtime specifics flagged.
4. Output: situation check + documents + union (SLC) referral.

## Rules

- Gig-by-gig contributions: days counted, stated as the key metric.
- Undeclared gigs ("alla romana"): illegality + lost protections, stated plainly.
- Rates year-stated; verify live.

## Examples

See `examples/spettacolo-cases.md`. Contribution logic in `references/giornate.md`.

## Edge cases

- TV/film extras: specific CCNL pockets flagged, not generalized.
- Teaching artists: mixed regimes mapped, referral for splits.
- Injury on stage: INAIL + specific procedures, urgent tone.
