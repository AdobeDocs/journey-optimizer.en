---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure a Channel configuration for Orchestrated campaigns by setting the delivery method, target dimension, and execution address, and how to add URL tracking parameters to tracked links.

**Intents:**

* Enable a Channel configuration for compatibility with Orchestrated campaigns.
* Choose a delivery method between Target Dimension and Target + Secondary Dimension.
* Select a previously created Target Dimension and, when applicable, a Secondary Dimension.
* Choose the source used to fetch the delivery address (Profile, Target Dimension, or Secondary Dimension) and select the specific delivery address field.
* Add URL tracking parameters using orchestrated campaign contextual attributes.

**Glossary:**

* **Channel configuration**: the configuration that defines how and to whom messages are delivered, including delivery level and execution address *(product-specific)*
* **Execution details**: the section of a Channel configuration where delivery method, target dimension, and execution address are set *(product-specific)*
* **Target Dimension**: delivery method that sends to the primary entity, e.g., recipient *(product-specific)*
* **Target + Secondary Dimension**: delivery method that sends using both primary and secondary entities, e.g., recipient + contract, or recipient + flights *(product-specific)*
* **Secondary Dimension**: the linked table selected to support multi-entity Orchestrated campaigns, where one profile can receive several messages, one per qualifying row *(product-specific)*
* **Execution Address**: the section where the Source used to fetch the delivery address (email address or phone number) is chosen *(product-specific)*
* **Delivery address**: the specific field selected to use for message delivery, chosen via the edit icon in the Delivery address field *(product-specific)*

**Guardrails:**

* The schema used for the secondary dimension must have a primary key; composite primary keys are not supported for secondary dimensions.

**Terminology:**

* Canonical name: Channel configuration — variants: Channel Configuration
* Do not confuse: "Target Dimension" (send to the primary entity, e.g., recipient) ≠ "Target + Secondary Dimension" (send using both primary and secondary entities, supporting one message per qualifying row in the linked Secondary Dimension table)
* Do not confuse: "Execution Address" (the section where the Source for the delivery address is chosen) ≠ "Delivery address" (the specific field selected for message delivery)

**FAQ:**

* **Q: What must be enabled before a Channel configuration can be used with Orchestrated campaigns?** — Enabled must be clicked in the Orchestrated campaigns tab of the Execution details section.
* **Q: What are the two delivery methods available?** — Target Dimension (primary entity only) and Target + Secondary Dimension (primary and secondary entities).
* **Q: Where can the execution address be sourced from?** — From Profile, Target Dimension, or Secondary Dimension, depending on where the delivery address is stored.
* **Q: Are composite primary keys supported for secondary dimensions?** — No, the schema used for the secondary dimension must have a primary key, and composite primary keys are not supported.
* **Q: How are URL tracking parameters defined for Orchestrated campaigns?** — Using contextual attributes with the `{{context.system.source.*}}` syntax, such as `context.system.source.id` or `context.system.source.actionName`.

**Examples:**

* URL tracking parameter example for Orchestrated campaigns: `www.YourLandingURL.com?utm_source=AJO&utm_campaign={{context.system.source.id}}&utm_content={{context.system.source.actionName}}`

**Related pages:**

* For creating and configuring the Channel configuration: Follow the steps detailed in this page (email/surface-personalization.md)
* For selecting a previously created Target Dimension: previously created Target Dimension (orchestrated/target-dimension.md)
* For learning more about URL tracking parameters: this section (email/url-tracking.md)

**Personas:**

* **admin:** Can enable a Channel configuration for Orchestrated campaigns by selecting Enabled, then choose Target Dimension or Target + Secondary Dimension as the delivery method. Can select the Source for the execution address from Profile, Target Dimension, or Secondary Dimension, then select the specific Delivery address field. The page states that the schema used for the secondary dimension must have a primary key, and composite primary keys are not supported. Where: "Configure your Channel configuration".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Create and configure your Channel configuration.
* **Success check:** Your channel is ready to use with Orchestrated campaigns, and messages are delivered according to the selected target dimension.
* **Previous:** After setting up your Target Dimension: Create your Targeting dimension (orchestrated/target-dimension.md); To create and configure your Channel configuration: Personalize email configuration settings (email/surface-personalization.md)
* **Next:** To learn more about URL tracking parameters: Configure URL tracking (email/url-tracking.md)

+++

<!-- ai-section-version: 1 | source-hash: a6c918cc -->
