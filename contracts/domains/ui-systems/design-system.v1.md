# UI Design System Contract v1

Contract ID: `universal.ui.design_system.v1`

## Purpose

Describe a UI design system's portable tokens, components, patterns, assets, and
accessibility expectations without depending on a specific design or component
tool.

## Required Shape

A design system descriptor should include:

- `schema`: `universal.ui.design_system.v1`.
- `id`: stable design system ID.
- `kind`: `ui_design_system`.
- `producer`: owning project, team, or package.
- `tokens`: color, typography, spacing, sizing, radius, elevation, motion, and
  breakpoint references.
- `components`: component catalog or descriptor references.
- `assets`: icons, imagery, fonts, illustrations, or media asset references.
- `themes`: theme names, overrides, modes, and inheritance rules.
- `accessibility`: contrast, focus, keyboard, labeling, and motion expectations.
- `usage`: supported platforms, frameworks, and integration constraints.

## Extension Points

Projects may add brand rules, platform-specific tokens, generated code, design
source references, migration guides, or visual examples. These should remain
references rather than hard requirements on one external tool.

## Invariants

- Token names and meanings are stable.
- Components reference their states and accessibility expectations.
- Generated assets are distinguished from source assets.
- Themes do not silently change semantic token meanings.

## Validation Rules

- Resolve token, component, asset, and theme references.
- Warn when color tokens omit contrast or semantic usage notes.
- Warn when component catalogs omit accessibility expectations.
- Warn when generated outputs are not marked as generated.

## Agent Implementation Notes

Use this contract before building, refactoring, or reviewing UI so agents can
preserve established visual and interaction conventions.

