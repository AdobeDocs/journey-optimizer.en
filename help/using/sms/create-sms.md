---
solution: Journey Optimizer
product: journey optimizer
title: Create an SMS/MMS message
description: Learn how to create an SMS/MMS message in Journey Optimizer
feature: SMS
topic: Content Management
role: User
level: Beginner
exl-id: 1f88626a-b491-4b36-8e3f-57f2b7567dd0
---
# Create a text message (SMS/MMS) {#create-sms}

>[!CONTEXTUALHELP]
>id="ajo_message_sms"
>title="Create a text message"
>abstract="To create a text message (SMS/MMS), add an SMS action in a journey or a campaign and start personalizing it with the personalization editor."

You can design and send text (SMS) and multimedia (MMS) messages with Adobe Journey Optimizer. You first need to add an SMS action in a journey or a campaign, and then define the content of the text message, as detailed below. Adobe Journey Optimizer also offers capabilities to test your text messages before sending, so that you can check the rendering, personalization attributes, and all other settings. 

>[!NOTE]
>
>In accordance with the industry standards and regulations, all SMS/MMS marketing messages must contain a way for the recipients to easily unsubscribe. To do this, SMS recipients can reply with opt-in and opt-out keywords. [Learn how to manage opt-out](../privacy/opt-out.md#sms-opt-out-management-sms-opt-out-management)


## Add a text message {#create-sms-journey-campaign}

Browse the tabs below to learn how to add a text message (SMS/MMS) in a campaign or a journey.

>[!BEGINTABS]

>[!TAB Add a text message to a Journey]

1. Open your journey then drag and drop an SMS activity from the **Actions** section of the palette.

    ![](assets/sms_create_1.png)

1. Provide basic information on your message (label, description, category), then choose the message surface to use.

    ![](assets/sms_create_2.png)

    For more information on how to configure a journey, refer to [this page](../building-journeys/journey-gs.md)

    The **[!UICONTROL Surface]** field is pre-filled, by default, with the last surface used for that channel by the user.

You can now start designing the content of your SMS message from the **[!UICONTROL Edit content]** button, as detailed below.

>[!TAB Add a text message to a Campaign]

1. Create a new scheduled or API-triggered campaign, select **[!UICONTROL SMS]** as your action and choose the **[!UICONTROL App surface]** to use. Learn more about SMS configuration in [this page](sms-configuration.md).

    ![](assets/sms_create_3.png)

1. Click **[!UICONTROL Create]**.

1. From the **[!UICONTROL Properties]** section, edit your Campaign's **[!UICONTROL Title]** and **[!UICONTROL Description]**.

    ![](assets/sms_create_4.png)

1. Click the **[!UICONTROL Select audience]** button to define the audience to target from the list of available Adobe Experience Platform audiences. [Learn more](../audience/about-audiences.md).

1. In the **[!UICONTROL Identity namespace]** field, choose the namespace to use in order to identify the individuals from the selected audience. [Learn more](../event/about-creating.md#select-the-namespace).

    ![](assets/sms_create_5.png)

1. Click **[!UICONTROL Create experiment]** to start configuring your content experiment and create treatments to measure their performance and identify the best option for your target audience. [Learn more](../campaigns/content-experiment.md)

1. In the **[!UICONTROL Actions tracking]** section, specify if you want to track clicks on links in your SMS message.

1. Campaigns are designed to be executed on a specific date or on a recurring frequency. Learn how to configure the **[!UICONTROL Schedule]** of your campaign in [this section](../campaigns/create-campaign.md#schedule). 

1. From the **[!UICONTROL Action triggers]** menu, choose the **[!UICONTROL Frequency]** of your SMS message:

    * Once
    * Daily
    * Weekly
    * Month
    
You can now start designing the content of your text message from the **[!UICONTROL Edit content]** button, as detailed below.

>[!ENDTABS]

## Define your SMS content{#sms-content}

>[!CONTEXTUALHELP]
>id="ajo_message_sms_content"
>title="Define your SMS content"
>abstract="Customize and personalize your text messages (SMS/MMS) by using the personalization editor to define the content and incorporate dynamic elements."

To configure your SMS content, follow the steps below. Settings for MMS are detailed in [this section](#mms-content).

1. From the journey or campaign configuration screen, click the **[!UICONTROL Edit content]** button to configure the text message content.

1. Click the **[!UICONTROL Message]** field to open the personalization editor.

    ![](assets/sms-content.png)

1. Use the personalization editor to define content, add personalization and dynamic content. You can use any attribute, such as the profile name or city for example. You can also define conditional rules. Browse to the following pages to learn more about [personalization](../personalization/personalize.md) and [dynamic content](../personalization/get-started-dynamic-content.md) in the personalization editor.

1. After defining your content, you can add tracked URLs to your message. To do this, access the **[!UICONTROL Helper functions]** menu and select **[!UICONTROL Helpers]**.

    Note that in order to use the URL shortening function, you must first configure a subdomain which will be then linked to your surface. [Learn more](sms-subdomains.md)
    
    >[!CAUTION]
    >
    > To access and edit SMS subdomains, you must have the **[!UICONTROL Manage SMS Subdomains]** permission on the production sandbox. Learn more about permissions in [this section](../administration/high-low-permissions.md).

    ![](assets/sms_tracking_1.png)

1. Within the **[!UICONTROL Helper functions]** menu, click **[!UICONTROL URL function]** and then select **[!UICONTROL Add URL]**.

    ![](assets/sms_tracking_2.png)

1. In the `originalUrl` field, paste the URL that you want to shorten and click **[!UICONTROL Save]**.

1. Click **[!UICONTROL Save]** and check your message in the preview. You can now test and check your message content as detailed in [this section](#sms-mms-test).

## Define your MMS content{#mms-content}

You can enhance your communication by sending Multimedia Message Service (MMS) messages, enabling the sharing of media such as videos, pictures, audio clips and GIFs, and more. Additionally, MMS allows for up to 1600 characters of text in your message.

>[!NOTE]
>
>* MMS channel comes with a few limitations listed in [this page](../start/guardrails.md#sms-guardrails).

To create MMS content, follow these steps:

1. Create a SMS as described in [this section](#create-sms-journey-campaign).

1. Edit your SMS content as detailed in [this section](#sms-content).

1. Enable the MMS option to add media to your SMS content.

    ![](assets/sms_create_6.png)

1. Add a **[!UICONTROL Title]** to your media.

1. Enter the URL of your media in the **[!UICONTROL Media]** field.

    ![](assets/sms_create_7.png)

1. Click **[!UICONTROL Save]** and check your message in the preview. You can now test and check your message content as detailed below.

## Test and send your messages {#sms-mms-test}

Use the **[!UICONTROL Simulate content]** button to preview your text message content, shortened URLs, and personalized content.

![](assets/sms-content-preview.png)

Once you have performed your tests and validated the content, you can send your text message to your audience. These steps are detailed in [this page](send-sms.md)

Once sent, you can measure the impact of your SMS within the Campaign or Journey reports. For more on reporting, refer to [this section](../reports/campaign-global-report.md#sms-tab).

**Related topics**

* [Preview, test and send your text message](send-sms.md)
* [Configure SMS channel](sms-configuration.md)
* [SMS/MMS reports](../reports/journey-global-report.md#sms-global)
* [Add a message in a journey](../building-journeys/journeys-message.md)
* [Add a message in a campaign](../campaigns/create-campaign.md)
