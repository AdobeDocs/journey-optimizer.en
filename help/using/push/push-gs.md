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
TQID: https://experienceleague.adobe.com/Nrs2AwD4RfgeXcAP3mhZBwt6WQUd4vUBC9CeCtIIgCU
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: c96d2aa5-76a2-443d-8d23-5de95577c909
    internal-label: Mobile SDK
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
  - id: fd2e3797-f2ea-4b36-a9af-52acf5e90513
    internal-label: Customer profiles
---
# Push notification data flow and components {#get-started-push}

>[!BEGINSHADEBOX]

**On this page:** Understand the push notification data flow, the key services and components involved, and how notifications are delivered end-to-end with Adobe Journey Optimizer.

>[!ENDSHADEBOX]

This page helps you setup and understand key services and workflows involved with push notifications in [!DNL Journey Optimizer]. 


>[!AVAILABILITY]
>
>The new **Mobile onboarding quick start workflow** is now available. Use this new product feature to rapidly configure the Mobile SDK to start collecting and validating mobile event data, and to send mobile push notifications. This capability is accessible via the Data Collection home page as a public beta. [Learn more](mobile-onboarding-wf.md)
>

Learn how to create push notifications on [this page](create-push.md).

Steps to configure push channel in [!DNL Adobe Journey Optimizer] are detailed on [this page](push-configuration.md).

The following pictorial shows the systems and services involved with associated data flows highlighting how push notifications are delivered from an end-to-end service standpoint.

![](assets/push-flow.png)

1. Registration of your branded mobile app (Android or iOS) with Apple's APNs and Google FCM push messaging messaging services
1. Messaging services generate a push token, which, is an identifier that [!DNL Adobe Journey Optimizer] will use to target the specific device with a push notification.
1. The previously generated push token is passed to Adobe Experience Platform and synchronized with the Real-time Customer Profile; this is done OOTB with an easy to integrate client SDK

    >[!NOTE]
    >
    >Token handling differs between platforms. On **Android (FCM)**, tokens are automatically marked as invalid when users clear app cache or reinstall the app, generating a new token and ECID. On **iOS (APNs)**, tokens do not consistently get marked as invalid in these scenarios. If a profile contains multiple ECIDs with valid tokens, push notifications will be sent to all associated devices.

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

* **Adobe Experience Platform Mobile SDK** which provides client-side integration APIs for your mobiles via Android and iOS compatible SDKs. The SDK provides an [!DNL Adobe Journey Optimizer] extension exposing a variety of APIs specific for push messaging and enable data flow like registering the push token or sending push tracking events or any other custom experience events to Adobe Experience Platform. The SDK also provides a variety of other extensions that enable other [!DNL Adobe CX Enterprise] as well as 3rd party partner capabilities.

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
* [Add a message in a journey](../building-journeys/journey-action.md)
* [Add a message in a campaign](../campaigns/create-campaign.md)