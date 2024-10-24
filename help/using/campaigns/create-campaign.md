---
solution: Journey Optimizer
product: journey optimizer
title: Create a campaign
description: Learn how to create campaigns in Journey Optimizer
feature: Campaigns
topic: Content Management
role: User
level: Beginner
keywords: create, optimizer, campaign, surface, messages
exl-id: 617d623c-e038-4b5b-a367-5254116b7815
---
# Create a campaign {#create-campaign}

>[!NOTE]
>
>Before creating a new campaign, make sure you have a channel configuration (i.e. message surface) and an Adobe Experience Platform audience ready for use. Learn more in these sections:
>
>* [Create channel configurations](../configuration/channel-surfaces.md) 
>* [Get started with audiences](../audience/about-audiences.md)

To create a new campaign, access the **[!UICONTROL Campaigns]** menu, then click **[!UICONTROL Create campaign]**. You can also duplicate an existing live campaign to create a new one. [Learn more](modify-stop-campaign.md#duplicate)

## Choose the campaign type {#campaigntype}

>[!CONTEXTUALHELP]
>id="ajo_campaigns_campaign_type"
>title="Campaign type"
>abstract="**Scheduled campaigns** are executed immediately or on a specified date and are meant to send send marketing type messages. **API-triggered** campaigns are executed using an API call. They are aimed at sending either marketing messages (promotional messages which require user consent) or transactional messages (non-commercial messages, that can also be sent to unsubscribed profiles in specific contexts)."

1. Select the type of campaign that you want to execute

    * **[!UICONTROL Scheduled - Marketing]**: execute the campaign immediately or on a specified date. Scheduled campaigns are aimed at sending **marketing** messages. They are configured and executed from the user interface.

    * **[!UICONTROL API-triggered - Marketing/Transactional]**: execute the campaign using an API call. API-triggered campaigns are aimed at sending either **marketing**, or **transactional** messages, i.e. messages sent out following an action performed by an individual: password reset, cart purchase etc. [Learn how to trigger a campaign using APIs](api-triggered-campaigns.md)

    ![](assets/create-campaign-modal.png)

1. Click **[!UICONTROL Create]** to create the campaign.

## Define the campaign properties {#create}

1. In the **[!UICONTROL Properties]** section, specify a name and a description for the campaign.

    <!--To test the content of your message, toggle the **[!UICONTROL Content experiment]** option on. This allows you to test multiple variables of a delivery on populations samples, in order to define which treatment has the biggest impact on the targeted population.[Learn more about content experiment](../content-management/content-experiment.md).-->

1. The **Tags** field allows you to assign Adobe Experience Platform Unified Tags to your campaign. This allows you to easily classify them and improve search from the campaigns list. [Learn how to work with tags](../start/search-filter-categorize.md#tags) 

1. To assign custom or core data usage labels to the campaign, click the **[!UICONTROL Manage access]** button. [Learn more on Object Level Access Control (OLA)](../administration/object-based-access.md)
    
## Define the campaign audience {#audience}

Define the population targeted by the campaign, follow these steps:

>[!IMPORTANT]
>
>The use of audiences and attributes from [audience composition](../audience/get-started-audience-orchestration.md) is currently unavailable for use with Healthcare Shield or Privacy and Security Shield.
>
>For API-triggered campaigns, the audience needs to be set via API call.
    
1. In the **Audience** section, click the **[!UICONTROL Select audience]** button to display the list of available Adobe Experience Platform audiences. [Learn more on audiences](../audience/about-audiences.md)

1. In the **[!UICONTROL Identity namespace]** field, choose the namespace to use in order to identify the individuals from the selected segment.

    Individuals belonging to a segment that does not have the selected identity (namespace) among their different identities will not be targeted by the campaign. [Learn more on namespaces](../event/about-creating.md#select-the-namespace)

    ![](assets/create-campaign-namespace.png)

    <!--If you are are creating an API-triggered campaign, the **[!UICONTROL cURL request]** section allows you to retrieve the **[!UICONTROL Campaign ID]** to use in the API call. [Learn more](api-triggered-campaigns.md)-->

## Create the message and configure tracking {#content}

1. In the **[!UICONTROL Actions]** section, select or create new configuration.

    A configuration is defined by a [System Administrator](../start/path/administrator.md). It contains all the technical parameters for sending the message, such as header parameters, subdomain, mobile apps, etc. [Learn more](../configuration/channel-surfaces.md).

    Only channel configurations compatible with the marketing campaign type are listed in the drop-down list.

    ![](assets/create-campaign-action.png)

    >[!NOTE]
    >
    >If you are creating a push notification campaign, you can enable the **[!UICONTROL Rapid delivery mode]**, which is a Journey Optimizer add-on that allows very fast push message sending in large volumes. [Learn more](../push/create-push.md#rapid-delivery)

1. Click the **[!UICONTROL Edit content]** button to create and design your message. Learn detailed steps to create your message content in the following pages:

    <table style="table-layout:fixed">
    <tr style="border: 0;">
    <td>
    <a href="../email/create-email.md">
    <img alt="Lead" src="../assets/do-not-localize/email.jpg">
    </a>
    <div><a href="../email/create-email.md"><strong>Create emails</strong>
    </div>
    <p>
    </td>
    <td>
    <a href="../push/create-push.md">
      <img alt="Infrequent" src="../assets/do-not-localize/push.jpg">
    </a>
    <div>
    <a href="../push/create-push.md"><strong>Create push notifications</strong></a>
    </div>
    <p>
    </td>
    <td>
    <a href="../sms/create-sms.md">
      <img alt="Validation" src="../assets/do-not-localize/sms.jpg">
    </a>
    <div>
    <a href="../sms/create-sms.md"><strong>Create SMS messages</strong></a>
    </div>
    <p>
    </td>
    </tr>
    </table>

1. Once your content is defined, use the **[!UICONTROL Simulate content]** button to preview and test your content with test profiles. [Learn more](../content-management/preview-test.md).

1. Click the arrow to go back to the campaign creation screen.

    ![](assets/create-campaign-design.png)

1. In the **[!UICONTROL Actions tracking]** section, specify if you want to track how your recipients react to your delivery: you can track clicks and/or opens.
        
    Tracking results will be accessible from the campaign report once the campaign has been executed. [Learn more on campaign reports](../reports/campaign-global-report-cja.md)

## Schedule the campaign {#schedule}

>[!CONTEXTUALHELP]
>id="ajo_campaigns_schedule"
>title="Campaign schedule"
>abstract="By default, campaigns start upon manual activation and terminate immediately after the message is sent once. Nevertheless, you have the flexibility to set a specific date and time for the message to be sent. Furthermore, you can specify an end date for recurring or API-triggered campaigns. In the Action triggers, you can also configure the message sending frequency to suit your preferences."

>[!CONTEXTUALHELP]
>id="ajo_campaigns_schedule_start"
>title="Campaign start"
>abstract="Specify a date and time at which the message should be sent."

>[!CONTEXTUALHELP]
>id="ajo_campaigns_schedule_end"
>title="Campaign end"
>abstract="Specify when a recurring campaign should stop being executed."

>[!CONTEXTUALHELP]
>id="ajo_campaigns_schedule_triggers"
>title="Campaign action triggers"
>abstract="Define a frequency at which the campaign's message should be sent."

By default, campaigns start once they have been activated manually, and end as soon as the message has been sent once.

You can define a frequency at which the campaign's message should be sent. To do this, use the **[!UICONTROL Action triggers]** options in the campaign creation screen to specify if the campaign should be executed daily, weekly, or monthly.

If you do not want to execute your campaign right after its activation, you can specify a date and time at which the message should be sent using the **[!UICONTROL Campaign start]** option. The **[!UICONTROL Campaign end]** option allows you to specify when a recurring campaign should stop being executed.

![](assets/create-campaign-schedule.png)

Once your campaign is ready, you can review and publish it. [Learn more](review-activate-campaign.md)
