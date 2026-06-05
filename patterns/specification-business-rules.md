---
id: ddd.specification-business-rules
title: Specification Business Rules
type: architecture-pattern
status: draft
summary: Represent important predicates and selection rules as named, composable domain concepts instead of scattering conditionals.
tags:
  - domain-driven-design
  - business-rules
  - specifications
  - query-patterns
  - domain-modeling
  - declarative-design
aliases:
  - specification pattern
  - business rule object
  - domain predicate
applies_when:
  - The same eligibility, validation, routing, or selection rule appears in multiple forms.
  - A rule is important to the domain but does not naturally belong to one entity or value object.
avoid_when:
  - The condition is local, trivial, and unlikely to be reused or discussed by domain experts.
  - Turning the rule into an object would hide a simple invariant that belongs inside an aggregate.
related:
  - ddd.aggregate-lifecycle-boundary
  - ddd.supple-domain-design
  - data.declarative-query-boundaries
sources:
  - "book: Eric Evans, Domain-Driven Design, 2003 final manuscript; Chapter 9: Making Implicit Concepts Explicit and Chapter 10: Supple Design"
source_confidence: high
last_reviewed: 2026-06-05
---

# Specification Business Rules

## Intent

Make domain rules explicit, reusable, testable, and combinable.

## Use when

- A business rule is duplicated in validation, search, reporting, and workflow decisions.
- Domain experts name a rule or policy, but code only contains low-level conditionals.
- A repository needs expressive search criteria that should remain meaningful in the domain model.
- Rules need to be combined, compared, or explained.

## Avoid when

- The rule is a private helper with no domain significance.
- The rule is an aggregate invariant that must always be enforced by the aggregate root.
- The persistence technology cannot support the specification and a simpler query object would be clearer.

## Context and problem

Many domain rules are predicates: a cargo is suitable for a route, a customer is delinquent, a container satisfies constraints, or an asset qualifies for a process. When those rules are embedded as scattered `if` statements, SQL fragments, UI validations, and report filters, the conceptual unity is lost and contradictions appear.

## Forces

- Rule reuse versus object proliferation
- Domain expression versus query translation limits
- Composability versus readability
- Centralized rule meaning versus aggregate-owned invariants

## Guidance

Extract important predicates into specification objects or equivalent named domain constructs. Let the specification state what is being tested in the ubiquitous language, while infrastructure or repositories translate it when persistence search is needed. Compose specifications when the domain combines rules, but keep combinations understandable to domain experts.

Specifications are not a dumping ground for all logic. Use them when a rule has independent meaning, crosses use cases, or needs to be passed, combined, tested, or queried.

## Implementation moves

- Find duplicated conditionals that represent the same domain decision.
- Give the rule a name from the ubiquitous language.
- Define a small interface for checking whether a candidate satisfies the rule.
- Add tests that describe the rule in domain examples.
- Let repositories accept specifications for domain-level search when practical.
- Keep database-specific translation outside the domain object.
- Compose rules with named operations only when the combination has clear meaning.

## Checks

- Can domain experts recognize and discuss the rule by name?
- Is the same rule no longer duplicated across validation, query, and workflow code?
- Are specifications tested independently from persistence translation?
- Does combining specifications preserve clear business meaning?

## Failure modes

- Creating generic rule engines that hide domain language.
- Letting specifications bypass aggregate invariants.
- Mixing SQL or framework details into the domain rule.
- Splitting every small condition into a class before it has domain weight.

## Agent trigger hints

Use this pattern when the user says or implies:

- specification pattern
- reusable business rules
- duplicated conditionals
- domain predicate
- complex search criteria

## Source notes

Synthesized from Chapters 9 and 10 in `work/book-domain-driven-design/chapter-out/`, including explicit concepts, specifications, and declarative specification composition. This file stores original guidance and source pointers only.
