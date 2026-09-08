---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to limit journey throughput when external data sources or custom actions have a capped number of requests per second, using Read Audience rate configuration, percentage splits, and wait activities.

**Intents:**

* Limit the throughput of an audience-triggered journey to protect an external system from being overwhelmed
* Configure the reading rate of a Read Audience activity to control how many profiles enter per second
* Combine percentage split conditions and wait activities to spread profile processing over time
* Understand the difference between journey-level throughput workarounds and sandbox-level capping capabilities
* Apply capping capabilities to custom actions at the product level

**Glossary:**

* **Throttling / throughput limiting**: Controlling the rate at which profiles flow through a journey to avoid exceeding the request capacity of an external system. *(product-specific)*
* **Read Audience reading rate**: A configurable parameter on the Read Audience activity that sets the maximum number of profiles entering the journey per second (range: 500–20,000 instances/second). *(product-specific)*
* **Capping API**: A Journey Optimizer API that defines a maximum request limit per endpoint for external data sources; requests beyond the cap are dropped. *(product-specific)*
* **Percentage split condition**: A condition activity that divides the profile flow into branches by percentage, used here to distribute profiles across time-staggered wait paths. *(product-specific)*

**Guardrails:**

* Read Audience reading rate can be set between 500 and 20,000 instances per second; values below 500/s require a workaround using percentage splits and wait activities
* Unitary journeys support up to 5,000 instances/second; audience-triggered journeys support up to 20,000 instances/second
* The percentage-split + wait workaround operates only at journey level, not across all journeys in the sandbox
* When multiple journeys target the same external endpoint in parallel, this workaround does not account for the combined load — capping capabilities should be used instead
* Remaining requests that exceed the capping limit on external data sources are dropped, not queued
* The workaround must be thoroughly tested before going to production

**Terminology:**

* Canonical name: Throughput limiting — Acronym: none — variants: throttling, rate limiting, journey throughput control
* Synonyms: "Capping" = "throttling" in the context of external endpoint protection
* Do not confuse: "Capping API (endpoint-level)" ≠ "reading rate (journey-level)" — The Capping API applies globally to all journeys in a sandbox targeting an endpoint; the reading rate and split/wait workaround apply only to the individual journey

**FAQ:**

* **Q: What is the maximum reading rate I can set on a Read Audience activity?** — Between 500 and 20,000 profiles per second; to go below 500/s, use a percentage split with wait activities.
* **Q: How do percentage splits and wait activities help limit throughput?** — By splitting profiles into branches (e.g., 20% each) and adding staggered wait timers per branch, you ensure that only a controlled number of profiles reach the external system per second.
* **Q: Does the percentage-split workaround protect all journeys targeting the same endpoint?** — No; it only works at the individual journey level. If multiple journeys run in parallel against the same endpoint, use sandbox-level Capping capabilities instead.
* **Q: What happens to requests that exceed the capping limit on an external data source?** — They are dropped; the Capping API does not queue excess requests.
* **Q: Should I use custom actions or data sources for external data use cases?** — Custom actions are preferred because they support response handling; data sources should be used only when the use case specifically requires them.

+++
