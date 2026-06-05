# UI Screen Contract v1

Contract ID: `universal.ui.screen.v1`

## Purpose

Describe one screen, page, panel, dialog, or app view in terms of layout regions,
data dependencies, states, actions, and accessibility behavior.

## Required Shape

A screen descriptor should include:

- `schema`: `universal.ui.screen.v1`.
- `id`: stable screen ID.
- `kind`: `ui_screen`.
- `purpose`: task or user goal supported by the screen.
- `layout`: regions, hierarchy, responsive behavior, and persistent controls.
- `data`: sources, schemas, loading behavior, and refresh rules.
- `states`: loading, empty, ready, error, offline, unauthorized, degraded, and
  modal states.
- `actions`: primary, secondary, destructive, navigation, and background actions.
- `components`: component references and ownership.
- `accessibility`: landmarks, focus order, labels, keyboard paths, and motion.

## Extension Points

Projects may add route bindings, analytics, feature flags, localization,
permissions, visual snapshots, or platform-specific layout variants.

## Invariants

- Primary user actions and failure states are explicit.
- Responsive behavior is documented for supported viewport classes.
- Data dependencies are discoverable.
- Accessibility expectations are preserved through refactors.

## Validation Rules

- Resolve component, data, route, and visual artifact references.
- Warn when screens omit error or empty states for remote data.
- Warn when destructive actions omit confirmation or permission notes.
- Warn when responsive screens omit viewport expectations.

## Agent Implementation Notes

Use this contract when adding or modifying user-facing screens so behavior,
layout, and state coverage remain recognizable.

