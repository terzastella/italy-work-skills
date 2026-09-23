---
name: meta-tags
description: Generate optimized title and meta descriptions with right lengths. Use when asked meta tags, SEO title, meta description.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[page/keyword]"
user-invocable: true
disable-model-invocation: false
---

# Meta Tags

Titles + descriptions that earn clicks: keyword up front, right length, no truncation.

## When to use

- "meta tags", "SEO title", "meta description", "snippet".
- Do not use for full audits (see `seo-audit`).

## Workflow

1. Ask: page/content, main keyword, tone (default informative).
2. Generate 3 titles + 3 descriptions. Format below with char counts.
3. Length rules: title ≤60, description 140-160. See `references/limits.md`.

## Output format

```text
Title 1 (54): <text with keyword>
Title 2 ...
Description 1 (152): <text with benefit + CTA>
...
Recommended: Title 2 + Description 1 (why: ...)
```

## Rules

- Main keyword within first 5 title words.
- Description with benefit + verb, never keyword only.
- No false clickbait: what you promise is on the page.

## Examples

See `examples/meta-cases.md`.

## Edge cases

- Multiple keywords → 1 primary per snippet, rest in body (see `keyword-map`).
- Brand to include → trailing `| Brand`, never first.
- Special chars/emoji → only if the brand already uses them, never by default.
