---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use general (unitary and business) events in journeys to trigger real-time, individual-level message delivery, including how to configure event timeouts and timeout paths.

**Intents:**
* Add a general event activity to a journey canvas to trigger real-time profile entry
* Configure an event timeout to limit how long a journey listens for an event
* Set up a timeout path to handle profiles that do not trigger the expected event in time
* Distinguish between unitary events and business events and understand when each is added automatically
* Combine event timeouts with Wait activities to control multi-event timeout behaviour

**Glossary:**
* **Unitary event**: An event that triggers the journey for one individual at a time, in real-time *(product-specific)*
* **Business event**: A non-profile-related event that triggers a journey for an audience of profiles, automatically adding a Read Audience activity *(product-specific)*
* **Event timeout**: A configurable duration (up to 90 days) after which the journey stops waiting for a specific event and routes the profile to a timeout path *(product-specific)*
* **Timeout path**: An optional journey branch that profiles follow when the expected event is not received within the timeout window *(product-specific)*

**Guardrails:**
* Event label and description are the only editable fields for a general event on the canvas; all other configuration is performed by a technical user and cannot be changed from the journey
* Maximum event timeout duration is 90 days
* When multiple events follow a Wait activity, the timeout must be configured on only one of those events; the defined timeout then applies to all events after the Wait
* If no timeout path is defined, the timeout acts as a Wait activity; profiles that do not receive the event remain in the journey until the timeout elapses

**Terminology:**
* Canonical name: General event — Acronym: none — variants: unitary event, custom event
* Synonyms: "general event" = "unitary event" (in the context of the canvas activity)
* Do not confuse: "business event" ≠ "unitary event" — a business event targets an audience of profiles, while a unitary event targets a single individual

**FAQ:**
* **Q: Can I change the event configuration from the journey canvas?** — No; only the label and description can be edited on the canvas. The full event configuration is set by a technical user and cannot be modified from the journey.
* **Q: What happens if no event is received before the timeout expires?** — If a timeout path is defined, the profile flows into that path. If no timeout path is set, the timeout behaves like a Wait activity and the profile continues the journey after the timeout period.
* **Q: What is the maximum event timeout duration?** — 90 days.
* **Q: When should I enable the timeout path option?** — Always enable it if you want profiles to exit that branch after the timeout; without a timeout path, profiles remain in the journey waiting for the event.
* **Q: How does a business event differ from a unitary event in the journey canvas?** — Dropping a business event automatically adds a Read Audience activity, because business events target multiple profiles simultaneously rather than a single individual.

+++
