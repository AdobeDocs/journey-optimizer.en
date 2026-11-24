---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to schedule an API triggered campaign with start and end dates in the **Schedule** tab, and states that the **Throttle delivery** option is not supported for API triggered campaigns.

**Intents:**

* Understand when an API triggered campaign starts and ends by default
* Set a start date and time with **Campaign start**
* Set an end date and time with **Campaign end**
* Understand that **Throttle delivery** is not supported for API triggered campaigns
* Understand that the sending rate is limited by pacing API calls upstream

**Glossary:**

* **Campaign start**: Option to specify a date and time at which the message is sent
* **Campaign end**: Option to specify when a campaign stops being executed
* **Throttle delivery**: Option in the **Delivery settings** section that sets a delivery rate per second. It is not supported for API triggered campaigns.
* **Delivery rate**: The number of messages per second entered with **Throttle delivery**. For an API triggered campaign, the value is not applied.

**Guardrails:**

* By default, API triggered campaigns start once they are triggered, and end as soon as the message has been sent once.
* Outside of the specified dates, the campaign is not executed.
* **Throttle delivery** is not supported for API triggered campaigns, in standard or High throughput mode: a delivery rate entered in **Delivery settings** is not applied.
* To limit the sending rate, pace the API calls upstream.

**Applicability:**

* Throttle delivery: not supported for API triggered campaigns (standard and High throughput modes).

**Terminology:**

* Canonical name: API triggered campaign schedule
* Do not confuse: **Campaign start** (when the message is sent) ≠ **Campaign end** (when the campaign stops being executed)

**FAQ:**

* **Q: When does an API triggered campaign start by default?** — Once it is triggered. It ends as soon as the message has been sent once.
* **Q: How do I send the message at a specific time?** — Use the **Campaign start** option to specify a date and time.
* **Q: Can I limit the delivery rate of an API triggered campaign with Throttle delivery?** — No. The option is not supported for API triggered campaigns, in standard or High throughput mode. Pace the API calls upstream.
* **Q: What happens if I enter a Delivery rate in an API triggered campaign?** — The value is not applied.

**Related pages:**

* Next step, review and activation: Learn more (campaigns/review-activate-api-triggered-campaign.md)

**Personas:**

* **developer:** Cannot use Throttle delivery to limit the delivery rate of an API triggered campaign, because the option is not supported. Paces the API calls upstream to limit the sending rate. Where: "Set rate control".

**Onboarding:**

* **Level:** Experienced
* **First minimal step:** Set the Campaign start and Campaign end options in the Schedule tab, and pace the API calls upstream if you need to limit the sending rate.
* **Success check:** The campaign runs within the dates you specified.
* **Next:** When your campaign configuration and content are ready: Review & activate the API triggered campaign (campaigns/review-activate-api-triggered-campaign.md)

+++

<!-- ai-section-version: 1 | source-hash: d0f88a1a -->
