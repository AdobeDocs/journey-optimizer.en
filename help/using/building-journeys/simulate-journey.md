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
# Simulate your journey {#simulate-journey}

>[!BEGINSHADEBOX]

**On this page:** Learn how to run Quick simulation and Manual simulation with simulated users to validate journey paths and review results before you publish.

>[!ENDSHADEBOX]

Not sure Simulation is the right method for you? [Compare all three validation options](choose-validation-method.md).

Use **[!UICONTROL Simulation]** to validate your journey with **simulated users** before you publish. This page walks you through **[!UICONTROL Quick simulation]** and **[!UICONTROL Manual simulation]**, creating and sending simulated users, triggering unitary events when your journey needs them, and reviewing the **[!UICONTROL Results]** log. 

>[!IMPORTANT]
>
>* To use **[!UICONTROL Simulation]**, assign at least one permission from the **[!UICONTROL Journeys]** capability: **Simulate journeys**, **Publish journeys**, or **Approve and Publish journeys**. The same permissions let you create and manage simulated users, **[!UICONTROL Simulated Users]** permissions are not required. [Learn more](../administration/permissions.md)
>
>* To manage simulated users without **[!UICONTROL Simulation]**, assign **Manage Simulated Users** or **View Simulated Users** from the **[!UICONTROL Simulated Users]** capability.
>
>* For AI in simulation (**[!UICONTROL Quick simulation]**, AI-generated users, **[!UICONTROL Generate event values]**), assign **[!UICONTROL Generate Content]** from the **[!UICONTROL AI Assistant]** capability.

For an overview by journey type, see [Get started with Journey simulation](simulate-journey-gs.md).

## Simulation types {#simulation-types}

After activation, batch journeys with read audience entry offer two ways to run a simulation:

* **[!UICONTROL Quick simulation]** runs end-to-end with generated users, generated event values, and default test settings, powered by the Journey Agent. It is a quick way to simulate a journey end to end with minimal intervention. Quick simulation starts as soon as you select this option. [Watch the Quick simulation video](simulate-journey-gs.md#video)

* **[!UICONTROL Manual simulation]** lets you run a simulation step by step, manually. Create simulated users (manually or with the Journey Agent), trigger them into the journey, define event payloads (manually or with the Journey Agent), and override waits.

![Simulation settings panel with Quick simulation and Manual simulation options next to the journey canvas](assets/quick-simulation-1.png)

### Quick simulation {#quick-simulation}

On any journey in **[!UICONTROL Simulation]**, **[!UICONTROL Quick simulation]** runs the journey with generated users, event values and pre-filled settings.


1. Select **[!UICONTROL Quick simulation]**.

1. Review the fields Adobe Journey Optimizer gathered for the run. Click **[!UICONTROL Update values]** to change test settings and execution addresses, or continue without changes. 

    This step appears only if the journey uses Waits or Channels. You can adjust all Wait durations and execution addresses for simulated users, for example, use your own email so messages from the run go to your inbox.

    ![Quick Simulation dialog on the Gathering information step with Update values and Continue to next step](assets/quick-simulation-2.png)
  
1. If you opened **[!UICONTROL Update values]**, edit the settings, for example, the address used for message proofs, then confirm to start the simulation.

    >[!NOTE]
    >
    >Pre-filled execution email, phone and push token fields come from values previously used in journey simulation and cached in your browser.

    ![Quick Simulation Update values step with wait time override and proof email, phone and push token fields](assets/quick-simulation-3.png)

1. The Journey Agent generates a set of simulated users from the journey definition.

    For journeys with an Email, SMS, or Push node, the Agent prompts you to confirm the email address, phone number, or push token to use. Simulated users are generated using those values. Once done, click **[!UICONTROL Generate]**.

1. When the run completes, click **[!UICONTROL View results]** to review paths, errors, and uncovered branches. See [View results](#viewing-results).

    ![Quick Simulation completed with all steps succeeded and View Results available](assets/quick-simulation-4.png)

Quick simulation also supports event-triggered journeys and journeys that include event activities. Event values are set and fired automatically for every generated simulated user. Once a user enters the journey, each event is triggered as soon as they reach the corresponding Wait.

### Manual simulation {#manual-simulation}

Choose **[!UICONTROL Manual simulation]** when you need to pick each simulated user, control send order, configure event payloads, and override **[!UICONTROL Wait]** durations for the run.

Continue with [Create and manage simulated users](#test-users), [Trigger your events](#firing-events), and [View results](#viewing-results).

## Create and manage simulated users {#test-users}

>[!CAUTION]
>
>Sending a simulated user triggers a real message send. if an impacted dataset, e.g. feedback events or tracking events, is profile-enabled, this can create a persistent profile in Adobe Experience Platform for that user, even though the run is a simulation.

Simulated users are temporary profile-like entities you define in **[!UICONTROL Simulation settings]**. This section covers how to create them, save them for reuse, adjust or remove them from the list, and send them into the journey.

If your journey uses an external audience, for example a CSV or Federated Audience Composition audience, and your conditions, expressions, or personalization rely on enrichment attributes from it, you can mock those attributes on a simulated user just like profile attributes. This lets you drive the user into a specific branch based on the value you set, without running the actual audience.

1. Start by populating the **[!UICONTROL Test users]** list:

    +++ Generate users with AI
        
    Adobe Journey Optimizer generates a set of simulated users from the journey definition. 
        
    For journeys with an Email, Push, or SMS node, the AI prompts you to confirm the email address, phone number, or push token to use. Simulated users are generated using those defined values. Once done, click [!UICONTROL Generate].

    Generated simulated users only show the attributes used in the current journey, for example in expressions or personalization.

    >[!NOTE]
    >
    >The email, phone and push token fields are pre-filled from values previously used in journey simulation and cached in your browser.

    ![Generate simulated users dialog with execution email, phone and push token fields and Generate button](assets/simulate-generate.png)

    +++

    +++ Browse inventory
        
    Choose **[!UICONTROL Browse inventory]** to add simulated users you already saved, for example, users you created from a form or JSON, or users you kept after an AI generation run.

    Note that when you select a simulated user from the inventory, only the attributes used in the current journey are shown, even if the user has values for other attributes set in a different journey.

    ![Simulated Users inventory dialog with search, user table, and Select button](assets/simulate-inventory.png)

    +++

    +++ Create from form

    1. Enter a **[!UICONTROL Display name]**, **[!UICONTROL Identity namespace]** and **[!UICONTROL Description]** to identify this simulated user. 
            
        ![Create Simulated Users form with display name, identity namespace, description, and Union schema attributes](assets/simulate-form.png)

    1. Then, select the attributes from the Union schema that you want to populate for this user. Note that only the attributes used in the current journey, for example in expressions or personalization, are available here. 
    
        Attributes are grouped by origin, in separate sections for profile attributes and, if your journey reads an external audience such as a CSV or Federated Audience Composition audience, for that audience's enrichment attributes.

    1. Click **[!UICONTROL Add audience membership]** to simulate segment memberships.

    1. In the **[!UICONTROL Create Simulated Users]** window, click **[!UICONTROL Add simulated user]** to define several simulated users in one session.

        You can change how users are shown in the list, collapse every card in stacked view, or open a user's attribute metadata.
    
        ![Create Simulated Users footer with Add simulated user, Collapse all, and layout view controls](assets/simulate-form-3.png)

    1. From your Simulated user menu, use **[!UICONTROL Duplicate]** to copy a user, **[!UICONTROL Apply all attributes to other users]** to copy one user's attributes to every other user in the session, or **[!UICONTROL Delete]** to remove a user.

        ![Create Simulated Users cards with Duplicate, Apply all attributes to other users, and Delete on each user](assets/simulate-form-2.png)

    1. Click **[!UICONTROL Save]** when you finish configuring users in this session.
        
    +++

    +++ Create from JSON

    In **[!UICONTROL Create Simulated Users]**, edit the JSON template to define users, then click **[!UICONTROL Format JSON]** and **[!UICONTROL Save]**.

    Note that **[!UICONTROL Create from JSON]** and **[!UICONTROL Update from JSON]** give you access to every attribute stored on the simulated user, including profile attributes and, if applicable, enrichment attributes from an external audience such as a CSV or Federated Audience Composition audience.

    ![Create Simulated Users JSON editor with users template and Format JSON control](assets/simulate-json.png)

    +++

<!--
    To reuse attribute values from a profile or [test profile](../audience/creating-test-profiles.md) in [!DNL Adobe Experience Platform]:

    1. Browse to the profile you want to use as a reference. On the profile detail page, click **[!UICONTROL View JSON]**. [Learn more](../audience/get-started-profiles.md)

        ![Profile JSON view in Adobe Experience Platform](assets/simulate-json-1.png)

    1. Copy the JSON from the viewer.

    1. In the journey, open **[!UICONTROL Simulation settings]**, start **[!UICONTROL Create Simulated Users]**, and choose **Create from JSON**.

    1. Paste the JSON into the matching part of the simulated user template (for example, the attribute block for one user). Click **[!UICONTROL Format JSON]** to validate the structure.

        ![Create Simulated Users JSON editor with pasted profile attributes](assets/simulate-json-2.png)

    1. Remove properties that exist on the [!DNL Adobe Experience Platform] profile only tied to the source profile, such as mergePolicyId or lastModifiedAt.

    1. Set the fields required by the simulated user template: **[!UICONTROL Display name]**, **[!UICONTROL Identity namespace]**, identity value, and channel execution addresses.

    1. Click **[!UICONTROL Save]**. Use ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg) on the saved simulated user to review the data before you run **[!UICONTROL Simulation]**.

        ![Create Simulated Users JSON editor with users template and Format JSON control](assets/simulate-json-3.png)

        If you paste profile JSON, remove or replace all production identifiers and contact points (email, phone, ECID, push token, and similar). Simulation will send messages using the data you provide.
-->

1. The simulated users you created appear in the **[!UICONTROL Test users]** list. For each entry, select one of the following:

    * ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg): Update the simulated user's details.
    * ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg): Run the simulation for this simulated user only.
        
        This option is not available for journeys starting with an Event, as the simulated user entrance is triggered by the event being sent. [Learn more](#firing-events)

    * ![Clear icon](assets/do-not-localize/Smock_Close_18_N.svg): Remove the user from this list. The simulated user is not deleted and remains available in the Simulated Users selection.

    ![Test users list with edit, send, and remove actions and simulated path highlighted on the canvas](assets/simulate-4-2.png)

1. To change the list after your selection, click **[!UICONTROL Manage users]** to add more simulated users, from the inventory or by creating new ones. To remove every user from the **[!UICONTROL Test users]** list for this run, choose **[!UICONTROL Clear all users]**.

    ![Manage users menu open with add-user options and Clear all users](assets/simulate-manage.png)

1. If your journey includes a **[!UICONTROL Wait]** activity, open the **[!UICONTROL Test settings]** tab to fine-tune how long that wait lasts during the simulation. For example, if the live **[!UICONTROL Wait]** activity is configured for several days, you can override it to 10 seconds so the simulated user only spends that long on the node before moving to the next activity.

1. Click **[!UICONTROL Send all]** to send every simulated user in the list into the journey, or click ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) on a row to send only that user. A `Simulated users have entered the journey successfully.` confirmation message appears when the simulated users successfully enter the journey.

    ![Test users tab after users enter the journey with success message and path on the canvas](assets/simulate-5-2.png)

1. If the journey includes unitary events, you need to select the event to trigger. See [Trigger your events](#firing-events).

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View results](#viewing-results).

1. When you finish testing, open the **[!UICONTROL Manage simulation]** menu:

    * **[!UICONTROL Stop simulation]** to exit the current simulation session.
    * **[!UICONTROL Reset simulation]** to clear all data from the current run, selected simulated users, defined event values, and other test settings, so you can start a new simulation from scratch.

        ![Manage simulation menu open with Reset simulation and Close simulation options](assets/simulate-15.png)

After you validate the journey in **[!UICONTROL Simulation]**, review the **[!UICONTROL Results]** log. If errors appear, leave **[!UICONTROL Simulation]**, apply the required changes to the journey, and run **[!UICONTROL Simulation]** again until the run looks correct. You can then publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

## Trigger your events {#firing-events}

>[!NOTE]
>
>Events triggered in Simulation are stored in dedicated datasets in Adobe Experience Platform, labeled as follows: ``JOtestmode - <schema of your event>``.

If your journey includes one or more unitary events, you can trigger them while Simulation is active. For journeys not starting from an Event but containing one, this section will not be visible until a simulated user enters the journey.

1. In **[!UICONTROL Select event type]**, select the event to fire for this simulation.

    ![Select event type dropdown open in the Test events section of Simulation settings](assets/simulate-10-2.png)

1. To apply the same change to every user in the list, use the **[!UICONTROL Manage events]** option to:

    * **[!UICONTROL Generate event values]** to let the Journey Agent generate all payloads using AI. When values are generated, the user is marked **[!UICONTROL Ready to send]**.
    * **[!UICONTROL Edit event data]** to change the payload for every simulated user in the list.

    ![Manage events menu in Test events with Generate with AI and Edit all options](assets/simulate-9-2.png)

1. Configure the event payload for each user by clicking the ![Edit event](assets/do-not-localize/Smock_Edit_18_N.svg) beside a user to:

    * **[!UICONTROL Generate event values]** to let the Journey Agent generate the payload using AI. When values are generated, the user is marked **[!UICONTROL Ready to send]**.
    * **[!UICONTROL Edit event data]** to change the payload for that simulated user only.

    ![Per-user menu in Test events with Generate event values and Edit event data options](assets/simulate-8-2.png)

1. In **[!UICONTROL Test events]**, either select **[!UICONTROL Send all]** to send this event for all simulated users listed under **[!UICONTROL Test users]**, or select ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) for a single event to be triggered for that user only.

    ![Test events section with Send all and per-user send controls for users marked Ready](assets/simulate-11-2.png)

1. After events are fired, the canvas updates to reflect each user's progression.

1. Access the **[!UICONTROL Results]** tab to open the execution log and review how each step ran. For more information, see [View results](#viewing-results).

1. When you finish testing, open the **[!UICONTROL Manage simulation]** menu:

    * **[!UICONTROL Stop simulation]** to exit the current simulation session.
    * **[!UICONTROL Reset simulation]** to clear all data from the current run, selected simulated users, defined event values, and other test settings, so you can start a new simulation from scratch.

        ![Manage simulation menu open with Reset simulation and Stop simulation options](assets/simulate-15.png)

## View results {#viewing-results}

The **[!UICONTROL Results]** tab allows you to view the test results. In the **[!UICONTROL Test user]** drop-down, select the simulated user whose execution you want to inspect. When you select a single simulated user, the canvas highlights the exact path that user followed through the journey, so you can confirm they entered the branch you expected.

Select **[!UICONTROL All]** to see results aggregated across every simulated user in the run. The canvas then shows every path covered by the run, which helps you compare coverage across profiles and scan the full simulation at a glance, including activities, outcomes, and errors, without picking a single simulated user first.

![Results tab with simulation summary, test user filter, and path coverage on the journey canvas](assets/simulate-6-2.png)

For each activity, the log can show whether the simulated user entered or exited the step, the timestamps and branch decisions for each step, and errors that occurred during the simulation.

For **Wait** activities, the log includes two duration-related values:

* **Defined duration**: The duration specified on the **Wait** activity for the published journey and applied once the journey is live. The log records whether Simulation applies an override from the test settings, for example 10 seconds, rather than relying solely on the value defined on the journey.
* **Actual duration**: The elapsed time the simulated user remained on the **Wait** activity. This value is set from the **[!UICONTROL Test settings]** tab.

When errors appear in the log, leave **Simulation**, apply the required changes to the journey, and run **Simulation** again. After validation succeeds, publish the journey. See [Publish your journey](../building-journeys/publish-journey.md).

{{$include /help/_includes/do-not-localize/building-journeys/ai-knowledge-reference-simulate-journey.md}}
