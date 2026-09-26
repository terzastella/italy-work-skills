# Third-party notices

This repo contains original skills in `skills/` plus **pinned verbatim copies**
in `vendors/` (see `vendors/upstreams.lock.json` for repo + commit + license).
Files under `vendors/` are never hand-edited.

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

## Vendored copies (this repo, `vendors/`)

* `vendors/anthropics-skills/` — 10 skills from
  https://github.com/anthropics/skills at commit
  `33375500bcea98d610eb30ce10ac4e59b89c390d`, Apache-2.0.
  Per-skill `LICENSE.txt` kept in each folder (`doc-coauthoring` covered by
  the upstream README's Apache-2.0 statement). Excludes `docx/pdf/pptx/xlsx`
  (source-available, link only).
* `vendors/mattpocock-skills/` — 6 skills from `skills/engineering/` of
  https://github.com/mattpocock/skills at commit
  `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, MIT.
  License: `vendors/third-party/LICENSE-mattpocock.txt`.
* `vendors/superpowers/` — 8 skills from `skills/` of
  https://github.com/obra/superpowers at commit
  `8ca22dba9a94f28898bbce59f2537ff4d87c747d`, MIT.
  License: `vendors/third-party/LICENSE-superpowers.txt`.

When adding references to new third-party skills, add a row in
`../catalog/vendors-manifest.json` with url, commit-sha and license.
