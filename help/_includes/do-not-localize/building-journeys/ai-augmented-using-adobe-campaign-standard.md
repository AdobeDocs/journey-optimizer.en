---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the built-in Adobe Campaign Standard Email, SMS, and Push actions in Journey Optimizer journeys via Campaign Transactional Messaging templates.

**Intents:**

* Configure the built-in Email, SMS, or Push actions in a journey using Adobe Campaign Standard integration
* Select and map a Campaign Standard transactional messaging template to journey fields
* Map Address and Personalization Data fields from journey events or datasources to the message payload
* Handle unsubscription for event-based and profile-based transactional email templates
* Configure push notification target platform and registration token for Campaign Standard push actions

**Glossary:**

* **Transactional Messaging**: Adobe Campaign Standard feature on which the built-in email, SMS, and push channels rely to execute message sending *(product-specific)*
* **rtEvent**: Abbreviation used for real-time transactional messages, also called event transactional messaging templates *(product-specific)*
* **Profile transactional template**: A Campaign Standard transactional messaging template of the profile type; for profile messages the Address (or Target for push) fields are retrieved automatically by the system, and for email the unsubscription mechanism is handled by Adobe Campaign Standard *(product-specific)*
* **Registration Token**: A field defined in the Target category of a push action; the expression depends on how the token is defined in the event payload or in other Journey Optimizer information *(product-specific)*

**Guardrails:**

* The built-in action must be configured before use; refer to the action configuration page.
* Both the Campaign Standard transactional message and its associated event must be published for the template to be usable in Journey Optimizer.
* Collections cannot be passed in Personalization Data fields.
* For real-time transactional messages (rtEvent), a specific setup is required for fatigue, block list, or unsubscription management; for example, add a condition before the message sending to check an unsubscribe attribute stored in Adobe Experience Platform or in a third-party system.
* For profile-based push messages, the Target fields are retrieved automatically; the Target category is only visible for event messages.
* Mobile app must be configured with Campaign Standard before the push action can be used.

**Terminology:**

* Canonical name: Adobe Campaign Standard — Acronym: n/a — variants: Campaign Standard
* Synonyms: "event" transactional messaging template = "real-time" template; "real-time transactional messages" = "rtEvent"
* Do not confuse: "profile transactional template" (unsubscription mechanism handled automatically by Adobe Campaign Standard for email) ≠ "event-based template (rtEvent)" (incorporate a link in the message that directs recipients to an unsubscription landing page)

**FAQ:**

* **Q: What channels are available through the Adobe Campaign Standard integration?** — Email, SMS, and Push are available as built-in actions when you have Adobe Campaign Standard.
* **Q: Does the transactional message need to be published in Campaign Standard before using it in Journey Optimizer?** — Yes, both the transactional message and its associated event must be published. If the event is published but the message is not, the message is not visible in the Journey Optimizer interface; if the message is published but its event is not, it is visible but not usable.
* **Q: How is unsubscription handled for profile-based email templates?** — Unsubscription is automatically handled by Adobe Campaign Standard when using a profile transactional template; include an Unsubscription link content block in the template.
* **Q: Can I pass a collection as personalization data?** — No, collections cannot be passed in Personalization Data; the transactional message must not expect collections.
* **Q: Where do I map the recipient address for an event-based email?** — The Address category in the activity configuration pane is only visible for event transactional messages; for profile messages the address is retrieved automatically.

+++
