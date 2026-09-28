---
name: scuola-privata-paritaria
description: Explain private parity schools with costs and value. Use when asked scuola privata, paritaria Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[level/city]"
user-invocable: true
disable-model-invocation: false
---

# Scuola Privata Paritaria

Private parity schools decoded: validity, costs, when they make sense.

## When to use

- "scuola privata", "paritaria Italy".
- Do not use for enrollment mechanics (see `scuola-iscrizioni`).

## Workflow

1. Parità concept: same legal value as statali, inspected requirements.
2. Costs: yearly fees ranges (year-stated) + detrazioni for school expenses where due.
3. Fit check: languages, hours, DSA support quality (see `dsa-bes-scuola`), commute.
4. Output: comparison framework + questions for open days.

## Rules

- No school endorsement, ever.
- Non-paritarie (pure private): titles NOT valid — stated bluntly.
- Costs with year; scholarships/borse where offered noted.

## Examples

See `examples/paritaria-cases.md`. Fit criteria in `references/criteri.md`.

## Edge cases

- Mid-year switch: nulla osta + timing, flag paperwork.
- DSA child: support quality questions first (see dsa skill).
- Religious vs lay: ethos fit stated as family decision, neutral.
