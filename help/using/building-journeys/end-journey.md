---
solution: Journey Optimizer
product: journey optimizer
title: Journey ending
description: Learn how a journey ends in Journey Optimizer
feature: Journeys
role: User
level: Intermediate
keywords: reenter, journey, end, live, stop
exl-id: ea1ecbb0-12b5-44e8-8e11-6d3b8bff06aa
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/-mknoNfkNCnfnLD1UCiA6C88NjookKqGr5tQdJ-f3T4
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: d7dd6f7f-9e2a-47ee-a2bc-b7b9caaefc1d
    internal-label: Profile entrance management
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
---
# End a journey {#journey-ending}

>[!BEGINSHADEBOX]

**On this page:** Learn how journeys end both for individual profiles and overall, and how to close or stop a live journey when you need to halt new entrances or all processing.

>[!ENDSHADEBOX]

>[!TIP]
>
>Looking for practical guidance on when and how profiles should exit journeys? See our [comprehensive guide to journey entry and exit criteria](entry-exit-criteria-guide.md), which includes real-world exit scenarios, best practices, and configuration guidance.

## How a live journey ends

Journeys are closed when the global journey timeout is reached, or after the last occurrence of a recurring audience-based journey. [Learn how journeys are closed](#close-journey).

If you need to terminate a live journey, we recommend that [you close it](#close-to-new-entrances) manually. The arrival of new customers in the journey is then blocked. Profiles who already entered in the journey are able to experience it to the end. 

You can also [stop a journey](#stop-journey), only in case of an emergency and if all journey processing must to be ended immediately. People who already entered a journey are all stopped in their progress. 

>[!IMPORTANT]
>
>* You cannot restart or delete a [closed](#close-journey) or [stopped](#stop-journey) journey. You can [create a new version](publish-journey.md#journey-versions) of it or [duplicate it](journey-ui.md#duplicate-a-journey). 
>
>* Only finished journeys can be deleted. 

## How profiles end a journey 

A journey ends for an individual in two specific contexts:

* The individual reaches at the last activity of a path, then moves to the [End tag](#end-tag).
* The individual reaches at a **Condition** activity (or a **Wait** activity with a condition) and does not match any of the conditions.

The individual can then reenter the journey if reentrance is allowed. [Learn more about entrance/reentrance management](../building-journeys/journey-properties.md#entrance)

## Journey End tag {#end-tag}

While authoring a journey, an End tag is displayed at the end of each path. This node cannot be added by a user, cannot be removed and only its label can be changed. It marks the end of each path of the journey. 

If the journey has several paths, we recommend that you add a label to each end to make reports easier to read. Learn more about [journey reports](../reports/live-report.md).

![End journey action button in journey toolbar](assets/journey-end.png)

## Close a journey {#close-journey}

A journey can close because of the following reasons:

* A non-recurring Read Audience journey **automatically stops** after a safety buffer following its scheduled run. [Learn more](#auto-stop-non-recurring)
* After the last occurrence of a recurring audience-based journey.
* The journey is closed manually via the [**[!UICONTROL Close to new entrances]**](#close-to-new-entrances) button.
* The global journey timeout of 91 days is reached.

After the **91-day journey global timeout**, a Read audience journey switches to the **Finished** status. This behavior is set for 91 days only as all information about profiles who entered the journey is removed 91 days after they entered. Persons still in the journey automatically are impacted. They exit the journey after the 91-day timeout.  Learn more about [the journey global timeout](../building-journeys/journey-properties.md#global_timeout).

### Automatic journey stop for non-recurring audiences {#auto-stop-non-recurring}

A **non-recurring Read Audience journey** automatically transitions to **[!UICONTROL Stopped]** status after a safety buffer following its scheduled run. This eliminates the previous behavior where non-recurring Read Audience journeys remained in **Live** status until the 91-day global timeout expired, even though no profiles were actively flowing through them.

**How it works:**

1. The journey runs and all profiles from the audience are processed.
1. As each profile reaches the end of the journey, it exits normally.
1. After the scheduled run, the journey remains in **[!UICONTROL Live]** status during a safety buffer period.
1. After the safety buffer elapses (~96 hours after the journey's scheduled run time), the journey automatically transitions to **[!UICONTROL Stopped]** status shortly afterward.

This behavior applies to **non-recurring Read Audience journeys** only. Recurring journeys are not affected.

* **Auto-stop timing:** The safety buffer accounts for two windows: a **24-hour idle window** to allow any in-flight sends to complete, and a **72-hour Quiet Hours allowance** (Quiet Hours can defer sends by up to 72 hours). The total buffer is approximately **96 hours (~4 days)** after the journey's scheduled run time. The journey remains in **[!UICONTROL Live]** status during this period. This is expected behavior and does not indicate a problem.

* **Waves-based journeys are excluded:** This auto-stop behavior does not apply to waves-based journeys, and journeys that use Send-Time Optimization. These journeys remain active across all scheduled waves and are stopped only by the standard [91-day global timeout](../building-journeys/journey-properties.md#global_timeout), unless they are closed or stopped manually.

* This auto-stop behavior does **not** apply to non-recurring journeys that include nodes causing waiting periods, such as **Wait** nodes (timer-based), **Reaction** nodes (waiting on events like email open or click), or event-triggered transitions. These journeys remain subject to the standard [91-day global timeout](../building-journeys/journey-properties.md#global_timeout).

* You can still close a non-recurring Read Audience journey manually at any time using the [**[!UICONTROL Close to new entrances]**](#close-to-new-entrances) option. The auto-stop behavior simply ensures the journey stops automatically when it is no longer needed, without requiring manual intervention.

### When is a journey considered "finished"? {#journey-finished-definition}

The definition of "finished" varies depending on the journey type:

| Journey Type | Recurring? | Has end date? | Definition of "finished" |
|--------------|------------|---------------|--------------------------|
| Read audience | No | n/a | ~96h after scheduled run (auto-stop buffer) |
| Read audience | Yes | No | 91 days after last occurrence start |
| Read audience | Yes | Yes | When end date is reached |
| Event-triggered journey | n/a | Yes | When end date is reached |
| Event-triggered journey | n/a | No | When closed in UI or via API |

### Close to new entrances {#close-to-new-entrances}

Closing a journey manually ensures that customers who already entered the journey can finish their path but new users are not able to enter the journey. When a journey is closed (for any of the reasons above), it will have the status **[!UICONTROL Closed]**. The journey stops letting new individuals enter the journey. Profiles already in the journey can finish the journey normally. After the default global timeout of 91 days, the journey will switch to the **Finished** status. 

You can stop a journey from the **Live** or **Paused** state. When the journey is **Paused**, you do not need to resume it to **Live** first. [Learn more about stopping a paused journey](journey-pause.md#stop-close-paused).

To close a journey from the list of journeys, click the **[!UICONTROL Ellipsis]** button that is located to the right of the journey name and select **[!UICONTROL Close to new entrances]**.

![Finish action dropdown in quick actions menu for ending journey](assets/journey-finish-quick-action.png)

You can also:

1. In the **[!UICONTROL Journeys]** list, click the journey you want to close.
1. On the top-right, click the down arrow.

    ![Finish options menu showing end journey and alternative actions](assets/finish_drop_down_list.png){width="50%" zoomable="yes"}

1. Click **[!UICONTROL Close to new entrances]**, and confirm in the dialog box.


## Stop a journey {#stop-journey}

In case you need to stop the progress of all individuals in the journey, you can stop it. Stopping the journey timeout all individuals in the journey. However, stopping a journey involves that people who already entered a journey are all stopped in their progress. The journey is basically switched off. If you want to end to a journey, best practice is [to close it](#close-journey). 

You can also stop a **Paused** journey directly, without resuming it to **Live** first. [Learn more](journey-pause.md#stop-close-paused).

You can stop a journey, for example, if a marketer realizes that the journey targets the wrong audience or a custom action supposed to deliver messages is not working correctly. To stop a journey from the list of journeys, click the **[!UICONTROL Ellipsis]** button that is located to the right of the journey name and select **[!UICONTROL Stop]**.

![Finish action dropdown in quick actions menu for ending journey](assets/journey-finish-quick-action.png)

You can also:

1. In the **[!UICONTROL Journeys]** list, click the journey you want to stop.
1. On the top-right, click the down arrow.

   ![Additional finish options including close journey and cleanup](assets/finish_drop_down_list2.png){width="50%" zoomable="yes"}

1. Click **[!UICONTROL Stop]**, and confirm in the dialog box.

When stopped, the journey status is set to **[!UICONTROL Stopped]**. 

>[!CAUTION]
>
>Stopping a journey requires the **[!DNL Manage journeys]** permission. If the journey includes inline campaigns or messaging nodes, users also need **Campaigns > Publish Campaigns** permissions. If the journey uses assets (for example, in emails), users must have access to those asset folders. Learn more about managing [!DNL Journey Optimizer] users' access rights in [this section](../administration/permissions-overview.md).

## Related topics

* [Journey entry and exit criteria guide](entry-exit-criteria-guide.md) - Complete guide with real-world examples and best practices
* [Profile entrance management](entry-management.md) - Configure how profiles enter journeys
* [Configure exit criteria](journey-properties.md#exit-criteria) - Set up automatic profile removal from journeys
* [Pause a journey](journey-pause.md) - Temporarily halt journey execution

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the different ways a live journey can end — including the global 91-day timeout, manual closure to new entrances, and emergency stop — along with their effects on in-progress profiles.

**Intents:**

* Close a live journey to new entrances while allowing current profiles to complete it
* Stop a journey immediately to halt all in-progress profiles
* Understand the difference between Closed, Stopped, and Finished journey statuses
* Determine when a journey is considered "finished" based on its type and configuration
* Delete a journey once it has reached the Finished status

**Glossary:**

* **End tag**: An auto-generated, non-removable node displayed at the end of each journey path during authoring; its label can be changed *(product-specific)*
* **Close to new entrances**: A manual action that prevents new profiles from entering a journey while allowing existing profiles to complete their path *(product-specific)*
* **Global journey timeout**: The 91-day maximum duration after which a journey automatically switches to Finished status and all profile data is removed *(product-specific)*
* **Stopped status**: A journey state in which all in-progress profiles are immediately halted; used only for emergencies *(product-specific)*

**Guardrails:**

* Closed and Stopped journeys cannot be restarted or deleted; only a new version or duplicate can be created.
* Only journeys in Finished status can be deleted.
* Stopping a journey requires the Manage journeys permission; journeys with inline campaigns or messaging nodes also require Campaigns > Publish Campaigns permission.
* After the 91-day global timeout, all profile journey data is removed and remaining profiles are automatically exited.
* A non-recurring Read Audience journey without long-running Wait, Reaction, or event-triggered nodes automatically transitions to Stopped approximately 96 hours (~4 days) after its scheduled run. The journey remains in Live status during this buffer. Waves-based journeys, and journeys that use Send-Time Optimization, are excluded from this auto-stop and remain subject to the 91-day global timeout unless manually closed or stopped.

**Terminology:**

* Canonical name: Close to new entrances — Acronym: n/a — variants: close journey, manually close
* Synonyms: "Stopped" journey ≠ "Closed" journey — stopped halts all profiles immediately; closed only blocks new entrances
* Do not confuse: "End tag" ≠ "End activity" — the End tag is auto-generated and cannot be removed; the End activity is a placeable canvas node

**FAQ:**

* **Q: What is the difference between closing and stopping a journey?** — Closing blocks new entrances but lets existing profiles finish; stopping immediately halts all profiles in their tracks.
* **Q: Why does a non-recurring journey remain in Live status for several days after its run?** — This is expected. AJO applies a safety buffer of ~96 hours (~4 days): 24 hours to allow in-flight sends to complete, plus 72 hours for Quiet Hours deferrals. The journey transitions to Stopped shortly after the buffer elapses.
* **Q: Do waves-based journeys auto-stop after ~96 hours?** — No. Waves-based journeys, and journeys that use Send-Time Optimization, are excluded from this automatic stop so they can stay active across all scheduled waves. They follow the standard 91-day journey timeout unless closed or stopped manually.
* **Q: When does a Read audience journey reach Finished status?** — For a non-recurring Read Audience journey: it auto-stops to Stopped approximately 96 hours (~4 days) after its scheduled run (safety buffer: 24h idle window + 72h Quiet Hours allowance). The journey remains in Live status during this buffer. If Wait, Reaction, or event nodes keep profiles active, the standard 91-day global timeout applies instead. Finished is reached when a Closed journey hits the 91-day global timeout, or per recurring-journey rules in the finished-definition table.
* **Q: Can I delete a Closed journey?** — No, only Finished journeys can be deleted.
* **Q: What happens to profiles still in a journey when the 91-day timeout hits?** — They are automatically exited from the journey at that point.
* **Q: Do I need special permissions to stop a journey?** — Yes, the Manage journeys permission is required, plus Campaigns > Publish Campaigns if the journey contains inline campaigns or messaging nodes.

+++
