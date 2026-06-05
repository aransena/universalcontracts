# Search Index Contract v1

Contract ID: `universal.knowledge.search_index.v1`

## Purpose

Describe a lexical, vector, hybrid, graph, or structured search index and what
data it covers.

## Required Shape

A search index descriptor should include:

- `schema`: `universal.knowledge.search_index.v1`.
- `id`: stable index ID.
- `kind`: `search_index`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: indexer project and version.
- `sources`: corpus, dataset, documents, chunks, or records indexed.
- `index`: files, service endpoint, database, or vector store reference.
- `fields`: indexed fields, analyzers, embeddings, filters, and sort keys.
- `query`: supported query modes and limits.

## Extension Points

Projects may add embedding models, tokenizer settings, ranking features,
synonyms, rerankers, ACL filters, or sharding metadata.

## Invariants

- The indexed source version is declared.
- Query behavior and limits are discoverable.
- Embedding indexes identify model and dimension.
- Access control behavior is explicit when indexed content is restricted.

## Validation Rules

- Resolve local source and index references.
- Warn when vector indexes omit embedding model details.
- Warn when indexes omit source version or build time.

## Agent Implementation Notes

Use this contract to connect document corpora, memory stores, retrieval systems,
and analysis tools.

