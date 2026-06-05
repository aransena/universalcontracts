# Pipeline Run Contract v1

Contract ID: `universal.data.pipeline_run.v1`

## Purpose

Describe a batch, streaming, or hybrid data pipeline execution with explicit
inputs, outputs, lifecycle, lineage, and validation results.

## Applies To

- ETL and ELT jobs
- Dataset exports
- Indexing jobs
- Feature generation
- Report generation
- Backfills and migrations

## Required Shape

A pipeline run descriptor should include:

- `schema`: `universal.data.pipeline_run.v1`.
- `id`: stable run ID.
- `kind`: `pipeline_run`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: pipeline project, version, and command.
- `contracts`: claimed contract IDs.
- `lifecycle`: path to lifecycle descriptor or embedded lifecycle summary.
- `inputs`: input datasets, streams, tables, files, or services.
- `outputs`: output datasets, artifacts, reports, or side effects.
- `parameters`: runtime options, partition ranges, and environment.
- `validation`: validation checks, conformance levels, and result files.

## Lifecycle

Pipeline runs compose `universal.core.lifecycle.v1`. Backfills and streaming jobs
may add checkpoints, watermarks, or paused states through a profile.

## Extension Points

Projects may add scheduler IDs, warehouse metadata, SQL text, DAG node records,
resource usage, retry history, or data quality profiles. These should not
replace the portable `inputs`, `outputs`, `parameters`, or `validation` fields.

## Invariants

- Inputs and outputs are explicit enough for lineage.
- Final states describe whether outputs are complete, partial, failed, or
  intentionally skipped.
- Validation results are linked rather than buried only in logs.
- Side effects are declared when outputs are not file-based.

## Validation Rules

- Validate lifecycle finalization.
- Resolve local inputs, outputs, and validation files.
- Warn when side effects are present without an external reference.
- Warn when a final successful run has no output references.

## Agent Implementation Notes

Use this contract when agents need to compare pipeline runs, debug data quality,
rerun a partition, or pass generated datasets to ML and visualization systems.

