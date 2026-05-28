---
solution: Journey Optimizer
product: journey optimizer
title: Create a WhatsApp message
description: Learn how to create a WhatsApp message in Journey Optimizer
feature: Whatsapp
topic: Content Management
role: User
level: Beginner
exl-id: cac6f675-59e0-431d-8c20-f24ef16d7bf2
TQID: https://experienceleague.adobe.com/fio2Etyk9FdkyTiHwRMkadrJ4bbsFz7--KvzQvUQrbc
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: b8df23d2-98a2-4406-86cc-2babe8728d36
    internal-label: WhatsApp channel (AJO)
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Create a WhatsApp message {#create-whatsapp}

With Adobe Journey Optimizer, you can design and send engaging messages on WhatsApp. Simply add a WhatsApp action to your journey or campaign and craft your message content as detailed below. Adobe Journey Optimizer also lets you test your WhatsApp messages before sending them, ensuring perfect rendering, accurate personalization, and proper configuration of all settings.

Note that only Outbound messages elements are supported in Journey Optimizer. 

+++ Learn more about supported message elements and interactive buttons

The following message types are supported in WhatsApp:

| Message Feature | Description |
|-|-|
| Headers | Optional text that appears above the body of your message.|
| Text | Supports dynamic content through parameters. |
| Images (JPEG, PNG) | Must be in 8-bit RGB or RGBA format and under 5 MB in size. |
| Videos | Must be 3GPP or MP4, under 16 MB, and hosted via URL. |
| Audio | Only available for response messages. Must be AAC, AMR, MP3, MP4 audio, or OGG format, hosted on a URL, and under 16 MB. |
| Documents | Must be under 100 MB, hosted on a URL, and in one of the following formats: .txt, .xls/.xlsx, .doc/.docx, .ppt/.pptx, or .pdf. |
| Body Text | Supports dynamic content through parameters. |
| Footer Text | Supports dynamic content through parameters. |

The following call-to-action options are available for your WhatsApp messages:

| Call to actions | Description |
|-|-|
| Quick reply | Short preset replies the user can tap to respond to your message. |
| Visit website | Only one button is permitted, with variable parameters included. |
| Call on WhatsApp | Provides a button that opens a WhatsApp chat with the specified phone number directly from the message. |
| Call phone number | Provides a button that initiates a phone call to the specified number when tapped by the user. |
| Call to action – URL | Opens a URL (**Visit website**). Only one URL button is permitted, with variable parameters included. |
| Call to action – phone | Uses the phone number from the template, for example **Call phone number** (places a call) or **Call on WhatsApp** (opens a chat with that number in WhatsApp). |

Note that **Copy code** interactive buttons are not supported.

+++

## Add a WhatsApp message {#create-whatsapp-journey-campaign}

Browse the tabs below to learn how to add a WhatsApp message in a campaign or a journey.

>[!BEGINTABS]

>[!TAB Add a WhatsApp message to a Journey]

1. Open your journey then drag and drop a **WhatsApp activity** from the **Actions** section of the palette.

    ![](assets/whatsapp-create-jo.png)

1. Provide basic information on your message (label, description, category), then choose the message configuration to use.

    For more information on how to configure a journey, refer to [this page](../building-journeys/journey-gs.md)

    The **[!UICONTROL configuration]** field is pre-filled, by default, with the last configuration used for that channel by the user.

1. In the **[!UICONTROL Business rules]** section, you can apply a rule set to control communication pressure on WhatsApp messages.

    Learn more about [rule sets](../conflict-prioritization/rule-sets.md), [channel frequency capping](../conflict-prioritization/channel-capping.md), and [quiet hours](../conflict-prioritization/quiet-hours.md).

You can now start designing the content of your WhatsApp message from the **[!UICONTROL Edit content]** button, as detailed below.

>[!TAB Add a WhatsApp message to a Campaign]

1. Access the **[!UICONTROL Campaigns]** menu, then click **[!UICONTROL Create campaign]**.

1. Select the **Scheduled - Marketing** campaign type.

1. From the **[!UICONTROL Properties]** section, edit your Campaign's **[!UICONTROL Title]** and **[!UICONTROL Description]**.

1. Click the **[!UICONTROL Select audience]** button to define the audience to target from the list of available Adobe Experience Platform audiences. [Learn more](../audience/about-audiences.md).

1. In the **[!UICONTROL Identity namespace]** field, choose the namespace to use in order to identify the individuals from the selected audience. [Learn more](../event/about-creating.md#select-the-namespace).

1. In the **[!UICONTROL Actions]** section, choose **[!UICONTROL WhatsApp]** and select or create a new configuration.

    Learn more about WhatsApp configuration on [this page](whatsapp-configuration.md).

    ![](assets/whatsapp-campaign-1.png)

1. Click **[!UICONTROL Create experiment]** to start configuring your content experiment and create treatments to measure their performance and identify the best option for your target audience. [Learn more](../content-management/content-experiment.md)

1. In the **[!UICONTROL Actions tracking]** section, specify if you want to track clicks on links in your WhatsApp message.

    Journey Optimizer also tracks interactions on supported WhatsApp template buttons, **Quick reply**, **Call to action – URL** and **Call to action – phone**, alongside your other channel reporting. **Copy code** buttons are not supported and their interactions are not tracked.

1. Campaigns are designed to be executed on a specific date or on a recurring frequency. Learn how to configure the **[!UICONTROL Schedule]** of your campaign in [this section](../campaigns/create-campaign.md#schedule). 

1. From the **[!UICONTROL Action triggers]** menu, choose the **[!UICONTROL Frequency]** of your WhatsApp message:

    * Once
    * Daily
    * Weekly
    * Month
    
You can now start designing the content of your WhatsApp message from the **[!UICONTROL Edit content]** button, as detailed below.

>[!ENDTABS]

## Define your WhatsApp content{#whatsapp-content}

>[!BEGINSHADEBOX]

Before designing your WhatsApp message in Journey Optimizer, you first need to create and design your template in Meta. [Learn more](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343)

Note that your WhatsApp template must first be approved by Meta before using it in Journey Optimizer. This process usually takes a few hours but may take up to 24 hours. [Learn more](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#approval-process)

>[!ENDSHADEBOX]

1. From the journey or campaign configuration screen, click the **[!UICONTROL Edit content]** button to configure the WhatsApp message content.

<!--
1. Select **[!UICONTROL Template message]**.
-->

1. Choose your **Template category**:

    * Marketing
    * Utility
    * Authentication

    [Learn more about Template categories](https://developers.facebook.com/docs/whatsapp/updates-to-pricing/new-template-guidelines/#template-category-guidelines)

    ![](assets/whatsapp-design-1.png)

1. From the **WhatsApp template** drop-down, select your previously created template designed in Meta. 

    [Learn more about how to create your Whatsapp templates](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343)

    ![](assets/whatsapp-design-2.png)

1. In the **[!UICONTROL Image URL]** field, add media URLs to replace any placeholders in your template. Meta's template media are only placeholders. To display images, audio, or video correctly, you must use external URLs from Adobe Experience Manager or other sources.

    ![](assets/whatsapp-design-3.png)

1. Use the personalization editor to add personalization to your template. You can use any attribute, such as the profile name or city for example. 

    Browse through the following page to learn more about [personalization](../personalization/personalize.md).

    ![](assets/whatsapp-design-4.png)

1. Use the **[!UICONTROL Simulate content]** button to preview your WhatsApp message content, shortened URLs, and personalized content. [Learn more](send-whatsapp.md)

Once you have performed your tests and validated the content, you can [send your WhatsApp message](send-whatsapp.md) to your audience and monitor its performance through [reporting](../reports/campaign-global-report-cja.md). For WhatsApp interaction data stored in Experience Platform, see [Analyze WhatsApp interactions](send-whatsapp.md#whatsapp-channel-context). 

<!--
* **[!UICONTROL Template message]**: Predefined message imported from Meta into Journey Optimizer. These are intended for sending notifications, alerts, or updates to your customers.

* **[!UICONTROL Response message]**: Message created in Journey Optimizer and sent in reply to customer queries or interactions.

>[!BEGINTABS]

>[!TAB Template message]

1. From the journey or campaign configuration screen, click the **[!UICONTROL Edit content]** button to configure the WhatsApp message content.

1. Select **[!UICONTROL Template message]**.

1. Choose your Template category. [Learn more](https://developers.facebook.com/docs/WhatsApp/updates-to-pricing/new-template-guidelines/)

1. From the **WhatsApp template** drop-down, select your previously created template designed in Meta.

1. Use the personalization editor to define content, add personalization and dynamic content. You can use any attribute, such as the profile name or city for example. You can also define conditional rules. Browse to the following pages to learn more about [personalization](../personalization/personalize.md) and [dynamic content](../personalization/get-started-dynamic-content.md) in the personalization editor.

1. Use the **[!UICONTROL Simulate content]** button to preview your WhatsApp message content, shortened URLs, and personalized content. [Learn more](send-whatsapp.md)

Once you have performed your tests and validated the content, you can send your WhatsApp message to your audience. These steps are detailed on [this page](send-whatsapp.md)

>[!TAB Response message]

1. From the journey or campaign configuration screen, click the **[!UICONTROL Edit content]** button to configure the WhatsApp message content.

1. Select **[!UICONTROL Response message]**.

1. Enter your text in the **[!UICONTROL Body]** field.

1. Use the personalization editor to define content, add personalization and dynamic content. You can use any attribute, such as the profile name or city for example. You can also define conditional rules. Browse to the following pages to learn more about [personalization](../personalization/personalize.md) and [dynamic content](../personalization/get-started-dynamic-content.md) in the personalization editor.

1. Use the **[!UICONTROL Simulate content]** button to preview your WhatsApp message content, shortened URLs, and personalized content. [Learn more](send-whatsapp.md)

Once you have performed your tests and validated the content, you can send your WhatsApp message to your audience. These steps are detailed on [this page](send-whatsapp.md)

>[!ENDTABS]
-->


## How-to video {#video}

The video below shows how to create a multi-step WhatsApp journey using Adobe Journey Optimizer.

+++ See video

>[!VIDEO](https://video.tv.adobe.com/v/3470282/?learn=on")

+++
