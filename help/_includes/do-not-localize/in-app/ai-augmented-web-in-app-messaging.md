---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure Web In-app Messaging support in the Web SDK, either through the Web SDK tag extension or directly with the Web SDK JavaScript library, using either automatic (Send data to Experience Platform) or manual triggers.

**Intents:**

* Meet the prerequisites for Web In-app Messaging, including the Web SDK tag extension version and CSP directive
* Configure Web In-app Messaging using the Web SDK tag extension for the Send data to Experience Platform trigger
* Configure Web In-app Messaging using the Web SDK tag extension for manual triggers
* Configure Web In-app Messaging directly from the Web SDK JavaScript library
* Control message display frequency through the personalization storage option

**Glossary:**

* **Web In-app message**: A notification sent to users within your web application to guide them to specific points of interest, such as promoting features, presenting offers, or facilitating onboarding *(product-specific)*
* **Enable personalization storage**: A Web SDK tag extension option that allows the Web SDK to track which experiences have been seen by the user across page loads *(product-specific)*
* **Send data to Experience Platform trigger**: A trigger type configured with a Send event action that automatically fetches personalization content *(product-specific)*
* **Manual trigger**: A trigger type configured with an Evaluate rulesets action to show messages after a specific user action *(product-specific)*
* **Render visual personalization decisions**: A Personalization option enabled on the action so visual personalization decisions are rendered *(product-specific)*
* **Decision context**: A section where you define the Key/Value pairs used in your campaign configuration to qualify for the in-app message *(product-specific)*
* **`personalizationStorageEnabled`**: A Web SDK configuration option controlling whether in-app messages appear with the frequency defined in your campaign or on every page load *(product-specific)*

**Guardrails:**

* The Web In-app messaging functionality requires the latest version of the Web SDK tag extension.
* When you configure Web In-App Messaging, you must include the `default-src blob:;` directive in your CSP.
* For the Send data to Experience Platform trigger, the rule uses Extension Core with Event Type Library Loaded (Page Top), and the action uses the Adobe Experience Platform Web SDK extension with Action Type Send event.
* For manual triggers, the rule uses Extension Core with Event Type Click (set on an element identified by a CSS selector), and the action uses Action Type Evaluate rulesets.
* `personalizationStorageEnabled: true` triggers the in-app message with the frequency defined in your campaign; `personalizationStorageEnabled: false` triggers the in-app message on every page load.

**Terminology:**

* Canonical name: Web In-app Messaging — Acronym: n/a — variants: Web In-app messaging, Web In-app message
* Synonyms: "Send data to Experience Platform trigger" = "automatic trigger (Method 1)"
* Do not confuse: "Web SDK tag extension" (configuration via tag rules and actions) ≠ "Web SDK JavaScript library" (configuration via `sendEvent`/`evaluateRulesets` commands)
* Do not confuse: "`sendEvent`" (Method 1: automatically fetch personalization content on page load) ≠ "`evaluateRulesets`" (Method 2: manually fetch based on user action)

**FAQ:**

* **Q: What are the prerequisites for Web In-app Messaging?** — The latest version of the Web SDK tag extension and a CSP that includes the `default-src blob:;` directive.
* **Q: What trigger types are supported?** — Sending data to Experience Platform and manually triggering the messages.
* **Q: How do I configure this without the tag extension?** — Use the Web SDK JavaScript library: `sendEvent` to automatically fetch personalization content on page load, or `evaluateRulesets` to fetch it after a specific user action.
* **Q: How do I control how often a message is shown?** — Use `personalizationStorageEnabled`: set to true to trigger with the frequency defined in your campaign, or false to trigger on every page load.
* **Q: What does Enable personalization storage do?** — It lets the Web SDK track which experiences have been seen by the user across page loads.

+++

<!-- ai-section-version: 1 | source-hash: f842b010 -->
