# source-cite cases

## Web quote verification

Input: text with "the standard allows max 64 chars (agentskills.io)".

Output:
```text
[1] Agent Skills. Specification. agentskills.io, 2026. <https://agentskills.io/specification>
    Supports: name max 64, lowercase+hyphen
Status: verified
```

## Dead link

Output: `[2] Rossi Blog. Skills guide. Blog, 2024. [dead link, verified on 23/09/2026]
Replaced with: [3] Official docs...` — never an invented link instead.
