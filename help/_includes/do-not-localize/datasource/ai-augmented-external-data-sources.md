---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create and configure external data sources that connect to third-party REST APIs, including the supported authentication modes, field group setup, custom authentication payloads, and certificate-based custom authentication.

**Intents:**

* Create and configure an external data source that connects to a third-party REST API
* Choose an authentication mode among [!UICONTROL No authentication], [!UICONTROL Basic], [!UICONTROL Custom], and [!UICONTROL API key]
* Define field groups per API parameter set with [!UICONTROL Method], [!UICONTROL Dynamic Values], and payload fields
* Configure custom authentication for protocols such as OAuth2 and check it with the [!UICONTROL Click to check the authentication] button
* Configure JWT client assertion authentication using default RS256 certificate signing or optional HMAC signing
* Set the token cache duration to limit calls to the authentication endpoint

**Glossary:**

* **External data source**: A connection to a third-party system that you create; you can create as many as you need *(product-specific)*
* **Field group**: A set of fields configured per API parameter set, with [!UICONTROL Method], [!UICONTROL Dynamic Values], [!UICONTROL Response Payload], and (for POST) [!UICONTROL Sent Payload] *(product-specific)*
* **Custom authentication mode**: An authentication mode for complex protocols such as OAuth2, where the action execution is a two-step process that first generates an access token and then injects it in the HTTP request *(product-specific)*
* **cacheDuration**: The parameter that specifies the retention duration of the generated token in the cache *(product-specific)*
* **Certificate-based custom authentication**: A custom authentication subtype (`subType: certificateCredential`) where Journey Optimizer signs a JWT client assertion and exchanges it for an access token; the default RS256 option uses Adobe's managed certificate and requires no client secret *(product-specific)*
* **HMAC-signed JWT client assertion**: An assertion signed using the OAuth `client_secret` as the signing key, selected through the optional `alg` field, without Adobe certificate registration *(product-specific)*

**Guardrails:**

* Use custom actions instead of data sources for external data source use cases now that responses are supported (recommended). Custom Actions without Data Lake persistence are the right choice when the data is only useful inside the journey and the external system is accessible via an API endpoint.
* REST APIs using POST or GET and returning JSON are supported; API Key, basic, and custom authentication modes are supported.
* The use of Adobe addresses that are not publicly available and the use of IP addresses is not allowed; HTTPS is strongly recommended for security reasons.
* Data source name: only alphanumeric characters and underscores are allowed, maximum length 30 characters (hard limit).
* Field group name: only alphanumeric characters and underscores are allowed, maximum length 30 characters (hard limit).
* The [!UICONTROL Sent Payload] field is only available if you select the POST method.
* The default cache duration is 1 hour (default) and can be adapted in the custom authentication payload; at least a one-minute buffer between the external API's token expiration period and the `cacheDuration` setting is recommended, especially under heavy workloads, to avoid expiration mismatches and 401 errors.
* The authentication token is cached per journey and is not shared between journeys; there is no persistence, so a service restart starts with a clean cache.
* Encode64 is the only function available in the authentication payload.
* For certificate-based custom authentication, `subType` and `aud` are mandatory; the token endpoint URL must be HTTPS, `method` must be `POST`, `client_id` must not be blank and must have no leading or trailing whitespace.
* For certificate-based custom authentication, `scope` is a single space-separated string in `bodyParams`, maximum 1000 characters total (hard limit).
* For RS256 only, you never upload or enter a certificate; before using the custom action in a live journey you must register Adobe's leaf certificate (not the intermediate or root CA) in your Identity Provider.
* The Adobe certificate applies to the default RS256 (RSA) option; Adobe rotates it 60 days before expiry (certificate lifetime 13 months) and the previous certificate remains valid until 30 days before expiry; customers are not currently notified, so periodically call the mTLS Public Certificate API to check the `expiryDate`.
* The optional `alg` field accepts `RS256` (default), `HS256`, `HS384`, and `HS512`. Omitting `alg` or setting it to `RS256` preserves the existing RSA flow; other values are rejected.
* HMAC-signed JWT authentication is available in Limited Availability.
* HMAC signing requires `client_id` and `client_secret` in `body.bodyParams`, `subType: certificateCredential`, explicit `aud`, `method: POST`, and `bodyType: form`. Minimum secret lengths in UTF-8 bytes are 32 for HS256, 48 for HS384, and 64 for HS512. The identity provider client must accept `client_secret_jwt` with the same secret and algorithm.
* For HMAC, Journey Optimizer does not send `client_secret` in the token request; it sends the other authored `bodyParams` plus `client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer` and `client_assertion`.
* The HMAC JWT header includes `typ` and the selected `alg`, with no `x5t`; `aud` is a single-element array and `exp` is `iat` + 300 seconds. RS256 uses `iat` + 600 seconds.
* When configuring custom authentication for a custom action, nested JSON objects (for example, sub-objects within `bodyParams`) are supported.

**Terminology:**

* Canonical name: external data source - variants: external data sources
* Do not confuse: [!UICONTROL Dynamic Values] (parameters defined in journeys and passed at call time) ≠ [!UICONTROL Response Payload] (example payload returned by the call) ≠ [!UICONTROL Sent Payload] (payload sent to the third-party system, POST only)
* Do not confuse: "RS256" (default JWT signing with Adobe's managed certificate) and "HS256", "HS384", or "HS512" (HMAC JWT signing with the OAuth client secret)

**FAQ:**

* **Q: What kinds of APIs are supported for external data sources?** — REST APIs using POST or GET and returning JSON, with API Key, basic, or custom authentication modes.
* **Q: What is the maximum length of a data source or field group name?** — 30 characters, using only alphanumeric characters and underscores.
* **Q: How do I verify that my custom authentication payload is configured correctly?** — Use the [!UICONTROL Click to check the authentication] button; when the test is successful, the button turns green.
* **Q: What is the default token cache duration and can I change it?** — The default cache duration is 1 hour, and you can adapt it by specifying another retention duration in the `cacheDuration` parameter of the custom authentication payload.
* **Q: Do I need to upload a certificate for certificate-based custom authentication?** - For the default RS256 option, Adobe manages the certificate and private key; you register Adobe's leaf certificate in your Identity Provider, retrieved from the mTLS Public Certificate API. HMAC signing requires no Adobe certificate registration.
* **Q: Are nested JSON objects allowed when configuring custom authentication for a custom action?** — Yes, nested JSON objects such as sub-objects within `bodyParams` are supported.

+++

<!-- ai-section-version: 1 | source-hash: 6eabf054 -->
