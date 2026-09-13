---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is the Developer getting-started path, covering how to implement the Mobile and Web SDKs, event streaming, custom action endpoints, and Journey Optimizer REST APIs, then test and debug those integrations.

**Intents:**

* Set up Adobe Experience Platform Mobile SDK and Web SDK integrations
* Implement code-based experiences for mobile and web surfaces
* Send events to trigger journeys using the Streaming Ingestion APIs
* Develop custom action endpoints that Journey Optimizer calls during journey execution
* Work with Journey Optimizer REST APIs, including API-triggered campaigns and capping and throttling
* Test and debug implementations using test mode with test profiles and Adobe Experience Platform Assurance

**Glossary:**

* **Mobile SDK**: A collection of libraries embedded in an iOS or Android app that identifies users, collects behavioral events, and delivers instructions from Journey Optimizer *(product-specific)*
* **Web SDK (`alloy.js`)**: A single JavaScript library that collects behavioral data, streams it to Adobe Experience Platform through a datastream, and receives personalization instructions back *(product-specific)*
* **Custom action**: A journey step where Journey Optimizer makes an outbound HTTP call to a URL you provide, such as a backend, CRM, or loyalty platform *(product-specific)*
* **Code-based experiences**: Personalized content delivered to any mobile or web surface, where Journey Optimizer returns a JSON payload and your code decides where and how to display it *(product-specific)*
* **Unitary events**: Person-specific action events (for example a button click or purchase completion), as distinct from business events such as inventory updates or price changes *(product-specific)*

**Guardrails:**

* Journey Optimizer applies a 5000 calls/second limit for custom action endpoints, but your system should be resilient.
* API-triggered campaign calls have a timeout of 60 seconds; internal retries handle unexpected timeouts.
* An API-triggered campaign must be activated before the endpoint accepts calls, and calls made outside configured campaign start and end dates will fail.
* Throttling queues calls for up to 6 hours (production sandboxes, custom actions only), while capping rejects calls that exceed the configured limit.
* High Throughput mode for API-triggered campaigns supports up to 5000 TPS and requires an add-on license.
* All integrations must use OAuth Server-to-Server authentication; the JWT method is deprecated.
* The Simulations API is available for API-triggered and Action (scheduled) campaigns and is not supported for Orchestrated campaigns.

**Terminology:**

* Canonical name: Developer — variants: Developer getting-started path
* Acronyms: SDK = Software Development Kit; XDM = Adobe Experience Data Model; TPS = transactions per second; API = Application Programming Interface
* Implementation order: Administrator → Data Engineer → Developer → Marketer
* Do not confuse: "Mobile SDK" (embedded iOS or Android libraries) ≠ "Web SDK" (`alloy.js` JavaScript library)
* Do not confuse: "Capping" (rejects calls that exceed the configured limit) ≠ "Throttling" (queues calls for up to 6 hours)

**FAQ:**

* **Q: What is the rate limit for custom action endpoints?** — Journey Optimizer applies a 5000 calls/second limit, but your endpoints should still be resilient.
* **Q: Which authentication method must API integrations use?** — OAuth Server-to-Server authentication; the JWT method is deprecated.
* **Q: What must be true before an API-triggered campaign endpoint accepts calls?** — The campaign must be activated, and calls outside any configured start and end dates will fail.
* **Q: What is the difference between capping and throttling?** — Capping rejects calls that exceed the configured limit, while throttling queues them for up to 6 hours (production sandboxes, custom actions only).
* **Q: Is the Simulations API supported for Orchestrated campaigns?** — No; it is available for API-triggered and Action (scheduled) campaigns, and you use the preview and proof workflow in the Orchestrated campaigns user interface instead.
* **Q: How do I test my implementation before it goes live?** — Use test mode with test profiles obtained from your Data Engineer, and use Adobe Experience Platform Assurance to inspect SDK events and troubleshoot.

+++

<!-- ai-section-version: 1 | source-hash: 31eccb8f -->
