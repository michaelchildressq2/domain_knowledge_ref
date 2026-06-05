# Data Modeling And Storage

Pattern count: 21

## Aggregate Lifecycle Boundary

- `id`: `ddd.aggregate-lifecycle-boundary`
- `type`: `architecture-pattern`
- `source`: `patterns/aggregate-lifecycle-boundary.md`
- `tags`: `domain-driven-design`, `aggregates`, `consistency`, `transactions`, `data-modeling`, `lifecycle-management`
- `summary`: Use aggregate roots to define consistency, reference, transaction, creation, retrieval, and deletion boundaries for domain objects.

## Analytical Column Storage

- `id`: `data.analytical-column-storage`
- `type`: `architecture-pattern`
- `source`: `patterns/analytical-column-storage.md`
- `tags`: `data-systems`, `analytics`, `storage-engine`, `data-warehouse`, `performance`, `cloud-agnostic`
- `summary`: Use column-oriented storage for analytical workloads that scan many rows but only a subset of columns.

## Batch Derived Views

- `id`: `data.batch-derived-views`
- `type`: `architecture-pattern`
- `source`: `patterns/batch-derived-views.md`
- `tags`: `data-systems`, `batch-processing`, `derived-data`, `analytics`, `data-pipeline`, `cloud-agnostic`
- `summary`: Use batch processing to build reliable derived datasets when freshness can lag and complete input scans are acceptable.

## Container Contracts for Reuse

- `id`: `platform.container-contracts-for-reuse`
- `type`: `architecture-pattern`
- `source`: `patterns/container-contracts-for-reuse.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `modular-architecture`, `operability`, `design-review`, `implementation-planning`, `module-boundaries`, `parameterization`, `version-control`, `kubernetes`, `container-contracts`
- `summary`: Treat reusable containers as callable components with explicit parameters, stable APIs, documented behavior, and compatibility checks.

## Data Continuity Strategy

- `id`: `iac.data-continuity-strategy`
- `type`: `architecture-pattern`
- `source`: `patterns/data-continuity-strategy.md`
- `tags`: `infrastructure-as-code`, `data-continuity`, `disaster-recovery`, `safe-change`, `database`
- `summary`: Handle persistent data explicitly when changing or replacing infrastructure, using segregation, replication, reload, or a deliberate mix.

## Declarative Query Boundaries

- `id`: `data.declarative-query-boundaries`
- `type`: `architecture-pattern`
- `source`: `patterns/declarative-query-boundaries.md`
- `tags`: `data-systems`, `query-languages`, `maintainability`, `modular-architecture`, `implementation-planning`, `cloud-agnostic`
- `summary`: Prefer declarative query interfaces when callers should state what data they need without encoding execution strategy.

## Document Model Locality

- `id`: `data.document-model-locality`
- `type`: `architecture-pattern`
- `source`: `patterns/document-model-locality.md`
- `tags`: `data-systems`, `data-modeling`, `document-database`, `query-patterns`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use document storage when related data is usually read and written together as one aggregate.

## Graph Relationship Modeling

- `id`: `data.graph-relationship-modeling`
- `type`: `architecture-pattern`
- `source`: `patterns/graph-relationship-modeling.md`
- `tags`: `data-systems`, `data-modeling`, `graph-database`, `query-patterns`, `design-review`, `cloud-agnostic`
- `summary`: Use graph modeling when relationships between entities are central, variable, and queried across multiple hops.

## Hot Spot Aware Partitioning

- `id`: `data.hot-spot-aware-partitioning`
- `type`: `architecture-pattern`
- `source`: `patterns/hot-spot-aware-partitioning.md`
- `tags`: `data-systems`, `partitioning`, `scalability`, `database`, `implementation-planning`, `cloud-agnostic`
- `summary`: Partition data to distribute load while accounting for skew, range access, secondary indexes, and rebalancing.

## Index Cost Tradeoff

- `id`: `data.index-cost-tradeoff`
- `type`: `decision-guide`
- `source`: `patterns/index-cost-tradeoff.md`
- `tags`: `data-systems`, `indexing`, `performance`, `database`, `implementation-planning`, `cloud-agnostic`
- `summary`: Add indexes deliberately because they speed reads but increase write cost, storage, and maintenance complexity.

## Isolation Level Explicitness

- `id`: `data.isolation-level-explicitness`
- `type`: `decision-guide`
- `source`: `patterns/isolation-level-explicitness.md`
- `tags`: `data-systems`, `transactions`, `isolation-levels`, `consistency`, `implementation-planning`, `cloud-agnostic`
- `summary`: Choose isolation levels by the anomalies the application can tolerate, not by database defaults or ACID labels.

## Leader Follower Replication

- `id`: `data.leader-follower-replication`
- `type`: `architecture-pattern`
- `source`: `patterns/leader-follower-replication.md`
- `tags`: `data-systems`, `replication`, `high-availability`, `database`, `runtime-operations`, `cloud-agnostic`
- `summary`: Use leader-follower replication when one primary write path and multiple read or failover copies fit the consistency and availability needs.

## Log Structured Storage

- `id`: `data.log-structured-storage`
- `type`: `architecture-pattern`
- `source`: `patterns/log-structured-storage.md`
- `tags`: `data-systems`, `storage-engine`, `performance`, `database`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use append-oriented storage and compaction when write throughput and sequential I/O dominate the workload.

## Materialized Conflict Constraints

- `id`: `data.materialized-conflict-constraints`
- `type`: `architecture-pattern`
- `source`: `patterns/materialized-conflict-constraints.md`
- `tags`: `data-systems`, `transactions`, `constraints`, `consistency`, `database`, `cloud-agnostic`
- `summary`: Materialize conflicts so the database can enforce invariants that would otherwise span predicate reads or missing rows.

## Multi Leader Conflict Design

- `id`: `data.multi-leader-conflict-design`
- `type`: `decision-guide`
- `source`: `patterns/multi-leader-conflict-design.md`
- `tags`: `data-systems`, `replication`, `conflict-resolution`, `multi-region`, `design-review`, `cloud-agnostic`
- `summary`: Use multi-leader replication only when write locality or offline operation justifies explicit conflict detection and resolution.

## Polyglot Persistence Fit

- `id`: `data.polyglot-persistence-fit`
- `type`: `decision-guide`
- `source`: `patterns/polyglot-persistence-fit.md`
- `tags`: `data-systems`, `data-modeling`, `database`, `design-review`, `cloud-agnostic`
- `summary`: Choose storage and query models based on access patterns, relationships, consistency needs, and evolution costs.

## Specification Business Rules

- `id`: `ddd.specification-business-rules`
- `type`: `architecture-pattern`
- `source`: `patterns/specification-business-rules.md`
- `tags`: `domain-driven-design`, `business-rules`, `specifications`, `query-patterns`, `domain-modeling`, `declarative-design`
- `summary`: Represent important predicates and selection rules as named, composable domain concepts instead of scattering conditionals.

## Storage Engine Fit

- `id`: `data.storage-engine-fit`
- `type`: `decision-guide`
- `source`: `patterns/storage-engine-fit.md`
- `tags`: `data-systems`, `storage-engine`, `database`, `performance`, `design-review`, `cloud-agnostic`
- `summary`: Choose storage engines by write/read mix, update pattern, range-query needs, and compaction behavior.

## Transaction Boundary Fit

- `id`: `data.transaction-boundary-fit`
- `type`: `decision-guide`
- `source`: `patterns/transaction-boundary-fit.md`
- `tags`: `data-systems`, `transactions`, `consistency`, `database`, `design-review`, `cloud-agnostic`
- `summary`: Use transactions where they simplify correctness, but keep boundaries aligned with invariants and operational cost.

## Ubiquitous Language

- `id`: `ddd.ubiquitous-language`
- `type`: `practice`
- `source`: `patterns/ubiquitous-language.md`
- `tags`: `domain-driven-design`, `domain-modeling`, `collaboration`, `terminology`, `code-readability`, `design-review`
- `summary`: Use the domain model as the shared language in speech, diagrams, tests, documents, and code.

## Unbundled Derived Data

- `id`: `data.unbundled-derived-data`
- `type`: `architecture-pattern`
- `source`: `patterns/unbundled-derived-data.md`
- `tags`: `data-systems`, `derived-data`, `data-integration`, `event-driven`, `modular-architecture`, `cloud-agnostic`
- `summary`: Compose specialized storage and processing systems by deriving views from a durable source of truth instead of forcing one database to do everything.
