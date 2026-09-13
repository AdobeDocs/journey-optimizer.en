---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how an administrator creates a custom channel in the Channel Builder by defining its general properties, endpoint, authentication, throttling policy, and message payload structure, then tests the connection and activates it.

**Intents:**

* Access and manage custom channels in the Channel Builder
* Define general properties such as name and icon for a custom channel
* Configure the endpoint URL, headers, query parameters, and policy settings
* Choose an authentication type and provide the authentication details
* Define the message payload structure and which fields marketers can author
* Test the connection and activate the channel

**Glossary:**

* **Channel Builder**: The central interface for defining new custom channels and for managing API credentials and subdomains *(product-specific)*
* **Endpoint configuration**: The HTTP URL of your external messaging system that Journey Optimizer calls with a POST request when a profile qualifies *(product-specific)*
* **Constant header value**: A static value set once and included in every request *(product-specific)*
* **Variable header value**: A value with an optional default that can be overridden in the channel configuration and resolved at runtime *(product-specific)*
* **Policy configuration**: The section defining how Journey Optimizer handles request throughput and failures through throttling, retry, and timeout settings *(product-specific)*
* **Test connection**: A button that sends a test request to your endpoint while the channel is in Draft status to validate the end-to-end connection *(product-specific)*

**Guardrails:**

* This capability requires the **View custom channels** and **Manage custom channels** permissions.
* The channel name must be unique, begin with a letter (A-Z), include only alphanumeric characters or the special characters _, ., -, and be greater than 1 character.
* An uploaded icon SVG file must be no larger than 150KB.
* The external endpoint must be HTTPS, accept the JSON payload the channel defines, support one of the Channel Builder authentication methods, and return an HTTP 2xx response.
* Throttling is disabled by default; the maximum number of requests per second default is 5,000, and once the limit is reached requests are queued and sent as soon as possible.
* Retry is enabled by default with a maximum retry count default of 3 (configurable range 0-10).
* The endpoint timeout default is 5,000 milliseconds.
* Modifying throttling or retry settings on an active channel takes effect immediately for all in-flight and future executions.
* When the authentication type is anything other than None, an initial set of API credentials is generated automatically when the channel is activated.
* After a channel is activated, only name, description, icon, throttling, and retry configuration remain editable; endpoint URL, headers, query parameters, authentication, and payload structure are locked.
* A required payload field that has no value triggers a validation error that prevents activation.

**Terminology:**

* Canonical name: custom channel — Acronym: n/a — variants: custom channel definition
* Synonyms: "set up a custom channel" = "create a custom channel" (both are used on this page for the same task)
* Do not confuse: "Constant" (static value included in every request) ≠ "Variable" (default value that can be overridden in the channel configuration)
* Do not confuse: "Enable throttling" (requests per second cap) ≠ "Enable retry" (retry count for failed requests)
* Do not confuse: "Draft" ≠ "Active" ≠ "Archived" channel statuses

**FAQ:**

* **Q: What permissions are required to create a custom channel?** — The View custom channels and Manage custom channels permissions.
* **Q: What statuses can a custom channel have?** — Draft, Active, or Archived.
* **Q: Which fields remain editable after activation?** — Only name, description, icon, throttling, and retry configuration; endpoint URL, headers, query parameters, authentication, and payload structure are locked.
* **Q: How do I validate the connection before activating?** — Use the Test connection button while the channel is in Draft status to send a test request to your endpoint, then check your external system's logs.
* **Q: What payload format is supported?** — JSON; you can paste a sample JSON payload so that a schema is inferred (importing a JSON schema is coming soon).
* **Q: What happens when I archive an active channel?** — It is removed from all selection drop-downs, while existing journeys and campaigns that already use it continue to function normally.

+++

<!-- ai-section-version: 1 | source-hash: 99f27e9a -->
