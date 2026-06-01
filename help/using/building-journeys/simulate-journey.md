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
badge: label="Limited Availability" type="Informative"
feature_v2: []
subfeature_v2: []
---
# Simulate your journey{#simulate-journey}
  
>[!IMPORTANT]
>
> This capability is available to all customers as a Limited Availability with essential capabilities.

You can set the journey to **[!UICONTROL Simulation]** in addition to **Draft**, **Test mode**, and **Live**. In Simulation, you test with **simulated users**: temporary profile-like entities you add, without using persistent test profiles in Adobe Experience Platform.
 
Adobe Journey Optimizer offers two ways to test and validate your journey:

* **[Simulation](#test-users)**: Use the **[!UICONTROL Simulation]** journey feature and simulated users for quick runs without pre-created profiles in Adobe Experience Platform.

* **[Test mode](testing-the-journey.md)**: Use persistent profiles flagged as test profiles in Adobe Experience Platform, reusable across sessions. Choose this approach when you need consistent, predefined data. [Learn how to create test profiles](../audience/creating-test-profiles.md).
 
Note that Journey Simulation is in **Limited availability**. To share feedback and help us improve the experience, open **[!UICONTROL Feedback]** from the top bar.
 
![Beta feedback menu](assets/beta-feedback.png)

## Create and manage simulated users {#test-users}

>[!IMPORTANT]
>
>You need at least one of the following permissions to access the **[!UICONTROL Simulation]** feature: **Simulate journeys**, **Publish journeys**, or **Approve and Publish journeys**. [Learn more](../administration/permissions.md)

Simulated users are temporary profile-like entities you define in **[!UICONTROL Simulation settings]**. This section covers how to create them, from the UI or a JSON file, save them for reuse, adjust or remove them from the list, and send them into the journey.
 
### Create simulated users

The following steps show you how to create simulated users from the UI or by importing a JSON file.

1. From your Journey, open **[!UICONTROL Simulate]** and choose **[!UICONTROL Simulation]**.

    ![Test mode button in journey interface](assets/test-mode-simulated.png)
    
1. Click **[!UICONTROL Create Simulated Users]** to create new users and select whether to create users from the UI or import them from JSON.

    To reuse simulated users instead, click **[!UICONTROL Select simulated users]** and choose entries you saved earlier.

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
    
1. If your journey includes a **[!UICONTROL Wait]** activity, open the **[!UICONTROL Test settings]** tab to fine-tune how long that wait lasts during the simulation.

1. Click **[!UICONTROL Send all]** to send every simulated users in the list into the journey. A `Simulated users have been sent successfully.` confirmation message appears when the simulated users successfully enter the journey.

    ![Simulated user selection panel](assets/simulate-5.png)

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View Results](#viewing-results).

After you validate the journey in **[!UICONTROL Simulation]**, review the **[!UICONTROL Results]** log. If errors appear, leave **[!UICONTROL Simulation]**, apply the required changes to the journey, and run **[!UICONTROL Simulation]** again until the run looks correct. You can then publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

### Select simulated users

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

1. Click **[!UICONTROL Send all]** to send every simulated users in the list into the journey. A `Simulated users entered the journey successfully.` confirmation message appears when the simulated users successfully enter the journey.

    ![Simulated user selection panel](assets/simulate-5.png)

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View Results](#viewing-results).

After you validate the journey in **[!UICONTROL Simulation]**, review the **[!UICONTROL Results]** log. If errors appear, leave **[!UICONTROL Simulation]**, apply the required changes to the journey, and run **[!UICONTROL Simulation]** again until the run looks correct. You can then publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

## Trigger your events {#firing_events}

If your journey includes one or more events, you can trigger them while Simulation is active.

1. In **[!UICONTROL Select event type]**, select the event to fire for this simulation.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-10.png)

1. Click **[!UICONTROL Configure events]** to open the editor and adjust the event as needed. To change the payload for a specific simulated user only, click ![Edit event](assets/do-not-localize/Smock_Edit_18_N.svg) beside that user.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-9.png)

1. In the **[!UICONTROL Trigger event]** view, specify which simulated users to include in the execution. Event configuration applies to a single event at a time. Modifying the selected event or the set of included users resets previously entered field values. Complete the current configuration before changing either selection.

    ![Event configuration with Test users list and event fields](assets/simulate-8.png)

1. Click **[!UICONTROL Done]**. 

1. Then, in **[!UICONTROL Test events]**, either select **[!UICONTROL Send all]** to send every simulated user listed under **[!UICONTROL Test users]** into the journey, or select ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) for a single user to execute the simulation for that user only.

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View Results](#viewing-results).

## View results {#viewing-results}

The **[!UICONTROL Results]** tab allows you to view the test results. In the **[!UICONTROL Test user]** drop-down, select the simulated user whose execution you want to inspect.
 
<!--
* **All simulated users**: Select **[!UICONTROL All]** to see results aggregated across every simulated user in the run. This view helps you scan the full simulation at a glance, activity, outcomes, and errors, without picking a single simulated user first.
-->

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
