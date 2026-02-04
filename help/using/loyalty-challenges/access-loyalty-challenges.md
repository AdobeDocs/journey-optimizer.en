---
solution: Journey Optimizer
product: journey optimizer
title: Access and manage Loyalty Challenges
description: Learn how to access, manage, and organize loyalty challenges and tasks in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
---

# Access and manage Loyalty Challenges {#access-loyalty-challenges}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](get-started.md) - Overview, workflow, prerequisites
* **Access Loyalty Challenges** ◀︎ **You are here** - Inventory, challenges and tasks management
* [Create challenges](create-challenges.md) - Build and configure challenges
* [Create tasks](create-tasks.md) - Define challenge tasks

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>This feature is currently in **private beta** and may not be available in your environment. To request access, contact your Adobe representative. Learn more about [availability labels](../rn/releases.md#availability-labels).

## Access Loyal Challenges

To access Loyalty Challenges, navigate to Journey Optimizer and select **[!UICONTROL Loyalty Challenge (Beta)]** under the **[!UICONTROL Journey management]** section.

The Loyalty Challenges interface provides a centralized location to view, manage, and organize all your challenges and tasks. You can access two main inventories:

* **Challenges inventory**: View and manage all loyalty challenges, monitor their status, and perform quick actions
* **Tasks inventory**: Browse reusable tasks that can be used across multiple challenges

## Challenges inventory {#challenges-tab}

The **[!UICONTROL Challenges]** tab displays all challenges sorted by last modified date, with the most recently modified challenges appearing first.

![](assets/challenges-inventory.png)

Key information displayed:

* **[!UICONTROL Challenge]**: Challenge name
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

  When you open a published challenge for editing, you first need to revert it to Draft status:

  * Any customizations made directly to the auto-generated journey will be lost
  * The challenge returns to Draft status
  * After making your changes, you must save and publish the challenge again
  * You must republish the associated journey to make the updated challenge available to customers

  >[!IMPORTANT]
  >
  >Reverting a published challenge to draft cannot be undone. Consider the impact on your active journey before proceeding.

## Tasks inventory {#tasks-tab}

The **[!UICONTROL Tasks]** tab displays all reusable tasks that can be used across multiple challenges. Tasks created here become available for selection when creating or editing any challenge.

![](assets/tasks-inventory.png)

Key information displayed:

* **[!UICONTROL Task Name]**: The name you assigned to the task
* **[!UICONTROL Description]**: Brief description of what the task requires
* **[!UICONTROL Task Activity]**: Type of activity (Purchase, Spend)
* **[!UICONTROL SKU]**: Eligible and/or excluded items
* **[!UICONTROL Used in challenges]**: Number of challenges currently using this task

From the Tasks tab, you can perform actions on tasks:

* **View/Edit task**: Select the task name to view full configuration and edit the task
* **Duplicate a task**: Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Duplicate]**
* **Delete a task**: Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Delete]**
