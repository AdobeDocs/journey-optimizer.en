---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page presents two practical journey use cases: a multi-channel message flow combining Read Audience, reaction events, email, and push; and a multi-phase loyalty journey pattern using the Jump activity to decompose complex journeys into manageable sub-journeys.

**Intents:**

* Build a multi-channel journey that sends a follow-up email if a customer does not open the initial email, or a thank-you push after an email open and purchase
* Configure a purchase event to trigger a thank-you push notification inside a journey
* Use reaction events to branch a journey based on email open behavior
* Decompose a complex multi-phase journey into smaller sub-journeys connected by Jump activities
* Create and configure a rule-based event for use as a journey trigger
* Define an audience based on city and birth year attributes for targeted journey entry

**Glossary:**

* **Reaction event**: In this use case, an event configured as **Email opened** that triggers when an individual in the audience opens the email. *(product-specific)*
* **Read Audience activity**: The activity through which all individuals belonging to the selected audience enter the journey. *(product-specific)*
* **Jump activity**: The activity used to connect sub-journeys so profiles pass from one phase to the next. *(product-specific)*
* **Rule-based event**: The event type used for the purchase event, with an **[!UICONTROL Event ID condition]** that identifies events triggering the journey. *(product-specific)*

**Guardrails:**
* The journey must be validated before testing. Errors in the Alerts panel must be resolved and validation rerun before continuing.

* In the multi-channel example, **Define the event timeout** is set to 1 day and **Set a timeout path** is enabled for individuals who do not open the first message.
* The audience used in the use case must be created before building the journey
* The purchase event must be configured before it can be used in the journey

**Terminology:**

* Canonical names: Read Audience, Reaction, **[!UICONTROL Jump]**.
* Do not confuse: the **Email opened** reaction event detects an email open; the purchase event detects a purchase before the thank-you push is sent.

**FAQ:**

* **Q: How do I send a follow-up message only to customers who did not open an email?** — Add a Reaction event (Email opened) with a timeout path; profiles that do not open within the timeout duration flow down the timeout path where the follow-up email is placed.
* **Q: How is the purchase event configured in the multi-channel use case?** — As a rule-based event with a condition such as `purchaseMessage="thank you"`, configured with a schema, payload fields (product, date, purchase ID), namespace, and profile identifier.
* **Q: Why decompose a complex journey into sub-journeys?** — The loyalty example exposes more than 20 unique customer paths, and complexity grows exponentially with each additional touchpoint or channel. Sub-journeys keep each phase manageable, testable, and independently maintainable.
* **Q: How many sub-journeys are used in the multi-phase loyalty example?** — Three sub-journeys: Phase 1 (app download), Phase 2 (first transaction), and Phase 3 (second transaction), connected sequentially using Jump activities.

+++

<!-- ai-section-version: 1 | source-hash: 8703ffa0 -->
