---
name: api-docs-it
description: Document endpoints and functions in English with call examples. Use when asked document API, API docs, endpoint documentation.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[file]"
user-invocable: true
disable-model-invocation: false
---

# API Docs

API docs that let you call it without reading the code.

## When to use

- "document API/endpoint/function", "API docs", "openapi".
- Do not use for general READMEs (see `readme-gen`).

## Workflow

1. Read handler/function: method, path, params, responses, errors.
2. Per item: purpose (1 line) + params (table) + request/response example + errors.
3. Technical names unchanged. Flag unvalidated params or unhandled errors as notes.
4. Document every endpoint with at least 1 copy-pasteable example.

## Output format

```markdown
### GET /users/{id}

Fetch a user.

Params: | Name | Where | Type | Required | Notes |
Example (bash): curl https://api.example.com/users/42
Response `200`, errors `404 user missing`.
```

## Rules

- Every endpoint has at least 1 copyable example.
- Errors documented with code + meaning, never just "error".
- Never invent endpoints not present in the code.

## Examples

See `examples/api-cases.md`. Table schema in `references/schema.md`.

## Edge cases

- Auth present → separate auth section with full header example.
- Pagination/filters → document defaults and limits.
- Code without validation → `[risk]` note instead of silence.
