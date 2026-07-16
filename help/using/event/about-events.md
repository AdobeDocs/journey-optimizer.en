---
solution: Journey Optimizer
product: journey optimizer
title: Work with journey events
description: Learn how to work with events in your journeys
feature: Journeys, Events
topic: Administration
role: Developer, Admin
level: Intermediate, Experienced
keywords: events, event, journey, definition, start
exl-id: fb3e51b5-4cbb-4949-8992-1075959da67d
TQID: https://experienceleague.adobe.com/xvLSBd-rwKKNqwQNDa4D8GfFzc-ND1FkC3EdstufkIY
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: baecb07f-ce89-4ebb-9cd9-0f7c053f944f
    internal-label: Journey management
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: d08afb72-92f6-4856-88e3-11ec34313c2f
    internal-label: Event configuration
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Work with journey events {#about-events}

>[!BEGINSHADEBOX]

**On this page:** Understand the three event types, their schema requirements, key constraints, and how to choose the right one for your use case.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_journey_event_list"
>title="Journey events"
>abstract="Journey Optimizer supports three types of events in journeys: unitary events, linked to a specific person's behavior (such as a purchase or a loyalty milestone); business events, triggered by a global occurrence (such as a flight cancellation or a stock update); and audience qualification events, triggered when a profile enters or exits an audience. Use events to trigger journeys and orchestrate the right actions for your profiles."

Use events to trigger journeys individually, delivering real-time messages to each user as they enter the journey.

In the event configuration, you configure the events expected in the journeys. You can use multiple events (in different steps of a journey) and several journeys can use the same event.

Event configuration is **mandatory** and must be performed by a Data engineer.

>[!IMPORTANT]
>
>* Before configuring events, make sure you have: the **Journey Optimizer Administrator** or **Data Engineer** role, an XDM schema with **Real-Time Customer Profile** enabled, an active streaming endpoint, and access to the correct sandbox. 
>
>* For event requirements and limitations (streaming, Query Service, batch ingestion), see [Journey guardrails - Events](../start/guardrails.md#events-g).

**Who does what:**

| Task | Role |
| --- | --- |
| Design and create the XDM schema | Data Engineer |
| Set up the streaming endpoint | Data Engineer |
| Configure unitary and business events (**Administration > Events**) | Data Engineer or Admin |
| Use events in a journey | Journey practitioner |
| Configure audience qualification events (selected on the canvas) | Journey practitioner |

You can configure three types of events: **Unitary events**, **Business events**, and **Audience qualification events**.

➡️ [Discover this feature in video](#video)

➡️ [Discover this feature in video](#video)

## Unitary events {#unitary-events}

**Unitary** events are linked to a person. They relate to the behavior of a person (for example, a person bought a product, visited a shop, exited a website, etc.) or something happening linked to a person (for example, a person reached 10,000 loyalty points). This is what [!DNL Journey Optimizer] will listen to in journeys to orchestrate the best next actions. Unitary events can be rule-based or system generated. [Learn how to create a unitary event](../event/about-creating.md).

**Schema requirement:** An XDM ExperienceEvent schema with a person-based primary identity and **Real-Time Customer Profile** enabled.

**Example:** A customer adds items to their cart and closes the browser. A cart-abandoned event fires, the profile enters the journey in real time, and receives a recovery email one hour later.

>[!NOTE]
>
>Unitary journeys include a reentrance guardrail: profile reentrance is blocked by default for 5 minutes after the journey triggers. For example, if an event triggers a journey at 12:01 for a profile and another arrives at 12:03, the journey does not restart for that profile.

## Business events {#business-events}

**Business** events are not linked to a specific profile. For example, it can be a news alert, a sports update, a flight change or cancelation, an inventory update, weather events, etc. While these events are not specific to a profile, they may be of interest to any number of profiles: individuals subscribed to particular news topics, passengers on a flight, shoppers interested in an out-of-stock product, etc. Business events are always rule-based. When you drop a business event in a journey, it automatically adds a **Read audience** activity right after. [Learn how to create a business event](../event/about-creating-business.md).

**Schema requirement:** A time-series XDM schema with a non-person primary identity, and the `_id` and `timestamp` fields populated. Plan for an audience export delay of 15 minutes to up to one hour.

**Example:** An airline cancels a flight. A business event fires, [!DNL Journey Optimizer] reads the audience of affected passengers, and sends each a rebooking notification.

## Audience qualification events {#audience-qualification-events}

An **audience qualification** event is triggered when a profile enters or exits an audience. For example, a customer crossing a loyalty spend threshold enters the Gold tier audience — that qualification triggers the journey for that profile in real time (for streaming audiences) or at the next batch evaluation. Unlike unitary events, audience qualification lets you build complex triggering logic using the full power of audience definitions, without requiring implementation changes to send a new event. Learn more on [audience qualification events](../building-journeys/audience-qualification-events.md).

**Schema requirement:** No additional schema required — the event relies on existing audience definitions already built in Adobe Experience Platform.

**Example:** A customer's loyalty spend crosses the Gold tier threshold. Their profile qualifies for the Gold audience, the journey triggers automatically, and sends a welcome reward.

>[!NOTE]
>
>Audience qualification events are not configured in **Administration > Events** — they are selected directly on the journey canvas as the first step of a journey.

## Event types at a glance {#event-comparison}

| | Unitary event | Business event | Audience qualification event |
| --- | --- | --- | --- |
| **Linked to a profile?** | Yes — triggered by a specific individual's action. | No — triggered by an external occurrence not tied to one person. | Yes — triggered when a profile enters or exits an audience. |
| **Entry behavior** | One profile enters the journey in real time. | Multiple profiles enter via an automatic Read Audience step. | One profile enters when audience membership changes. |
| **Typical use cases** | Cart abandonment recovery, form submission, app login, loyalty milestone. | Flight cancellation, stock replenishment alert, breaking news, weather event. | Re-engagement of lapsed customers, loyalty tier changes, VIP offboarding flows. |
| **How it starts the journey** | Event-based entry — no audience needed. | Business event + automatic Read Audience (added by Journey Optimizer). | Profile enters or exits a defined audience. |
| **Multiple per journey?** | Yes — you can listen to several unitary events across journey steps. | No — only one business event per journey, placed at the start. | Yes — can be combined with other activities. |
| **Event ID type** | Rule-based or system-generated. | Always rule-based. | No event ID — based on audience membership evaluation. |
| **Configured in Administration?** | Yes | Yes | No — selected directly on the journey canvas. |

>[!NOTE]
>
>A journey can contain only **one** business event, which must be the first activity. Journey Optimizer automatically adds a **Read Audience** activity after it to define which profiles receive the journey triggered by that event.

## Event ID type {#event-id-type}

For **business** events, the event ID type is always rule-based. 

For **unitary** events, there are two types of event ID:

* **Rule-based** events: this type of event does not generate an eventID. Using the simple expression editor, you simply define a rule which will be used by the system to identify the relevant events that will trigger your journeys. This rule can be based on any field available in the event payload, for example the profile's location or the number of items added to the profile's cart. 

   >[!CAUTION]
   >
   >A capping rule is defined for rule-based events. It limits the number of qualified events that a journey can process to 5,000 per seconds for a given Organization. It corresponds to Journey Optimizer SLAs. Refer to your Journey Optimizer licensing and [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"}.

* **System-generated** events: these events require an eventID. This eventID field is automatically generated when creating the event. The system pushing the event should not generate an ID, it should pass the one available in the payload preview. 

>[!NOTE]
>
>Only streamed events can trigger journeys. The following **cannot** be used to trigger a journey:
>
>* Events ingested in batch
>* Events inserted via **Query Service**
>* Events from internal [!DNL Journey Optimizer] datasets (Message Feedback, Email Tracking, and similar)
>
>If you cannot get streamed events, build an audience based on those events and use a **Read Audience** activity instead. To use events for segmentation only, enable the dataset for **Real-Time Customer Profile**.

## How to choose {#choose-event-type}

Use the following criteria to select the right event type for your journey — the key question is: **are you triggering an action for one specific person, or broadcasting to many profiles?** [Learn more on journey types](../building-journeys/journey.md#journey-types).

Each event type maps to a specific journey pattern:

| Event type | Journey pattern |
| --- | --- |
| Unitary event | Real-time, single-profile journey — triggers immediately when a person acts |
| Business event | Broadcast journey — targets many profiles via an automatic Read Audience step |
| Audience qualification event | Segment-triggered journey — fires when a profile enters or exits an audience |

* **Choose a unitary event** when the trigger is tied to a specific individual — for example, a purchase, a form submission, or a loyalty milestone. Unitary events require a person-based primary identity in the schema and start the journey immediately for that profile. [Learn how to configure a unitary event](../event/about-creating.md).

* **Choose a business event** when the trigger is a global occurrence — for example, a product restock, a price drop, or a flight cancellation — and you want to broadcast to a set of profiles related to that signal. Business events must be the first step in the journey and automatically target profiles via a **Read Audience** activity. They require a time-series schema with a non-people primary identity and the `_id` and `timestamp` fields. Plan for an audience export delay of 15 minutes to up to one hour. [Learn how to configure a business event](../event/about-creating-business.md).

* **Choose an audience qualification event** when the trigger is a profile entering or exiting an audience, and you need more complex segmentation logic than a single event can provide — for example, re-engaging lapsed customers who just met a spend threshold, or triggering an offboarding flow when a VIP member drops out of the loyalty tier. [Learn more on audience qualification events](../building-journeys/audience-qualification-events.md).

>[!CAUTION]
>
>Business events cannot be used in the same journey as unitary events or audience qualification activities.

## Key constraints {#key-constraints}

Use this summary to plan your implementation before configuring events.

| Constraint | Details |
| --- | --- |
| Throughput limit | 5,000 events per second per organization, across all sandboxes (unitary and Read Audience journeys) |
| Reentrance block | Profile reentrance blocked for 5 minutes after a unitary journey triggers |
| Business events per journey | Maximum 1, must be the first step |
| Mix business + unitary in one journey | Not supported |
| Batch events | Cannot trigger journeys — use a **Read Audience** activity instead |
| Audience qualification — Administration | Not configured in **Administration > Events** — selected directly on the journey canvas |
| Edit a live event | Can only change the name, description, or add payload fields |

## How events reach Journey Optimizer {#data-cycle}

Events must be sent to [!DNL Journey Optimizer] as POST calls through [Adobe Experience Platform Streaming Ingestion APIs](https://experienceleague.adobe.com/docs/experience-platform/xdm/api/getting-started.html){target="_blank"}. The payload must follow XDM formatting, and the event schema must have **Real-Time Customer Profile** enabled.

Both authenticated and unauthenticated streaming modes are supported. Batch-ingested events and events from internal [!DNL Journey Optimizer] datasets (message feedback, email tracking, and similar) cannot be used to trigger journeys — use a **Read Audience** activity instead for those use cases.


## Event throughput limits {#event-throughput}

Adobe Journey Optimizer enforces separate throughput limits per event type, at an organization level across all sandboxes:

* **Unitary events**: 5,000 events per second
* **Read Audience based journey events**: 5,000 events per second

These limits apply to all events used in active journeys, which includes **Live**, **Dry run**, **Closed** and **Paused** journeys. When a limit is reached, new events get queued and processed at 5,000 per second until the queue is drained.

For more details on journey processing rates and how different journey types impact throughput, [learn more on journey processing rates](../building-journeys/entry-management.md#journey-processing-rate).

The following types of events are counted toward these quotas:

* **External Unitary Events**: Includes both rule-based and system-generated events. If the same raw event qualifies for multiple rule definitions, each matched rule counts as a separate event toward the quota.

* **Audience Qualification Events**: If the same streaming audience is used in multiple journeys, each usage counts separately. For instance, using the same audience in an audience qualification activity in two journeys results in two counted events.

* **Reaction Events**: Events triggered by profile reactions (email opened, email clicked, etc.) within a journey.

* **Business Events**: Events not tied to a specific profile, but to a business-related event.

* **Analytics Events**: If the [integration with Adobe Analytics to trigger journeys](about-analytics.md) has been enabled, these events are also included.

* **Resume Events**: Technical event triggered when a profile resumes from a paused journey. Learn more about [resuming paused journeys](../building-journeys/journey-pause.md#journey-resume-steps).

* **Wait Node Completion Events**: When a profile exits a wait node, a technical event is generated to resume the journey.

>[!NOTE]
>
>Except for wait and resume events, all other event types also count toward the quota when used in journeys based on read audiences.

## Updating and deleting an event {#update-event}


To avoid breaking existing journeys, when you edit an event used in a **Draft**, **Live** or **Closed** journey, you can only change the name, the description or add payload fields. 

Any event used in **Live**, **Draft** or **Closed** journeys cannot be deleted. To delete a used event, you must stop journeys using it, and/or remove it from the Draft journeys where it is used. You can check the **[!UICONTROL Used in]** field. It displays the number of journeys that use that particular event. You can click the **[!UICONTROL View journeys]** button to display the list of corresponding journeys.

## Frequently asked questions {#faq}

**Can I use the same event in multiple journeys?**
Yes — several journeys can listen to the same event simultaneously.

**Can I combine a business event and a unitary event in the same journey?**
No — business events cannot be used in the same journey as unitary events or audience qualification activities.

**Do I need to configure anything for audience qualification events?**
No — audience qualification events are not configured in **Administration > Events**. Select the audience directly on the journey canvas as the first step.

**Can I use batch-ingested data to trigger a journey?**
No — only streamed events can trigger journeys. For batch data, build an audience and use a **Read Audience** activity instead.

**My journey isn't triggering — what should I check?**

* Verify that your event schema has **Real-Time Customer Profile** enabled.
* Confirm that events are streamed — batch-ingested events cannot trigger journeys.
* For rule-based events, verify that the rule condition matches the incoming payload fields.
* Check that the journey is in **Live** status and that the profile meets any entry conditions.

## Next steps {#next-steps}

* [Configure a unitary event](../event/about-creating.md)
* [Configure a business event](../event/about-creating-business.md)
* [Learn more on audience qualification events](../building-journeys/audience-qualification-events.md)
* [Manage journey entry and reentrance](../building-journeys/entry-management.md)

>[!TIP]
>
>If your journey is not triggering, verify that your event schema has **Real-Time Customer Profile** enabled and that events are streamed — batch-ingested events cannot trigger journeys.

## How-to videos {#video}

Learn how to configure an event, specify the streaming endpoint and the payload for an event.

>[!VIDEO](https://video.tv.adobe.com/v/336253?quality=12)

Understand the applicable use cases for business events. Learn how to build a journey using a business event and which best practices to apply.

>[!VIDEO](https://video.tv.adobe.com/v/334234?quality=12)
