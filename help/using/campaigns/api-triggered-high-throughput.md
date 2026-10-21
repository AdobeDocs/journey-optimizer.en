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
TQID: 'https://experienceleague.adobe.com/SwmK1epuhZUf4EWnaLRHTBH-eE1hEV02Z8nqXGtMb6U'
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: a653cc2e-bc85-4353-a306-399e5b247978
    internal-label: Journey Optimizer campaigns
  - id: 629f438c-ea49-5ade-aa39-c2a256ff3036
    internal-label: API
subfeature_v2:
  - id: f7479fa1-474b-479d-8c98-f6cee5865a38
    internal-label: API triggered campaigns
  - id: ee67bd4a-25ee-4cdd-9eab-0d7549fde0c6
    internal-label: Campaign management
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: d378ca77-2da1-4f39-ad92-1917fe974a38
    internal-label: Experienced
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Activate High throughput mode for API triggered campaigns {#high-throughput}

>[!BEGINSHADEBOX]

**On this page:** Activate High throughput mode for API triggered campaigns so you can send very large-scale, real-time transactional messages (email and push) at up to 5000 transactions per second without relying on profiles.

>[!ENDSHADEBOX]

High Throughput mode is designed for organizations that need **very large-scale, real-time transactional messaging** (up to 5000 transactions per second). Unlike regular API triggered campaigns, High throughput campaigns operate independently of Adobe Profiles and require a different configuration model.  

This page explains how High throughput campaigns differ from standard API triggered campaigns, setup requirements, and when to choose each mode.  

## Guardrails & limitations {#guardrails}

* **Access** - Available across all regions except Switzerland for organizations licensed with the High Throughput transactional messaging add-on.

* **Channels**: Email and push notifications.

* **Personalization**:  

  * All personalization must be included in the API payload as **contextual data**. [Learn how to personalize content using contextual data](../campaigns/api-triggered-campaign-content.md#contextual) 
  * Profile-based personalization is not supported. If profile variables are used, validation errors will occur.  

* **High throughput channel configurations** - High throughput email channel configurations do not support contextual or profile-based personalization, and there is no personalization editor for the configuration. This is stricter than the campaign-level rule above: a campaign can receive contextual attributes in the API payload, but the channel configuration itself cannot be personalized. Channel configurations that use [profile-based personalization](../email/surface-personalization.md) cannot be used with high throughput campaigns.

* **Unsupported features** - [Message Export](../configuration/message-export.md), dynamic subdomains, and conversion of an existing standard IP pool or channel configuration to high throughput are not supported for high throughput.

* **API endpoint** - High Throughput campaigns use a different endpoint than standard API triggered campaigns. For details, see [Execute an API triggered campaign](../campaigns/trigger-campaigns.md#trigger).

* **Campaign exclusivity** - High throughput campaigns do not use Adobe Profiles. Messages are delivered whether or not a profile exists.

  Moreover, a campaign cannot be used for both profile-enabled and non-profile use cases. If you need both, create two separate campaigns, and ensure the calling system decides which one to trigger based on the context.

* **Datasets for feedback and tracking** -  Feedback and tracking data for high throughput campaigns are stored in dedicated datasets that are not enabled for profiles. As a result, these events are not stitched to profiles, even if a matching profile exists.

  The datasets used are: 

  * **AJO Message Feedback Event Dataset - Non Profile** — used for both email and push feedback.
  * **AJO Email Tracking Experience Event Dataset - Non Profile** — used for email tracking only. A dedicated non-profile tracking dataset for push is not yet available.

* **Throughput allocation** - The throughput provisioned under the High Throughput add-on is exclusively reserved for high throughput campaigns. There is no sharing of throughput between standard and high throughput API triggered campaigns.

* **Personalized PDF attachments** - Not supported when High throughput traffic is routed through the secondary region. [Learn more about personalized PDF attachments](../email/pdf-attachments.md#personalized-attachments)
* **Push notifications**:

  * **Web push** — High Throughput web push campaigns run on shared infrastructure and do not benefit from the dedicated capacity reserved for High Throughput mobile push.
  * **Payload size** — The maximum payload size is 5 KB.
  * **Denylist behavior** — When a message hits a denylist, delivery feedback is retained but no profile-update feedback is produced. This means denylist responses do not trigger profile updates or token invalidation in Adobe Experience Platform.

## Choosing between standard vs. High throughput campaigns

Use this table to decide which API triggered campaign type fits your use case:  

| Feature / Requirement | Standard API triggered Campaign | High Throughput Campaign |
| ------------------------ | --------------------------------- | --------------------------- |
| **Availability** | Included in base offering | Requires High Throughput transactional messaging add-on. |
| **Throughput** | Up to 500 transactions per second | Up to 5000 transactions per second |
| **Channels** | Email, Mobile message, Push | Email, Push |
| **Personalization** | Profile + contextual in the API payload | Contextual in the API payload only |
| **Profile & stitching** | Exists or gets created with events stitched to profile | No profile |
| **Message volume** | Standard entitlement & message packs | Separate tiered message volumes |
| **Infrastructure** | Standard | Enhanced |
| **Uptime** | 99,9% | 99,99% |
| **Health check API** | Yes | Yes |

In other words:

* Choose **Standard API triggered** campaigns if:  
  * You don't have High Throughput contracted.  
  * Your throughput needs are <500 TPS.  
  * You require personalization based on Adobe Profiles.  
  * You want campaign data stitched to profiles for future targeting.
  * You want to use another channel than Email or Push.

* Choose **High throughput** campaigns if:  
  * You need throughput >500 TPS.  
  * You don't require profile stitching.  
  * You can pass all personalization in the API payload.  
  * You want to use the Email or Push channel.

## Setup guidelines {#setup-guidelines}

To configure High Throughput campaigns correctly, follow these guidelines:

1. **One-time activation** - After purchasing the High Throughput transactional messaging add-on, contact Adobe Customer Care or your Adobe representative so that the required backend activation and one-time setup can be completed. This is not required for every campaign or channel configuration.
1. **Create a dedicated High Throughput IP pool** - When you create the IP pool, enable the High Throughput option. [Learn how to create IP pools](../configuration/ip-pools.md)
1. **Create a High Throughput email channel configuration** - Enable the High Throughput toggle and select the High Throughput IP pool you created. Only High Throughput IP pools are listed. [Learn how to set up channel configurations](../configuration/channel-surfaces.md)
1. **Use the configuration in High Throughput campaigns only** - When you create a High Throughput API triggered campaign, only High Throughput channel configurations are available for selection.

>[!IMPORTANT]
>
>The IP pool and channel configurations designated for high-throughput transactional messages must be used exclusively for that purpose, and not be used with standard transactional messaging using API triggered campaigns or journeys.

>[!CAUTION]
>
>The type of an IP pool or channel configuration cannot be changed after creation. A standard resource cannot be converted to High Throughput, and a High Throughput resource cannot be converted back to standard.

### Matching resources {#matching-resources}

High Throughput resources must be used together:

* A High Throughput campaign can only use a High Throughput channel configuration.
* A High Throughput channel configuration can only use a High Throughput IP pool.
* Standard and High Throughput resources cannot be mixed. Standard campaigns and configurations are not available in the High Throughput drop-down lists, and vice versa.

>[!NOTE]
>
>The High Throughput IP pool and channel configuration flow described above applies to the email channel. For push, setup remains a manual process: contact Adobe Customer Care.

## High availability {#high-availability}

To maintain high availability, High Throughput uses a secondary region. When you purchase the High Throughput add-on, a secondary setup is provisioned automatically alongside your primary resources, and part of your High Throughput traffic is routed through the secondary region.
