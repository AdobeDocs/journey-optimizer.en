---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to choose the channel and the channel configuration of an API triggered campaign in the **Actions** tab, and how to set optimization, multilingual, capping, tracking, and Rapid delivery mode options.

**Intents:**

* Add an action to an API triggered campaign and choose its communication channel
* Select a channel configuration for the message
* Use the **Message Optimization** section for content experiments, targeting rules, or both
* Add multilingual content with the **Languages** section
* Apply capping rules, track engagement, or enable Rapid delivery mode, depending on the channel

**Glossary:**

* **Channel configuration**: Defined by a System Administrator; contains the technical parameters for sending the message, such as header parameters, subdomain, mobile apps *(product-specific)*
* **Business rules**: Drop-down list in which you select a rule set to apply capping rules to the campaign
* **Capping rules**: Frequency capping by communication type, applied through a rule set, to prevent overloading customers with similar messages
* **Action tracking**: Section used to track how recipients react to email or mobile deliveries; results are accessible from the campaign report once the campaign has been executed
* **Rapid delivery mode**: A [!DNL Journey Optimizer] add-on that allows very fast push message sending in large volumes through campaigns *(product-specific)*

**Guardrails:**

* Available channels vary based on your licensing model and add-ons.

**Prerequisites and permissions:**

* A channel configuration, defined by a System Administrator

**Applicability:**

* Capping rules (**Business rules**): Email, Push, Mobile
* Track engagement (**Action tracking**): Email, Mobile
* Rapid delivery mode: Push
* High Throughput API triggered campaigns: email channel only

**Terminology:**

* Canonical name: API triggered campaign action
* Do not confuse: "channel" (the communication channel selected with **Add action**) ≠ "channel configuration" (the technical parameters defined by a System Administrator)

**FAQ:**

* **Q: How do I choose the channel of an API triggered campaign?** — In the **Actions** tab, click **Add action** and select the communication channel.
* **Q: Which channels can I use?** — Available channels vary based on your licensing model and add-ons. High Throughput API triggered campaigns currently support the email channel only.
* **Q: Who defines the channel configuration?** — A System Administrator defines it.
* **Q: Which channels support capping rules and engagement tracking?** — Capping rules apply to Email, Push, and Mobile. Tracking applies to Email and Mobile.
* **Q: Which channel supports Rapid delivery mode?** — Push.

**Examples:**

* Rapid delivery mode is used when delay in message delivery is business-critical, for example an urgent push alert such as breaking news sent to users who have installed a news channel app.

**Related pages:**

* Supported channels: Channels in journeys & campaigns (channels/gs-channels.md)
* Setting up channel configurations: Learn how to set up channel configurations (configuration/channel-surfaces.md)
* Content experiments and targeting rules: Optimization in campaigns (content-management/gs-message-optimization.md)
* Multilingual content: Get started with multilingual content (content-management/multilingual-gs.md)
* Rule sets for capping: Learn how to work with rule sets (conflict-prioritization/rule-sets.md)
* Campaign reports: Learn more about campaign reports (reports/campaign-global-report-cja.md)
* Enabling Rapid delivery mode for push notifications: on this page (push/create-push.md#rapid-delivery)
* Next step, designing the content: Learn more (campaigns/api-triggered-campaign-content.md)

+++

<!-- ai-section-version: 1 | source-hash: 48b9be61 -->
