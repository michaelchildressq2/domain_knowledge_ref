---
id: iac.ansible-cloud-dynamic-inventory
title: Ansible Cloud Dynamic Inventory
type: operational-practice
status: draft
summary: Drive Ansible cloud runs from provider inventory plugins, resource tags, and cache controls instead of hand-maintained host lists.
tags:
  - infrastructure-as-code
  - ansible
  - cloud
  - dynamic-inventory
  - tagging
  - runtime-operations
  - scalability
aliases:
  - Ansible cloud inventory
  - dynamic inventory plugin
  - EC2 inventory
  - cloud resource tags
applies_when:
  - Hosts are created, destroyed, or grouped by cloud provider APIs.
  - Ansible needs to target cloud instances by tags, regions, VPCs, roles, or lifecycle state.
  - Static inventories drift from the actual provider state.
avoid_when:
  - Host membership is stable, small, and owned manually.
  - A CMDB or deployment platform is the authoritative inventory source instead of the cloud provider.
related:
  - iac.ansible-inventory-as-system-model
  - iac.resource-matching
  - iac.remote-iac-testing
sources:
  - "book: Bas Meijer, Lorin Hochstein, and Rene Moser, Ansible: Up and Running, third edition; Chapters 4, 17, 20, and 24."
source_confidence: high
last_reviewed: 2026-06-05
---

# Ansible Cloud Dynamic Inventory

## Intent

Keep Ansible's target model aligned with changing cloud infrastructure by discovering hosts from provider APIs, using meaningful resource tags, and controlling inventory cache behavior.

## Use when

- Cloud instances are autoscaled, rebuilt, or provisioned outside the Ansible project.
- The same playbook targets resources by environment, role, application, VPC, region, or lifecycle state.
- Inventory files are becoming stale or duplicated from provider metadata.
- API calls are expensive enough to require caching.
- Operators need to inspect discovered hosts before applying changes.

## Avoid when

- The provider API is not authoritative for the host set.
- Required cloud credentials are too broad for the intended Ansible operation.
- Inventory cache staleness would be more dangerous than manual updates.
- Tags are missing, inconsistent, or not governed.

## Context and problem

Static inventories do not age well in elastic cloud environments. Instances appear and disappear, IP addresses change, and host role is often captured in provider metadata or tags. Hand-maintained inventory duplicates provider truth and fails at the moment automation needs accuracy.

The Ansible source shows cloud modules, resource tags, dynamic inventory, inventory plugins, and inventory caching. The operational pattern is to make tagging and plugin configuration part of the automation contract, not an afterthought.

## Forces

- Fresh provider discovery versus slower API calls and rate limits.
- Tag-driven grouping versus weak tag governance.
- Broad cloud credentials versus least-privilege inventory access.
- Cached inventory speed versus stale host membership.
- Cloud-native grouping versus reusable playbook group names.

## Guidance

Use provider inventory plugins for cloud-managed hosts and make resource tags meaningful enough to drive grouping. Define which tags are required for Ansible targeting, ownership, lifecycle, and cleanup. Configure inventory caching deliberately, with TTLs that match the volatility and risk of the environment.

Do not let dynamic inventory become invisible magic. Operators should be able to list the inventory, inspect generated groups, understand filters, and know which credentials were used for discovery.

## Implementation moves

- Choose the maintained provider inventory plugin for the target cloud.
- Define required tags for application, environment, role, owner, lifecycle, and cost or cleanup metadata.
- Filter inventory by explicit regions, accounts, subscriptions, projects, VPCs, or tag expressions.
- Use inventory cache backends and TTLs appropriate to API cost and change frequency.
- Scope cloud credentials to discovery and required operations.
- Run inventory listing in CI or preflight checks for critical playbooks.
- Align discovered groups with playbook group names and role boundaries.

## Checks

- Are all targetable cloud resources tagged consistently?
- Can the inventory plugin be run from a clean control-node runtime?
- Are discovery credentials least-privilege?
- Is cache TTL documented and safe for the expected rate of infrastructure change?
- Can operators inspect discovered groups before a production run?
- Does the playbook behave safely when no hosts match?

## Failure modes

- Running against stale cached inventory after cloud resources changed.
- Targeting by loose tags that match unrelated resources.
- Giving inventory discovery credentials broad write permissions.
- Hardcoding cloud instance IPs while claiming to use dynamic inventory.
- Hiding provider filters in local config that CI and controller jobs do not use.

## Agent trigger hints

Use this pattern when the user says or implies:

- Ansible dynamic inventory
- cloud inventory plugin
- target EC2 or cloud hosts by tag
- inventory cache
- Ansible cloud resources
- stale inventory

## Source notes

Synthesized from Ansible: Up and Running, third edition, especially Chapter 4 on dynamic inventory basics, Chapter 17 on cloud tags, inventory plugins, and caching, Chapter 20 on caching behavior, and Chapter 24 on decoupled inventories. No source excerpts are stored here.
