# catalog/ — machine-readable index

- `skills.json`: list of original skills in `../skills/` (name, path, description, compatibility). English.
- `vendors-manifest.json`: links to official skills only (url, license, install), no copies.
- `../llms.txt` stays at root by agent convention and points here.
- `_registry.md`: unique-name registry with per-category seats (bilingual notes ok).

When adding a skill, update `skills.json` (and `../llms.txt`).
