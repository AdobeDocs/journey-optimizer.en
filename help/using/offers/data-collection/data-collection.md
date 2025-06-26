---
title: Data collection
description: Learn more about Decision Management feedback data collection
feature: Decision Management, Datasets
topic: Integrations
role: User, Data Engineer, Developer
level: Experienced
exl-id: 278cb255-439c-4ce8-ab59-07df79774b98
---
# Decision management data collection {#data-collection}

## Understanding data collection

You can collect offer decisioning feedback in Adobe Experience Platform, including which offers are displayed and how users interact with them. This data can be used for:
* Composing [Decision management reports](../reports/get-started-events.md);
* Using [frequency capping](../offer-library/add-constraints.md#capping) rules;
* Building [AI models](../ranking/create-ranking-strategies.md) that can be used as a ranking method.

## Types of events

The way data is collected varies according to the event type you want to capture.

### Decision events

Each time Decision management makes a decision, information related to that decision event is **automatically** sent to Adobe Experience Platform for all channels. [Learn more](../reports/get-started-events.md)

### Impression and click events

Decision management impressions and clicks are defined as follows:

* An **impression** event is when an offer is displayed to a user.

* A **click** event is when a user clicks or interacts with an offer.

Feedback on impressions and clicks is captured depending on the [!DNL Journey Optimizer] channel that is used.

**Emails** authored by [!DNL Journey Optimizer] **automatically** track impressions and clicks.

However, **most channels** require impressions and clicks data to be sent into Adobe Experience Platform as an **experience event**. This includes:

* Web pages using the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/docs/experience-platform/edge/home.html){target="_blank"} to render offers

* Mobile apps using the [Adobe Experience Platform Mobile SDK](https://experienceleague.adobe.com/docs/platform-learn/data-collection/mobile-sdk/overview.html){target="_blank"} to render offers - [Learn more](https://developer.adobe.com/client-sdks/documentation/adobe-journey-optimizer-decisioning/#ab-sj-tracking-servers){target="_blank"}
* Kiosks
* Messages sent through third-party applications
<!--Mobile push notifications authored by [!DNL Journey Optimizer] - [Learn more](https://developer.adobe.com/client-sdks/documentation/adobe-journey-optimizer/api-reference/#handlenotificationresponse){target="_blank"}-->

>[!NOTE]
>
>Channels that use a decisioning API request to receive offers need feedback sent in as an experience event. In other words, if the offer needs instructions on how to render, you can assume that you should send in feedback as experience events.

### Custom events

Feedback on custom events tied to an offer can be sent into Adobe Experience Platform according to your own preferences. For example, if an offer has multiple buttons such as *Interested*, *Not interested*, etc., you may want to send in those events separately, but these can also be sent in as experience events.

## Sending in feedback data

To send in feedback data, you need to create a dataset to collect events and, for each event type, define an experience event that will be sent into Adobe Experience Platform.

* Learn how to create a dataset where the experience events will be collected in [this section](create-dataset.md).

* Learn how to define experience events to send in feedback data in [this section](schema-requirement.md).
