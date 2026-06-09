---
solution: Journey Optimizer
product: journey optimizer
title: Simulate your journey
description: Learn how to simulate your journey
feature: Journeys, Test Profiles
topic: Content Management
role: User
level: Intermediate
keywords: test, journey, check, error, troubleshooting
version: Journey Orchestration
feature_v2: []
subfeature_v2: []
---
# Get started with Journey simulation {#simulate-journey-gs}
 
>[!IMPORTANT]
>
>You need at least one of the following permissions to access the **[!UICONTROL Simulation]** feature: **Simulate journeys**, **Publish journeys**, or **Approve and Publish journeys**. [Learn more](../administration/permissions.md)
>
>To use AI in **[!UICONTROL Simulation]** (**[!UICONTROL Quick simulation]**, generating simulated users with AI, **[!UICONTROL Generate event values]**), users require **[!UICONTROL Generate Content]** permission from the **[!UICONTROL AI Assistant]** capability. 

You can set the journey to **[!UICONTROL Simulation]** in addition to **Draft**, **Test mode**, and **Live**. In Simulation, you test with **simulated users**: temporary profile-like entities you add, without using persistent test profiles in Adobe Experience Platform.
   
Adobe Journey Optimizer offers two ways to test and validate your journey:

* **[Simulation](simulate-journey.md#test-users)**: Use the **[!UICONTROL Simulation]** journey feature and simulated users without pre-created profiles in Adobe Experience Platform, supporting both AI-powered and manually created users.

* **[Test mode](testing-the-journey.md)**: Use persistent profiles flagged as test profiles in Adobe Experience Platform, reusable across sessions. Choose this approach when you need consistent, predefined data. [Learn how to create test profiles](../audience/creating-test-profiles.md).

## Simulation by journey type {#by-journey-type}

The **[!UICONTROL Simulation]** panel shows only the steps your journey needs. That depends on how profiles enter the journey. From these factors, Adobe Journey Optimizer surfaces different simulation experiences. Expand each type below to see how the run differs and which panels you use.

For details, see [Simulate your journey](simulate-journey.md).

+++ Batch journey with a Read audience


The journey is triggered by a **[!UICONTROL Read audience]** and the canvas has no unitary event activities. During simulation, the audience population is not triggered. Only simulated users enter the journey.
Simulated users selected for the simulation appear in the **Test users** section:

![Simulation panel for a batch journey with read audience only](assets/simulate-batch.png)

+++

+++ Batch journey with a read audience and unitary events

A segment-trigger journey that includes one or more unitary events along the path. You first trigger simulated users to enter the simulation and then trigger events for the users that wait at an event node.
Simulated users selected for the simulation and configured events will be visible respectively in the Test users and Test events sections. The Test events section will not be visible until a simulated user enters the journey.

![Simulation panel for a batch journey with read audience only](assets/simulate-batch-2.png)

+++

+++ Unitary journey

The journey starts with a unitary event, not a read audience. A simulated user does not enter the journey until that start event is fired for them.
Simulated users selected for the simulation and configured events will be visible respectively in the **Test users** and **Test events** sections. The **Test users** section does not include an action to trigger a simulated user into the journey. You trigger entry from **Test events**.

![Simulation panel for a batch journey with read audience only](assets/simulate-batch-3.png)

+++

## Launch Simulation {#launch}

Switch the journey to **[!UICONTROL Simulation]** to test with simulated users. Step-by-step tasks are detailed in [Simulate your journey](simulate-journey.md).

1. From your journey, click **[!UICONTROL Simulate]** and choose **[!UICONTROL Simulation]**.

    ![Test mode button in journey interface](assets/test-mode-simulated.png)

1. Wait for activation to complete. While the journey switches to **[!UICONTROL Simulation]**, the controls in the panel are disabled and re-enable automatically once activation finishes.

## Limitations {#limitations}

In this release, **[!UICONTROL Simulation]** may not support every activity, channel, or integration that **[!UICONTROL Test mode]** or a live journey supports, and behavior may change as the capability matures. Use this article for supported workflows.

Refer to the drop-downs below to learn more about Simulation limitations.

+++ Node-level restrictions

Some nodes prevent **[!UICONTROL Simulation]** from starting. Others run in simulation with the behavior described below. When a node must be removed or changed before you simulate, update the journey first.

| Restricted node | Notes |
| --- | --- |
| Business Events | You cannot run journeys that start with a business event in **[!UICONTROL Simulation]**. |
| Supplemental ID (multiple re-entrance) | **[!UICONTROL Simulation]** does not start when multiple re-entrance is enabled and the same simulated user could have several active instances at once. |
| Content Decision node | Remove or change this activity before you simulate the journey. |
| Dataset Lookup | **[!UICONTROL Simulation]** does not support customer dataset lookups by key. Remove or change this activity before you run a simulation. |
| **[!UICONTROL Optimize]** activity | **[!UICONTROL Experiment]** and **[!UICONTROL Targeting rule]** are not supported. Remove or change the node before you simulate.<br><br>Other **[!UICONTROL Optimize]** methods behave as follows:<br><br>**[!UICONTROL Percentage split]**: The Journey Agent creates one simulated user per branch, not according to branch percentages. At runtime, live evaluation picks the branch and it may differ from the generated path. You cannot mock a branch choice. To steer users, rely on branch order on the canvas. The top branch is always chosen.<br><br>**[!UICONTROL Time condition]**: Conditions apply at runtime as in a live journey. For example, a window from 8:00 to 20:00 only lets users through while simulation runs inside that window. You cannot mock execution time. Set the condition to match the current time when you test.<br><br>**[!UICONTROL Date condition]**: Conditions apply at runtime as in a live journey. For example, a date of June 8, 2026 only lets users through when simulation runs on that date. You cannot mock execution date. Set the condition to the current date when you test.<br><br>**[!UICONTROL Profile cap]**: Caps are not enforced during simulation. The Journey Agent creates one simulated user per branch. You cannot mock a branch choice. To steer users, rely on branch order on the canvas. The top branch is always chosen. |
| Timeout and error branches | The Journey Agent does not generate users for activity timeout or error branches. Users only enter those paths if a real timeout or error happens during simulation. |
| Timeout branch (event activities) | Simulated users are created, but in **[!UICONTROL Manual simulation]** the Journey Agent does not decide who enters an event timeout branch. Control the path by sending or not sending the event. For example, to test a timeout branch, wait out the configured timeout and do not send the event. **[!UICONTROL Quick simulation]** can send or withhold events automatically to cover timeout branches. |
| Reaction events | Reaction events run in simulation, but the action must happen in real life. For example, an email **open** reaction requires opening the proof message. You cannot mock reactions in the simulation UI. |
| External data sources | Calls run during simulation the same way as in a live journey. Downstream activities can use the response, but you cannot mock it. When a response value feeds an **[!UICONTROL Optimize]** activity, the Journey Agent cannot invent that output. It only generates inputs for the call. For example, if a call takes a profile city and returns weather, the Agent sets a city on the simulated user and the live call returns the weather. |
| Custom actions | Behavior matches external data sources. Outbound calls run for real. The Journey Agent fills in inputs. Outputs come from the live response. You cannot mock responses. |
| External audience attribute enrichment | Journeys that use personalized attributes from external audience sources do not start in **[!UICONTROL Simulation]** when this validation applies. |

+++

</br>

+++ Functional limitations

The following capabilities are not supported in **[!UICONTROL Simulation]**.

| Capability | Notes |
| --- | --- |
| Exit criteria | Exit criteria are not applied when you run **[!UICONTROL Simulation]**. |
| [!DNL Adobe Journey Optimizer] decisioning inside an action, for example, email content with Adobe Journey Optimizer decisioning | Action proofs for content that uses [!DNL Adobe Journey Optimizer] decisioning are not generated. |
| Mock custom action response | [!UICONTROL Custom actions] perform a real outbound call by default. Mocking the response so no external call runs is not supported. |
| Consent policy evaluation | Consent cannot be mocked at the simulated-user level and consent policies are not evaluated during simulation. |
| Journey capping and arbitration | Not evaluated nor enforced during simulation. |
| Frequency capping (by channel or communication type) | Not evaluated nor enforced during simulation. |
| Opt-out management, suppression, and allow lists | Not evaluated nor applied during simulation. |
| Dynamic subdomain and dynamic attributes in channel configurations | Not supported. |
| Send Time Optimization (STO) | Not evaluated nor applied during simulation. |
| Sandbox tooling (copy simulated users across sandboxes) | Not supported. |
| Wave sending in journeys | Not supported. |
| Quiet hours | Not evaluated nor applied during simulation. |
| Privacy service | Simulated users are not GDPR-compliant persistent profiles. Do not include real customer data in simulated users. |

+++

</br>

+++ Quantitative guardrails 

These guardrails apply to **[!UICONTROL Simulation]**. Numeric caps are enforced in the journey interface and at runtime. Limits may change in a later release. If you run near a ceiling, verify behavior in your sandbox.

| Guardrail | Limit | Notes |
| --- | --- | --- |
| Maximum simulated users that can be selected and triggered in one batch (batch journeys, event-triggered flows, and audience-qualification flows) | 20 | Counted for each **[!UICONTROL Send all]** or **[!UICONTROL Trigger selected events]**, not a cumulative cap for the whole journey. |
| Maximum simulated users per generation request | 50 | Maximum simulated users the Journey Agent generates in one request through **[!UICONTROL Quick simulation]** or **[!UICONTROL Generate with AI]** in **[!UICONTROL Manual simulation]**. If the journey has more than **50** paths, the Journey Agent randomly selects paths to produce those **50** simulated users. |
| Maximum unique simulated users tested in a single simulation run | 100 | Reaching **100** unique users in one run blocks **[!UICONTROL Select simulated users]** for new simulated users. If you are at **90**, you can add at most **10** more before the same block. |
| Maximum journeys that can run in **[!UICONTROL Simulation]** at the same time in one sandbox | 20 | Cap is shared by every **[!UICONTROL Simulation]** journey in that sandbox at once. |
| Maximum active simulated users in one sandbox | 2,000 | Maximum simulated users that can exist in the sandbox at one time. Adobe may adjust this limit based on customer feedback. |
| Event Pre-fill (Browser Only) | — | You can pre-fill event payload fields only in the browser-based simulation UI. Pre-filled values stay in that browser and are not synced to other browsers, devices, or sessions, so you may see different pre-fill data in each place you test. |

+++

+++AI Assistant — Page context

- **TL;DR:** This page introduces the Journey Simulation feature in Adobe Journey Optimizer, explaining how it differs from Test mode, which journey types it supports, how to launch a simulation, and what its node-level, functional, and quantitative limitations are.

**Intents:**
- Understand the difference between Simulation and Test mode for validating journeys
- Launch a Simulation session for a batch, unitary, or mixed journey type
- Identify which journey nodes block or restrict Simulation from running
- Determine which features are unsupported during Simulation (e.g., consent, frequency capping, STO)
- Plan around quantitative guardrails such as maximum simulated users per sandbox
- Decide whether to use Quick simulation or Manual simulation based on testing needs

**Glossary:**
- **Simulated users**: Temporary profile-like entities created for Simulation without persisting in Adobe Experience Platform *(product-specific)*
- **Simulation**: A journey state (alongside Draft, Test mode, and Live) used for testing with simulated users rather than persistent test profiles *(product-specific)*
- **Journey Agent**: The AI component that generates simulated users, event values, and test settings during Quick simulation and AI-assisted Manual simulation *(product-specific)*
- **Quick simulation**: An automated end-to-end simulation run that generates users and events with minimal manual input *(product-specific)*
- **Manual simulation**: A step-by-step simulation mode where users and events are created and triggered individually *(product-specific)*

**Guardrails:**
- Requires at least one of: **Simulate journeys**, **Publish journeys**, or **Approve and Publish journeys** permissions
- AI-powered simulation features require the **Generate Content** permission from the AI Assistant capability
- Maximum 20 simulated users per Send all or Trigger selected events batch
- Maximum 50 simulated users per AI generation request
- Maximum 100 unique simulated users per single simulation run
- Maximum 20 journeys running Simulation simultaneously in one sandbox
- Maximum 2,000 active simulated users in one sandbox at a time
- Business event-triggered journeys cannot be simulated
- Supplemental ID journeys with multiple re-entrance enabled cannot be simulated
- Consent policies, frequency capping, opt-out, STO, and quiet hours are not evaluated during Simulation
- Simulated users must not contain real customer data (not GDPR-compliant)

**Terminology:**
- Canonical name: Simulation — Acronym: none — variants: Journey Simulation, Simulation mode
- Canonical name: Simulated users — Acronym: none — variants: test users (in UI labels)
- Synonyms: "Simulation" = "Simulation mode"; "simulated users" = "test users" (UI label only)
- Do not confuse: "Simulation" ≠ "Test mode" (Test mode uses persistent AEP test profiles; Simulation uses temporary simulated users)

**FAQ:**
- **Q: What permissions do I need to use Simulation?** — You need at least one of: Simulate journeys, Publish journeys, or Approve and Publish journeys. AI features additionally require Generate Content permission from the AI Assistant capability.
- **Q: How does Simulation differ from Test mode?** — Simulation uses temporary simulated users created on the fly without persistent Adobe Experience Platform profiles; Test mode uses persistent profiles explicitly flagged as test profiles in AEP.
- **Q: Can I simulate a journey that starts with a Business Event?** — No. Journeys triggered by a Business Event cannot be run in Simulation.
- **Q: How many simulated users can I test in a single simulation run?** — Up to 100 unique simulated users per run; each Send all action is capped at 20 users at once.
- **Q: Are consent policies enforced during Simulation?** — No. Consent policy evaluation, frequency capping, opt-out management, and quiet hours are all not evaluated during Simulation.
- **Q: What happens if my journey has more than 50 paths during AI generation?** — The Journey Agent randomly selects paths to produce a maximum of 50 simulated users.

+++
