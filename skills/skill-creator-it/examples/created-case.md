# skill-creator-it worked case

## Request: "create skill to translate CSV"

Questions asked: name (`csv-translator`)? trigger? examples? scripts yes/no?
Answers: name ok, trigger "translate csv, localize table", example given, no scripts.

Files created:
- `skills/csv-translator/SKILL.md` from asset template (name == folder)
- `skills/csv-translator/references/columns.md` (headers preserved, encoding)
- `skills/csv-translator/examples/case.md` (3-line before/after)

Gates: `validate.py --skill csv-translator` OK, `security-check.py` clean,
`install.py --skill csv-translator --dest ./tmp-test --dry-run` ok.
Indexes: row in `catalog/skills.json`, `llms.txt`, `plugin.json`,
`docs/COMPATIBILITY.md`, regenerate `docs/CATALOG.md` (`build-catalog.py`),
`check-indexes.py` green. Final summary with commands run.
