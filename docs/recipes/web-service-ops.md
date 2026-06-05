# Recipe: Web App to Service to Ops

## Flow

```text
web project -> routes -> API client -> service endpoint -> database -> deployment -> service health -> incident
```

## Contracts

- `universal.web.project.v1`
- `universal.web.route.v1`
- `universal.web.api_client.v1`
- `universal.web.browser_storage.v1`
- `universal.web.form.v1`
- `universal.api.service_surface.v1`
- `universal.api.endpoint.v1`
- `universal.db.database_schema.v1`
- `universal.ops.deployment.v1`
- `universal.ops.service_health.v1`
- `universal.ops.incident.v1`

## Interoperability Handoff

1. Routes declare data dependencies, auth, states, and user actions.
2. API clients declare request, response, retry, cache, and error behavior.
3. Service endpoints declare schemas, auth, errors, and limits.
4. Database schema contracts explain storage and migrations.
5. Deployment and health contracts connect runtime state to incident response.

## Agent Notes

When changing a route, trace the whole path from screen state through service
errors and operational health. This reduces drift between frontend behavior and
backend reality.

