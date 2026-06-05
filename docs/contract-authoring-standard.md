# Contract Authoring Standard

Universal Contracts are agent-facing references. Each contract should be easy to
scan, compose, and validate at a lightweight level.

## Canonical Sections

New contracts should use these sections in order:

1. `Purpose`
2. `Applies To`
3. `Composes`
4. `Required Shape`
5. `Extension Points`
6. `Lifecycle`
7. `Invariants`
8. `Conformance Levels`
9. `Validation Rules`
10. `Minimal Example`
11. `Agent Implementation Notes`

Sections may be omitted only when they do not apply. For example, a static
descriptor can omit `Lifecycle`, but it should still explain finality or status
when outputs can be partial or failed.

## Required Header

Every contract file must start with:

```text
# Contract Name v1

Contract ID: `universal.<area>.<name>.v1`
```

The filename should use kebab-case, while the contract ID uses snake_case for
the contract name:

```text
contracts/domains/web-apps/api-client.v1.md
Contract ID: `universal.web.api_client.v1`
```

## Contract Shape

Contracts should describe the portable spine rather than every implementation
detail. The `Required Shape` section should identify the files, fields,
messages, endpoints, or descriptors another project can rely on for discovery,
handoff, validation, and integration.

Project-specific detail belongs in:

- additive fields
- local schemas
- declared profiles
- example manifests
- implementation briefs

## Maturity

Catalog maturity values:

- `draft`: exploratory; names and fields can change.
- `candidate`: useful for early adopters; breaking changes should be rare.
- `stable`: safe for broad use; breaking changes require a new version.
- `deprecated`: retained for compatibility; replacement should be listed.

Published catalog entries should be `candidate` or above. Exploratory contracts
may start as `draft` in work-in-progress branches, but they should not be
published in `contracts/catalog.json` until they pass the candidate gate.

## Promotion Gates

Promote maturity in `contracts/maturity.json`, not by editing generated catalog
output directly.

To publish at `candidate`, a contract should have:

- canonical sections with no linter warnings
- at least one of: a representative example, a guide entry, or a recipe entry
- clear extension points and validation rules
- no known contradiction with the shared field dictionary
- a promotion reason in `contracts/maturity.json`

To promote from `candidate` to `stable`, a contract should also have:

- multiple real or representative examples
- settled field names and portable meanings
- schema support where machine validation is useful
- successful use across at least two independent project styles or profiles
- migration notes for any known breaking changes

## Standardization Policy

Older first-pass contracts may not yet use every canonical section. The linter
warns about section drift so authors can improve consistency over time without
blocking exploratory work.
