---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces actions and custom actions in Journey Optimizer, which let you deliver personalized real-time experiences and connect third-party systems through REST API calls.

**Intents:**

* Understand what actions and custom actions are and how they extend journeys
* Distinguish built-in message capability from third-party custom actions
* Identify when to use the Adobe Campaign v7/v8 integration versus a custom action
* Access the action list from the Configurations Actions area
* Learn who is responsible for configuring custom actions

**Glossary:**

* **Action**: A connection through which you deliver personalized, real-time experiences to customers, such as push notifications, email, SMS, or other digital engagement *(product-specific)*
* **Custom action**: A configured connection to a third-party system that sends messages or API calls, defined by technical users and made available to marketers *(product-specific)*
* **Built-in message capability**: The messaging capability that comes with Journey Optimizer, distinct from custom actions *(product-specific)*

**Guardrails:**

* The configuration of custom actions must be performed by a technical user.
* An action can be configured with any service from any provider that can be called through a REST API with a JSON-formatted payload.
* Once configured, custom actions appear in the left palette of your journey, in the Action category.

**Terminology:**

* Canonical name: Custom action — Acronym: n/a — variants: action, custom actions
* Do not confuse: "built-in message capability" (native Journey Optimizer messaging) ≠ "custom action" (third-party connection through a REST API)
* Do not confuse: "action" (the general connection concept) ≠ "custom action" (the configured third-party connection)

**FAQ:**

* **Q: What is a custom action?** — A configured connection of a third-party system to send messages or API calls, usable with any provider callable through a REST API with a JSON-formatted payload.
* **Q: Who must configure custom actions?** — The configuration of custom actions must be performed by a technical user.
* **Q: How do I connect Adobe Campaign v7 or v8?** — An integration is available upon request; refer to the Adobe Campaign v7/v8 integration page.
* **Q: Where do custom actions appear after configuration?** — In the left palette of your journey, in the Action category.
* **Q: Where is the action list found?** — Select Configurations in the ADMINISTRATION menu section, then click Manage in the Actions section.

+++

<!-- ai-section-version: 1 | source-hash: 420dfa1f -->
