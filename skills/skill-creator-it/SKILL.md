---
name: skill-creator-it
description: Create new English skills following this repo's standard. Use when asked to create skill, new skill, skill scaffolding, skill template.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "<skill-name>"
user-invocable: true
disable-model-invocation: false
---

# Skill Creator

Generates the scaffolding of a new English skill following the `agentskills.io`
standard and this repo's conventions.

## When to use

- "create skill ...", "new skill for ...", "skill scaffolding".
- Do not use for editing existing skills (edit directly).

## Workflow

1. Ask (if missing): hyphen-case name, what it does in 1 sentence, trigger
   ("Use when..."), good/bad examples, scripts needed (yes/no).
2. Create `skills/<name>/SKILL.md` from `assets/template-SKILL.md`
   (name == folder, description with what+when).
3. Add minimum depth: 1 reference in `references/` or 1 example in
   `examples/` (see `references/spec-checklist.md`).
4. Validate: `python scripts/validate.py --skill <name>` must pass.
   If `name != folder` or body <20 chars, fix before continuing.
5. Dry-run install test:
   `python scripts/install.py --skill <name> --dest ./tmp-test --dry-run`
6. Update indexes: `catalog/skills.json`, `llms.txt`,
   `.claude-plugin/plugin.json`, tables in `README.md` and `docs/COMPATIBILITY.md`.
7. Show summary: files created + commands run + next steps.

## Rules

- English, sober tone, no emoji.
- Max ~500 lines per `SKILL.md` (spec year-stated: agentskills.io). Details in `references/`, code in `scripts/`.
- Never secrets, tokens, PII, personal absolute paths in generated files.
- Never `git commit/push`, never publish to marketplaces (local-only repo).

## Examples

User: `create skill csv-translator`
Reply: asks trigger + examples, then creates `skills/csv-translator/SKILL.md`
with description `Translate CSV headers EN/ES preserving structure. Use when asked
translate csv, localize table.`, reference with 2 examples, validates and summarizes.

## Edge cases

- Non hyphen-case name (`My Skill!`) → propose `my-skill`, ask confirmation.
- Duplicate skill (folder exists) → do not overwrite, propose `extend <name>`.
- Vague request ("skill for everything") → ask 1 concrete use case + 1 example.
