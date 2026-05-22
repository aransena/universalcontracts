# Manifest Contract v1

Contract ID: `universal.core.manifest.v1`

## Purpose

Define a common manifest pattern for bundles, sessions, artifacts, datasets,
plugins, and other self-describing outputs.

## Required Fields

- `schema`: manifest schema or contract ID.
- `id`: stable identifier for this bundle or artifact.
- `kind`: broad object kind, such as `recording_bundle`, `dataset`,
  `plugin`, `build_artifact`, or `runtime`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: project, version, command, and optional host/runtime details.
- `contracts`: contract IDs this object claims to implement.

## Recommended Fields

- `name`: human-readable name.
- `description`: short description.
- `metadata`: recorder-owned or producer-owned metadata.
- `user_metadata_path`: pointer to user-editable metadata when present.
- `files`: file roles and relative paths.
- `children`: child manifests or nested bundle references.
- `derived`: derived artifacts generated from this object.
- `validation`: validator names, results, and conformance status.

## Path Rules

- Paths inside a manifest should be relative to the manifest file unless marked
  as absolute.
- Relative paths must not escape the bundle root.
- Consumers should follow manifest file roles before falling back to conventional
  filenames.

## Invariants

- `schema`, `id`, `kind`, and `created_at` must be present.
- A manifest must be valid JSON.
- Producer-owned fields must not require user editing.
- User-editable metadata should live outside the producer-owned manifest.

