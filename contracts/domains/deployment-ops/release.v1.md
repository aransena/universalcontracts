# Release Contract v1

Contract ID: `universal.ops.release.v1`

## Purpose

Describe a versioned releasable package, artifact set, image, model, plugin, or
service build.

## Required Shape

A release descriptor should include:

- `schema`: `universal.ops.release.v1`.
- `id`: stable release ID.
- `kind`: `release`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: build or release project and command.
- `version`: release version, tag, commit, or build number.
- `artifacts`: packages, images, binaries, schemas, model files, or manifests.
- `provenance`: source, build, checksums, signatures, or SBOM references.
- `compatibility`: runtime, migration, API, or host compatibility notes.
- `status`: draft, candidate, released, deprecated, revoked, or unknown.

## Extension Points

Projects may add changelogs, deployment rings, approvals, compliance, signing,
or marketplace metadata.

## Invariants

- Release identity is stable.
- Artifacts and provenance are traceable.
- Compatibility and migration expectations are explicit.
- Revoked or deprecated releases are distinguishable from active ones.

## Validation Rules

- Resolve artifact and provenance references.
- Warn when released artifacts lack checksums or source refs.
- Warn when compatibility is absent for installable outputs.

## Agent Implementation Notes

Use this contract for packaging, deployment, rollback, audit, and distribution
workflows.

