---
solution: Journey Optimizer
product: journey optimizer
title: Audience Qualification events
description: Learn how to use and configure audience qualification events
feature: Journeys, Activities, Audiences
topic: Content Management
role: User
level: Intermediate
keywords: qualification, events, audience, journey, platform
exl-id: 7e70b8a9-7fac-4450-ad9c-597fe0496df9
version: Journey Orchestration
---
# Audience Qualification events {#segment-qualification}

>[!CONTEXTUALHELP]
>id="ajo_journey_event_segment_qualification"
>title="Audience qualification events"
>abstract="This activity listens to entrances and exits of profiles in [!DNL Adobe Experience Platform] audiences to move individuals through a journey."

## About audience qualification events{#about-segment-qualification}

This activity listens to entrances and exits of profiles in [!DNL Adobe Experience Platform] audiences. It can make individuals enter a journey or move forward. For more information about audience creation, refer to this [section](../audience/about-audiences.md).

Let's say you have a "silver customer" audience. With this activity, you can make all new silver customers enter a journey and send them a series of personalized messages.

This type of event can be positioned as the first step or later in the journey.

➡️ [Discover this feature in video](#video) 


>[!CAUTION]
>
>Before starting to configure an Audience qualification, [read the Guardrails and Limitations](#audience-qualification-guardrails).


## Configure the activity {#configure-segment-qualification}

To configure the **[!UICONTROL Audience Qualification]** activity, follow these steps:

1. Unfold the **[!UICONTROL Events]** category and drop an **[!UICONTROL Audience Qualification]** activity into your canvas.

   ![Audience Qualification event in journey palette](assets/segment5.png)

1. Add a **[!UICONTROL Label]** to the activity. This step is optional.

1. Click in the **[!UICONTROL Audience]** field and select the audiences you want to leverage.

   >[!NOTE]
   >
   >You can customize the columns displayed in the list and sort them.

   ![Audience selection dropdown for qualification event configuration](assets/segment6.png)

   Once the audience is added, the **[!UICONTROL Copy]** button allows you to copy its name and ID:

   `{"name":"Loyalty membership","id":"8597c5dc-70e3-4b05-8fb9-7e938f5c07a3"}`

   ![Copy button to copy audience name and ID in JSON format](assets/segment-copy.png)

1. In the **[!UICONTROL Behaviour]** field, choose whether you want to listen to audience entrances, exits or both.

   >[!NOTE]
   >
   >**[!UICONTROL Enter]** and **[!UICONTROL Exit]** correspond to the **Realized** and **Exited** audience participation statuses from [!DNL Adobe Experience Platform].
   >See the [Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/tutorials/evaluate-a-segment.html#interpret-segment-results){target="_blank"}.

1. Select a namespace. This is only needed if the event is positioned as the first step of the journey. By default, the field is pre-filled with the last used namespace.

    >[!NOTE]
    >
    >You can only select a people-based identity namespace.
    >Lookup table namespaces (for example, ProductID for a Product lookup) are not available in the **Namespace** dropdown list.

   ![Namespace selection for audience qualification identity](assets/segment7.png)

The payload contains the following context information, which you can use in conditions and actions:

* the behavior (entrance, exit)
* the timestamp of qualification
* the audience id

When using the expression editor in a condition or action that follows an **[!UICONTROL Audience Qualification]** activity, you have access to the **[!UICONTROL AudienceQualification]** node. You can choose between the **[!UICONTROL Last qualification time]** and the **[!UICONTROL status]** (enter or exit).

See [Condition activity](../building-journeys/condition-activity.md#about_condition).

A new journey that includes an **Audience Qualification** event becomes operational ten minutes after you publish it. This interval matches the cache refresh interval of the dedicated service. Wait ten minutes before using this journey.

## Best practices {#best-practices-segments}

The **[!UICONTROL Audience Qualification]** activity enables immediate entry into journeys for individuals qualifying or disqualifying from an [!DNL Adobe Experience Platform] audience.

The reception speed of this information is high. Measurements show 10,000 events received per second. Plan for entry spikes, avoid them when possible, and prepare your journey to handle them. Learn more about journey processing rates and throughput limits in [this section](entry-management.md#journey-processing-rate).

### Batch audiences {#batch-speed-segment-qualification}

When using Audience Qualification for a batch audience, note that a peak of entrance occurs at the time of the daily calculation. The size of the peak depends on how many individuals enter or exit the audience each day.

Moreover, if the batch audience is newly created and immediately used in a journey, the first batch of calculation can drive many entries. Plan for this spike.

### Streamed audiences {#streamed-speed-segment-qualification}

When using Audience Qualification for streamed audiences, there is less risk of large entrance and exit peaks because evaluation is continuous. If the audience definition qualifies many customers at once, a peak can still occur.

Avoid using open and send events with streaming segmentation. Instead, use real user-activity signals like clicks, purchases, or beacon data. For frequency or suppression logic, use business rules instead of send events. [Learn more](../audience/about-audiences.md)

See the [[!DNL Adobe Experience Platform] streaming segmentation documentation](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/methods/streaming-segmentation){target="_blank"}.

>[!NOTE]
>
>For streaming segmentation, newly ingested data may take up to **2 hours** to propagate fully within [!DNL Adobe Experience Platform] for real-time use. Audiences that rely on day-based or time-based conditions (e.g., "events that occurred today") may experience additional complexity in qualification timing. If your journey depends on immediate audience qualification, consider adding a short [Wait activity](wait-activity.md) at the beginning. You can also allow buffer time to ensure accurate qualification.

#### Why not all qualified profiles may enter the journey {#streaming-entry-caveats}

When using streaming audiences with the **Audience Qualification** activity, not all profiles that qualify for the audience will necessarily enter the journey. This behavior can occur for the following reasons:

* **Profiles already in the audience**: Only profiles that newly qualify for the audience after the journey is published will trigger entry. Profiles already in the audience before publishing will not enter.

* **Journey activation time**: When you publish a journey, the **Audience Qualification** activity takes up to **10 minutes** to become active and start listening for profile entries and exits. [Learn more about journey activation](#configure-segment-qualification).

* **Quick exits from audience**: If a profile qualifies for the audience but exits before the journey entry is triggered, that profile may not enter the journey.

* **Timing between qualification and journey processing**: Due to the distributed nature of [!DNL Adobe Experience Platform], there may be timing gaps. A profile can qualify before the journey processes the qualification event.

**Recommendations:**

* After publishing a journey, wait at least 10 minutes before sending events or data that will trigger profile qualification. This ensures the journey is fully activated and ready to process entries.

* For critical use cases where you need to ensure all qualified profiles enter, consider using a [Read Audience](read-audience.md) activity instead. It processes all profiles in an audience at a specific time.

* Monitor your journey's [entry rate and throughput](entry-management.md#profile-entrance-rate) to understand profile flow patterns.

* If profiles are not entering as expected, refer to the [troubleshooting guide](troubleshooting-execution.md#checking-if-people-enter-the-journey) for additional diagnostic steps.

### How to avoid overloads {#overloads-speed-segment-qualification}

Here are a few best practices to avoid overloading systems leveraged in journeys (data sources, custom actions, channel action activities):

* Do not use a batch audience immediately after its creation in an **[!UICONTROL Audience Qualification]** activity. This avoids the first calculation peak. A yellow warning appears in the journey canvas if you are about to use an audience that has never been calculated.

   ![Error message when audience not found in [!DNL Adobe Experience Platform]](assets/segment-error.png)

* Put in place a capping rule for data sources and actions used in journeys to avoid overloading them. Learn more in [Journey Orchestration documentation](https://experienceleague.adobe.com/docs/journeys/using/working-with-apis/capping.html){target="_blank"}. Note that the capping rule has no retry. If you need to retry, use an alternative path in the journey by checking the box **[!UICONTROL Add an alternative path in case of a timeout or an error]** in conditions or actions.

* Before using the audience in a production journey, evaluate the volume of individuals qualifying for this audience daily. To do so, check the **[!UICONTROL Audience]** menu, open the audience, and look at the **[!UICONTROL Profiles over time]** graph.

   ![Warning message when audience has too many events for real-time processing](assets/segment-overload.png)

Learn more about entry rate limits and throughput in [this section](entry-management.md#profile-entrance-rate).

## Guardrails and limitations {#audience-qualification-guardrails}

Follow the guardrails and recommendations below to build Audience Qualification journeys. See also [Audience Qualification best practices](#best-practices-segments).


* Audience Qualification journeys are primarily designed to work with streaming audiences. This combination guarantees a better real-time experience. It is strongly recommended to use **streaming audiences** in the Audience Qualification activity.

   However, if you want to use batch ingestion-based attributes in your streaming audience or a batch audience for an Audience Qualification journey, consider the time span for audience evaluation/activation. A batch audience or streaming audience using batch-ingested attributes becomes ready for use in the **Audience Qualification** activity approximately **2 hours** after the completion of your segmentation job. This job runs once a day at the time defined by your Adobe Organization administrator.

* [!DNL Adobe Experience Platform] audiences are calculated either once a day (**batch** audiences) or in real-time (for **streamed** audiences, using the High Frequency Audiences option of [!DNL Adobe Experience Platform]).

   * If the selected audience is streamed, individuals belonging to this audience potentially enter the journey in real-time.
   * If the audience is batch, people newly qualified for this audience will potentially enter the journey when the audience calculation is executed on [!DNL Adobe Experience Platform].

   As a best practice, use streaming audiences in a **Audience Qualification** activity. For batch use cases, please use a **[Read audience](read-audience.md)** activity.

    >[!NOTE]
    >
    >Due to the batch nature of audiences created using composition workflows and custom uploads, these audiences cannot be targeted in an "Audience Qualification" activity. Only audiences created using segment definitions can be leveraged in this activity.

   
* Experience event field groups cannot be used in journeys starting with a **Read Audience**, an **Audience Qualification** or a **Business Event** activity.

* When using an **Audience Qualification** activity in a journey, that activity may take up to 10 minutes to be active and listen to profiles entering or exiting the audience.


>[!CAUTION]
>
>[Guardrails for Real-time Customer Profile data and segmentation](https://experienceleague.adobe.com/docs/experience-platform/profile/guardrails.html){target="_blank"} also apply to [!DNL Adobe Journey Optimizer].



## How-to video {#video}

Understand the applicable use cases for Audience Qualification journeys in this video. Learn how to build a journey with Audience Qualification and which best practices to apply.

>[!VIDEO](https://video.tv.adobe.com/v/3425028?quality=12)
