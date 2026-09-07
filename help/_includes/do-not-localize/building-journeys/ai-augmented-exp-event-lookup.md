---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page outlines alternative patterns and best practices for using Experience Event data in Adobe Journey Optimizer journeys, in the context of the deprecation of direct experience event lookup in the journey expression editor.

**Intents:**

* Suppress opted-out profiles using built-in consent management instead of experience event expressions
* Exclude bounced email addresses using the AJO automatic suppression list
* Build generic suppression logic using batch audiences with event-based criteria
* Prevent over-communication by applying frequency capping rules or time-based audience conditions
* Personalize abandoned cart or browse communications using AEP Data Distiller or Computed attributes

**Glossary:**

* **Experience event**: A time-stamped, immutable record of a customer action or behavior stored in Adobe Experience Platform *(product-specific)*
* **Computed attribute**: A profile-level attribute derived from aggregating or summarizing experience event data over time, available for use in journey expressions *(product-specific)*
* **Suppression list**: AJO's built-in list of email addresses automatically excluded from future sends due to hard bounces or spam complaints *(product-specific)*
* **Frequency capping**: A business rule that limits how many messages a profile can receive within a defined time window *(product-specific)*
* **Data Distiller**: An AEP capability that enables SQL-based batch queries to extract and transform event data into profile-enabled datasets *(product-specific)*

**Guardrails:**

* Starting July 8, 2025, new customer organizations cannot create expressions using experience event attributes in the journey expression editor.
* Starting April 1, 2026, organizations that have not used experience event attributes in journey expressions in the last 90 days will lose access to this capability.
* Direct experience event lookup in journey conditions is being retired; alternatives include batch audiences, computed attributes, and AEP Data Distiller.
* Capabilities NOT impacted by the retirement include: triggering journeys with events, listening to events within a journey, using journey context data from trigger events, configuring events, and detecting reaction events.

**Terminology:**

* Canonical name: Experience event lookup — Acronym: EE lookup — variants: experience event expressions, event attribute lookup
* Synonyms: "batch audience with event-based logic" = "event-based segment" as a suppression/inclusion mechanism
* Do not confuse: "experience event lookup in expression editor" ≠ "triggering a journey with an event" — triggering journeys with events is NOT being retired

**FAQ:**

* **Q: Can I still trigger a journey using an experience event?** — Yes, triggering journeys with unitary or business events is not impacted by this change.
* **Q: What is the recommended replacement for experience event lookup in journey conditions?** — Use batch audiences built with AEP Segment Builder event-based logic, computed attributes, or AEP Data Distiller for complex transformations.
* **Q: Is my existing organization affected right now?** — New organizations are affected from July 8, 2025. Existing organizations are affected from April 1, 2026 only if they have not used the capability in the last 90 days.
* **Q: How do I handle cart abandonment personalization without direct event lookup?** — Use AEP Data Distiller to extract and write event data to a profile-enabled dataset, or use Computed attributes to capture the latest abandonment state on the profile.
* **Q: What capabilities are NOT impacted by this deprecation?** — Triggering journeys with events, listening to events inside journeys, using trigger event context data in expressions, configuring events, and detecting reaction events (e.g., email opens) are all unaffected.

+++
