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

You can add up to **3** integrations per **[!UICONTROL Fragment]** and up to **5** on the message. Integrations that come only from fragments do not count toward the **5**.

## Apply integration personalization to your content {#apply-integration-personalization}

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

<!--
## Map one API call to another {#map-integration-chain}

You can **chain** integrations so that values returned by one active integration drive the inputs (path, headers, or query parameters) of another. That lets you build a real-time data flow in a single message without custom code.

Before you start, make sure that:

* An administrator has configured and activated every integration you need. See [Configure your Integration](integrations.md).
* Variable path placeholders, headers, and query parameters are set up in the integration configuration with marketer-facing labels.
* The administrator exposed the response fields you need in each integration's **[!UICONTROL Response payload]** so they appear when authoring.

In the below example, a reservation system integration returns a flight booking reference from the profile context. A separate flight-information integration expects that reference as a **path variable**. In the personalization editor, you map the second integration's variable to a field from the first integration's response, instead of a static value or profile attribute alone.

1. Open your message or fragment and place the cursor where you want personalized content (for example, a **[!UICONTROL Text]** field).

1. Open the personalization editor and go to **[!UICONTROL Integrations]** → **[!UICONTROL Open integrations]**.

1. Select the integration whose output will supply the downstream input (in the example, the reservation or profile API that returns the flight identifier).

1. Define that integration's inputs as usual—static values, profile attributes, or other allowed mappings—then save so its response is available for chaining.

    >[!NOTE]
    >
    > Fields must appear in the administrator-defined response payload for each integration. You cannot reference response properties that were not exposed in configuration.

1. Select the **second** integration (for example, the API that needs the flight number or booking reference on the URL path).

1. For each input that must come from the first call—often a **path variable** or **variable** header/query parameter—choose the mapping source that references the **first integration's response** (for example, the flight booking reference field from the reservation payload). Do not use a static test value if you need live, profile-specific data.

1. Insert the response tokens you need in the content (for example, destination name from the flight API, loyalty balance from a loyalty integration) using the ![add](assets/do-not-localize/Smock_Add_18_N.svg) control.

1. Save the personalization.

When you **simulate** or send, Journey Optimizer resolves integrations in order: the first call runs with the profile context you configured; its output is used to build the second request. Different integrations may run at simulation time and at send time according to your setup and channel behavior.

-->

## How-to video {#video}

This video shows how **Integrations** connect Adobe Journey Optimizer to external APIs so you can pull live data and content into **outbound** channels, Email, SMS, and Push, for more relevant personalization.

>[!VIDEO](https://video.tv.adobe.com/v/3484118/?learn=on)
