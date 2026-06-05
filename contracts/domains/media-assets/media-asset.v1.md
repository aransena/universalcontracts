# Media Asset Contract v1

Contract ID: `universal.media.media_asset.v1`

## Purpose

Describe an image, video, audio, 3D, document-like media file, or asset bundle
with formats, metadata, rights, provenance, and derived renditions.

## Required Shape

A media asset descriptor should include:

- `schema`: `universal.media.media_asset.v1`.
- `id`: stable asset ID.
- `kind`: image, video, audio, model_3d, document_media, or asset_bundle.
- `created_at`: ISO 8601 UTC timestamp when ingested or produced.
- `producer`: capture, import, generation, or editing project.
- `files`: original, proxy, thumbnail, metadata, transcript, checksum, or sidecar
  roles.
- `format`: MIME type, codec, container, dimensions, duration, or sample rate.
- `rights`: license, owner, usage limits, and attribution.
- `sources`: capture, generation prompt, edit, or upstream asset references.

## Extension Points

Projects may add color profiles, EXIF, camera metadata, AI generation settings,
asset taxonomy, moderation labels, or content hashes.

## Invariants

- Original and derived files are distinguishable.
- Rights and usage constraints are explicit for sharing.
- Format metadata is sufficient for preview or transcoding decisions.
- Provenance is preserved for generated or edited assets.

## Validation Rules

- Resolve local file and sidecar references.
- Warn when shareable assets omit rights.
- Warn when format metadata is too sparse for generic preview tools.

## Agent Implementation Notes

Use this contract when assets move between capture, editing, storage, preview,
upload, training, or publishing systems.

