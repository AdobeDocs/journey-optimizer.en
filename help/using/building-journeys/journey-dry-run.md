---
solution: Journey Optimizer
product: journey optimizer
title: Journey Dry run
description: Learn how to publish a journey in Dry run mode
feature: Journeys
role: User
level: Intermediate
badge: label="Limited availability" type="Informative"
keywords: publish, journey, live, validity, check
exl-id: 58bcc8b8-5828-4ceb-9d34-8add9802b19d
---
# Journey Dry run {#journey-dry-run}

>[!CONTEXTUALHELP]
>id="ajo_journey_dry_run"
>title="Dry run mode"
>abstract="This journey is in Dry run. Journey Dry run is a special journey publication mode in Adobe Journey Optimizer that allows journey practitioners to test a journey using real production data without contacting real customers or updating profile information.  This feature helps journey practitioners gain confidence in their journey design and audience targeting before publishing it live."


>[!CONTEXTUALHELP]
>id="ajo_journey_dry_run_start"
>title="Publish a journey in dry run mode"
>abstract="Journey Dry run is a special journey publication mode in Adobe Journey Optimizer that allows journey practitioners to test a journey using real production data. Once you designed your journey, execute a dry run to confirm it is functional and ensure steps are correct. This publication mode lets you smoke test a journey, without sending communication to any profile."

Journey Dry run is a special journey publication mode in Adobe Journey Optimizer that allows journey practitioners to test a journey using real production data without contacting real customers or updating profile information.  This feature helps journey practitioners gain confidence in their journey design and audience targeting before publishing it live. 


>[!AVAILABILITY]
>
>This capability is only available for a set of organizations (Limited Availability), and will be rolled out globally in a future release.


## Key benefits {#journey-dry-run-benefits}

Journey Dry run boosts practitioner confidence and journey success by enabling safe, data-driven testing of customer journeys using real production data—without the risk of contacting customers or altering profile information. This feature empowers journey practitioners to validate audience reach and branch logic before going live, ensuring that journeys align with their intended business goals.

With Journey Dry run, you gain the ability to identify issues early, optimize targeting strategies, and improve journey design based on actual data—not assumptions. Integrated directly into the journey canvas, Dry run delivers intuitive reporting and visibility into key performance indicators, allowing teams to iterate confidently and streamline approval workflows. This enhances operational efficiency, reduces launch risk, and drives better customer engagement outcomes.

Ultimately, this feature improves time-to-value and reduces journey failures.

Journey Dry run brings:

1. **Safe testing environment**: Profiles in Dry run mode are not contacted, ensuring no risk of sending communications or impacting live data. 
1. **Audience insights**: Journey practitioners can predict audience reachability at various journey nodes, including opt-outs, exclusions, and other conditions. 
1. **Real-Time feedback**: Metrics are displayed directly in the journey canvas, similar to live reporting, enabling journey practitioners to refine their journey design. 

During the Dry run, the journey is executed with the following specificities:

* **Channel action** nodes including Email, SMS or Push notifications are not executed
* **Custom actions** are disabled during Dry run, and their responses are set to null
* **Wait nodes** are bypassed during Dry run.
        <!--You can override the wait block timeouts, then if you have wait blocks duration longer than allowed dry run journey duration, then that branch will not execute completely.-->
* **Data sources**, including external data sources, are executed by default

>[!CAUTION]
>
>* Permissions to start Dry Run are restricted to users with the **[!DNL Publish journeys]** high-level permission. Permissions to stop Dry Run are restricted to users with the **[!DNL Manage journeys]** high-level permission. Learn more about managing [!DNL Journey Optimizer] users' access rights in [this section](../administration/permissions-overview.md).
>
>* Before starting using the Dry run capability, [read out the Guardrails and Limitations](#journey-dry-run-limitations).


## Start a Dry run {#journey-dry-run-start}

You can use the Dry run capability in any Draft journey with no error.

To activate Dry run, follow these steps:

1. Open the journey you want to test. 
1. Select the **Dry run** button.

    ![Start the journey dry run](assets/dry-run-button.png)

1. Confirm the publication.

    A status message, **Activating Dry run**, appears while the transition is happening.

1. Once activated, the journey enters **Dry run** mode. 

## Monitor a Dry run {#journey-dry-monitor}

Once the Dry mode publication is launched, you can visualize the journey execution and how profiles progress through journey branches and nodes.

Metrics are displayed directly in the journey canvas.

![Monitor the journey dry run execution](assets/dry-run-metrics.png)

For each activity, in their activity box, you can check:

* **[!UICONTROL Entered]**: Total number of individuals who entered this activity. For **Action** activities, as they are not executed in Dry run mode, this metric indicates profiles passing through.
* **[!UICONTROL Exited (met exit criteria)]**: Total number of individuals who exited the journey from that activity, due to an exit criteria.
* **[!UICONTROL Exited (forced exit)]**: Total number of individuals who exited the journey while it was paused due to a journey practitioner configuration. This metric is always equals to zero for journeys in Dry run mode.
* **[!UICONTROL Error]**: Total number of individuals who had an error on that activity.


At the journey level, on the top left section of the canvas, you can check: 

* The total number of **Entered profiles**
* The total number of **Exited profiles**
* The total number of **Profiles in error**
* The total number of **Discarded profiles** in the journey

You can also access the **Last 24-hours reports** and **All-time reports** for the Dry run. To access these reports, click the **View report** button  on the upper-right corner of the journey canvas. 

![Access the reports for the journey dry run execution](assets/dry-run-report.png)

>[!CAUTION]
>
> Reporting data is available only when the Dry run is **active**.  Once stopped, reporting data will no longer be accessible. Use the **Export** button above the reports to download them if needed.


## Stop a Dry run {#journey-dry-run-stop}

Dry run journeys **must** be stopped manually. 

Click the **Close** button to end the test, and click **Back to Draft** to confirm.

<!-- After 14 days, Dry run journeys automatically transition to the **Draft** status.-->

## Guardrails and limitations {#journey-dry-run-limitations}

* The Dry run mode is not available for journeys containing reaction events
* Profiles in Dry run mode are counted towards engageable profiles 
* Journeys in Dry run mode are counted towards live journey quota
* Dry run journeys do not impact business rules
* When creating a new journey version, if a previous journey version is **Live**, then the Dry run activation is not allowed on the new version.
* Journey Dry run generates stepEvents. These stepEvents have a specific flag and Dry run ID:
    * `_experience.journeyOrchestration.stepEvents.inDryRun` returns `true` if the Dry run is activated, and `false` otherwise 
    * `_experience.journeyOrchestration.stepEvents.dryRunID` returns the ID of a dry run instance

* When analysing journey reporting metrics using Adobe Experience Platform Query service, Dry Run-generated step events must be excluded. To perform this, set the `inDryRun` flag to `false`.