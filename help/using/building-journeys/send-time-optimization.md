---
solution: Journey Optimizer
product: journey optimizer
title: Send time optimization
description: Learn how to parameter send time optimization in your messages
feature: Journeys, Activities, Email, Push, Send Time Optimization
topic: Content Management
role: User
level: Intermediate
keywords: send-time, send, message, optimization, journey, AI, Intelligent
exl-id: ec604e91-4c7f-459c-b6ff-d825919e7181
---
# Send-Time Optimization{#send-time-optimization}

>[!CONTEXTUALHELP]
>id="jo_bestsendtime_disabled"
>title="About Sent time optimization"
>abstract="Adobe Journey Optimizer's Send-Time Optimization feature, powered by Adobe's AI services, can predict the best time to send an email or push message to maximize engagement based on historical open and click rates."

>[!CONTEXTUALHELP]
>id="jo_bestsendtime_disabled"
>title="About Sent time optimization"
>abstract="Adobe Journey Optimizer's Send-Time Optimization feature, powered by Adobe's AI services, can predict the best time to send an email or push message to maximize engagement based on historical open and click rates."

>[!CONTEXTUALHELP]
>id="jo_bestsendtime_email"
>title="Activate Send-Time Optimization"
>abstract="Choose whether to optimize on email opens or email click-throughs by selecting the appropriate radio button. You can also choose to bracket the send times used by the system by entering a value for the Send within the next option."

>[!CONTEXTUALHELP]
>id="jo_bestsendtime_push"
>title="Activate Send-Time Optimization"
>abstract="Push messages defaults to the opens option, as clicks are not applicable for push messaging. You can also choose to bracket the send times used by the system by entering a value for the Send within the next option."


Adobe Journey Optimizer's Send-Time Optimization feature, powered by Adobe's Journey AI services, chooses the optimal send time for email and push messages to maximize customer engagement, based on your customers' historical open and click behavior.

Send-Time Optimization is only available for Journey Optimizer's built-in Email and Push action types and is not currently available for messages sent through custom actions or for other action types. Send-Time Optimization is only available for Email and Push actions within Journeys and is not currently available for messages sent through Campaigns.

>[!AVAILABILITY]
>
>* At least 1,000 profiles with recent messaging data is recommended for initial Send-Time Optimization training and scoring.
>
>* Send-Time Optimization only applies to **Email** and **Push notification** channels.

## Enable Send-Time Optimization{#enable-send-time-optimization}

The Send-Time Optimization feature is enabled for Adobe Journey Optimizer customers upon request. Contact Adobe Customer Care or your Adobe representative to activate the feature for your organization.

## Use Send-Time Optimization{#use-send-time-optimization}

Use Send-Time Optimization on an email or push action by turning on the Send-Time Optimization switch from the action parameters.

![](assets/sto-use.png)

>[!TIP]
>
>Send-Time Optimization should not be used for urgent, time-sensitive operational messages – for example, an order confirmation, a password reset notification, or a flight gate change notification. Send-Time Optimization is best used on less-urgent marketing communications – for example, a weekly ad, promotional information on a new product, or information about a month-long sale.

For email messages, choose whether to optimize on email opens or email click-throughs by selecting the appropriate radio button. Push messages are always optimized for opens.

>[!TIP]
>
>For the best results, most email messages should be optimized for Clicks. Choose to optimize for Opens if your email message is informational in nature and not intended to directly drive an action.

For both email and push messages, choose the maximum number of hours that the system will wait before sending the message by setting a value for the "Send within the next" option. You may choose a value from 1 to 168 hours.

>[!TIP]
>
>For the best results, choose a maximum wait time between 6 and 24 hours. Choosing a lower value for maximum wait time reduces the number of available send times and therefore may reduce the potential value of Send-Time Optimization. Choosing a higher value for maximum wait time may result in a message being outdated or irrelevant by the time it is sent.

When your journey is activated and a customer reaches the Email or Push action in the journey, Send-Time Optimization will choose the best predicted send time available for each user within your specified limits.


## How Send-Time Optimization works {#how-send-time}

The Send-Time Optimization model ingests your organization's Adobe Journey Optimizer customer behavior data and looks at user-level open and click events to determine when your customers are most likely to engage with your messaging.

Send-Time Optimization makes predictions for each hour of the week, for each user, based on three types of behavioral data:

1. The behavior of your users overall
1. The behavior of lookalike users in the same time zone
1. The behavior of that individual user

These predictions are weighted and combined using a Bayesian approach, resulting in a "heat map" for each metric (email opens, email clicks, and push opens), for each customer, that indicates the hours of the week that contacting that user is most and least likely to result in the desired engagement outcome (open/click), as illustrated in the below example heatmap:

![](assets/heatmap-1.png)

If a user with the above predicted probabilities is targeted for a message at 9 AM Wednesday with Send-Time Optimization turned on and a 7 hour maximum wait time, the selected send time for the message will be 12 PM:

![](assets/heatmap-2.png)

## Send-Time Optimization model training and scoring details  {#model-send-time}

Once the Send-Time Optimization feature is enabled for your organization, the Journey AI model is trained on email and push send, open and click events across all your organization's journeys and actions over the last 16 weeks – regardless of whether those actions use Send-Time Optimization. This allows Send-Time Optimization to benefit from all data generated by your customers.

Models are initially trained and scored weekly. After 16 weeks, models are retrained and rescored monthly. Model scoring includes all customer profiles – both existing and new since the last scoring run.

Messages sent by Send-Time Optimization receive either an "exploration" message send time selected to test different send times and observe how customers respond, or an "optimized" message send times selected to maximize click/open rates. 5% of send events receive an "exploration" send time and 95% of send events are "optimized".

Exploration send times are selected at random from the send times made available by your configured maximum wait time. For example, in the case that a message is selected at 9 AM Wednesday with Send-Time Optimization turned on and a 3 hour maximum wait time, Exploration send times for the message will be split evenly between 9 AM, 10 AM, 11 AM and 12 PM.


## Frequently Asked Questions {#faq-send-time}

+++How long do I need to wait before using Send-Time Optimization?

Your organization should use the Email action within Journey Optimizer for a minimum of 30 days before using Send-Time Optimization within Email to allow for the collection of some email send, open, and click events.

Your organization should use the Push action within Journey Optimizer for a minimum of 30 days before using Send-Time Optimization within Push to allow for the collection of some push send and open events.

If your organization has already been using the Email and/or Push action types for at least 30 days, your organization does not need to wait longer to use Send-Time Optimization after it has been enabled by Adobe. Results will continue to improve as your organization gathers data for up to 16 weeks.

+++

+++How can I see the send time a particular user will receive a message at?

In order to minimize the model's impact on profile richness, model scores are stored compressed in 3 Profile attributes stored in `_experience.intelligentServices.journeyAI.sendTimeOptimization`, and are not designed to be human readable.

+++


+++What is the average benefit of Send-Time Optimization?

Send-Time Optimization may increase email click rate and push open rate in the range of approximately 2% to 10% across all messages optimized by an organization.

For example, if an organization sending email without send time optimization has a 5.0% click rate on average, the same set of emails with send time optimization might result in as much as a 5.5% click rate on average (5.0% * (1+10%) = 5.5%).

Due to variability within small sample sizes, a benefit from Send-Time Optimization may not be observable on single message sends.

Organizations are more likely to experience greater benefits from using Send-Time Optimization when:

* Existing journeys use send times that are fixed and not well-optimized
* Variability in customer behavior (clicks and opens) corresponds to customer location and customer preferences
* Organizations use Send-Time Optimization on a larger fraction of email & push messages
* Organizations choose maximum wait times within the recommended range of 6-12 hours

+++

+++I always click on emails or push messages at 12pm, why didn't the algorithm send a message to me at 12pm?


This may occur for multiple reasons:

* Your message was selected as an "Exploration" message send time instead of an "Optimized" message send time.
* The behavior of lookalike users influenced the model to recommend another send time.

+++

+++How does Send-Time Optimization know a user's time zone?

Send-Time Optimization uses the `timeZone` profile field to determine a user's time zone. If not available for that user, Send-Time Optimization attempts to infer a user's time zone from other geographic information in the user's profile such as country and state.

+++


+++Will Send-Time Optimization send Push messages to users during the night in their local time zone?

Send-Time Optimization may send Push messages to users during the night in their local time zone in the following circumstances:

* When users exhibit behavior that indicates they are likely to interact with a message sent at night
* When the model chooses an "Exploration" send time

To avoid sending Push messages to customers during night time hours, schedule batch Push message sends to occur in the morning or early afternoon and choose a shorter duration for Send-Time Optimization. (For example, a 9 AM send time and 8 hour maximum wait time.)

+++



