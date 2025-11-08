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
---

# Activate High throughput mode for API triggered campaigns {#high-throughput}

High Throughput mode is designed for organizations that need **very large-scale, real-time transactional messaging** (up to 5000 transactions per second). Unlike regular API triggered campaigns, High throughput campaigns operate independently of Adobe Profiles and require a different configuration model.  

This page explains how High throughput campaigns differ from standard API triggered campaigns, setup requirements, and when to choose each mode.  

## Guardrails & limitations

*  **Access** - Available only in the US region for organizations licensed with the High Throughput transactional messaging add-on.

* **Channels**: Currently available only for email.  

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
| **Throughput** | Up to 500 transactions per second | Up to 5000 transactions per second |
| **Channels** | Email, SMS, Push | Email |
| **Personalization** | Profile + contextual in the API payload | Contextual in the API payload only |
| **Profile & stitching** | Exists or gets created with events stitched to profile | No profile|
| **Message volume** | Standard entitlement & message packs | Separate tiered message volumes|
| **Infrastructure** | Standard | Enhanced |
| **Uptime** | 99,9% | 99,99%|
| **Health check API** | Yes | Yes |

In other words:

* Choose **Standard API triggered** campaigns if:  
  * You don't have High Throughput contracted.  
  * Your throughput needs are <500 TPS.  
  * You require personalization based on Adobe Profiles.  
  * You want campaign data stitched to profiles for future targeting.
  * You want to use another channel than Email.

* Choose **High throughput** campaigns if:  
  * You need throughput >500 TPS.  
  * You don't require profile stitching.  
  * You can pass all personalization in the API payload.  
  * You want to use the Email channel.  

## Setup guidelines

To configure High Throughput campaigns correctly, follow these guidelines: 

1. Create a new IP pool. [Learn how to create IP pools](../configuration/ip-pools.md)
1. Create a new channel configuration. [Learn how to set up channel configurations](../configuration/channel-surfaces.md)
1. Contact Adobe Customer Care to request the activated surface to be mapped to the High throughput capability. Provide the channel configuration and IP Pool details along with your organization ID.

>[!IMPORTANT]
>
>The IP pool and channel configurations designated for high-throughput transactional messages must be used exclusively for that purpose, and not be used with standard transactional messaging using API triggered campaigns or journeys.
