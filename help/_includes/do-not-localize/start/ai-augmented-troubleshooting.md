---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is a troubleshooting FAQ that provides answers and fixes for common Journey Optimizer issues across channels, data, audiences, rules, decisioning, and configuration.

**Intents:**

* Diagnose email, push, SMS, in-app, content card, and WhatsApp delivery and rendering issues
* Resolve data ingestion, dataset enablement, and TTL questions
* Investigate audience count discrepancies and Engageable Profiles increases
* Fix rule set, frequency capping, and quiet hours problems
* Resolve API errors such as 429 Too Many Requests and 403 access errors
* Know what to include when contacting Adobe support

**Glossary:**

* **Engageable Profiles**: A metric reflecting the number of unique profiles engaged by journeys or campaigns over the past 12 months *(product-specific)*
* **Suppression list**: The list to which addresses are automatically added after hard bounces, spam complaints, or manual additions; once suppressed, a profile does not receive messages from that channel *(product-specific)*
* **Quiet hours**: Time-based exclusion rules configured within a Channel rule set that define a blackout window during which messages are held until the next allowed window or discarded *(product-specific)*
* **Simulation**: The tool in Experience Decisioning used to test offer responses against a specific profile without sending live traffic *(product-specific)*
* **Test mode**: The mode used to verify journey event functionality; the multilingual validation error prevents journeys from being set to Test mode or Published *(product-specific)*
* **Adobe Experience Platform Assurance**: The tool used to inspect live SDK events and verify decision requests and tracking calls *(product-specific)*

**Guardrails:**

* When contacting Adobe support, include environment details, impact level, replication steps, logs or screenshots, and relevant IDs.
* If a recipient responds STOP to an SMS, all future messages from that short number are blocked, including transactional messages; use a separate short number for guaranteed transactional delivery.
* WhatsApp delivery requires the recipient to have explicitly opted in and the message to use a pre-approved template; free-form messages are only permitted within a 24-hour customer service window.
* Once an address is on the suppression list, the profile does not receive any messages from that channel regardless of campaign or journey targeting.
* A 429 response means your integration exceeded the API rate limit for the endpoint; wait for the duration specified in the Retry-After response header before retrying, using exponential backoff.
* Time-to-Live (TTL) settings do not affect existing sandboxes and are automatically applied only to newly provisioned ones.
* For a dataset to power profile-based personalization, the XDM schema must have Profile enabled and the dataset must be toggled on for Real-time Customer Profile.

**Terminology:**

* Canonical name: Troubleshooting FAQ — Acronym: n/a — variants: troubleshooting articles
* Synonyms: "Data Collection Core Service" = "DCCS"; "Domain-based Message Authentication, Reporting, and Conformance" = "DMARC"
* Do not confuse: "Simulation" (Experience Decisioning tool to test offer responses against a profile without sending live traffic) ≠ "Test mode" (used to verify journey event functionality and gate multilingual publishing)
* Do not confuse: "Exclusions" (counts all exclusion events, including duplicates for the same profile) ≠ "unique profile exclusions"

**FAQ:**

* **Q: Why are transactional SMS not delivered after a recipient replied STOP?** — Replying STOP blocks all future messages from that short number, including transactional ones; send transactional SMS through a separate short number that recipients have not opted out from.
* **Q: What does a 429 Too Many Requests error mean, and how do I resolve it?** — It means your integration exceeded the API rate limit; implement exponential backoff and wait for the duration in the Retry-After response header before retrying.
* **Q: Why is a dataset not being enabled for Real-time Customer Profile?** — The XDM schema must have Profile enabled and the dataset must be toggled on for Real-time Customer Profile, and the dataset must contain at least one identity field mapped to a recognized namespace.
* **Q: Why are my WhatsApp messages not being sent?** — Delivery requires the recipient to have explicitly opted in and the message to use a pre-approved template registered with the WhatsApp Business API; if either condition is not met, the message is silently blocked.
* **Q: Why has the Engageable Profiles count increased significantly?** — It can result from journeys or campaigns targeting large audiences that have not been engaged recently, or from changes in datasets enabled for Profile Service.
* **Q: What information should I include in a support ticket?** — Include environment details, impact level, replication steps, logs or screenshots, and relevant IDs.

+++

<!-- ai-section-version: 1 | source-hash: 95fbf8d4 -->
