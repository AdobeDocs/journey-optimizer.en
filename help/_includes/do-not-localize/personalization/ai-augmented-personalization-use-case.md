---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page walks through an order status push notification use case combining three types of personalization — profile field, offer decision, and contextual journey data — in a single message.

**Intents:**

* Create a journey with an order event and a Push action activity
* Add profile-based personalization (customer's first name) to the push title
* Add contextual data personalization (order number, item name, order progress) from the journey event
* Add offer decision personalization to the push body
* Test the journey in test mode and publish

**Glossary:**

* **Profile personalization**: Personalization based on a profile field such as first name, accessed via `profile.*` attributes. *(product-specific)*
* **Offer decision**: Personalization based on decision management variables; inserted from the Offer decisions menu in the personalization editor. *(product-specific)*
* **Contextual personalization**: Personalization based on data from the journey — event fields (e.g., order number, item name, order progress) and journey properties (e.g., journey ID, errors). Available only when a journey has passed contextual data to the message. *(product-specific)*
* **Journey Properties**: Technical fields related to the journey for a given profile — such as journey ID or errors encountered — accessible under Contextual attributes > Journey Orchestration. *(product-specific)*

**Guardrails:**

* Contextual attributes are available in the personalization editor only if a journey has passed contextual data to the message.
* Test mode works only with test profiles; the profile identifier entered in the event configuration must correspond to an existing test profile.

**Terminology:**

* **Canonical name:** contextual personalization — variants: context-based personalization, journey context personalization
* **Synonyms:** "Journey Orchestration" (UI label under Contextual attributes menu) = contextual journey data source
* **Do not confuse:** Profile personalization (static profile field values, always available) ≠ Contextual personalization (journey event and properties data, only available after journey context has been passed to the message) ≠ Offer decision personalization (decision management variables)

**FAQ:**

* **Q: What three types of personalization are combined in this use case?** — Profile personalization (customer's first name from `profile.*`), contextual data personalization (order number, item name, and order progress from the journey event), and offer decision personalization (a decision management offer inserted in the body).
* **Q: Where do contextual attributes come from in the personalization editor?** — Contextual attributes come from events placed before the channel action activity in the journey, and from journey technical properties. They appear in the personalization editor under Contextual attributes > Journey Orchestration > Events (event fields) or Journey Properties (journey metadata).
* **Q: What are the prerequisites for this use case?** — An order event must be configured with order number, status, and item name fields, and a decision must exist in decision management.
* **Q: How do I test the push notification in this use case?** — Click the Test button in the journey, then click "Trigger an event" and enter the event values in the Event configuration window. Test mode only works with test profiles; the profile identifier must correspond to an existing test profile.

+++

<!-- ai-section-version: 1 | source-hash: ae5284c7 -->
