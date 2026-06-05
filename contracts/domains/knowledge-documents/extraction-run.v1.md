# Extraction Run Contract v1

Contract ID: `universal.knowledge.extraction_run.v1`

## Purpose

Describe an OCR, parsing, chunking, metadata extraction, entity extraction, or
embedding run over documents.

## Required Shape

An extraction run descriptor should include:

- `schema`: `universal.knowledge.extraction_run.v1`.
- `id`: stable extraction run ID.
- `kind`: `extraction_run`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: extractor project and version.
- `inputs`: documents, corpus, parameters, prompts, or schemas.
- `outputs`: extracted text, chunks, metadata, embeddings, annotations, or logs.
- `lifecycle`: run state and timestamps.
- `quality`: confidence, errors, warnings, or coverage metrics.

## Extension Points

Projects may add model references, OCR engine data, parser versions,
normalization rules, or human review status.

## Invariants

- Extracted outputs point back to source documents.
- Parameters and extractor version are recorded.
- Confidence and errors are preserved when available.
- Failed runs keep enough detail to retry or inspect.

## Validation Rules

- Resolve local input and output references.
- Warn when outputs lack source document IDs.
- Warn when extraction quality is undocumented.

## Agent Implementation Notes

Use this contract for reproducible text extraction, indexing, and document
analysis pipelines.

