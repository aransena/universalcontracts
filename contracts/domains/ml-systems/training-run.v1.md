# ML Training Run Contract v1

Contract ID: `universal.ml.training_run.v1`

## Purpose

Describe a training, fine-tuning, or optimization run as a reproducible lifecycle
with inputs, outputs, metrics, logs, and derived model artifacts.

## Applies To

- Model training jobs
- Fine-tuning runs
- Hyperparameter trials
- Feature learning jobs
- Distillation, quantization, and adapter training

## Required Shape

A training run descriptor should include:

- `schema`: `universal.ml.training_run.v1`.
- `id`: stable run ID.
- `kind`: `training_run`, `fine_tuning_run`, `optimization_run`, or similar.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: training project, version, and command.
- `contracts`: claimed contract IDs.
- `lifecycle`: path to lifecycle descriptor or embedded lifecycle summary.
- `inputs`: datasets, model checkpoints, configs, seeds, and code references.
- `outputs`: model artifacts, checkpoints, logs, metrics, and reports.
- `parameters`: hyperparameters and runtime configuration.
- `metrics`: final or latest metrics with references to full metric streams.

## Lifecycle

Training runs compose `universal.core.lifecycle.v1`. Common states are:

```text
created -> prepared -> running -> closing -> closed
running -> failed
prepared -> cancelled
```

Long-running systems may add paused or checkpointed substates through a profile.

## Extension Points

Projects may add scheduler metadata, hardware topology, distributed training
details, experiment tracker IDs, feature store references, or optimizer-specific
fields. These should be declared through project-local schemas when they are
needed by downstream automation.

## Invariants

- Inputs and outputs are explicit enough to trace lineage.
- Final metrics correspond to a known checkpoint or model artifact.
- Failed runs keep enough metadata to explain failure and recover partial
  outputs when appropriate.
- User-editable notes do not overwrite producer-owned run metadata.

## Validation Rules

- Validate lifecycle finalization and timestamps.
- Resolve all local input and output paths.
- Check that output model artifacts claim compatible source references.
- Warn when metrics are present without units, split names, or dataset refs.

## Agent Implementation Notes

Use this contract when an agent needs to compare runs, reproduce a model, resume
from a checkpoint, or hand model outputs to evaluation and deployment tools.

