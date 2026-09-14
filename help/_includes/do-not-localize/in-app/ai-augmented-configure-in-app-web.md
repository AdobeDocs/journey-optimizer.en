---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the Web In-app channel in Adobe Experience Platform Data Collection by setting up the Web SDK extension, creating Sent data to platform and Manual trigger rules, and creating an In-app web channel configuration in Journey Optimizer.

**Intents:**

* Install and configure the Adobe Experience Platform Web SDK extension with the Personalization Storage option enabled
* Create a Sent data to platform rule using the Library Loaded (Page Top) event and a Send event action
* Create a Manual rule using a Click event and an Evaluate rulesets action
* Enable Render visual personalization decisions and define Decision Context Key/Value pairs
* Create an In-app web configuration from the Channels General settings menu
* Define an App configuration using a Page URL or a Pages matching rule

**Glossary:**

* **Adobe Experience Platform Web SDK extension**: The Tag extension that must be installed in your Tag properties to support Web In-app messaging *(product-specific)*
* **Personalization Storage**: A Web SDK extension option that stores event histories on the client, a prerequisite for implementing Frequency Rules in the Rules builder *(product-specific)*
* **Sent data to platform rule**: A rule configured with a Library Loaded (Page Top) event and a Send event action *(product-specific)*
* **Manual rule**: A rule configured with a Click event and an Evaluate rulesets action *(product-specific)*
* **Render visual personalization decisions**: An option enabled in the action configuration to deliver visual personalization *(product-specific)*
* **Decision Context**: The section where you define the Key and Value pairs that determine which experience to deliver *(product-specific)*
* **In-app web configuration**: A channel configuration created from Channels > General settings > Channel configurations to configure the In-app messaging channel *(product-specific)*
* **Pages matching rule**: An App configuration option that targets multiple URLs following the same pattern by defining Domain and Page criteria *(product-specific)*
* **Marketing action**: A selection that associates consent policies to the messages using the configuration to respect customer preferences *(product-specific)*

**Guardrails:**

* Ensure you are using the latest version of the Adobe Experience Platform Web SDK extension.
* The Personalization Storage option must be enabled; it is a prerequisite for implementing Frequency Rules in the Rules builder.
* Configuration names must begin with a letter (A-Z) and can only contain alpha-numeric characters, plus the underscore, dot, and hyphen characters.
* Marketing action(s) selected on the configuration apply all associated consent policies to messages using that configuration.
* From your Library, use Save & Build to development after adding your rule.

**Terminology:**

* Canonical name: In-app web configuration — Acronym: n/a — variants: Web In-app channel configuration, In-app web channel configuration
* Synonyms: "Sent data to platform rule" = "Sent data to platform trigger"
* Do not confuse: "Sent data to platform rule" (Library Loaded (Page Top) event with a Send event action) ≠ "Manual rule" (Click event with an Evaluate rulesets action)

**FAQ:**

* **Q: What must I install before configuring the Web In-app channel?** — The latest version of the Adobe Experience Platform Web SDK extension in your Tag properties, with the Personalization Storage option enabled.
* **Q: Why do I need to enable Personalization Storage?** — It stores event histories on the client, which is a prerequisite for implementing Frequency Rules in the Rules builder.
* **Q: What are the two trigger rule types I can configure?** — A Sent data to platform rule (Library Loaded (Page Top) event with a Send event action) and a Manual rule (Click event with an Evaluate rulesets action).
* **Q: How do I target multiple pages with one configuration?** — Use a Pages matching rule as the App configuration and define Domain and Page criteria instead of a single Page URL.
* **Q: What naming rules apply to a channel configuration?** — Names must begin with a letter (A-Z) and can only contain alpha-numeric characters plus underscore, dot, and hyphen.

+++

<!-- ai-section-version: 1 | source-hash: 84dc85c1 -->
