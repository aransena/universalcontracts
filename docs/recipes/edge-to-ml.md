# Recipe: Edge Device to ML Model

## Flow

```text
edge device -> telemetry/control -> recording bundle -> dataset -> training run -> model artifact -> evaluation report
```

## Contracts

- `universal.edge.board_target.v1`
- `universal.edge.firmware_project.v1`
- `universal.edge.telemetry_control.v1`
- `universal.capture.recording_bundle.v1`
- `universal.core.stream.v1`
- `universal.data.dataset.v1`
- `universal.data.pipeline_run.v1`
- `universal.ml.training_run.v1`
- `universal.ml.model_artifact.v1`
- `universal.ml.evaluation_report.v1`

## Interoperability Handoff

1. Edge telemetry declares timestamps, units, buffering, and message schemas.
2. Recording bundles preserve streams and payload indexes.
3. Dataset descriptors declare fields, sources, privacy, and checksums.
4. Training runs reference datasets, parameters, lifecycle, and outputs.
5. Model artifacts and evaluation reports preserve downstream compatibility.

## Agent Notes

Do not collapse sensor-specific fields into undocumented columns. Add them to
field dictionaries, stream descriptors, or project-local profiles.

