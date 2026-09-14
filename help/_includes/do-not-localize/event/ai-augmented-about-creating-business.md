---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure a business event, which is not linked to a specific profile and is always rule-based, so a journey can be triggered for a set of profiles when a global occurrence happens, such as a product coming back in stock.

**Intents:**

* Create a business event and define its name, description, schema, and payload fields
* Choose a time series schema and select the required `_id` and `timestamp` fields
* Define the Event ID condition that identifies the events that trigger the journey
* Preview the payload to validate the payload definition and share it with the person responsible for sending events
* Understand how business events behave with reentrance, multiple executions, and testing

**Glossary:**

* **Business event**: An event that is not linked to a specific profile and is always rule-based, used to trigger a journey for a set of profiles when a global occurrence happens *(product-specific)*
* **Read audience activity**: The activity that is the only one allowed after a business event and is automatically added as the next step *(product-specific)*
* **Event ID condition**: The condition, written in the simple expression editor, used by the system to identify the events that trigger the journey *(product-specific)*
* **One-shot business event**: A business event whose first event job data is reused during a one-hour time window for a given journey *(product-specific)*

**Guardrails:**

* Only time series schemas are available; Experience Events, Decision Events, and Journey Step Events schemas are not available.
* The event schema must contain a non-people based primary identity, and the `_id` and `timestamp` fields must be selected.
* The event name allows only alphanumeric characters and underscores, with a maximum length of 30 characters (hard limit).
* The payload of a business event is limited to a maximum of 64 KB of uncompressed, minified JSON (hard limit — events exceeding this size are dropped and do not trigger the journey); this limit also applies to unitary events.
* Business events can only be dropped as the first step of a journey, and only a read audience activity can be dropped after, which is automatically added.
* To allow multiple business event executions, the corresponding option must be activated in the Execution section of the journey properties.
* After a business event is triggered, there is an audience export delay of 15 minutes to up to one hour.
* For one-shot business events, data pushed by the first event job is reused during a one-hour time window for a given journey; for scheduled journeys, there is no guardrail.
* Business events cannot be used in conjunction with unitary events or audience qualification activities.
* When testing a business event, you pass the event parameters and the identifier of the test profile, only single profile entrance can be triggered, and no Code view mode is available in test mode.

**Terminology:**

* Canonical name: Business event — Acronym: n/a — variants: business event configuration, rule-based business event
* Do not confuse: "Business event" (not linked to a specific profile, always rule-based) ≠ "Unitary event" (linked to a specific profile)
* Do not confuse: "Time series schema" (the only schema type available for business events) ≠ "Experience Events, Decision Events, and Journey Step Events schemas" (not available)

**FAQ:**

* **Q: What schema type does a business event require?** — Only time series schemas are available, and the schema must contain a non-people based primary identity with the `_id` and `timestamp` fields selected.
* **Q: How large can a business event payload be?** — Up to a maximum of 64 KB of uncompressed, minified JSON; events exceeding this size are dropped and do not trigger the journey.
* **Q: Where can a business event be placed in a journey?** — Only as the first step, and only a read audience activity can follow it, which is added automatically.
* **Q: How long is the delay before profiles enter the journey?** — After a business event is triggered, the audience export delay is 15 minutes to up to one hour.
* **Q: Can a business event be combined with unitary events?** — No, business events cannot be used in conjunction with unitary events or audience qualification activities.
* **Q: What happens to profiles already in the journey when a new business event arrives?** — Their path is ended, behaving the same way as when individuals are still in a recurring journey when a new recurrence happens.

+++

<!-- ai-section-version: 1 | source-hash: 9de81a1b -->
