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
- `semantic`: lifecycle, timestamps, stream stats, and references are coherent.
- `replay`: a consumer can replay or iterate known streams.
- `roundtrip`: a producer can write a fixture and a reader can consume it.

