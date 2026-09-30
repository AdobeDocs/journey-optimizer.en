---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the Send test request capability to validate custom action configurations by making real API calls directly from Journey Optimizer, before or after using them in live journeys.

**Intents:**

* Send a real test API call to validate a custom action configuration
* Provide the correct payload depending on whether the method is GET or POST
* Enter authentication details required for each test request
* Understand the benefits of in-product testing compared to external tools
* Diagnose discard events and idle-timeouts when chaining journeys via custom actions

**Glossary:**

* **Send test request**: The capability administrators use to validate a custom action configuration by making real API calls directly from Adobe Journey Optimizer, checking request structure, headers, authentication, and payload *(product-specific)*
* **Discard event**: An event that is received but discarded, appearing in logs with codes such as notSuitableInitialEvent, when it does not meet the second journey's entry conditions *(product-specific)*
* **Idle timeout**: A timeout that may occur if the second journey is not ready, leading to discard events in the logs *(product-specific)*
* **IP (egress) proxy**: A proxy that, when enabled for your organization, is bypassed by the Send test request call *(product-specific)*

**Guardrails:**

* To use the Send test request capability, a custom action must be pre-configured with a URL, headers, and authentication settings.
* Users must have the Manage journeys events, data sources and actions permission, which is included in the Journey Administrators role; the View journeys events permission alone is not sufficient.
* If the custom action method is GET, no payload is required; if the method is POST, you must provide a JSON payload.
* Adobe Journey Optimizer raises an error if the structure of the JSON is incorrect, but not if there is a mismatch with a data type; for instance, no error is raised if an integer parameter is used for what should be a string.
* If your organization has the IP (egress) proxy enabled, the Send test request call bypasses it; to confirm proxy routing, run a test or live journey.
* For chained journeys, the second journey must be published or in test mode before the custom action is triggered, and within its active date window.

**Terminology:**

* Canonical name: Send test request — Acronym: n/a — variants: test request, in-product troubleshooting capability
* Synonyms: "AJO Journey" = "the executor of the test request, using the exact request structure and Adobe Journey Optimizer specific headers"
* Do not confuse: "Basic Authentication" (user provides the password) ≠ "API Key Authentication" (user enters the API key value) ≠ "Custom Authentication" (user supplies parameters in the request bodyParam)
* Do not confuse: "GET" method (no payload required) ≠ "POST" method (JSON payload required)

**FAQ:**

* **Q: What does the Send test request capability do?** — It validates a custom action configuration by making real API calls directly from Adobe Journey Optimizer, ensuring the request structure, headers, authentication, and payload are correctly formatted before being used in a journey.
* **Q: What permissions are required?** — Users must have the Manage journeys events, data sources and actions permission, included in the Journey Administrators role; the View journeys events permission alone is not sufficient.
* **Q: Do I need a payload for the test request?** — If the custom action method is GET, no payload is required; if the method is POST, you must provide a JSON payload.
* **Q: Does Journey Optimizer validate the payload data types?** — It raises an error if the JSON structure is incorrect, but not if there is a data type mismatch, so an integer used where a string is expected does not raise an error.
* **Q: Can I use this capability for live journeys?** — Yes, the Send test request capability can be used for troubleshooting live journeys, as the custom action is already deployed.
* **Q: Why is an event discarded when chaining journeys?** — The event can be received but discarded, appearing in logs with codes such as notSuitableInitialEvent, when it does not meet the second journey's qualification condition or the second journey is not ready.

+++

<!-- ai-section-version: 1 | source-hash: 4dcd4449 -->
