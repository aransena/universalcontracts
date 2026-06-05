# Replication Contract v1

Contract ID: `universal.db.replication.v1`

## Purpose

Describe replication, synchronization, mirroring, or read-model update behavior
between databases, stores, regions, services, or devices.

## Required Shape

A replication descriptor should include:

- `schema`: `universal.db.replication.v1`.
- `id`: stable replication ID.
- `kind`: `replication`.
- `source`: source database, table, collection, bucket, topic, or service.
- `target`: destination database, table, collection, bucket, topic, or service.
- `mode`: snapshot, incremental, streaming, bidirectional, fanout, or custom.
- `consistency`: ordering, lag, conflict resolution, and convergence behavior.
- `lifecycle`: bootstrap, catchup, running, paused, failed, and recovery states.
- `observability`: lag metrics, checkpoints, errors, alerts, and audit logs.

## Extension Points

Projects may add shard mappings, region topology, schema transforms, device sync
metadata, warehouse load options, or provider-specific replication IDs.

## Invariants

- Source and target are distinguishable and versioned.
- Conflict and lag behavior are explicit.
- Replication failures preserve restart checkpoints.
- Consumers can tell whether replicated data is authoritative or derived.

## Validation Rules

- Resolve source, target, schema, and observability references.
- Warn when bidirectional replication omits conflict behavior.
- Warn when replicated data omits lag or freshness semantics.
- Warn when restart checkpoints are unavailable.

## Agent Implementation Notes

Use this contract for read replicas, search indexes, analytics mirrors,
offline-first sync, regional replication, and edge-to-cloud data movement.
