# Artifact Contract v1

Contract ID: `universal.core.artifact.v1`

## Purpose

Describe derived outputs such as compressed media, remuxed video, model
inference, reports, indexes, plots, exports, or transformed datasets.

## Required Shape

Each derived artifact has an `artifact.json` descriptor:

- `schema`: `universal.core.artifact.v1`.
- `id`: stable artifact identifier.
- `kind`: artifact kind.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: tool, command, project, and version.
- `sources`: source bundle, stream, artifact, or file references.
- `files`: output file roles and relative paths.
- `status`: `ok`, `partial`, `failed`, or `unknown`.

## Recommended Fields

- `parameters`: options used to generate the artifact.
- `stats`: counts, bytes, duration, quality metrics.
- `errors`: structured errors or warnings.
- `reproducibility`: command and environment details.

## Extension Points

Projects may add artifact-kind-specific parameters, metrics, provenance,
compatibility, or runtime metadata. Extensions must not change the meaning of
`sources`, `files`, or `status`.

## Invariants

- Derived artifacts must not overwrite source data.
- Sources must be declared.
- Failed artifacts should keep enough metadata to explain the failure.
- Consumers should treat artifact files as immutable once status is `ok`.

## Validation Rules

- Resolve local file and source references.
- Warn when status is `ok` but declared files are missing.
- Warn when generated artifacts omit source references.
- Warn when failed artifacts omit error information.

## Agent Implementation Notes

Use this contract whenever an output is derived from another source. Preserve
source references and status semantics so downstream agents can decide whether
the artifact is usable.
