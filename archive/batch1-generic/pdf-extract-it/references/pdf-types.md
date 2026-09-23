# PDF types — how to recognize them

| Type | Signal | Strategy |
|------|--------|----------|
| Native | selectable text | direct extraction + tables |
| Scan | pages = images | OCR, mark doubts `[p. N?]` |
| Mixed | some pages text | page by page, declare type |
| Form | fillable fields | list fields:values |
| Encrypted | asks password | ask, do not bypass |

Quick check: try copying 2 lines. If they paste → native.
