# Partitioning Scaling And Performance

Pattern count: 22

## Ambassador Local Service Broker

- `id`: `platform.ambassador-local-service-broker`
- `type`: `architecture-pattern`
- `source`: `patterns/ambassador-local-service-broker.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `modular-architecture`, `scalability`, `safe-change`, `migration`, `runtime-operations`, `module-boundaries`, `parameterization`, `kubernetes`, `service-discovery`, `ambassador`
- `summary`: Put service discovery, sharding, request splitting, or environment-specific brokering behind a local endpoint so application code can remain simple and portable.

## Analytical Column Storage

- `id`: `data.analytical-column-storage`
- `type`: `architecture-pattern`
- `source`: `patterns/analytical-column-storage.md`
- `tags`: `data-systems`, `analytics`, `storage-engine`, `data-warehouse`, `performance`, `cloud-agnostic`
- `summary`: Use column-oriented storage for analytical workloads that scan many rows but only a subset of columns.

## Backpressure For Streams

- `id`: `data.backpressure-for-streams`
- `type`: `architecture-pattern`
- `source`: `patterns/backpressure-for-streams.md`
- `tags`: `data-systems`, `stream-processing`, `backpressure`, `reliability`, `runtime-operations`, `cloud-agnostic`
- `summary`: Propagate overload signals through streaming systems so slow consumers do not cause unbounded queues or cascading failure.

## Coordinated Batch Aggregation

- `id`: `platform.coordinated-batch-aggregation`
- `type`: `architecture-pattern`
- `source`: `patterns/coordinated-batch-aggregation.md`
- `tags`: `platform-engineering`, `data-platform`, `data-consistency`, `scalability`, `operability`, `design-review`, `runtime-operations`, `testing`, `idempotency`, `batch-processing`, `aggregation`
- `summary`: Use join barriers and reduce stages when parallel batch outputs must be made complete or aggregated into final results.

## Data Continuity Strategy

- `id`: `iac.data-continuity-strategy`
- `type`: `architecture-pattern`
- `source`: `patterns/data-continuity-strategy.md`
- `tags`: `infrastructure-as-code`, `data-continuity`, `disaster-recovery`, `safe-change`, `database`
- `summary`: Handle persistent data explicitly when changing or replacing infrastructure, using segregation, replication, reload, or a deliberate mix.

## Event Driven Function Boundaries

- `id`: `platform.event-driven-function-boundaries`
- `type`: `decision-guide`
- `source`: `patterns/event-driven-function-boundaries.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `operability`, `scalability`, `cost-management`, `design-review`, `implementation-planning`, `module-boundaries`, `testing`, `faas`, `event-driven`
- `summary`: Use FaaS for small stateless request transformations, asynchronous event handlers, and pipelines only when observability, cost, and state constraints fit.

## Hot Spot Aware Partitioning

- `id`: `data.hot-spot-aware-partitioning`
- `type`: `architecture-pattern`
- `source`: `patterns/hot-spot-aware-partitioning.md`
- `tags`: `data-systems`, `partitioning`, `scalability`, `database`, `implementation-planning`, `cloud-agnostic`
- `summary`: Partition data to distribute load while accounting for skew, range access, secondary indexes, and rebalancing.

## Immutable Server Image

- `id`: `iac.immutable-server-image`
- `type`: `architecture-pattern`
- `source`: `patterns/immutable-server-image.md`
- `tags`: `infrastructure-as-code`, `immutability`, `server-images`, `safe-change`, `runtime-operations`, `cloud-agnostic`
- `summary`: Prefer replacing servers from updated images over mutating long-lived servers when the platform and workload support it.

## Index Cost Tradeoff

- `id`: `data.index-cost-tradeoff`
- `type`: `decision-guide`
- `source`: `patterns/index-cost-tradeoff.md`
- `tags`: `data-systems`, `indexing`, `performance`, `database`, `implementation-planning`, `cloud-agnostic`
- `summary`: Add indexes deliberately because they speed reads but increase write cost, storage, and maintenance complexity.

## Load And Performance Characterization

- `id`: `data.load-and-performance-characterization`
- `type`: `decision-guide`
- `source`: `patterns/load-and-performance-characterization.md`
- `tags`: `data-systems`, `scalability`, `performance`, `capacity-planning`, `design-review`, `cloud-agnostic`
- `summary`: Describe scalability using workload dimensions, service-level expectations, and performance distributions before choosing scaling tactics.

## Log Structured Storage

- `id`: `data.log-structured-storage`
- `type`: `architecture-pattern`
- `source`: `patterns/log-structured-storage.md`
- `tags`: `data-systems`, `storage-engine`, `performance`, `database`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use append-oriented storage and compaction when write throughput and sequential I/O dominate the workload.

## Partition Rebalancing

- `id`: `data.partition-rebalancing`
- `type`: `delivery-pattern`
- `source`: `patterns/partition-rebalancing.md`
- `tags`: `data-systems`, `partitioning`, `runtime-operations`, `scalability`, `safe-change`, `cloud-agnostic`
- `summary`: Plan partition movement as an operational workflow with bounded load, stable routing, and rollback or retry behavior.

## Reliability Scalability Maintainability

- `id`: `data.reliability-scalability-maintainability`
- `type`: `decision-guide`
- `source`: `patterns/reliability-scalability-maintainability.md`
- `tags`: `data-systems`, `reliability`, `scalability`, `maintainability`, `design-review`, `cloud-agnostic`
- `summary`: Evaluate data-system designs through reliability, scalability, and maintainability rather than a single technology preference.

## Replicated Stateless Serving

- `id`: `platform.replicated-stateless-serving`
- `type`: `architecture-pattern`
- `source`: `patterns/replicated-stateless-serving.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `high-availability`, `scalability`, `zero-downtime`, `design-review`, `runtime-operations`, `rollback`, `testing`, `kubernetes`, `load-balancing`
- `summary`: Run multiple interchangeable service replicas behind a load balancer with readiness checks, rollout controls, and optional replicated edge layers.

## Reusable Work Queue Interface

- `id`: `platform.reusable-work-queue-interface`
- `type`: `architecture-pattern`
- `source`: `patterns/reusable-work-queue-interface.md`
- `tags`: `platform-engineering`, `data-platform`, `scalability`, `operability`, `modular-architecture`, `implementation-planning`, `runtime-operations`, `module-boundaries`, `idempotency`, `kubernetes`, `work-queue`
- `summary`: Build batch work queues from a generic queue manager, a versioned source interface, and worker containers launched by the orchestrator.

## Scatter Gather Request Parallelism

- `id`: `platform.scatter-gather-request-parallelism`
- `type`: `architecture-pattern`
- `source`: `patterns/scatter-gather-request-parallelism.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `scalability`, `high-availability`, `performance`, `design-review`, `runtime-operations`, `testing`, `kubernetes`, `scatter-gather`
- `summary`: Parallelize one request across many workers only when partial results can be merged and tail-latency, straggler, and availability costs are explicitly controlled.

## Sharded Service Routing

- `id`: `platform.sharded-service-routing`
- `type`: `architecture-pattern`
- `source`: `patterns/sharded-service-routing.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `scalability`, `high-availability`, `data-consistency`, `design-review`, `runtime-operations`, `module-boundaries`, `testing`, `kubernetes`, `sharding`
- `summary`: Split stateful serving across shards with deterministic routing, careful shard-key design, consistent hashing, and targeted replication for hot or critical shards.

## Shared Cluster Boundary

- `id`: `iac.shared-cluster-boundary`
- `type`: `decision-guide`
- `source`: `patterns/shared-cluster-boundary.md`
- `tags`: `infrastructure-as-code`, `kubernetes`, `governance`, `security`, `cost-management`, `design-review`
- `summary`: Share clusters only when isolation, ownership, capacity, and change-management boundaries are explicit and enforceable.

## Storage Engine Fit

- `id`: `data.storage-engine-fit`
- `type`: `decision-guide`
- `source`: `patterns/storage-engine-fit.md`
- `tags`: `data-systems`, `storage-engine`, `database`, `performance`, `design-review`, `cloud-agnostic`
- `summary`: Choose storage engines by write/read mix, update pattern, range-query needs, and compaction behavior.

## Stream Derived Views

- `id`: `data.stream-derived-views`
- `type`: `architecture-pattern`
- `source`: `patterns/stream-derived-views.md`
- `tags`: `data-systems`, `stream-processing`, `derived-data`, `event-driven`, `runtime-operations`, `cloud-agnostic`
- `summary`: Use stream processing to maintain derived data incrementally when low-latency updates matter.

## Timeout Retry Backoff

- `id`: `data.timeout-retry-backoff`
- `type`: `delivery-pattern`
- `source`: `patterns/timeout-retry-backoff.md`
- `tags`: `data-systems`, `distributed-systems`, `resilience`, `runtime-operations`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use timeouts, retries, backoff, and idempotency together so transient faults do not become overload or duplicate side effects.

## Workflow Queue Composition

- `id`: `platform.workflow-queue-composition`
- `type`: `architecture-pattern`
- `source`: `patterns/workflow-queue-composition.md`
- `tags`: `platform-engineering`, `data-platform`, `scalability`, `high-availability`, `modular-architecture`, `design-review`, `runtime-operations`, `idempotency`, `testing`, `event-driven`, `workflow`
- `summary`: Compose multi-stage batch workflows with explicit copier, filter, splitter, sharder, and merger queue patterns backed by reliable pub/sub infrastructure.
