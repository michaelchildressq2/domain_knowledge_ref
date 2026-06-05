# Replication Consistency And Coordination

Pattern count: 30

## Aggregate Lifecycle Boundary

- `id`: `ddd.aggregate-lifecycle-boundary`
- `type`: `architecture-pattern`
- `source`: `patterns/aggregate-lifecycle-boundary.md`
- `tags`: `domain-driven-design`, `aggregates`, `consistency`, `transactions`, `data-modeling`, `lifecycle-management`
- `summary`: Use aggregate roots to define consistency, reference, transaction, creation, retrieval, and deletion boundaries for domain objects.

## Cluster Per Environment

- `id`: `iac.cluster-per-environment`
- `type`: `architecture-pattern`
- `source`: `patterns/cluster-per-environment.md`
- `tags`: `infrastructure-as-code`, `kubernetes`, `environment-parity`, `high-availability`, `safe-change`
- `summary`: Use separate clusters when environment isolation, failure containment, or change independence outweighs shared-cluster efficiency.

## Conflict Free Domain Design

- `id`: `data.conflict-free-domain-design`
- `type`: `architecture-pattern`
- `source`: `patterns/conflict-free-domain-design.md`
- `tags`: `data-systems`, `replication`, `conflict-resolution`, `eventual-consistency`, `implementation-planning`, `cloud-agnostic`
- `summary`: Shape replicated operations so concurrent updates commute or merge without losing user intent.

## Consensus For Coordination

- `id`: `data.consensus-for-coordination`
- `type`: `architecture-pattern`
- `source`: `patterns/consensus-for-coordination.md`
- `tags`: `data-systems`, `consensus`, `coordination`, `distributed-systems`, `reliability`, `cloud-agnostic`
- `summary`: Use consensus-backed coordination for leader election, membership, locks, and configuration that require agreement despite failures.

## Coordinated Batch Aggregation

- `id`: `platform.coordinated-batch-aggregation`
- `type`: `architecture-pattern`
- `source`: `patterns/coordinated-batch-aggregation.md`
- `tags`: `platform-engineering`, `data-platform`, `data-consistency`, `scalability`, `operability`, `design-review`, `runtime-operations`, `testing`, `idempotency`, `batch-processing`, `aggregation`
- `summary`: Use join barriers and reduce stages when parallel batch outputs must be made complete or aggregated into final results.

## Copy Paste Environments

- `id`: `iac.copy-paste-environments`
- `type`: `anti-pattern`
- `source`: `patterns/copy-paste-environments.md`
- `tags`: `infrastructure-as-code`, `anti-pattern`, `environment-parity`, `configuration-drift`, `stack-design`, `cloud-agnostic`
- `summary`: Duplicating stack source per environment creates short-term isolation but long-term drift and delivery overhead.

## Data Continuity Strategy

- `id`: `iac.data-continuity-strategy`
- `type`: `architecture-pattern`
- `source`: `patterns/data-continuity-strategy.md`
- `tags`: `infrastructure-as-code`, `data-continuity`, `disaster-recovery`, `safe-change`, `database`
- `summary`: Handle persistent data explicitly when changing or replacing infrastructure, using segregation, replication, reload, or a deliberate mix.

## Derived Data Over Distributed Transactions

- `id`: `data.derived-data-over-distributed-transactions`
- `type`: `decision-guide`
- `source`: `patterns/derived-data-over-distributed-transactions.md`
- `tags`: `data-systems`, `data-integration`, `distributed-workflow`, `derived-data`, `design-review`, `cloud-agnostic`
- `summary`: Prefer replayable derived dataflows over distributed transactions when integrating heterogeneous stores for read optimization.

## Eventual Consistency Boundaries

- `id`: `data.eventual-consistency-boundaries`
- `type`: `architecture-pattern`
- `source`: `patterns/eventual-consistency-boundaries.md`
- `tags`: `data-systems`, `eventual-consistency`, `consistency`, `distributed-systems`, `design-review`, `cloud-agnostic`
- `summary`: Use eventual consistency only where product semantics, repair mechanisms, and user expectations can tolerate temporary divergence.

## Fencing Tokens

- `id`: `data.fencing-tokens`
- `type`: `architecture-pattern`
- `source`: `patterns/fencing-tokens.md`
- `tags`: `data-systems`, `distributed-systems`, `coordination`, `consistency`, `runtime-operations`, `cloud-agnostic`
- `summary`: Use monotonically increasing fencing tokens to prevent stale leaders or lock holders from corrupting shared resources.

## Isolation Level Explicitness

- `id`: `data.isolation-level-explicitness`
- `type`: `decision-guide`
- `source`: `patterns/isolation-level-explicitness.md`
- `tags`: `data-systems`, `transactions`, `isolation-levels`, `consistency`, `implementation-planning`, `cloud-agnostic`
- `summary`: Choose isolation levels by the anomalies the application can tolerate, not by database defaults or ACID labels.

## Layered Domain Architecture

- `id`: `ddd.layered-domain-architecture`
- `type`: `architecture-pattern`
- `source`: `patterns/layered-domain-architecture.md`
- `tags`: `domain-driven-design`, `layered-architecture`, `domain-layer`, `separation-of-concerns`, `modular-architecture`, `testability`
- `summary`: Isolate domain logic from UI, application coordination, and infrastructure so the model can stay expressive and testable.

## Leader Election Safety

- `id`: `data.leader-election-safety`
- `type`: `architecture-pattern`
- `source`: `patterns/leader-election-safety.md`
- `tags`: `data-systems`, `coordination`, `leader-election`, `distributed-systems`, `runtime-operations`, `cloud-agnostic`
- `summary`: Design leader election so only one effective leader can perform protected work at a time.

## Leader Follower Replication

- `id`: `data.leader-follower-replication`
- `type`: `architecture-pattern`
- `source`: `patterns/leader-follower-replication.md`
- `tags`: `data-systems`, `replication`, `high-availability`, `database`, `runtime-operations`, `cloud-agnostic`
- `summary`: Use leader-follower replication when one primary write path and multiple read or failover copies fit the consistency and availability needs.

## Lease Based Ownership Election

- `id`: `platform.lease-based-ownership-election`
- `type`: `architecture-pattern`
- `source`: `patterns/lease-based-ownership-election.md`
- `tags`: `platform-engineering`, `cloud-architecture`, `high-availability`, `data-consistency`, `operability`, `design-review`, `runtime-operations`, `idempotency`, `testing`, `kubernetes`, `leader-election`
- `summary`: Elect one active owner among replicas with consensus-backed compare-and-swap, renewable leases, and fencing checks before protected actions.

## Linearizability When Needed

- `id`: `data.linearizability-when-needed`
- `type`: `decision-guide`
- `source`: `patterns/linearizability-when-needed.md`
- `tags`: `data-systems`, `consistency`, `linearizability`, `distributed-systems`, `design-review`, `cloud-agnostic`
- `summary`: Use linearizability for operations that require a single up-to-date view, and avoid paying its cost for data that can be stale or mergeable.

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

## Partial Failure Design

- `id`: `data.partial-failure-design`
- `type`: `architecture-pattern`
- `source`: `patterns/partial-failure-design.md`
- `tags`: `data-systems`, `distributed-systems`, `reliability`, `failure-modes`, `design-review`, `cloud-agnostic`
- `summary`: Design distributed systems assuming some components can be slow, unreachable, or mistaken while others continue running.

## Polyglot Persistence Fit

- `id`: `data.polyglot-persistence-fit`
- `type`: `decision-guide`
- `source`: `patterns/polyglot-persistence-fit.md`
- `tags`: `data-systems`, `data-modeling`, `database`, `design-review`, `cloud-agnostic`
- `summary`: Choose storage and query models based on access patterns, relationships, consistency needs, and evolution costs.

## Replication Lag Aware Reads

- `id`: `data.replication-lag-aware-reads`
- `type`: `architecture-pattern`
- `source`: `patterns/replication-lag-aware-reads.md`
- `tags`: `data-systems`, `replication`, `consistency`, `read-models`, `runtime-operations`, `cloud-agnostic`
- `summary`: Design read paths around the user-visible anomalies created by asynchronous replication lag.

## Repository Boundaries

- `id`: `iac.repository-boundaries`
- `type`: `decision-guide`
- `source`: `patterns/repository-boundaries.md`
- `tags`: `infrastructure-as-code`, `version-control`, `modular-architecture`, `delivery-pipeline`, `governance`, `cloud-agnostic`
- `summary`: Choose infrastructure repository boundaries based on ownership, delivery cadence, dependency management, and change isolation.

## Saga With Compensation

- `id`: `data.saga-with-compensation`
- `type`: `architecture-pattern`
- `source`: `patterns/saga-with-compensation.md`
- `tags`: `data-systems`, `distributed-workflow`, `transactions`, `event-driven`, `implementation-planning`, `cloud-agnostic`
- `summary`: Coordinate multi-step business workflows with explicit state and compensating actions when one distributed transaction is not appropriate.

## Sandbox IaC Testing

- `id`: `iac.sandbox-iac-testing`
- `type`: `testing-practice`
- `source`: `patterns/sandbox-iac-testing.md`
- `tags`: `infrastructure-as-code`, `testing`, `sandbox`, `isolation`, `cost-control`, `safe-change`
- `summary`: Test infrastructure changes in isolated disposable environments so validation can create, update, and destroy resources without harming production or shared systems.

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

## Terraform Remote State Backend

- `id`: `iac.terraform-remote-state-backend`
- `type`: `implementation-pattern`
- `source`: `patterns/terraform-remote-state-backend.md`
- `tags`: `infrastructure-as-code`, `terraform`, `state-management`, `remote-state`, `locking`, `reproducibility`, `security`
- `summary`: Store Terraform state in a shared remote backend with locking, encryption, versioning, and tightly scoped access instead of treating local state or version control as team-safe storage.

## Terraform State Isolation Layout

- `id`: `iac.terraform-state-isolation-layout`
- `type`: `architecture-pattern`
- `source`: `patterns/terraform-state-isolation-layout.md`
- `tags`: `infrastructure-as-code`, `terraform`, `state-management`, `environments`, `blast-radius`, `file-layout`, `stack-design`
- `summary`: Split Terraform state by environment and component using explicit file layout and backend keys so failures, permissions, plans, and dependencies stay bounded.

## Timeout Retry Backoff

- `id`: `data.timeout-retry-backoff`
- `type`: `delivery-pattern`
- `source`: `patterns/timeout-retry-backoff.md`
- `tags`: `data-systems`, `distributed-systems`, `resilience`, `runtime-operations`, `implementation-planning`, `cloud-agnostic`
- `summary`: Use timeouts, retries, backoff, and idempotency together so transient faults do not become overload or duplicate side effects.

## Transaction Boundary Fit

- `id`: `data.transaction-boundary-fit`
- `type`: `decision-guide`
- `source`: `patterns/transaction-boundary-fit.md`
- `tags`: `data-systems`, `transactions`, `consistency`, `database`, `design-review`, `cloud-agnostic`
- `summary`: Use transactions where they simplify correctness, but keep boundaries aligned with invariants and operational cost.
