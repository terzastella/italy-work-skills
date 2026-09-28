---
name: ztl-permessi
description: Explain ZTL zones with permits and fines. Use when asked ZTL, zona traffico limitato, city permit Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[city]"
user-invocable: true
disable-model-invocation: false
---

# ZTL e Permessi

City zones decoded: hours, permits, cameras — per comune, always.

## When to use

- "ZTL", "zona traffico limitato", "city permit Italy".
- Do not use for fine appeals (see `multe-ricorso`).

## Workflow

1. City + zone: hours, gates, resident/visitor rules (comune ordinances, year-stated).
2. Permits: resident, garage, disabled, delivery — application paths.
3. Cameras (varchi): passages logged automatically; pass types that authorize.
4. Output: zone map + permit steps + fine-avoidance checklist.

## Rules

- Every fact per comune + year; ZTLs differ wildly — never generalize.
- Rental cars: fines follow the driver via rental company data — stated.
- Tourists: park outside + transit basics, no improvisation advice.

## Examples

See `examples/ztl-cases.md`. Comune variance in `references/comuni.md`.

## Edge cases

- Moved recently → resident permit timing vs cameras already active, urgent.
- Delivery/caregiver access → temporary passes paths.
- Fined already → appeal basics routed (see multe-ricorso), no tactics.
