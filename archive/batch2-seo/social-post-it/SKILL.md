---
name: social-post-it
description: Write per-channel social posts with hook and CTA. Use when asked social post, LinkedIn post, Instagram post, caption.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[topic/channel]"
user-invocable: true
disable-model-invocation: false
---

# Social Posts

One post per channel: strong hook, short body, single CTA.

## When to use

- "social post/LinkedIn/Instagram", "caption", "carousel".
- Do not use for long articles (see `blog-outline`).

## Workflow

1. Ask: channel, topic, goal (comments, clicks, followers).
2. Channel rules from `references/canali.md` (lengths, hashtags, tone).
3. Output: ready post + 2 alternative hooks + hashtags.
4. Carousel: 1 idea per slide, max 8.

## Rules

- Hook within first 2 lines (the rest hides behind "more...").
- 1 CTA per post, never two.
- Hashtags: max 5, relevant, never generic-only (`#love`).
- No emoji rain: max 3, functional.

## Examples

See `examples/social-cases.md`.

## Edge cases

- Same content multi-channel → rewrite per channel, not copy-paste.
- Serious topic → zero forced humor, sober tone.
- No real data → `[data]` placeholder, no invented numbers.
