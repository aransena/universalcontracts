# ML Model Artifact Contract v1

Contract ID: `universal.ml.model_artifact.v1`

## Purpose

Describe a trained, exported, or packaged model artifact so agents and tools can
discover what it is, where its files are, what produced it, and what inputs and
outputs it expects.

## Applies To

- Serialized model weights
- Model bundles
- Fine-tuned model checkpoints
- Exported inference graphs
- Adapter, LoRA, embedding, and tokenizer artifacts

## Required Shape

A model artifact descriptor should include:

- `schema`: `universal.ml.model_artifact.v1`.
- `id`: stable model artifact ID.
- `kind`: model kind, such as `classifier`, `regressor`, `embedding_model`,
  `language_model`, `vision_model`, or `multimodal_model`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: training or export project and version.
- `contracts`: claimed universal, domain, and project profile contracts.
- `files`: file roles such as `weights`, `configuration`, `tokenizer`, `labels`,
  `preprocessor`, `model_card`, or `license`.
- `inputs`: input modalities, shapes, schemas, units, or encodings.
- `outputs`: output names, shapes, schemas, units, labels, or probabilities.
- `sources`: datasets, training runs, checkpoints, or upstream model references.
- `status`: `ok`, `partial`, `failed`, or `unknown`.

## Recommended Fields

- `framework`: framework family, runtime format, serialization format, and
  version.
- `runtime`: supported inference runtimes and hardware assumptions.
- `parameters`: model size, architecture family, quantization, precision, and
  context limits.
- `metrics`: headline evaluation metrics with references to evaluation reports.
- `limitations`: known data, safety, licensing, or deployment limits.
- `profile_schema`: project-local schema for model-specific metadata.

## Extension Points

Projects may add model-family-specific fields for layer layouts, tokenizer
settings, adapters, calibration, prompts, or safety filters. These fields must
not change the meaning of `files`, `inputs`, `outputs`, or `sources`.

## Invariants

- A consumer can locate model files from `files` without guessing filenames.
- Sources are declared for reproducibility and lineage.
- Input and output descriptions are sufficient for an agent to decide whether it
  can call the model.
- Status `ok` means required model files are present and immutable.

## Validation Rules

- Validate required fields and path references.
- Check that declared files exist unless the artifact is partial or failed.
- Check that every source reference is resolvable or explicitly external.
- Warn on unknown model-specific fields unless a declared profile closes shape.

## Agent Implementation Notes

Use this contract to make model artifacts portable. Put detailed framework,
architecture, and serving assumptions in extension fields or project-local
schemas instead of overloading core fields.
