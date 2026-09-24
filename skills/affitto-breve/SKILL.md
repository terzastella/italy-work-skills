---
name: affitto-breve
description: Guide short rentals with cedolare and CIN rules. Use when asked affitti brevi, short rental Italy, airbnb rules, CIN code.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[properties]"
user-invocable: true
disable-model-invocation: false
---

# Affitti Brevi

Short rentals done right: when it becomes a business, cedolare math, CIN duties.

## When to use

- "affitti brevi", "short rental Italy", "airbnb rules", "CIN code".
- Do not use for long-term leases (see `affitto-check`).

## Workflow

1. Count units for tourist rental: 1 = light touch; 2+ = entrepreneurial presumptions kick in.
2. Tax: cedolare secca first unit rate vs 26% on additional units (year-stated) + alternative IRPEF note.
3. Duties: CIN code display, guest reporting (alloggiati), safety basics.
4. Condo rules: building bans/limits check (regolamento), tourist-tax collection where due.

## Rules

- Unit-count thresholds with year; rules tightened over years — verify current.
- Cedolare percentages with year, never timeless.
- Platform income is visible to AdE: no "invisible" advice, ever.

## Examples

See `examples/brevi-cases.md`. Thresholds in `references/soglie.md`.

## Edge cases

- Mixed long+short portfolio → per-unit regime mapping, no blending.
- Non-resident owner → fiscal representative paths flagged, referral.
- Historic-center restrictions → municipal bans checked first.
