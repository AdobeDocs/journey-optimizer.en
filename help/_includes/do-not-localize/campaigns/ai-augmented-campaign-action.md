---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the action of a campaign in the **Actions** tab: select a channel and a channel configuration, set optimization and multilingual content, add several inbound actions, and apply channel-specific settings.

**Intents:**

* Select a channel and a channel configuration for a campaign message
* Add up to 10 inbound actions in a single campaign
* Use channel optimization when selecting multiple outbound channels
* Run content experiments or use targeting rules from the **Optimization** section
* Add multilingual content, capping rules, engagement tracking, priority scores, or other channel-specific settings

**Glossary:**

* **Channel configuration**: Defined by a System Administrator; contains the technical parameters for sending the message, such as header parameters, subdomain, mobile apps. *(product-specific)*
* **Inbound channels**: Code-based experience, In-app message, Content Card, Web action.
* **Outbound channels**: Email, Push, Mobile (Mobile message).
* **Channel optimization**: Automatically selects the best channel for each customer at send time when multiple outbound channels (Email, Push, Mobile) are selected. *(product-specific)*
* **Rapid delivery mode**: A [!DNL Journey Optimizer] add-on that allows very fast push message sending in large volumes through campaigns. *(product-specific)*
* **Priority score**: A numeric value assigned to a campaign to prioritize an inbound campaign when there is an imposed constraint such as a frequency cap. *(product-specific)*

**Guardrails:**

* A single campaign can have up to 10 actions when inbound channels are selected (hard limit); this applies to inbound actions only.
* Adding several actions to one campaign is only available for inbound channels. For outbound channels (Email, Push, Mobile message), use channel optimization.
* Priority score: enter a numeric value from 0-100; the higher the number, the higher the priority. It applies to Web, In-app, and Code-based.
* Capping rules (**Business rules** drop-down list) apply to Email, Direct mail, Push, Mobile.
* **Action tracking** applies to Email and Mobile.
* Additional delivery rules apply to Content cards; **Edit triggers** applies to In-app.
* Once the campaign is live, all actions are activated simultaneously.

**Applicability:**

* Available channels vary based on the licensing model and add-ons.

**Terminology:**

* Canonical name: Campaign action
* Do not confuse: "inbound channels" (Code-based experience, In-app message, Content Card, Web action) ≠ "outbound channels" (Email, Push, Mobile)
* Do not confuse: "channel configuration" (technical parameters defined by a System Administrator) ≠ "channel" (the communication channel selected with **Add action**)

**FAQ:**

* **Q: How many actions can I add to one campaign?** — Up to 10 inbound actions. This is only available for inbound channels (Code-based experience, In-app message, Content Card, Web action).
* **Q: Can I add several Email actions to the same campaign?** — Adding several actions is only available for inbound channels. For outbound channels (Email, Push, Mobile message), use channel optimization.
* **Q: What is a priority score and which range can I enter?** — A numeric value from 0-100 that prioritizes an inbound campaign when there is an imposed constraint such as a frequency cap. The higher the number, the higher the priority.
* **Q: Who defines the channel configuration?** — A System Administrator.
* **Q: When are the actions of a multi-action campaign activated?** — All actions are activated simultaneously once the campaign is live.

**Examples:**

* Send a code-based experience to multiple endpoints with slightly different contents: create multiple code-based actions within the same campaign, each with a different endpoint configuration.
* Rapid delivery mode: send an urgent push alert, for example breaking news to users who have installed a news channel app, when delay in message delivery is business-critical.

**Related pages:**

* Channel configurations: Learn how to set up channel configurations (configuration/channel-surfaces.md)
* Channel optimization for outbound channels: Channel optimization (building-journeys/channel-optimization.md)
* Optimization options: Get started with content optimization (content-management/gs-message-optimization.md)
* Multilingual content: Get started with Multilingual content (content-management/multilingual-gs.md)
* Capping rules: Learn how to work with rule sets (conflict-prioritization/rule-sets.md)
* Priority scores: Learn how to assign priority scores to journeys & campaigns (conflict-prioritization/priority-scores.md)
* Rapid delivery mode for Push: Configure a push notification, Rapid delivery mode section (push/create-push.md#rapid-delivery)
* Campaign reports: Learn more about campaign reports (reports/campaign-global-report-cja.md)
* Content cards delivery rules: Learn how to create content cards (content-card/create-content-card.md)
* In-app triggers: Learn how to create an In-app message (in-app/create-in-app.md)
* Next step, content: Edit the Action campaign content (campaigns/campaign-content.md)

+++

<!-- ai-section-version: 1 | source-hash: 28547d42 -->
