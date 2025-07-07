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


+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](../gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](../configuration-steps.md)<br/><br/>[Access and manage orchestrated campaigns](../access-manage-orchestrated-campaigns.md)|[Key steps to create an orchestrated campaign](../gs-campaign-creation.md)<br/><br/>[Create and schedule the campaign](../create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](../orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](../start-monitor-campaigns.md)<br/><br/>[Reporting](../reporting-campaigns.md)|[Work with the rule builder](../orchestrated-rule-builder.md)<br/><br/>[Build your first query](../build-query.md)<br/><br/>[Edit expressions](../edit-expressions.md)<br/><br/>[Retargeting](../retarget.md)|[Get started with activities](about-activities.md)<br/><br/>Activities:<br/>[And-join](and-join.md) - [Build audience](build-audience.md) - [Change dimension](change-dimension.md) - <b>[Channel activities](channels.md)</b> - [Combine](combine.md) - [Deduplication](deduplication.md) - [Enrichment](enrichment.md) - [Fork](fork.md) - [Reconciliation](reconciliation.md) - [Save audience](save-audience.md) - [Split](split.md) - [Wait](wait.md)|

{style="table-layout:fixed"}

+++


<br/>

[!DNL Adobe Journey Optimizer] allows you to automate and execute marketing campaigns across channels - email, SMS, and push notifications. You can combine these channel activities into the campaign canvas to create cross-channel orchestrated campaigns that can trigger actions based on customer behavior and data. 

For example:
* Send a welcome series through email, SMS, and push.
* Deliver a follow-up email post-purchase.
* Send personalized birthday greetings via SMS.

By using channel activities, you can create comprehensive and personalized campaigns that engage customers across multiple touchpoints and drive conversions.

>[!PREREQUISITES]
>
>Before adding a channel activity, define the target audience using a [Build audience activity](build-audience.md).

## Add a channel activity and define its properties {#add}

1. Add a channel activity into the canvas. Available channel activities are **[!UICONTROL Email]**, **[!UICONTROL SMS]** and **[!UICONTROL Push]**.

    ![image showing the canvas with available activities](../assets/channel-add.png)

1. Select the activity and click **[!UICONTROL Edit email]**, **[!UICONTROL Edit SMS]**, or **[!UICONTROL Edit Push]** depending on the chosen channel.

    ![image showing the canvas with an Email activity](../assets/channel-edit.png)

1. In the **[!UICONTROL Properties]** tab, enter a description then switch to the **[!UICONTROL Actions]** tab to configure the activity.

## Set up the channel configuation and settings {#configuration}

Use the **[!UICONTROL Actions]** tab to select a channel configuration for your message and configure additional settings such as tracking, content experiment, or multilingual content.

1. Select a channel configuration.

    A configuration is defined by a [System Administrator](../../start/path/administrator.md). It contains all the technical parameters for sending the message, such as header parameters, subdomain, mobile apps, etc. [Learn how to set up channel configurations](../../configuration/channel-surfaces.md).

    ![image showing the Actions section](../assets/channel-actions.png)

1. Track engagement (for Email and SMS).

    Use the **[!UICONTROL Action tracking]** section to track how your recipients react to your email or SMS deliveries. Tracking results are accessible from the campaign report once the campaign has been executed. [Learn more about campaign reports](../../reports/campaign-global-report-cja.md)

1. Enable Rapid delivery mode (for Push).

    Rapid delivery mode is a [!DNL Journey Optimizer] add-on that allows very fast push message sending in large volumes though campaigns. Rapid delivery is used when delay in message delivery is business-critical, when you want to send an urgent push alert on mobile phones, for example a breaking news to users who have installed your news channel app. For more information on performances when using Rapid delivery mode, refer to [Adobe Journey Optimizer product description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html).

1. Create a content experiment.

    Use the **[!UICONTROL Content experiment]** section to define multiple delivery treatments in order to measure which one performs best for your target audience. Click the **[!UICONTROL Create experiment]** button then follow the steps detailed in this section: [Create a content experiment](../../content-management/content-experiment.md).

1. Add multilingual content.

    Use the **[!UICONTROL Languages]** section to create content in multiple languages within your campaign. To do so, click the **[!UICONTROL Add languages]** button and select the desired **[!UICONTROL Language settings]**. Detailed information on how to set up and use multilingual capabilities are available in this section: [Get started with multilingual content](../../content-management/multilingual-gs.md)

    ![image showing the Content experiment section](../assets/channel-experiment.png)

When your channel activity has been configured, select the **[!UICONTROL Content]** tab to define its content.

## Define the content {#content}

Switch to the **[!UICONTROL Content]** tab to create your message. The steps process vary based on the selected channel. Learn detailed steps to create your message content in the following pages.

<table style="table-layout:fixed"><tr style="border: 0; text-align: center;" >
<td><a href="../../email/create-email.md"><img alt="email" src="../../channels/assets/do-not-localize/email.png"></a><br/><a href="../../email/create-email.md"><strong>Create an email</strong></a></td>
<td><a href="../../sms/create-sms.md"><img alt="sms" src="../../channels/assets/do-not-localize/sms.png"></a><br/><a href="../../sms/create-sms.md"><strong>Create a SMS</strong></a></td>
<td><a href="../../push/create-push.md"><img alt="push" src="../../channels/assets/do-not-localize/push.png"></a><a href="../../push/create-push.md"><strong>Create a push notification</strong></a></td>
</tr></table>

Once the content is created, use the **[!UICONTROL Simulate Content]** button to preview and test your content with test profiles or sample input data uploaded from a CSV / JSON file, or added manually. [Learn more](../../content-management/preview-test.md)

![image showing the Simulate Content button](../assets/channel-simulate.png)

## Next steps {#next}

When the message content is ready, navigate back to your orchestrated campaign using the **[!UICONTROL Back]** arrow. You can then complete the activities orchestration in the canvas and publish the campaign to start the messages sending. [Learn how to start and monitor orchestrated campaigns](../start-monitor-campaigns.md)

![image showing the back button](../assets/channel-back.png)

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
