---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is the getting-started hub for Adobe Journey Optimizer journeys, explaining what journeys are, the four journey types, the six-step creation workflow, real-world use cases, and links to advanced capabilities.

**Intents:**

* Understand what journeys are and how they differ from campaigns and orchestrated campaigns
* Choose the right journey type (Unitary, Read Audience, Audience Qualification, or Business event) for a use case
* Follow the six-step journey creation workflow: Plan, Design, Test, Publish, Monitor, Optimize
* Use Simulation, Test mode, or Dry run to validate a journey before going live
* Publish a journey and monitor performance through reports and alerts
* Explore advanced capabilities such as expressions, timezone management, copy to sandbox, and throughput control

**Glossary:**

* **Journey**: An automated, multistep customer experience that orchestrates personalized interactions across channels in response to customer behavior, business events, or scheduled campaigns. *(product-specific)*
* **Journey designer**: The visual drag-and-drop canvas in AJO used to build and configure journey flows without writing code. *(product-specific)*
* **Test mode**: A journey validation mode that uses persistent Adobe Experience Platform test profiles (explicitly flagged as test profiles) to traverse a draft journey before it is published. *(product-specific)*
* **Dry run**: A special publication mode that executes the journey against real production data without sending communications or updating profiles. *(product-specific)*
* **Simulation**: A validation mode that uses temporary simulated users, manually created or auto-generated; simulated users do not persist in Adobe Experience Platform. *(product-specific)*
* **Orchestrated campaigns**: Multi-step batch workflows in AJO that use relational data (profiles + products/stores/bookings) and process all profiles together with exact pre-send counts. *(product-specific)*

**Guardrails:**

* Live journeys cannot be structurally edited; changes require creating a new version
* Test mode and dry run must be used before publishing to catch issues

**Terminology:**

* Canonical name: Journey — Acronym: none — variants: customer journey, AJO journey
* Synonyms: "journey designer" = "canvas" = "journey canvas"
* Do not confuse: "Journey" ≠ "Campaign" — Journeys maintain individual customer state for real-time, multi-step behavior-driven experiences; Campaigns deliver messages in batch to audiences on a schedule or via API trigger
* Do not confuse: "Simulation" ≠ "Test mode" ≠ "Dry run" — Simulation uses temporary simulated users; Test mode uses persistent AEP test profiles in a draft journey; Dry run executes against real production data without contacting customers or updating profiles

**FAQ:**

* **Q: What is the difference between a journey and a campaign in Journey Optimizer?** — Journeys provide 1:1 real-time orchestration where each profile progresses at its own pace through conditional logic; Campaigns deliver messages simultaneously to an audience on a schedule or via API trigger; Orchestrated campaigns are batch canvas workflows for complex multi-entity segmentation.
* **Q: Can I edit a live journey?** — Limited elements such as name and message content can be edited; structural changes require creating a new version of the journey.
* **Q: What are the steps to build a journey?** — The six-step workflow is: Plan, Design in the canvas, Test (test mode or dry run), Publish, Monitor performance, and Optimize/iterate.
* **Q: How do I validate a journey without contacting real customers?** — Use Simulation (temporary simulated users — note this does send real messages, but only to the execution addresses configured on those simulated users), Test mode (persistent AEP test profiles — note this does send real messages to those test profiles' inboxes), or Dry run (real production data, action nodes bypassed, no messages sent). Dry run profiles count toward Engageable Profiles and live journey quota. See [Choose a validation method](choose-validation-method.md) for a full comparison.
* **Q: What journey type should I use for a welcome email triggered by a subscription?** — Use a Unitary journey, which is triggered by a specific individual event such as a subscription sign-up.

+++
