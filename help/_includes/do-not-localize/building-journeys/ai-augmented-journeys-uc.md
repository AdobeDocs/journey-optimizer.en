---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page presents two practical journey use cases: a multi-channel message flow combining Read Audience, reaction events, email, and push; and a multi-phase loyalty journey pattern using the Jump activity to decompose complex journeys into manageable sub-journeys.

**Intents:**

* Build a multi-channel journey that sends a follow-up email or push based on whether a customer opens an initial email
* Configure a purchase event to trigger a thank-you push notification inside a journey
* Use reaction events to branch a journey based on email open behavior
* Decompose a complex multi-phase journey into smaller sub-journeys connected by Jump activities
* Create and configure a rule-based event for use as a journey trigger
* Define an audience based on city and birth year attributes for targeted journey entry

**Glossary:**

* **Reaction event**: A journey event that triggers when a profile interacts with a message (e.g., opens an email or clicks a link), enabling behavior-driven branching. *(product-specific)*
* **Read Audience activity**: The journey entry activity that loads all profiles in a specified Adobe Experience Platform audience to begin the journey. *(product-specific)*
* **Jump activity**: An action activity that pushes a profile from one journey (origin) to another (target), enabling modular sub-journey architecture. *(product-specific)*
* **Rule-based event**: An event type where the trigger condition is defined by a rule expression rather than an orchestration ID, useful for purchase or behavioral triggers. *(product-specific)*

**Guardrails:**

* A reaction event timeout path must be configured to handle profiles who do not interact with the message within the defined duration
* The audience used in the use case must be created before building the journey
* The purchase event must be configured before it can be used in the journey
* Sub-journeys connected via Jump must use the same namespace as the origin journey
* Email address override (parameter override) should only be used for specific use cases, not as a general replacement for the primary address

**Terminology:**

* Canonical name: Reaction event — Acronym: none — variants: reaction activity, message reaction
* Synonyms: "origin journey" = "source journey"; "target journey" = "destination journey"
* Do not confuse: "Read Audience activity" ≠ "Audience Qualification activity" — Read Audience loads all audience members in batch at once; Audience Qualification triggers per profile in real-time as membership changes

**FAQ:**

* **Q: How do I send a follow-up message only to customers who did not open an email?** — Add a Reaction event (Email opened) with a timeout path; profiles that do not open within the timeout duration flow down the timeout path where the follow-up email is placed.
* **Q: How is the purchase event configured in the multi-channel use case?** — As a rule-based event with a condition such as `purchaseMessage="thank you"`, configured with a schema, payload fields (product, date, purchase ID), namespace, and profile identifier.
* **Q: Why decompose a complex journey into sub-journeys?** — Complex journeys can expose 20 or more unique customer paths, and complexity grows exponentially with each touchpoint. Sub-journeys keep each phase readable, testable, and independently maintainable.
* **Q: Can a profile be in both the origin and target journey at the same time after a Jump?** — Yes; when a profile reaches a Jump step, it continues progressing in the origin journey while simultaneously entering the target journey.
* **Q: How many sub-journeys are used in the multi-phase loyalty example?** — Three sub-journeys: Phase 1 (app download), Phase 2 (first transaction), and Phase 3 (second transaction), connected sequentially using Jump activities.

+++
