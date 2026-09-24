---
name: screening-prevenzione
description: Map free screenings by age and region. Use when asked screening gratuiti, prevention screening Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[age/region]"
user-invocable: true
disable-model-invocation: false
---

# Screening e Prevenzione

Free checks mapped: mammography, colon, cervix — invitation paths.

## When to use

- "screening gratuiti", "prevention screening Italy".
- Do not use for medical advice.

## Workflow

1. Programs by age/sex (year-stated): mammography bands, colon bands, cervix (Pap/HPV-DNA).
2. Invitation: ASL letters/calls — what to do if never invited.
3. Outside bands: GP route + ticket logic (see ticket-esenzioni).
4. Output: personal map + booking steps.

## Rules

- Bands with year + region (programs vary) — verify local ASL.
- No medical opinions, admin navigation only.
- Missed invite: rebooking path, no panic.

## Examples

See `examples/screening-cases.md`. Programs in `references/programmi.md`.

## Edge cases

- Moved regions → re-registration in screening lists flagged.
- Family history: earlier access via GP, not self-prescribed panic.
- Private screening offers: compare with free track first.
