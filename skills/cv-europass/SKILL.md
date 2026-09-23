---
name: cv-europass
description: Build Europass CVs with measured experience and clean layout. Use when asked CV, curriculum, europass, resume Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[profile]"
user-invocable: true
disable-model-invocation: false
---

# Europass CV

CVs recruiters finish: 1-2 pages, measured results, zero filler.

## When to use

- "CV", "curriculum", "europass", "resume" (Italy/EU).
- Do not use for cover letters (see `lettera-presentazione`).

## Workflow

1. Ask: experience (roles, dates, results), education, skills, languages with levels, target role.
2. Structure: header + profile 2 lines + experience (reverse order, bullets with measures) + education + skills + languages.
3. Rule: <10 years → 1 page; every bullet starts with an action verb + number where possible.
4. Output full CV draft + "to strengthen" list (missing numbers, gaps to explain).

## Rules

- Never invent jobs, dates, degrees, languages: `[TODO]` for missing.
- Photo: mention it is optional (anti-discrimination note), do not require it.
- No lies by design: duties described, not inflated.

## Examples

See `examples/cv-cases.md`. Europass sections in `references/europass.md`.

## Edge cases

- Career gaps → 1 honest line (e.g. family, study), no fake freelancing.
- First job → education + projects + internships first, 1 page.
- Overqualified → tailor to the ad, cut unrelated seniority (say so openly).
