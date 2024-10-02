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

[!DNL Journey Optimizer] comes with built-in channel action capabilities. You can simply add, to your journey, an outbound (email, text message (SMS/MMS), push) or inbound (In-app, web, code-based experience, content card) activity, and define settings and content. It is then executed and sent in the context of the journey.

>[!NOTE]
>
>You can also set up specific actions to send you messages. [Learn more](#recommendation)

To add a built-in channel action to a journey, follow the steps below.

1. Start your journey with an [Event](general-events.md) or a [Read Audience](read-audience.md) activity.

1. From the **Actions** section of the palette, drag and drop an outbound (**email**, **push**, **SMS**) or inbound (**In-app**, **web**, **code-based experience**, **content card**) activity into the canvas.

   ![](assets/journey-web-activity.png)

1. Configure your activity.
   
   * Learn the detailed steps to create your message content as follows:

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
      >Each inbound message activity comes with a 3-days **Wait** activity. [Learn more](../building-journeys/wait-activity.md#auto-wait-node)

### Recommendation {#recommendation}

[!DNL Journey Optimizer] comes with built-in message capability. However, custom actions enable you to configure connection of a third-party system to send messages or API calls.

* If you are using a third-party system to send your messages, you can create a custom action. [Learn more](../action/action.md)

* If you are working with Campaign and Journey Optimizer, refer to these sections:

   * [[!DNL Journey Optimizer] and Campaign v7/v8](../action/acc-action.md)
   * [[!DNL Journey Optimizer] and Campaign Standard](../action/acs-action.md)

## Update live content{#update-live-content}

You can update the content of a built-in channel action in a live journey. 

To do this, open your live journey, select the channel activity and click **Edit content**.

![](assets/add-a-message2.png)

However, you cannot change the attributes used in personalization, whether they are profile attributes or contextual data (from event or journey properties).

If you modified contextual data, the following error message will be displayed: ERR_AUTHORING_JOURNEYVERSION_201

If you modified profile attributes, the following error message will be displayed: ERR_AUTHORING_JOURNEYVERSION_202

Note that for the In-app activity, any changes can be made to the content while the journey is live, but In-app triggers cannot be modified.

## Send-Time Optimization{#send-time-optimization}

>[!CONTEXTUALHELP]
>id="jo_bestsendtime_disabled"
>title="About Sent time optimization"
>abstract="Adobe Journey Optimizer's Send-Time Optimization feature, powered by Adobe's AI services, can predict the best time to send an email or push message to maximize engagement based on historical open and click rates."

>[!NOTE]
>
>This feature is not enabled by default. You can reach out to your Adobe representative to activate it.
>
>The Send-Time Optimization feature only applies to Email and Push channels.

### About Send-Time Optimization {#about-send-time}

Adobe Journey Optimizer's Send-Time Optimization feature, powered by Adobe's AI services, can predict the best time to send an **email** or **push message** to maximize engagement based on historical open and click rates. Use our machine-learning model to schedule personalized send times for each user to grow the open and click rates of your messages.

The Send-Time Optimization model ingests your Adobe Journey Optimizer data and looks at user-level open (for email and push) and click (for email) rates to determine when your customers are most likely to engage with your messaging. Send-Time Optimization requires a minimum of one month of message-tracking data to make informed recommendations. For each user, the system will automatically pick the best time using the following scores:

* The best hour of each day of the week to maximize engagement
* The best day of the week to maximize engagement
* The best hour of the best day of the week to maximize engagement

The model varies whether you are talking about scoring or training. Training is conducted weekly initially and then quarterly. Scoring is weekly initially and then monthly.

* Training - the development of the algorithm used to make the score
* Scoring - the application of a score to individual profiles based on the trained model

This information is stored with the user's profile and is referenced at journey execution to tell Adobe Journey Optimizer when to send your message. 

### Frequently-Asked-Questions {#faq-send-time}

+++ What can Send-Time Optimization do? How does it handle new profiles? Does it spread the send over a 6/12/24 hour window?

Send-Time Optimization tries to predict the best time to engage with customers and optimize open/click rates of emails. The score is in a format of `3*7*24` attributes for each profile. The `7*24` attributes describe the ranking of the predicted best time to send out emails to the recipient and 3 is for optimizing email open rate, email click rate and push open rate.

+++

+++Where can I see the expected send time for each profile?

You can see the overall score in the **Profiles** interface. For each of the three sets of 168 scores, the ranks go from -83 to 84. The higher the rank is, the better time was chosen to interact with the recipient. Since you can define the start and duration of a journey, the best rank (84) may not fall into that time window. In this case, we recommend choosing an hour with the highest rank value.

+++


+++What reporting is available?

Access your journey, click the **View report** button in the top right and select the **Journey** tab on the left. [Read more](../reports/journey-global-report.md)

+++

+++How does Send-Time Optimization data affect profile richness?

Send-Time Optimization adds the score/attributes to each profile but no new profile is created.

+++

### Activate Send-Time Optimization{#activate-send-time-optimization}

>[!CONTEXTUALHELP]
>id="jo_bestsendtime_email"
>title="Activate Send-Time Optimization"
>abstract="Choose whether to optimize on email opens or email click-throughs by selecting the appropriate radio button. You can also choose to bracket the send times used by the system by entering a value for the Send within the next option."

>[!CONTEXTUALHELP]
>id="jo_bestsendtime_push"
>title="Activate Send-Time Optimization"
>abstract="Push messages defaults to the opens option, as clicks are not applicable for push messaging. You can also choose to bracket the send times used by the system by entering a value for the Send within the next option."

Enable Send-Time Optimization on an email or push message by selecting the **Send-Time Optimization** switch from the activity parameters. 

![](../building-journeys/assets/jo-message5.png)

For email messages, choose whether to optimize on email opens or email click-throughs by selecting the appropriate radio button. Push messages defaults to the opens option, as clicks are not applicable for push messaging. 

You can also choose to bracket the send times used by the system by entering a value for the **Send within the next** option. If you choose "six hours" as the value, [!DNL Journey Optimizer] will check each user profile and pick the optimal send time within six hours from the journey execution time.

**What happens if the optimal time is outside the window?**

Let's take an example with the following setup:

* Optimize on clicks
* Action is meant to start at 10 AM
* Window is 3 hours

A profile can have an optimal open time which is outside the window. For example, John's optimal open on click is at 5 PM. 

At profile level, there are scores for every hour of the week. In this example, the email will always be sent within the window. At run time, the system checks the list of scores within that window (3 hour window starting at 10 AM). The system then compares the scores for 10, 11 and noon and selects the highest. The email is sent at that time.
