# UI Accessibility Contract v1

Contract ID: `universal.ui.accessibility.v1`

## Purpose

Describe accessibility expectations for screens, components, flows, and
interactive surfaces.

## Required Shape

An accessibility descriptor should include:

- `schema`: `universal.ui.accessibility.v1`.
- `id`: stable accessibility surface ID.
- `kind`: `ui_accessibility`.
- `subjects`: screens, components, routes, forms, or flows covered.
- `semantics`: roles, names, descriptions, landmarks, and relationships.
- `keyboard`: tab order, shortcuts, focus traps, escape behavior, and activation.
- `focus`: initial focus, restored focus, visible focus, and focus management.
- `announcements`: live regions, status updates, errors, and async changes.
- `contrast`: text, icons, controls, states, and theme expectations.
- `motion`: animation, reduced-motion behavior, timing, and vestibular risks.

## Extension Points

Projects may add audit reports, assistive technology notes, localization
requirements, media captions, cognitive accessibility, or platform-specific
guidance.

## Invariants

- Interactive controls have accessible names and keyboard behavior.
- Focus order is predictable.
- Error and status changes are perceivable.
- Accessibility expectations are treated as part of the UI contract, not as
  optional styling.

## Validation Rules

- Resolve subject, report, and fixture references.
- Warn when interactive subjects omit keyboard or focus behavior.
- Warn when async state changes omit announcement behavior.
- Warn when contrast expectations are missing for themeable UI.

## Agent Implementation Notes

Use this contract when implementing, testing, or reviewing UI behavior that must
remain usable across input methods and assistive technologies.

