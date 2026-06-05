# File Upload Contract v1

Contract ID: `universal.app.file_upload.v1`

## Purpose

Describe user or system file upload surfaces, validation, storage, processing,
security, and lifecycle behavior.

## Required Shape

A file upload descriptor should include:

- `schema`: `universal.app.file_upload.v1`.
- `id`: stable upload surface ID.
- `kind`: `file_upload`.
- `subject`: route, API, form, job, integration, or storage boundary accepting
  uploads.
- `inputs`: accepted file roles, media types, size limits, metadata, and sources.
- `storage`: bucket, prefix, database, filesystem, object layout, and retention.
- `validation`: type checks, virus scanning, checksum, dimensions, schema, and
  content rules.
- `processing`: thumbnailing, extraction, transcoding, indexing, or workflow
  steps.
- `security`: auth, permissions, signed URLs, privacy, access, and deletion
  behavior.

## Extension Points

Projects may add multipart upload details, client-side preflight, resumable
uploads, media processing queues, moderation, or provider-specific metadata.

## Invariants

- Accepted file types and limits are explicit.
- Uploaded bytes are not trusted until validation completes.
- Storage paths and access rules are discoverable.
- Processing outputs link to source files and provenance.

## Validation Rules

- Resolve route, API, form, object store, media, and processing references.
- Warn when upload surfaces omit size or type limits.
- Warn when uploaded files lack access or deletion behavior.
- Warn when derived media omit provenance links.

## Agent Implementation Notes

Use this contract before adding uploads, attachment handling, media ingestion,
document import, avatar storage, or user-generated files.
