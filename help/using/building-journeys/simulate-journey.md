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
---
# Simulate your journey{#simulate-journey}

Use this guide after you [launch Simulation](simulate-journey-gs.md) on a journey and choose **[!UICONTROL Manual simulation]**. The sections below follow the same order as a typical run:

* **[Create and manage simulated users](#test-users)**: Build or select simulated users, send them into the journey, and adjust wait behavior for the run.
* **[Trigger your events](#firing_events)**: Fire unitary events so users waiting on event nodes (or entering a unitary journey) can progress on the canvas.
* **[View results](#viewing-results)**: Open the execution log, review paths and errors, and confirm the journey is ready to publish.

### Quick simulation {#quick-simulation}

Use **[!UICONTROL Quick simulation]** when you want a fast, hands-off run that exercises the journey using sensible defaults. Adobe Journey Optimizer automatically:

* Gathers the profile information required by the journey, such as email address, phone number, and wait time.
* Generates simulated users based on the journey definition (for example, 10 users when 10 are expected).
* Triggers each generated user into the journey.

Once the run completes, click **[!UICONTROL View results]** to inspect the outcome. For more information, see [View results](#viewing-results).

### Manual simulation {#manual-simulation}

Use **[!UICONTROL Manual simulation]** when you need full control over the simulated users, the events you fire, and the order in which they enter the journey. The interface guides you through each step:

1. Add test users: generate them with AI, select previously saved users, or create new ones.
1. Trigger the test users into the journey.
1. Fire any unitary events the journey expects.
1. Review the results.

The next sections describe each step in detail.

## Create and manage simulated users {#test-users}

>[!IMPORTANT]
>
>You need the **Simulate journeys** permission to access the **[!UICONTROL Simulation]** feature. [Learn more](../administration/permissions.md)

Simulated users are temporary profile-like entities you define in **[!UICONTROL Simulation settings]**. This section covers how to create them, save them for reuse, adjust or remove them from the list, and send them into the journey.

You can populate the **[!UICONTROL Test users]** list in three ways:

* **Generate users with AI** — Adobe Journey Optimizer generates a set of simulated users from the journey definition. For journeys with an Email or SMS node, the AI prompts you to confirm the email address or phone number to use; the value defaults to the address attached to your IMS profile.
* **Select existing users** — Pick simulated users you previously created and saved.
* **Create new users** — Define new simulated users from a UI form or by importing a JSON object.

### Create simulated users {#create-simulated-users}

The following steps show you how to create simulated users from the UI or by importing a JSON file.

1. From your Journey, open **[!UICONTROL Simulate]** and choose **[!UICONTROL Simulation]**.

    ![Test mode button in journey interface](assets/test-mode-simulated.png)
    
1. Click **[!UICONTROL Create Simulated Users]** to create new users and select whether to create users from the UI or import them from JSON.

    To reuse simulated users instead, click **[!UICONTROL Select simulated users]** and choose entries you saved earlier. To let Adobe Journey Optimizer generate users for you from the journey definition, choose the AI generation option.

    ![Simulated user selection panel](assets/simulate-2.png)

1. If you create simulated users from JSON, update the corresponding fields with your simulated user data.

1. If you create simulated users from UI, enter a **[!UICONTROL Display name]** and **[!UICONTROL Description]** to identify this simulated user. Then, select the attributes from the Union schema that you want to populate for this user.

    ![Attribute selection from Union schema](assets/simulate-3.png)

1. Click add **[!UICONTROL Audience membership]** to simulate segment memberships.

1. Click **[!UICONTROL Add profile]** to create multiple simulated users in a single session.

1. For each simulated user you added in this session, you can use the following actions:

    * **[!UICONTROL Duplicate]**: Adds a new simulated user that replicates the completed configuration of an existing entry, you can then edit the duplicate as needed.
    * **[!UICONTROL Apply to all]**: Propagates the attribute values or settings from one simulated user to every other simulated user in the list.
    * **[!UICONTROL Delete]**: Removes the selected simulated user from the list.

1. Click **[!UICONTROL Save]** to store one or more simulated users for future use.

1. After you save, the simulated users you created appear in the **[!UICONTROL Test users]** list. For each entry, open the options menu and select one of the following:

    * ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg): Update the simulated user's details.
    * ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg): Run the simulation for this simulated user only.
    * ![Clear icon](assets/do-not-localize/Smock_Close_18_N.svg): Remove the user from this list. The simulated user is not deleted and remains available in the Simulated Users selection.

    ![Simulated user selection panel](assets/simulate-4.png)
    
1. If your journey includes a **[!UICONTROL Wait]** activity, open the **[!UICONTROL Test settings]** tab to fine-tune how long that wait lasts during the simulation. For example, if the live **[!UICONTROL Wait]** activity is configured for several days, you can override it to 10 seconds so the simulated user only spends that long on the node before moving to the next activity.

1. Click **[!UICONTROL Send all]** to send every simulated user in the list into the journey, or click ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) on a row to send only that user. A `Simulated users have been sent successfully.` confirmation message appears when the simulated users successfully enter the journey.

    ![Simulated user selection panel](assets/simulate-5.png)

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View results](#viewing-results).

After you validate the journey in **[!UICONTROL Simulation]**, review the **[!UICONTROL Results]** log. If errors appear, leave **[!UICONTROL Simulation]**, apply the required changes to the journey, and run **[!UICONTROL Simulation]** again until the run looks correct. You can then publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

### Select simulated users {#select-simulated-users}

Simulated users that you create manually are stored and can be selected from this list when Simulation is enabled on other journeys.

1. Set the journey to **[!UICONTROL Simulation]**. Open the **[!UICONTROL Simulate]** entry point and choose **[!UICONTROL Simulation]** so the journey uses the Simulation feature, for example alongside Test mode or Live, depending on your workspace.

    ![Test mode button in journey interface](assets/test-mode-simulated.png)

1. In the **[!UICONTROL Simulation settings]** panel, you can either select previously created simulated users clicking **[!UICONTROL Select simulated users]**.

    ![Test mode in journey interface](assets/simulate-11.png)

1. Select from the list of simulated users that were previously created and saved.

1. Once you have selected your simulated users, they are now available in the **[!UICONTROL Test users]** list. From the options menu, choose between the following option:

    * ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg) to edit users and change its details.
    * ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) to send your simulation to only one simulated user.
    * ![Clear icon](assets/do-not-localize/Smock_Close_18_N.svg) to clear your simulated users from the list. Note that clearing it does not delete it, it can still be selectable from the Simulated users list.

    ![Simulated user selection panel](assets/simulate-4.png)

1. Click **[!UICONTROL Send all]** to send every simulated user in the list into the journey, or click ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) on a row to send only that user. A `Simulated users entered the journey successfully.` confirmation message appears when the simulated users successfully enter the journey.

    ![Simulated user selection panel](assets/simulate-5.png)

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View results](#viewing-results).

After you validate the journey in **[!UICONTROL Simulation]**, review the **[!UICONTROL Results]** log. If errors appear, leave **[!UICONTROL Simulation]**, apply the required changes to the journey, and run **[!UICONTROL Simulation]** again until the run looks correct. You can then publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

### Test users table actions {#test-users-actions}

Once test users are added to the **[!UICONTROL Test users]** list, the following table-level actions are available:

* **[!UICONTROL Manage users]** — Generate users from the journey definition. Use this option when you want Adobe Journey Optimizer to populate the list automatically based on what the journey expects.
* **[!UICONTROL Add users]** — Add more users to the current list, either by selecting from the simulated users inventory or by creating new ones from a form or JSON object.
* **[!UICONTROL Clear]** — Remove every user from the list. Cleared users are not deleted from the simulated users inventory and remain available for selection.

To trigger users into the journey, use the per-row and global send controls:

* ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) — Send only the selected user into the journey.
* **[!UICONTROL Send all]** — Send every user in the list at once.

>[!NOTE]
>
>Click any row in the **[!UICONTROL Test users]** list to preview the path that user will take through the journey canvas before you trigger it.

## Trigger your events {#firing_events}

If your journey includes one or more unitary events, you trigger them while Simulation is active. The exact flow depends on the journey type:

* **Batch journey with read audience and unitary events** — After you send simulated users into the journey, they wait at the event node. Trigger the expected event(s) to let each user progress further on the canvas.
* **Unitary journey** — The journey starts with a unitary event. After you add (or create) a user, fire the start event for that user to enter the journey. See [Trigger the start event for a unitary journey](#unitary-trigger).

1. In **[!UICONTROL Select event type]**, select the event to fire for this simulation.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-10.png)

1. Configure the event payload for each user. You can:

    * Click **[!UICONTROL Configure events]** to open the editor and adjust the event as needed.
    * Click ![Edit event](assets/do-not-localize/Smock_Edit_18_N.svg) beside a user to change the payload for that simulated user only.
    * Click **[!UICONTROL Generate event values]** beside a user to let Adobe Journey Optimizer generate the payload using AI. When values are generated, the user is marked **[!UICONTROL Ready to send]**.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-9.png)

1. To apply the same change to every user in the list, use the global controls:

    * **[!UICONTROL Edit all]** — Open the editor and apply the same payload to every user.
    * **[!UICONTROL Generate all]** — Generate event values for every user in a single action.
    * **[!UICONTROL Send all]** — Trigger the event for every user marked **[!UICONTROL Ready to send]**.

1. In the **[!UICONTROL Trigger event]** view, specify which simulated users to include in the execution. Event configuration applies to a single event at a time. Modifying the selected event or the set of included users resets previously entered field values. Complete the current configuration before changing either selection.

    ![Event configuration with Test users list and event fields](assets/simulate-8.png)

1. Click **[!UICONTROL Done]**.

1. In **[!UICONTROL Test events]**, either select **[!UICONTROL Send all]** to send every simulated user listed under **[!UICONTROL Test users]** into the journey, or select ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) for a single user to execute the simulation for that user only.

1. After events are fired, the canvas updates to reflect each user's progression. Click any row in the **[!UICONTROL Test users]** list to see the new path that user took through the journey.

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View results](#viewing-results).

### Trigger the start event for a unitary journey {#unitary-trigger}

For journeys that start with a unitary event, the trigger step is also how the user enters the journey.

1. Add a user to the **[!UICONTROL Test users]** list. To create a new user on the fly, fill in **[!UICONTROL Display name]**, **[!UICONTROL Email]**, and (optionally) **[!UICONTROL Description]**.
1. Select the start event for the journey.
1. Edit or generate the event payload. When editing, you can assign an **[!UICONTROL Event ID]** to the event.
1. Mark the event as **[!UICONTROL Ready]**, then trigger it. The user enters the journey and the canvas reflects its path.

<!-- TODO: new screenshot — Unitary journey: select start event and assign event ID. -->

## View results {#viewing-results}

The **[!UICONTROL Results]** tab allows you to view the test results. In the **[!UICONTROL Test user]** drop-down, select the simulated user whose execution you want to inspect.

<!--
* **All simulated users**: Select **[!UICONTROL All]** to see results aggregated across every simulated user in the run. This view helps you scan the full simulation at a glance, activity, outcomes, and errors, without picking a single simulated user first.
-->

The results view summarizes the run, surfaces uncovered paths, and lets you inspect individual users:

* **Run summary** — Overall outcome of the simulation across every user that was triggered.
* **Uncovered paths** — Paths in the journey that were not reached by any simulated user during the run. Use this list to identify branches that need additional users or events to be exercised before publishing.
* **Per-user path preview** — Click a user in the **[!UICONTROL Test users]** list to animate that user's path through the canvas. Useful when you want to confirm where a specific user ended up or where it is currently waiting.
* **Per-node logs** — Detailed log for every node a user crossed, including entry, exit, and any errors recorded during simulation.

<!-- TODO: new screenshot — Results view with uncovered paths summary and per-user path animation. -->

For each activity, the log can show whether the simulated user entered or exited the step, and errors that occurred during the simulation.

![Logs for test users](assets/simulate-6.png)

For **Wait** activities, the log includes two duration-related values:

* **Defined duration**: The duration specified on the **Wait** activity for the published journey and applied once the journey is live. The log records whether Simulation applies an override from the test settings, for example 10 seconds, rather than relying solely on the value defined on the journey.
* **Actual duration**: The elapsed time the simulated user remained on the **Wait** activity. This value is set from the **[!UICONTROL Test settings]** tab.

When errors appear in the log, leave **Simulation**, apply the required changes to the journey, and run **Simulation** again. After validation succeeds, publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

## Limitations {#limitations}

In this release, **[!UICONTROL Simulation]** may not support every activity, channel, or integration that **[!UICONTROL Test mode]** or a live journey supports, and behavior may change as the capability matures. Use the procedures in this article for supported workflows.

Refer to the drop-downs below to learn more on Simulation limitations.

+++ Node-level restrictions

If a journey contains any of the following nodes, it cannot be started in **[!UICONTROL Simulation]**. The journey must be modified, or the relevant node removed, before simulation can run.

| Restricted node | Notes |
| --- | --- |
| Business Events | Journeys that start with a business event cannot be run in **[!UICONTROL Simulation]**. |
| Supplemental ID (multiple re-entrance) | Concurrent re-entrance (several active instances for the same simulated user) prevents **[!UICONTROL Simulation]** from starting. |
| Content Decision node | This activity must be removed or changed before you can simulate the journey. |
| Dataset Lookup | Customer dataset lookups by key are not supported; journeys that include this activity cannot be run in **[!UICONTROL Simulation]**. |
| Path Experimentation (Optimize — Experiment variant) | Not supported in **[!UICONTROL Simulation]**. You can still use **[!UICONTROL Optimize]** for flows that used to live under **[!UICONTROL Condition]** (for example, data source conditions). |
| Path Targeting (Optimize, Targeting Rule variant) | Not supported in **[!UICONTROL Simulation]**. |
| External audience attribute enrichment | Journeys that use personalized attributes from external audience sources will not start in **[!UICONTROL Simulation]** when this validation is active. |

+++

</br>

+++ Functional limitations

The following capabilities are not supported in **[!UICONTROL Simulation]**.

| Capability | Notes |
| --- | --- |
| Exit criteria | Exit criteria are not applied when you run **[!UICONTROL Simulation]**. |
| [!DNL Adobe Journey Optimizer] decisioning inside an action (for example, email content with Adobe Journey Optimizer decisioning) | Action proofs for content that uses [!DNL Adobe Journey Optimizer] decisioning are not generated. |
| Mock custom action response | [!UICONTROL Custom actions] perform a real outbound call by default. Mocking the response so no external call runs is not supported. |
| Consent policy evaluation | Consent cannot be mocked at the simulated-user level. |
| Journey capping and arbitration | Not supported in **[!UICONTROL Simulation]**. |
| Frequency capping (by channel or communication type) | Not supported in **[!UICONTROL Simulation]**. |
| Opt-out management, suppression, and allow lists | Follows messaging routing configuration where it applies. |
| Dynamic subdomain and dynamic attributes in channel configurations | Follows messaging routing configuration where it applies. |
| Send Time Optimization (STO) | Not supported in **[!UICONTROL Simulation]**. |
| Sandbox tooling (copy simulated users across sandboxes) | Not supported. |
| Wave sending in journeys | Not supported. |
| Quiet hours | Not supported. |
| Opt-out management, suppression, and allow lists | Not supported. |
| Dynamic subdomain and dynamic attributes in channel configurations | Not supported. |
| Privacy service | Simulated users are not GDPR-compliant persistent profiles. Do not include real customer data in simulated users. |

+++

</br>

+++ Quantitative guardrails 

These guardrails apply to **[!UICONTROL Simulation]**. Numeric caps are enforced in the journey interface and at runtime. Limits may change in a later release; if you run near a ceiling, verify behavior in your sandbox.

| Guardrail | Limit | Notes |
| --- | --- | --- |
| Maximum simulated users that can be selected and triggered in one batch (batch journeys, event-triggered flows, and audience-qualification flows) | 20 | Counted for each **[!UICONTROL Send all]** or **[!UICONTROL Trigger selected events]**; not a cumulative cap for the whole journey. |
| Maximum unique simulated users tested in a single simulation run | 100 | Reaching **100** unique users in one run blocks **[!UICONTROL Select simulated users]** for new simulated users. If you are at **90**, you can add at most **10** more before the same block. |
| Maximum journeys that can run in **[!UICONTROL Simulation]** at the same time in one sandbox | 20 | Cap is shared by every **[!UICONTROL Simulation]** journey in that sandbox at once. |
| Maximum active simulated users in one sandbox | 2,000 | Maximum simulated users that can exist in the sandbox at one time. Adobe may adjust this limit based on customer feedback. |
| Event Pre-fill (Browser Only) | — | You can pre-fill event payload fields only in the browser-based simulation UI. Pre-filled values stay in that browser and are not synced to other browsers, devices, or sessions, so you may see different pre-fill data in each place you test. |

+++
