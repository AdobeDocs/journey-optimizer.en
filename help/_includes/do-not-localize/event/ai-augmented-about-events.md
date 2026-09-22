---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page describes the three journey event types (unitary, business, and audience qualification), their schema requirements and key constraints, how to choose the right one, throughput limits, and how events reach Journey Optimizer.

**Intents:**

* Understand the differences between unitary, business, and audience qualification events
* Choose the right event type for a use case based on whether you target one person or many profiles
* Learn the schema requirements and entry behavior for each event type
* Understand event ID types and which events can trigger journeys
* Plan for throughput limits and reentrance behavior before configuring events
* Know what can be changed or deleted on an event used in a journey

**Glossary:**

* **Unitary event**: An event linked to a person, based on their behavior, which can be rule-based or system generated and starts a real-time single-profile journey *(product-specific)*
* **Business event**: An event not linked to a specific profile, always rule-based, that automatically adds a Read Audience activity and broadcasts to many profiles *(product-specific)*
* **Audience qualification event**: An event triggered when a profile enters or exits an audience, selected directly on the journey canvas rather than in Administration *(product-specific)*
* **Read Audience activity**: The activity automatically added after a business event to define which profiles receive the journey *(product-specific)*
* **Rule-based event**: A unitary or business event that does not generate an eventID and instead defines a rule used to identify relevant events *(product-specific)*
* **System-generated event**: A unitary event that requires an eventID, automatically generated when the event is created *(product-specific)*

**Guardrails:**

* Event configuration is mandatory and must be performed by a Data engineer; prerequisites are the Journey Optimizer Administrator or Data Engineer role, an XDM schema with Real-Time Customer Profile enabled, an active streaming endpoint, and access to the correct sandbox.
* Throughput is limited to 5,000 events per second per organization, across all sandboxes, for unitary events and for Read Audience based journey events (hard limit); when a limit is reached, new events are queued and processed at 5,000 per second until the queue is drained.
* A capping rule limits rule-based events to 5,000 qualified events per second for a given Organization, corresponding to Journey Optimizer SLAs.
* Throughput limits apply to all events used in active journeys, which includes Live, Dry run, Closed, and Paused journeys.
* Profile reentrance is blocked by default for 5 minutes after a unitary journey triggers.
* A journey can contain only one business event, which must be the first step; business events cannot be used in the same journey as unitary events or audience qualification activities.
* Only streamed events can trigger journeys; events ingested in batch, inserted via Query Service, or from internal Journey Optimizer datasets cannot, and a Read Audience activity should be used instead.
* Unitary events require an XDM ExperienceEvent schema with a person-based primary identity and Real-Time Customer Profile enabled; business events require a time-series schema with a non-person primary identity and populated `_id` and `timestamp` fields, with an audience export delay of 15 minutes to up to one hour.
* When editing an event used in a Draft, Live, or Closed journey, you can only change the name, the description, or add payload fields; events used in Live, Draft, or Closed journeys cannot be deleted.

**Terminology:**

* Canonical name: Journey event — Acronym: n/a — variants: event, journey trigger event
* Do not confuse: "Unitary event" (linked to a specific person) ≠ "Business event" (external occurrence not tied to one person) ≠ "Audience qualification event" (triggered when a profile enters or exits an audience)
* Do not confuse: "Rule-based" (defines a rule, no eventID generated) ≠ "System-generated" (requires an automatically generated eventID)

**FAQ:**

* **Q: Can I use the same event in multiple journeys?** — Yes, several journeys can listen to the same event simultaneously.
* **Q: Can I combine a business event and a unitary event in the same journey?** — No, business events cannot be used in the same journey as unitary events or audience qualification activities.
* **Q: Do I need to configure anything for audience qualification events?** — No, they are not configured in Administration > Events; the audience is selected directly on the journey canvas as the first step.
* **Q: Can I use batch-ingested data to trigger a journey?** — No, only streamed events can trigger journeys; for batch data, build an audience and use a Read Audience activity instead.
* **Q: What is the throughput limit for events?** — 5,000 events per second per organization, across all sandboxes, for unitary events and for Read Audience based journey events.
* **Q: My journey is not triggering — what should I check?** — Verify the event schema has Real-Time Customer Profile enabled, confirm events are streamed, check that rule-based conditions match the incoming payload, and confirm the journey is in Live status with the profile meeting any entry conditions.

+++

<!-- ai-section-version: 1 | source-hash: 7d9ddd04 -->
