---
id: iac.terraform-stable-resource-addressing
title: Terraform Stable Resource Addressing
type: implementation-pattern
status: draft
summary: Use stable keys, lifecycle-aware refactors, and cautious conditionals so Terraform does not replace resources merely because list order, count indexes, or addresses changed.
tags:
  - infrastructure-as-code
  - terraform
  - refactoring
  - for-each
  - count
  - lifecycle
  - zero-downtime
  - safe-change
aliases:
  - terraform for_each over count
  - stable terraform addresses
  - terraform count gotcha
  - terraform refactor safely
  - terraform zero downtime deployment
applies_when:
  - Terraform resources are created from collections, conditionals, generated names, or reusable modules.
  - A refactor, list edit, or deployment update could cause unexpected replacement.
avoid_when:
  - The resources are disposable and replacement has no data, availability, or dependency consequence.
  - The collection is truly fixed-order and index identity is part of the intended contract.
related:
  - iac.safe-infrastructure-change
  - iac.small-safe-changes
  - iac.data-continuity-strategy
  - iac.terraform-test-strategy
sources:
  - "book: Yevgeniy Brikman, Terraform: Up & Running, third edition; Chapter 5, Loops, Conditionals, Deployment, and Gotchas."
source_confidence: high
last_reviewed: 2026-06-05
---

# Terraform Stable Resource Addressing

## Intent

Prevent Terraform from destroying or replacing resources because implementation addresses changed rather than because the intended infrastructure changed.

## Use when

- A resource uses `count`, `for_each`, dynamic blocks, or conditional creation.
- A list of resources may gain, lose, or reorder elements.
- Resource replacement could affect data, availability, DNS, identity, or downstream dependencies.
- A module is being refactored, renamed, split, or moved.
- A zero-downtime rollout requires old and new capacity to overlap.

## Avoid when

- Resource identity is intentionally positional and the cost of replacement is negligible.
- The change is a clean rebuild of a disposable test environment.
- The provider cannot support the desired lifecycle behavior and the team has accepted downtime.
- The code is simpler and safer with explicit resources than with generalized loops.

## Context and problem

Terraform tracks resources by address. When resources are produced by `count`, addresses are tied to numeric indexes. Inserting or removing an item in the middle of a list can shift indexes and make Terraform believe several resources changed identity. Similar surprises happen with conditional resources, generated names, and refactors that move resources between modules or rename blocks.

The issue is not that loops or conditionals are bad. The issue is that Terraform resource addresses become part of the operational identity of managed infrastructure. Changes to address shape need the same care as changes to the infrastructure itself.

## Forces

- Loops reduce duplication, but unstable indexes can create accidental replacements.
- `for_each` gives stable keys, but those keys become long-lived identifiers.
- Zero-downtime lifecycle settings help, but provider constraints may still force replacement.
- Refactoring improves maintainability, but state must be moved deliberately.
- Conditional resources simplify optional behavior, but can produce missing references or mode explosion.

## Guidance

Prefer `for_each` with stable meaningful keys when resources represent independently identifiable things. Use `count` for simple homogeneous replicas where index-based identity is acceptable. Treat keys, resource names, and module paths as durable API-like choices once real infrastructure exists.

Before refactoring Terraform structure, plan the state transition. Use Terraform-supported state moves, import, moved blocks, or staged changes to preserve identity where possible. For availability-sensitive resources, design rollout mechanics explicitly rather than assuming Terraform will infer zero downtime.

## Implementation moves

- Use maps or sets with stable keys for independently managed resources.
- Avoid list indexes for users, databases, subnets, IAM bindings, DNS records, or other named resources.
- Choose keys that will not change when display names, ordering, or optional metadata changes.
- Review plans for destroy/create actions caused by address changes rather than desired replacement.
- Use lifecycle settings such as create-before-destroy only when the provider and naming model support overlap.
- Use moved blocks or state migration commands when renaming, moving, or extracting modules.
- Add tests or policy checks for unexpected deletes on protected resource types.

## Checks

- Would adding an item to the middle of a collection replace existing resources?
- Are `for_each` keys meaningful and stable enough to keep for years?
- Does the plan show destroy/create because of address movement rather than infrastructure intent?
- Are state moves documented and reviewed for refactors?
- Can old and new resources coexist when zero downtime is required?
- Do conditional branches leave references valid in both enabled and disabled modes?

## Failure modes

- Using `count` over an ordered list for resources that have real names or data.
- Changing `for_each` keys casually and causing replacement.
- Renaming modules or resources without moving state.
- Adding create-before-destroy where unique names prevent coexistence.
- Hiding too many lifecycle paths behind conditionals that are never tested together.

## Agent trigger hints

Use this pattern when the user says or implies:

- Terraform count vs for_each
- resource address changed
- Terraform wants to replace everything
- refactor Terraform safely
- moved block
- zero downtime Terraform
- create_before_destroy
- conditional resource

## Source notes

Synthesized from Chapter 5 of Terraform: Up & Running, third edition, especially loops, conditionals, zero-downtime deployment, valid-plan failure modes, and safe refactoring guidance. No source excerpts are stored here.
