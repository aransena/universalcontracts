# Annotation Set Contract v1

Contract ID: `universal.knowledge.annotation_set.v1`

## Purpose

Describe labels, highlights, spans, comments, entities, or review decisions over
documents, datasets, media, or conversations.

## Required Shape

An annotation set descriptor should include:

- `schema`: `universal.knowledge.annotation_set.v1`.
- `id`: stable annotation set ID.
- `kind`: `annotation_set`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: annotation tool, project, or reviewer source.
- `subjects`: documents, records, media, messages, or artifacts being annotated.
- `labels`: label schema, ontology, or guideline reference.
- `files`: annotation records, summary, conflicts, or review notes.
- `status`: draft, reviewed, approved, rejected, or unknown.

## Extension Points

Projects may add span formats, geometry, temporal ranges, adjudication,
confidence, annotator identity, or task assignment metadata.

## Invariants

- Annotation targets are resolvable.
- Label meanings are declared.
- Draft and approved annotations are distinguishable.
- User or reviewer identity policy is explicit when relevant.

## Validation Rules

- Resolve local subject, label, and annotation files.
- Warn when labels lack definitions.
- Warn when approved annotations include unresolved conflicts.

## Agent Implementation Notes

Use this contract for review workflows, supervised datasets, search enrichment,
and quality control.

