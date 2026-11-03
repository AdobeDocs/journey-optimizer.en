---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure an Action for an external endpoint and use the `externalDataLookup` helper in the personalization editor to dynamically fetch that data at runtime for personalizing inbound channel content.

**Intents:**

* Configure an Action defining an external endpoint (URL, HTTP method, parameters, request/response schemas)
* Insert the `externalDataLookup` helper in a personalization expression for an inbound action
* Pass variable header, query, payload, or path parameters to the external endpoint at call time
* Access fetched data via the result alias using personalization expressions and helper functions
* Handle timeouts and errors gracefully with fallback content patterns
* Debug external lookup issues using Adobe Experience Platform Assurance

**Glossary:**

* **externalDataLookup**: A helper function in the personalization editor that dynamically fetches data from a configured external endpoint at request time, for use in inbound channel content personalization. *(product-specific)*
* **Action**: A configuration object in Journey Optimizer (Administration > Configurations) that defines an external endpoint — URL, HTTP method, header/query parameters, POST body schema, and response schema. Required before using `externalDataLookup`. *(product-specific)*
* **result variable**: An arbitrary alias assigned in the `externalDataLookup` call; used to reference all fields from the fetched response in subsequent personalization expressions.
* **Inbound channels**: Channels where content is delivered on demand when a user opens a surface — Code-based Experience, Web, In-App Message. *(product-specific)*
* **AEP Edge Network**: The infrastructure that receives personalization requests and triggers the external data lookup call at runtime.

**Guardrails:**

* Feature is in Limited Availability — only available for a set of organizations.
* Default timeout for external endpoint calls: 300ms (default; contact your Adobe representative to increase this timeout for a specific endpoint).
* Response schema browsing is not supported in the personalization editor; Journey Optimizer does not validate references to JSON attributes from the response used in expressions.
* Supported data types for payload variable parameters: `String`, `Integer`, `Decimal`, `Boolean`, `listString`, `listInt`, `listInteger`, `listDecimal`.
* Variable substitution within `externalDataLookup` helper parameters is not currently supported.
* Dynamic URL paths are not currently supported.
* Authentication options in the Action configuration are not currently supported by `externalDataLookup`; use header fields for API key-based or plaintext authorization as a workaround.
* Changes to an Action configuration are not reflected in live campaigns or journeys using that Action; copy or modify any live campaigns/journeys to apply the changes.
* Multi-pass rendering is supported.
* Journey Optimizer does not currently cache external endpoint responses.
* The external endpoint must be able to handle at least as much concurrent load and throughput as the inbound traffic sent to the AEP Edge Network for the given surface.

**Terminology:**

* **Canonical name:** externalDataLookup — variants: external data lookup, external data lookup helper, External Data Lookup Helper
* **Synonyms:** "externalDataLookup" = "external data lookup helper"
* **Do not confuse:** `actionId` (ID of the configured Action, identifying the external endpoint) ≠ `result` (alias for the fetched response data) ≠ parameter names (variable values passed to the endpoint at call time)
* **Do not confuse:** using `externalDataLookup` in an inbound personalization action (fetches data dynamically at Edge Network request time) ≠ using a Custom Action in a journey activity (fetches content within a journey flow)

**FAQ:**

* **Q: What happens if the external endpoint times out or returns an error?** — The result variable will be empty. Attribute references within the result will display as blank, and array iterations will return no items. Use fallback content patterns — such as `?: "none found"` for single attributes or `{%#if result%}…{%else%}…{%/if%}` for entire content blocks — to handle these cases gracefully.
* **Q: How do I pass a contextual attribute from the request as a parameter to an external data lookup?** — Use the Contextual Attributes > Datastream > Event menu in the personalization editor to browse the Experience Event schema and insert the relevant attribute as a parameter value, for example: `query.myQueryParameter=context.datastream.event.<schemaId>.my.xdm.attribute`.
* **Q: Does Journey Optimizer cache external endpoint responses?** — Not currently. Caching will be supported in the future.
* **Q: How do I debug issues with externalDataLookup?** — Use Adobe Experience Platform Assurance. Start an Assurance session, initiate a Journey Optimizer call from your web or mobile implementation, and use the Edge Delivery view to inspect the customActions block for timeout or error details.
* **Q: Can I use authentication in the Action configuration with externalDataLookup?** — Authentication options in the Action configuration are not currently supported. For API key-based or other plaintext authorization, specify the credentials as header fields in the Action configuration.

+++

<!-- ai-section-version: 1 | source-hash: a3ce801a -->
