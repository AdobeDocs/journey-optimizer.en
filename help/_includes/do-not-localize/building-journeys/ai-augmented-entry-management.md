---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how profile entry management works across the four journey types in Adobe Journey Optimizer, including throughput limits, reentrance settings, and the behavior of Wait and action activities on processing rate.

**Intents:**

* Understand the entry behavior and throughput limits for each journey type (Unitary event, Business event, Read audience, Audience qualification)
* Enable or disable profile reentrance and configure the reentrance wait period
* Allow multiple business event executions for a Business journey
* Identify how Wait activities and action activities affect journey processing rate
* Ensure a profile is not present in the same journey at the same time

**Glossary:**

* **Reentrance**: The ability for a profile to enter the same journey again after previously exiting it; configurable with a wait period *(product-specific)*
* **Reentrance wait period**: The minimum time that must pass before a profile can re-enter a journey; default is 5 minutes, maximum is 90 days in journey properties *(product-specific)*
* **TPS (Transactions Per Second)**: The throughput rate at which profiles can enter or be processed in a journey *(product-specific)*
* **Unitary event journey**: A journey triggered by a single event associated with one profile *(product-specific)*
* **Read audience journey**: A journey that processes a batch of profiles belonging to a defined audience, either once or on a recurring schedule *(product-specific)*
* **Business event journey**: A journey triggered by a business event that targets an audience, creating one journey instance per profile *(product-specific)*
* **Audience qualification journey**: A journey triggered when a profile enters or exits a streaming audience in real-time *(product-specific)*

**Guardrails:**

* A profile cannot be present multiple times in the same journey at the same time across all active versions.
* Read audience journeys: maximum 20,000 TPS (sandbox-level quota; shared across all concurrent Read Audience journeys in the same sandbox)
* Audience qualification and Unitary event journeys: maximum 5,000 TPS (org-level quota; shared with each other across all sandboxes in the org)
* Business events count toward the 5,000 TPS org-level quota; the subsequent Read audience activity shares the 20,000 TPS sandbox-level quota
* Default reentrance wait period is 5 minutes; maximum configurable value is 90 days in journey properties
* Fixed-time Wait activities can cause profile surges exceeding 20,000 TPS and are not recommended.
* Custom action default capping is 300,000 calls per minute.
* For Business journeys, audience data from the first execution is reused for 1 hour.

**Terminology:**

* Canonical name: Profile entrance management — Acronym: n/a — variants: profile entry management, journey entry
* Synonyms: "reentrance" = "re-entry"
* Do not confuse: "Unitary event journey" ≠ "Audience qualification journey" — both are unitary scenarios but triggered differently (event emission vs. audience membership change)

**FAQ:**

* **Q: Can a profile enter the same journey twice simultaneously?** — No, the system uses the profile identity as a key and prevents the same profile from being at different places in the same journey at the same time.
* **Q: What is the default reentrance wait period?** — 5 minutes, configurable up to a maximum of 90 days in journey properties.
* **Q: How many profiles per second can a Read audience journey process?** — Up to 20,000 TPS at sandbox level, though this maximum may not be achievable if multiple journeys run simultaneously in the same sandbox.
* **Q: What happens to throughput after a Wait activity with a fixed time?** — Multiple profiles may exit the wait simultaneously, potentially exceeding 20,000 TPS; relative-time Wait activities are recommended to avoid this.
* **Q: Can a profile appear in a Business journey multiple times at the same time?** — Yes, but only in the context of different business events.

+++
