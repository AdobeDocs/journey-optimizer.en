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
* Choose an authentication mode among No authentication, Basic, Custom, and API key
* Define field groups per API parameter set with Method, Dynamic Values, and payload fields
* Configure custom authentication for protocols such as OAuth2 and check it with the check authentication button
* Configure certificate-based custom authentication for enterprise APIs such as Microsoft Entra ID and Okta
* Set the token cache duration to limit calls to the authentication endpoint

**Glossary:**

* **External data source**: A connection to a third-party system that you create; you can create as many as you need *(product-specific)*
* **Field group**: A set of fields configured per API parameter set, with Method, Dynamic Values, Response Payload, and (for POST) Sent Payload *(product-specific)*
* **Custom authentication mode**: An authentication mode for complex protocols such as OAuth2, where the action execution is a two-step process that first generates an access token and then injects it in the HTTP request *(product-specific)*
* **cacheDuration**: The parameter that specifies the retention duration of the generated token in the cache *(product-specific)*
* **Certificate-based custom authentication**: A custom authentication subtype (`subType: certificateCredential`) where Journey Optimizer uses Adobe's managed certificate to sign a JWT client assertion and exchange it for an access token, with no client secret required *(product-specific)*

**Guardrails:**

* REST APIs using POST or GET and returning JSON are supported; API Key, basic, and custom authentication modes are supported.
* Adobe addresses that are not publicly available and the use of IP addresses are not allowed; HTTPS is strongly recommended for security reasons.
* Data source name: only alphanumeric characters and underscores are allowed, maximum length 30 characters (hard limit).
* Field group name: only alphanumeric characters and underscores are allowed, maximum length 30 characters (hard limit).
* The Sent Payload field is only available if you select the POST method.
* The default cache duration is 1 hour (default) and can be adapted in the custom authentication payload; a one-minute buffer between the external API's token expiration and the `cacheDuration` setting is recommended to avoid 401 errors.
* The authentication token is cached per journey and is not shared between journeys; there is no persistence, so a service restart starts with a clean cache.
* Encode64 is the only function available in the authentication payload.
* For certificate-based custom authentication, `subType` and `aud` are mandatory; the token endpoint URL must be HTTPS, `method` must be `POST`, `client_id` must not be blank and must have no leading or trailing whitespace.
* `scope` is a single space-separated string in `bodyParams`, maximum 1000 characters total (hard limit).
* You never upload or enter a certificate; before using the custom action in a live journey you must register Adobe's leaf certificate (not the intermediate or root CA) in your Identity Provider.
* The Adobe certificate uses RS256 (RSA); Adobe rotates it 60 days before expiry (certificate lifetime 13 months) and the previous certificate remains valid until 30 days before expiry; customers are not currently notified, so periodically call the mTLS Public Certificate API to check the `expiryDate`.
* Nested JSON objects (for example, sub-objects within `bodyParams`) are supported.

**Terminology:**

* Canonical name: external data source — Acronym: n/a — variants: external data sources, third-party data source
* Synonyms: "check the authentication" = "Click to check the authentication" button
* Do not confuse: "Dynamic Values" (parameters defined in journeys and passed at call time) ≠ "Response Payload" (example payload returned by the call) ≠ "Sent Payload" (payload sent to the third-party system, POST only)
* Do not confuse: "standard custom authentication" ≠ "certificate-based custom authentication" (`subType: certificateCredential`, using Adobe's managed certificate instead of a client secret)

**FAQ:**

* **Q: What kinds of APIs are supported for external data sources?** — REST APIs using POST or GET and returning JSON, with API Key, basic, or custom authentication modes.
* **Q: What is the maximum length of a data source or field group name?** — 30 characters, using only alphanumeric characters and underscores.
* **Q: How do I verify that my custom authentication payload is configured correctly?** — Use the Click to check the authentication button; when the test is successful, the button turns green.
* **Q: What is the default token cache duration and can I change it?** — The default cache duration is 1 hour, and you can adapt it by specifying another retention duration in the `cacheDuration` parameter of the custom authentication payload.
* **Q: Do I need to upload a certificate for certificate-based custom authentication?** — No, Adobe manages the certificate and private key; you register Adobe's leaf certificate in your Identity Provider, retrieved from the mTLS Public Certificate API.
* **Q: Are nested JSON objects allowed in the custom authentication body?** — Yes, nested JSON objects such as sub-objects within `bodyParams` are supported.

+++

<!-- ai-section-version: 1 | source-hash: d67dbb8a -->
