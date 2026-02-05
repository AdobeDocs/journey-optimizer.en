---
solution: Journey Optimizer
product: journey optimizer
title: Access & manage challenges and tasks
description: Learn how to access, manage, and organize loyalty challenges and tasks in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
mini-toc-levels: 1
---

# Access & manage challenges and tasks {#access-loyalty-challenges}

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. To request access, contact your Adobe representative. Learn more about [availability labels](../rn/releases.md#availability-labels).

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](get-started.md) - Overview, workflow, prerequisites
* **Access & manage challenges and tasks** ◀︎ **You are here** - Inventory, challenge and task management
* [Create challenges](create-challenges.md) - Build and configure challenges
* [Create tasks](create-tasks.md) - Define challenge tasks

>[!ENDSHADEBOX]

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
* **[!UICONTROL Status]**: Current status of the associated journey (Draft, Live, Stopped, etc.)
* **[!UICONTROL Start/End Date (UTC)]**: When the challenge becomes active and expires

From the Challenges tab, you can perform actions on challenges:

* **View challenge**: Select the challenge name to open its details page
* **Duplicate a challenge**: Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Duplicate]**. A copy is created with all tasks, content, and messaging intact.
* **Delete a challenge**: Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Delete]**
* **Edit a challenge**: Select the challenge name to open its details page and edit it.

  When you open a published challenge for editing, you first need to revert it to "Draft" status. Any customizations made directly to the auto-generated journey will be lost. After making your changes, save and publish the challenge again, and republish the associated journey.

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
* **Delete a task**: Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Delete]**
