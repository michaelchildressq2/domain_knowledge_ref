---
id: platform.data-continuity-during-change
title: Data Continuity During Infrastructure Change
type: architecture-pattern
status: seed
summary: Change infrastructure or application shape without losing, corrupting, or
  making critical data unavailable.
tags:
- platform-engineering
- data-continuity
- data-consistency
- safe-change
- migration
- zero-downtime
- rollback
- roll-forward
- design-review
- cloud-agnostic
aliases:
- data migration safety
- continuity during change
- expand and contract data changes
- safe schema migration
applies_when:
- A deployment, migration, refactor, or infrastructure replacement touches persistent
  data.
- The user asks how to avoid downtime or data loss during a change.
- Old and new versions may run at the same time.
avoid_when:
- The data is disposable or can be regenerated after the change.
- A maintenance window with full outage is acceptable and simpler.
- The system has no persistent state or user-visible data dependency.
related:
- platform.safe-infrastructure-change
- platform.data-consistency
- platform.disaster-recovery
sources:
- 'iac2: Kief Morris, Infrastructure as Code, 2nd Edition, O''Reilly Media'
- synthesis: general platform engineering and database migration practice
source_confidence: medium
last_reviewed: 2026-06-04
subject_area: data
---

# Data Continuity During Infrastructure Change

## Intent

Protect data access and correctness while the system changes underneath it. Make the transition safe for old and new runtime shapes.

## Use when

- A database, queue, storage bucket, schema, state store, network path, identity policy, or platform resource will be replaced or reshaped.
- A blue-green, canary, rolling, or parallel run strategy needs data compatibility.
- The user asks about migration, zero downtime, stateful cutover, backfill, rollback, or compatibility.

## Avoid when

- A simple stop-the-world migration is acceptable and clearly lower risk.
- Data can be recreated from source events or upstream systems.
- The change is purely stateless and has no persisted or in-flight data.

## Context and problem

Infrastructure changes often treat resources as replaceable, but data is not always disposable. A safe change must account for old readers, new readers, old writers, new writers, in-flight operations, backups, and rollback or roll-forward paths.

## Forces

- Reversibility versus speed: reversible changes often require more steps.
- Compatibility versus simplicity: old and new versions may need to coexist temporarily.
- Data safety versus availability: locking protects data but can interrupt users.
- Rollback versus roll-forward: after data shape changes, rollback may no longer be safe.

## Guidance

Separate the infrastructure transition from the data transition. Prefer small compatible steps: prepare, run in parallel or compatibility mode, migrate or backfill, cut traffic, verify, then remove old paths only after confidence is high.

## Implementation moves

- Identify every reader, writer, and background process that touches the data.
- Design an expand step that lets old and new code coexist.
- Backfill or replicate data with validation and progress visibility.
- Cut over traffic or ownership gradually when possible.
- Keep rollback safe until the point where roll-forward becomes the safer recovery path.
- Verify counts, checksums, business invariants, lag, error rates, and user-visible behavior.
- Remove old structures only after a stabilization period.

## Checks

- Can old and new versions run at the same time?
- What happens to writes during cutover?
- Is rollback safe after each step, or is roll-forward required?
- Are in-flight messages, jobs, and retries compatible with the new shape?
- What evidence proves the migrated data is complete and correct?

## Failure modes

- Replacing a stateful resource as if it were stateless compute.
- Deleting old data paths before proving the new path.
- Running incompatible application versions during a rolling deploy.
- Assuming backup restore is a rollback strategy when schema or semantics changed.
- Forgetting background jobs, reporting pipelines, or caches.

## Agent trigger hints

Use this pattern when the user says or implies:

- zero downtime migration
- safe database migration
- preserve data during rebuild
- blue green with data
- expand and contract
- cutover plan
- backfill and verify

## Source notes

This is an original synthesis. The public O'Reilly table of contents names safe infrastructure change and data continuity as concerns; this pattern generalizes the practice for agent guidance without copying book text.
