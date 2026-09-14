---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the requirements an XDM Experience Event schema must meet so that streamed events can be ingested into Adobe Experience Platform and used to trigger Journey Optimizer journeys.

**Intents:**

* Understand that Journey Optimizer events are XDM Experience Events sent to Adobe Experience Platform via Streaming Ingestion
* Build an XDM schema of the ExperienceEvent class for journey events
* Add the Orchestration eventID field group for system-generated events
* Declare an identity field to identify individual profiles in the event
* Mark the schema and dataset for profile so the data is available for profile

**Glossary:**

* **XDM ExperienceEvent class**: The class the schema must belong to for use with Journey Optimizer events *(product-specific)*
* **Orchestration eventID field group**: The field group that must be included for system-generated events, which Journey Optimizer uses to identify events used in journeys *(product-specific)*
* **Identity map**: The fallback that can be used to identify individual profiles when no identity field is specified, which is not recommended *(product-specific)*
* **Streaming Ingestion**: The mechanism by which XDM Experience Events are sent to Adobe Experience Platform *(product-specific)*

**Guardrails:**

* The schema must be of the XDM ExperienceEvent class.
* For system-generated events, the schema must include the Orchestration eventID field group.
* An identity field should be declared to identify individual profiles; if no identity is specified, an identity map can be used, which is not recommended.
* To make the data available for profile, mark the schema and dataset for profile.
* Starting July 8, 2025, new customer organizations cannot create expressions using experience event attributes in journey conditions.
* Starting April 1, 2026, organizations that have not accessed experience events via journey expressions in the last 90 days will no longer have access to this capability; accessing context from the starting event of a journey is not impacted.

**Terminology:**

* Canonical name: XDM ExperienceEvent schema — Acronym: XDM — variants: XDM Experience Event schema, ExperienceEvent class schema
* Do not confuse: "identity field" (declared field for identifying individual profiles, recommended) ≠ "identity map" (fallback used when no identity is specified, not recommended)

**FAQ:**

* **Q: What class must the schema use?** — The schema must be of the XDM ExperienceEvent class.
* **Q: What is required for system-generated events?** — The schema must include the Orchestration eventID field group, which Journey Optimizer uses to identify events used in journeys.
* **Q: Is a dataset required for the events?** — Having a dataset is not strictly necessary, but sending events to a specific dataset lets you maintain users' event history for future reference and analysis.
* **Q: What happens if I do not declare an identity field?** — An identity map can be used instead, but this is not recommended.
* **Q: Are experience event attributes in journey conditions still available?** — Starting July 8, 2025, new customer organizations cannot create such expressions, and starting April 1, 2026, organizations that have not accessed them via journey expressions in the last 90 days lose access; accessing context from the starting event is not impacted.

+++

<!-- ai-section-version: 1 | source-hash: 78b1a882 -->
