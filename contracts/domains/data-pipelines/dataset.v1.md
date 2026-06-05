# Dataset Contract v1

Contract ID: `universal.data.dataset.v1`

## Purpose

Describe a dataset or data release so agents can locate files, understand schema,
track lineage, and decide whether the data can be shared, visualized, uploaded,
or used for analysis.

## Applies To

- Tabular datasets
- Partitioned data lakes
- Feature sets
- Document, image, audio, and video collections
- Evaluation fixtures
- Exported application data

## Required Shape

A dataset descriptor should include:

- `schema`: `universal.data.dataset.v1`.
- `id`: stable dataset ID.
- `kind`: `dataset`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: project, version, and command or job.
- `contracts`: claimed contract IDs.
- `files`: roles such as `data`, `schema`, `metadata`, `manifest`,
  `checksums`, `preview`, or `license`.
- `format`: file format, encoding, compression, and partitioning.
- `records`: count, estimate, or explanation when count is unknown.
- `fields`: portable field descriptions or a reference to a schema file.
- `sources`: upstream datasets, streams, jobs, or external references.

## Recommended Fields

- `splits`: train, validation, test, holdout, or custom slices.
- `quality`: missingness, freshness, validation results, and known issues.
- `privacy`: sensitivity, retention, consent, and access constraints.
- `license`: usage license and attribution requirements.
- `versioning`: snapshot, partition, or changelog semantics.

## Extension Points

Projects may add domain-specific columns, feature statistics, geospatial
metadata, sensor calibration, or annotation details. Custom columns should be
declared in `fields` or a referenced schema.

## Invariants

- Generic consumers can locate dataset files and schemas through `files`.
- Field names, units, and meanings are not hidden in application code.
- Sources and licenses are explicit enough for sharing decisions.
- Unknown columns are additive unless a declared profile says otherwise.

## Validation Rules

- Resolve local file roles and schema references.
- Check that declared required files exist.
- Warn when fields lack units or descriptions for non-obvious values.
- Warn when privacy or license status is omitted for shareable datasets.

## Agent Implementation Notes

Use this contract as the handoff point between capture, pipelines, ML training,
visualization, upload, and analysis tools.

