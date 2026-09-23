# Test frameworks — how to generate

| Framework | File | Command | Note |
|-----------|------|---------|------|
| pytest | `test_<mod>.py` | `pytest -q` | `tmp_path` for files |
| unittest | `test_<mod>.py` | `python -m unittest` | `TestCase` + `setUp` |
| node:test | `*.test.js` | `node --test` | `assert/strict` |

If unknown: ask before generating. Never mix frameworks in one repo.
Mock only external I/O (`requests`, fs, db). Names: `test_<fun>_<case>`.
