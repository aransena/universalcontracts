# Document Corpus Contract v1

Contract ID: `universal.knowledge.document_corpus.v1`

## Purpose

Describe a collection of documents, metadata, schemas, extraction outputs, and
indexes for search, retrieval, analysis, or sharing.

## Required Shape

A document corpus descriptor should include:

- `schema`: `universal.knowledge.document_corpus.v1`.
- `id`: stable corpus ID.
- `kind`: `document_corpus`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: ingestion or curation project.
- `documents`: document manifests, paths, or collection references.
- `metadata`: corpus-level fields, ownership, license, and privacy notes.
- `indexes`: search, vector, graph, or lookup index references.
- `sources`: upstream repositories, exports, websites, or datasets.

## Extension Points

Projects may add taxonomy, deduplication, chunking, OCR, embeddings,
permissions, or domain-specific metadata.

## Invariants

- Documents are discoverable through manifest references.
- Source and license status are explicit for sharing decisions.
- Indexes declare what corpus version they cover.
- Sensitive document classes are marked.

## Validation Rules

- Resolve local document and index references.
- Warn when license or privacy status is missing.
- Warn when indexes omit source corpus version.

## Agent Implementation Notes

Use this contract for retrieval, document QA, corpus exports, and downstream
analysis.

