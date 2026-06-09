---
solution: Journey Optimizer
product: journey optimizer
title: Reactions events
description: Learn how to use reaction events to respond to message tracking data such as opens and clicks within your journeys, and configure timeout paths for non-responders.
feature: Journeys, Activities
topic: Content Management
role: User
level: Intermediate
keywords: journey, events, reaction, tracking, platform
exl-id: 235384f3-0dce-4797-8f42-1d4d01fa42d9
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/6myO49j2-TgkX0-diC8JDePxvMBPjZGnMYdxO466cP4
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: d08afb72-92f6-4856-88e3-11ec34313c2f
    internal-label: Event configuration
  - id: d8353d85-5da7-453d-bd68-40ad33fa0ab7
    internal-label: Action activities
  - id: e57d1da4-32c2-4cc6-945c-9feb219156ff
    internal-label: Event activities
  - id: ebd64fe4-362a-4a1c-9476-b2573ed12a95
    internal-label: Reaction events
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Reaction events {#reaction-events}

>[!CONTEXTUALHELP]
>id="ajo_journey_event_reaction"
>title="Reaction events"
>abstract="This activity allows you to react to tracking data related to a message sent within the same journey. We capture this information in real-time at the moment it is shared with [!DNL Adobe Experience Platform]."

## Overview {#overview}

Among the different event activities available in the palette, you will find the built-in **[!UICONTROL Reactions]** event. This activity allows you to react to tracking data related to a message sent within the same journey. We capture this information in real-time at the moment it is shared with [!DNL Adobe Experience Platform]. 

You can react to clicked or opened messages. For example, you can send another message if an individual opened the previous email or clicked inside it, or send a different follow-up message if they did not engage with your communication.

See [Action activities](../building-journeys/about-journey-activities.md#action-activities).

You can use the **[!UICONTROL Reaction]** activity to perform an action when there is no reaction to your messages. To do this, create a second path parallel to the **[!UICONTROL Reaction]** activity and add a **[!UICONTROL Wait]** activity. If there is no reaction during the period defined in the **[!UICONTROL Wait]** activity, the second path will be chosen. You can choose to send, for example, a follow-up message. 

## How to configure reaction events {#configure}

![Reaction event configuration with channel selection and event type options](assets/journey45.png)

Follow these steps to configure the reaction events:

1. Place a **[!UICONTROL Reaction]** activity **immediately** after a [channel action activity](journey-action.md) on the journey canvas.
1. Add a **[!UICONTROL Label]** to the reaction. This step is optional.
1. From the drop-down list, select the action activity you want to react to. You can select any action activity positioned in the previous steps of the path.
1. Depending on the action you selected, choose what you want to react to. 
1. You can define an event timeout (between 40 seconds and 90 days) and a timeout path. This creates a second path for individuals who did not react within the defined duration. When testing a journey that uses a reaction event, the test mode **[!UICONTROL Wait time]** default and minimum value is 40 seconds. See [this section](../building-journeys/testing-the-journey.md).

## Guardrails and limitations {#guardrails-limitations}

* A **[!UICONTROL Reaction]** activity must be placed **immediately** after a [channel action activity](journey-action.md) in the journey canvas. 
* You cannot use a **[!UICONTROL Reaction]** activity if there is no channel action activity before it.
* Placing a **[!UICONTROL Wait]** activity or any other activity between the channel action and the **[!UICONTROL Reaction]** activity is not supported and may result in the Reaction not working as expected.
* Reaction events can only track messages sent within the same journey. They cannot track messages that take place in a different journey.
* Reaction events track clicks on links of the type "tracked". Unsubscription and mirror page links are not taken into account.
* Email opens are tracked using a 0-pixel image included in the email. If email clients (such as Gmail) block images, email opens will not be taken into account.

+++AI Assistant — Page context

- **TL;DR:** This page explains how to use the built-in Reaction event activity in Adobe Journey Optimizer to branch journey paths based on real-time message engagement data such as email opens and link clicks.

**Intents:**
- Add a Reaction event activity to respond to message opens or clicks within a journey
- Configure a timeout duration and fallback path for profiles that do not engage
- Create a parallel path with a Wait activity to handle non-responders
- Select a specific upstream channel action activity to listen to

**Glossary:**
- **Reaction event**: A built-in journey event activity that listens to real-time tracking data (opens, clicks) from a message sent earlier in the same journey *(product-specific)*
- **Timeout path**: A secondary journey branch that profiles follow if they do not produce the expected reaction within the defined timeout period *(product-specific)*

**Guardrails:**
- The Reaction activity must be placed immediately after a channel action activity; no other activity can be placed between them.
- A Reaction activity cannot be used if there is no channel action activity before it in the path.
- Reaction events can only track messages sent within the same journey; cross-journey tracking is not supported.
- Unsubscription links and mirror page links are not tracked by reaction events.
- Email opens rely on a 0-pixel tracking image; if the email client blocks images (e.g., Gmail), opens will not be recorded.
- Event timeout range is 40 seconds to 90 days; the minimum value in test mode is also 40 seconds.

**Terminology:**
- Canonical name: Reaction events — Acronym: none — variants: reaction activity, engagement tracking event
- Synonyms: "Reaction event" = "message engagement event" = "tracking event"
- Do not confuse: "Reaction event" ≠ "external event" (reaction events are built-in and tied to same-journey messages; external events come from outside the journey)

**FAQ:**
- **Q: Can a Reaction event track a message sent in a different journey?** — No; reaction events only track messages sent within the same journey.
- **Q: How do I handle profiles that do not open or click a message?** — Add a parallel path alongside the Reaction activity with a Wait activity; profiles that do not react within the wait duration will follow that second path.
- **Q: Are unsubscribe link clicks tracked by reaction events?** — No; only tracked link types are captured. Unsubscription and mirror page links are excluded.
- **Q: What happens if an email client blocks images?** — Email opens tracked via the 0-pixel image will not be recorded for clients that block images, such as Gmail.
- **Q: What is the valid timeout range for a reaction event?** — Between 40 seconds and 90 days.

+++
