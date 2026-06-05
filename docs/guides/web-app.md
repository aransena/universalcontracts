# Guide: Building or Reviewing a Web App

## Start Here

Use `universal.profile.web_application.v1` when the change crosses routes, UI,
API clients, browser state, auth, or tests.

Use these contracts first:

- `universal.web.project.v1`
- `universal.web.app_surface.v1`
- `universal.web.route.v1`
- `universal.core.command.v1`
- `universal.core.config.v1`
- `universal.core.environment.v1`

## Add UI Contracts

If the task changes visible UI, add:

- `universal.ui.design_system.v1`
- `universal.ui.component.v1`
- `universal.ui.screen.v1`
- `universal.ui.user_flow.v1`
- `universal.ui.accessibility.v1`

If visual behavior is important, add:

- `universal.ui.visual_regression.v1`
- `universal.web.test_surface.v1`

## Add Backend Integration Contracts

If the web app calls services, add:

- `universal.web.api_client.v1`
- `universal.core.api_surface.v1`
- `universal.api.endpoint.v1`

If browser state persists, add:

- `universal.web.browser_storage.v1`

If user input mutates data, add:

- `universal.web.form.v1`
- `universal.core.permissions.v1`

If the feature touches common app services, add:

- `universal.app.auth_identity.v1`
- `universal.app.user_session.v1`
- `universal.app.access_control.v1`
- `universal.app.cache_policy.v1`
- `universal.app.search_surface.v1`
- `universal.app.notification.v1`
- `universal.app.file_upload.v1`

## Agent Checklist

1. Identify routes and screens affected.
2. Preserve command, configuration, and environment assumptions.
3. Preserve design-system tokens and component contracts.
4. Declare API clients, cache behavior, errors, and browser storage.
5. Add or update examples and tests for key user flows.
