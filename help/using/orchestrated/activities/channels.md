---
solution: Journey Optimizer
product: journey optimizer
title: Add a channel activity in a multistep campaign
description: Learn how to add a channel activity in a multistep campaign
exl-id: ffe1e77c-6c4f-4f23-9183-d715a4c7c402
version: Campaign Orchestration
TQID: https://experienceleague.adobe.com/ouwufvPEUXGewSP5TvsfI0qPxpVqaqso3me4qEc2WQM
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
subfeature_v2:
  - id: b5e335a9-0e5f-4dda-8845-c4ac5dca2be4
    internal-label: Orchestration activities
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Channel activities {#channel}

>[!BEGINSHADEBOX]

**On this page:** Learn how to add and configure email, SMS, push, and direct mail channel activities to send marketing or transactional messages within an Orchestrated campaign.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_orchestration_email"
>title="Email activity"
>abstract="The Email activity lets you send emails within your Orchestrated campaign, for both one-time and recurring messages. It serves to automate the process of sending emails to a target calculated within the same Orchestrated campaign. You can combine channel activities into a multistep campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_sms"
>title="SMS activity"
>abstract="The SMS activity lets you send SMS within your Orchestrated campaign for both one-time and recurring messages. It serves to automate the process of sending SMS to a target calculated within the same Orchestrated campaign. You can combine channel activities into the multistep campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_push"
>title="Push activity"
>abstract="The Push activity lets you send Push notifications as part of your Orchestrated campaign. It enables the delivery of both one-time and recurring Orchestrated campaigns, automating the sending of Push notifications to a predefined target within the same Orchestrated campaign. You can combine channel activities into the campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_target"
>title="Target"
>abstract="The **[!UICONTROL Target]** section sets the target of the delivery for this channel activity. Use **[!UICONTROL Target dimension]** to select which target dimension applies to this send. Then choose **[!UICONTROL One message per profile]** to send a single message per person, or **[!UICONTROL One message per secondary dimension]** to send one message per qualifying secondary dimension — for example, one email per flight when the same traveler has several matching flights."


>[!CONTEXTUALHELP]
>id="ajo_orchestration_line"
>title="Line activity"
>abstract="The **Line** activity lets you add a LINE action to your Orchestrated campaign. Build personalized content, from text and stickers to images, videos, locations, and Flex Messages, to engage customers on LINE."


<!--
UNUSED IDs in BJ

>[!CONTEXTUALHELP]
>id="ajo_orchestration_push_ios"
>title="Push iOS activity"
>abstract="The Push iOS activity lets you send iOS Push notifications as part of your Orchestrated campaign. It enables the delivery of both one-time and recurring Orchestrated campaigns, automating the sending of iOS Push notifications to a predefined target within the same workflow. You can combine channel activities into the campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_push_android"
>title="Push Android activity"
>abstract="The Push Android activity lets you send Android Push notifications as part of your Orchestrated campaign. It enables the delivery of both one-time and recurring messages, automating the sending of Android Push notifications to a predefined target within the same Orchestrated campaign. You can combine channel activities into the Orchestrated campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."
-->

>[!CONTEXTUALHELP]
>id="ajo_orchestration_directmail"
>title="Direct mail activity"
>abstract="The Direct mail activity facilitates direct mail sending within your Orchestrated campaign, for both one-time and recurring messages. It serves to automate the process of generating the extraction file required by direct mail providers. You can combine channel activities into the Orchestrated campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data."

>[!CONTEXTUALHELP]
>id="ajo_orchestration_custom"
>title="Custom channel activity"
>abstract="The Custom channel activity lets you send messages through third-party systems or custom integrations within your Orchestrated campaign. It enables you to trigger external delivery processes — such as partner platforms or proprietary messaging tools — by exporting audience data to an external system. You can combine custom channel activities with other channel activities in the campaign canvas to create cross-channel campaigns that engage customers across both native and custom touchpoints."

[!DNL Adobe Journey Optimizer] allows you to automate and execute campaigns across channels—email, SMS, push notifications, direct mail, and custom—for both marketing and transactional messages. You can combine these channel activities into the campaign canvas to create cross-channel Orchestrated campaigns. These campaigns can trigger actions based on customer behavior and data.

For example:

* Send a welcome series through email, SMS, push and direct mail.
* Deliver a follow-up email post-purchase.
* Send personalized birthday greetings via SMS.
* Trigger a message through a custom channel when a customer abandons their shopping cart.

By using channel activities, you can create comprehensive and personalized campaigns that engage customers across multiple touchpoints and drive conversions.

## Guardrails and limitations {#channel-guardrails}

* **Supported channels** - Only SMS, Push, Email and Direct mail channels are supported in Orchestrated campaigns.

* **Channel activities limit** - An Orchestrated campaign supports a maximum of 10 channel activities (Email, SMS, Push, or Direct mail). Only channel activities count toward this limit, targeting and flow control activities do not.

    If you exceed the limit when saving or publishing, the operation fails. To stay within the limit, reduce the number of channel activities or split message delivery across multiple Orchestrated campaigns.

See [Guardrails and limitations](../guardrails.md) for all Orchestrated campaign guardrails and limitations.

## Add a channel activity and define its properties {#add}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_category"
>title="Category"
>abstract="Choose Marketing or Transactional for this channel activity. Marketing messages use marketing channel configurations and follow your standard business rules. Transactional messages are for operational communications — often triggered by an individual's action (for example, a password reset or purchase confirmation) or for time-sensitive notices such as disruptions or cancellations. They use transactional channel configurations, business rules are bypassed, and opt-in is not required."

>[!PREREQUISITES]
>
>Before adding a channel activity, define the target audience using a [Build audience](build-audience.md) or a [Read audience](read-audience.md) activity.

1. Add a channel activity into the canvas. Available channel activities are **[!UICONTROL Email]**, **[!UICONTROL SMS]**, **[!UICONTROL Push]** and **[!UICONTROL Direct mail]**.

    ![image showing the canvas with available activities](../assets/channel-add.png)

1. In the right rail, use the **[!UICONTROL Category]** field to choose **[!UICONTROL Marketing]** or **[!UICONTROL Transactional]** for this message. Transactional messages do not require opt-in and are suited for time-sensitive communications such as disruptions, emergencies, or cancellations.

1. Select the activity and click **[!UICONTROL Edit email]**, **[!UICONTROL Edit SMS]**, **[!UICONTROL Edit Push]**, or **[!UICONTROL Edit direct mail]** depending on the chosen channel.

    ![image showing the canvas with an Email activity](../assets/channel-edit.png)

1. In the **[!UICONTROL Properties]** tab, enter a description then switch to the **[!UICONTROL Actions]** tab to configure the activity.

## Marketing vs Transactional messages {#marketing-vs-transactional}

Choosing the right category determines how messages are delivered and which rules apply:

| | Marketing | Transactional |
| --- | --- | --- |
| **Opt-in required** | Yes | No |
| **Business rules** | Applied (frequency capping, fatigue rules) | Bypassed |
| **Channel configuration type** | Marketing channel configuration | Transactional channel configuration |
| **Typical use cases** | Promotions, newsletters, seasonal campaigns | Order confirmations, password resets, disruption alerts |
| **Audience** | Opted-in subscribers only | Any profile, regardless of opt-in status |

>[!NOTE]
>
>Use Transactional only for operational or time-sensitive communications. Misclassifying a promotional message as Transactional bypasses consent and business rules, which may violate regulatory requirements.

## Set up the channel configuration and settings {#configuration}

Use the **[!UICONTROL Actions]** tab to select a channel configuration for your message and configure additional settings such as tracking, content experiment, or multilingual content.

1. **Select a channel configuration**

    A configuration is defined by a [System Administrator](../../start/path/administrator.md). It contains all the technical parameters for sending the message, such as header parameters, subdomain, mobile apps, etc. [Learn how to set up channel configurations](../../configuration/channel-surfaces.md)

    ![image showing the Actions section](../assets/channel-actions.png)

1. **Apply capping rules**

    In the **[!UICONTROL Rule set]** drop-down list, select a channel rule set to apply capping rules to your campaign. Leveraging channel rule sets allows you to set frequency capping by communication type to prevent overloading customers with similar messages. [Learn how to work with rule sets](../../conflict-prioritization/rule-sets.md).

1. **Create a content experiment**

    Use the **[!UICONTROL Content experiment]** section to define multiple delivery treatments in order to measure which one performs best for your target audience. Click the **[!UICONTROL Create experiment]** button then follow the steps detailed in this section: [Create a content experiment](../../content-management/content-experiment.md).

1. **Add multilingual content**

    Use the **[!UICONTROL Languages]** section to create content in multiple languages within your campaign. To do so, click the **[!UICONTROL Add languages]** button and select the desired **[!UICONTROL Language settings]**. Detailed information on how to set up and use multilingual capabilities are available in this section: [Get started with multilingual content](../../content-management/multilingual-gs.md).

    ![image showing the Content experiment section](../assets/channel-experiment.png)

Additional settings are available depending on the selected communication channel. Expand the sections below for more information.

+++**Track engagement** (Email and SMS).

Use the **[!UICONTROL Action tracking]** section to track how your recipients react to your email or SMS deliveries. Tracking results are accessible from the campaign report once the campaign has been executed. [Learn more about campaign reports](../../reports/campaign-global-report-cja.md)

+++

+++**Enable Rapid delivery mode** (Push).

Rapid delivery mode is a [!DNL Journey Optimizer] add-on that allows very fast push message sending in large volumes through campaigns. Rapid delivery is used when delay in message delivery is business-critical. For instance, you want to send an urgent push alert on mobile phones, such as breaking news to users who have installed your news channel app. Learn how to enable Rapid delivery mode for Push notifications [on this page](../../push/create-push.md#rapid-delivery).

For more information on performance when using Rapid delivery mode, refer to [Adobe Journey Optimizer product description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"}.

+++

When your channel activity has been configured, select the **[!UICONTROL Content]** tab to define its content.

## Define the content {#content}


### Create the message content

Switch to the **[!UICONTROL Content]** tab to create your message. The process steps vary based on the selected channel. Learn detailed steps to create your message content in the following pages.

<table style="table-layout:fixed"><tr style="border: 0; text-align: center;" >
<td><a href="../../email/create-email.md"><img alt="email" src="../../channels/assets/do-not-localize/email.png"></a><br/><a href="../../email/create-email.md"><strong>Create an email</strong></a></td>
<td><a href="../../mobile/create-mobile-message.md"><img alt="sms" src="../../channels/assets/do-not-localize/sms.png"></a><br/><a href="../../mobile/create-mobile-message.md"><strong>Create an SMS</strong></a></td>
<td><a href="../../push/create-push.md"><img alt="push" src="../../channels/assets/do-not-localize/push.png"></a><a href="../../push/create-push.md"><strong>Create a push notification</strong></a></td><td><a href="../../direct-mail/create-direct-mail.md"><img alt="direct mail" src="../../channels/assets/do-not-localize/direct-mail.jpg"></a><a href="../../direct-mail/create-direct-mail.md"><strong>Create a direct mail</strong></a></td><td><a href="../../custom-channel/create-custom-channel.md"><img alt="custom channel" src="../../channels/assets/do-not-localize/web.jpg"></a><br/><a href="../../custom-channel/create-custom-experience.md"><strong>Create a custom action</strong></a></td><td><a href="../../line/get-started-line.md"><img alt="line" src="../../channels/assets/do-not-localize/line.jpg"></a><br/><a href="../../line/get-started-line.md"><strong>Create a LINE message (LA)</strong></a></td></tr></table>

### Add personalization {#add-personalization}

From the message editor on a channel activity, insert **[!UICONTROL Profile attributes]** and **[!UICONTROL Target attributes]** from the campaign worktable (targeting dimension and enrichment data).

➡️ [Learn how to add personalization in Orchestrated campaigns](../add-personalization.md), including enrichment collection arrays, array functions, and `{{#each}}` iteration.

### Check and test your content {#simulate-content-test-profiles}

Once the content is created, you can preview and test it using either simulation method:

* Click **[!UICONTROL Simulate content]** to test content variations with sample input data or AI auto-generation. [Learn how to simulate content variations](../../test-approve/simulate-sample-input.md)
* Click **[!UICONTROL Simulate content]**, then select **[!UICONTROL Simulate content (AEP profiles)]** from the dropdown to preview and test your content with test profiles. [Learn more](../../content-management/preview-test.md)

![image showing the Simulate Content button](../assets/channel-simulate.png)

When you simulate content with **test profiles** in an Orchestrated campaign, two important constraints apply:

* **Execution must have reached the channel activity in test** - Run the campaign in test using the **[!UICONTROL Start]** button so the workflow reaches the channel activity you want to simulate. In test mode, the workflow pauses at the channel activity, so a channel activity that comes after another channel activity is never reached. You cannot use **[!UICONTROL Simulate Content]** for those downstream channel activities. See [Test your campaign before publishing](../start-monitor-campaigns.md#test).

* **The test profile must match the channel activity target** - Use a test profile that belongs to the audience targeted by that channel activity. If the profile is not in that audience, selecting it will not render a preview of your content. See [Select test profiles](../../content-management/test-profiles.md).

## Confirm message sending

By default, for non-recurring orchestrated campaigns, message delivery is paused until you explicitly approve the send. After publishing the campaign, confirm the send request from the channel activity's properties pane.

![image showing the Confirm button](../assets/confirm-sending.png)

Sending confirmation can be disabled before publishing the orchestrated campaign. To do so, select the channel activity in the canvas to display its properties, and turn on **[!UICONTROL Send without confirmation]**.

![image showing the Send without confirmation button](../assets/send-without-confirmation.png)

## Set rate control {#rate-control}

[!DNL Journey Optimizer] allows you to enable rate control for outbound actions in Orchestrated campaigns.

This feature is particularly useful for preventing overload on downstream systems, such as landing pages or customer care platforms. For example, you can set a rate limit of 165 messages per second to ensure steady delivery without overwhelming downstream systems.

To set rate control, follow these steps:

1. Select an outbound channel activity in the canvas and click **[!UICONTROL Edit email]**, **[!UICONTROL Edit SMS]**, or **[!UICONTROL Edit Push]** depending on the chosen channel.

    ![image showing the canvas with an Email activity](../assets/channel-edit.png)

1. Navigate to the **[!UICONTROL Schedule]** tab, and enable the **[!UICONTROL Throttle delivery]** option in the **[!UICONTROL Delivery settings]** section.

    ![Rate control settings with throttle delivery option and delivery rate per second](../assets/rate-control.png)

1. Specify the desired **[!UICONTROL Delivery rate]** per second.

    * Minimum delivery rate supported: 1 per second.
    * Maximum delivery rate supported: 2000 per second when the "Throttle delivery" option is enabled.

>[!IMPORTANT]
>
>When setting a delivery rate, the maximum timeframe for which a campaign audience can execute is 12 hours. If the delivery rate is set to a value that does not allow all the audience to be sent the message in the 12-hour timeframe, then the remaining profiles will be excluded from the campaign. You can see the count of these excluded profiles in the campaign report.

<!--
## Example: cross-channel campaign with a custom channel {#example-custom}

The following example shows an Orchestrated campaign that combines native and custom channels to re-engage lapsed customers.

The campaign targets customers who have not made a purchase in the last 90 days:

1. A **Build audience** activity filters profiles with no purchase in the last 90 days.
1. A **Split** activity divides the audience into two groups:
   * **Group A** — customers with a known email address receive a re-engagement email with a personalized discount offer.
   * **Group B** — customers without an email address, or those who did not open the email after 3 days, are routed to a **Custom channel** activity that triggers a message through a third-party messaging platform (for example, a WhatsApp Business provider or an in-house notification system).
1. Both branches converge on a **Wait** activity, then a follow-up **SMS** is sent to all profiles who still have not converted.

This pattern lets you extend your campaign reach beyond native channels and engage customers on the platforms they are most active on, without requiring a separate campaign workflow.
-->

## Next steps {#next}

When the message content is ready, navigate back to your Orchestrated campaign using the **[!UICONTROL Back]** arrow. You can then complete the activities orchestration in the canvas and publish the campaign to start sending messages. [Learn how to start and monitor Orchestrated campaigns](../start-monitor-campaigns.md)

![image showing the back button](../assets/channel-back.png)

<!--
## Examples {#cross-channel-workflow-sample}

Here is a cross-channel Orchestrated campaign example with a segmentation and two deliveries. The Orchestrated campaign targets all customers who live in Paris and who are interested in coffee machines. Among this population, an email is sent to the regular customers and an SMS is sent to the VIP clients.

![](../assets/workflow-channel-example.png)

<!--
description, which use case you can perform (common other activities that you can link before of after the activity)

how to add and configure the activity

example of a configured activity within a workflow
The Email delivery activity allows you to configure the sending an email in a workflow. 
-->

<!--
You can also create a recurring Orchestrated campaign to send a personalized SMS every first day of the month at 8 PM to all customers living in Paris.

![](../assets/workflow-channel-example2.png)
-->

<!--
 Scheduled emails available?

This can be a single send email and sent just once, or it can be a recurring email.
* Single send emails are standard emails, sent once.
* Recurring emails allow you to send the same email multiple times to different targets over a defined period. You can aggregate the deliveries per period in order to get reports that correspond to your needs.

When linked to a scheduler, you can define recurring emails.
Email recipients are defined upstream of the activity in the same workflow, via an Audience targeting activity.
-->


<!--The message preparation is triggered according to the workflow execution parameters. From the message dashboard, you can select whether to request or not a manual confirmation to send the message (required by default). You can start the workflow manually or place a scheduler activity in the workflow to automate execution.-->

