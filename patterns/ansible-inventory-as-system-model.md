---
id: iac.ansible-inventory-as-system-model
title: Ansible Inventory As System Model
type: architecture-pattern
status: draft
summary: Model hosts, groups, connection data, ownership, and runtime discovery in inventory so playbooks can target systems deliberately without embedding topology assumptions.
tags:
  - infrastructure-as-code
  - ansible
  - inventory
  - configuration-management
  - topology
  - runtime-operations
  - platform-engineering
aliases:
  - ansible inventory design
  - group_vars host_vars
  - inventory as topology
  - dynamic inventory model
applies_when:
  - Ansible playbooks manage more than a few hosts, environments, roles, or ownership groups.
  - Host membership changes through cloud provisioning, CMDB data, or inventory plugins.
  - Teams need reusable projects that can run against different inventories.
avoid_when:
  - A tiny local lab can be represented clearly with an inline or one-file inventory.
  - Another platform owns targeting completely and Ansible only receives an already-scoped host list.
related:
  - iac.externalized-configuration
  - iac.ansible-variable-precedence-contract
  - iac.ansible-cloud-dynamic-inventory
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 4, 5, 11, 17, 21, 23, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Inventory As System Model

## Intent

Represent the managed system in inventory: which hosts exist, how they group by function or environment, how Ansible connects to them, and which variables describe their role in the system.

## Use when

- Playbooks need to target web, database, network, Windows, cloud, or application groups differently.
- Environments share playbooks but differ in host membership and credentials.
- Inventory data comes from cloud APIs, network devices, generated files, or Automation Controller.
- Operators need to inspect target membership before running a play.
- Infrastructure owners and playbook authors are different people.

## Avoid when

- The inventory is only a temporary bootstrap target and will be replaced by a managed source.
- Encoding topology in inventory would duplicate a more authoritative system without synchronization.
- The playbook should act on a single explicit host passed by an external orchestrator.

## Context and problem

Ansible separates projects from inventories, but teams often let topology leak into playbooks through hardcoded hostnames, environment conditionals, and special-case tasks. That makes projects less reusable and makes it hard to see which systems a run will affect.

Inventory is more than a host list. It can express groups of groups, aliases, ports, connection mechanisms, host and group variables, network inventory, cloud-discovered hosts, and controller-managed ownership. A deliberate inventory model makes playbooks simpler and run scope more auditable.

## Forces

- Static inventory is easy to review, but dynamic environments need discovery.
- Functional group names help playbooks stay reusable, but ownership and access boundaries must still be visible.
- Host variables are convenient, but variable sprawl makes precedence hard to reason about.
- Inventory plugins reduce duplication, but they introduce API latency, caching, and credential concerns.
- Automation Controller can separate projects and inventories, but only if the repository layout supports that separation.

## Guidance

Keep playbooks focused on desired behavior and put target identity, grouping, connection details, and environment-specific facts in inventory or inventory-backed variable files. Group hosts by function, role, environment, and operational boundary when those groupings drive different tasks or permissions. Use dynamic inventory when a provider or CMDB is the source of truth, and cache inventory deliberately when discovery is expensive.

Maintain a reviewable path from a playbook run to the affected hosts. Operators should be able to list inventory, inspect group graphs, and understand which host variables will apply before a change is executed.

## Implementation moves

- Separate project repositories from inventory repositories when teams or environments differ.
- Use `group_vars` and `host_vars` for inventory-scoped data instead of hardcoding values in plays.
- Prefer functional group names that describe system role, such as `web`, `db`, `network`, or `bastion`.
- Use groups of groups for environment or stack composition when the relationship matters.
- Configure connection variables close to the inventory source for Linux, Windows, network devices, and cloud targets.
- Use dynamic inventory plugins or scripts for cloud and CMDB-backed host membership.
- Enable inventory caching when discovery latency or API rate limits make repeated calls expensive.
- Run inventory graph or list commands as part of review and troubleshooting.

## Checks

- Can the same project run against staging and production by changing inventory, not playbook code?
- Can reviewers see which hosts are targeted by each play?
- Are inventory variables placed at the narrowest useful scope?
- Are dynamic inventory credentials, cache TTLs, and failure behavior documented?
- Can infrastructure owners update inventory access without editing reusable playbook logic?

## Failure modes

- Hardcoding hostnames or environment branches inside reusable playbooks.
- Mixing secrets, connection details, topology, and role defaults without a clear precedence model.
- Trusting dynamic inventory without cache invalidation, tags, or ownership metadata.
- Using group names that reflect accidents of implementation instead of operational roles.
- Letting Automation Controller projects and inventories drift from the repository layout.

## Agent trigger hints

Use this pattern when the user says or implies:

- design Ansible inventory
- group_vars or host_vars
- dynamic inventory
- inventory plugin
- separate inventory from playbooks
- target hosts safely

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapters 4 and 5 on inventory and variables, Chapter 11 on host patterns and run targeting, Chapter 17 on cloud dynamic inventory, Chapter 21 on network inventory, Chapter 23 on controller inventories, and Chapter 24 on decoupling projects from inventories. No source excerpts are stored here.
