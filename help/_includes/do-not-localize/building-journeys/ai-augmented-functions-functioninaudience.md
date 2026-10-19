---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents the `inAudience` function, which checks in real-time whether a journey profile belongs to a named Adobe Experience Platform audience and returns a boolean used in journey conditions.

**Intents:**
* Branch a journey path based on whether a profile is a member of a specific audience using `inAudience`
* Combine multiple `inAudience` checks with AND/OR logic to create complex targeting conditions
* Verify that a profile has not entered a specific audience using a negation check (`inAudience("...") == false`)
* Understand the propagation timing differences between Read Audience journeys and unitary event journeys
* Identify and fix broken audience references caused by audience renames in Adobe Experience Platform

**Glossary:**
* **Realized**: Audience participation status indicating the individual currently qualifies for the audience definition and is an active member *(product-specific)*
* **Exited**: Audience participation status indicating the individual has left the audience and no longer qualifies *(product-specific)*
* **Merge policy**: A rule in Adobe Experience Platform that determines how profile data from multiple datasets is combined when evaluating audience membership *(product-specific)*
* **Batch projection**: The profile data store refreshed on a schedule (within 2 hours after ingestion) used by Read Audience journeys *(product-specific)*
* **Streaming projection**: The real-time profile data store (typically available within 15 minutes) used in unitary event journeys and after Wait activities *(product-specific)*

**Guardrails:**
* A single journey can retrieve up to 100 audiences
* The audience name parameter must be a string constant; field references and dynamic expressions are not supported
* Renaming an audience in Adobe Experience Platform does not automatically update `inAudience` references in journey expressions — manual updates are required
* Inconsistent merge policies across multiple audiences used in the same journey can cause errors or alerts

**Terminology:**
* Canonical name: inAudience — Acronym: none — variants: inSegment (legacy name)
* Synonyms: "inAudience" = "audience membership check function"
* Do not confuse: "Realized" (active member) ≠ "Exited" (no longer a member)
* Do not confuse: "inAudience" (current function) ≠ "inSegment" (deprecated legacy function)

**FAQ:**
* **Q: What does `inAudience` return when a profile has exited the audience?** — It returns `false`; only profiles with "Realized" status are considered active members and return `true`.
* **Q: How many audiences can I check in a single journey?** — Up to 100 audiences can be retrieved within a single journey.
* **Q: What happens if I rename an audience in Adobe Experience Platform after using it in a journey?** — The journey expression is not updated automatically; you must manually edit the `inAudience` call to use the new audience name, otherwise the condition will break.
* **Q: How quickly is audience membership available after a profile update in a Read Audience journey?** — In a Read Audience journey before a Wait activity, data is read from the batch projection refreshed within 2 hours after ingestion.
* **Q: Can I pass a profile attribute as the audience name parameter?** — No, the audience name must be a string constant; field references and expressions are not supported.

+++
