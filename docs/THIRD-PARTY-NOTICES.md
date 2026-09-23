# Third-party notices

This repo contains ONLY original skills. Official skills are referenced
(not copied) in `../catalog/vendors-manifest.json`.

## Anthropic — anthropics/skills

* Repo: https://github.com/anthropics/skills
* Spec: https://agentskills.io/specification
* License: Apache-2.0 for most example skills
  (frontend-design, skill-creator, mcp-builder, webapp-testing, etc.)
* Exception: `skills/docx`, `skills/pdf`, `skills/pptx`, `skills/xlsx`
  powering Claude's document features are **source-available,
  not open-source**. Do not copy them into this repo, link only.
* Allowed use: `/plugin marketplace add anthropics/skills`

## OpenAI — Codex / ChatGPT

* Docs: https://developers.openai.com/codex/skills
* Skills path: `.agents/skills/` (repo/user/admin/system)
* Reusable distribution: via Plugin (bundle of skill + app/MCP)
* Note: Custom GPTs in ChatGPT retiring (no new 25/09/2026,
  execution stops 11/12/2026 for Enterprise, then Free/Plus/Pro).
  Migration to Plugins. See `CHATGPT-MIGRATION.md`.

## xAI — Grok

* Docs: https://docs.x.ai/build/features/skills-plugins-marketplaces.md
  and https://x.ai/news/grok-skills
* Skills path: `./.grok/skills/`, `~/.grok/skills/`, plugin `skills/`
* Declared compatibility: also reads `.claude/`, `.agents/skills/`, `AGENTS.md`
* Built-in: Word, Presentations, Spreadsheets, PDFs, Skill Creator (no setup)

When adding references to new third-party skills, add a row in
`../catalog/vendors-manifest.json` with url, commit-sha and license.
