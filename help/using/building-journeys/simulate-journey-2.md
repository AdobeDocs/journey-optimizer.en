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
hide: true
feature_v2: []
subfeature_v2: []
---
# Simulate your journey{#simulate-journey}
 
Use **[!UICONTROL Simulation]** to validate your journey with **simulated users** before you publish. This page walks you through **[!UICONTROL Quick simulation]** and **[!UICONTROL Manual simulation]**, creating and sending simulated users, triggering unitary events when your journey needs them, and reviewing the **[!UICONTROL Results]** log. 

For an overview by journey type, see [Get started with Journey simulation](simulate-journey-gs.md).

## Simulation types {#simulation-types}

After activation, batch journeys with read audience entry offer two ways to run a simulation:

* **[!UICONTROL Quick simulation]** runs end-to-end with generated users and defaults. Note that quick simulation is not available with unitary journeys. 

* **[!UICONTROL Manual simulation]** lets you choose users, send order, event payloads, and wait overrides step by step. 

![Quick simulation and Manual simulation in the Simulation panel](assets/quick-simulation-1.png)

### Quick simulation {#quick-simulation}

On a batch journey in **[!UICONTROL Simulation]**, **[!UICONTROL Quick simulation]** runs the journey with generated users and pre-filled settings.

1. Select **[!UICONTROL Quick simulation]**.

1. Review the fields Adobe Journey Optimizer gathered for the run. Click **[!UICONTROL Update values]** to change proof or channel settings, or continue without changes.

    ![Quick simulation review step](assets/quick-simulation-2.png)
  
1. If you opened **[!UICONTROL Update values]**, edit the settings, for example, the address used for message proofs, then confirm to start the simulation.

    ![Quick simulation update values](assets/quick-simulation-3.png)

1. Adobe Journey Optimizer generates simulated users from the journey definition and triggers each user into the journey.

1. When the run completes, click **[!UICONTROL View results]** to review paths, errors, and uncovered branches. See [View results](#viewing-results).

    ![Quick simulation completed run](assets/quick-simulation-4.png)

### Manual simulation {#manual-simulation}

Choose **[!UICONTROL Manual simulation]** when you need to pick each simulated user, control send order, configure event payloads, and override **[!UICONTROL Wait]** durations for the run. This flow applies to batch and unitary journeys.

Continue with [Create and manage simulated users](#test-users), [Trigger your events](#firing_events), and [View results](#viewing-results).

## Create and manage simulated users {#test-users}

>[!IMPORTANT]
>
>You need at least one of the following permissions to access the **[!UICONTROL Simulation]** feature: **Simulate journeys**, **Publish journeys**, or **Approve and Publish journeys**. [Learn more](../administration/permissions.md)

Simulated users are temporary profile-like entities you define in **[!UICONTROL Simulation settings]**. This section covers how to create them, save them for reuse, adjust or remove them from the list, and send them into the journey.

1. Start by populating the **[!UICONTROL Test users]** list:

    +++ Generate users with AI
        
    Adobe Journey Optimizer generates a set of simulated users from the journey definition. 
        
    For journeys with an Email or SMS node, the AI prompts you to confirm the email address or phone number to use. Once done, click **[!UICONTROL Generate]**.

    ![Simulated user selection panel](assets/simulate-generate.png)

    +++

    +++ Browse inventory
        
    Choose **[!UICONTROL Browse inventory]** to add simulated users you already saved, for example, users you created from a form or JSON, or users you kept after an AI generation run.
        
    ![Simulated user selection panel](assets/simulate-inventory.png)

    +++

    +++ Create from form

    1. Enter a **[!UICONTROL Display name]**, **[!UICONTROL Identity namespace]** and **[!UICONTROL Description]** to identify this simulated user. 
            
        ![Simulated user selection panel](assets/simulate-form.png)

    1. Then, select the attributes from the Union schema that you want to populate for this user.

    1. Click **[!UICONTROL Add audience membership]** to simulate segment memberships.

    1. In the **[!UICONTROL Create Simulated Users]** window, click **[!UICONTROL Add simulated user]** to define several simulated users in one session.

        You can change how users are shown in the list, collapse every card in stacked view, or open a user's attribute metadata.
    
        ![Simulated user selection panel](assets/simulate-form-3.png)

    1. From your Simulated user menu, use **[!UICONTROL Duplicate]** to copy a user, **[!UICONTROL Apply all attributes to other users]** to copy one user's attributes to every other user in the session, or **[!UICONTROL Delete]** to remove a user.

        ![Simulated user selection panel](assets/simulate-form-2.png)

    1. Click **[!UICONTROL Save]** when you finish configuring users in this session.
        
    +++

    +++ Create from JSON

    Define new simulated users by updating the corresponding fields with your simulated user data.

    ![Simulated user selection panel](assets/simulate-json.png)

    +++

1. The simulated users you created appear in the **[!UICONTROL Test users]** list. For each entry, select one of the following:

    * ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg): Update the simulated user's details.
    * ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg): Run the simulation for this simulated user only.
    * ![Clear icon](assets/do-not-localize/Smock_Close_18_N.svg): Remove the user from this list. The simulated user is not deleted and remains available in the Simulated Users selection.

    ![Simulated user selection panel](assets/simulate-4-2.png)

1. To change the list after your selection, click **[!UICONTROL Manage users]** to add more simulated users, from the inventory or by creating new ones. To remove every user from the **[!UICONTROL Test users]** list for this run, choose **[!UICONTROL Clear all users]**.

    ![Simulated user selection panel](assets/simulate-manage.png)

1. If your journey includes a **[!UICONTROL Wait]** activity, open the **[!UICONTROL Test settings]** tab to fine-tune how long that wait lasts during the simulation. For example, if the live **[!UICONTROL Wait]** activity is configured for several days, you can override it to 10 seconds so the simulated user only spends that long on the node before moving to the next activity.

1. Click **[!UICONTROL Send all]** to send every simulated user in the list into the journey, or click ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) on a row to send only that user. A `Simulated users have entered the journey successfully.` confirmation message appears when the simulated users successfully enter the journey.

    ![Simulated user selection panel](assets/simulate-5-2.png)

1. If the journey includes unitary events, you need to select the event to trigger. See [Trigger your events](#firing_events).

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View results](#viewing-results).

After you validate the journey in **[!UICONTROL Simulation]**, review the **[!UICONTROL Results]** log. If errors appear, leave **[!UICONTROL Simulation]**, apply the required changes to the journey, and run **[!UICONTROL Simulation]** again until the run looks correct. You can then publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

## Trigger your events {#firing_events}

If your journey includes one or more unitary events, you trigger them while Simulation is active.

1. In **[!UICONTROL Select event type]**, select the event to fire for this simulation.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-10-2.png)

1. To apply the same change to every user in the list, use the **[!UICONTROL Manage events]** option to:

    * **[!UICONTROL Generate event values]** to let Adobe Journey Optimizer generate the payload using AI. When values are generated, the user is marked **[!UICONTROL Ready to send]**.
    * **[!UICONTROL Edit event date]** to change the payload for that simulated user only.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-9-2.png)

1. Configure the event payload for each user by clicking the ![Edit event](assets/do-not-localize/Smock_Edit_18_N.svg) beside a user to:

    * **[!UICONTROL Generate event values]** to let Adobe Journey Optimizer generate the payload using AI. When values are generated, the user is marked **[!UICONTROL Ready to send]**.
    * **[!UICONTROL Edit event date]** to change the payload for that simulated user only.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-8-2.png)

1. In **[!UICONTROL Test events]**, either select **[!UICONTROL Send all]** to send every simulated user listed under **[!UICONTROL Test users]** into the journey, or select ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) for a single user to execute the simulation for that user only.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-11-2.png)

1. After events are fired, the canvas updates to reflect each user's progression. Click any row in the **[!UICONTROL Test users]** list to see the new path that user took through the journey.

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View results](#viewing-results).

## View results {#viewing-results}

The **[!UICONTROL Results]** tab allows you to view the test results. In the **[!UICONTROL Test user]** drop-down, select the simulated user whose execution you want to inspect.

Select **[!UICONTROL All]** to see results aggregated across every simulated user in the run. This view helps you scan the full simulation at a glance, activities, outcomes, and errors, without picking a single simulated user first.

![Logs for test users](assets/simulate-6-2.png)

For each activity, the log can show whether the simulated user entered or exited the step, and errors that occurred during the simulation.

For **Wait** activities, the log includes two duration-related values:

* **Defined duration**: The duration specified on the **Wait** activity for the published journey and applied once the journey is live. The log records whether Simulation applies an override from the test settings, for example 10 seconds, rather than relying solely on the value defined on the journey.
* **Actual duration**: The elapsed time the simulated user remained on the **Wait** activity. This value is set from the **[!UICONTROL Test settings]** tab.

When errors appear in the log, leave **Simulation**, apply the required changes to the journey, and run **Simulation** again. After validation succeeds, publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).
