---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents the legacy `inSegment` function, which checks whether a journey profile belongs to a named Adobe Experience Platform audience and returns a boolean.

**Intents:**
* Check if a profile is an active member of a named audience using `inSegment`
* Use `inSegment('name') == true` to confirm realized (active) audience membership in a journey condition
* Use `inSegment('name') == false` to confirm exited (inactive) audience membership

**Glossary:**
* **Realized**: Audience participation status meaning the entity currently qualifies for the segment definition *(product-specific)*
* **Exited**: Audience participation status meaning the entity is leaving or has left the segment definition *(product-specific)*

**Guardrails:**
* Up to 100 audiences can be retrieved in a single journey
* The audience name must be a string constant; field references and expressions are not supported as parameters

**Terminology:**
* Canonical name: inSegment — Acronym: none — variants: inAudience (current preferred function)
* Synonyms: "inSegment" = "audience membership check" (legacy)
* Do not confuse: "inSegment" (legacy/deprecated function) ≠ "inAudience" (current recommended function)
* Do not confuse: "realized" (active member) ≠ "exited" (no longer a member)

**FAQ:**
* **Q: What is the difference between `inSegment` and `inAudience`?** — `inSegment` is the legacy function name; `inAudience` is the current recommended function. Both check audience membership, but `inAudience` has more complete documentation including guardrails and propagation timing details.
* **Q: What does `inSegment('name') == true` mean?** — It means the profile has a "realized" segmentMembership status, i.e., the individual is an active member of the audience.
* **Q: Can I pass a dynamic expression as the audience name?** — No, the audience name must be a string constant; field references and expressions are not supported.
* **Q: How many audiences can I evaluate in one journey?** — Up to 100 audiences can be retrieved within a single journey.

+++
