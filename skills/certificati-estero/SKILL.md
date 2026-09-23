---
name: certificati-estero
description: Guide legalization and apostille for use abroad. Use when asked legalizzazione, apostille, certificati estero.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[document/country]"
user-invocable: true
disable-model-invocation: false
---

# Certificati per l'Estero

Documents valid abroad: apostille vs legalization, sworn translations.

## When to use

- "legalizzazione", "apostille", "certificati estero".
- Do not use for immigration advice (see `permesso-soggiorno` for inbound).

## Workflow

1. Destination: Hague-convention country (apostille) vs other (legalization chain).
2. Steps: competent authority (prefettura/procura by document) + sworn translation where needed.
3. Timelines/costs with year; consulate role where applicable.
4. Output: path + offices + documents + warning on intermediaries' fees.

## Rules

- Hague list changes: verify destination status live, never from memory.
- Sworn translations (asseverazioni) via tribunale path explained.
- No "express" promises: timelines are ranges.

## Examples

See `examples/certificati-cases.md`. Path map in `references/percorsi.md`.

## Edge cases

- Non-Hague countries (e.g. many Arab states, China specifics) → full chain, extra time flagged.
- Old certificates → fresh issue usually required (3-6 month validity), state it.
- Urgent need → prefettura fast tracks where existing, no guarantees.
