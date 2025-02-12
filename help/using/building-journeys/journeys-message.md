---
solution: Journey Optimizer
product: journey optimizer
title: Add a built-in channel action to a journey
description: Learn how to add a built-in channel action to a journey
feature: Journeys, Activities, Channels Activity
topic: Content Management
role: User
level: Intermediate
keywords: journey, message, push, sms, email, in-app, web, content card, code-based experience
exl-id: 4db07a9e-c3dd-4873-8bd9-ac34c860694c
---
# Use built-in channel actions {#add-a-message-in-a-journey}

>[!CONTEXTUALHELP]
>id="ajo_message_activity"
>title="Built-in channel action"
>abstract="Journey Optimizer comes with built-in channel action capabilities. You can simply add, to your journey, an outbound (email, text message (SMS/MMS), push) or inbound (In-app, web, code-based experience, content card) activity, and define settings and content. It is then executed and sent in the context of the journey."

[!DNL Journey Optimizer] comes with built-in channel action capabilities which are used to send messages: when a profile enters this activity, a message is sent to them. 

To add a built-in channel action to your journey, drag and drop a channel activity, and define its settings and content. It is then executed and sent in the context of the journey.

>[!NOTE]
>
>You can also set up custom actions to send you messages. [Learn more](#recommendation)

## Add a message in a journey  {#add-msg-in-journey}

With built-in channel actions, you can configure outbound or inbound messages. Supported inbound channels are email, text message (SMS/MMS), push notifications. Supported outbound channels are In-app, web, code-based experience, content card. 

To add a built-in channel action to a journey, follow the steps below.

1. Start your journey with an [Event](general-events.md) or a [Read Audience](read-audience.md) activity.

1. From the **Actions** section of the palette, drag and drop a channel activity into the canvas.

   ![](assets/journey-web-activity.png)


1. Configure your activity. Detailed configuration guidelines are available in the links below.
   
   * Learn the detailed steps to create your outbound action as follows:

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
      <a href="../push/create-push.md"><strong>Create push notifications<strong></a>
      </div>
      <p>
      </td>
      <td>
      <a href="../sms/create-sms.md">
      <img alt="Validation" src="../assets/do-not-localize/sms.jpg">
      </a>
      <div>
      <a href="../sms/create-sms.md"><strong>Create text messages (SMS/MMS)</strong></a>
      </div>
      <p>
      </td>
      </tr>
      </table>

      >[!NOTE]
      >
      >For emails and push notifications, you can enable Send-Time Optimization. [Learn more](send-time-optimization.md)

   * Learn the detailed steps to create your inbound action as follows:

      <table style="table-layout:fixed">
      <tr style="border: 0;">
      <td>
      <a href="../in-app/create-in-app.md">
      <img alt="Lead" src="../assets/do-not-localize/in-app.jpg">
      </a>
      <div><a href="../in-app/create-in-app.md"><strong>Create In-app messages</strong>
      </div>
      <p>
      </td>
      <td>
      <a href="../web/create-web.md">
      <img alt="Lead" src="../assets/do-not-localize/web-create.jpg">
      </a>
      <div><a href="../web/create-web.md"><strong>Create web experiences</strong>
      </div>
      <p>
      </td>
      <td>
      <a href="../content-card/create-content-card.md">
      <img alt="Lead" src="../assets/do-not-localize/sms-config.jpg">
      </a>
      <div><a href="../content-card/create-content-card.md"><strong>Create content cards</strong>
      </div>
      <p>
      </td>
      <td>
      <a href="../code-based/create-code-based.md">
      <img alt="Infrequent" src="../assets/do-not-localize/web-design.jpg">
      </a>
      <div>
      <a href="../code-based/create-code-based.md"><strong>Create code-based experiences<strong></a>
      </div>
      <p>
      </td>
      </tr>
      </table>

      >[!NOTE]
      >
      >Each inbound message activity comes with a 3-days **Wait** activity. [Learn more](wait-activity.md#auto-wait-node)


## Update a live content {#update-live-content}

You can update the content of a built-in channel action in a live journey.

To do this, open your live journey, select the channel activity and click **Edit content**.

![](assets/add-a-message2.png)

However, you cannot change the attributes used in personalization, whether they are profile attributes or contextual data (from event or journey properties).

If you modified contextual data, the following error message will be displayed: `ERR_AUTHORING_JOURNEYVERSION_201`

If you modified profile attributes, the following error message will be displayed: `ERR_AUTHORING_JOURNEYVERSION_202`

Note that for the In-app activity, any changes can be made to the content while the journey is live, but In-app triggers cannot be modified.

## Send with custom actions {#recommendation}

Instead of using the built-in message capabilities, you can use custom actions to configure connection of a third-party system to send messages or API calls.

* If you are using a third-party system to send your messages, you can create a custom action. [Learn more](../action/action.md)

* If you are working with Adobe Campaign, refer to these sections:

   * [[!DNL Journey Optimizer] and Campaign v7/v8](../action/acc-action.md)
   * [[!DNL Journey Optimizer] and Campaign Standard](../action/acs-action.md)