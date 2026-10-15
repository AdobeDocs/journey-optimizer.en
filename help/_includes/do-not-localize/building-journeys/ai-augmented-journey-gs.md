---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page walks through the four key steps to create a first journey in Adobe Journey Optimizer — defining an entry point, designing the canvas, testing with test mode or Dry run, and publishing — along with guidance on choosing the right entry type.

**Intents:**
* Create a new journey and configure its properties in the JOURNEY MANAGEMENT menu
* Choose the correct entry point (Read Audience, Audience Qualification, unitary event, or business event) for a given use case
* Design a multi-step journey by dragging and dropping events, orchestration activities, and channel actions onto the canvas
* Test a journey using Test mode with test profiles or Dry run before publishing
* Execute a Dry run to validate audience targeting with real production data without contacting customers
* Publish a journey to make it live and monitor its performance with reporting tools

**Glossary:**
* **Read Audience**: An entry activity that processes all profiles in a batch audience at once or on a schedule *(product-specific)*
* **Audience Qualification**: An entry activity triggered in real time when a profile enters or exits a streaming audience *(product-specific)*
* **Unitary event**: A real-time trigger that enters one profile at a time into a journey when a specific action occurs *(product-specific)*
* **Business event**: A non-profile event (e.g., flight cancellation, stock replenishment) that triggers a journey for multiple profiles simultaneously via an automatic Read Audience step *(product-specific)*
* **Test mode**: A way to view test profiles as they move along a journey to detect potential errors before activation *(product-specific)*
* **Dry run**: A special publication mode that uses real production data to validate journey logic without contacting actual customers or updating profiles *(product-specific)*

**Guardrails:**
* The journey must pass configuration validation before testing. Publication requires completed testing and current, passed validation; edits after validation require **[!UICONTROL Validate]** again and resolution of errors before continuing.
* A journey cannot be published if it contains errors; all errors must be resolved first
* Configure an event before building an event-based journey to define the trigger and the data it carries
* Audience creation in Adobe Experience Platform is a prerequisite for audience-based journeys

**Terminology:**
* Canonical name: Journey — variant: customer journey
* Synonyms: "Dry run" = "Dry run mode"
* Do not confuse: "Test mode" uses test profiles; "Dry run" uses real production data without contacting customers or updating profiles

**FAQ:**
* **Q: What is the first thing I need to do before creating an event-triggered journey?** — Configure the event to define the trigger and the data it carries; then use an event-based entry.
* **Q: Which entry point is recommended for someone new to Journey Optimizer?** — Start with an audience-based journey using a Read Audience activity — it requires no prior event configuration and is the easiest way to get familiar with the canvas.
* **Q: Can I test my journey before it goes live?** — Yes; first Validate and resolve any errors, then use Test mode with test profiles or Dry run with real production data without contacting real customers or updating profile information.
* **Q: What happens if my journey has errors when I try to publish?** — You cannot publish a journey with errors; all configuration errors must be resolved before publication.
* **Q: How do I break up a complex journey with many steps?** — Use the Jump activity to connect smaller sub-journeys, reducing complexity and making each sub-journey easier to test independently.

+++

<!-- ai-section-version: 1 | source-hash: 92f4371f -->
