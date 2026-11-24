---
solution: Journey Optimizer
product: journey optimizer
title: Schedule an API triggered campaign
description: Learn how to schedule an API triggered campaign.
feature: Campaigns, API
topic: Content Management
role: Developer
level: Experienced
keywords: campaigns, API-triggered, REST, optimizer, messages
exl-id: e04b0d38-6b3d-4086-a0f0-c1b8f6d9634f
TQID: 'https://experienceleague.adobe.com/4cCtvRATLk-gNyMcY-jESte82DKpgVbhA75pE4fNKmQ'
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
---
# Schedule the API triggered campaign {#api-schedule}

>[!BEGINSHADEBOX]

**On this page:** Set start and end dates in the Schedule tab so your API triggered campaign sends at the right time.

>[!ENDSHADEBOX]

Use the **[!UICONTROL Schedule]** tab to define the campaign schedule.

## Set start and end dates

By default, API triggered campaigns start once they are triggered, and end as soon as the message has been sent once. If you do not want to execute your campaign right after it is triggered, you can specify a date and time at which the message should be sent using the **[!UICONTROL Campaign start]** option.

The **[!UICONTROL Campaign end]** option allows you to specify when a campaign should stop being executed. Outside of the specified dates, the campaign will not be executed.

![](assets/api-triggered-schedule.png)

>[!NOTE]
>
>When scheduling campaigns in [!DNL Adobe Journey Optimizer], ensure your start date/time aligns with the desired first delivery.

## Set rate control

>[!IMPORTANT]
>
>The **[!UICONTROL Throttle delivery]** option is not supported for API triggered campaigns, in standard or High throughput mode. A **[!UICONTROL Delivery rate]** entered in the **[!UICONTROL Delivery settings]** section is not applied. To limit the sending rate, pace your API calls upstream.

## Next steps {#next}

Once your campaign configuration and content are ready, you can review and activate it. [Learn more](../campaigns/review-activate-api-triggered-campaign.md)

{{$include /help/_includes/do-not-localize/campaigns/ai-augmented-api-triggered-campaign-schedule.md}}
