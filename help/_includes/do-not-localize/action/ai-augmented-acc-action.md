---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to integrate Journey Optimizer with Adobe Campaign v7 or v8 so journeys can send emails, push notifications, and SMS through Adobe Campaign Transactional Messaging.

**Intents:**

* Request activation of the connection between Journey Optimizer and Adobe Campaign environments
* Prepare the transactional message, its associated event, and the JSON payload in Adobe Campaign
* Configure a Campaign action of type Adobe Campaign Classic in Journey Optimizer
* Set payload fields as static or variable for mapping on the journey canvas
* Update an existing Campaign action when the Real-Time endpoint changes

**Glossary:**

* **Campaign action activity**: The activity available in the journey designer palette for each configured Adobe Campaign v7/v8 action *(product-specific)*
* **Transactional Messaging**: The Adobe Campaign capability used to send emails, push notifications, and SMS triggered from Journey Optimizer *(product-specific)*
* **eventType**: The internal name of the Adobe Campaign event referenced in the JSON payload *(product-specific)*
* **ctx**: The payload object holding variables based on the personalization present in the Campaign message *(product-specific)*

**Guardrails:**

* There is no throttling of messages; the system caps the number of messages that can be sent to 4,000 per 5 minutes, based on the current Campaign SLA.
* Because of that cap, Journey Optimizer should only be used in unitary use cases (individual events, not audiences).
* You must configure one action on the canvas per template, meaning one action in Journey Optimizer for each Adobe Campaign template you wish to use.
* There is no validation that the payload or Campaign message is correct.
* You cannot use a Campaign action with an audience qualification event.
* Adobe recommends using a dedicated Message Center hosted or Managed Services instance to avoid impacting other Campaign operations.

**Terminology:**

* Canonical name: Adobe Campaign v7/v8 integration — Acronym: ACC — variants: Campaign action, Adobe Campaign Classic action, Campaign v7/v8 custom action
* Synonyms: "Adobe Campaign Classic" = "Adobe Campaign v7"
* Do not confuse: "Campaign action" (Adobe Campaign v7/v8 integration) ≠ "custom action" (generic third-party REST API action)

**FAQ:**

* **Q: How is the connection between Journey Optimizer and Adobe Campaign established?** — It is set up by Adobe at provisioning time; if it was not requested then, contact Adobe Journey Optimizer support and provide the Org ID, Sandbox Name, Campaign Server URL, Real-Time Server URL, and Campaign version.
* **Q: What is the message sending cap for this integration?** — There is no throttling, but the system caps messages to 4,000 per 5 minutes based on the current Campaign SLA.
* **Q: Why should this integration be used only for unitary use cases?** — Because there is no throttling and messages are capped to 4,000 per 5 minutes, it suits individual events rather than audiences.
* **Q: Why can a Campaign action not be used with an audience qualification event?** — Campaign actions are not supported with an audience qualification event.
* **Q: How do I update a Campaign action when the Real-Time endpoint changes?** — Edit the action, update the URL field with the new RT endpoint, adjust the Payload if needed, click Test to validate the connection, then Save.

+++

<!-- ai-section-version: 1 | source-hash: 6a049c54 -->
