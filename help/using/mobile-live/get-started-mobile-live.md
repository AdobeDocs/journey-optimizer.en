---
solution: Journey Optimizer
product: journey optimizer
title: Get started with Live activities
description: Learn how to send Live activities in Journey Optimizer
topic: Content Management
role: User
level: Beginner
hide: yes
hidefromtoc: yes
exl-id: c9766603-df19-4efd-8319-27e9764254b4
---
# Get started with Live activity {#get-started-mobile-live}

>[!BEGINSHADEBOX]

* **[Get started with Live activity](get-started-mobile-live.md)**
* [Live activity configuration](mobile-live-configuration.md)
* [Live Activity integration with Adobe Experience Platform Mobile SDK](mobile-live-configuration-sdk.md)
* [Create a Live activity](create-mobile-live.md)
* [Frequently asked questions](mobile-live-faq.md)
* [Live activity campaign report](../reports/campaign-global-report-cja-activity.md)

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>Live activity in Journey Optimizer is only compatible with iOS.

Live activities provide real-time updates and interactive experiences within mobile apps, allowing users to stay informed about ongoing events or tasks directly on their device's screen. 

This feature enhances engagement by delivering live information, such as progress tracking, event updates, or interactive content, without requiring users to open the app.

Live Activities can **only** be initiated via **API-triggered** campaigns, allowing you to provide custom payloads and perform all personalization through your own payload.
The appropriate **API-triggered** campaigns type must be selected based on the intended Live activity use case:

* Select **API-triggered Marketing** for audience-based campaigns
    
    Designed for audiences or segments-based communication where the same update is sent to multiple users, e.g. sports scores, event updates, shared experiences.

* Select **API-triggered Transactional** for individual campaigns
    
    Intended individual users identified by their profile, e.g. order status, delivery tracking.

## Quick start guide

Complete the steps below to configure and implement Live activities in your application:

1. **[Configure Adobe Journey Optimizer](mobile-live-configuration.md)**
    
    Set up your environment by creating a mobile configuration.

1. **[Integrate the Adobe Experience Platform Mobile SDK](mobile-live-configuration-sdk.md)**

    Integrate with Adobe Experience Platform Mobile SDK to enable real-time, dynamic updates on the Lock Screen and Dynamic Island. 

1. **[Create Live activities in Journey Optimizer](create-mobile-live.md)**

    Use API-triggered campaigns in Journey Optimizer to start your Live activities. 

1. **[Track your campaigns](../reports/campaign-global-report-cja-activity.md)**

    Start measuring the impact of your Live activities with built-in reports.
