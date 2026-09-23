# Reusable prompt patterns

| Pattern | Use | Variables |
|---------|-----|-----------|
| Instructor | explain/do step by step | `{{topic}}`, `{{level}}` |
| Reviewer | review with severity | `{{text}}`, `{{criteria}}` |
| Translator | faithful EN/IT | `{{text}}`, `{{direction}}` |
| Extractor | extract fields | `{{text}}`, `{{fields}}` |
| Planner | step plans | `{{goal}}`, `{{constraints}}` |

Every prompt: role + `{{variables}}` + numbered instructions + format + example.
1 task per prompt. Real example always.
