---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how Federated Audience Composition in Journey Optimizer queries an enterprise data warehouse to build and enrich Adobe Experience Platform audiences without duplicating sensitive data.

**Intents:**

* Query a data warehouse for data or profile attributes to use in composing audiences
* Enrich Adobe Experience Platform audiences for deeper personalization using enterprise data warehouse and trusted partner data
* Compose audiences from both profile-based and non-profile data while leaving sensitive data in the warehouse
* Use an audience created through Federated Audience Composition (a federated audience) in a journey or a campaign

**Glossary:**

* **Federated Audience Composition**: A Journey Optimizer capability that queries a data warehouse for data or profile attributes to compose audiences, leaving sensitive data in the warehouse and avoiding data duplication; using it requires the Federated Audience Composition add-on *(product-specific)*
* **Federated audience**: An audience created using Federated Audience Composition (federated data), in which audiences are queried and composed from external data warehouses without copying data into Adobe Experience Platform; it can be selected in journeys and campaigns *(product-specific)*

**Guardrails:**

* Federated Audience Composition leaves sensitive data in the warehouse and avoids data duplication.
* Using Federated Audience Composition audiences requires the Federated Audience Composition add-on.
* The performance of a federated audience depends on the query capabilities of the external data warehouse.
* You can select a federated audience in campaigns and journeys.
* In journeys, a federated audience is supported in Read Audience and Condition activities. It is not supported in Audience Qualification activities, because of the batch nature of these audiences; only audiences created using segment definitions can be used in an Audience Qualification activity.
* A federated audience is a static composition, updated when the federated audience composition is executed: its members stay the same until the next execution.
* The identity namespace of the audience must match the journey namespace.
* Preview and proof are currently not supported for audiences created using Federated Audience Composition.
* Incremental read is not functionally supported for Federated Audience Composition audiences: on each recurrence of a Read Audience activity, the entire audience is processed, regardless of the Incremental read toggle.

**Terminology:**

* Canonical name: Federated Audience Composition — Acronym: FAC — variants: Federated Audience Composition add-on
* Canonical name: Federated audience — variants: Federated Data Audience, FAC audience
* Do not confuse: "Federated Audience Composition" (FAC; the capability that queries the data warehouse and composes audiences) ≠ "federated audience" (an audience created using that capability, which you select in a journey or campaign)

**FAQ:**

* **Q: What does Federated Audience Composition do?** — It queries a data warehouse for data or profile attributes to use in composing audiences, leaving sensitive data in the warehouse and avoiding data duplication.
* **Q: What kinds of data can it use?** — Both profile-based data and non-profile data.
* **Q: How does it help with sensitive data?** — It leaves sensitive data in the warehouse and avoids data duplication.
* **Q: What is the difference between Federated Audience Composition and a federated audience?** — Federated Audience Composition (FAC) is the capability that queries the data warehouse and composes audiences. A federated audience is an audience created using it, which you can then select in a journey or campaign.
* **Q: Where can I use a federated audience in a journey?** — In Read Audience and Condition activities. It cannot be used in an Audience Qualification activity.
* **Q: When is a federated audience updated?** — It is a static composition that is updated when the federated audience composition is executed, so its members stay the same until the next execution.
* **Q: Can I use enrichment attributes from a federated audience?** — Yes. When targeting an audience created using Federated Audience Composition, you can use its enrichment attributes to build your journey and personalize your messages.

**Examples:**

* A quick-service restaurant group enriches the profiles of customers that recently placed orders online with each customer's preferred restaurant location, and sends them offers that can be used at those preferred locations.
* Federated audiences are best for enterprise data warehouse integration, audience composition using external data sources, and scenarios requiring data to remain in external systems.

+++

<!-- ai-section-version: 2 | source-hash: 557cbac8 | related: audience/target-audiences.md, building-journeys/journey-faq.md, building-journeys/read-audience.md, audience/enrichment-attributes.md -->
