# Smell → refactor step catalog

| Smell | Step type | Verify |
|-------|-----------|--------|
| Duplication | extract function | existing tests green |
| Function >50 lines | split in 2-3 | same outputs on cases |
| Vague names | local rename | grep usages updated |
| Params >4 | group into object | call sites updated |
| Silent try/except | log + re-raise | error test |
| Circular dependency | invert with interface | imports ok |

Order: breaking stuff first, then smelly stuff.
