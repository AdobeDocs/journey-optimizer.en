---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Configure OAuth 2.0 authentication for a custom channel by defining the token endpoint request, identifying credential fields, extracting the access token from the response, and specifying where to add it to delivery requests.

**Intents:**

* Configure OAuth 2.0 authentication when creating a custom channel or managing API credentials
* Choose a form or JSON body for the token endpoint request
* Identify credential fields in headers, query parameters, and request bodies
* Extract an access token from a top-level or nested response field
* Add the retrieved token to a delivery request header or query parameter
* Understand token caching and authentication configuration limits

**Glossary:**

* **Token endpoint**: The authorization server endpoint that Journey Optimizer calls to retrieve an access token
* **Authentication payload**: The configuration of the OAuth 2.0 token request, separate from the message payload sent to the delivery endpoint *(product-specific)*
* **Credential paths**: The paths identifying request fields that contain credentials, configured through `credentialPaths` *(product-specific)*
* **Token path**: The dot-separated path to the access token in the token endpoint response, configured through `tokenPath` *(product-specific)*
* **Token location configuration**: The delivery request header or query parameter to which the retrieved token is added, configured through `locationConfig` *(product-specific)*

**Guardrails:**

* Set the authentication configuration `type` to `oauth2` and use `post` for token requests.
* The token endpoint must be an absolute HTTPS URL with a non-empty host and a maximum length of 2048 characters.
* Token request bodies support `form` and `json` payloads; choose the format expected by your authorization server.
* Credential paths must start with `header`, `queryParam`, or `payload`, use dots as separators, and contain no empty path segments.
* Form credential paths use the form field key. JSON credential paths use the JSON object path. Do not include `content` or form array indexes in credential paths.
* Supported token locations are `header` and `queryParam`.
* The token endpoint timeout must be between 300 and 60000 milliseconds.
* When token caching is enabled, the cache duration must be between 300 and 3600 seconds. Journey Optimizer reuses the token for the configured duration instead of retrieving a token for every delivery request.
* Credential values must contain between 1 and 1024 characters.
* An empty `tokenPath` is allowed only when the entire response is the token.

**Terminology:**

* Canonical name: OAuth 2.0 authentication - variants: OAuth 2.0 authentication payload, OAuth token request configuration
* Do not confuse: "authentication payload" (configuration for retrieving an access token) with "message payload" (content sent to the custom channel delivery endpoint)
* Do not confuse: `credentialPaths` (credential fields in the token request) with `tokenPath` (access token field in the token response)
* Do not confuse: `request.headers` and `request.queryParams` (values sent to the token endpoint) with `locationConfig` (where the retrieved token is added to delivery requests)

**FAQ:**

* **Q: When should I use a form or JSON payload?** - Use `form` when the token endpoint expects form fields, and `json` when it expects a JSON request body.
* **Q: How do I identify a client secret in a form body?** - Use the form field key, for example, `payload.client_secret`, without `content` or an array index.
* **Q: How do I identify credentials in a nested JSON body?** - Use dot notation, for example, `payload.credentials.client_secret`.
* **Q: How do I extract a token from a nested response?** - Set `tokenPath` to the response field path, for example, `data.access_token`.
* **Q: Where can Journey Optimizer add the token to delivery requests?** - Set `locationConfig.location` to `header` or `queryParam` and `locationConfig.key` to the header or query parameter name.
* **Q: Does Journey Optimizer retrieve a token for every delivery request?** - When caching is enabled, it reuses the token for the configured cache duration.

+++