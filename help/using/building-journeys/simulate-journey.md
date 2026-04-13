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
> The use of Journey Simulation is currently unavailable for use with Healthcare Shield or Privacy and Security Shield.

>[!AVAILABILITY]
>
>This feature is currently available to all customers as a limited availability release.

Alongside states such as **Draft**, **Test mode**, and **Live**, your journey can be set to **[!UICONTROL Simulation]**. That status is dedicated to validating the journey using **simulated users** (temporary profiles you create or generate on the fly), without first creating persistent test profiles in Adobe Experience Platform. The experience is delivered through an updated interface compared to earlier iterations, but you still drive validation with simulated users as the underlying approach.

Adobe Journey Optimizer offers two ways to test and validate your journey:

* **[Simulation](#simulated-users)**: Use the **[!UICONTROL Simulation]** journey status and simulated users for quick runs without pre-created profiles in Adobe Experience Platform.

* **[Test mode](testing-the-journey.md)**: Use persistent profiles flagged as test profiles in Adobe Experience Platform, reusable across sessions. Choose this approach when you need consistent, predefined data. [Learn how to create test profiles](../audience/creating-test-profiles.md).

## Create and manage simulated users {#simulated-users}

### Create simulated users

Use **[!UICONTROL Simulation]** when you want to test your journey without creating persistent test profiles in Adobe Experience Platform. You work from the **[!UICONTROL Simulation]** journey status and generate or pick simulated users in the **[!UICONTROL Simulation settings]** experience.

1. Set the journey to **[!UICONTROL Simulation]**. Open the **[!UICONTROL Simulate]** entry point and choose **[!UICONTROL Simulation]** so the journey uses the Simulation status (alongside options such as Test mode or Live, depending on your workspace).

    ![Test mode button in journey interface](assets/test-mode-simulated.png)
    
1. Click **[!UICONTROL Create Simulated Users]** to create new users and select whether to create users from the UI or import them from a JSON file.

    ![Simulated user selection panel](assets/simulate-2.png)

1. If creating from a JSON file, simply update the corresponding fields with your Test user data

1. If creating from the UI, enter a **[!UICONTROL Display name]** and **[!UICONTROL Description]** to identify this simulated user. Then, select the attributes from the Union schema that you want to populate for this user.

    ![Attribute selection from Union schema](assets/simulate-3.png)

1. Click add **[!UICONTROL Audience membership]** to simulate segment memberships.

1. Click **[!UICONTROL Add profile]** to create multiple simulated users in a single session.

1. From your created profiles, following options are available:

    * Duplicate
    * Apply all
    * Delete

1. Click **[!UICONTROL Save]** to store the simulated user(s) for future use.

1. Once you have created your simulated users, they are now available in the Test users list. From the options menu, choose between the following option:

    * ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg) to edit users and change its details.
    * ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) to send your simulation to only one test user.
    * ![Clear icon](assets/do-not-localize/Smock_Close_18_N.svg) to clear your test users from the list. Note that clearing it does not delete it, it can still be selectable from the Simulated users list.

    ![Simulated user selection panel](assets/simulate-3.png)

1. Click **[!UICONTROL Send all]** to send every test users in the list into the journey. A `Simulated users entered the journey successfully.` confirmation message appears when the profiles successfully enter the journey.

    ![Simulated user selection panel](assets/simulate-5.png)

1. Click the **[!UICONTROL Show log]** button to view the test results and verify the journey execution. See [View logs](#viewing_logs) for more details.

1. If errors occur, leave **[!UICONTROL Simulation]**, adjust your journey, and run Simulation again. When testing is complete, you can publish your journey. See [Publish your journey](../building-journeys/publish-journey.md).

### Select simulated users

Simulated users that you **create manually** in a journey are **available in your other journeys** as well.

1. Set the journey to **[!UICONTROL Simulation]**. Open the **[!UICONTROL Simulate]** entry point and choose **[!UICONTROL Simulation]** so the journey uses the Simulation status (alongside options such as Test mode or Live, depending on your workspace).

    ![Test mode button in journey interface](assets/test-mode-simulated.png)

1. In the **[!UICONTROL Simulation settings]** panel, you can either select previously created simulated users clicking Select simulated users.

1. Select from the list of simulated users that were previously created and saved.

1. Once you have selected your simulated users, they are now available in the Test users list. From the options menu, choose between the following option:

    * ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg) to edit users and change its details.
    * ![Send icon](assets/do-not-localize/Smock_Send_18_N.svg) to send your simulation to only one test user.
    * ![Clear icon](assets/do-not-localize/Smock_Close_18_N.svg) to clear your test users from the list. Note that clearing it does not delete it, it can still be selectable from the Simulated users list.

    ![Simulated user selection panel](assets/simulate-4.png)

1. Click **[!UICONTROL Send all]** to send every test users in the list into the journey. A `Simulated users entered the journey successfully.` confirmation message appears when the profiles successfully enter the journey.

    ![Simulated user selection panel](assets/simulate-5.png)

1. Click the **[!UICONTROL Show log]** button to view the test results and verify the journey execution. See [View logs](#viewing_logs) for more details.

1. If errors occur, leave **[!UICONTROL Simulation]**, adjust your journey, and run Simulation again. When testing is complete, you can publish your journey. See [Publish your journey](../building-journeys/publish-journey.md).

## Trigger your events {#firing_events}

A test event menu is available if the Journey has one or multiple events.

1. Choose from **[!UICONTROL Select event type]** the event you want to trigger for this simulation. 

1. Click ![Edit event](assets/do-not-localize/Smock_Edit_18_N.svg) to further customize the fields passed and the execution of the event sending. 

1. Open your test user drop-down and select your Event type and how it is produced.

    ![Event configuration interface with fields and drop-down for event selection](assets/simulate-8.png)

1. Once configured, select Trigger selected events.

Following message is displayed: `Events triggered successfully`.

## View logs {#viewing_logs}

The **[!UICONTROL Show log]** button allows you to view the test results. Select from the test user drop-down, the information you want to know for each test user.

Information for each activity is displayed such as profile entered/exited or any error that occured during the simulation

If errors occur, leave **[!UICONTROL Simulation]**, adjust your journey, and run Simulation again. When testing is complete, you can publish your journey. See [Publish your journey](../building-journeys/publish-journey.md).

![Logs for test users](assets/simulate-6.png)
