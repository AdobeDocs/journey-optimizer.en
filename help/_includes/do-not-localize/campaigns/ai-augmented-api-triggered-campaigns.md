---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces API triggered campaigns, which you create in Journey Optimizer and then launch through a call to the Interactive Message Execution REST API, and lists the key steps to create one.

**Intents:**

* Understand what an API triggered campaign is and when to use it
* Know the two kinds of messages an API triggered campaign can send, marketing and transactional
* Follow the ordered key steps to create and trigger an API triggered campaign
* Find which channels are available for API triggered campaigns

**Glossary:**

* **API triggered campaign**: A campaign that you first create in Journey Optimizer, then launch through an API call *(product-specific)*
* **Interactive Message Execution REST API**: The API used to launch the execution of an API triggered campaign *(product-specific)*
* **Trigger**: The REST API payload that carries real-time context data used for personalization

**Guardrails:**

* Available channels vary based on your licensing model and add-ons.

**Prerequisites and permissions:**

* The prerequisites listed in the Get started with campaigns page must be met before you start creating the campaign.

**Terminology:**

* Canonical name: API triggered campaign
* Acronym: AJO — Adobe Journey Optimizer

**FAQ:**

* **Q: What can an API triggered campaign send?** — Marketing communications to an audience at the right time, or transactional or operational messages to an individual, such as a password reset.
* **Q: What data can personalize an API triggered campaign message?** — Profile attributes and real-time context data in the trigger, which is a REST API payload.
* **Q: How do I launch an API triggered campaign?** — Create the campaign in Journey Optimizer, then launch its execution through an API call using the Interactive Message Execution REST API.
* **Q: Which channels are available?** — Available channels vary based on your licensing model and add-ons.
* **Q: What are the steps to create an API triggered campaign?** — Define the campaign properties, configure the campaign action, edit the campaign content, define the campaign audience, schedule the campaign, review and activate the campaign, then trigger the campaign execution.

**Examples:**

* A customer wants to reset a password: a transactional API triggered campaign sends the message to that individual, personalized with real-time context data in the trigger.

**Related pages:**

* Define the campaign properties, first creation step: Define the campaign properties (campaigns/api-triggered-campaign-properties.md)
* Configure the campaign action: Configure the campaign action (campaigns/api-triggered-campaign-action.md)
* Edit the campaign content: Edit the campaign content (campaigns/api-triggered-campaign-content.md)
* Define the campaign audience: Define the campaign audience (campaigns/api-triggered-campaign-audience.md)
* Schedule the campaign: Schedule the campaign (campaigns/api-triggered-campaign-schedule.md)
* Review and activate the campaign: Review & activate the campaign (campaigns/review-activate-api-triggered-campaign.md)
* Trigger the campaign execution: Trigger the campaign execution (campaigns/trigger-campaigns.md)
* Prerequisites before starting with campaigns: in this section (campaigns/get-started-with-campaigns.md#prerequisites)
* Complete campaign creation workflow with type-specific guides: complete campaign creation workflow with type-specific guides (campaigns/get-started-with-campaigns.md#workflow)
* Supported channels: Channels in journeys & campaigns (channels/gs-channels.md#channels)

+++

<!-- ai-section-version: 1 | source-hash: ecb05f59 -->
