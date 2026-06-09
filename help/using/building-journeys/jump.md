---
solution: Journey Optimizer
product: journey optimizer
title: Jumping from one journey to another
description: Jumping from one journey to another
feature: Journeys, Activities
topic: Content Management
role: User
level: Intermediate
keywords: jump, actvity, journey, split, splitting
exl-id: 46d8950b-8b02-4160-89b4-1c492533c0e2
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/qCnWzqjO5YRbKO-WHUo950uoHS0skcZT6sdYyNJ4esE
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
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
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
---
# Jump from one journey to another {#jump}

>[!CONTEXTUALHELP]
>id="ajo_journey_jump"
>title="Jump activity"
>abstract="The Jump action activity allows you to push individuals from one journey to another. This feature allows you to simplify the design of very complex journeys and build journeys based on common and reusable journey patterns."

The **[!UICONTROL Jump]** action activity allows you to push individuals from one journey to another. This feature allows you to:

* simplify the design of very complex journeys by splitting them into several ones  
* build journeys based on common and reusable journey patterns

In the origin journey, add a **[!UICONTROL Jump]** activity and select a target journey. When the individual enters the **[!UICONTROL Jump]** step, an internal event is sent to the first event of the target journey. If the **[!UICONTROL Jump]** action succeeds, the individual continues to progress in the journey. The behavior is similar to other actions.

In the target journey, the first event triggered internally by the **[!UICONTROL Jump]** activity makes the individual flow in the journey.

## Lifecycle {#jump-lifecycle}

Assume you have added a **[!UICONTROL Jump]** activity in journey A to journey B. Journey A is the **origin journey**, and journey B is the **target journey**.  

Here are the different steps of the execution process:

**Journey A** is triggered from an external event:

1. Journey A receives an external event related to an individual.
1. The individual reaches the **[!UICONTROL Jump]** step. 
1. The individual is pushed to journey B and moves on to the next steps in journey A, after the **[!UICONTROL Jump]** step.

In journey B, the first event is triggered internally via the **[!UICONTROL Jump]** activity from journey A:

1. Journey B receives an internal event from journey A.
1. The individual starts flowing in journey B.

>[!NOTE]
>
>Journey B can also be triggered via an external event.

### Profile behavior during a Jump {#jump-profile-behavior}

When a profile reaches the **[!UICONTROL Jump]** step, it continues progressing in the origin journey (Journey A) while simultaneously entering the target journey (Journey B). The profile is therefore active in both journeys at the same time.

This means:

* The profile completes any remaining steps in Journey A after the Jump activity (for example, a follow-up wait or closing action).
* The profile also starts flowing through Journey B from its first event, independently of Journey A.
* If the profile is **already active** in Journey B when the Jump is executed, it will **not** enter Journey B again. Journey A continues normally; no error is reported.

>[!NOTE]
>
>The case above — profile already active in Journey B — results in a **silent skip**: no error is raised and Journey A continues normally. In other situations, the Jump can **fail** and Journey A applies its standard action-error handling. See [Runtime failures](#jump-troubleshoot) for the full list of cases.

## Best practices and limitations {#jump-limitations}

Use these guidelines to keep Jump activity behavior predictable and safe.

### Authoring {#jump-limitations-authoring}

* The **[!UICONTROL Jump]** activity is only available in journeys that use a namespace.
* You can only jump to a journey that uses the same namespace as the origin journey.
* You cannot jump to a journey that starts with an **Audience Qualification** event or **Read Audience**. 
* You cannot have a **[!UICONTROL Jump]** activity and an **Audience Qualification** event or **Read Audience** in the same journey.
* You can include as many **[!UICONTROL Jump]** activities as needed in a journey. After a **[!UICONTROL Jump]**, you can add any activity needed.
* You can have as many jump levels as needed. For example, journey A jumps to journey B, which jumps to journey C, and so on.
* The target journey can also include as many **[!UICONTROL Jump]** activities as needed.
* Loop patterns are not supported. There is no way to link two or more journeys together, which would create an infinite loop. The **[!UICONTROL Jump]** activity configuration screen prevents you from doing this.

### Execution {#jump-limitations-exec}

* When the **[!UICONTROL Jump]** activity is executed, the latest version of the target journey is triggered.
* A unique individual can only be present once in the same journey. As a result, if the individual pushed from the origin journey is already in the target journey, the individual will not enter the target journey. No error will be reported on the **[!UICONTROL Jump]** activity because this is normal behavior.

## Design strategy: bite-sized sub-journeys {#jump-strategy}

Complex customer journeys can quickly become difficult to build and maintain, especially as additional channels or touchpoints are introduced. Even a journey with a handful of milestones can expose 20 or more unique paths a customer can take, and that complexity grows exponentially with each addition.

A practical approach to managing this is to break large journeys into smaller, focused sub-journeys — one per business phase or milestone — and connect them using the **[!UICONTROL Jump]** activity. This keeps each journey readable, testable, and independently maintainable.

**Step 1 — Visualize the end-to-end journey**

Map the full customer journey and identify its high-level phases. For example, a loyalty onboarding journey might include three distinct phases: download the mobile app, make a first transaction, make a second transaction.

**Step 2 — Annotate phases and define sub-journeys**

Mark the boundary of each phase and define its business objective. Each phase becomes a candidate sub-journey with a clear entry condition and goal.

**Step 3 — Build and connect sub-journeys**

Build each phase as a separate journey in Journey Optimizer, then use **[!UICONTROL Jump]** activities to pass profiles from one sub-journey to the next. The result is a set of simpler, reusable journeys that combine to produce the full end-to-end experience — with less risk of introducing errors.

>[!TIP]
>
>For a worked example using a multi-phase loyalty program, see [Multi-phase loyalty journey](journeys-uc.md#multi-phase-loyalty).

## Configuring the Jump activity {#jump-configure}

1. Design your **origin journey**.

   ![Jump activity in journey palette for transitioning between journeys](assets/jump1.png)

1. At any step of the journey, add a **[!UICONTROL Jump]** activity, from the **[!UICONTROL ACTIONS]** category. Add a label and description.

   ![Target journey selection dropdown in jump activity configuration](assets/jump2.png)

1. Click inside the **Target journey** field. 
   The list displays all journey versions that are draft, live or in test mode. Journeys that use a different namespace or that start with an **Audience Qualification** event are not available. Target journeys that would create a loop pattern are also filtered out.

   ![Jump activity showing target journey and action parameters](assets/jump3.png)

   >[!NOTE]
   >
   >You can click the **Open target journey** icon, on the right side, to open the target journey in a new tab.

1. Select the target journey that you want to jump to.
   The **First event** field is prefilled with the name of the target journey's first event. If your target journey includes multiple events, the **[!UICONTROL Jump]** is only allowed on the first event.

   ![Parameter mapping configuration for jump activity with expression editor](assets/jump4.png)

1. The **Action parameters** section displays all the fields of the target event. Map each field with fields from the origin event or data source, as with other types of actions. This information will be passed to the target journey at runtime.
1. Add the next activities to finish your origin journey.

   ![Test mode interface for testing jump activity between journeys](assets/jump5.png)


   >[!NOTE]
   >
   >The individual's identity is automatically mapped. This information is not visible in the interface.

Your **[!UICONTROL Jump]** activity is configured. As soon as your journey is live or in test mode, individuals reaching the **[!UICONTROL Jump]** step will be pushed to the target journey.

When a **[!UICONTROL Jump]** activity is configured in a journey, a **[!UICONTROL Jump]** entry icon is automatically added at the beginning of the target journey. This helps you identify that the journey can be triggered externally but also internally from a **[!UICONTROL Jump]** activity. 

![Journey flow showing jump from source journey to target journey](assets/jump7.png)

## Troubleshooting {#jump-troubleshoot}

### Configuration errors

The following issues prevent the Jump from working correctly and appear as errors on the journey canvas:

* The target journey no longer exists.
* The target journey is draft, closed, or stopped.
* The first event of the target journey has changed and the mapping is broken.

![Journey analytics showing jump activity execution metrics](assets/jump6.png)

### Runtime failures

In the following cases, the Jump step is treated as a **failed action** in Journey A. Journey A applies the standard action-error handling and continues:

* The existing target journey instance has been terminated and the target journey is non-reentrant.
* A reentrance period is configured on the target journey. Even when re-entry is allowed in principle, the profile cannot re-enter until the period elapses (the Jump fails with a "non-reentrant for the period" status).
* The target journey version cannot be located, has been deleted, is in a finished state, or has been stopped.

+++AI Assistant — Page context

* **TL;DR:** This page explains the Jump activity, which pushes profiles from one journey to another to simplify complex journey designs through reusable sub-journey patterns.

**Intents:**

* Use the Jump activity to transfer profiles from an origin journey to a target journey
* Decompose a complex journey into smaller, manageable sub-journeys connected by Jump activities
* Configure the Jump activity by selecting a target journey and mapping action parameters
* Understand profile behavior when a Jump is executed (profile active in both journeys simultaneously)
* Troubleshoot Jump configuration errors and runtime failures
* Avoid loop patterns when chaining multiple journeys with Jump activities

**Glossary:**

* **Jump activity**: An action activity that sends an internal event to the first event of a target journey, causing the profile to begin flowing through that journey. *(product-specific)*
* **Origin journey**: The journey that contains the Jump activity and initiates the transfer of a profile to another journey. *(product-specific)*
* **Target journey**: The journey that receives the profile via the Jump activity's internal event trigger. *(product-specific)*
* **Silent skip**: The behavior when a profile is already active in the target journey at the time of a Jump — the Jump is skipped without an error, and the origin journey continues normally. *(product-specific)*

**Guardrails:**

* Jump activity is only available in journeys that use a namespace; origin and target journeys must share the same namespace
* Cannot jump to a journey starting with an Audience Qualification event or Read Audience
* Cannot use a Jump activity and an Audience Qualification event or Read Audience in the same journey
* Loop patterns (circular journey chains) are not supported and are prevented by the configuration UI
* At runtime, the latest live version of the target journey is triggered
* A profile can only be present once in the same journey at a time; if already active in the target journey, the Jump is silently skipped
* If the target journey is draft, closed, stopped, deleted, or its first event mapping is broken, the Jump results in a configuration error

**Terminology:**

* Canonical name: Jump activity — Acronym: none — variants: Jump action, journey jump
* Synonyms: "origin journey" = "source journey"; "target journey" = "destination journey"
* Do not confuse: "silent skip" ≠ "runtime failure" — A silent skip occurs when the profile is already in the target journey (no error raised); a runtime failure occurs when the target journey is unreachable or non-reentrant (treated as a failed action)

**FAQ:**

* **Q: What happens to a profile in the origin journey after a Jump?** — The profile continues progressing through any remaining steps in the origin journey after the Jump step while simultaneously entering the target journey; it is active in both journeys at the same time.
* **Q: Can I jump to a Read Audience journey?** — No; you cannot jump to a journey that starts with a Read Audience or Audience Qualification event.
* **Q: What triggers the target journey when a Jump is executed?** — An internal event is sent to the first event of the target journey by the Jump activity; the profile then flows through the target journey from that first event.
* **Q: How do I prevent infinite loops when chaining journeys with Jump?** — Loop patterns are blocked by the Jump activity configuration UI, which filters out target journeys that would create a circular chain.
* **Q: What version of the target journey is triggered by a Jump?** — The latest live (or test mode) version of the target journey is triggered at runtime.

+++
