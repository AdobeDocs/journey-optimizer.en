---
title: In-app channel prerequisites and configuration
description: Learn how to configure your environment to send In-app messages with Journey Optimizer
role: Admin
feature: In App
level: Intermediate
keywords: in-app, message, configuration, platform
exl-id: 469c05f2-652a-4899-a657-ddc4cebe3b42
TQID: https://experienceleague.adobe.com/GWlxb1IJ5oZue5m0s4nN7iOa1S-IfHEFNuU7Lcj0H2s
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a653cc2e-bc85-4353-a306-399e5b247978
    internal-label: Journey Optimizer campaigns
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: b856530c-d60b-42d8-a19d-df2dfd7fe62a
    internal-label: Access control
  - id: cf64c7f6-7428-4ae5-b158-8df9771f38f4
    internal-label: Channel configurations
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
  - id: fdac7813-bd56-47ae-9f6d-fa94ad1c5dee
    internal-label: Overview
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: c18d9e03-ac7d-4811-9c92-3e92ddc70ade
    internal-label: Mobile experience
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Prerequisites and configuration {#inapp-configuration}

## Configuration steps {#inapp-steps}

To send In-app messages in your journeys and campaigns with [!DNL Journey Optimizer], you need to go through the following configuration steps.

1. Make sure you have the correct permissions on Journey Optimizer campaigns before starting, even if you plan to only use in-app messages in journeys. Campaign permissions are still required. [Learn more](../campaigns/get-started-with-campaigns.md#prerequisites).
1. Enable Adobe Journey Optimizer in your Adobe Experience Platform Data Collection datastream, and check your default merge policy in Adobe Experience Platform, as detailed in the [Delivery prerequisites](#delivery-prerequisites) below. 
1. Create an In-app message channel configuration in Administration > Channels > Channel configurations, as detailed in [this section](#channel-prerequisites). 
1. If you are using content experiments, make sure to follow the requirements listed in [this section](#experiment-prerequisite).

Once done, you can create, configure and send your first In-app message. Learn how to achieve this in [this section](create-in-app.md).

>[!CAUTION]
>
>When targeting pseudonymous profiles (unauthenticated visitors) with your In-app messages, consider setting a Time-To-Live (TTL) for automatic profile deletion to manage your engageable profile count and associated costs. [Learn more](../start/guardrails.md#profile-management-inbound)

## Delivery prerequisites {#delivery-prerequisites}

For the In-app messages to be delivered correctly, the following settings must be defined:

* In the [Adobe Experience Platform Data Collection](https://experienceleague.adobe.com/docs/experience-platform/edge/datastreams/overview.html){target="_blank"}, make sure you have a datastream defined such as under the **[!UICONTROL Adobe Experience Platform]** service you have the Adobe Experience Platform Edge and **[!UICONTROL Adobe Journey Optimizer]** option enabled.

    This ensures that the Journey Optimizer inbound events are correctly handled by the Adobe Experience Platform Edge. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/edge/datastreams/configure.html){target="_blank"}
    
    >[!NOTE]
    >
    >The use of `context.datastream` attributes is currently supported only for Web channel campaigns in Journey Optimizer. Attempting to use `context.datastream` in In-App messages will result in validation errors such as `Invalid syntax Missing schema field: 'datastream`.

    ![](assets/inapp_config_6.png)

* In [Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html){target="_blank"}, make sure you have the default merge policy with the **[!UICONTROL Active-On-Edge Merge Policy]** option enabled. To do this, select a policy under the **[!UICONTROL Customer]** > **[!UICONTROL Profiles]** > **[!UICONTROL Merge Policies]** Experience Platform menu. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/ui-guide.html#configure){target="_blank"}

    This merge policy is used by [!DNL Journey Optimizer] inbound channels to correctly activate and publish inbound campaigns on the edge. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/ui-guide.html){target="_blank"}
    
    >[!NOTE]
    >
    >When using a custom **[!UICONTROL Dataset preference]** merge policy, make sure to add the **[!UICONTROL Journey Inbound]** dataset within the specified merge policy.

    ![](assets/inapp_config_8.png)

* To troubleshoot the delivery of Journey Optimizer mobile experiences, you can use the **Edge Delivery** view within **Adobe Experience Platform Assurance**. This plugin enables you to inspect request calls in detail, verify whether the expected edge calls occur as anticipated, and examine profile data, including identity maps, segment memberships, and consent settings. Additionally, you can review the activities the request qualified for and identify those it did not.

    Using the **Edge Delivery** plugin helps you gain the insights needed to understand and troubleshoot your inbound implementations effectively.

    [Learn more about Edge Delivery view](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/view/edge-delivery){target="_blank"}

## Create an In-app configuration {#channel-prerequisites}

To create an In-app configuration in Journey Optimizer, follow these steps:

1. Access the **[!UICONTROL Channels]** > **[!UICONTROL General settings]** > **[!UICONTROL Channel configurations]** menu, then click **[!UICONTROL Create channel configuration]**.

    ![](assets/inapp_config_1.png)

1. Enter a name and a description (optional) for the configuration, then select the channel to configure.

    >[!NOTE]
    >
    > Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore `_`, dot`.` and hyphen `-` characters.

1. To assign custom or core data usage labels to the configuration, you can select **[!UICONTROL Manage access]**. [Learn more about Object Level Access Control (OLAC)](../administration/object-based-access.md).

1. Select **[!UICONTROL Marketing action]**(s) to associate consent policies to the messages using this configuration. All consent policies associated with the marketing action are leveraged in order to respect the preferences of your customers. [Learn more](../action/consent.md#surface-marketing-actions)

1. Select **In-app messaging** channel.

    ![](assets/inapp_config_9.png)

1. Select the platform for which you want to define the settings. This allows you to specify the target app for each platform and ensures consistent content delivery across multiple platforms.

    >[!NOTE]
    >
    >For iOS and Android platforms, delivery is based solely on the app ID. If both apps share the same app ID, content will be delivered to both, regardless of the platform selected in the **[!UICONTROL Channel configuration]**.
    >To restrict In-app messages delivery to a specific platform, you must implement device-specific rules within your journey or campaign logic.

    ![](assets/inapp_config_10.png)

1. For Web: 

    * You can either input a **[!UICONTROL Page URL]** to apply changes to a specific page.

    * You can create a rule to target multiple URLs that follow the same pattern. 

        +++ How to build a Pages matching rule.

        1. Select **[!UICONTROL Pages matching rule]** as App configuration and enter your **[!UICONTROL Page URL]**.

        1. In the **[!UICONTROL Edit configuration rule]** window, define your criteria for the **[!UICONTROL Domain]** and **[!UICONTROL Page]** fields.
        1. From the condition dropdowns, further personalize your criteria.

            Here, for example, to edit elements that are displayed on all the sales product pages of your Luma website, select Domain > Starts with > luma and Page > Contains > sales.

            ![](assets/in_app_web_surface_4.png)

        1. Click **[!UICONTROL Add another page rule]** to create another rule if needed.

        1. Select the **[!UICONTROL Default authoring and preview URL]**.

        1. Save your changes. The rule is displayed in the **[!UICONTROL Create campaign]** screen.

        +++

1. For iOS and Android:

    * Enter your **[!UICONTROL App id]**.

1. Submit your changes.

You can now select your configuration when creating your In-app message.

## Reporting prerequisites {#experiment-prerequisites}

To enable reporting for In-app channel, you need to make sure the [dataset](../data/get-started-datasets.md) used in your In-app implementation [datastream](https://experienceleague.adobe.com/docs/experience-platform/datastreams/overview.html){target="_blank"} is also included in your reporting configuration. In other words, when configuring reporting, if you add a dataset that is not present in your app datastream, app data will not display in your reports. Learn how to add datasets for reporting in [this section](../reports/reporting-configuration.md#add-datasets).

If you are **not** using the following pre-defined [field groups](https://experienceleague.adobe.com/docs/experience-platform/xdm/tutorials/create-schema-ui.html#field-group){target="_blank"} for your dataset schema: `AEP Web SDK ExperienceEvent` and `Consumer Experience Event` (as defined on [this page](https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/initial-configuration/configure-schemas.html#add-field-groups){target="_blank"}), make sure to add the following field groups: `Experience Event - Proposition Interactions`, `Application Details`, `Commerce Details`, and `Web Details`. These are needed by [!DNL Journey Optimizer] reporting as they are tracking which campaigns and journeys each profile is participating in.

[Learn more about reporting configuration](../reports/reporting-configuration.md)

>[!NOTE]
>
>* The dataset is used read-only by the [!DNL Journey Optimizer] reporting system and doesn't affect data collection or data ingestion.
>* Adding the required field groups is additive only — it applies to pages where a campaign or journey is running and leaves all other tracking untouched.

**Related topics:**

* [Create an In-app message](create-in-app.md)
* [Create a campaign](../campaigns/create-campaign.md)
* [Design In-app message](design-in-app.md)
* [In-app report](../reports/campaign-global-report-cja-inapp.md)


