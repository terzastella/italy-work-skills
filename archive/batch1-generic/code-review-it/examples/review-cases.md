# code-review-it cases

## Function with bug + secret

Input:
```python
def login(u, p):
    import requests
    r = requests.post(API, data={"u": u, "p": p}, verify=False)
    return r.json()["token"]
API = "https://api.example.com/login?key=DEMO"
```

Output:
```text
Verdict: BLOCKED (secret + disabled TLS)
[SEVERE] login:6 — hardcoded API key. Fix: move to env var.
[SEVERE] login:4 — verify=False disables TLS. Fix: remove, handle certificates.
[MEDIUM] login:5 — KeyError if response lacks token. Fix: .get + status check.
Top-3 fixes in impact order.
```

## Clean code

Output: `No significant issues. Optional: type hints on signature.`
