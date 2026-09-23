# systematic-debug cases

## Crash with traceback

Input:
```text
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    load("data.csv")
FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
```

Output:
```text
Reproduction: python app.py → FileNotFoundError data.csv
Isolation: line 12, relative path depends on cwd
Root cause: file is looked up in cwd instead of script folder
Fix: absolute path from __file__ | Verify: run from another folder
```

## Intermittent error

Output: declare intermittence + `add timestamped logging and seed, rerun 5 times`.
Never a final fix without stable reproduction.
