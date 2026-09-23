---
name: seo-audit
description: On-page SEO audits with ordered issues and fixes. Use when asked SEO audit, SEO check, optimize page, on-page SEO.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[url or file]"
user-invocable: true
disable-model-invocation: false
---

# SEO Audit

Concrete on-page audits: what blocks ranking and how to fix it, in order.

## When to use

- "SEO audit", "SEO check", "optimize page", "why doesn't it rank".
- Do not use for content strategy (see `content-gap`, `keyword-map`).

## Workflow

1. Analyze: title, meta description, H1/H2, URL, images (alt), internal links, stated speed, mobile.
2. Issues ordered by impact with 1-line fix (format below).
3. Close with /100 score and top-3 priorities.

## Output format

```text
Score: <n>/100
[BLOCKER] <item> — <issue>. Fix: <1 line>
[MEDIUM] <item> — <issue>. Fix: <1 line>
[MINOR] <item> — <issue>. Fix: <1 line>
Top-3: <in order>
```

## Rules

- Max 12 issues, impact first.
- Every fix copy-pasteable or immediately actionable, never generic "improve SEO".
- Never guarantee rankings ("#1 on Google"): probabilities and priorities only.

## Examples

See `examples/audit-cases.md`. Item checklist in `references/checklist.md`.

## Edge cases

- No site access (URL only) → audit from visible + `[verify in Search Console]` tag.
- New site without traffic → technical focus (indexing), not keywords.
- Internal duplicate content → flag canonicals, do not rewrite everything here.
