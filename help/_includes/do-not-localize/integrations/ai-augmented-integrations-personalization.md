---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how marketers apply configured external integrations to personalize email, SMS, and push content, chain one API call's response into another, and use Adobe Target Delivery API responses in message templates.

**Intents:**

* Apply a configured integration to personalize Text or HTML content via Add personalization
* Control fallback behavior with the required field when an integration fails or returns no data
* Chain integrations so one call's response feeds the next call's inputs
* Map first-call output to second-call input using Pills mode or a Let helper
* Use Adobe Target Recommendations by fetching, extracting, and parsing the Target Delivery API response
* Render JSON or HTML mbox content with the externalDataLookup, valueAtPath, and parseJson helpers

**Glossary:**

* **required field**: An Integrations helper field that defines how failures or missing data interact with default content *(product-specific)*
* **Pills mode**: A mode that unlocks the advanced integration menu and lets you map first-call output directly to second-call input without a Let statement *(product-specific)*
* **externalDataLookup**: The helper that calls a configured integration and stores its full response in a named result variable *(product-specific)*
* **valueAtPath**: The helper that extracts an element from an array by its 0-based index and assigns it to a template variable *(product-specific)*
* **parseJson**: The helper that converts a raw JSON string field into a structured object for direct field access *(product-specific)*
* **Simulation**: The mode in which Journey Optimizer runs chained integrations in order, alongside send *(product-specific)*

**Guardrails:**

* You can add up to 3 integrations per Fragment and up to 5 on the message; integrations that come only from fragments do not count toward the 5.
* Journey Optimizer Fragments are available with Integrations but support outbound channels only.
* Once a fragment is published, adding and saving new integrations is disabled to avoid impact on existing journeys and campaigns.
* An administrator must have configured and activated each integration (endpoint, authentication, policies, response payload, and activation) before use.
* Tokens in a template must use only fields the administrator exposed in the integration configuration; unexposed fields are rejected in the editor.
* With required=true (default), rendering stops for that message, the send is excluded with ExternalDataLookupExclusion, and the exclusion is recorded in the message feedback dataset; with required=false, the result variable is set to null and rendering continues.
* For valueAtPath, if idx is out of bounds, rendering throws an exception; PQL expressions cannot be used as the path. Available since release 2025.9.0.
* For parseJson, if the JSON string is invalid or the reference is null, result is set to null and no rendering error is thrown. Available since 2026.6.0.

**Terminology:**

* Canonical name: External integrations for personalization — Acronym: n/a — variants: Integrations, integration personalization
* Synonyms: "required=true" = "default"
* Do not confuse: "required=true" (rendering stops, send excluded) ≠ "required=false" (result set to null, rendering continues)
* Do not confuse: JSON content (type is json; parse content with parseJson) ≠ HTML content (type is html; render content directly with triple braces)

**FAQ:**

* **Q: How many integrations can I add?** — Up to 3 per Fragment and up to 5 on the message; fragment-only integrations do not count toward the 5.
* **Q: What happens if an integration returns no data?** — With required=true the message rendering stops and the send is excluded (ExternalDataLookupExclusion, recorded in the message feedback dataset); with required=false the result is null and rendering continues, so use fallbacks or conditional logic.
* **Q: Can I feed one integration's response into another?** — Yes; chain integrations so calls run in order in the same message, mapping first-call output to second-call input in Pills mode or through a Let variable.
* **Q: How do I use an Adobe Target JSON mbox response?** — Fetch it with externalDataLookup, extract the mbox with valueAtPath, then parse options.content with parseJson before accessing nested fields.
* **Q: How do I render an Adobe Target HTML mbox response?** — Fetch and extract the mbox, then render content directly with triple braces; skip parseJson.

+++

<!-- ai-section-version: 1 | source-hash: 39ffe68f -->
