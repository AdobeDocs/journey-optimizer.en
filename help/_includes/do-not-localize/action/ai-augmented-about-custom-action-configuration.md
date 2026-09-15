---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure a custom action that connects a third-party REST API to your journeys by defining its endpoint, authentication, transport security, and payload parameters.

**Intents:**

* Create and name a custom action from the Configurations Actions area
* Define the endpoint URL, method, headers, and query parameters
* Configure authentication, including certificate-based custom authentication and mutual TLS
* Define request, response, and failure response payload parameters as constants or variables
* Understand the capping, throughput, and endpoint constraints that apply to custom actions

**Glossary:**

* **Custom action**: An additional action defined by technical users and made available to marketers that calls a third-party service through a REST API with a JSON-formatted payload *(product-specific)*
* **Endpoint Configuration**: The section where you define the external service URL, method, headers, and query parameters *(product-specific)*
* **Constant parameter**: A parameter whose value is set in the action configuration by a technical persona and is always the same across journeys; the marketer cannot see it *(product-specific)*
* **Variable parameter**: A parameter whose value can vary and that marketers fill or map when using the custom action in a journey *(product-specific)*
* **Allow NULL values**: An option that keeps Null values in the external call *(product-specific)*
* **Certificate-Based Custom Authentication**: An authentication type enabled by setting "subType": "certificateCredential" in the custom authorization payload, where Journey Optimizer signs a JWT client assertion with Adobe's managed certificate and exchanges it for an access token *(product-specific)*
* **Slow custom action service**: A dedicated service through which calls are routed when an endpoint has a response time greater than 0.75 seconds *(product-specific)*

**Guardrails:**

* The action name allows only alphanumeric characters and underscores, with a maximum length of 30 characters (hard limit).
* Custom actions support JSON format only when using request or response payloads.
* Custom actions cannot use the DELETE method; only POST, GET, or PUT are supported. To update an existing resource, use PUT.
* Only the default ports are allowed: 80 for http and 443 for https. Adobe addresses that are not public and IP addresses are not allowed.
* A capping limit of 300,000 calls over one minute is defined for all custom actions (a default that can be raised via the Capping or Throttling APIs); the default capping is performed per host and per sandbox and applies at the domain level.
* The 300,000 calls per minute cap is enforced as a sliding window per sandbox and per endpoint for endpoints with response times less than 0.75 seconds; for endpoints with response times greater than 0.75 seconds, a separate limit of 150,000 calls per 30 seconds (also a sliding window) applies.
* A throttling configuration cannot go below 200 TPS, so any targeted endpoint must support at least 200 TPS.
* When an endpoint has a response time greater than 0.75 seconds, its custom action calls are routed through a dedicated slow custom action service instead of the default service.
* Field names in the payload cannot contain a dot character, nor start with a dollar character.
* When a custom action is used in a journey, most parameters are read-only; only the Name, Description, URL fields and the Authentication section can be modified.
* You should not target public endpoints with custom actions.

**Terminology:**

* Canonical name: Custom action — Acronym: n/a — variants: custom actions, action configuration
* Synonyms: "URL Configuration" = "Endpoint Configuration"
* Do not confuse: "Constant" (value fixed in the action configuration, hidden from the marketer) ≠ "Variable" (value that marketers pass or map in the journey)
* Do not confuse: "TLS" (transport layer security, with fallback from TLS 1.3 to TLS 1.2) ≠ "mTLS" (mutual TLS, which also verifies the client certificate)

**FAQ:**

* **Q: Why can the action name not be saved?** — The name allows only alphanumeric characters and underscores and cannot exceed 30 characters.
* **Q: Which methods are supported for a custom action?** — POST, GET, and PUT are supported; DELETE is not supported, and PUT should be used to update an existing resource.
* **Q: What is the capping limit for custom actions?** — 300,000 calls over one minute per host and per sandbox at the domain level; endpoints slower than 0.75 seconds instead use a limit of 150,000 calls per 30 seconds.
* **Q: How is mutual TLS activated?** — No additional configuration is required in the custom action or journey; mTLS occurs automatically when an mTLS-enabled endpoint is detected.
* **Q: Why is a custom action call routed to a different service?** — When an endpoint has a response time greater than 0.75 seconds, its calls are routed through a dedicated slow custom action service instead of the default service.

+++

<!-- ai-section-version: 1 | source-hash: 6a18f80f -->
