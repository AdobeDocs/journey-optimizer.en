---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to capture the response payload returned by a custom action's API call and leverage it to orchestrate journeys, personalize messages, and handle errors.

**Intents:**

* Configure a custom action to capture success and failure response payloads
* Leverage response payload fields in conditions, other actions, and message personalization
* Handle errors and timeouts using the jo_status_code field and the errorResponse node
* Inspect custom action responses through test mode logs
* Use the expression syntax to reference response fields, including default values and collections

**Glossary:**

* **Response payload**: The example payload pasted in the Response (success response) field whose fields are retrieved on each call *(product-specific)*
* **Error response payload**: The payload captured when a call fails, enabled by selecting Define a failure response payload, exposed under the errorResponse node *(product-specific)*
* **jo_status_code**: A built-in field, always available even when no response payload is defined, that carries the call outcome *(product-specific)*
* **actionsHistory**: A section shown in test mode logs that displays the payload returned by the external endpoint *(product-specific)*
* **currentActionField**: A reference used to access the current item when manipulating collections in a custom action response *(product-specific)*
* **Test mode**: The mode through which you access status logs related to custom action responses *(product-specific)*

**Guardrails:**

* Scalar arrays are supported in the response payload, but heterogeneous arrays are not supported.
* Only newly created custom actions include the jo_status_code field out-of-the-box; to use it with an existing custom action you need to update the action, for example by updating the description and saving.
* An action call is considered in error when the returned http code is greater than 2xx or if an error occurs, and the journey flows to the dedicated timeout or error branch.
* If an error response payload is configured, its fields are exposed under the errorResponse node for failed calls; if none is configured, that node is not available.
* Each profile entering the custom action triggers one call, even if the response is always the same.

**Terminology:**

* Canonical name: API call response in custom actions — Acronym: n/a — variants: custom action response, response payload
* Synonyms: "success response" = "Response field"
* Do not confuse: "Response" (success response payload) ≠ "Error Response" (failure response payload defined via Define a failure response payload)
* jo_status_code values: http_<code> (for example http_200 or http_400), timedout (timeout error), capped (capping error), internalError (internal error)

**FAQ:**

* **Q: Which array types are supported in the response payload?** — Scalar arrays are supported; heterogeneous arrays are not supported.
* **Q: Why does an existing custom action not expose the jo_status_code field?** — Only newly created custom actions include it out-of-the-box; update the existing action, for example by updating the description and saving, to add it.
* **Q: When is an action call considered in error?** — When the returned http code is greater than 2xx or an error occurs, after which the journey flows to the dedicated timeout or error branch.
* **Q: Where can the returned payload be inspected?** — Through test mode logs, in the actionsHistory section that displays the payload returned by the external endpoint.
* **Q: Can response payload fields be used in native channels?** — Yes, response payload fields from custom actions can be used in native channels (email, push, SMS) for message personalization.

+++

<!-- ai-section-version: 1 | source-hash: 7033cc37 -->
