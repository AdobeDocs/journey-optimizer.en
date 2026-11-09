---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure Event Mapping schema validation and JSONata transformer expressions so that incoming customer events are matched and reshaped into the Adobe Loyalty Event format for Loyalty Challenges.

**Intents:**

* Understand how an Event Mapping identifies and claims incoming events through XDM schema ID matching.
* Write a JSONata transformer expression that reshapes a source event into the Adobe Loyalty Event format.
* Add JSON Schema validation to an event mapping to reject malformed events before transformation.
* Avoid common transformer mistakes such as collapsing multiple line items into one object or losing array indices on identity fields.
* Use the API operations to create, list, update, and delete event mappings.
* Understand the native Loyalty Event fallback for events that do not match any mapping.

**Glossary:**

* **Event Mapping**: a configuration that tells the platform which events to claim (matching) and how to reshape them (transformation) *(product-specific)*
* **Adobe Loyalty Event**: the JSON object format that the Challenge Service processes *(product-specific)*
* **Transformer**: a JSONata expression that receives the incoming event JSON and returns a valid Adobe Loyalty Event object *(product-specific)*
* **`item_set`**: an array of string identifiers on a line item that challenge tasks' include/exclude lists match against *(product-specific)*
* **`xdmSchemaId`**: the field on an event mapping that is compared against the schema ID read from an incoming event's envelope to determine a match *(product-specific)*
* **Data Collection Core Service (DCCS)**: the service through which events carrying an XDM schema reference in their envelope arrive *(product-specific)*
* **Native Loyalty Event**: an event that is ingested directly, without a transformer, when it already conforms to the Adobe Loyalty Event format *(product-specific)*

**Guardrails:**

* `loyalty_identity` is required and must contain `id`, the member's loyalty ID.
* `item_list` is required and must have at least one item; an empty item_list is rejected.
* `item_set` is required per item.
* `timestamp` is required and must be ISO 8601.
* `utc_offset` is recommended; it is needed for daypart matching and streak-day counting, and without it daypart window matching and consecutive-day streak counting are both skipped.
* `_id` is optional, used for dedup if the org has duplicate detection enabled.
* `sub_total` is optional; omitting it means zero spend for spend-threshold tasks.
* In the Event Mapping configuration, `name`, `xdmSchemaId`, `schema`, and `transformer` are required fields; `guid` is system-assigned and read-only.
* The platform walks the org's event mappings in order and applies the first one that matches; events that do not match any mapping fall through to native ingestion.
* `event_name` is used only for internal metrics and reporting; it is not used as a task filter — task qualification is determined by `item_set` contents, not the event name.
* Events that fail schema validation are rejected before transformation runs.
* If the transformer's JSONata expression is invalid, the API returns a `422` error with a description of the parse failure.
* Once a match is found by `xdmSchemaId`, the `xdmEntity` body — not the outer envelope — is passed to the transformer; for DCCS events specifically, paths referencing the outer envelope (e.g. `/body/xdmMeta/...`) will not be found and will silently produce null.
* `identityMap` is an array per namespace; omitting `[0]` causes JSONata to return a sequence instead of a single value when more than one identity is present, turning `loyalty_identity.id` into a list.
* Custom tenant identity-like fields (e.g. `_yourtenant.identification.core.email`) are frequently empty in production events even though they return a value in sample data; `identityMap` is the reliable source of identity.
* Using a single object literal with a path like `productListItems.SKU` instead of mapping over the array (`productListItems.{ ... }`) collapses multiple line items into one, with `quantity` becoming an array instead of a per-item value.
* If a nested array field (e.g. `productCategories`) is added to `item_set` without indexing it, the result can expand to more entries than expected.
* `timestamp` must be ISO 8601; a Unix epoch integer must be converted (e.g. with `$fromMillis`).
* Dividing `unit_price` by quantity is only correct if the source field is a line total; dividing an already-per-unit price by quantity silently produces a wrong value.

**Terminology:**

* Canonical name: Event Mapping — no documented named variant; the page refers back to an event mapping informally as "this definition" in context, not as a defined synonym.
* Canonical name: Adobe Loyalty Event — variants: Loyalty Event format
* Acronym: XDM — Experience Data Model (expansion per the acronyms list; not spelled out on this page, which uses only "XDM")
* Acronym: DCCS — expansion not given on the page ("Data Collection Core Service" is the page's own spelled-out form on first use, not an approved-list acronym)
* Do not confuse: "the outer AJO envelope" (never passed to the transformer) ≠ "the `xdmEntity` body" (what the transformer always receives once a match is found, per How Matching Works and the DCCS pitfall)
* Do not confuse: "Event Mapping" (the matching-and-transformation configuration) ≠ "transformer" (the JSONata expression field within an event mapping)

**FAQ:**

* **Q: How does the platform decide which event mapping applies to an incoming event?** — It reads the XDM schema ID from the event's envelope, walks the org's event mappings in order, and applies the first one whose `xdmSchemaId` matches.
* **Q: What happens to an event that does not match any event mapping?** — It falls through to native ingestion as a native Adobe Loyalty Event; if it already conforms to the Loyalty Event format, no transformer is needed.
* **Q: What part of the event does the transformer receive once a match is found?** — The `xdmEntity` body, not the outer envelope.
* **Q: What causes `loyalty_identity.id` to become a list instead of a single string?** — Omitting the `[0]` index on an `identityMap` namespace array when more than one identity is present.
* **Q: Why would `item_set` contain more entries than expected?** — Because a nested array field (such as `productCategories`) was added to `item_set` without indexing it.
* **Q: What happens if `item_list` is empty or missing?** — The event is rejected as invalid.
* **Q: What happens if the transformer expression has invalid JSONata syntax?** — The API returns a `422` error with a description of the parse failure when the event mapping is saved.

**Personas:**

* **admin:** Can create, list, update, and delete event mappings through the API operations at the base path /loyalty/metadata/config/events. Each event mapping requires the name, xdmSchemaId, schema, and transformer fields; guid is system-assigned and read-only. The page states that the platform walks the org's event mappings in order and applies the first one that matches, and that events failing schema validation are rejected before transformation runs. Where: "API Reference".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Create an event mapping by sending a POST request to /loyalty/metadata/config/events with the name, xdmSchemaId, and transformer fields.
* **Success check:** Using the JSONata Exerciser, the transformer expression's output for the source event matches the expected Adobe Loyalty Event format.

+++

<!-- ai-section-version: 1 | source-hash: 78ff3376 -->
