# catalog/ — machine-readable index

- `skills.json` (v1.14.0, 271 entries: 247 ours + 24 vendors): source of truth for
  `skills/` + `vendors/` (name, path, description, license, compatibility;
  vendors carry `"origin"`). English.
- `vendors-manifest.json` (v1.14.0): pinned third-party sources (repo, commit,
  license, local path) + reference-only entries (Codex/Grok, no repo to pin).
- `../llms.txt` stays at root by agent convention and points here.
- `_registry.md`: unique-name registry, one name once (v3).

When adding a skill, update `skills.json`, `../llms.txt`,
`.claude-plugin/plugin.json`, `docs/COMPATIBILITY.md`, and regenerate
`docs/CATALOG.md` with `python scripts/build-catalog.py`.
