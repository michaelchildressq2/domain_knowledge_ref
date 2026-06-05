---
id: iac.ansible-custom-module-boundary
title: Ansible Custom Module Boundary
type: design-pattern
status: draft
summary: Create a custom Ansible module when desired-state behavior, validation, check mode, and change reporting are too important or complex for shell tasks or roles.
tags:
  - infrastructure-as-code
  - ansible
  - modules
  - extensibility
  - idempotency
  - testing
  - api-integration
aliases:
  - write custom Ansible module
  - Ansible module development
  - action plugin versus module
  - supports_check_mode
applies_when:
  - A task wraps complex API or system behavior that should expose Ansible-style arguments and changed results.
  - Shell or command tasks require too many guards to be safe.
  - The capability will be reused across roles, projects, or collections.
avoid_when:
  - An existing maintained module or collection already models the desired state.
  - A simple role or templated command is clearer and safe enough.
related:
  - iac.declarative-imperative-separation
  - iac.ansible-playbook-convergence
  - iac.ansible-collection-dependency-manifest
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 10, 15, 19, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Custom Module Boundary

## Intent

Move complex procedural logic behind an Ansible module interface so playbooks retain clear desired-state semantics, validation, check mode support, and accurate change reporting.

## Use when

- Existing modules and collections do not support the target API or resource.
- A shell task needs many conditionals, parsing steps, retries, or state checks.
- A capability needs to return structured facts or changed status.
- Check mode should predict changes without mutating the target.
- The logic will be shared in a collection or across multiple roles.

## Avoid when

- A maintained module already exists and can be used or extended upstream.
- The work is simply task composition and belongs in a role.
- The behavior is a local one-off that would not justify module maintenance.
- The team cannot test the module or document its arguments.

## Context and problem

Shell and command tasks are tempting because they can do anything the target system allows. They also bypass much of what makes Ansible valuable: typed parameters, validation, idempotent state checks, check mode, structured results, and accurate changed flags. As commands grow, the playbook becomes a fragile script.

The Ansible source asks whether a module should be developed, describes custom module placement and collection packaging, and emphasizes module return data, changed status, argument handling, and check mode. The boundary is not Python versus YAML; it is whether the behavior should become a state-aware Ansible primitive.

## Forces

- Reusing existing modules versus maintaining custom code.
- Playbook readability versus module implementation cost.
- State-aware behavior versus quick shell execution.
- Local library modules versus collection distribution.
- Accurate change reporting versus easy but noisy tasks.

## Guidance

Search existing modules and collections first. If none fits, create a custom module when the operation deserves an Ansible contract: explicit arguments, validation, predictable return data, idempotency, check mode behavior, and useful error messages. Package reusable modules in a collection when they belong to a broader content set.

Keep modules narrow. A module should model one resource or operation boundary, not hide an entire playbook. Test module behavior independently and through playbooks that consume it.

## Implementation moves

- Compare existing modules, action plugins, roles, and collection options before writing code.
- Define argument spec, required parameters, defaults, mutually exclusive options, and validation.
- Implement read-before-write logic so the module knows whether change is needed.
- Return accurate `changed`, `failed`, and structured result data.
- Support check mode where prediction is possible.
- Use module utilities for shared code instead of copying helpers.
- Document the module using Ansible's expected documentation structure.
- Package reusable modules in a collection and test them in CI.

## Checks

- Is there no maintained module that already solves the problem?
- Does the module model desired state rather than hiding a long script?
- Are arguments validated before target mutation?
- Does `changed` mean the target actually changed?
- Does check mode avoid mutation and still produce useful output?
- Is the module documented and tested from a clean runner?

## Failure modes

- Writing a custom module before searching existing collections.
- Moving a monolithic shell script into a module without improving state semantics.
- Returning `changed: true` for every successful execution.
- Ignoring check mode and breaking dry-run workflows.
- Keeping local modules outside collection or library paths where CI and controller jobs cannot find them.

## Agent trigger hints

Use this pattern when the user says or implies:

- write a custom Ansible module
- shell task is too complex
- supports_check_mode
- AnsibleModule argument_spec
- changed true every time
- package module in collection

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 19 on custom modules, argument handling, changed results, documentation, and check mode; Chapter 15 on collections; Chapter 10 on complex playbook alternatives; and Chapter 24 on choosing the right tool. No source excerpts are stored here.
