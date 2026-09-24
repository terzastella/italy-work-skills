---
name: assicurazione-viaggio
description: Explain travel insurance with claim steps. Use when asked assicurazione viaggio, travel insurance Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[trip]"
user-invocable: true
disable-model-invocation: false
---

# Assicurazione Viaggio

Trip cover decoded: medical, baggage, cancellation — claim steps that work.

## When to use

- "assicurazione viaggio", "travel insurance Italy".
- Do not use for choosing insurers (criteria only, no endorsements).

## Workflow

1. Needs by trip: medical (limits, USA multiplier), baggage, cancellation, sports.
2. Exclusions that bite: pre-existing, alcohol, off-piste, pandemics clauses — read first.
3. Claim: immediate notice + receipts + forms + deadlines.
4. Output: needs-matched checklist + questions for insurer.

## Rules

- Exclusions read BEFORE price comparison — stated as rule #1.
- EHIC vs policy split in EU: what each covers.
- No product endorsement.

## Examples

See `examples/viaggio-cases.md`. Coverage map in `references/coperture.md`.

## Edge cases

- Annual multi-trip vs single: math compared on user trips.
- Cruise/adventure extras: special riders flagged.
- Claim denied → motivi read + IVASS path mentioned.
