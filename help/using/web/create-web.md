---
title: Create web experiences
description: Learn how to author a web page and edit its content in Journey Optimizer
feature: Web Channel
topic: Content Management
role: User
level: Beginner
exl-id: e28c038b-49ed-4685-bfe6-514116eb0711

---
# Create web experiences {#create-web}

[!DNL Journey Optimizer] allows you to personalize the web experience you deliver to your customers through inbound web campaigns.

>[!CAUTION]
>
>Currently in [!DNL Journey Optimizer] you can only create web experiences using **campaigns**.

[Learn how to create a web campaign in this video](#video)

## Create a web campaign {#create-web-campaign}

>[!CONTEXTUALHELP]
>id="ajo_web_surface"
>title="Define a web configuration"
>abstract="A web configuration can match a single page URL or multiple pages, allowing you to deliver content modifications across one or several web pages."

>[!CONTEXTUALHELP]
>id="ajo_web_surface_rule"
>title="Build a pages matching rule"
>abstract="A pages matching rule enables to target multiple URLs matching the same rule - for example, if you want to apply the changes to a hero banner across a whole website or add a top image that displays on all the product pages of a website."

To start building your web experience through a campaign, follow the steps below.

>[!NOTE]
>
>If this is your first time creating a web experience, make sure you follow the prerequisites described in [this section](web-prerequisites.md).

1. Access the **[!UICONTROL Campaigns]** menu, then click **[!UICONTROL Create campaign]**.[Learn more](../campaigns/create-campaign.md)


1. Select the type of campaign that you want to execute

    * **Scheduled - Marketing**: execute the campaign immediately or on a specified date. Scheduled campaigns are aimed at sending marketing messages. They are configured and executed from the user interface.

    * **API-triggered - Marketing/Transactional**: execute the campaign using an API call. API-triggered campaigns are aimed at sending either marketing, or transactional messages, i.e. messages sent out following an action performed by an individual: password reset, cart purchase etc.

1. Complete the steps to create a web campaign, such as the campaign properties, [audience](../audience/about-audiences.md), and [schedule](../campaigns/create-campaign.md#schedule).

1. Select the **[!UICONTROL Web]** action.

1. Select or create a new configuration. [Learn more on web configuration](web-configuration.md)

    ![](assets/web-campaign-steps.png)

For more information on how to configure a campaign, refer to [this page](../campaigns/get-started-with-campaigns.md).

## Test the web campaign {#test-web-campaign}

>[!CONTEXTUALHELP]
>id="ajo_web_designer_preview"
>title="Preview your web experience"
>abstract="Get a simulation of what your web experience will look like."

Once you [authored your web experience](edit-web-content.md) using the web designer, you can use test profiles to preview your modified web pages. If you inserted personalized content, you can check how this content is displayed, using test profile data.

To do this, click **[!UICONTROL Simulate content]** from either the web campaign edit content screen or the web designer, then add a test profile to check your web page using the test profile data.

![](assets/web-designer-preview.png)

You can also open it in the default browser, or copy the test URL to paste it in any browser. This allows you to share the link with your team and stakeholders who will be able to preview the new web experience in any browser before the campaign goes live.

>[!NOTE]
>
>When copying the test URL, the content displayed is the one personalized for the test profile used when the content simulation was generated in [!DNL Journey Optimizer].

Detailed information on how to select test profiles and preview your content is available in the [Content Management](../content-management/preview-test.md) section.

## Activate the web campaign {#activate-web-campaign}

Once you defined your [web campaign settings](#configure-web-campaign) and you edited your content as desired using the [web designer](edit-web-content.md#work-with-web-designer), you can review and activate your web campaign. Follow the steps below.

<!--
>[!NOTE]
>
>You can also preview your web campaign content before activating it. [Learn more](#test-web-campaign)-->

1. From your web campaign, select **[!UICONTROL Review to activate]**.

1. Check and edit if needed the content, properties, configuration, audience and schedule.

1. Select **[!UICONTROL Activate]**.

    ![](assets/web-campaign-activate.png)

    >[!NOTE]
    >
    >After you click **[!UICONTROL Activate]**, it can take up to 15 minutes for web campaigns changes to be available live on your website.

Your web campaign takes the **[!UICONTROL Live]** status and is now visible to the selected audience. Each recipient of your campaign can see the modifications you added to your website using the [!DNL Journey Optimizer] web designer.

>[!NOTE]
>
>If you defined a schedule for your web campaign, it has the **[!UICONTROL Scheduled]** status until the start date and time are reached.
>
>If you activate a web campaign impacting the same pages as another campaign which is already live, all the changes will be applied to your web pages.

Learn more on activating campaigns in [this section](../campaigns/review-activate-campaign.md).

## Stop a web campaign {#stop-web-campaign}

When a web campaign is live, you can stop it to prevent your audience from seeing your modifications. Follow the steps below.

1. Select a live campaign from the list.

1. From the top menu, select **[!UICONTROL Stop campaign]**.

    ![](assets/web-campaign-stop.png)

1. The modifications you added will not be visible anymore to the audience you defined.

>[!NOTE]
>
>Once a web campaign is stopped, you cannot edit or activate it again. You can only duplicate it and activate the duplicated campaign.

## How-to video{#video}

The video below shows how to create a web campaign, configure its properties, review, and publish it.

>[!VIDEO](https://video.tv.adobe.com/v/3418800/?quality=12&learn=on)