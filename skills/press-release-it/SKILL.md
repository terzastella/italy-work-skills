---
name: press-release-it
description: Write press releases with journalistic structure. Use when asked press release.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[news]"
user-invocable: true
disable-model-invocation: false
---

# Press Release

Releases journalists use: news first, details after, real contacts.

## When to use

- "press release".
- Do not use for social posts or landings.

## Workflow

1. Ask: news (1 sentence), who/what/when/where/why, data, spokesperson, contacts.
2. Structure: Title → Subtitle → 5W lead (3 lines) → Body → Quote → Boilerplate → Contacts.
3. Max 1 page. 1 quote, real or `[to collect]`.
4. Ready output + send email subject (≤60 chars).

## Rules

- Lead with the 5Ws, no creative intros.
- Verified facts: dates, names, numbers only as provided.
- Company boilerplate max 3 lines, contacts with real name+phone/email.
- Never "market leader" without a source.

## Examples

See `examples/press-cases.md`. Checklist in `references/checklist.md`.

## Edge cases

- Weak news → advise against a release, propose post/blog.
- Missing data → draft with `[TODO]`, do not fantasize.
- Embargo → embargo date and time on top, clear.
