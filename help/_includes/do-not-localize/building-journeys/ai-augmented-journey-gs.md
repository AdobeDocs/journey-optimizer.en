---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page walks through the four key steps to create a first journey in Adobe Journey Optimizer — defining an entry point, designing the canvas, testing with test mode or Dry run, and publishing — along with guidance on choosing the right entry type.

**Intents:**
* Create a new journey and configure its properties in the Journey Management menu
* Choose the correct entry point (Read Audience, Audience Qualification, unitary event, or business event) for a given use case
* Design a multi-step journey by dragging and dropping events, orchestration activities, and channel actions onto the canvas
* Test a journey using Simulation, Test mode with persistent AEP test profiles, or Dry run before publishing
* Execute a Dry run to validate audience targeting with real production data without contacting customers
* Publish a journey to make it live and monitor its performance with reporting tools

**Glossary:**
* **Read Audience**: An entry activity that processes all profiles in a batch audience at once or on a schedule *(product-specific)*
* **Audience Qualification**: An entry activity triggered in real time when a profile enters or exits a streaming audience *(product-specific)*
* **Unitary event**: A real-time trigger that enters one profile at a time into a journey when a specific action occurs *(product-specific)*
* **Business event**: A non-profile event (e.g., flight cancellation, stock replenishment) that triggers a journey for multiple profiles simultaneously via an automatic Read Audience step *(product-specific)*
* **Test mode**: A validation mode that uses persistent Adobe Experience Platform test profiles (explicitly flagged as test profiles) to traverse a draft journey before publication *(product-specific)*
* **Simulation**: A validation mode that uses temporary simulated users generated on the fly; simulated users do not persist in Adobe Experience Platform *(product-specific)*
* **Dry run**: A special publication mode that uses real production data to validate journey logic without contacting actual customers or updating profiles *(product-specific)*

**Guardrails:**
* A journey cannot be published if it contains errors; all errors must be resolved first
* Event configuration (for event-based entry) must be completed by a data engineer before the journey can be built
* Journey guardrails and limitations are documented separately and should be reviewed before designing at scale
* Audience creation in Adobe Experience Platform is a prerequisite for audience-based journeys

**Terminology:**
* Canonical name: Journey — Acronym: none — variants: customer journey, orchestration flow
* Synonyms: "Test mode" = "journey testing"; "Dry run" = "dry run mode"
* Do not confuse: "Simulation" ≠ "Test mode" ≠ "Dry run" — Simulation uses temporary simulated users; Test mode uses persistent AEP test profiles; Dry run uses real production data without contacting customers or updating profiles

**FAQ:**
* **Q: What is the first thing I need to do before creating an event-triggered journey?** — Configure the event with a data engineer to define the trigger and the data it carries; then reference the event as the journey entry point.
* **Q: Which entry point is recommended for someone new to Journey Optimizer?** — Start with an audience-based journey using a Read Audience activity — it requires no prior event configuration and is the easiest way to get familiar with the canvas.
* **Q: Can I test my journey before it goes live?** — Yes; use Simulation with temporary simulated users, Test mode with persistent AEP test profiles, or Dry run to execute against real production data without sending communications.
* **Q: What happens if my journey has errors when I try to publish?** — You cannot publish a journey with errors; all configuration errors must be resolved before publication.
* **Q: How do I break up a complex journey with many steps?** — Use the Jump activity to connect smaller sub-journeys, reducing complexity and making each sub-journey easier to test independently.

+++
