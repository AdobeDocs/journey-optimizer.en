---
solution: Journey Optimizer
product: journey optimizer
title: Audience Qualification events
description: Learn about audience qualification events
feature: Journeys, Activities, Audiences
topic: Content Management
role: User
level: Intermediate
keywords: qualification, events, audience, journey, platform
exl-id: 7e70b8a9-7fac-4450-ad9c-597fe0496df9
---
# Audience Qualification events {#segment-qualification}

## About audience qualification events{#about-segment-qualification}

>[!CONTEXTUALHELP]
>id="ajo_journey_event_segment_qualification"
>title="Audience qualification events"
>abstract="This activity allows your journey to listen to the entrances and exits of profiles in Adobe Experience Platform audiences in order to make individuals enter or move forward in a journey."

This activity allows your journey to listen to the entrances and exits of profiles in Adobe Experience Platform audiences in order to make individuals enter or move forward in a journey. For more information on audience creation, refer to this [section](../audience/about-audiences.md).

Let's say you have a "silver customer" audience. With this activity, you can make all new silver customers enter a journey and send them a series of personalized messages.

This type of event can be positioned as the first step or later in the journey.

➡️ [Discover this feature in video](#video) 

### Important notes{#important-notes-segment-qualification}

* Keep in mind that Adobe Experience Platform audiences are calculated either once a day (**batch** audiences) or in real-time (for **streamed** audiences, using the High Frequency Audiences option of Adobe Experience Platform).

   * If the selected audience is streamed, the individuals belonging to this audience will potentially enter the journey in real-time.
   * If the audience is batch, people newly qualified for this audience will potentially enter the journey when the audience calculation is executed on Adobe Experience Platform.

   As a best practice, we therefore recommend only using streaming audiences in a **Audience qualification** activity. For batch use cases, please use a **[Read audience](read-audience.md)** activity.

    >[!NOTE]
    >
    >Due to the batch nature of audiences created using composition workflows and custom upload, you cannot target these audiences in an "Audience Qualification" activity. Only audiences created using segment definitions can be leveraged in this activity.

* Experience event field groups can not be used in journeys starting with a Read audience, an Audience qualification or a business event activity.

* When using an audience qualification in a journey, that audience qualification activity may take up to 10 minutes to be active and listen to profiles entering or exiting the audience.

### Configure the activity {#configure-segment-qualification}

To configure the **[!UICONTROL Audience Qualification]** activity, follow these steps:

1. Unfold the **[!UICONTROL Events]** category and drop an **[!UICONTROL Audience Qualification]** activity into your canvas.

   ![](assets/segment5.png)

1. Add a **[!UICONTROL Label]** to the activity. This step is optional.

1. Click in the **[!UICONTROL Audience]** field and select the audiences you want to leverage.

   >[!NOTE]
   >
   >Note that you can customize the columns displayed in the list and sort them.

   ![](assets/segment6.png)

   Once the audience is added, the **[!UICONTROL Copy]** button allows you to copy its name and ID:

   `{"name":"Loyalty membership","id":"8597c5dc-70e3-4b05-8fb9-7e938f5c07a3"}`

   ![](assets/segment-copy.png)

1. In the **[!UICONTROL Behaviour]** field, choose whether you want to listen to audience entrances, exits or both.

   >[!NOTE]
   >
   >Note that **[!UICONTROL Enter]** and **[!UICONTROL Exit]** correspond to the **Realized** and **Exited** audience participation statuses from Adobe Experience Platform. For more on how to evaluate an audience, refer to the [Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/tutorials/evaluate-a-segment.html#interpret-segment-results){target="_blank"}. 

1. Select a namespace. This is only needed if the event is positioned as the first step of the journey. By default, the field is pre-filled with the last used namespace.

    >[!NOTE]
    >
    >You can only select a people-based identity namespace. If you have defined a namespace for a lookup table (for example: ProductID namespace for a Product lookup), it will not be available in the **Namespace** dropdown list.

   ![](assets/segment7.png)

The payload contains the following context information, which you can use in conditions and actions:

* the behavior (entrance, exit)
* the timestamp of qualification
* the audience id

When using the expression editor in a condition or action that follows an **[!UICONTROL Audience Qualification]** activity, you have access to the **[!UICONTROL AudienceQualification]** node. You can choose between the **[!UICONTROL Last qualification time]** and the **[!UICONTROL status]** (enter or exit).

See [Condition activity](../building-journeys/condition-activity.md#about_condition).

![](assets/segment8.png)

A new journey that includes an audience qualification event is operational ten minutes after you have published it. This time interval corresponds to the cache refresh interval of the dedicated service. Therefore, you must wait ten minutes before using this journey.

## Best practices {#best-practices-segments}

The **[!UICONTROL Audience Qualification]** activity enables the immediate entrance in journeys of individuals getting qualified or disqualified from an Adobe Experience Platform audience.

The reception speed of this information is high. Measurements made show a speed of 10 000 events received per seconds. As a result, you should make sure you understand how peaks of entrance might happen, how to avoid them and how to make your journey ready for them.

### Batch audiences{#batch-speed-segment-qualification}

When using audience qualification for a batch audience, note that a peak of entrance will happen at the time of the daily calculation. The size of the peak will depend on the number of individuals entering (or exiting) the audience daily.

Moreover, if the batch audience is newly created and immediately used in a journey, the first batch of calculation might make a very large number of individuals enter the journey.

### Streamed audiences{#streamed-speed-segment-qualification}

When using audience qualification for streamed audiences, there is less risk of getting large peaks of entrances/exits due to the continuous evaluation of the audience. Still, if the audience definition leads to making a large volume of customers qualify at the same time, there might be a peak too.

Avoid using open and send events with streaming segmentation. Instead, use real user-activity signals like clicks, purchases, or beacon data. For frequency or suppression logic, use business rules rather than send events. [Learn more](../audience/about-audiences.md#open-and-send-event-guardrails)

For more information on streaming segmentation, refer to [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/api/streaming-segmentation.html#api).

### How to avoid overloads{#overloads-speed-segment-qualification}

Here are a few best practices that will help to avoid overloading systems leveraged in journeys (data sources, custom actions, channel action activities).

Do not use, in an **[!UICONTROL Audience Qualification]** activity, a batch audience immediately after its creation. It will avoid the first calculation peak. Note that there will be a yellow warning in the journey canvas if you're about to use an audience that has never been calculated.

![](assets/segment-error.png)

Put in place a capping rule for data sources and actions used in journeys to avoid overloading them. Learn more in [Journey Orchestration documentation](https://experienceleague.adobe.com/docs/journeys/using/working-with-apis/capping.html){target="_blank"}. Note that the capping rule has no retry. If you need to retry, you must use an alternative path in the journey by checking the box **[!UICONTROL Add an alternative path in case of a timeout or an error]** in conditions or actions.

Before using the audience in a production journey, always evaluate first the volume of individuals qualifying for this audience every day. To do so, you can check the **[!UICONTROL Audience]** menu, open the audience then look at the **[!UICONTROL Profiles over time]** graph.

![](assets/segment-overload.png)

## How-to video {#video}

Understand the applicable use cases for audience qualification journeys. Learn how to build a journey with audience qualification and which best practices to apply.

>[!VIDEO](https://video.tv.adobe.com/v/3425028?quality=12)
