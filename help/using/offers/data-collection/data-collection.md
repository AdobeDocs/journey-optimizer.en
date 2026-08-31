---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Data collection
description: Learn more about Decision Management feedback data collection
badge: label="Legacy" type="Informative"
feature: Decision Management, Datasets
topic: Integrations
role: User, Developer
level: Experienced
exl-id: 278cb255-439c-4ce8-ab59-07df79774b98
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/-xLnILnYeTkebBswLoIyVxKl61aaOWqX1vp6GaAoG0A
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
---
# Decision management data collection {#data-collection}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../experience-decisioning/gs-experience-decisioning.md)

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

## Suppress feedback events {#suppress-feedback}

When testing your implementation, you can use the `dryRun` flag to suppress feedback events and prevent them from being captured for reporting and frequency capping counters.

>[!CAUTION]
>
>The `dryRun` flag is intended for testing purposes only. Make sure to remove it before going live, as leaving it active in production will silently suppress all feedback data and prevent frequency capping counters from being incremented.

Add the `dryRun` flag into the XDM event `data` block in your client implementation:

```json
{
    "data": {
        "__adobe": {
            "ajo": {
                "dryRun": true
            }
        }
    }
}
```
