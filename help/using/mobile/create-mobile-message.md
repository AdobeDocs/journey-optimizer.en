---
solution: Journey Optimizer
product: journey optimizer
title: Create a Mobile message
description: Learn how to create a Mobile message in Journey Optimizer
feature: SMS
topic: Content Management
role: User
level: Beginner
exl-id: 1f88626a-b491-4b36-8e3f-57f2b7567dd0
TQID: https://experienceleague.adobe.com/xgPlWorA3lsIF8ZBPHdg2UAK8cLKUsJO-2ONc7ZG8AU
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: e5329d1b-e590-4e24-a3fb-ef3fe0f2c721
    internal-label: Subdomains
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Create a Mobile message {#create-sms}

>[!CONTEXTUALHELP]
>id="ajo_message_sms"
>title="Create a Mobile message"
>abstract="To create a Mobile message, add an SMS action in a journey or a campaign and start personalizing it with the personalization editor."

>[!AVAILABILITY]
>
>RCS is not a HIPAA-Ready Service and must not be used to collect, store, or process any sensitive personal data, including permitted health data, e.g. personal health information, that your organization may otherwise be permitted to process in Journey Optimizer.

You can design and send text (SMS), rich communication (RCS) and multimedia (MMS) messages with Adobe Journey Optimizer. You first need to add an Mobile message action in a journey or a campaign, and then define the content of the Mobile message, as detailed below. Adobe Journey Optimizer also offers capabilities to test your Mobile messages before sending, so that you can check the rendering, personalization attributes, and all other settings. 

In accordance with the industry standards and regulations, all SMS/RCS/MMS marketing messages must contain a way for the recipients to easily unsubscribe. To do this, SMS recipients can reply with opt-in and opt-out keywords. [Learn how to manage opt-out](../privacy/opt-out.md#opt-out-decision-management)

## Add a Mobile message {#create-sms-journey-campaign}

Browse the tabs below to learn how to add a Mobile message in a campaign or a journey.

>[!BEGINTABS]

>[!TAB Add a Mobile message to a Journey]

1. Open your journey then drag and drop an **[!UICONTROL Action]** activity from the **[!UICONTROL Actions]** section of the palette. Learn more about the [Action activity](../building-journeys/journey-action.md).

    >[!IMPORTANT]
    >
    >Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release. Existing journeys using these activities continue to work without any changes—no migration is required.

1. Select **[!UICONTROL Mobile message]** as the action type and click **[!UICONTROL Add]**.  

    ![](assets/sms_create_1.png)

1. Enter a **[!UICONTROL Label]** to identify your action in the journey canvas.

1. Click the **[!UICONTROL Configure action]** button.

1. You are directed to the **[!UICONTROL Actions]** tab. From there, select or create the Mobile message configuration to use. [Learn more](mobile-configuration.md)

    ![](assets/sms_create_2.png)

1. Additionally, you can apply capping rules to your Mobile message action by selecting a rule set in the **[!UICONTROL Business rules]** drop-down list. [Learn more](../conflict-prioritization/channel-capping.md)

1. Select the **[!UICONTROL Edit content]** button and create your content as desired. [Learn more](design-mobile.md)

1. Go back to the journey canvas. If necessary, complete your journey flow by dragging and dropping additional actions or events. [Learn more](../building-journeys/about-journey-activities.md)

For more information on how to create, configure and publish a journey, refer to [this page](../building-journeys/journey-gs.md).

>[!TAB Add a Mobile message to a Campaign]

1. Access the **[!UICONTROL Campaigns]** menu, then click **[!UICONTROL Create campaign]**.

1. Select the type of campaign that you want to execute

    * **Scheduled - Marketing**: execute the campaign immediately or on a specified date. Scheduled campaigns are aimed at sending marketing messages. They are configured and executed from the user interface.

    * **API-triggered - Marketing/Transactional**: execute the campaign using an API call. API-triggered campaigns are aimed at sending either marketing or transactional messages, i.e., messages sent out following an action performed by an individual: password reset, cart purchase, etc.

1. From the **[!UICONTROL Properties]** section, edit your Campaign's **[!UICONTROL Title]** and **[!UICONTROL Description]**.

1. From the **[!UICONTROL Action]** tab, click **[!UICONTROL Add action]** and choose **[!UICONTROL Mobile message]**. Then, select or create a new configuration.

    Learn more about Mobile message configuration on [this page](mobile-configuration.md).

    ![](assets/sms_create_3.png)

1. Click **[!UICONTROL Create experiment]** to start configuring your content experiment and create treatments to measure their performance and identify the best option for your target audience. [Learn more](../content-management/content-experiment.md)

1. In the **[!UICONTROL Actions tracking]** section, specify if you want to track clicks on links in your Mobile message.

1. From the **[!UICONTROL Audience]** tab, click the **[!UICONTROL Select audience]** button to define the audience to target from the list of available Adobe Experience Platform audiences. [Learn more](../audience/about-audiences.md).

1. In the **[!UICONTROL Identity namespace]** field, choose the namespace to use in order to identify the individuals from the selected audience. [Learn more](../event/about-creating.md#select-the-namespace).

1. From the **[!UICONTROL Schedule]** tab, you can design your Campaigns to be executed on a specific date or on a recurring frequency. Learn how to configure the **[!UICONTROL Schedule]** of your campaign in [this section](../campaigns/campaign-schedule.md#action-campaign-schedule). 

1. From the **[!UICONTROL Action triggers]** menu, choose the **[!UICONTROL Frequency]** of your Mobile message:

    * Once
    * Daily
    * Weekly
    * Month
    
You can now start designing the content of your Mobile message from the **[!UICONTROL Edit content]** button, as detailed below. [Learn more](design-mobile.md)

For more information on how to create, configure and activate a campaign, refer to [this page](../campaigns/get-started-with-campaigns.md).

>[!ENDTABS]

**Related topics**

* [Design a mobile message](design-mobile.md)
* [Add a message in a campaign](../campaigns/create-campaign.md)
* [Preview, test and send your Mobile message](send-mobile-message.md)
* [Configure Mobile message channel](mobile-configuration.md)
* [Mobile message reports](../reports/journey-global-report-cja-sms.md)

