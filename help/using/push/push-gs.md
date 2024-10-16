---
solution: Journey Optimizer
product: journey optimizer
title: Push Notification flow in Adobe Journey Optimizer
description: Understand push notification data flow and components
topic: Mobile
feature: Push, Overview
role: Admin
level: Intermediate
exl-id: 9718c4b6-2558-4dfd-9d8f-f8845def19ba
---
# Push notification data flow and components {#get-started-push}

This page helps you setup and understand key services and workflows involved with push notifications in [!DNL Journey Optimizer]. 


>[!AVAILABILITY]
>
>The new **mobile onboarding quick start workflow** is now available. Use this new product feature to rapidly configure the Mobile SDK to start collecting and validating mobile event data, and to send mobile push notifications. This capability is accessible via the Data Collection home page as a public beta. [Learn more](mobile-onboarding-wf.md)
>

Learn how to create push notifications on [this page](create-push.md).

Steps to configure push channel in [!DNL Adobe Journey Optimizer] are detailed on [this page](push-configuration.md).

The following pictorial shows the systems and services involved with associated data flows highlighting how push notifications are delivered from an end-to-end service standpoint.

![](assets/push-flow.png)

1. Registration of your branded mobile app (Android or iOS) with Apple's APNs and Google FCM push messaging messaging services
1. Messaging services generate a push token, which, is an identifier that [!DNL Adobe Journey Optimizer] will use to target the specific device with a push notification.
1. The previously generated push token is passed to Adobe Experience Platform and synchronized with the Real-time Customer Profile; this is done OOTB with an easy to integrate client SDK
1. Push messages are authored in [!DNL Adobe Journey Optimizer], push messages are created against a channel configuration (i.e. message preset)
1. Push messages may be included on the orchestration canvas in Journeys
1. Upon Journey publication, customer profiles based on Journey conditions are qualified to receive push notifications, push messaging payloads are personalized at this step
1. Personalized push payloads are forwarded to an internal push messaging delivery service
1. This internal service then validates the credentials of the app associated with the message, and
1. Sends the message to Apple & Google messaging services for final delivery
1. Feedback from messaging services are noted, errors and successes are logged for reporting in Journey Live & Customer Journey Analytics report
1. Push notifications are delivered to end-user devices
1. End-user push notification interactions are send in as Experience Events from the end-user client via SDK integration

## Roles of key services in push notifications {#roles-of-key-services}

* **Push notification service providers** are the core component web services that deliver notifications from remote servers to mobile apps.
    
    [!DNL Adobe Journey Optimizer]  supports both Android and iOS platforms and consequently integrate with following:
    * [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging) - to send notifications to Android mobile app
    * [Apple Push Notification Service (APNs)](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html) - to send notifications to iOS mobile app

* **Adobe Experience Platform Mobile SDK** which provides client-side integration APIs for your mobiles via Android and iOS compatible SDKs. The SDK provides an [!DNL Adobe Journey Optimizer] extension exposing a variety of APIs specific for push messaging and enable data flow like registering the push token or sending push tracking events or any other custom experience events to Adobe Experience Platform. The SDK also provides a variety of other extensions that enable other Adobe Experience Cloud as well as 3rd party partner capabilities.

    SDK integration also requires setup of Adobe Experience Platform [Data Collection](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html){target="_blank"} services such as:

    * Creating a datastream to configure the profile and experience event datasets against which the data flows into Adobe Experience Platform
    * Creating client-side mobile property and adding extensions. The SDK closely integrates with these extensions to provide a seamless data collection experience.
    * Registering the mobile app bundle identifier and app credentials

* **Adobe Experience Platform Real-time Customer Profile**  maintains a holistic view of each individual customer by combining data from multiple channels, including web, mobile, CRM, and third party. Profile allows you to consolidate your customer data into a unified view offering an actionable, timestamped account of every customer interaction. The push token for a given app user is stored against the user's profile as record data while the interactions the user does with push notifications are tracked as time-series events data. [Learn more about Adobe Experience Platform Real-time Customer Profile](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html){target="_blank"}.

* **[!DNL Adobe Journey Optimizer]** : once your mobile app integrations with above mentioned components are in place and your customer profiles in Adobe Experience Platform, you may author and orchestrate push notifications in [!DNL Adobe Journey Optimizer] to engage with your users.

## Push technical setup and practitioner workflows {#push-technical-setup}

The following pictorial shows the various steps, end-to-end, involved in configuring the components that form the skeleton of push data flow. The action items have been categorized based on the role performing the configuration and the component being configured. 

![](assets/user-flow.png)

**Related topics**

* [Configure push channel](push-configuration.md)
* [Push notification report](../reports/journey-global-report-cja-push.md)
* [Create a push notification](create-push.md)
* [Add a message in a journey](../building-journeys/journeys-message.md)
* [Add a message in a campaign](../campaigns/create-campaign.md)