---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure a custom action that connects a third-party REST API to your journeys by defining its endpoint, authentication, transport security, and payload parameters.

**Intents:**

* Create and name a custom action from the [!UICONTROL Configurations] > [!UICONTROL Actions] area
* Define the endpoint [!UICONTROL URL], [!UICONTROL Method], [!UICONTROL Headers], and [!UICONTROL Query parameters]
* Configure authentication, including default RS256 or optional HMAC JWT signing, and understand automatic mutual TLS activation
* Define request, response, and failure response payload parameters as constants or variables
* Understand the capping, throughput, and endpoint constraints that apply to custom actions

**Glossary:**

* **Custom action**: An additional action defined by technical users and made available to marketers to send messages or API calls to a third-party system *(product-specific)*
* **[!UICONTROL Endpoint Configuration]**: The section where you define the external service [!UICONTROL URL], [!UICONTROL Method], [!UICONTROL Headers], and [!UICONTROL Query parameters] *(product-specific)*
* **Constant parameter**: A parameter whose value is set in the action configuration by a technical persona and is always the same across journeys; the marketer cannot see it *(product-specific)*
* **Variable parameter**: A parameter whose value can vary and that marketers fill or map when using the custom action in a journey *(product-specific)*
* **[!UICONTROL Allow NULL values]**: An option that keeps Null values in the external call, with limitations for arrays of int, string, and similar values *(product-specific)*
* **Certificate-Based Custom Authentication**: An authentication type enabled by setting "subType": "certificateCredential" in the custom authorization payload, where Journey Optimizer signs a JWT client assertion and exchanges it for an access token; by default, RS256 signing uses Adobe's managed certificate and requires no client secret *(product-specific)*
* **HMAC signing**: JWT assertion signing selected through the optional `alg` field, using the OAuth `client_secret` in `body.bodyParams` without Adobe certificate registration *(product-specific)*
* **Slow custom action service**: A dedicated service through which calls are routed when an endpoint has a response time greater than 0.75 seconds *(product-specific)*

**Guardrails:**

* The action name allows only alphanumeric characters and underscores, with a maximum length of 30 characters (hard limit).
* Custom actions support JSON format only when using request or response payloads.
* Custom actions cannot use the DELETE method; only [!UICONTROL POST], [!UICONTROL GET], or [!UICONTROL PUT] are supported. To update an existing resource, use PUT.
* Only the default ports are allowed: 80 for http and 443 for https. Adobe addresses that are not public and IP addresses are not allowed.
* A capping limit of 300,000 calls over one minute (default) is defined for all custom actions and can be raised via the Capping or Throttling APIs; the default capping is performed per host and per sandbox and applies at the domain level.
* The 300,000 calls per minute cap is enforced as a sliding window per sandbox and per endpoint for endpoints with response times less than 0.75 seconds; for endpoints with response times greater than 0.75 seconds, a separate limit of 150,000 calls per 30 seconds (also a sliding window) applies.
* For a targeted endpoint, a throttling configuration cannot go below 200 TPS (hard limit), so the endpoint must support at least 200 TPS.
* When an endpoint has a response time greater than 0.75 seconds, its custom action calls are routed through a dedicated slow custom action service instead of the default service.
* Field names in the payload cannot contain a dot `.` character, nor start with a `$` character.
* When a custom action is used in a journey, most parameters are read-only; only the [!UICONTROL Name], [!UICONTROL Description], [!UICONTROL URL] fields and the [!UICONTROL Authentication] section can be modified.
* The [!UICONTROL Request] payload field is optional and only available for POST and PUT; the [!UICONTROL Response] payload field is optional and available for all calling methods.
* Even with [!UICONTROL Allow NULL values] enabled, an integer array `[1, null, 2, 3]` is sent as `[1, 2, 3]`; if such an array is null, it is sent as an empty array.
* Adobe periodically rotates the mTLS client certificate. Keep the endpoint's trust store updated, accept overlapping old and new certificates, and validate the certificate chain up to the Root CA (DigiCert) rather than pinning a specific leaf certificate fingerprint. Adobe does not currently send proactive rotation notifications; regularly check the Adobe Public Certificate API.
* You should not target public endpoints with custom actions.
* Omitting `alg` or setting it to `RS256` preserves the default RSA flow. HMAC signing accepts `HS256`, `HS384`, or `HS512`; other `alg` values are rejected.
* HMAC-signed JWT authentication is available in Limited Availability.
* HMAC signing requires an identity provider that accepts `client_secret_jwt` and an OAuth `client_secret` in `body.bodyParams`. Journey Optimizer uses the secret to sign the assertion but does not send it in the token request.

**Terminology:**

* Canonical name: Custom action - variants: custom actions
* Synonyms: [!UICONTROL URL Configuration] = [!UICONTROL Endpoint Configuration]
* Do not confuse: [!UICONTROL Constant] (value fixed in the action configuration, hidden from the marketer) ≠ [!UICONTROL Variable] (value that marketers pass or map in the journey)
* Do not confuse: "TLS" (TLS 1.3 is supported by default; negotiation may fall back to TLS 1.2 if the client does not support TLS 1.3) ≠ "mTLS" (mutual TLS, which also verifies the client certificate)

**FAQ:**

* **Q: What characters and length are allowed for an action name?** — The name allows only alphanumeric characters and underscores and cannot exceed 30 characters.
* **Q: Which methods are supported for a custom action?** — [!UICONTROL POST], [!UICONTROL GET], and [!UICONTROL PUT] are supported; DELETE is not supported, and PUT should be used to update an existing resource.
* **Q: What is the capping limit for custom actions?** — The default is 300,000 calls over one minute per host and per sandbox at the domain level, and it can be raised through the Capping or Throttling APIs. The sliding-window limits are 300,000 calls per minute per sandbox and per endpoint for response times less than 0.75 seconds, and 150,000 calls per 30 seconds for endpoints with response times greater than 0.75 seconds.
* **Q: How is mutual TLS activated?** — No additional configuration is required in the custom action or journey; mTLS occurs automatically when an mTLS-enabled endpoint is detected.
* **Q: Why is a custom action call routed to a different service?** — When an endpoint has a response time greater than 0.75 seconds, its calls are routed through a dedicated slow custom action service instead of the default service.
* **Q: How do I select HMAC signing for a custom action?** - Set the optional `alg` field to `HS256`, `HS384`, or `HS512` in the custom authorization payload and add your OAuth `client_secret` to `body.bodyParams`. This is a payload field, not a separate UI control; no Adobe certificate registration is required.

+++

<!-- ai-section-version: 1 | source-hash: 6a18f80f -->
