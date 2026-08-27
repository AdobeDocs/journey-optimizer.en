---
solution: Journey Optimizer
product: journey optimizer
title: Publish the journey
description: Learn how to publish a journey in Adobe Journey Optimizer, create new versions, manage journey statuses, and understand republishing requirements.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
keywords: publish, journey, live, validity, check
exl-id: e0ca8aef-4f1d-4631-8c34-1692d96e8b51
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/Hhvwpfq0phAjvzIGgv-NMnnhWhYJ-PpLOL0F4Q-CnqA
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2: []
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
---
# Publish your journey {#publishing-the-journey}

>[!BEGINSHADEBOX]

**On this page:** Learn how to publish a journey to set it Live, including prerequisites, the publication process, version management, and republishing requirements.

>[!ENDSHADEBOX]

Publishing a journey activates it: it moves to the **[!UICONTROL Live]** status, becomes available for new profiles to enter, and switches to read-only mode. You cannot publish a journey that contains errors.

>[!NOTE]
>
>When you save or publish a journey, Journey Optimizer validates the total journey payload size and may warn or block publication if you approach or exceed the limit. Learn more in [Journey payload size validation](../start/guardrails.md#journey-payload-size).

➡️ [Discover this feature in video](#video)

## Before you publish {#before-you-publish}

Before publishing, make sure your journey meets the following prerequisites:

* **No validation errors** — You cannot publish a journey that contains errors. [Test your journey](testing-the-journey.md) first, and [troubleshoot any activity errors](../building-journeys/troubleshooting.md#activity-errors).
* **Publish permission** — Publishing requires the **[!DNL Publish journeys]** high-level permission. Learn more about [managing access rights](../administration/permissions-overview.md).
* **Payload within limit** — The journey payload must be within the configured limit (4 MB by default). See [Journey payload size validation](../start/guardrails.md#journey-payload-size).
* **Approval policy compliance** — If your journey is subject to an approval policy, publishing submits it for approval instead of publishing it right away. Once an approver signs off, the journey is published automatically — there is no separate publish step to perform afterward. [Learn more](../test-approve/gs-approval.md).

### Choose the right validation method before publishing {#choose-validation-method}

Validate your journey using one of the available testing options. Each uses a different type of data and fits a different stage of your build:

| Option | Data used | Best for | Sends real messages? |
| --- | --- | --- | --- |
| [Simulation](simulate-journey-gs.md) | Temporary simulated users, manually created or auto-generated | Fast iteration during journey design — no need to create or wait for AEP test profiles to propagate | Yes — to the execution addresses defined at the simulated user level |
| [Test mode](testing-the-journey.md) | Persistent AEP test profiles | Step-by-step manual validation of branch and message logic in a draft journey | Yes — to the test profiles' real inboxes, using the same delivery pipeline as production |
| [Dry run](journey-dry-run.md) | Real production audience data | Final pre-launch check of actual audience reach and targeting at scale, without contacting anyone | No |

Dry run never delivers real communications or updates live profile data. Simulation and Test mode do deliver real messages — Simulation to the execution addresses defined on the simulated users, and Test mode to the real inboxes of profiles you have explicitly flagged as test profiles.

<!-- For a full comparison of these three methods, see [Choose how to test and validate your journey](choose-validation-method.md). -->

## Publication process {#journey-publication}

Steps to publish a journey are detailed below:

1. Verify that the journey is valid and has no errors, and that it meets the [prerequisites above](#before-you-publish).

1. To publish the journey, click on the **[!UICONTROL Publish]** option, located in the top-right drop-down menu.

    >[!NOTE]
    >
    > If your journey is subject to an approval policy, clicking **[!UICONTROL Publish]** submits the journey for approval instead of publishing it right away. Once an approver signs off, the journey is published automatically — you do not need to publish it again. [Learn more](../test-approve/gs-approval.md)

    ![Publish button in journey toolbar to activate the journey](assets/journeyuc1_18.png)

When the journey is published, it is in **read-only** mode. In read-only mode, you can only modify the activity labels and descriptions, the journey's name, and the journey's description. If you need to make additional modifications to a published journey, create [a new version](journey-ui.md#journey-filter) of your journey.

### Journey statuses {#journey-statuses}

After publication, a journey moves through several statuses:

* **[!UICONTROL Live]** — The journey is published and profiles can enter it.
* **[!UICONTROL Closed]** — A previous version that was automatically ended when a new version was published. No entrance can happen.
* **[!UICONTROL Finished]** — The journey has completed according to its end criteria. For the exact definition of when a journey is considered finished, see [How journeys end](end-journey.md#journey-finished-definition).

### Stop a journey {#stop-journey}

When you stop a journey, it is permanently stopped. All the individuals flowing through the journey are permanently stopped, and the journey stops allowing new entries. If you need to run the journey again, duplicate it and publish the new journey. For more information on how journeys end, see [How journeys end](end-journey.md).

### Republishing requirements {#republishing}

In some cases, you must republish a journey for changes or assets to remain effective:

>[!IMPORTANT]
>
>* If changes are made to an offer decision used in a journey's message, you need to unpublish the journey and republish it. This ensures that the changes are incorporated into the journey's message and that the message is consistent with the latest updates.
>
>* Assets/Images are accessible in delivered content for up to 2 years (730 days) since their first publication in any fragment/inline message. Re-publishing is required after this expiry period (any time after 730 days) to keep them accessible for another 2 years. Any re-publication done within 730 days of the first publication will not extend the expiry of assets/images to the next 730 days.

## Journey versions {#journey-versions}

In the journey list, all journey versions are displayed with the version number. When you search for a journey, newest versions appear at the top of the list the first time the application opens. Then, you can define the sorting you want and the application will keep it as a user preference. The journey's version is also displayed at the top of the journey edition interface, above the canvas.

![Journey versions list showing published and draft versions](assets/journeyversions1.png)

>[!NOTE]
>
>Usually, a profile cannot be present multiple times in the same journey, at the same time, for all active versions of the journey. If reentrance is enabled, a profile can reenter a journey, but cannot do it until they fully exited that previous instance of the journey. [Read more](entry-management.md).

### Create a new version of a journey {#journey-create-new-version}

If you need to modify to a live journey, create a new version of your journey. To create a new version of an existing journey, follow the steps below:

1. Open the latest version of your live journey, click **[!UICONTROL Create a new version]** and confirm.

    ![Create new version dialog for duplicating journey](assets/journeyversions2.png)

    >[!NOTE]
    >
    >You can only create a new version from the latest version of a journey.

1. Make your modifications, click **[!UICONTROL Publish]** and confirm.

From the moment the journey is published, individuals will start to flow into the latest version of the journey. People who have already entered a previous version stay in it until they finish the journey. If they later reenter the same journey, they will go into the latest version.

Journey versions can be stopped individually. All versions of journeys have the same name.

When you publish a new version of a journey, the previous version automatically ends and switches to the **Closed** status. No entrance in the journey can happen. Even if you stop the latest version, the previous version stays closed.


>[!NOTE]
>
>Specific guardrails and limitation apply to the versioning of the journeys. Learn more on [this page](../start/guardrails.md#journey-versions-g).


## Frequently asked questions {#faq}

**Why cannot I publish my journey?**

The most common reason is that the journey contains validation errors — you cannot publish a journey with errors. Other blockers include exceeding the [payload size limit](../start/guardrails.md#journey-payload-size), missing the **[!DNL Publish journeys]** permission, or a pending [approval](../test-approve/gs-approval.md). See [Before you publish](#before-you-publish) and [troubleshoot activity errors](../building-journeys/troubleshooting.md#activity-errors).

**Can I edit a journey after it is published?**

A published journey is in read-only mode. You can only change activity labels and descriptions, the journey's name, and the journey's description. For any other change, [create a new version](#journey-create-new-version) of the journey.

**What happens to profiles already in the journey when I publish a new version?**

New profiles flow into the latest version. Profiles already in a previous version stay there until they finish; if they later reenter, they go into the latest version. The previous version automatically switches to **[!UICONTROL Closed]** and accepts no new entries. See [Journey versions](#journey-versions).

**How do I re-run a stopped journey?**

Stopping a journey is permanent. To run it again, duplicate it and publish the new journey. See [Stop a journey](#stop-journey).

**Do I need to republish after changing an offer decision or updating assets?**

Yes. If you change an offer decision used in a journey's message, unpublish and republish the journey so the change is applied. Assets and images expire 730 days after first publication; republish after that period to keep them accessible. See [Republishing requirements](#republishing).

**Can I publish a journey that requires approval?**

If your journey is subject to an approval policy, clicking **[!UICONTROL Publish]** submits it for approval instead of publishing it right away. The journey is published automatically once an approver signs off — there is no separate publish step to perform afterward. [Learn more about approval](../test-approve/gs-approval.md).

## Related topics {#related-topics}

* [Test your journey](testing-the-journey.md) - Validate your journey with test profiles before publishing
* [Journey simulation](simulate-journey-gs.md) - Validate your journey with simulated users before publishing
* [Journey Dry run](journey-dry-run.md) - Test with real production data without contacting profiles
* [Troubleshooting](../building-journeys/troubleshooting.md#activity-errors) - Resolve activity and publication errors
* [How journeys end](end-journey.md#journey-finished-definition) - Understand journey completion and statuses
* [Profile entrance management](entry-management.md) - Configure how profiles enter and re-enter journeys
* [Journey guardrails and limitations](../start/guardrails.md#journeys-guardrails-journeys) - Review publication and versioning guardrails

## How-to video {#video}

Learn how to publish a journey in this video:

>[!VIDEO](https://video.tv.adobe.com/v/3424998?quality=12)

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to publish an Adobe Journey Optimizer journey, manage journey versions, and understand the constraints that apply once a journey is live.

**Intents:**
* Publish a journey to make it live and available for profile entry
* Verify journey validity and resolve errors before publishing
* Create a new version of a live journey to make modifications
* Understand read-only restrictions that apply after a journey is published
* Stop a journey permanently or manage transitions between versions

**Glossary:**
* **Journey version**: A numbered iteration of a journey; new versions are created to modify a live journey without disrupting profiles already in progress *(product-specific)*
* **Closed status**: The state a previous journey version enters automatically when a new version is published; no new profiles can enter a Closed journey *(product-specific)*
* **Approval policy**: An optional governance workflow requiring explicit approval before a journey can be published *(product-specific)*

**Guardrails:**
* A journey with errors cannot be published.
* Journey Optimizer validates the total journey payload size at save and publish time; publication may be blocked if the limit is exceeded.
* After publishing, a journey is in read-only mode; only labels, descriptions, and the journey name can be edited.
* A new version can only be created from the latest version of a journey.
* When a journey is stopped, it is permanently stopped; it must be duplicated to run again.
* Assets and images in delivered content are accessible for up to 730 days from first publication; re-publishing is required after that period.
* If an offer decision used in a journey message changes, the journey must be unpublished and republished.
* Specific guardrails apply to journey versioning (see guardrails page).

**Terminology:**
* Canonical name: Publish Journey — Acronym: none — variants: activate journey, go live
* Synonyms: "Publish" = "activate" = "go live"
* Do not confuse: Stop (emergency halt of all profiles) ≠ Close to new entrances (manual graceful close; existing profiles finish) ≠ Closed status (automatic when a new version is published, or after manual close to new entrances)
* Do not confuse: Simulation (temporary simulated users, no AEP test profiles needed) ≠ Test mode (persistent AEP test profiles, draft journeys only) ≠ Dry run (real production audience data, no contact, no profile update, action nodes bypassed)

**FAQ:**
* **Q: Can I edit a journey after it is published?** — Only labels, descriptions, and the journey name can be changed. To make other modifications, create a new version of the journey.
* **Q: What happens to profiles in an older journey version when a new version is published?** — Profiles already in the previous version stay there until they finish; new profiles enter the latest version.
* **Q: Can I republish a Closed journey version?** — No. Once a previous version is Closed, it stays closed even if the latest version is stopped.
* **Q: What should I do if an offer decision used in the journey changes?** — Unpublish the journey and republish it to incorporate the updated offer decision.
* **Q: Is approval required before publishing?** — Only if your journey is subject to an approval policy; in that case, publishing submits the journey for approval instead of publishing it right away, and it is published automatically once an approver signs off.

+++
