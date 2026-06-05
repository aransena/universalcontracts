# Recipe: UI Change Control

## Flow

```text
design system -> component -> screen -> user flow -> web route -> visual regression -> accessibility -> web test surface
```

## Contracts

- `universal.ui.design_system.v1`
- `universal.ui.component.v1`
- `universal.ui.screen.v1`
- `universal.ui.user_flow.v1`
- `universal.ui.visual_regression.v1`
- `universal.ui.accessibility.v1`
- `universal.web.route.v1`
- `universal.web.test_surface.v1`

## Interoperability Handoff

1. Design systems declare tokens, components, themes, and accessibility rules.
2. Components declare props, states, events, slots, and examples.
3. Screens declare layout, data, states, actions, and components.
4. User flows declare entry points, steps, exits, roles, and side effects.
5. Visual and accessibility contracts preserve behavior across refactors.

## Agent Notes

Do not make UI changes by visual guesswork alone. Identify the component,
screen, and flow contracts first, then update tests and visual artifacts that
prove the behavior.

