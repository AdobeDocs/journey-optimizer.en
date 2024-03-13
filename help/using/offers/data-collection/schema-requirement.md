---
product: experience platform
solution: Experience Platform
title: Configure events capture
description: Learn how to configure your offer schema to capture events
feature: Ranking, Datasets, Decision Management
role: Developer, Data Engineer
level: Experienced
exl-id: f70ba749-f517-4e09-a381-243b21713b48
---
# Configure data collection {#schema-requirements}

To be able to get feedback on event types other than decision events, you must set the correct value for each event type in an **experience event** that is sent into Adobe Experience Platform.

>[!CAUTION]
>
>For each event type, make sure the schema used in the dataset has the **[!UICONTROL Experience Event - Proposition Interactions]** field group associated with it. [Learn more](create-dataset.md)

Below are the schema requirements you need to implement into your JavaScript code.

>[!NOTE]
>
>Decision events do not need to be sent in as Decision management will generate these events automatically and put them in the **[!UICONTROL ODE DecisionEvents]** dataset<!--to check--> that is auto-generated.

## Track impressions {#track-impressions}

Make sure the event type and source are as follows:

**Experience event type:** `decisioning.propositionDisplay`
**Source:** Web.sdk/Alloy.js (`sendEvent command -> xdm : {eventType, interactionMixin}`) or batch ingestion
+++**Sample payload:**

```
{
    "@id": "a7864a96-1eac-4934-ab44-54ad037b4f2b",
    "xdm:timestamp": "2023-09-26T15:52:25+00:00",
    "xdm:eventType": "decisioning.propositionDisplay",
    "https://ns.adobe.com/experience/decisioning/propositions":
    [
        {
            "xdm:items":
            [
                {
                    "xdm:id": "personalized-offer:f67bab756ed6ee4",
                },
                {
                    "xdm:id": "personalized-offer:f67bab756ed6ee5",
                }
            ],
            "xdm:id": "3cc33a7e-13ca-4b19-b25d-c816eff9a70a", //decision event id - taken from experience event for "nextBestOffer"
            "xdm:scope": "scope:12cfc3fa94281acb", //decision scope id - taken from experience event for "nextBestOffer"
        }
    ]
}
```

+++

## Track clicks {#track-clicks}

Make sure the event type and source are as follows:

**Experience event type:** `decisioning.propositionInteract`
**Source:** Web.sdk/Alloy.js (`sendEvent command -> xdm : {eventType, interactionMixin}`) or batch ingestion
+++**Sample payload:**

```
{
    "@id": "a7864a96-1eac-4934-ab44-54ad037b4f2b",
    "xdm:timestamp": "2023-09-26T15:52:25+00:00",
    "xdm:eventType": "decisioning.propositionInteract",
    "https://ns.adobe.com/experience/decisioning/propositions":
    [
        {
            "xdm:items":
            [
                {
                    "xdm:id": "personalized-offer:f67bab756ed6ee4"
                },
                {
                    "xdm:id": "personalized-offer:f67bab756ed6ee5"
                },
            ],
            "xdm:id": "3cc33a7e-13ca-4b19-b25d-c816eff9a70a", //decision event id
            "xdm:scope": "scope:12cfc3fa94281acb", //decision scope id
        }
    ]
}
```

+++

## Track custom events {#track-custom-events}

For custom events, the schema used in the dataset must also have the **[!UICONTROL Experience Event - Proposition Interactions]** field group associated with it, but there is no specific requirement on the experience event type that must be used to tag these events.

>[!NOTE]
>
>To have your custom events accounted for in [frequency capping](../offer-library/add-constraints.md#capping), you need to connect the experience event to Adobe Experience Platform endpoints by sending it to either one of these two Edge data collection endpoints:
>
>* POST /ee/v2/interact
>* POST /ee/v2/collect
>
>If you are using the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/docs/experience-platform/edge/home.html){target="_blank"} or [Adobe Experience Platform Mobile SDK](https://experienceleague.adobe.com/docs/platform-learn/data-collection/mobile-sdk/overview.html){target="_blank"}, the connection is made automatically.
