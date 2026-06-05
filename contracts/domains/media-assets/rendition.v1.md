# Rendition Contract v1

Contract ID: `universal.media.rendition.v1`

## Purpose

Describe a derived media representation such as a thumbnail, proxy, transcode,
waveform, preview, sprite sheet, or optimized delivery file.

## Required Shape

A rendition descriptor should include:

- `schema`: `universal.media.rendition.v1`.
- `id`: stable rendition ID.
- `kind`: `rendition`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: processing project and command.
- `source`: source media asset or file reference.
- `files`: rendition outputs and metadata.
- `format`: codec, container, dimensions, bitrate, duration, or sample rate.
- `parameters`: processing options, quality settings, and transforms.
- `status`: ok, partial, failed, or unknown.

## Extension Points

Projects may add CDN metadata, adaptive bitrate variants, sprite grids,
watermark settings, color transforms, or accessibility outputs.

## Invariants

- Renditions do not overwrite source assets.
- Source asset and processing parameters are declared.
- Status `ok` means required output files are present and immutable.
- Consumers can choose a rendition from format metadata.

## Validation Rules

- Resolve source and rendition file references.
- Warn when status is `ok` but output files are missing.
- Warn when transform parameters are omitted.

## Agent Implementation Notes

Use this contract for preview generation, media delivery, upload preparation,
and downstream visualization.

