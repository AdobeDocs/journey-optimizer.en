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
* Follow the six-step journey creation workflow: Plan, Design, Validate and test, Publish, Monitor, Optimize
* Use Simulation, Test mode, or Dry run to validate a journey before going live
* Publish a journey and monitor performance through reports and alerts
* Explore advanced capabilities such as expressions, timezone management, copy to sandbox, and throughput control

**Glossary:**

* **Journey**: An automated, multistep customer experience that orchestrates personalized interactions across channels in response to customer behavior, business events, or scheduled campaigns. *(product-specific)*
* **Journey designer**: The visual drag-and-drop canvas in Adobe Journey Optimizer used to build and configure journey flows without writing code. *(product-specific)*
* **Test mode**: A way to walk real, designated test profiles through the journey step by step. *(product-specific)*
* **Dry run**: A way to execute the journey against real production data without sending communications or updating profiles. *(product-specific)*
* **Journey Simulation**: A way to test journeys for fast iteration with temporary simulated users, with no test profiles needed. *(product-specific)*
* **Orchestrated campaigns**: Multi-step batch workflows in Adobe Journey Optimizer that use relational data (profiles + products/stores/bookings) and process all profiles together with exact pre-send counts. *(product-specific)*

**Guardrails:**
* Configuration validation must pass before testing. Errors in the Alerts panel must be resolved and validation rerun before continuing. Publication requires current, passed validation; edits after validation require **[!UICONTROL Validate]** again.

* Live journeys cannot be structurally edited; changes require creating a new version
* After validation passes, test before publishing using Journey Simulation, test mode, or dry run

**Terminology:**

* Canonical name: Journey — variant: customer journey
* Synonyms: "journey designer" = "canvas"
* Do not confuse: "Journey" ≠ "Campaign" — Journeys maintain individual customer state for real-time, multi-step behavior-driven experiences; Campaigns deliver messages in batch to audiences on a schedule or via API trigger
* Do not confuse: "Journey Simulation" uses temporary simulated users; "test mode" uses real, designated test profiles; "dry run" executes against real production data without sending communications or updating profiles

**FAQ:**

* **Q: What is the difference between a journey and a campaign in Journey Optimizer?** — Journeys provide 1:1 real-time orchestration where each profile progresses at its own pace through conditional logic; Campaigns deliver messages simultaneously to an audience on a schedule or via API trigger; Orchestrated campaigns are batch canvas workflows for complex multi-entity segmentation.
* **Q: Can I edit a live journey?** — Limited elements such as name and message content can be edited; structural changes require creating a new version of the journey.
* **Q: What are the steps to build a journey?** — The six-step workflow is: Plan, Design, Validate and test, Publish, Monitor, and Optimize.
* **Q: How do I test a journey without sending communications or updating profiles?** — First Validate and resolve any errors, then use dry run to execute the journey against real production data without sending communications or updating profiles.
* **Q: What journey type should I use for a welcome email triggered by a subscription?** — Use a Unitary journey, which is triggered by a specific individual event such as a subscription sign-up.

+++

<!-- ai-section-version: 1 | source-hash: c0a7eb89 -->
