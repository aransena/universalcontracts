# UI Visual Regression Contract v1

Contract ID: `universal.ui.visual_regression.v1`

## Purpose

Describe visual comparison coverage, baselines, viewports, tolerances, masks,
and artifacts in a tool-agnostic way.

## Required Shape

A visual regression descriptor should include:

- `schema`: `universal.ui.visual_regression.v1`.
- `id`: stable visual regression surface ID.
- `kind`: `ui_visual_regression`.
- `subjects`: screens, components, routes, states, or flows under comparison.
- `baselines`: approved image, video, or render artifact references.
- `viewports`: device classes, dimensions, pixel density, and orientation.
- `states`: data fixtures, themes, locales, auth state, and interaction state.
- `tolerances`: pixel, perceptual, layout, animation, or content thresholds.
- `masks`: ignored regions, dynamic content, or volatile timestamps.
- `artifacts`: diffs, captures, reports, logs, or traces.

## Extension Points

Projects may add renderer metadata, anti-aliasing policy, animation settling,
font loading rules, platform matrices, or approval workflows.

## Invariants

- Baselines and captured states are traceable.
- Dynamic regions are explicitly masked instead of accepted silently.
- Viewport coverage matches supported responsive behavior.
- Visual failures produce inspectable artifacts.

## Validation Rules

- Resolve baseline, subject, fixture, and artifact references.
- Warn when responsive subjects omit viewport coverage.
- Warn when tolerances are absent or overly broad.
- Warn when dynamic content is not masked or stabilized.

## Agent Implementation Notes

Use this contract when reviewing UI changes or preserving visual behavior across
framework, styling, or component refactors.

