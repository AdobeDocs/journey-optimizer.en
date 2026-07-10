---
solution: Journey Optimizer
product: journey optimizer
title: Use an audience in a journey
description: Learn how to configure and use the Read Audience activity to make individuals from [!DNL Adobe Experience Platform] audiences enter journeys.
feature: Journeys, Activities, Audiences
topic: Content Management
role: User
level: Intermediate
keywords: activity, journey, read audience, audience, segment, batch, entry point, trigger, schedule, Audience Qualification
exl-id: 7b27d42e-3bfe-45ab-8a37-c55b231052ee
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/XqBTB8kE-KCmI49eHBp63dX09vu5Zh1Dl2BDwH0BkU4
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
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: c3f67a94-f1ff-4f5e-bf6f-bc22405930a3
    internal-label: Wait activity
  - id: cfba2953-2ce9-4b00-a00c-71cd338ae63f
    internal-label: Custom actions
  - id: d2e8a157-b3b0-4143-9ff3-809bf400be56
    internal-label: Sandboxes
  - id: e57d1da4-32c2-4cc6-945c-9feb219156ff
    internal-label: Event activities
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: ff2b9b37-92e0-45fc-b853-379d44c08c89
    internal-label: Audience segmentation
---
# Use an audience in a journey {#segment-trigger-activity}

>[!BEGINSHADEBOX]

**On this page:** Learn how to configure the Read Audience activity to bring profiles from an Adobe Experience Platform audience into a journey, on demand or on a schedule, and personalize each profile's path.

>[!ENDSHADEBOX]

Use the Read Audience activity to start journeys with defined audiences. You choose the audience and when it runs; then use [conditions](#audience-targeting-in-journeys), timers, and actions to personalize each profile's path.

## About the Read Audience activity {#about-segment-trigger-activity}

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment"
>title="Read Audience activity"
>abstract="Adds all qualified profiles from a selected [!DNL Adobe Experience Platform] audience to this journey. Runs once or on a schedule."

The **Read Audience** activity is the journey entry-point activity that adds all profiles from a selected [!DNL Adobe Experience Platform] audience to a journey. You can run the entrance once or on a recurring schedule. In APIs and technical references this activity is also referred to as segment-trigger or audience-based journey entry.

**When to use Read Audience vs Audience Qualification**

| Use **Read Audience** when | Use **[Audience Qualification](audience-qualification-events.md)** when |
|----------------------------|-----------------------------------------------------------------------|
| You want to run a journey once or on a schedule (batch). | You need profiles to enter the journey in real time as they qualify. |
| Your audience is batch-evaluated (e.g. daily snapshot). | Your audience is streaming or event-based. |
| You are okay with a delay between audience evaluation and journey entry. | You need immediate entry when a profile qualifies. |

>[!TIP]
>
>**Real-world examples**
>* **Weekly newsletter** → Read Audience. Your audience is a daily batch snapshot. You schedule the journey every Monday at 9 AM. All qualified profiles enter together.
>* **Loyalty tier upgrade** → Audience Qualification. As soon as a profile reaches Gold status in a streaming audience, they enter the journey immediately to receive a congratulations email.
>* **Re-engagement series** → Read Audience. You run a recurring journey every 30 days targeting profiles inactive for 90+ days.

**Key limits:** One Read Audience per journey (must be the first activity); one audience per activity; up to five concurrent Read Audience runs per organization; 20,000 profiles per second per sandbox; 12-hour job timeout. Full details in [Guardrails and limitations](../start/guardrails.md#read-segment-g).

**Prerequisites:** An [!DNL Adobe Experience Platform] audience that is built and evaluated (Realized status), a people-based identity namespace selected for the journey, and—for recurring runs—understanding of [scheduling and throughput limits](../start/guardrails.md#read-segment-g).

For example, the `Luma app opening and checkout` audience created in the [Build audiences](../audience/about-audiences.md) use case can be used as the entry point. All qualified profiles enter the journey and progress through individualized paths using conditions, timers, events, and actions.

➡️ [Discover this feature in video](#video)


>[!CAUTION]
>
>* Before using the Read audience activity, [read the Guardrails and Limitations](#must-read).

## Configure the activity {#configuring-segment-trigger-activity}

You will set: **Audience** (mandatory), **Namespace** (mandatory), **Reading rate** (mandatory, default 5,000/s), and **Schedule** (when the journey runs). Optionally add a **Label** and **Supplemental identifier**. The steps below walk you through each setting.

### Add activity and select audience {#add-activity-and-select-audience}

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_label"
>title="Label"
>abstract="Optional label to identify this activity in reporting and test mode logs."

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_audience"
>title="Audience"
>abstract="The [!DNL Adobe Experience Platform] audience whose profiles enter this journey. All qualified profiles are read in. Batch audiences are recommended for reliable, consistent counts, and only one audience can be read per activity."

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_namespace"
>title="Namespace"
>abstract="The identity (e.g. email, ECID) used to identify individuals entering the journey. Only people-based namespaces are available, and profiles without this identity cannot enter. By default, the field is pre-filled with the last used namespace."

1. Unfold the **[!UICONTROL Orchestration]** category and drop a **[!UICONTROL Read Audience]** activity into your canvas.

    The activity must be positioned as the first step of a journey.

1. Add a **[!UICONTROL Label]** to the activity (optional). An optional label helps you identify the activity in reporting and in test mode logs.

1. In the **[!UICONTROL Audience]** field, choose the [!DNL Adobe Experience Platform] audience that will enter the journey, then click **[!UICONTROL Save]**. You can select any [!DNL Adobe Experience Platform] audience generated using [segment definitions](../audience/creating-a-segment-definition.md).

   >[!NOTE]
   >
   >In addition, you can target [!DNL Adobe Experience Platform] audiences created using [audience compositions](../audience/get-started-audience-orchestration.md).
   >You can also target audiences [uploaded from a CSV file](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/overview.html#import-audience){target="_blank"}.
   >[Learn more about how to generate and target audiences in Journey Optimizer](../audience/about-audiences.md).

    Note that you can customize the columns displayed in the list and sort them.

    ![Audience selection interface showing available [!DNL Adobe Experience Platform] audiences](assets/read-segment-selection.png)

    Once the audience is added, the **[!UICONTROL Copy]** button allows you to copy its name and ID:

    `{"name":"Luma app opening and checkout","id":"8597c5dc-70e3-4b05-8fb9-7e938f5c07a3"}`

   ![Copy button to copy audience name and ID in JSON format](assets/read-segment-copy.png)

    >[!NOTE]
    >
    >Only the individuals with the **Realized** audience participation status will enter the journey. For more on how to evaluate an audience, refer to the [Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/tutorials/evaluate-a-segment.html#interpret-segment-results){target="_blank"}.

1. In the **[!UICONTROL Namespace]** field, choose the namespace to use in order to identify the individuals. By default, the field is pre-filled with the last used namespace. [Learn more about namespaces](../event/about-creating.md#select-the-namespace).

    >[!NOTE]
    >
    >Individuals belonging to an audience that does not have the selected identity (namespace) among their different identities cannot enter the journey. You can only select a people-based identity namespace. If you have defined a namespace for a lookup table (for example: ProductID namespace for a Product lookup), it will not be available in the **Namespace** dropdown list.

### Supplemental identifier {#read-audience-supplemental-id}

You can optionally enable **Use a supplemental identifier** to run the journey in the context of a secondary identifier (for example, an order ID or booking ID) in addition to the profile ID. This allows multiple entrances of the same profile when the supplemental identifier differs.

[Learn how to use supplemental identifiers in journeys](supplemental-identifier.md). For Read audience journeys, the supplemental identifier is prepared from the **union/profile schema** for **Unified Profile Service** audiences, or selected from eligible attributes on **external audiences** (for example, audiences [imported from a CSV file](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/overview.html#import-audience){target="_blank"} or resulting from [composition workflows](../audience/get-started-audience-orchestration.md)). The reading rate is limited to 500 profiles per second per journey instance when supplemental ID is used.

### Guardrails and recommendations {#must-read}

All guardrails and limitations for the **Read Audience** activity (concurrency, throughput, one audience per activity, job timeout, retries, and more) are listed in [Guardrails and limitations](../start/guardrails.md#read-segment-g).

**Recommendations**

* As a best practice, use batch audiences in a **Read audience** activity for reliable and consistent counts. Read audience is designed for batch use cases. If your use case needs real-time data, use the [Audience qualification](audience-qualification-events.md) activity instead.
* Audiences [imported from a CSV file](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/overview.html#import-audience) or resulting from [composition workflows](../audience/get-started-audience-orchestration.md) can be selected in the **Read Audience** activity. These audiences are not available in the **Audience Qualification** activity.
* For information about audience snapshot timing, batch segmentation completion windows, and how to ensure your journey always runs on the freshest data, see [Timing and data propagation](#timing-and-data-propagation). For recurring journeys, consider enabling the **[!UICONTROL Trigger after batch audience evaluation]** option to automatically delay execution until the latest audience snapshot is ready. [Learn more](#schedule).

>[!CAUTION]
>
>[Guardrails for Real-time Customer Profile data and segmentation](https://experienceleague.adobe.com/docs/experience-platform/profile/guardrails.html){target="_blank"} also apply to [!DNL Adobe Journey Optimizer].

**Next:** Set the [reading rate](#profile-entry-and-reading-rate) and [schedule](#schedule), then [test and publish](#testing-publishing).

### Profile entry and reading rate {#profile-entry-and-reading-rate}

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_reading_rate"
>title="Reading rate"
>abstract="Maximum profiles entering the journey per second (500–20,000). Default is 5,000."

Set the **[!UICONTROL Reading rate]** (mandatory). This is the maximum number of profiles that can enter the journey per second. This rate applies only to this activity and no others in the journey. If you want to define a throttling rate on custom actions, for example, you need to use the throttling API. Refer to this [page](../configuration/throttling.md).

This value is stored in the journey version payload. The default value is 5,000 profiles per second. You can modify this value from 500 to 20,000 profiles per second.

>[!NOTE]
>
>The overall reading rate per sandbox is set to 20,000 profiles per second. Therefore, the reading rate of all the read audiences that run simultaneously in the same sandbox add up to at most 20,000 profiles per second. You cannot modify this cap. Learn more about journey processing rates and throughput in [this section](entry-management.md#journey-processing-rate).

### Schedule the journey {#schedule}

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_scheduler_start_date"
>title="Start date / time"
>abstract="The date and time when the journey starts reading the audience and profiles begin entering. Combine it with the recurrence options below to schedule recurring runs."

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_scheduler_repeat_until"
>title="Repeat until"
>abstract="The date when recurring runs stop. After this date, the journey no longer reads the audience or admits new profiles."

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_scheduler_repeat_every"
>title="Repeat every"
>abstract="How often the journey re-reads the audience and runs again, for example daily or weekly. Determines the recurrence interval between runs until the Repeat until date is reached."

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_scheduler_incremental_read"
>title="Incremental read"
>abstract="After the first run, only new profiles added to the audience enter the journey."

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_scheduler_force_reentrance"
>title="Force reentrance"
>abstract="Clears all participants from the journey before each new audience read, so every run starts fresh and profiles can re-enter on each occurrence."

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_scheduler_synchronize_audience"
>title="Trigger after batch audience evaluation"
>abstract="Delays each run until the batch audience has been freshly evaluated, so the journey reads the most up-to-date audience snapshot instead of stale data. Recommended for recurring journeys that depend on the latest segmentation results."

>[!CONTEXTUALHELP]
>id="ajo_journey_read_segment_scheduler_synchronize_audience_wait_time"
>title="Wait time for fresh audience evaluation"
>abstract="How long the journey waits for fresh audience data (1–6 hours, in minutes or hours)."

By default, journeys are configured to run once. To define a specific date/time and frequency at which the journey should run, follow the steps below.

>[!NOTE]
>
>**Journey status and the 91-day global timeout:**
>
>* **Non-recurring** Read audience journeys automatically transition to **Stopped** status once the last active profile exits — unless the journey includes nodes that cause waiting periods (Wait nodes, Reaction nodes, or event-triggered transitions), in which case the standard [91-day global timeout](journey-properties.md#global_timeout) applies. [Learn more](end-journey.md#auto-stop-non-recurring)
>* **Recurring** Read audience journeys with no end date **remain Live** as long as the journey is published. They move to **Finished** status 91 days after the execution of their **last occurrence**.
>* The 91-day timeout applies to individual **profiles** flowing through the journey (maximum time a profile can remain active), not to the journey's Live status.
>* The 91-day **reporting window** is a separate concept: the UI shows performance data for approximately the last 91 days. Older data is not accessible in the UI but the journey continues to run. [Learn more](journey-properties.md#global_timeout)

1. In the **[!UICONTROL Read audience]** activity properties, select **[!UICONTROL Edit journey schedule]**.

    ![Edit journey schedule button in Read audience activity properties](assets/read-segment-schedule.png)

1. The journey's properties display. In the **[!UICONTROL Scheduler type]** drop-down list, select the frequency at which you want the journey to run.

    ![Scheduler type dropdown with frequency options: once, daily, weekly, monthly](assets/read-segment-schedule-list.png)

For recurring journeys, specific options are available to help you manage the entry of profiles into the journey. Expand the sections below for more information on each option.

>[!NOTE]
>
>**How audience snapshots are used**
>
>Each Read Audience execution uses the audience membership available at the time that execution runs. For batch audiences, [!DNL Journey Optimizer] reads from the latest available batch audience snapshot. It does not recalculate the audience in real time when the journey starts.
>
>For recurring journeys, each occurrence uses the snapshot available for that occurrence. If you want the journey to wait for the latest batch audience evaluation before it runs, enable **[!UICONTROL Trigger after batch audience evaluation]**.

![Read audience recurring options: Incremental read, Force reentrance, Trigger after batch](assets/read-audience-options.png)

+++**[!UICONTROL Incremental read]**

When a journey with a recurring **Read audience** executes for the first time, all the profiles in the audience enter the journey. This option allows you to target, after the first occurrence, only the individuals who entered the audience since the last execution of the journey.

When using this option, the system looks back **24 hours** from the time of the last audience evaluation job performed by [!DNL Adobe Experience Platform]'s segmentation service.

After segmentation completes, a profile snapshot export job begins which allows Journey Optimizer to detect and process new profiles. If the journey is scheduled between these two jobs, the incremental read will not pick up profiles that became members of the audience since the last execution of the journey.

To minimize the risk of missing profiles:
* Enable the **[!UICONTROL Trigger after batch audience evaluation]** option to extend the look-back period to the time of the last successful journey execution, regardless of how long ago it occurred
* Schedule journeys to run well after daily batch segmentation jobs complete (typically 2-3 hours buffer)
* For time-critical use cases requiring immediate profile inclusion, consider using [Audience Qualification](audience-qualification-events.md) activities with streaming audiences instead

>[!CAUTION]
>
>If you are targeting a [custom upload audience](../audience/about-audiences.md#about-segments) in your journey, profiles are only retrieved on the first recurrence when this option is enabled in a recurring journey. These audiences are fixed.

+++

+++**[!UICONTROL Force reentrance on recurrence]**

This option allows you to make all profiles still present in the journey automatically exit it on the next execution.

For example, if you have a 2-day wait in a daily recurring journey, activating this option moves profiles to the next journey execution. This happens the day after, whether they are in the next run audience or not.

If the lifespan of your profiles in this journey may be longer than the recurrence frequency, do not activate this option to make sure that profiles can finish their journey.

+++

+++**How [!UICONTROL Incremental read] and [!UICONTROL Force reentrance on recurrence] work together**

These two options control different parts of the journey execution:

* **[!UICONTROL Incremental read]** controls **which profiles are selected from the audience** for the next recurring run.
* **[!UICONTROL Force reentrance on recurrence]** controls **what happens to profiles who are still active in the journey** when the next recurring run starts.

Use the table below to understand the combined behavior on the next run.

| [!UICONTROL Incremental read] | [!UICONTROL Force reentrance on recurrence] | Behavior on the next run |
| ------------------------------ | ------------------------------------------- | ------------------------ |
| Off | Off | [!DNL Journey Optimizer] reads the full audience for that run. Profiles who are still active in the journey are not reset automatically. |
| On | Off | [!DNL Journey Optimizer] reads only profiles who were added to the audience since the last execution. Profiles who are still active in the journey are not reset automatically. |
| Off | On | [!DNL Journey Optimizer] removes active participants from the current journey execution before starting the next run, then reads the full audience again. This allows profiles to start fresh on the new occurrence. |
| On | On | [!DNL Journey Optimizer] removes active participants from the current journey execution before starting the next run, then reads only profiles who were added to the audience since the last execution. Force reentrance resets active journey participation, but incremental read still limits selection to newly added audience members. |

In other words, **[!UICONTROL Force reentrance on recurrence] does not disable [!UICONTROL Incremental read]**. If both options are enabled, profiles are removed from their active journey instance before the next occurrence starts, but the next occurrence still selects only the audience members considered new since the last execution.

>[!IMPORTANT]
>
>A profile removed by **[!UICONTROL Force reentrance on recurrence]** is not automatically treated as a new audience member for **[!UICONTROL Incremental read]**. Audience selection still depends on whether the profile was newly added to the audience since the last execution.

+++

+++**[!UICONTROL Trigger after batch audience evaluation]**

For journeys scheduled daily and targeting batch audiences, you can define a time window of up to 6 hours for the journey to wait for fresh audience data from batch segmentation jobs. If the segmentation job completes within the time window, the journey triggers. Otherwise, it skips the journey until its next occurrence. This option ensures journeys run with accurate and up-to-date audience data.

For example, if a journey is scheduled for 6 PM daily, you can specify a number of minutes or hours to wait before the journey runs. When the journey wakes up at 6 PM, it checks for a fresh audience, meaning an audience newer than the one used in the previous journey execution. During the specified time window, the journey will execute immediately upon detecting the fresh audience. If no fresh audience is detected, the journey execution will be skipped for that day.

+++

<!--
### Segment filters {#segment-filters}

[!CONTEXTUALHELP]
>id="jo_segment_filters"
>title="About segment filters"
>abstract="This option targets only the individuals who entered or exited a specific segment during a specific time window. For example, it can retrieve only the customers who entered the VIP segment since last week."

You can choose to target only the individuals who entered or exited a specific segment during a specific time window. For example, you can decide to only retrieve all the customers who entered the VIP segment since last week. Only the new VIP customers will be targeted. All the customers who were already part of the VIP segment before will be excluded.

To activate this mode, click the **Segment Filters** toggle. Two fields are displayed:

**Segment membership**: choose whether you want to listen to segment entrances or exits. 

**Lookback window**: define when you want to start to listen to entrances or exits. This lookback window is expressed in hours, starting from the moment the journey is triggered.  If you set this duration to 0, the journey will target all members of the segment. For recurring journeys, it will take into account all entrances/exits since the last time the journey was triggered.
-->

## Test and publish the journey {#testing-publishing}

The **[!UICONTROL Read Audience]** activity allows you to test the journey on a unitary profile.

To do this, activate the test mode.

![Test mode interface for Read Audience activity with test profile selection](assets/read-segment-test-mode.png)

Configure and run the test mode as usual. [Learn how to test a journey](testing-the-journey.md).

Once the test is running, the **[!UICONTROL Show logs]** button allows you to see the test results. For more on this, refer to [this section](testing-the-journey.md#viewing_logs)

![Test logs showing audience execution results and profile flow](assets/read-segment-log.png)

Once the tests are successful, you can publish your journey (see [Publishing the journey](../building-journeys/publish-journey.md)). Individuals belonging to the audience will enter the journey on the date/time specified in the journey's properties **[!UICONTROL Scheduler]** section.

>[!NOTE]
>
>For recurring audience-based journeys, the journey will automatically close once its last occurrence is executed. If no end date/time has been specified, you will have to close the journey to new entrances manually to end it.

## Audience targeting in journeys {#audience-targeting-in-journeys}

Audience-based journeys always start with a **Read Audience** activity to retrieve individuals belonging to an [!DNL Adobe Experience Platform] audience. Those profiles are read once or on a recurring schedule.

After they enter the journey, you orchestrate them using **Condition** activities: segment by attributes or behavior, exclude part of the population, or merge branches back together (union). The sections below describe each pattern.

**Segmentation**

You can use conditions to perform segmentation using the **Condition** activity. For example, you can make VIP persons take a particular path and non-VIP flow in another path.

The segmentation can be based on:

* data source data
* the context of events part of the journey data, for example: did a person click on the message received an hour ago?
* a date, for example: are we in June when a person goes through the journey?
* a time, for example: is it morning in the person's timezone?
* an algorithm splitting the audience flowing in the journey based on a percentage, for example: 90% - 10% to exclude a control group

![Condition activity for audience segmentation into VIP and non-VIP paths](assets/read-segment-audience1.png)

>[!NOTE]
>
>When using the "Daily" scheduler type with a **[!UICONTROL Read Audience]** activity, you can define a time window for the journey to wait for fresh audience data. This ensures accurate targeting and prevents issues caused by delays in batch segmentation jobs. [Learn how to schedule a journey](#schedule)

**Exclusion**

The same **Condition** activity used for segmentation (see above) also allows you to exclude part of the population. For example, you can exclude VIP persons by making them flow into a branch with an end step right after.

This exclusion could happen right after audience retrieval, for population counting purposes or along a multistep journey.

![Journey path with exclusion branch using End activity](assets/read-segment-audience2.png)

**Union**

Journeys allow you to create N branches and join them together after a segmentation. As a result, you can make two audiences return to a common experience.

For example, after following a different experience during ten days in a journey, VIP and non-VIP customers can return to the same path. After a union, you can split the audience again by performing a segmentation or an exclusion.

![Journey paths merging back together after segmentation using union](assets/read-segment-audience3.png)

## Troubleshooting {#audience-count-mismatch}

This section helps you resolve **audience count mismatches** (fewer or more profiles entering than expected), **zero profiles processed** (Read Audience alert or no entries), and **delayed or missing entries** (timing and data propagation).

>[!NOTE]
>
>When a Read Audience activity executes, the system generates internal events (called `segmentExportJob` events) to track the lifecycle of the audience export operation. These events are recorded at the activity level, not per individual profile, and can be queried for monitoring and troubleshooting purposes. Learn more about [querying Read Audience events](../reports/query-examples.md#read-segment-queries).

**Find your issue:**

| Symptom | Go to |
|---------|--------|
| Fewer (or more) profiles entered than the audience size | [Timing and data propagation](#timing-and-data-propagation), [Data validation and monitoring](#data-validation-and-monitoring) |
| Read Audience processed zero profiles; alert fired | [Zero profiles processed](#zero-profiles-processed) |
| Entries delayed or missing for batch audiences | [Timing and data propagation](#timing-and-data-propagation) |
| Need to verify segment job status or namespace | [Data validation and monitoring](#data-validation-and-monitoring) |

### Zero profiles processed {#zero-profiles-processed}

If the **Read Audience** activity has not processed any profile (e.g. you see the [Read Audience alert](../reports/alerts.md#alert-read-audiences)):

1. **Check if the audience is empty** – In [!DNL Adobe Experience Platform], verify the audience size and that profiles are in **Realized** status. An empty or not-yet-evaluated audience will result in zero entries.
2. **Check namespace** – The namespace selected in the Read Audience activity must be present on the profiles in your audience. Profiles without that identity cannot enter the journey. [Learn more about namespaces](../event/about-creating.md#select-the-namespace).
3. **Review Alerts and retries** – Failures are reported in **Alerts**. The system retries export job creation every 10 minutes for up to 1 hour. [Learn more about retries and alerts](#read-audience-retry).

If the issue persists after these checks, see [Timing and data propagation](#timing-and-data-propagation) and [Data validation and monitoring](#data-validation-and-monitoring) for batch and configuration causes.

### Timing and data propagation {#timing-and-data-propagation}

* **Batch segmentation job completion**: For batch audiences, ensure that the daily batch segmentation job has completed and snapshots are updated before the journey runs. Batch audiences become ready for use approximately **2 hours** after segmentation job completion. Learn more about [audience evaluation methods](https://experienceleague.adobe.com/docs/experience-platform/segmentation/home.html#evaluate-segments){target="_blank"}.

* **Data ingestion timing**: Verify that profile data ingestion has fully completed before the journey execution. If profiles were ingested shortly before the journey starts, they may not be reflected in the audience yet. Learn more about [data ingestion in [!DNL Adobe Experience Platform]](https://experienceleague.adobe.com/docs/experience-platform/ingestion/home.html){target="_blank"}.

* **Use "Trigger after batch audience evaluation" option**: For daily scheduled journeys using batch audiences, consider enabling the **[!UICONTROL Trigger after batch audience evaluation]** option. This ensures the journey waits for fresh audience data (up to 6 hours) before executing. [Learn more about scheduling](#schedule)

* **Add a Wait activity**: For streaming audiences with recently ingested data, consider adding a **Wait** activity at the beginning of the journey to allow time for data propagation and profile qualification. [Learn more about the Wait activity](wait-activity.md)

* **`inAudience()` condition timing:** When using `inAudience()` in a condition node within a Read Audience journey, segment membership is read from the batch projection of the profile. Data in this projection is refreshed within **2 hours** after ingestion. For full details on propagation timing scenarios, refer to the [inAudience function documentation](functions/functioninaudience.md#propagation-timing).

### Data validation {#data-validation-and-monitoring}

* **Check segmentation job status**: Monitor batch segmentation job completion times in the [!DNL Adobe Experience Platform] [monitoring dashboard](https://experienceleague.adobe.com/docs/experience-platform/dataflows/ui/monitor-segments.html){target="_blank"}. Use it to verify when audience data is ready.

* **Verify merge policies**: Ensure that the merge policy configured for your audience matches the expected behavior for combining profile data from different sources. Learn more about [merge policies in [!DNL Adobe Experience Platform]](https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/overview.html){target="_blank"}.

* **Review segment definitions**: Confirm that segment definitions are configured correctly and include all expected qualification criteria. Learn more about [building audiences](../audience/creating-a-segment-definition.md). Pay special attention to:
    * Time-based conditions that may exclude profiles based on event timestamps
    * Attribute qualifications that depend on recently updated data
    * Streaming vs. batch evaluation methods

* **Validate namespace configuration**: Ensure the namespace selected in the **Read Audience** activity matches the primary identity used by profiles in your audience. Profiles without the selected namespace will not enter the journey. Learn more about [identity namespaces](../event/about-creating.md#select-the-namespace).

### Best practices

* **Schedule journeys after segmentation**: For batch audiences, schedule journey execution at least 2-3 hours after the typical batch segmentation job completion time. [Learn more about journey scheduling](#schedule)

* **Use streaming audiences for real-time use cases**: If you need immediate profile qualification and journey entry, use [Audience Qualification](audience-qualification-events.md) activities with streaming audiences instead of **Read Audience** with batch audiences.

* **Test with smaller audiences first**: Before launching large-scale journeys, test with a smaller subset to validate that counts match expectations. [Learn how to test a journey](testing-the-journey.md)

* **Monitor regularly**: Set up regular monitoring of audience sizes and journey entry metrics to detect discrepancies early. Learn more about [journey processing rates and entry management](entry-management.md).

### When to contact support

If count mismatches or zero-profile runs persist after following the steps above, contact Adobe support. Have ready: audience name/ID, journey name/ID, scheduled run time(s), sandbox, and a short description of the discrepancy (e.g. "Audience shows 10K realized, only 2K entered the journey on [date]").

## Retries {#read-audience-retry}

Retries are applied by default on audience-triggered journeys (starting with a **Read Audience** or a **Business Event**) while retrieving the export job. If an error occurs during the export job creation, retries will be made every 10mn, for 1 hour max. After that, we will consider it as a failure. Those types of journeys can therefore be executed up to 1 hour after the scheduled time.

Unsuccessful **Read Audience** triggers are captured and displayed in **Alerts**. The **Read Audience alert** warns you if a **Read Audience** activity has not processed any profile 10 minutes after the scheduled execution time. This failure can be caused by technical issues or an empty audience. If the failure is due to technical issues, retries can still occur depending on the issue type. For example, if export job creation fails, we retry every 10 minutes for up to 1 hour. [Learn more](../reports/alerts.md#alert-read-audiences)

For the full list of Read Audience guardrails (including retry and throughput limits), see [Guardrails and limitations](../start/guardrails.md#read-segment-g).

## Related topics

* [Build audiences](../audience/about-audiences.md) - Create and manage the audience segments you want to target in your Read Audience journeys.
* [Audience Qualification activity](audience-qualification-events.md) - Trigger journeys in real time as profiles enter or exit an audience, instead of processing them in batch.
* [Use supplemental identifiers in journeys](supplemental-identifier.md) - Extend Read Audience journeys to target secondary entities such as bookings, contracts, or subscriptions linked to a profile.
* [Guardrails and limitations](../start/guardrails.md#read-segment-g) - Review throughput limits, retry behavior, and audience size thresholds before launching at scale.
* [Journey processing rates and entry management](entry-management.md) - Understand how profiles are injected into the journey and what controls entry and re-entry.
* [Test a journey](testing-the-journey.md) - Validate your journey logic using test profiles before going live.
* [Publish a journey](../building-journeys/publish-journey.md) - Activate your journey and monitor its initial execution.
* [Send a message to subscribers](message-to-subscribers-uc.md) - End-to-end use case: target a subscription list with a Read Audience journey, from setup to delivery.
* [Best practices for Read Audience journeys](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/mastering-read-audience-journeys-in-adobe-journey-optimizer-a/ba-p/761445){target="_blank"} - Community blog covering common pitfalls, count discrepancies, and proven best practices.

## How-to video {#video}

Understand the applicable use cases for a journey that is triggered by the read audience activity. Learn how to build batch-based journeys and which best practices to apply.

>[!VIDEO](https://video.tv.adobe.com/v/3424997?quality=12)

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and use the Read Audience activity in Adobe Journey Optimizer to add profiles from an Adobe Experience Platform audience into a journey, either once or on a recurring schedule, with guidance on scheduling, throughput, troubleshooting, and best practices.

**Intents:**
* Configure a Read Audience activity as the entry point of a journey
* Select an Adobe Experience Platform audience and identity namespace for the journey
* Set the reading rate to control how many profiles enter per second
* Schedule a journey to run once, daily, weekly, or on a custom recurrence
* Enable Incremental read to process only new audience members on recurring runs
* Troubleshoot audience count mismatches, zero-profile runs, and delayed entries
* Decide between Read Audience and Audience Qualification based on batch vs. real-time needs

**Glossary:**
* **Read Audience activity**: The journey entry-point activity that reads all qualified profiles from a selected Adobe Experience Platform audience and adds them to the journey *(product-specific)*
* **Reading rate**: The maximum number of profiles that can enter the journey per second (500–20,000; default 5,000) *(product-specific)*
* **Incremental read**: A recurring journey option that processes only profiles newly added to the audience since the last journey execution *(product-specific)*
* **Force reentrance on recurrence**: A scheduling option that removes all active journey participants before each new run so profiles can re-enter fresh *(product-specific)*
* **Trigger after batch audience evaluation**: A scheduling option that delays journey execution until a fresh batch audience snapshot is available (up to 6 hours) *(product-specific)*
* **Supplemental identifier**: A secondary identifier (e.g., order ID) that allows the same profile to enter the journey multiple times when the identifier differs *(product-specific)*

**Guardrails:**
* Only one Read Audience activity is allowed per journey, and it must be the first activity.
* Only one audience can be selected per Read Audience activity.
* Up to five concurrent Read Audience runs per organization.
* Maximum reading rate is 20,000 profiles per second per sandbox (sum of all concurrent Read Audience activities).
* Reading rate is limited to 500 profiles per second when a supplemental identifier is used.
* Only profiles with Realized audience participation status enter the journey.
* Only people-based identity namespaces are available; profiles without the selected namespace cannot enter.
* The 12-hour job timeout applies to Read Audience export jobs.
* Retries for failed export jobs occur every 10 minutes for up to 1 hour.
* For custom upload audiences with Incremental read enabled, profiles are only retrieved on the first recurrence (these audiences are fixed).
* Scale the Winner is not available for Read Audience journeys (path experimentation).

**Terminology:**
* Canonical name: Read Audience — Acronym: none — variants: segment-trigger, audience-based journey entry, Read Segment (legacy API name)
* Synonyms: "Read Audience" = "segment trigger" = "audience-triggered journey"
* Do not confuse: "Read Audience" ≠ "Audience Qualification" (Read Audience is batch/scheduled; Audience Qualification is real-time streaming)

**FAQ:**
* **Q: When should I use Read Audience instead of Audience Qualification?** — Use Read Audience for batch, scheduled use cases (e.g., weekly newsletters, re-engagement campaigns). Use Audience Qualification when profiles must enter the journey immediately as they qualify in real time.
* **Q: Why are fewer profiles entering the journey than the audience size?** — Common causes include profiles not having the selected namespace, batch segmentation jobs not yet completed before the journey ran, or profiles not being in Realized status. Enable "Trigger after batch audience evaluation" and check namespace configuration.
* **Q: What does Incremental read do on the first run?** — On the first execution, all audience profiles enter. On subsequent runs, only profiles newly added to the audience since the last execution are processed.
* **Q: What happens if the export job fails?** — The system retries every 10 minutes for up to 1 hour. Failures are reported in Alerts. After 1 hour without success, the run is considered failed.
* **Q: Can the same profile enter a Read Audience journey multiple times?** — Yes, if a supplemental identifier is configured and differs between entries, or if Force reentrance on recurrence is enabled. Without these, a profile cannot be present multiple times at the same time.
* **Q: How long does a one-shot Read Audience journey remain live?** — It auto-stops to Stopped when the last profile exits, unless the journey includes Wait, Reaction, or event-triggered transitions — in which case the 91-day global timeout applies. It does not remain Live until Finished at 91 days by default.

+++
