---
solution: Journey Optimizer
product: journey optimizer
title: Test your journey
description: Learn how to simulate your journey
feature: Journeys, Test Profiles
topic: Content Management
role: User
level: Intermediate
keywords: test, journey, check, error, troubleshooting
version: Journey Orchestration
badge: label="Limited Availability" type="Informative"
---
# Simulate your journey{#testing_the_journey}

>[!IMPORTANT]
>
> This capability is available to all customers as a Limited Availability with essential capabilities.

You can set the journey to **[!UICONTROL Simulation]** in addition to **Draft**, **Test mode**, and **Live**. In Simulation, you test with **simulated users**: temporary profiles you add, without using persistent test profiles in Adobe Experience Platform.

Adobe Journey Optimizer offers two ways to test and validate your journey:

* **[Simulation](#test-users)**: Use the **[!UICONTROL Simulation]** journey status and simulated users for quick runs without pre-created profiles in Adobe Experience Platform.

* **[Test mode](testing-the-journey.md)**: Use persistent profiles flagged as test profiles in Adobe Experience Platform, reusable across sessions. Choose this approach when you need consistent, predefined data. [Learn how to create test profiles](../audience/creating-test-profiles.md).

Note that Journey Simulation is in **Limited availability**. To share beta feedback and help us improve the experience, open **[!UICONTROL Beta feedback]** from the top bar.

![Beta feedback menu](assets/beta-feedback.png)

## Limitations {#limitations}

In this release, **[!UICONTROL Simulation]** may not support every activity, channel, or integration that **[!UICONTROL Test mode]** or a live journey supports, and behavior may change as the capability matures. Use the procedures in this article for supported workflows.

Refer to the drop-downs below to learn more on Simulation limitations.

+++ Node-level restrictions

If a journey contains any of the following nodes, it cannot be started in simulation mode in this **Limited Availability** release. The journey must be modified, or the relevant node removed, before simulation can run.

| Restricted node | Behavior in Limited Availability |
| --- | --- |
| Business Events | Not supported: journeys that enter through a business event cannot be run in **[!UICONTROL Simulation]** with Limited Availability release. |
| Supplemental ID (multiple re-entrance) | Not supported: concurrent re-entrance (several active instances for the same profile) prevents **[!UICONTROL Simulation]** from starting. |
| Content Decision node | Blocked: this activity must be removed or changed before you can simulate the journey. |
| Dataset Lookup | Not supported: customer dataset lookups by key block **[!UICONTROL Simulation]** for any journey that includes this activity. |
| Path Experimentation (Optimize — Experiment variant) | Blocked with Limited Availability release. You can still use **[!UICONTROL Optimize]** for flows that used to live under **[!UICONTROL Condition]** (for example, data source conditions). |
| Path Targeting (Optimize, Targeting Rule variant) | Blocked with Limited Availability release.|
| Not supported outbound actions | **[!UICONTROL WhatsApp]** and **[!UICONTROL Direct mail]** in the journey stop **[!UICONTROL Simulation]** from starting. |
| Inbound actions | **[!UICONTROL In-app]**, **[!UICONTROL Web]**, **[!UICONTROL Code-based experience]**, and **[!UICONTROL Content card]** actions in the journey stop **[!UICONTROL Simulation]** from starting. |

+++

</br>

+++ Functionality not supported in Limited Availability

The following capabilities are explicitly out of scope for this **Limited Availability** release.

| Capability | Status in Limited Availability |
| --- | --- |
| Exit criteria | Not supported: exit criteria are not applied when you run **[!UICONTROL Simulation]** in this release. |
| External audiences | Not supported: you cannot start **[!UICONTROL Simulation]** on a journey that uses an audience that is not based on [!DNL Unified Profile Service] (UPS). |
| [!DNL Adobe Journey Optimizer] decisioning inside an action (for example, email content with Adobe Journey Optimizer decisioning) | Not available: action proofs for content that uses [!DNL Adobe Journey Optimizer] decisioning are not generated in this release. |
| Mock custom action response | [!UICONTROL Custom actions] perform a real outbound call by default. Mocking the response so no external call runs is not available in this release. |
| Consent policy evaluation | Not available: consent cannot be mocked at the simulated-user level in this release. |
| Journey capping and arbitration | Not supported in **[!UICONTROL Simulation]** in this release. |
| Frequency capping (by channel or communication type) | Not supported in **[!UICONTROL Simulation]** in this release. |
| Opt-out management, suppression, and allow lists | Follows messaging routing configuration where it applies. |
| Dynamic subdomain and dynamic attributes in channel configurations | Follows messaging routing configuration where it applies. |
| Send Time Optimization (STO) | Not supported in **[!UICONTROL Simulation]** in this release. |
| Sandbox tooling (copy simulated users across sandboxes) | Not available in this release. |
| Wave sending in journeys | Not available in this release. |
| Quiet hours | Not available in this release. |
| Privacy service | Simulated users are not GDPR-compliant persistent profiles. Do not include real customer data in simulated users. |

+++

</br>

+++ Quantitative guardrails 

These numeric limits apply to **[!UICONTROL Simulation]** in this **Limited Availability** release. They are enforced in the journey interface and at runtime. Limits may change in a later release, if you run near a ceiling, verify behavior in your sandbox.

| Guardrail | Limit | Notes |
| --- | --- | --- |
| Maximum simulated profiles that can be selected and triggered in one batch (batch journeys, event-triggered flows, and audience-qualification flows) | 20 | Counted for each **[!UICONTROL Send all]** or **[!UICONTROL Trigger selected events]**; not a cumulative cap for the whole journey. |
| Maximum unique simulated users tested in a single simulation run | 100 | Reaching **100** unique users in one run blocks **[!UICONTROL Select simulated users]** for new profiles. If you are at **90**, you can add at most **10** more before the same block. |
| Maximum times the same simulated user can be tested in a single simulation run | 5 | Per user, per run. The profile may still enter the journey more often, but only the most recent executions (up to this number) are guaranteed to keep full log detail. |
| Simulation logs retention (time-to-live) | 30 days | Log records are removed automatically when they reach this age. |
| Maximum simulation logs retrieved in one call for a profile run | 200 | Same upper bound as **[!UICONTROL Test mode]**. |
| Maximum journeys that can run in **[!UICONTROL Simulation]** at the same time in one sandbox | 20 | Cap is shared by every **[!UICONTROL Simulation]** journey in that sandbox at once. |
| Maximum active simulated users in one sandbox | 10,000 | Maximum simulated users that can exist in the sandbox at one time. |
| Simulation logs retained per journey | Last 5 simulation runs | Each new run beyond five drops the oldest retained run. |
| Event pre-filling — maximum pre-filled events stored per journey | 20 | When full, the oldest event is removed first. Limit may change by release. |
| Event pre-filling — maximum simulated profiles per event for storing payload | 10 | When full, the oldest profile is removed first. Limit may change by release. |
| Event pre-filling data time-to-live | 7 days | After this period, pre-filled event data is purged. |

+++

## Create and manage simulated users {#test-users}

>[!IMPORTANT]
>
>You need the **Simulate journeys** permission to use the **[!UICONTROL Simulate]** menu. [Learn more](../administration/permissions.md)

Simulated users are temporary profiles you define in **[!UICONTROL Simulation settings]**. This section covers how to create them, from the UI or a JSON file, save them for reuse, adjust or remove them from the list, and send them into the journey.

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

1. Click **[!UICONTROL Send all]** to send every simulated users in the list into the journey. A `Simulated users have been sent successfully.` confirmation message appears when the profiles successfully enter the journey.

    ![Simulated user selection panel](assets/simulate-5.png)

1. Access **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View results](#viewing_logs).

After you validate the journey in **[!UICONTROL Simulation]**, review the **[!UICONTROL Results]** log. If errors appear, leave **[!UICONTROL Simulation]**, apply the required changes to the journey, and run **[!UICONTROL Simulation]** again until the run looks correct. You can then publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

### Select simulated users

Simulated users that you create manually are stored and can be selected from this list when Simulation is enabled on other journeys.

1. Set the journey to **[!UICONTROL Simulation]**. Open the **[!UICONTROL Simulate]** entry point and choose **[!UICONTROL Simulation]** so the journey uses the Simulation status, for example alongside Test mode or Live, depending on your workspace.

    ![Test mode button in journey interface](assets/test-mode-simulated.png)

1. In the **[!UICONTROL Simulation settings]** panel, you can either select previously created simulated users clicking **[!UICONTROL Select simulated users]**.

    ![Test mode in journey interface](assets/simulate-11.png)

1. Select from the list of simulated users that were previously created and saved.

1. Once you have selected your simulated users, they are now available in the **[!UICONTROL Test users]** list. From the options menu, choose between the following option:

    * ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg) to edit users and change its details.
    * ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) to send your simulation to only one simulated user.
    * ![Clear icon](assets/do-not-localize/Smock_Close_18_N.svg) to clear your simulated users from the list. Note that clearing it does not delete it, it can still be selectable from the Simulated users list.

    ![Simulated user selection panel](assets/simulate-4.png)

1. Click **[!UICONTROL Send all]** to send every simulated users in the list into the journey. A `Simulated users entered the journey successfully.` confirmation message appears when the profiles successfully enter the journey.

    ![Simulated user selection panel](assets/simulate-5.png)

1. Click **[!UICONTROL Show log]** to open the execution log and review how each step ran. For more information, see [View logs](#viewing_logs).

After you validate the journey in **[!UICONTROL Simulation]**, review the **[!UICONTROL Results]** log. If errors appear, leave **[!UICONTROL Simulation]**, apply the required changes to the journey, and run **[!UICONTROL Simulation]** again until the run looks correct. You can then publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

## Trigger your events {#firing_events}

If your journey includes one or more events, you can trigger them while Simulation is active.

1. In **[!UICONTROL Select event type]**, select the event to fire for this simulation.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-10.png)

1. Click ![Edit event](assets/do-not-localize/Smock_Edit_18_N.svg) to adjust the event for this simulated user.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-9.png)

1. In the simulated user drop-down, select the profile and finish configuring the event and how it is generated.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-8.png)

1. Click **[!UICONTROL Trigger selected events]**. 
    
    A `Events triggered successfully` confirmation message appears when the profiles successfully enter the journey.

1. Click **[!UICONTROL Show log]** to open the execution log and review how each step ran. For more information, see [View logs](#viewing_logs).

## View results {#viewing-logs}

The **[!UICONTROL Results]** tab allows you to view the test results. In the **[!UICONTROL Test user]** drop-down, select the profile whose execution you want to inspect.

For each activity, the log can show whether the profile entered or exited the step, and errors that occurred during the simulation.

![Logs for test users](assets/simulate-6.png)

For **Wait** activities, the log includes two duration-related values:

* **Defined duration**: The duration specified on the **Wait** activity for the published journey and applied once the journey is live. The log records whether Simulation applies an override from the test settings, for example 10 seconds, rather than relying solely on the value defined on the journey.
* **Actual duration**: The elapsed time the simulated user remained on the **Wait** activity. This value is set from the **[!UICONTROL Test settings]** tab.

When errors appear in the log, leave **Simulation**, apply the required changes to the journey, and run **Simulation** again. After validation succeeds, publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).
