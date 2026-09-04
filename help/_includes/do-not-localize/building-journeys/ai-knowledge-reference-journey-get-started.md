---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This is the comprehensive getting-started guide for journey orchestration in Adobe Journey Optimizer, covering key capabilities (real-time and batch delivery, contextual data, built-in and custom actions, the visual designer, Journey Fragments, and testing), common use cases, and links to all major learning resources.

**Intents:**
* Understand the key capabilities available in the Journey Optimizer journey designer before building a first journey
* Navigate to the correct resource for creating, managing, testing, or troubleshooting journeys
* Learn how to trigger 1:1 real-time messages across any channel using the journey designer
* Discover how Journey Fragments enable reuse of common node logic across journeys
* Access video tutorials and step-by-step guides for common journey use cases such as welcome series, cart abandonment, and send-time optimization

**Glossary:**
* **Journey designer**: The drag-and-drop visual canvas in Adobe Journey Optimizer used to build and orchestrate multi-step customer journeys *(product-specific)*
* **Journey Fragment**: A reusable set of journey nodes (e.g., eligibility check, channel routing logic) built once and inserted into multiple journeys *(product-specific)*
* **Unitary delivery**: A real-time message triggered for a single profile when a specific event occurs *(product-specific)*
* **Batch delivery**: Messages sent to all profiles in an Adobe Experience Platform audience at once or on a schedule *(product-specific)*
* **Send-Time Optimization (STO)**: An AI-driven feature that predicts the optimal time to send a message to each individual profile to maximise engagement *(product-specific)*
* **Custom action**: A journey activity that connects to a third-party system via API to send messages or retrieve data *(product-specific)*

**Guardrails:**
* Journey guardrails and limitations are detailed separately on the guardrails page and should be reviewed before designing at scale
* Custom actions require prior configuration by a technical user before they can be used in a journey
* Journey Fragments must be Active before they can be inserted into a journey

**Terminology:**
* Canonical name: Journey — Acronym: none — variants: customer journey, orchestration flow, multistep journey
* Synonyms: "journey designer" = "journey canvas" = "journey builder"
* Do not confuse: "built-in channel actions" ≠ "custom actions" — built-in actions use native AJO channels; custom actions call external third-party APIs

**FAQ:**
* **Q: What is the difference between real-time (unitary) delivery and batch delivery in journeys?** — Unitary delivery triggers a message for one profile at a time in real-time when an event occurs. Batch delivery processes all profiles in an audience at once or on a schedule using a Read Audience activity.
* **Q: Can I reuse common logic (like an eligibility check) across multiple journeys?** — Yes; save the nodes as a Journey Fragment and insert the Active fragment into any journey across the sandbox.
* **Q: Where do I go to create my first journey?** — Follow the step-by-step guide on the "Create your first journey" page, which walks through entry point selection, canvas design, testing, and publication.
* **Q: How do I send messages through a third-party system from a journey?** — Configure a custom action to call the external API, then add it as an action activity in the journey canvas.
* **Q: Where can I find answers to common journey questions?** — Visit the Journey FAQ page for answers covering concepts, building, testing, execution, monitoring, and best practices.

+++
