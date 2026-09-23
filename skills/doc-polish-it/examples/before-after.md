# doc-polish-it before/after example

## Before

```text
# stuff
fixed various bug. see here https://...
Use like this: python scripts/install.py --all (does everything)
```

Problems: vague title, past tense, bare link, command without context,
generic "does everything".

## After

```markdown
# Universal installer

Copies `skills/*` to the folders agents read.

## Usage (bash):

    python scripts/install.py --all --dest ./tmp-test --dry-run

See `scripts/install.py` for per-agent destinations.
```

## What changed

- Specific title instead of "stuff"
- Active voice + imperative
- Command with context in `bash` code block
- Backtick paths
- Removed generic "does everything"
