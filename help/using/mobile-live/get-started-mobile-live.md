---
solution: Journey Optimizer
product: journey optimizer
title: Get started with Live activities
description: Learn how to send Live activities in Journey Optimizer
topic: Content Management
role: User
level: Beginner
exl-id: c9766603-df19-4efd-8319-27e9764254b4
---
# Get started with Live activities {#get-started-mobile-live}


Live activities are persistent, glanceable UI elements displayed on the device lock screen. They let your app present real-time, up-to-date information — keeping users informed throughout an ongoing event without requiring them to open the app or receive repeated push notifications.

>[!AVAILABILITY]
>
>Live activities in Adobe Journey Optimizer are only compatible with Apple iOS.

Unlike traditional push notifications, Live activities represent **state-based engagement**: instead of delivering one-time alerts, they maintain a continuous, contextual presence that updates dynamically as events evolve.


<table style="table-layout:fixed"><tr style="border: 0;">
<td>
<img alt="iOS Live activities on Lock Screen and Dynamic Island" src="assets/do-not-localize/live-activity.jpeg">
</td>
<td>
<p><strong>Key benefits</strong></p>
<p>Live activities shift mobile engagement from notification-based to state-based, enabling brands to:</p>
<ul>
<li>Maintain a <strong>continuous presence</strong> on the Lock Screen throughout high-value events</li>
<li><strong>Update information dynamically</strong> without overwhelming users with repeated notifications</li>
<li>Deliver <strong>richer, more contextual</strong> mobile moments tied to real-world events</li>
<li><strong>Increase engagement and retention</strong> during active transactions or live experiences</li>
</ul>
</td>
</tr>
</table>

With Adobe Journey Optimizer, you can remotely **start**, **update**, and **end** Live activities programmatically through API-triggered campaigns — supporting both individual and audience-based use cases at scale.

Live activities can **only** be initiated via **API-triggered** campaigns, allowing you to provide custom payloads and perform all personalization through your own payload.
The appropriate **API-triggered** campaign type must be selected based on the intended Live activity use case:

* Select **API-triggered Marketing** for broadcast use cases — audience-based updates sent at scale:

    * Sports scores and live event countdowns
    * Flight status updates for all passengers on a route
    * Shared experiences across a user segment

* Select **API-triggered Transactional** for individual use cases — 1:1 real-time updates per user:

    * Order tracking and delivery progress
    * Ride or service status updates
    * Real-time booking and appointment confirmations

## Quick start guide

Complete the steps below to configure and implement Live activities in your application:

1. **[Configure Adobe Journey Optimizer](mobile-live-configuration.md)**
    
    Set up your environment by creating a mobile configuration.

1. **[Integrate the Adobe Experience Platform Mobile SDK](mobile-live-configuration-sdk.md)**

    Integrate with Adobe Experience Platform Mobile SDK to enable real-time, dynamic updates on the Lock Screen and Dynamic Island. 

1. **[Create a Live activity in Journey Optimizer](create-mobile-live.md)**

    Use API-triggered campaigns in Journey Optimizer to start your Live activity.

1. **[Track your campaigns](../reports/campaign-global-report-cja-activity.md)**

    Start measuring the impact of your Live activity with built-in reports.

## How-to video

Discover how to configure iOS Live activities with Adobe Journey Optimizer to deliver rich, real-time updates on the iPhone Lock Screen and Dynamic Island.

>[!VIDEO](https://video.tv.adobe.com/v/3479864/?learn=on)
