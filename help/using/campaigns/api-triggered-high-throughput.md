The file doesn't exist in the pipeline repo — it's a documentation file provided as context. I'll write the complete updated markdown directly as instructed (output only the file, no explanations).

---

solution: Journey Optimizer
product: journey optimizer
title: Activate High throughput mode for API triggered campaigns
description: Learn how to activate the High throughput mode for API triggered campaigns.
feature: Campaigns, API
topic: Content Management
role: Developer
level: Experienced
keywords: campaigns, API-triggered, REST, optimizer, messages
exl-id: 2b3e87dc-097a-4d05-873c-f421d11338c3
TQID: https://experienceleague.adobe.com/SwmK1epuhZUf4EWnaLRHTBH-eE1hEV02Z8nqXGtMb6U
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: a653cc2e-bc85-4353-a306-399e5b247978
    internal-label: Journey Optimizer campaigns
subfeature_v2:
  - id: f7479fa1-474b-479d-8c98-f6cee5865a38
    internal-label: API triggered campaigns
  - id: ee67bd4a-25ee-4cdd-9eab-0d7549fde0c6
    internal-label: Campaign management
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Activate High throughput mode for API triggered campaigns {#high-throughput}

>[!BEGINSHADEBOX]

**On this page:** Activate High throughput mode for API triggered campaigns so you can send very large-scale, real-time transactional messaging at up to 5000 transactions per second (email) or up to 1500 transactions per second (push) without relying on profiles.

>[!ENDSHADEBOX]

High Throughput mode is designed for organizations that need **very large-scale, real-time transactional messaging**. Unlike regular API triggered campaigns, High throughput campaigns operate independently of Adobe Profiles and require a different configuration model.

This page explains how High throughput campaigns differ from standard API triggered campaigns, setup requirements, and when to choose each mode.

## Guardrails & limitations

*  **Access** - Available only in the US region for organizations licensed with the High Throughput transactional messaging add-on.

* **Channels**: Available for email and push notifications.

* **Throughput**:

  * **Email** - Up to 5000 transactions per second.
  * **Push** - Up to 1500 transactions per second. The following tiered throughput levels are available: 500 TPS (base), 1000 TPS, and 1500 TPS. Higher tiers require the appropriate add-on entitlement.

* **Personalization**:

  * All personalization must be included in the API payload as **contextual data**. [Learn how to personalize content using contextual data](../campaigns/api-triggered-campaign-content.md#contextual)
  * Profile-based personalization is not supported. If profile variables are used, validation errors will occur.

* **Personalized channel configurations** - Channel configurations that use [profile-based personalization](../email/surface-personalization.md) cannot be used with high throughput campaigns. Only surfaces without profile personalization can be used.

* **API endpoint** - High Throughput campaigns use a different endpoint than standard API triggered campaigns. For details, see [Execute an API triggered campaign](../campaigns/trigger-campaigns.md#trigger).

* **Campaign exclusivity** - High throughput campaigns do not use Adobe Profiles. Messages are delivered whether or not a profile exists.

  Moreover, a campaign cannot be used for both profile-enabled and non-profile use cases. If you need both, create two separate campaigns, and ensure the calling system decides which one to trigger based on the context.

* **Datasets for feedback and tracking** -  Feedback and tracking data for high throughput campaigns are stored in dedicated datasets that are not enabled for profiles. As a result, these events are not stitched to profiles, even if a matching profile exists.

  The datasets used are:

  * **AJO Message Feedback Event Dataset - Non Profile**
  * **AJO Email Tracking Experience Event Dataset - Non Profile**

* **Throughput allocation** - The throughput provisioned under the High Throughput add-on is exclusively reserved for high throughput campaigns. There is no sharing of throughput between standard and high throughput API triggered campaigns.

## Choosing between standard vs. High throughput campaigns

Use this table to decide which API triggered campaign type fits your use case:

| Feature / Requirement | Standard API triggered Campaign | High Throughput Campaign |
|------------------------|---------------------------------|---------------------------|
| **Availability** | Included in base offering | Requires High Throughput transactional messaging add-on. |
| **Throughput** | Up to 500 transactions per second | Up to 5000 TPS (email); up to 1500 TPS (push) |
| **Channels** | Email, SMS, Push | Email, Push |
| **Personalization** | Profile + contextual in the API payload | Contextual in the API payload only |
| **Profile & stitching** | Exists or gets created with events stitched to profile | No profile|
| **Message volume** | Standard entitlement & message packs | Separate tiered message volumes|
| **Infrastructure** | Standard | Enhanced |
| **Uptime** | 99,9% | 99,99%|
| **Health check API** | Yes | Yes |

In other words:

* Choose **Standard API triggered** campaigns if:
  * You don't have High Throughput contracted.
  * Your throughput needs are ≤500 TPS.
  * You require personalization based on Adobe Profiles.
  * You want campaign data stitched to profiles for future targeting.
  * You need SMS messaging.

* Choose **High throughput** campaigns if:
  * You need throughput >500 TPS.
  * You don't require profile stitching.
  * You can pass all personalization in the API payload.
  * You want to use the Email or Push channel.

## Setup guidelines

To configure High Throughput campaigns correctly, follow these guidelines:

1. **For email high throughput only** - Create a new IP pool. [Learn how to create IP pools](../configuration/ip-pools.md)
1. Create a new channel configuration. [Learn how to set up channel configurations](../configuration/channel-surfaces.md)
1. Contact Adobe Customer Care to request the activated surface to be mapped to the High throughput capability. Provide the channel configuration and IP Pool details (for email) along with your organization ID.

>[!IMPORTANT]
>
>The channel configurations designated for high-throughput transactional messages must be used exclusively for that purpose, and not be used with standard transactional messaging using API triggered campaigns or journeys. For email high throughput, the IP pool designated for this purpose must also be used exclusively for high-throughput sending.