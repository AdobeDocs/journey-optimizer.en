---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to browse, build, and manage Adobe Experience Platform audiences in Adobe Journey Optimizer and target them in journeys and campaigns.

**Intents:**

* Browse and manage audiences from the Customer > Audiences menu and the Audience Portal
* Understand the different audience types available (segment definitions, custom upload, audience composition, Federated Audience Composition)
* Understand how segment-definition audiences are refreshed by evaluation type (streaming, batch, edge)
* Target audiences when building journeys or creating campaigns
* Monitor how audience activation counts toward the Engageable Profiles license metric

**Glossary:**

* **Audience**: A collection of people who share similar behaviors and/or characteristics, configured and maintained on Adobe Experience Platform using the Segmentation Service and accessible in Journey Optimizer *(product-specific)*
* **Audience Portal**: The Adobe Experience Platform area where audiences are managed, found, and explored with standardized labeling, governance controls, searchable folders, and tags *(product-specific)*
* **Segment definition**: A method of generating an audience using Adobe Experience Platform Segmentation Service, refreshed at different times depending on its evaluation type *(product-specific)*
* **Custom upload**: An audience type imported from a CSV file *(product-specific)*
* **Audience composition**: A composition workflow that combines existing audiences on a visual canvas using actions such as rank, split, and join to create new audiences *(product-specific)*
* **Federated Audience Composition**: A capability to federate datasets directly from an existing data warehouse to build and enrich Adobe Experience Platform audiences and attributes *(product-specific)*
* **Engageable Profiles**: The license metric that counts profiles engaged through an audience activation *(product-specific)*

**Guardrails:**

* Streaming segmentation audiences are updated in real time as new data flows in.
* Batch segmentation audiences are refreshed every 24 hours; when used in journeys, newly qualified segment members may not appear until the next snapshot.
* Edge segmentation audiences are evaluated instantaneously on the edge.
* Profiles engaged through an audience activation (journey, campaign, or decisioning activity) count toward the organization's Engageable Profiles license metric; each profile is counted once per sandbox over a rolling 12-month window.

**Terminology:**

* Canonical name: Audience — Acronym: n/a — variants: segment, audiences
* Synonyms: "Audiences menu" = "Customer > Audiences"
* Do not confuse: "Streaming segmentation" (updated in real time) ≠ "Batch segmentation" (refreshed every 24 hours) ≠ "Edge segmentation" (evaluated instantaneously on the edge)
* Do not confuse: "Segment definition" (build a new audience definition with Segmentation Service) ≠ "Custom upload" (import an audience from a CSV file) ≠ "Audience composition" (combine existing audiences on a visual canvas)

**FAQ:**

* **Q: Where do I find audiences in Journey Optimizer?** — From the Customer > Audiences menu.
* **Q: What methods can generate an audience?** — Segment definitions, custom upload (CSV), audience composition, and Federated Audience Composition.
* **Q: How often are audiences refreshed?** — It depends on the evaluation type: streaming updates in real time, batch refreshes every 24 hours, and edge is evaluated instantaneously on the edge.
* **Q: Does using an audience affect my license metric?** — Yes; profiles engaged through an audience activation count toward the Engageable Profiles metric, each counted once per sandbox over a rolling 12-month window.

+++

<!-- ai-section-version: 1 | source-hash: 1b27bf17 -->
