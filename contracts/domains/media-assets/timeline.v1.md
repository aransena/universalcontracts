# Timeline Contract v1

Contract ID: `universal.media.timeline.v1`

## Purpose

Describe time-based media structure such as clips, tracks, edits, markers,
captions, chapters, or synchronized sensor streams.

## Required Shape

A timeline descriptor should include:

- `schema`: `universal.media.timeline.v1`.
- `id`: stable timeline ID.
- `kind`: `timeline`.
- `timebase`: units, frame rate, sample rate, or timestamp policy.
- `tracks`: audio, video, text, data, annotation, or control tracks.
- `segments`: clips, ranges, source references, offsets, and durations.
- `markers`: chapters, events, cues, or named time points.
- `files`: project, interchange, preview, or export files.

## Extension Points

Projects may add NLE project metadata, EDL, OTIO, captions, waveform, sensor
alignment, or review states.

## Invariants

- Time units and origin are explicit.
- Segment source references are resolvable.
- Track roles are declared.
- Timeline edits do not imply source media mutation.

## Validation Rules

- Resolve source and file references.
- Warn when segments omit duration or source offsets.
- Warn when mixed clocks or frame rates lack alignment notes.

## Agent Implementation Notes

Use this contract for media review, editing, synchronized playback, annotation,
and capture visualization.

