---
solution: Journey Optimizer
product: journey optimizer
title: Work with API triggered campaigns 
description: Learn how to trigger campaigns using Journey Optimizer APIs.
feature: Campaigns, API
topic: Content Management
role: Developer
level: Experienced
keywords: campaigns, API-triggered, REST, optimizer, messages
exl-id: 0ef03d33-da11-43fa-8e10-8e4b80c90acb
---

# Work with API triggered campaigns {#trigger-campaigns}

>[!CONTEXTUALHELP]
>id="campaigns_overview_api_triggered"
>title="API triggered campaigns"
>abstract="**Transactional API triggered campaigns**<br/>Trigger real-time messages through API calls<br/><br/>**Marketing messages**<br/>Promotional content (requires opt-in, subject to business rules)<br/><br/>**Transactional messages**<br/>Service-related content (confirmation, alerts, not subject to marketing consent)<br/><br/>**Available channels**<br/>Email, SMS, Push notifications"

## About API triggered campaigns {#about}

API triggered campaigns allow either for marketing communications to reach out to an audience at the right time, or for transactional/operational messages to an individual like a password reset, where the need may involve personalization by not just using profile attribute but also the real-time context data in the trigger which is a REST API payload.

To do this, you first need to create an API triggered campaign in Journey Optimizer, and then launch its execution through an API call using the [Interactive Message Execution REST API](https://developer.adobe.com/journey-optimizer-apis/references/messaging/#tag/execution).

Available channels for API-triggered campaigns are Email, SMS and Push messages.

➡️ [Discover this feature in video](#video) 

## Key steps for API triggered campaigns creation {#steps}

1. [Define the campaign properties](api-triggered-campaign-properties.md)
1. [Configure the campaign action](api-triggered-campaign-action.md)
1. [Edit the campaign content](api-triggered-campaign-content.md)
1. [Define the campaign audience](api-triggered-campaign-audience.md)
1. [Schedule the campaign](api-triggered-campaign-schedule.md)
1. [Review & activate the campaign](review-activate-api-triggered-campaign.md)
1. [Trigger the campaign execution](trigger-campaigns.md)

>[!IMPORTANT]
>
>Before creating your campaign, make sure you have reviewed the general [campaign prerequisites](../campaigns/get-started-with-campaigns.md#prerequisites).

## How-to videos {#video}

Learn how to create a campaign and trigger it from an external system based on user interactions, using the Interactive Message Execution REST API.

>[!VIDEO](https://video.tv.adobe.com/v/3425358?quality=12)
