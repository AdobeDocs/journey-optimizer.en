---
solution: Journey Optimizer
product: journey optimizer
title: Use the Wait activity in Orchestrated campaigns
description: Learn how to use the Wait activity in Orchestrated campaigns
exl-id: 11ef095b-77ec-4e2e-ab4d-49a248354f08
version: Campaign Orchestration
TQID: https://experienceleague.adobe.com/-AI0PuvH2o43jG3d6cpP9-IwD6LxL37nzFv19R-wkcQ
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: b423a773-0a58-4a77-b65d-3dd4ae6ef841
    internal-label: Campaign Orchestration (AJO)
subfeature_v2:
  - id: b5e335a9-0e5f-4dda-8845-c4ac5dca2be4
    internal-label: Orchestration activities
---
# Wait {#wait}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_wait"
>title="Wait activity"
>abstract="The **Wait** activity is used to delay the transition from an activity to another."

The **[!UICONTROL Wait]** activity is a **[!UICONTROL Flow control]** component used to introduce a delay between two activities in an Orchestrated campaign. This helps ensure your follow-up activities are better timed and more relevant to user engagement.

For example, you can wait a few days after an email delivery to track opens and clicks before sending a follow-up message. 

## Configuration{#wait-configuration}

>[!IMPORTANT]
>
>Data in temporary tables does not persist beyond **5 days**. When you use **[!UICONTROL Duration]** or **[!UICONTROL Fixed time]** waits, ensure the elapsed time until the next activity completes within that limit so intermediate data remains available.

Follow these steps to configure the **[!UICONTROL Wait]** activity:

1. Add a **[!UICONTROL Wait]** activity into your Orchestrated campaign.

1. Select the Wait type that best fits your needs:

    * **[!UICONTROL Duration]**: Specify a delay in seconds, minutes, hours, or days before proceeding to the next activity.

    * **[!UICONTROL Fixed time]**: Set a specific date and time after which the next activity starts.

    ![](../assets/wait_activity.png)

## Example{#wait-example}

The following example illustrates the **[!UICONTROL Wait]** activity in a typical use case.  An email with a promo code is sent to profiles celebrating their birthdays. After 2 days, an SMS is sent to the same group as a reminder that their birthday promo code is about to expire.

![](../assets/wait-example.png)
