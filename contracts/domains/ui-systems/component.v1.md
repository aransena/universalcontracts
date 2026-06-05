# UI Component Contract v1

Contract ID: `universal.ui.component.v1`

## Purpose

Describe a reusable UI component's public interface, variants, states, events,
composition rules, and accessibility behavior.

## Required Shape

A component descriptor should include:

- `schema`: `universal.ui.component.v1`.
- `id`: stable component ID.
- `kind`: `ui_component`.
- `producer`: owning package or project.
- `props`: public properties, types, defaults, required status, and units.
- `variants`: visual or behavioral variants and allowed combinations.
- `states`: loading, empty, disabled, active, selected, error, focused, and
  custom states.
- `events`: user actions, callbacks, emitted messages, and side effects.
- `slots`: child content, composition points, and layout expectations.
- `accessibility`: role, labels, keyboard behavior, focus, and announcements.
- `examples`: minimal usage, edge cases, and expected rendered states.

## Extension Points

Projects may add framework bindings, token usage, animations, testing hooks,
analytics events, or platform-specific adaptations.

## Invariants

- Public props and events are stable for consumers.
- Variant combinations are documented or intentionally unconstrained.
- Accessibility semantics are part of the component contract.
- Internal implementation details do not become required integration behavior.

## Validation Rules

- Resolve local example, token, and test references.
- Warn when interactive components omit keyboard or focus behavior.
- Warn when visual variants lack state examples.
- Warn when breaking props are changed without versioning.

## Agent Implementation Notes

Use this contract before changing reusable components or composing them into
screens and flows.

