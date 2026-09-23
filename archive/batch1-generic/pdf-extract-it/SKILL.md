---
name: pdf-extract-it
description: Extract text and tables from PDFs, native or scanned. Use when asked extract PDF, read PDF, text from PDF, PDF tables.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Bash
argument-hint: "[file.pdf]"
user-invocable: true
disable-model-invocation: false
---

# PDF Extract

From PDF to usable text: first understand which PDF it is, then pick the right tool.

## When to use

- "extract PDF", "read PDF", "text from PDF", "PDF tables", "merge PDFs".
- Do not use for creating PDFs.

## Workflow

1. Check: native PDF (selectable text) or scan (images)?
2. Native → text + table extraction in markdown, page by page.
3. Scan → declare OCR limits, extract what is readable, flag dubious pages.
4. Output: clean text + source note (`file.pdf` p. N). Never invent missing content.
5. Tables → markdown with headers; if unreadable, describe structure instead of inventing cells.

## Rules

- Never fill missing cells or sentences: mark `[unreadable p. N]`.
- Max ~50 pages per pass; beyond that, split into blocks.
- Respect copyright: short excerpts ok, no full book reproduction.

## Examples

See `examples/extract-cases.md`. PDF types in `references/pdf-types.md`.

## Edge cases

- Encrypted PDF → ask for password, do not bypass protections.
- Image-only PDF without OCR → extract metadata + structure, declare limit.
- Fillable forms → list fields and values, do not "fill in" without confirmation.
