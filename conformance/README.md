# Conformance

Conformance should be small, local, and automatable.

## Recommended Validator Behavior

A validator should:

1. Load the root manifest.
2. Check the declared contract IDs.
3. Validate JSON files against known schemas when a schema is available.
4. Resolve relative paths and reject paths that escape the bundle root.
5. Check lifecycle consistency.
6. Check stream descriptors.
7. For JSONL streams, verify every non-empty line is a JSON object.
8. For binary indexed streams, verify index offsets and sizes against
   `payloads.bin`.
9. Check final stats when the lifecycle state is final.
10. Report unknown fields as warnings only when the contract allows extension.

## Conformance Levels

- `shape`: required files and JSON fields exist.
- `portable`: manifest paths resolve and generic consumers can discover known
  surfaces such as streams, datasets, artifacts, commands, models, routes, or
  services.
- `semantic`: lifecycle, timestamps, stream stats, references, offsets, and
  source relationships are coherent.
- `profile`: declared domain or project profiles validate successfully.
- `strict-project`: application-owned checks pass.
- `replay`: a consumer can replay or iterate known streams or event surfaces.
- `roundtrip`: a producer can write a fixture and a reader can consume it.

Validators should default to `shape` and `portable` checks and treat unknown
fields as extension data unless a declared profile closes the shape. See
`docs/extensibility-and-conformance.md`.

## Lightweight Repository Linting

This repository includes a linter for reference-system consistency:

```text
python3 scripts/lint_contracts.py
```

The linter checks:

- duplicate or missing contract IDs
- catalog entries that do not match contract files
- maturity metadata that references unknown contracts or domain packs
- invalid catalog maturity values
- catalog entries below the configured minimum maturity
- examples that reference unknown contract IDs
- snake_case field and column naming in examples
- UTC `*_at` timestamp strings and integer nanosecond timestamp fields
- section-shape drift as warnings

Regenerate the catalog after adding, removing, or renaming contracts:

```text
python3 scripts/generate_catalog.py
```

The linter is intentionally not a strict project validator. It protects
discoverability and consistency while leaving implementation-specific validation
to profiles and project-local tools.
