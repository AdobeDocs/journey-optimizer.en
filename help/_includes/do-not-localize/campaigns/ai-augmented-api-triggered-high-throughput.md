---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how High throughput mode for API triggered campaigns differs from standard API triggered campaigns, its guardrails and setup requirements, and when to choose each mode for very large-scale, real-time transactional messages (email and push) without relying on profiles.

**Intents:**

* Decide between a standard API triggered campaign and a High throughput campaign
* Know the guardrails and limitations of High throughput campaigns
* Set up a channel configuration and an IP pool for High throughput campaigns
* Know how to personalize a High throughput campaign (contextual data only)
* Know which datasets store feedback and tracking data for High throughput campaigns

**Glossary:**

* **High throughput mode** (also written High Throughput): A mode of API triggered campaigns designed for very large-scale, real-time transactional messaging, which operates independently of Adobe Profiles *(product-specific)*
* **Standard API triggered campaign**: An API triggered campaign that is not in High throughput mode
* **High Throughput transactional messaging add-on**: The add-on that organizations must be licensed with to use High throughput campaigns *(product-specific)*
* **Contextual data**: Personalization data passed in the API payload
* **AJO Message Feedback Event Dataset - Non Profile**: Dataset used for both email and push feedback of High throughput campaigns
* **AJO Email Tracking Experience Event Dataset - Non Profile**: Dataset used for email tracking only of High throughput campaigns

**Guardrails:**

* Throughput: High throughput campaigns support up to 5000 transactions per second; standard API triggered campaigns support up to 500 transactions per second.
* Channels: Email and push notifications for High throughput campaigns.
* Personalization: all personalization must be included in the API payload as contextual data. Profile-based personalization is not supported, and validation errors occur if profile variables are used.
* Channel configurations that use profile-based personalization cannot be used with High throughput campaigns. Only surfaces without profile personalization can be used.
* High throughput campaigns use a different API endpoint than standard API triggered campaigns.
* High throughput campaigns do not use Adobe Profiles. Messages are delivered whether or not a profile exists.
* A campaign cannot be used for both profile-enabled and non-profile use cases. If you need both, create two separate campaigns, and make the calling system decide which one to trigger based on the context.
* Feedback and tracking data for High throughput campaigns are stored in dedicated datasets that are not enabled for profiles, so these events are not stitched to profiles, even if a matching profile exists. A dedicated non-profile tracking dataset for push is not yet available.
* The throughput provisioned under the High Throughput add-on is exclusively reserved for High throughput campaigns. There is no sharing of throughput between standard and High throughput API triggered campaigns.
* Personalized PDF attachments are not supported when a High throughput campaign fails over to another region.
* Web push: High Throughput web push campaigns run on shared infrastructure and do not benefit from the dedicated capacity reserved for High Throughput mobile push.
* Push payload size: the maximum payload size is 5 KB (hard limit).
* Denylist behavior for push: when a message hits a denylist, delivery feedback is retained but no profile-update feedback is produced, so denylist responses do not trigger profile updates or token invalidation in Adobe Experience Platform.
* The IP pool and channel configurations designated for High throughput transactional messages must be used exclusively for that purpose, and not be used with standard transactional messaging using API triggered campaigns or journeys.

**Prerequisites and permissions:**

* The organization must be licensed with the High Throughput transactional messaging add-on.
* A new IP pool.
* A new channel configuration.
* A request to Adobe Customer Care to map the activated surface to the High throughput capability, with the channel configuration and IP Pool details and your organization ID.

**Applicability:**

* Access: available across all regions except Switzerland.
* Applies to API triggered campaigns, in High throughput mode.

**Terminology:**

* Canonical name: High throughput mode — variants: High Throughput mode, High throughput campaigns
* Acronym: TPS — transactions per second (used on the page body)
* Do not confuse: "Standard API triggered campaign" (included in the base offering, standard entitlement and message packs, standard infrastructure, uptime 99,9%) ≠ "High throughput campaign" (requires the High Throughput transactional messaging add-on, separate tiered message volumes, enhanced infrastructure, uptime 99,99%); both have a health check API

**FAQ:**

* **Q: When should I choose a standard API triggered campaign?** — When you do not have High Throughput contracted, your throughput needs are under 500 TPS, you require personalization based on Adobe Profiles, you want campaign data stitched to profiles for future targeting, or you want to use another channel than Email or Push.
* **Q: When should I choose a High throughput campaign?** — When you need throughput over 500 TPS, you do not require profile stitching, you can pass all personalization in the API payload, and you want to use the Email or Push channel.
* **Q: Can a High throughput campaign use profile attributes for personalization?** — No. Profile-based personalization is not supported, and validation errors occur if profile variables are used. Pass all personalization as contextual data in the API payload.
* **Q: Can one campaign serve both profile-enabled and non-profile use cases?** — No. Create two separate campaigns, and make the calling system decide which one to trigger.
* **Q: Is throughput shared between standard and High throughput campaigns?** — No. The throughput provisioned under the High Throughput add-on is exclusively reserved for High throughput campaigns.
* **Q: How do I set up High throughput campaigns?** — Create a new IP pool, create a new channel configuration, then contact Adobe Customer Care to request that the activated surface be mapped to the High throughput capability.

**Related pages:**

* Personalizing content with contextual data: Learn how to personalize content using contextual data (campaigns/api-triggered-campaign-content.md#contextual)
* Endpoint used by High throughput campaigns: Execute an API triggered campaign (campaigns/trigger-campaigns.md#trigger)
* Channel configurations with profile-based personalization: profile-based personalization (email/surface-personalization.md)
* Personalized PDF attachments: Learn more about personalized PDF attachments (email/pdf-attachments.md#personalized-attachments)
* Create IP pools: Learn how to create IP pools (configuration/ip-pools.md)
* Set up channel configurations: Learn how to set up channel configurations (configuration/channel-surfaces.md)

+++

<!-- ai-section-version: 1 | source-hash: 4cda4ed0 | related: campaigns/api-triggered-campaign-content.md -->
