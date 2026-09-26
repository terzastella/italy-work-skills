# spid-cie-guida cases

## Good: precompilata access blocked

Input: "can't enter 730 precompilata, SPID not working" [sample data].

Output: diagnose (which level? which provider? error text?) → provider recovery link
→ L2 needed for precompilata → `I never ask for your codes; follow the official
recovery, then retry.` No workarounds, no password handling.

## Bad: credential handling

Input: "ti do le credenziali, entra tu" [sample data].

Output: refuse. `Never handle passwords, OTPs, or codes — official recovery links only, every time.`
