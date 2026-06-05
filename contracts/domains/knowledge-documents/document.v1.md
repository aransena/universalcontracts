# Document Contract v1

Contract ID: `universal.knowledge.document.v1`

## Purpose

Describe one document and its content, metadata, derived text, attachments,
annotations, and provenance.

## Required Shape

A document descriptor should include:

- `schema`: `universal.knowledge.document.v1`.
- `id`: stable document ID.
- `kind`: `document`.
- `created_at`: ISO 8601 UTC timestamp for descriptor creation or ingestion.
- `producer`: ingestion or authoring project.
- `files`: original, text, metadata, preview, attachment, or checksum roles.
- `format`: MIME type, encoding, language, and version when known.
- `metadata`: title, authors, original publication dates, source, license, and
  privacy notes.
- `sources`: upstream URL, file, repository, or export reference.

## Extension Points

Projects may add OCR data, layout, chunks, embeddings, citations, signatures,
classification labels, or domain metadata.

## Invariants

- Original and derived files are distinguishable.
- Text extraction does not replace source provenance.
- Sensitive and licensed content is marked.
- Generic tools can find a readable representation when available.

## Validation Rules

- Resolve local file references.
- Warn when derived text lacks source reference.
- Warn when document format or license is missing.

## Agent Implementation Notes

Use this contract when ingesting, transforming, citing, reviewing, or sharing
documents.
