---
name: doc-polish-it
description: Improve READMEs and docs with sober tone, structure and correct code blocks. Also translates IT to EN. Use when asked to improve docs, rewrite readme, fix text, polish docs.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[file.md]"
user-invocable: true
disable-model-invocation: false
---

# Doc Polish

Improves technical documentation without distorting it. Sober tone, correct code blocks.

## When to use

- "improve readme", "rewrite docs", "fix text", "polish docs", "translate IT to EN".
- Do not use for code, only markdown/text.

## Workflow

1. Read the whole target file. If >300 lines, work per section.
2. Apply the checklist in `references/checklist.md`. For new READMEs use `assets/template-readme.md`.
3. Output: either patch the file (if edit requested) or rewritten text in a code block.
4. End with a bullet list "What changed" (max 8 items).
5. Never add emoji, badges, marketing unless requested.
6. Worked example: see `examples/before-after.md`.

## Rules

- Single H1, H2/H3 hierarchy without jumps.
- Sentences <25 words, active voice, imperative for instructions.
- Code blocks always with language (`bash`, `python`, ...) — year-stated tool versions where relevant.
- Paths/files in backticks, e.g. `skills/invoice-it/SKILL.md`.
- For IT→EN translation: keep structure and code unchanged, translate prose only.
- Broken links or `<your-username>` placeholders -> flag, do not invent URLs.

## Examples

Input:
```text
# stuff
fixed various bug. see here https://...
```

Output:
```markdown
# Clear title

What it does in 2 lines.

## Install
...
```

+ `What changed: title, structure, code blocks...`

## Edge cases

- Missing file -> ask for correct path, do not create from scratch.
- Text with secrets -> do not repeat them, flag and redact.
- Translation request -> structure and code unchanged, prose only.
