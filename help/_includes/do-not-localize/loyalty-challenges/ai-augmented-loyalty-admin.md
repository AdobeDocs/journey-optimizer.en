---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how administrators configure Loyalty Challenges through global settings, performance settings, reward providers, event mappings, product inventory, and exclusions before marketers author challenges.

**Intents:**

* Select the Experience Platform identity namespace used to identify loyalty members
* Select the loyalty profile and event datasets and the priority KPI for loyalty insights
* Create and edit a reward provider, including reward definitions, a reward proxy, and an auth token generator
* Create an event mapping so incoming experience events are interpreted for Custom event tasks
* Upload a product inventory CSV that groups catalog items for use in task eligibility rules
* Upload a CSV of organization-wide item and group exclusions for task configuration

**Glossary:**

* **Reward provider**: the external system that Journey Optimizer calls to fulfill rewards when customers make progress or complete challenges *(product-specific)*
* **Reward definition**: a reward type a provider can issue (for example, points or stars) and the payload Journey Optimizer sends when rewards are fulfilled *(product-specific)*
* **Reward proxy**: an optional intermediate server that fulfillment calls are routed through instead of sending them directly to the reward API endpoint *(product-specific)*
* **Auth token generator**: configuration used to obtain a fresh bearer token (or similar) before each call to the reward API *(product-specific)*
* **Event mapping**: configuration that tells Journey Optimizer how to identify and interpret an incoming Experience Platform experience event, such as a purchase or check-in *(product-specific)*
* **Product inventory**: a CSV-based mapping of item identifiers to product groups, used to target items in tasks without entering every item ID *(product-specific)*
* **Exclusions**: a CSV-based mapping of item identifiers to exclusion groups that are excluded program-wide from task eligibility *(product-specific)*
* **Key performance indicator (KPI)**: the organization's priority metric for the Loyalty Insights dashboard, determining which insights receive emphasis *(product-specific)*

**Guardrails:**

* Events that do not match any event mapping are ignored.
* Bring your own data challenges fulfill rewards through the organization's own data integration; reward providers configured in this section do not apply to those challenges.
* The profile dataset schema must include the Loyalty details and identityMap field groups, with identities supplied in identityMap; additional field groups can be included.
* The event dataset schema must include the Loyalty event details and Commerce details field groups; additional field groups can be included.

**Prerequisites and permissions:**

* Loyalty Challenges configuration requires administrator access to the Journey Optimizer instance, in addition to the permissions needed for Loyalty Challenges.

**Terminology:**

* Canonical name: event mapping — variants: event mappings
* Do not confuse: "product inventory" (item-to-group mappings used for task eligibility, uploaded via CSV) ≠ "exclusions" (item-to-group mappings used to exclude items program-wide, also uploaded via CSV)
* Do not confuse: "reward provider" (the external fulfillment system and its connection details) ≠ "reward definition" (one reward type and payload configuration belonging to a reward provider)

**FAQ:**

* **Q: What does global settings configure?** — The Experience Platform identity namespace used for Loyalty Challenges, matching how member profiles are identified in your data.
* **Q: What does performance settings configure?** — The loyalty profile dataset, loyalty event dataset, and the priority KPI for the Loyalty Insights dashboard.
* **Q: What field groups must the loyalty datasets include?** — The profile dataset schema must include Loyalty details and identityMap; the event dataset schema must include Loyalty event details and Commerce details.
* **Q: What happens to events that do not match any event mapping?** — They are ignored.
* **Q: Do reward providers apply to Bring your own data challenges?** — No, those challenges fulfill rewards through your own data integration, not through reward providers configured here.
* **Q: What is a reward proxy used for?** — To route fulfillment calls through an intermediate server instead of sending them directly to the reward API endpoint.

**Related pages:**

* For focused guidance on reward definition design and payload strategy: Reward Definition guide (loyalty-challenges/reward-definition-guide.md)
* For configuring challenge rewards after a reward provider is created: Learn how to configure challenge rewards (loyalty-challenges/create-challenges.md)
* For creating Bring your own data challenges: Learn how to create Bring your own data challenges (loyalty-challenges/create-challenges.md)
* For focused guidance on transformer authoring: Event Transformer guide (loyalty-challenges/event-transformer-guide.md)
* For writing custom JSONata mapping expressions: Learn how to write JSONata expressions (loyalty-challenges/event-transformer-guide.md)
* For creating Custom event tasks that reference event mappings: Learn how to create tasks (loyalty-challenges/create-tasks.md)
* For configuring eligible items using product inventory groups: Learn how to create tasks (loyalty-challenges/create-tasks.md)
* For defining eligible items and exclusions on tasks: Learn how to define eligible items and exclusions on tasks (loyalty-challenges/create-tasks.md)
* For background on loyalty data and datasets: Loyalty data and datasets (loyalty-challenges/loyalty-data-and-datasets.md)
* For more information about loyalty insights and performance monitoring: Explore loyalty performance (loyalty-challenges/loyalty-performance.md)

**Personas:**

* **admin:** Can select the identity namespace, loyalty profile and event datasets, and priority KPI in global and performance settings. Can create reward providers with reward definitions, proxies, and auth token generators, create event mappings, and upload product inventory and exclusions CSV files. The page states that Loyalty Challenges configuration requires administrator access to the Journey Optimizer instance, in addition to the permissions needed for Loyalty Challenges. Where: "Overview".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Select the Loyalty configurations menu from the left navigation to open the configuration interface.
* **Success check:** The interface is organized into tabs: Global settings, Performance settings, Reward providers, Event mapping, Product inventory, and Exclusions.
* **Previous:** For background on loyalty data and datasets before configuring performance settings: Loyalty data and datasets (loyalty-challenges/loyalty-data-and-datasets.md)
* **Next:** After creating a reward provider, configure challenge rewards: Create loyalty challenges (loyalty-challenges/create-challenges.md); After uploading product inventory, reference groups when creating tasks: Create tasks for loyalty challenges (loyalty-challenges/create-tasks.md)

+++

<!-- ai-section-version: 1 | source-hash: fe263432 -->
