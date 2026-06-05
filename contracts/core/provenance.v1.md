# Provenance Contract v1

Contract ID: `universal.core.provenance.v1`

## Purpose

Describe origin, lineage, transforms, checksums, and reproducibility metadata for
files, datasets, artifacts, models, reports, and releases.

## Required Shape

A provenance descriptor should include:

- `schema`: `universal.core.provenance.v1`.
- `id`: stable provenance record ID.
- `kind`: `provenance`.
- `subject`: artifact, dataset, bundle, service, or release being described.
- `sources`: upstream files, datasets, streams, artifacts, commits, services, or
  external references.
- `transforms`: commands, jobs, tools, parameters, and environment references.
- `checksums`: content hashes or integrity metadata where available.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: project, version, and command.

## Extension Points

Projects may add supply-chain attestations, SBOM references, experiment tracker
IDs, signing metadata, or external catalog IDs. These should complement, not
replace, portable source and transform fields.

## Invariants

- Sources are explicit enough for audit or reproduction.
- Checksums identify content rather than only filenames when integrity matters.
- Transform metadata distinguishes user parameters from derived values.
- External references identify their authority or namespace.

## Validation Rules

- Resolve local sources and checksum files.
- Check that checksums use declared algorithms.
- Warn when generated artifacts lack source references.
- Warn when reproducibility depends on undeclared environment details.

## Agent Implementation Notes

Use this contract across capture, data, ML, deployment, release, document, and
media workflows.

