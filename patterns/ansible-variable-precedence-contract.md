---
id: iac.ansible-variable-precedence-contract
title: Ansible Variable Precedence Contract
type: design-pattern
status: draft
summary: Treat Ansible variable sources and precedence as an explicit contract so defaults, inventory values, secrets, facts, and overrides do not silently fight each other.
tags:
  - infrastructure-as-code
  - ansible
  - configuration-management
  - parameterization
  - variable-precedence
  - secrets-management
  - operability
aliases:
  - ansible variable precedence
  - group_vars host_vars precedence
  - ansible defaults versus vars
  - extra vars override
applies_when:
  - A playbook or role reads values from defaults, vars, inventory, facts, vault files, templates, or extra vars.
  - Different environments need different values without forking the playbook.
  - Operators need to debug why a value was selected.
avoid_when:
  - A role has no external configuration and fixed values are clearer.
  - The value is produced at runtime and should not be configurable by inventory or callers.
related:
  - iac.externalized-configuration
  - iac.ansible-inventory-as-system-model
  - iac.ansible-vault-secret-boundary
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 5, 7, 9, 10, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Variable Precedence Contract

## Intent

Make variable ownership, override order, and safe customization points explicit so Ansible configuration remains predictable as roles, inventories, facts, and secrets accumulate.

## Use when

- Role defaults are intended for callers to override.
- Role vars should remain internal implementation details.
- Inventory variables differ by host, group, environment, or ownership boundary.
- Extra vars are used for emergency overrides or deployment decisions.
- Templates combine facts, inventory, vault data, and role parameters.

## Avoid when

- The value is local to a single task and does not need to be part of a public contract.
- A hardcoded safe default is better than exposing a knob that users will misconfigure.
- The team cannot explain which variable source should win.

## Context and problem

Ansible makes variable use easy, but its power comes with a precedence model that can surprise contributors. The same logical setting can appear in role defaults, role vars, group vars, host vars, facts, vault files, registered variables, and extra vars. If a team does not define what each source is for, changes become difficult to review and debugging becomes guesswork.

The Ansible source repeatedly distinguishes defaults that users may override, vars that usually should not be changed, group and host inventory values, facts discovered from hosts, and extra vars that have very high precedence. A pattern is needed to turn those mechanics into a configuration contract.

## Forces

- Flexible overrides versus predictable role behavior.
- DRY configuration versus local clarity at the inventory boundary.
- Environment-specific values versus reusable playbook code.
- Secure secret placement versus easy template rendering.
- Runtime facts versus declared desired state.

## Guidance

Design variable sources intentionally. Put public role inputs in defaults, keep internal constants out of caller override paths, put environment and host variation in inventory, put secrets in encrypted or external secret sources, and reserve extra vars for explicit operator or pipeline decisions. Document the variables a role accepts and the sources that are allowed to override them.

When debugging, inspect the resolved host variables and the path by which the value was provided. If a variable can be set in many places, narrow the accepted sources rather than relying on everyone remembering precedence details.

## Implementation moves

- Classify variables as role input, role internal, inventory data, fact-derived data, secret, or run-time override.
- Put overrideable role inputs in `defaults/main.yml`.
- Avoid putting caller-customizable values in role `vars` unless they are intentionally hard to override.
- Place environment and host values in `group_vars` or `host_vars` at the narrowest useful scope.
- Keep secret values in vault files or external secret lookups, not plain inventory.
- Use namespaced variable names for shared roles to reduce collisions.
- Document required variables, defaults, sensitive variables, and accepted override mechanisms.
- Add assertions for missing or invalid variables before destructive tasks run.

## Checks

- Can a reviewer tell where each important value should be set?
- Are role defaults safe and intentionally overrideable?
- Are internal role values protected from accidental inventory overrides?
- Are secrets separated from nonsecret variables and encrypted or externally sourced?
- Are extra vars used deliberately rather than as a workaround for unclear ownership?
- Is there an assertion or validation for values that can damage infrastructure?

## Failure modes

- Defining the same variable in multiple places and relying on precedence trivia.
- Putting secrets in plain inventory because templates need easy access.
- Using extra vars in pipelines until normal environment configuration is bypassed.
- Making role vars public by accident, then breaking consumers when refactoring.
- Letting facts override desired state without checking whether the fact is current or relevant.

## Agent trigger hints

Use this pattern when the user says or implies:

- Ansible variable precedence
- where should this Ansible variable live
- group_vars versus host_vars
- role defaults versus vars
- extra vars override everything
- Ansible picked the wrong value

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 5 on variables, facts, and precedence; Chapter 7 on application variables and secrets; Chapter 9 on role defaults and vars; Chapter 10 on lookups and vault data; and Chapter 24 on role and inventory organization. No source excerpts are stored here.
