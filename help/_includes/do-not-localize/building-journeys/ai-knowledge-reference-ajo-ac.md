---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides a step-by-step use case for sending a transactional email from Adobe Journey Optimizer using the integration with Adobe Campaign v7/v8, covering Campaign template creation, event and action configuration, and journey design.

**Intents:**
* Configure a transactional email template in Adobe Campaign v7/v8 for use with Journey Optimizer
* Create an event in Journey Optimizer that includes custom fields such as a purchase order number
* Create and configure a Campaign Classic action in Journey Optimizer with a JSON payload
* Map journey event fields to Campaign personalization variables in the action configuration
* Build and publish a journey that triggers a Campaign transactional email

**Glossary:**
* **Transactional Messaging**: A Campaign feature that sends real-time, triggered emails based on events; must be configured before this integration can be used *(product-specific)*
* **Event type (eventType)**: An enumeration value defined in Campaign that identifies the type of transactional event; its internal name is referenced in the JSON payload *(product-specific)*
* **Campaign Classic action**: A Journey Optimizer action type that connects to Adobe Campaign v7/v8 to send transactional messages *(product-specific)*
* **Payload field**: The JSON structure pasted into a Journey Optimizer action that defines the data fields sent to Campaign *(product-specific)*

**Guardrails:**
* Campaign v7/v8 build 9125 or higher is required for this integration
* The Transactional Messaging feature must be configured in the Campaign instance before use
* After creating a new event type in Campaign, you must disconnect and reconnect to the instance for it to take effect
* Personalization field values set as "Constant" in the action must be changed to "Variable" to allow dynamic population at runtime

**Terminology:**
* Canonical name: Adobe Campaign v7/v8 — Acronym: ACC — variants: Campaign Classic, Campaign v7, Campaign v8
* Synonyms: "eventType" = "event type internal name"
* Do not confuse: "Campaign Classic action" ≠ "custom action" (Campaign Classic action is a specific built-in action type for ACC integration)

**FAQ:**
* **Q: What Campaign version is required for this integration?** — Campaign v7/v8 build 9125 or higher is required.
* **Q: What must be configured in Campaign before starting?** — The Transactional Messaging feature must be configured and a transactional email template must be created based on the event type.
* **Q: How do I make personalization fields dynamic in the Journey Optimizer action?** — In the action payload configuration, change the field configuration from "Constant" to "Variable" for fields that will be populated at runtime.
* **Q: Where does the first name personalization data come from in this use case?** — The first name comes from the Adobe Experience Platform data source, while the order number comes from the Journey Optimizer event payload.
* **Q: How do I connect the Journey Optimizer action to the Campaign template?** — Select "Adobe Campaign Classic" as the Action type, then paste the JSON payload that matches the transactional message template structure.

+++
