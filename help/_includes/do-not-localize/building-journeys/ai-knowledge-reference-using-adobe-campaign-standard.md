---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the built-in Adobe Campaign Standard Email, SMS, and Push action activities in Journey Optimizer journeys via Campaign Transactional Messaging templates.

**Intents:**

* Configure Email, SMS, or Push action activities in a journey using Adobe Campaign Standard integration
* Select and map a Campaign Standard transactional messaging template to journey fields
* Map Address and Personalization Data fields from journey events or datasources to the message payload
* Handle unsubscription for event-based and profile-based transactional email templates
* Configure push notification target platform and registration token for Campaign Standard push actions

**Glossary:**

* **Transactional Messaging**: Adobe Campaign Standard capability for sending triggered, real-time messages (email, SMS, push) based on events *(product-specific)*
* **rtEvent**: Real-time event transactional message template in Adobe Campaign Standard, used for event-based messaging *(product-specific)*
* **Profile transactional template**: A Campaign Standard transactional message template that uses profile data for recipient resolution and unsubscription handling *(product-specific)*
* **Registration Token**: Device-level identifier required to target a push notification to a specific mobile app installation *(product-specific)*

**Guardrails:**

* The built-in action must be configured before use; refer to the action configuration page.
* Both the Campaign Standard transactional message and its associated event must be published for the template to be usable in Journey Optimizer.
* Collections cannot be passed in Personalization Data fields.
* For event-based (rtEvent) templates, unsubscription management must be handled manually with a condition before sending.
* For profile-based push messages, the Target fields are retrieved automatically; the Target category is only visible for event messages.
* Mobile app must be configured with Campaign Standard before the push activity can be used.

**Terminology:**

* Canonical name: Adobe Campaign Standard — Acronym: ACS — variants: Campaign Standard
* Synonyms: "event transactional message" = "rtEvent"; "real-time transactional message" = "rtEvent"
* Do not confuse: "profile transactional template" (unsubscription handled automatically) ≠ "event transactional template" (unsubscription must be handled manually)

**FAQ:**

* **Q: What channels are available through the Adobe Campaign Standard integration?** — Email, SMS, and Push notification channels are available as built-in action activities.
* **Q: Does the transactional message need to be published in Campaign Standard before using it in Journey Optimizer?** — Yes, both the transactional message and its associated event must be published; an unpublished message will not be usable even if visible in the interface.
* **Q: How is unsubscription handled for profile-based email templates?** — Unsubscription is automatically handled by Adobe Campaign Standard when using a profile transactional template; include an Unsubscription link content block in the template.
* **Q: Can I pass a collection as personalization data?** — No, collections cannot be passed in Personalization Data; the transactional message must not expect collections.
* **Q: Where do I map the recipient address for an event-based email?** — The Address category in the activity configuration pane is only visible for event transactional messages; for profile messages the address is retrieved automatically.

+++
