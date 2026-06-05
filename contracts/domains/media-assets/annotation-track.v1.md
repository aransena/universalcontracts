# Media Annotation Track Contract v1

Contract ID: `universal.media.annotation_track.v1`

## Purpose

Describe spatial, temporal, textual, or semantic annotations over media assets
or timelines.

## Required Shape

An annotation track descriptor should include:

- `schema`: `universal.media.annotation_track.v1`.
- `id`: stable annotation track ID.
- `kind`: `annotation_track`.
- `subject`: media asset, timeline, stream, or segment reference.
- `timebase`: timestamp units and alignment.
- `labels`: label schema, ontology, or guideline reference.
- `files`: annotation records, summary, conflicts, or review notes.
- `status`: draft, reviewed, approved, rejected, or unknown.

## Extension Points

Projects may add bounding boxes, masks, keypoints, polygons, transcription,
speaker labels, confidence, review status, or annotator metadata.

## Invariants

- Annotation targets and time alignment are explicit.
- Label meanings are declared.
- Draft and approved annotations are distinguishable.
- Unknown annotation fields are additive unless a profile closes shape.

## Validation Rules

- Resolve subject, label, and annotation file references.
- Warn when timebase is missing for temporal annotations.
- Warn when approved tracks include unresolved conflicts.

## Agent Implementation Notes

Use this contract for media labeling, review, training data, visual analytics,
and synchronized playback.

