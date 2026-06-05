# ML Evaluation Report Contract v1

Contract ID: `universal.ml.evaluation_report.v1`

## Purpose

Describe an evaluation result for a model, pipeline, prompt, dataset, or service
so agents can compare quality, reproduce the evaluation, and route results to
dashboards or approval workflows.

## Applies To

- Offline model evaluations
- Benchmark runs
- Regression test reports
- Safety or bias assessments
- Human review summaries
- Production shadow evaluations

## Required Shape

An evaluation report descriptor should include:

- `schema`: `universal.ml.evaluation_report.v1`.
- `id`: stable report ID.
- `kind`: `evaluation_report`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: evaluation project and version.
- `contracts`: claimed contract IDs.
- `subject`: model, artifact, service, prompt, or pipeline being evaluated.
- `datasets`: datasets, slices, fixtures, or traffic samples used.
- `metrics`: named metric values with units, directions, and split or slice.
- `files`: roles such as `summary`, `records`, `confusion_matrix`, `plots`,
  `failures`, or `review_notes`.
- `status`: `ok`, `partial`, `failed`, or `unknown`.

## Recommended Fields

- `thresholds`: acceptance criteria and pass/fail status.
- `comparison`: baseline or previous report reference.
- `environment`: runtime, hardware, dependency, and seed details.
- `limitations`: caveats that affect interpretation.

## Extension Points

Metrics may include domain-specific fields, but each metric should keep a stable
name, value, unit or dimension, and direction such as `higher_is_better` or
`lower_is_better`.

## Invariants

- The evaluated subject is declared.
- Datasets or samples are identified enough for reproduction or audit.
- Metric values do not require a human to infer units or split names.
- Failed reports retain error information.

## Validation Rules

- Resolve local files and subject references.
- Check that metric names are stable strings and values are numeric or
  explicitly structured.
- Warn when metrics omit units, direction, or dataset slice.
- Warn when status is `ok` but summary files are missing.

## Agent Implementation Notes

Use this contract when deciding whether a model or service is ready for
deployment, regression comparison, visualization, or downstream analysis.

