---
name: landing-copy
description: Write landing page copy with ordered sections and CTAs. Use when asked landing page, landing copy, site copy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[product/audience]"
user-invocable: true
disable-model-invocation: false
---

# Landing Copy

Landing pages that convert: 1 promise, proof, 1 action.

## When to use

- "landing page", "landing copy", "site/product copy".
- Do not use for articles (see `blog-outline`).

## Workflow

1. Ask: product, audience, action (just one), proof (data/testimonials).
2. Fixed sections: Hero (H1+sub+CTA) → Benefits (3) → How it works (3 steps) → Proof → FAQ (3) → Final CTA.
3. Max 60 words per section. Same CTA everywhere.
4. Ready output + note on what is missing (screenshots, pricing, testimonials).

## Rules

- 1 action per page, never "buy or contact or subscribe".
- Benefits > features ("save 2h" not "advanced dashboard").
- No invented testimonials: `[testimonial]` placeholder if missing.
- Pricing only if provided, never invented "from" prices.

## Examples

See `examples/landing-cases.md`. Section order in `references/sections.md`.

## Edge cases

- No proof/data → honest hero + "discovery" CTA, no fake numbers.
- Multiple audiences → 1 landing per audience, not all together.
- High price → objections section before CTA.
