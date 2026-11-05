---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the Adobe Experience Platform identities, profile attributes, experience events, audiences, and datasets that Loyalty Challenges requires, and explains how dataset time-to-live affects data retention.

**Intents:**

* Identify which Adobe Experience Platform profile attributes, experience events, audiences, and datasets support Loyalty Challenges.
* Align the identity namespace used for Loyalty Challenges with how members are identified in profile data.
* Configure event mappings so marketers can enter custom event values in the task builder.
* Ingest external loyalty data into Adobe Experience Platform using Sources connectors.
* Understand how dataset time-to-live affects retention of loyalty-related data.

**Glossary:**

* **Loyalty configurations**: the menu where reward fulfillment and event mapping are configured *(product-specific)*
* **Global settings**: the area within the Loyalty configurations menu where the identity namespace is selected *(product-specific)*
* **Loyalty Details**: the Experience Platform schema field group that defines the `loyalty` object and its properties (for example `points`, `tier`, `program`, and `status`) *(product-specific)*
* **Purchase, Spend, Custom event tasks**: task types that depend on experience events ingested into Adobe Experience Platform *(product-specific)*
* **Dataset time-to-live (TTL)**: controls how long data is retained in the data lake and, when applicable, in the Profile store *(product-specific)*

**Guardrails:**

* Event payloads must use the same identity namespace as the Loyalty Challenges configuration so progress can be attributed to the correct profile.

**Prerequisites and permissions:**

* Matching event mappings (event name, Experience event schema, and field mappings) must be configured in the Loyalty configurations menu before marketers can enter custom event values in the task builder for Custom event tasks.

**Terminology:**

* Acronym: TTL — Time-to-live
* Do not confuse: "Loyalty configurations" (menu for reward fulfillment and event mapping) ≠ "Global settings" (sub-area for identity namespace selection)

**FAQ:**

* **Q: Which Experience Platform class do challenge audiences, personalization, and reporting use?** — Profiles in the XDM Individual Profile class.
* **Q: What schema field group holds standard loyalty attributes on the profile?** — The Loyalty Details field group, which defines the `loyalty` object and properties such as `points`, `tier`, `program`, and `status`.
* **Q: What must be configured before marketers can enter custom event values for Custom event tasks?** — Matching event mappings (event name, Experience event schema, and field mappings) in the Loyalty configurations menu.
* **Q: How can external loyalty or rewards data be used in Loyalty Challenges?** — Ingest it into Adobe Experience Platform using Sources connectors.
* **Q: How does dataset TTL affect Loyalty Challenges?** — Dataset time-to-live controls how long operational and reporting data is retained in the data lake and, when applicable, in the Profile store. Journey Optimizer applies TTL guardrails to many system-generated datasets, and loyalty-related datasets follow the same Platform retention model for your sandbox.

**Related pages:**

* For configuring loyalty challenges and event mappings: Learn how to configure loyalty challenges (loyalty-challenges/loyalty-admin.md)
* For connector onboarding and end-to-end setup: Get started with sources connectors (start/get-started-sources.md)
* For selecting audiences when configuring challenge eligibility: audiences (audience/about-audiences.md)
* For exploring loyalty performance dashboards: Explore Loyalty performance (loyalty-challenges/loyalty-performance.md)
* For dataset retention guardrails: Datasets Time-to-live (TTL) guardrails in Journey Optimizer (data/datasets-ttl.md)

**Personas:**

* **admin:** Can coordinate with the Adobe administrator to adjust organization-level archive and retention settings managed through the Loyalty metadata service. The page states that dataset time-to-live controls how long data is retained in the data lake and, when applicable, in the Profile store. Where: "Dataset time-to-live (TTL)".
* **developer:** Can use the Loyalty Details schema field group, which defines the loyalty object and properties such as points, tier, program, and status. Can configure event mappings (event name, Experience event schema, and field mappings) in the Loyalty configurations menu for Custom event tasks, before marketers enter custom event values in the task builder. The page states that event payloads must use the same identity namespace as the Loyalty Challenges configuration so progress can be attributed to the correct profile. Where: "Experience events".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Configure reward fulfillment and event mapping in the Loyalty configurations menu.
* **Success check:** Marketers can enter custom event values in the task builder.

+++

<!-- ai-section-version: 1 | source-hash: 56b9bb02 -->
