---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces the three categories of journey activities — events, orchestration, and actions — and explains best practices for labeling, managing parameters, and handling errors in Adobe Journey Optimizer journeys.

**Intents:**
* Identify and distinguish between event, orchestration, and action activities in a journey
* Add labels and descriptions to journey activities for easier identification and reporting
* Configure an alternative path to handle timeouts or errors in a journey activity
* Override advanced parameters on a specific journey activity
* Combine multiple activity types to build cross-channel journey scenarios
* Troubleshoot activity configuration errors before publishing a journey

**Glossary:**
* **Event activity**: A journey activity triggered by an incoming event (e.g., purchase, audience qualification) that starts or advances a profile through the journey *(product-specific)*
* **Orchestration activity**: A journey activity (e.g., Optimize, Read Audience, Wait) that controls the flow and branching logic of a journey *(product-specific)*
* **Action activity**: A journey activity that delivers a communication or calls an external system as the result of a trigger *(product-specific)*
* **Custom action**: A user-configured action that connects Journey Optimizer to a third-party system for sending messages or data *(product-specific)*
* **Alternative path**: A fallback branch added to an activity so the journey continues even when a timeout or error occurs *(product-specific)*

**Guardrails:**
* Tests and publications cannot be performed if configuration errors are still detected in any activity
* Advanced/technical parameters on most activities are read-only and cannot be modified without using the parameter override feature

**Terminology:**
* Canonical name: Journey Activity — Acronym: none — variants: activity, node, step
* Synonyms: "action activity" = "channel action" = "message action"
* Do not confuse: "Orchestration activity" ≠ "Action activity" (orchestration controls flow; actions deliver communications)

**FAQ:**
* **Q: What is the difference between event, orchestration, and action activities?** — Event activities trigger journey entry or progression; orchestration activities control branching and flow logic; action activities deliver messages or call external systems.
* **Q: How do I add a label to a journey activity?** — Open the activity properties pane and fill in the Label field; the label appears as a suffix under the activity node on the canvas.
* **Q: What happens when an error occurs in an action or condition activity?** — The profile's journey stops unless you check the "Add an alternative path in case of a timeout or an error" option on that activity.
* **Q: Can I use Adobe Campaign to send messages from a journey?** — Yes, Journey Optimizer supports integration with Adobe Campaign v7/v8, Campaign Standard, and Marketo Engage for sending messages via custom action activities.
* **Q: How do I override a read-only advanced parameter on an activity?** — Click the "Enable parameter override" icon to the right of the parameter field to force a custom value.

+++
