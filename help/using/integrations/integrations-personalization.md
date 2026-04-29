---
solution: Journey Optimizer
product: journey optimizer
title: Enable External Integrations
description: Integrate external integrations into the channel authoring process to enrich content with personalized and dynamic information
feature: Integrations
topic: Content Management
role: User
level: Beginner
keywords: integration
---

# Using External integrations for personalization {#integrations-personalization}

Before you use external integrations in your content, confirm an administrator has **configured and activated** each integration (endpoint, authentication, policies, response payload, and activation) as described in [Work with Integrations](integrations.md).

As a marketer, you can use configured integrations to personalize your content. Follow these steps:

1. Access your campaign content and click **[!UICONTROL Add personalization]** from your Text or HTML **[!UICONTROL Components]**. 

    [Learn more on components](../email/content-components.md)

    ![](assets/external-integration-content-1.png)

1. Navigate to the **[!UICONTROL Integrations]** section and click **[!UICONTROL Open integrations]** to view all active integrations.
    
    Note that **Journey Optimizer Fragments** are available with Integrations but support outbound channels only. Once a fragment is published, adding and saving new integrations is disabled to avoid impact on existing journeys and campaigns.

    ![](assets/external-integration-content-2.png)

1. Select an integration and click **[!UICONTROL Save]**.
    
    ![](assets/external-integration-content-3.png)

1. Enable the **[!UICONTROL Pills]** mode to unlock the advanced integration menu.

    ![](assets/external-integration-content-4.png)

1. When you author integration personalization, the Integrations helper includes a **`required`** field that defines how failures or missing data interact with default content:

    * **`required=true`** (default): Rendering stops for that message. The send is excluded with **`ExternalDataLookupExclusion`**, and that exclusion is recorded in the **message feedback dataset**.
    * **`required=false`**: The result variable is set to **`null`** and rendering continues. Use default text, fallbacks, or conditional logic in your template so profiles do not receive empty content when the integration does not return data.

        ![](assets/external-integration-content-8.png)

1. To complete your integration setup, define your integration attributes, which were previously specified during [configuration](integrations.md#configure). 

    You can assign values to these attributes using either static values, which remain constant, or profile attributes, which dynamically pull information from user profiles.

    ![](assets/external-integration-content-5.png)

1. Once integration attributes are defined, you can now use the integration fields in your content for personalized messaging by clicking the ![add](assets/do-not-localize/Smock_Add_18_N.svg) icon.

    ![](assets/external-integration-content-6.png)

    >[!NOTE]
    >
    >Tokens in your template must use only fields the administrator exposed in the integration configuration. For example, `{{weatherResponse.temperature}}` is valid when `temperature` is exposed; `{{weatherResponse.humidity}}` is rejected in the editor if `humidity` was not exposed.

1. Click **[!UICONTROL Save]**.

Your integration personalization is now successfully applied to your content, ensuring each recipient receives a tailored, relevant experience based on the attributes you have configured.

![](assets/external-integration-content-7.png)

## How-to video {#video}

This video shows how **Integrations** connect Adobe Journey Optimizer to external APIs so you can pull live data and content into **outbound** channels, Email, SMS, and Push, for more relevant personalization.

>[!VIDEO](https://video.tv.adobe.com/v/3484118/?learn=on)
