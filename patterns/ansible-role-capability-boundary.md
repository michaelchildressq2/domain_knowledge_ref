---
id: iac.ansible-role-capability-boundary
title: Ansible Role Capability Boundary
type: design-pattern
status: draft
summary: Design Ansible roles as small, documented, versioned capabilities with clear defaults, dependencies, handlers, and test scenarios.
tags:
  - infrastructure-as-code
  - ansible
  - roles
  - module-boundaries
  - composability
  - versioning
  - testing
aliases:
  - ansible role design
  - role boundary
  - role requirements yml
  - reusable ansible roles
applies_when:
  - A task set will be reused across playbooks, projects, teams, or environments.
  - Ansible content needs a convention-based layout for tasks, handlers, templates, files, defaults, and variables.
  - Role dependencies must be installed or versioned consistently.
avoid_when:
  - The tasks are unique to one playbook and extracting a role would hide the workflow.
  - A collection, module, or external tool is a better abstraction for the capability.
related:
  - iac.component-boundaries
  - iac.terraform-production-module-design
  - iac.ansible-molecule-role-quality-gate
  - iac.ansible-collection-dependency-manifest
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 9, 14, 15, 22, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Role Capability Boundary

## Intent

Package reusable Ansible behavior as a role that does one coherent thing, exposes safe defaults, declares dependencies, and can be tested independently before it is composed into larger playbooks.

## Use when

- The same configuration behavior appears in multiple playbooks.
- A service, package, hardening baseline, image preparation step, or application component has a stable lifecycle.
- Role consumers need documented variables and handlers.
- A team wants to share content through Galaxy, a private repository, or a collection.
- CI/CD needs a unit of Ansible content to lint and test.

## Avoid when

- The role would contain unrelated services simply because they are deployed together today.
- The behavior is a one-off orchestration sequence that is clearer inline.
- A custom module is needed because the work is procedural, stateful, or too complex for tasks.
- Dependencies are unstable and extracting a shared role would freeze the wrong boundary.

## Context and problem

Ansible roles provide a convention-based directory structure that automatically loads tasks, handlers, files, templates, defaults, and variables. That convention makes reuse easy, but it can also encourage large roles that mix several concerns, hide dependencies, or expose unclear variable contracts.

The Ansible source treats roles as the basic reusable component for many projects, recommends role dependency manifests, distinguishes project roles from shared and Galaxy roles, and pairs roles with Molecule tests. This pattern turns role layout into a capability boundary.

## Forces

- Reuse versus readability of the top-level playbook.
- Small roles versus excessive wiring and dependency management.
- Flexible defaults versus stable behavior.
- Shared Galaxy roles versus locally owned implementation details.
- Role dependencies versus explicit playbook composition.

## Guidance

Make each role responsible for one coherent system capability. Expose overrideable defaults for supported customization, keep internal variables private, and make handler notifications part of the role contract. Declare external role and collection dependencies in manifests rather than assuming they are installed.

Treat a role as releasable content. It should have a README, supported platforms, variable documentation, examples, lint rules, and Molecule scenarios or equivalent tests. If a role becomes a bundle of roles, modules, and plugins, move the distribution boundary toward a collection.

## Implementation moves

- Name the role after the capability it owns, not after a temporary project.
- Keep `tasks`, `handlers`, `templates`, `files`, `defaults`, and `vars` aligned with the role's public contract.
- Put caller-facing variables in defaults and document them.
- Keep internal variables in role vars or task-local scope when callers should not override them.
- Use handlers for restart and reload behavior caused by changed tasks.
- Declare dependencies in `requirements.yml` or collection manifests.
- Version shared roles and require consumers to pin versions.
- Add Molecule scenarios for supported platforms and major configuration modes.

## Checks

- Can the role be described as one capability?
- Are role inputs, outputs, dependencies, and handlers documented?
- Can the role be tested without running an entire production playbook?
- Are dependencies declared and versioned?
- Are defaults safe for new users and overrideable for expected variation?
- Does the role avoid reaching into unrelated inventory or project state?

## Failure modes

- Creating a monolithic role that configures an entire stack.
- Hiding hard dependencies on other roles, collections, binaries, or facts.
- Putting user-tunable variables in `vars` and then forcing awkward overrides.
- Publishing a role without tests or supported-platform evidence.
- Using role dependencies where explicit playbook composition would be easier to review.

## Agent trigger hints

Use this pattern when the user says or implies:

- design an Ansible role
- split playbook into roles
- role defaults and vars
- requirements.yml
- Galaxy role
- reusable Ansible content

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 9 on roles and role requirements, Chapter 14 on Molecule role testing, Chapter 15 on collections, Chapter 22 on CI/CD for roles, and Chapter 24 on decoupling roles and collections. No source excerpts are stored here.
