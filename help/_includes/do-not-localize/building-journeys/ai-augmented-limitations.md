---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the hard technical limitations that apply to journey actions, journey versions, custom actions, events, reaction events, data sources, and audience reading in Adobe Journey Optimizer.

**Intents:**

* Understand the sending and retry limits for journey actions
* Learn which journey version transitions are allowed or blocked
* Identify restrictions on custom action URL, method, and header configuration
* Understand data source requirements for external system integration
* Avoid timing issues when starting a journey at the same moment as profile creation

**Glossary:**

* **Reaction event**: A journey activity that listens for a profile's interaction with a channel action (e.g., email open or click); must be placed immediately after the channel action activity. *(product-specific)*
* **Rule-based event**: An event type where the trigger is defined by a logical condition rather than a system-generated orchestration ID. *(product-specific)*
* **SLT (Service Level Target)**: The latency benchmark for API-based profile creation/update in Adobe Experience Platform — less than 1 minute from ingestion to Unified Profile at the 95th percentile for 20K RPS.

**Guardrails:**

* No sending throttling is applied; three retries are automatically performed on error and cannot be adjusted
* Two actions cannot run in parallel; they must be added sequentially
* A journey starting with an event activity in v1 cannot start with a non-event activity in later versions
* A journey starting with an Audience Qualification in v1 must always start with Audience Qualification in all subsequent versions; the audience and namespace cannot be changed
* A journey starting with Read Audience cannot start with a different event in next versions
* Custom action URL does not support dynamic parameters; only POST and PUT call methods are supported
* Custom action query parameter and header names must not start with "." or "$"; IP addresses and internal Adobe addresses (.adobe.) are not allowed
* Reaction activities must be placed immediately after a channel action activity; inserting a Wait or other activity between them is not supported
* External data sources must be accessible via REST API, support JSON, and handle the request volume
* Batch audiences are only evaluated once per day at the daily batch evaluation time — they are not recalculated at retrieval time
* When a journey is triggered simultaneously with a profile creation, profile data may not yet be available due to Platform ingestion latency

**Terminology:**

* Canonical name: Journey limitations — Acronym: none — variants: journey guardrails, journey restrictions
* Do not confuse: "Reaction event limitation" ≠ "general action limitation" — The Reaction event must be placed directly after a channel action; the general action limitation covers retries, parallelism, and throttling

**FAQ:**

* **Q: How many times does Journey Optimizer retry a failed action?** — Three retries are performed automatically; the number of retries cannot be configured.
* **Q: Can I place a Wait activity between a channel action and a Reaction event?** — No; the Reaction event must be placed immediately after the channel action activity. Adding any activity in between is not supported and may cause the Reaction event to not work as expected.
* **Q: Can I change the first event type when creating a new journey version?** — No; the entry mechanism set in v1 must be preserved in all subsequent versions. A journey starting with an event must continue to start with an event, and a journey starting with Audience Qualification must always start with Audience Qualification.
* **Q: Why might my journey not work when triggered at the same time as a profile is created?** — Profile creation via API has a latency before data is available in Unified Profile (SLT < 1 minute at 95th percentile). Adding a Wait activity after the first event gives Platform time to complete ingestion.
* **Q: Are streaming audiences always current in journeys?** — Yes; streaming audiences are always up-to-date. Batch audiences, however, are only evaluated once per day at the daily batch evaluation time, not at the moment of retrieval.

+++
