---
name: readme-gen
description: Generate READMEs from existing repos with standard structure. Use when asked create readme, missing readme, document project.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[folder]"
user-invocable: true
disable-model-invocation: false
---

# Readme Gen

Honest READMEs generated from real code, not imagination.

## When to use

- "create readme", "missing readme", "document project".
- Do not use for polishing existing READMEs (see `doc-polish-it`).

## Workflow

1. Inspect repo: folder structure, entrypoints, dependencies, scripts, license.
2. Extract only verified facts: commands that really exist, files that really exist.
3. Fill the template in `assets/readme-template.md`. Mark what you cannot find as `[TODO]`.
4. Show the README, do not write it without confirmation if one exists.

## Rules

- Zero invented commands: every cited command must exist in the repo.
- Zero invented badges (build/coverage) without real CI files.
- Visible placeholders `[TODO: description]`, never realistic-looking fake text.

## Examples

See `examples/readme-cases.md`.

## Edge cases

- Empty repo → skeleton + list of what is missing, not a fake full README.
- Existing README → ask overwrite/integrate, default integrate.
- Monorepo → root README + pointers, not one README for all detail.
