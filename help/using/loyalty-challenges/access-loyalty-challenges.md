---
solution: Journey Optimizer
product: journey optimizer
title: Access & manage challenges and tasks
description: Learn how to access, manage, and organize loyalty challenges and tasks in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: true
badge: label="Private beta" type="Informative"
mini-toc-levels: 1
exl-id: 8907c18e-4623-4743-a76b-333f34e13baf
---
# Access & manage challenges and tasks {#access-loyalty-challenges}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](get-started.md)
* **Access & manage challenges and tasks** ◀︎ **You are here**
* [Create challenges](create-challenges.md)
* [Create tasks](create-tasks.md)
* [Loyalty Challenges API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges/){target="_blank"}

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta**. For full details about the release cycle and availability phases, see [Journey Optimizer release cycle](../rn/releases.md).

## Access & manage challenges and tasks

To access Loyalty Challenges, navigate to Journey Optimizer and select **[!UICONTROL Loyalty Challenge (Beta)]** under the **[!UICONTROL Journey management]** section. The Loyalty Challenges interface provides a centralized location to view, manage, and organize all your challenges and tasks.

The interface provides access to two main inventories:

* **Challenges**: View and manage all loyalty challenges, monitor their status, and perform quick actions such as viewing, editing, duplicating, or deleting challenges
* **Tasks**: Browse reusable tasks that can be used across multiple challenges, and manage task definitions independently

## Challenges inventory {#challenges-tab}

The **[!UICONTROL Challenges]** tab displays all challenges sorted by last modified date, with the most recently modified challenges appearing first.

![](assets/challenges-inventory.png)

Key information displayed:

* **[!UICONTROL State]**: Current state of the challenge (Draft or Published)
* **[!UICONTROL Tasks]**: Number of tasks configured in the challenge
* **[!UICONTROL Journey]**: Link to the auto-generated journey associated with the challenge
* **[!UICONTROL Status]**: Current status of the auto-generated journey that delivers the challenge.
* **[!UICONTROL Start/End Date (UTC)]**: When the challenge becomes active and expires

From the Challenges tab, you can perform actions on challenges:

* **View challenge**: Select the challenge name to open its details page
* **Duplicate a challenge**: Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Duplicate]**. A copy is created with all tasks, content, and messaging intact.
* **Delete a challenge**: Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Delete]**.

  >[!IMPORTANT]
  >
  >You can delete a challenge even when it is published. Consider the impact before deleting.

* **Edit a challenge**: Select the challenge name to open its details page and make the desired changes.

  When you open a published challenge for editing, you first need to revert it to Draft state. Any customizations made directly to the auto-generated journey will be lost. After making your changes, save and publish the challenge again, then publish the associated journey. [Learn how to launch a challenge](create-challenges.md#launch)

  >[!IMPORTANT]
  >
  >Reverting a published challenge to draft cannot be undone. Consider the impact on your active journey before proceeding.

## Tasks inventory {#tasks-tab}

The **[!UICONTROL Tasks]** tab displays all reusable tasks that can be used across multiple challenges. Tasks created here become available for selection when creating or editing any challenge.

![](assets/tasks-inventory.png)

Key information displayed:

* **[!UICONTROL Description]**: Brief description of what the task requires
* **[!UICONTROL Task Activity]**: Type of activity (Purchase, Spend)
* **[!UICONTROL SKU]**: Eligible and/or excluded items
* **[!UICONTROL Used in challenges]**: Number of challenges currently using this task

From the Tasks tab, you can perform actions on tasks:

* **View/Edit a task**: Select the task name to view the full configuration and edit the task
* **Duplicate a task**: Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Duplicate]**
* **Delete a task**: Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Delete]**.

  >[!IMPORTANT]
  >
  >You can delete a task even when it is used in one or more challenges. Consider the impact on challenges that reference the task before deleting.
