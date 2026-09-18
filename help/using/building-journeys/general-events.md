---
solution: Journey Optimizer
product: journey optimizer
title: General events
description: Learn how to use general events
feature: Journeys, Events
topic: Content Management
role: User
level: Intermediate
keywords: custom, general, events, journey
exl-id: b1813122-7031-452e-9ac5-a4ea7c6dc57c
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/jKMddtFlzmUinPK5-onY2u-kRAd1MD126biQVwq3aAg
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
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
# General events {#general-events}

>[!BEGINSHADEBOX]

**On this page:** Learn how to use general events to trigger journeys unitarily in real time and configure event timeouts and timeout paths to listen for an event only during a defined period.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_journey_event_custom"
>title="Unitary events"
>abstract="Events allow you to trigger your journeys unitarily to send messages, in real-time, to the individual flowing into the journey. For this type of event, you can only add a label and a description. The event configuration is performed by a data engineer and cannot be edited."

>[!CONTEXTUALHELP]
>id="ajo_journey_event_business_canvas"
>title="Business events"
>abstract="These events allow you to start a journey using a non-profile-related event. When that event is fired, you will be able to send messages to an audience of profiles. For this type of event, you can only add a label and a description. The event configuration is performed by a technical user and cannot be edited."

Events allow you to trigger your journeys unitarily to send messages, in real-time, to the individual flowing into the journey.

For this type of event, you can only add a label and a description. The rest of the configuration cannot be edited. It was performed by the technical user. See [this page](../event/about-events.md).

Learn more about event throughput and journey processing rates in [this section](entry-management.md#journey-processing-rate).

![General events configuration panel with event selection and settings](assets/general-events.png)

When you drop a business event, it automatically adds a **Read Audience** activity. For more information on business events, refer to [this section](../event/about-events.md) 

## Listening to events during a specific time {#events-specific-time}

An event activity positioned in the journey listens to events indefinitely. To listen to an event only during a certain time, you must configure a timeout for the event.

The journey will then listen to the event during the time specified in the timeout. If an event is received during that period, the person will flow in the event path. If not, the customer will either flow into the timeout path if it is defined, or will continue that journey.

If no timeout path is defined, the timeout setting will act as a wait activity, making the profile wait for a period of time, which could be stopped if an event happens before the end of that wait. If you want profiles to be excluded from that journey after timeout, you will have to set a timeout path.

To configure a timeout for an event, follow these steps:

1. Activate the **[!UICONTROL Define the event timeout]** option from the event properties.

1. Specify the amount of time the journey will wait for the event. The maximum duration is **90 days**.

1. When no event is received within the specified timeout, best practice is to send the individuals into a timeout path. For this, enable the **[!UICONTROL Set a timeout path]** option. In that case, the journey continues for the individual once the timeout is reached. We recommend that you always enable the **[!UICONTROL Set a timeout path]** option.

    ![Event timeout configuration with duration and timeout path options](assets/event-timeout.png)

In this example, the journey sends a first welcome email to a customer after he/she enters the lobby. It then sends a meal discount email only if the customer enters the restaurant within the next day. We therefore configured the restaurant event with a 1-day timeout:

* If the restaurant event is received less than 1 day after the welcome email, the meal discount email is sent.
* If no restaurant event is received within the next day, the person flows through the timeout path.

Note that if you want to configure a timeout on multiple events positioned after a **[!UICONTROL Wait]** activity, you need to configure the timeout on one of these events only.

The defined timeout applies to all the events positioned after the **[!UICONTROL Wait]** activity:

* If one event is received within the timeout duration, the individual flows into the received event's path.
* If no event is received within the timeout duration, the individual flows into the timeout branch of the event where the timeout has been defined.

![Multiple events with timeout configurations in journey](assets/event-timeout-group.png)

{{$include /help/_includes/do-not-localize/building-journeys/ai-augmented-general-events.md}}
