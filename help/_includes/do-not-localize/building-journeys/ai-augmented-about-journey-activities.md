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
* **Event activity**: An activity used to start a journey; when the event arrives, the journey triggers and each profile follows its defined steps *(product-specific)*
* **Orchestration activity**: An activity that helps determine the next step in the journey; examples include Optimize, Read Audience, and Wait *(product-specific)*
* **Action activity**: An activity representing what happens as a result of a trigger, such as sending a message *(product-specific)*
* **Custom action**: A specific action that can be created when using a third-party system to send messages *(product-specific)*
* **Alternative path**: A fallback branch added to an activity so the journey continues even when a timeout or error occurs *(product-specific)*

**Guardrails:**
* Before testing or publishing, the journey must be validated. Errors in the Alerts panel must be resolved and validation rerun before continuing.
* Most activities display advanced or technical parameters that cannot be modified; in some particular contexts, their values can be overridden using **[!UICONTROL Enable parameter override]**.

**Terminology:**
* Canonical name: journey activities. Categories: Event activities, Orchestration activities, Action activities.
* Do not confuse: "Orchestration activity" ≠ "Action activity" (orchestration helps determine the next step; actions represent what happens as a result of a trigger).

**FAQ:**
* **Q: What is the difference between event, orchestration, and action activities?** — Events trigger journey entry; orchestration activities help determine the next step; actions represent what happens as a result of a trigger, such as sending a message.
* **Q: What does a label add to an activity?** — The **[!UICONTROL Label]** adds a suffix to the name under the activity in the canvas, helping identify repeated activities and making debugging and reports easier to read.
* **Q: What happens when an error occurs in an action or condition activity?** — The profile's journey stops unless you check the "Add an alternative path in case of a timeout or an error" option on that activity.
* **Q: How can I send messages using a third-party system?** — Create a specific custom action when using a third-party system to send messages.
* **Q: When can I override an advanced parameter on an activity?** — In some particular contexts, click the **[!UICONTROL Enable parameter override]** icon to the right of the field to force a value.

+++

<!-- ai-section-version: 1 | source-hash: 25f2ba60 -->
