---
solution: Journey Optimizer
product: journey optimizer
title: Add a channel activity in a multistep campaign
description: Learn how to add a channel activity in a multistep campaign
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: ffe1e77c-6c4f-4f23-9183-d715a4c7c402
---
# Channel activities {#channel}

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](../gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](../configuration-steps.md)<br/><br/>[Key steps for orchestrated campaign creation](../gs-campaign-creation.md)|[Create an orchestrated campaign](../create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](../orchestrate-activities.md)<br/><br/><br/>[Start and monitor the campaign](../start-monitor-campaigns.md)<br/><br/>[Reporting](../reporting-campaigns.md)|[Work with the Query Modeler](../orchestrated-rule-builder.md)<br/><br/>[Build your first query](../build-query.md)<br/><br/>[Edit expressions](../edit-expressions.md)|[Get started with activities](about-activities.md)<br/><br/>Activities:<br/>[And-join](and-join.md) - [Build audience](build-audience.md) - [Change dimension](change-dimension.md) - **[Channel activities](channels.md)** - [Combine](combine.md) - [Deduplication](deduplication.md) - [Enrichment](enrichment.md) - [Fork](fork.md) - [Reconciliation](reconciliation.md) - [Split](split.md) - [Wait](wait.md)|

{style="table-layout:fixed"}

+++

<br/>

[!DNL Adobe Journey Optimizer] allows you to automate and execute marketing campaigns across channels. You can combine channel activities into the orchestrated campaign canvas to create cross-channel orchestrated campaigns that can trigger actions based on customer behavior and data. 

For example, you can create a welcome email campaign that includes a series of messages across different channels, such as email, SMS, and push. You can also send a follow-up email after a customer has completed a purchase, or send a personalized birthday message to a customer via SMS. 

By using channel activities, you can create comprehensive and personalized campaigns that engage customers across multiple touchpoints and drive conversions. Supported channels are Email, SMS and Push. 

## Prerequisites {#channel-activity-prereq}

Start building your orchestrated campaign with the relevant activities:

* Before inserting a channel activity, you must define the audience. The audience is the main target of your delivery: the profiles who receive the messages. [Learn how to use the Build audience activity ](build-audience.md)

* To send a recurring delivery, start your orchestrated campaign with a **[!UICONTROL Scheduler]** activity. You can also use a **[!UICONTROL Scheduler]** activity for one-shot single deliveries to set the contact date for that delivery. That contact date can also be set in the delivery settings. [LEarn how to schedule an orchestrated camapign](../create-orchestrated-campaign.md#schedule)

## Configure a channel activity {#create-a-delivery-in-a-workflow}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_email"
>title="Email activity"
>abstract="The Email activity lets you send emails within your orchestrated campaign, both for both one-time and recurring messages. It serves to automate the process of sending emails to a target calculated within the same orchestrated campaign. You can combine channel activities into a multistep campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_sms"
>title="SMS activity"
>abstract="The SMS activity lets you send SMS within your orchestrated campaign, for both one-time and recurring messages. It serves to automate the process of sending SMS to a target calculated within the same orchestrated campaign. You can combine channel activities into the multistep campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_push"
>title="Push activity"
>abstract="The Push activity let you send Push notifications as part of your orchestrated campaign. It enables the delivery of both one-time and recurring orchestrated campaigns, automating the sending Push notifications to a predefined target within the same orchestrated campaign. You can combine channel activities into the campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

<!--
UNUSED IDs in BJ

>[!CONTEXTUALHELP]
>id="ajo_orchestration_push_ios"
>title="Push iOS activity"
>abstract="The Push iOS activity let you send iOS Push notifications as part of your orchestrated campaign. It enables the delivery of both one-time and recurring orchestrated campaigns, automating the sending iOS Push notifications to a predefined target within the same workflow. You can combine channel activities into the campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_push_android"
>title="Push Android activity"
>abstract="The Push Android activity ket you send Android Push notifications as part of your orchestrated campaign. It enables the delivery of both one-time and recurring messages, automating the sending Android Push notifications to a predefined target within the same orchestrated campaign. You can combine channel activities into the orchestrated campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

-->

>[!CONTEXTUALHELP]
>id="ajo_orchestration_directmail"
>title="Direct mail activity"
>abstract="The Direct mail activity facilitates direct mail sending within your orchestrated campaign, for both one-time and recurring messages. It serves to automate the process of generating the extraction file required by direct mail providers. You can combine channel activities into the orchestrated campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

To set up a delivery in the context of an orchestrated campaign, follow the steps below.

### Add a channel activity and define its properties {#add}

1. Add a channel activity into the canvas. Available channel activities are **[!UICONTROL Email]**, **[!UICONTROL SMS]** and **[!UICONTROL Push]**.

    ![image showing the canvas with available activities](../assets/channel-add.png)

1. Select the added activity and click the **[!UICONTROL Edit Email]**, **[!UICONTROL Edit SMS]**, or **[!UICONTROL Edit Push]** button depending on the chosen channel.

    ![image showing the canvas with an Email activity](../assets/channel-edit.png)

1. In the **[!UICONTROL Properties]** tab, enter a description for your campaign.

### Set up the channel configuation and settings {#configuration}

1. Select the **[!UICONTROL Actions]** tab and choose the channel configuration to use for your message.

    A configuration is defined by a [System Administrator](../../start/path/administrator.md). It contains all the technical parameters for sending the message, such as header parameters, subdomain, mobile apps, etc. [Learn how to set up channel configurations](../../configuration/channel-surfaces.md).

1. Depending on the channel, several options are available. Browse the tabs below for more information:

    >[!BEGINTABS]

    >[!TAB Email]

    Use the **[UICONTROL Track email opens]** and **[!UICONTROL Track clicks on links and buttons in email]** options to track how your recipients react to your delivery.
    
    Tracking results are accessible from the campaign report once the campaign has been executed. [Learn more about campaign reports](../reports/campaign-global-report-cja.md)

    >[!TAB SMS]

    Use the **[!UICONTROL Track clicks on links in SMS]** option to track clicks on links in your SMS.
    
    Tracking results are accessible from the campaign report once the campaign has been executed. [Learn more about campaign reports](../reports/campaign-global-report-cja.md)

    >[!TAB Push]

    Rapid delivery mode is a **[!DNL Journey Optimizer]** add-on that allows very fast push message sending in large volumes. 

    Enable the **[!UICONTROL Rapid delivery mode]** option to perform high speed message sending on Push channel to an audience size of under 30M. [Learn more](../push/create-push.md#rapid-delivery)

    >[!ENDTABS]

1. The **[!UICONTROL Content experiment]** section allows you to define multiple delivery treatments in order to measure which one performs best for your target audience.

    To do so, click the **[!UICONTROL Create experiment]** button then follow the steps detailed in this section: [Create a content experiment experimentation capabilities](../../content-management/content-experiment.md).

1. The **[!UICONTROL Languages]** section allows you to create content in multiple languages within your campaign.

    To do so, click the **[!UICONTROL Add languages]** button and select the desired **[!UICONTROL Language settings]**. Detailed information on how to set up and use multilingual capabilities are available in this section: [Get started with multilingual content](../../content-management/multilingual-gs.md)

### Define the content {#content}

Select the **[!UICONTROL Content]** tab to define the content of the message. The content creation process depends on the selected channel.

Learn detailed steps to create your message content in the following pages:

<table style="table-layout:fixed"><tr style="border: 0;">
<td><a href="../../email/create-email.md"><img alt="email" src="../../channels/assets/do-not-localize/email.png"></a>
<div align="center"><a href="../../email/create-email.md"><strong>Email</strong></a></div></td>
<td><a href="../sms/../create-sms.md"><img alt="sms" src="../../channels/assets/do-not-localize/sms.png"></a>
<div align="center"><a href="../../sms/create-sms.md"><strong>SMS</strong></a></div></td>
<td><a href="../push/create-push.md"><img alt="push" src="../../channels/assets/do-not-localize/push.png"></a>
<div align="center"><a href="../../push/create-push.md"><strong>Push notification</strong></a></div></td>
</tr></table>

Once your content is defined, use the **[!UICONTROL Simulate content]** button to preview and test your content with test profiles or sample input data uploaded from a CSV / JSON file, or added manually. [Learn more](../content-management/preview-test.md).

## Next steps {#next}

Navigate back to your orchestrated campaign using the **[!UICONTROL Back]** arrow.

![image showing the back button](../assets/channel-back.png)

You can now complete the activities orchestration in the canvas and publish the campaign to start the messages sending. [Learn how to start and monitor orchestrated campaigns](../start-monitor-campaigns.md)

<!--
## Examples {#cross-channel-workflow-sample}

Here is a cross-channel orchestrated campaign example with a segmentation and two deliveries. The orchestrated campaign targets all customers who live in Paris and who are interested in coffee machines. Among this population, an email is sent to the regular customers and an SMS is sent to the VIP clients.

![](../assets/workflow-channel-example.png)

<!--
description, which use case you can perform (common other activities that you can link before of after the activity)

how to add and configure the activity

example of a configured activity within a workflow
The Email delivery activity allows you to configure the sending an email in a workflow. 

-->

<!--You can also create a recurring orchestrated campaign to send a personalized SMS every first day of the month at 8 PM to all customers living in Paris.

![](../assets/workflow-channel-example2.png)-->

<!-- Scheduled emails available?

This can be a single send email and sent just once, or it can be a recurring email.
* Single send emails are standard emails, sent once.
* Recurring emails allow you to send the same email multiple times to different targets over a defined period. You can aggregate the deliveries per period in order to get reports that correspond to your needs.

When linked to a scheduler, you can define recurring emails.
Email recipients are defined upstream of the activity in the same workflow, via an Audience targeting activity.

-->


<!--The message preparation is triggered according to the workflow execution parameters. From the message dashboard, you can select whether to request or not a manual confirmation to send the message (required by default). You can start the workflow manually or place a scheduler activity in the workflow to automate execution.-->
