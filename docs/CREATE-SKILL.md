# Creating a new skill

## 1. Copy the template

```bash
cp -r templates/skill-starter skills/my-skill
```

## 2. Spec rules (agentskills.io)

- Folder `skills/my-skill/` with mandatory `SKILL.md`.
- Frontmatter: `name` (hyphen-case, == folder name, max 64) + `description`
  (what it does + when to use it, max 1024). Recommended: `license`,
  `compatibility`, `metadata: {author, version, lang}`.
- Body: operative instructions + examples + edge cases. Max ~500 lines,
  ~5000 tokens recommended. Details in `references/`, code in `scripts/`,
  templates in `assets/`.
- Paths relative to the skill root in references.

## 3. Our checklist

- [ ] `name` == folder
- [ ] `description` contains trigger ("Use when...")
- [ ] Good + bad example
- [ ] No secrets, no personal absolute paths
- [ ] `python scripts/validate.py --skill my-skill` green
- [ ] Install test: `python scripts/install.py --skill my-skill --dest ./tmp-test --all`
- [ ] Add row to `README.md`, `catalog/skills.json`, `llms.txt`

## 4. Multi-agent fields

Copy the superset frontmatter from the template: works on Claude/Codex/Grok/Cursor
unmodified. `allowed-tools` Claude only, `argument-hint/user-invocable`
Grok only — others ignore them without errors.

## 0. Language rule (locked, option A)

- Skill content: **English only** (instructions, references, examples, scripts).
  Frontmatter `metadata lang: "en"`.
- Italian survives only as **domain artifact**: invoice bodies, email bodies,
  formulas, VAT rates, AdE/INPS references, legal wording.
- Only `README.md` stays in Italian. Everything else (docs, catalog, scripts) in English.
- Rationale: agents trigger and marketplaces work in English; Italian users are
  served through Italian outputs, not Italian instructions.
