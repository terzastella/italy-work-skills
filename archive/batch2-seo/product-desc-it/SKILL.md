---
name: product-desc-it
description: Write product pages selling benefits with real specs. Use when asked product description, product page, ecommerce copy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[product]"
user-invocable: true
disable-model-invocation: false
---

# Product Pages

Product pages: benefits up top, real specs below, zero fluff.

## When to use

- "product description", "product page", "ecommerce copy".
- Do not use for full landings (see `landing-copy`).

## Workflow

1. Ask: product, audience, 3 real specs, price (if needed), differentiator.
2. Structure: Name+benefit 1 line → 3 benefits → specs (table) → contents/usage → CTA.
3. Max 150 words + table.

## Rules

- Benefits with measure when possible ("10 minutes" not "super fast").
- Specs only as provided: never invent materials, sizes, certifications.
- Reviews only real or `[review to collect]`.
- Prices only if provided.

## Examples

See `examples/product-cases.md`. Schema in `references/schema.md`.

## Edge cases

- Boring product → usage angle ("for whom, when"), not adjectives.
- Missing specs → short honest table + `[TODO]`.
- Competitor comparison → verifiable facts, never disparage.
