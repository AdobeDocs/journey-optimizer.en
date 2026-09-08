---
solution: Journey Optimizer
product: journey optimizer
title: Journey Dry run
description: Learn how to publish a journey in Dry run mode
feature: Journeys
role: User
level: Intermediate
keywords: publish, journey, live, validity, check
exl-id: 58bcc8b8-5828-4ceb-9d34-8add9802b19d
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/a7qFw84obtkCRDmiqMxQNgvqhI4b6t5suROeF7ZPh1I
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
  - id: baecb07f-ce89-4ebb-9cd9-0f7c053f944f
    internal-label: Journey management
subfeature_v2:
  - id: b15c7c2e-788c-4eb7-86a8-390565b0d2c9
    internal-label: Journey design
  - id: b32bb433-f8c6-4931-8e52-e657230a3bf2
    internal-label: Audiences
  - id: cfba2953-2ce9-4b00-a00c-71cd338ae63f
    internal-label: Custom actions
  - id: d8353d85-5da7-453d-bd68-40ad33fa0ab7
    internal-label: Action activities
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
  - id: b5520579-b31f-4df7-9281-f0d9f91e2edc
    internal-label: Customer engagement
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
---
# Journey Dry run {#journey-dry-run}

>[!BEGINSHADEBOX]

**On this page:** Learn how to publish a journey in Dry run mode to test it with real production data without contacting real customers or updating profiles, so you can validate your design before going live.

>[!ENDSHADEBOX]

Not sure Dry run is the right method for you? [Compare all three validation options](choose-validation-method.md).

>[!CONTEXTUALHELP]
>id="ajo_journey_dry_run"
>title="Dry run mode"
>abstract="This journey is in Dry run. Journey Dry run is a special journey publication mode in [!DNL Adobe Journey Optimizer] that allows journey practitioners to test a journey using real production data without contacting real customers or updating profile information.  This feature helps journey practitioners gain confidence in their journey design and audience targeting before publishing it live."


>[!CONTEXTUALHELP]
>id="ajo_journey_dry_run_start"
>title="Publish a journey in dry run mode"
>abstract="Journey Dry run is a special journey publication mode in [!DNL Adobe Journey Optimizer] that allows journey practitioners to test a journey using real production data. Once a journey is designed, a dry run confirms it is functional and ensures steps are correct. This publication mode lets you smoke test a journey, without sending communication to any profile."

Journey Dry run is a special journey publication mode in [!DNL Adobe Journey Optimizer] that allows journey practitioners to test a journey using real production data without contacting real customers or updating profile information.  This feature helps journey practitioners gain confidence in their journey design and audience targeting before publishing it live. 

➡️ [Learn more about journey dry run in this video](#dry-run-video)

## Key benefits {#journey-dry-run-benefits}

Journey Dry run boosts practitioner confidence and journey success by enabling safe, data-driven testing of customer journeys using real production data—without the risk of contacting customers or altering profile information. This feature empowers journey practitioners to validate audience reach and branch logic before going live, ensuring that journeys align with their intended business goals.

With Journey Dry run, you gain the ability to identify issues early, optimize targeting strategies, and improve journey design based on actual data—not assumptions. Integrated directly into the journey canvas, Dry run delivers intuitive reporting and visibility into key performance indicators, allowing teams to iterate confidently and streamline approval workflows. This enhances operational efficiency, reduces launch risk, and drives better customer engagement outcomes.

Ultimately, this feature improves time-to-value and reduces journey failures.

Journey Dry run brings:

1. **Safe testing environment**: Profiles in Dry run mode are not contacted, ensuring no risk of sending communications or impacting live data. 
1. **Audience insights**: Journey practitioners can predict audience reachability at various journey nodes, including opt-outs & exclusions based on Journey conditions.
1. **Real-Time feedback**: Metrics are displayed directly in the journey canvas, similar to live reporting, enabling journey practitioners to refine their journey design. 

## Dry run execution logic {#journey-dry-run-exec}

During the Dry Run, the journey runs in simulation mode, applying the following specific behaviors to each journey activity without triggering real actions:

* **Channel action** nodes including Email, SMS or Push notifications are not executed. 
* **Custom actions** are disabled during Dry run, and their responses are set to null.

  To enhance readability, custom actions and channel activities appear greyed out during the execution of a Dry run.

  ![Greyed out action activities in a Dry run journey](assets/dry-run-greyed-activities.png){width="80%"}

* **Data sources**, including external data sources, and **Wait** activities are disabled by default during Dry run. However you can change this behavior [when activating the Dry run mode](#journey-dry-run-start).

* **Reaction** nodes are not executed: all profiles entering it will exit with success. However, the following priority rules apply:

  * If a **Reaction** node is used with one or multiple **unitary event** nodes in parallel, profiles will always go through the reaction event.
  * If a **Reaction** node is used with one or multiple **reaction event** nodes in parallel, profiles will always go though the first one in the canvas (the one at the top).

* **Read Audience** activities with a scheduled execution time (daily, weekly, or monthly) do not follow the time configured in the journey — the schedule is anchored to the moment Dry run was activated. For example, if your journey is set to run daily at 10 AM but you activate the Dry run at 8 AM, all subsequent scheduled reads during the Dry run execute at 8 AM.

>[!CAUTION]
>
>* Permissions to start a Dry run are restricted to users with the **[!DNL Publish journeys]** high-level permission. Permissions to stop a Dry run are restricted to users with the **[!DNL Manage journeys]** high-level permission. Learn more about managing [!DNL Journey Optimizer] users' access rights in [this section](../administration/permissions-overview.md).
>
>* Before starting using the Dry run capability, [read out the Guardrails and Limitations](#journey-dry-run-limitations).

## Start a Dry run {#journey-dry-run-start}

You can use the Dry run capability in any Draft journey with no error.

To activate Dry run, follow these steps:

1. Open the journey you want to test. 
1. Select the **[!UICONTROL Dry run]** button.

    ![Start the journey dry run](assets/dry-run-button.png)

1. Select the if you want to enable or disable **Wait** activities and **External data sources** calls, and confirm the Dry run publication.

    ![Confirm the journey dry run publication](assets/dry-run-publish.png){width="50%"}

    A status message, **[!UICONTROL Activating Dry run]**, appears while the transition is happening.

1. Once activated, the journey enters **[!UICONTROL Dry run]** mode. 


## Monitor a Dry run {#journey-dry-monitor}

Once the Dry mode publication is launched, you can visualize the journey execution and how profiles progress through journey branches and nodes.

Metrics are displayed directly in the journey canvas. Learn more about journey live reporting and metrics, in [Live report in the journey canvas](report-journey.md). 

![Monitor the journey dry run execution](assets/dry-run-metrics.png)

You can also access the **Last 24-hours reports** and **All-time reports** for the Dry run. To access these reports, click the **View report** button  on the upper-right corner of the journey canvas. 

![Access the reports for the journey dry run execution](assets/dry-run-report.png)

>[!CAUTION]
>
> Reporting data is available only when the Dry run is **active**.  Once stopped, reporting data will no longer be accessible. Use the **Export** button above the reports to download them if needed.


## Stop a Dry run {#journey-dry-run-stop}

After 14 days, Dry run journeys automatically transition to the **[!UICONTROL Draft]** status.

Dry run journeys can also be stopped manually. To deactivate the Dry run mode, follow these steps:

1. Open the Dry run journey you want to stop. 
1. Select the **[!UICONTROL Close]** button to end the test.
    Links to last 24h and all time reports are available in the confirmation screen.

    ![Stop the journey dry run execution](assets/dry-run-stop.png){width="50%"}

1. Click **[!UICONTROL Back to Draft]** to confirm.


## Guardrails and limitations {#journey-dry-run-limitations}

* Profiles in Dry run mode are counted towards [Engageable Profiles](../audience/license-usage.md)
* Journeys in Dry run mode are counted towards live journey quota
* Dry run journeys do not impact business rules
<!--* When creating a new journey version, if a previous journey version is **Live**, then the Dry run activation is not allowed on the new version.-->
* **Jump** actions are not enabled in Dry run. 
    When a source journey triggers a **Jump** event to a destination one, that jump event would not be applicable to a Dry run journey version. For instance, if the latest version of a journey is in Dry run and the previous one is **Live**, then the jump event would ignore the Dry run version and only be applicable for the **Live** one.

## Journey step events and dry run {#journey-step-events}

Journey Dry run generates **stepEvents**. These stepEvents have a specific flag and Dry run ID: `inDryRun` and `dryRunID`.

![Journey dry run schema attributes](assets/dry-run-attributes.png)

* `_experience.journeyOrchestration.stepEvents.inDryRun` returns `true` when the journey is in Dry run mode, and `null` for test or live journeys (non–dry run).
* `_experience.journeyOrchestration.stepEvents.dryRunID` returns the ID of the dry run instance when in Dry run mode; for test or live journeys, it is `null`.


If you export stepEvent data to **external systems**, you can filter Dry run executions using the `inDryRun` flag.

When analyzing **journey reporting metrics** using [!DNL Adobe Experience Platform] Query service, Dry Run-generated step events must be excluded. To do this, exclude step events where `inDryRun` is `true` (i.e. include only events where `inDryRun` is `null` or `false`).

## Frequently asked questions {#faq}

**Does a Dry run send messages to real customers?**

No. Dry run uses real production data but does not contact profiles or update profile information. Channel actions (Email, SMS, Push) are not executed, and custom actions are disabled with their responses set to `null`.

**What permissions do I need to start or stop a Dry run?**

Starting a Dry run requires the **[!DNL Publish journeys]** high-level permission. Stopping a Dry run requires the **[!DNL Manage journeys]** high-level permission. Learn more in the [permissions section](../administration/permissions-overview.md).

**On which journeys can I run a Dry run?**

You can use Dry run on any **[!UICONTROL Draft]** journey that has no error.

**How long does a Dry run last?**

After 14 days, Dry run journeys automatically transition back to the **[!UICONTROL Draft]** status. You can also stop a Dry run manually at any time.

**Are Wait activities and external data sources executed during a Dry run?**

By default, **Wait** activities and **Data sources** (including external data sources) are disabled during a Dry run. You can change this behavior when [activating the Dry run mode](#journey-dry-run-start).

**Do Dry run profiles and journeys count towards my quotas?**

Yes. Profiles in Dry run mode count towards [Engageable Profiles](../audience/license-usage.md), and journeys in Dry run mode count towards the live journey quota. However, Dry run journeys do not impact business rules.

**Can I still access Dry run reports after stopping the test?**

No. Reporting data is available only while the Dry run is **active**. Once stopped, the data is no longer accessible — use the **Export** button above the reports to download it beforehand if needed.

**How do I exclude Dry run data from my reporting?**

Dry run generates **stepEvents** flagged with `inDryRun` and a `dryRunID`. When analyzing journey reporting metrics with [!DNL Adobe Experience Platform] Query service, exclude step events where `inDryRun` is `true` (include only events where `inDryRun` is `null` or `false`).

**Does the scheduled execution time of a Read Audience activity change in Dry run?**

Yes. For journeys using a **Read Audience** activity with a scheduled time (daily, weekly, or monthly), the Dry run anchors the schedule to the moment Dry run was activated — not the time configured in the journey. For example, if the journey is set to run at 10 AM but you activate the Dry run at 8 AM, all daily reads during the Dry run execute at 8 AM.

## How-to video {#dry-run-video}

Learn how to dry run your journeys in this video.

>[!VIDEO](https://video.tv.adobe.com/v/3464681/?learn=on&enablevpops)

{{$include /help/_includes/do-not-localize/building-journeys/ai-augmented-journey-dry-run.md}}
