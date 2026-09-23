# prompt-pack-it cases

## Reusable reviewer prompt

User input: "prompt to review emails".

Pack:
```text
# Email Reviewer
Role: sober English reviewer
Input: {{email}}
Instructions:
1. Flag tone, typos, structure
2. Propose corrected version
Output: issue list + corrected text
Example: [sample data] input→output
```

Test: applied to sample email, simulated output shown, ambiguities fixed.

## Vague request (blocked)

Input: "make me a prompt for everything".
Output: `Tell me 1 task + 1 real example, then I build the pack.` — never a generic pack.
