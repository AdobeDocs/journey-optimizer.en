---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure a unitary event, which is linked to a specific profile and can be rule-based or system-generated, including its type, schema and payload fields, identity type, profile identifier, and payload preview.

**Intents:**

* Create a unitary event and choose the Rule Based or System Generated Event ID type
* Define the schema and select the payload fields the journey expects to receive
* Define the Event ID condition for rule-based events using the simple or advanced expression editor
* Add an identity type and define the profile identifier that reconciles the event with a profile
* Use the advanced expression editor to build more complex keys
* Preview the payload to validate the payload definition

**Glossary:**

* **Unitary event**: An event linked to a specific profile that can be rule-based or system-generated *(product-specific)*
* **Identity type**: The type of key used to identify the person associated to the event, previously known as namespace; only people-based identity types can be selected *(product-specific)*
* **Profile identifier**: The field, or combination of fields, from the event payload that allows the system to identify the person associated to the event *(product-specific)*
* **eventID**: The field required for system-generated events, automatically generated when creating the event; the system pushing the event should pass the one available in the payload preview *(product-specific)*
* **Orchestration field group**: The field group that must be added to the XDM schema for system-generated events so the schema contains all information required to work with Journey Optimizer *(product-specific)*
* **Advanced expression editor**: The editor you can switch to for creating more complex keys, such as a concatenation of two event fields *(product-specific)*

**Guardrails:**

* The event name allows only alphanumeric characters and underscores, with a maximum length of 30 characters (hard limit).
* When you select the System Generated type, only schemas that have the eventID type field are available; when you select the Rule Based type, all Experience Event schemas are available.
* Adding an identity type is optional but recommended, and only a people-based identity type can be selected.
* Only one identity type is allowed per journey, so events used in the same journey must use the same identity type.
* The same key, for example CRMID=3224, cannot be at two different places in the same journey.
* For system-generated events, the payload preview requires saving and re-opening the event to generate an event ID.

**Terminology:**

* Canonical name: Unitary event — Acronym: n/a — variants: unitary event configuration
* Synonyms: "Identity type" = "namespace"
* Do not confuse: "Rule Based" (defines a condition and does not generate an eventID) ≠ "System Generated" (requires an eventID automatically generated when creating the event)
* Do not confuse: "Event ID condition" (rule used to identify events that trigger the journey) ≠ "Profile identifier" (key used to identify the person associated to the event)

**FAQ:**

* **Q: What are the two Event ID types for a unitary event?** — Rule Based, which defines a condition and does not generate an eventID, and System Generated, which requires an eventID automatically generated when creating the event.
* **Q: Is defining an identity type required?** — It is optional but recommended, as it allows you to leverage information stored in the Real-time Customer Profile Service; only a people-based identity type can be selected.
* **Q: Why can two profiles not sit at the same place in a journey with the same key?** — A person cannot be at two different places in the same journey, so the system does not allow the same key to be at different places in the same journey.
* **Q: What schemas are available for a System Generated event?** — Only schemas that have the eventID type field; for Rule Based events, all Experience Event schemas are available.
* **Q: How do I preview the payload for a system-generated event?** — Save the event and re-open it first to generate an event ID, then use the View Payload icon to check the preview.

+++

<!-- ai-section-version: 1 | source-hash: bf9f8d81 -->
