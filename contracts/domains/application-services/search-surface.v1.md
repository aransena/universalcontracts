# Search Surface Contract v1

Contract ID: `universal.app.search_surface.v1`

## Purpose

Describe user-facing or service-facing search surfaces, indexes, documents,
filters, ranking, permissions, and freshness behavior.

## Required Shape

A search surface descriptor should include:

- `schema`: `universal.app.search_surface.v1`.
- `id`: stable search surface ID.
- `kind`: `search_surface`.
- `subject`: route, API, service, corpus, model, dataset, or user workflow.
- `sources`: databases, documents, events, object stores, media, or external
  indexes.
- `index`: lexical, vector, hybrid, database, cache, or external index reference.
- `queries`: query syntax, filters, facets, sort, pagination, and limits.
- `results`: result shape, highlights, ranking signals, permissions, and
  empty-state behavior.
- `freshness`: indexing delay, rebuild, incremental update, and stale behavior.

## Extension Points

Projects may add analyzers, embeddings, synonyms, personalization, query logs,
spell correction, relevance tests, or moderation rules.

## Invariants

- Search results respect access control and tenant boundaries.
- Index freshness and rebuild behavior are explicit.
- Query and result shapes are stable for callers.
- Ranking or relevance expectations are testable where important.

## Validation Rules

- Resolve source, index, access control, route, and API references.
- Warn when search results omit permission behavior.
- Warn when stale indexes omit freshness semantics.
- Warn when filters or pagination are not declared for public search.

## Agent Implementation Notes

Use this contract before adding search boxes, admin search, vector search,
document retrieval, faceted browsing, or search APIs.
