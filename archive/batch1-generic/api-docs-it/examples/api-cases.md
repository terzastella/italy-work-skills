# api-docs-it cases

## Endpoint with auth and pagination

Input (code): `GET /orders?page&limit` with `X-Key` header, 401/422 errors.

Output:
```markdown
### GET /orders

List orders, paginated.

## Authentication
`X-Key: <key>` on every call.

| Name | Where | Type | Required | Default | Notes |
|------|-------|------|----------|---------|------|
| page | query | int | no | 1 | min 1 |
| limit | query | int | no | 20 | max 100 |

Example (bash):
    curl -H "X-Key: $KEY" "https://api.example.com/orders?page=2"

| Code | When | Body |
|------|------|------|
| 200 | ok | `{orders: [...], total: 140}` |
| 401 | missing key | `{error: "unauthorized"}` |
| 422 | limit>100 | `{error: "limit max 100"}` |
```
