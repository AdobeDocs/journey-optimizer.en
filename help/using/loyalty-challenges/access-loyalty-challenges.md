---
solution: Journey Optimizer
product: journey optimizer
title: Access Loyalty Challenges
description: Learn how to access, search, and filter loyalty challenges in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
---

# Access Loyalty Challenges {#access-loyalty-challenges}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](get-started.md) - Overview, workflow, prerequisites
* **Access Loyalty Challenges** ◀︎ **You are here** - Inventory and filtering
* [Create challenges](create-challenges.md) - Build and configure challenges
* [Create tasks](create-tasks.md) - Define challenge tasks
* [Manage challenges](manage-challenges.md) - Edit, monitor, optimize

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. To request access, contact your Adobe representative. Learn more about [availability labels](../rn/releases.md#availability-labels).

## Access the Loyalty Challenges inventory {#access-inventory}

<!-- SCREENSHOT: Journey Optimizer main menu showing "Loyalty challenges" under "Customer journeys" section -->

To access Loyalty Challenges, navigate to Journey Optimizer and select **[!UICONTROL Loyalty challenges]** under the **[!UICONTROL Customer journeys]** section.

<!-- SCREENSHOT: Loyalty Challenges landing page showing the two tabs: Challenges and Tasks -->

The Loyalty Challenges page displays with two tabs:

* **[!UICONTROL Challenges]**: View and manage all loyalty challenges

* **[!UICONTROL Tasks]**: View and manage all tasks that can be reused across challenges

## Challenges inventory {#challenges-tab}

<!-- SCREENSHOT: Challenges tab showing the inventory table with columns: Challenge name, Status, Type, Start date, End date, Created by, Last modified, Tags -->

The Challenges tab displays all challenges sorted by last modified date, with the most recently modified challenges appearing first. The following information is displayed:

* **[!UICONTROL Challenge name]**: The name you assigned to the challenge
* **[!UICONTROL Status]**: Current state of the challenge (see status descriptions below)
* **[!UICONTROL Type]**: Challenge type (Standard, Streak, or Sequential)
* **[!UICONTROL Start date]**: When the challenge becomes active
* **[!UICONTROL End date]**: When the challenge expires
* **[!UICONTROL Created by]**: User who created the challenge
* **[!UICONTROL Last modified]**: Date and time of last modification
* **[!UICONTROL Tags]**: Any tags applied to the challenge for organization

### Challenge statuses {#challenge-statuses}

<!-- VISUAL: Status badges showing different challenge statuses with color coding: Draft (gray), Scheduled (blue), Live (green), Completed (gray), Stopped (red), Archived (gray) -->

Challenges display with different statuses indicating their current state in the lifecycle:

* **Draft**: Challenge is being created or edited
* **Scheduled**: Challenge is published and will become active on the start date
* **Live**: Challenge is active and customers can participate
* **Completed**: Challenge end date has passed or objectives have been met
* **Stopped**: Challenge was manually stopped before completion
* **Archived**: Challenge has been archived for organizational purposes

For detailed information on status transitions and the challenge lifecycle, see [Challenge lifecycle](manage-challenges.md#challenge-lifecycle).

### Search and filter challenges {#search-challenges}

<!-- SCREENSHOT: Search bar and filter panel showing available filters (status, type, dates, tags) with an example of active filters applied -->

You can quickly locate challenges using search and filters:

**Search:**

* Use the search bar to find challenges by entering keywords from the challenge name or description. The search updates results in real-time as you type.

**Filters:**

* Apply one or more filters to narrow your results:
  * **Status**: Filter by challenge status (Draft, Scheduled, Live, Completed, Stopped, Archived)
  * **Type**: Filter by challenge type (Standard, Streak, Sequential)
  * **Dates**: Filter by start date or end date ranges
  * **Tags**: Filter by tags applied to challenges

You can combine multiple filters simultaneously. For example, filter for Live Standard challenges tagged with "Summer2024" to quickly find active seasonal campaigns.

To clear filters, select **[!UICONTROL Clear all]** or remove individual filters.

### Take actions on challenges {#inventory-actions}

<!-- SCREENSHOT: More actions menu (three dots) expanded showing options: Edit, Duplicate, Stop, Archive, Delete -->

From the Challenges tab, you can perform quick actions on challenges:

* **View challenge details**: Select the challenge name to open its details page
* **Edit a challenge**: Select the **[!UICONTROL More actions]** menu (three dots) and choose **[!UICONTROL Edit]**
* **Duplicate a challenge**: Select the **[!UICONTROL More actions]** menu and choose **[!UICONTROL Duplicate]**
* **Stop a live challenge**: Select the **[!UICONTROL More actions]** menu and choose **[!UICONTROL Stop]**
* **Archive a challenge**: Select the **[!UICONTROL More actions]** menu and choose **[!UICONTROL Archive]**
* **Delete a draft challenge**: Select the **[!UICONTROL More actions]** menu and choose **[!UICONTROL Delete]** (only available for drafts)

For detailed information on managing challenges after creation, including editing limitations, duplication strategies, performance monitoring, and troubleshooting, see [Manage challenges](manage-challenges.md).

## Tasks inventory {#tasks-tab}

<!-- SCREENSHOT: Tasks tab showing the inventory table with columns: Task name, Task type, Description, Created by, Last modified, Used in challenges -->

The Tasks tab displays all reusable tasks that can be used across multiple challenges. Tasks created here become available for selection when creating or editing any challenge.

The Tasks inventory displays the following information:

* **[!UICONTROL Task name]**: The name you assigned to the task
* **[!UICONTROL Task type]**: Type of action (Purchase, Spend amount, Visit, Engagement, Custom event)
* **[!UICONTROL Description]**: Brief description of what the task requires
* **[!UICONTROL Created by]**: User who created the task
* **[!UICONTROL Last modified]**: Date and time of last modification
* **[!UICONTROL Used in challenges]**: Number of challenges currently using this task

### Take actions on tasks {#tasks-actions}

From the Tasks tab, you can perform actions on tasks:

* **View task details**: Select the task name to view full configuration
* **Edit a task**: Select the **[!UICONTROL More actions]** menu (three dots) and choose **[!UICONTROL Edit]**
* **Duplicate a task**: Select the **[!UICONTROL More actions]** menu and choose **[!UICONTROL Duplicate]**
* **Delete a task**: Select the **[!UICONTROL More actions]** menu and choose **[!UICONTROL Delete]** (only if not used in any active challenges)
* **View usage**: See which challenges are currently using the task

## Next steps {#next-steps}

Now that you know how to access and navigate the Loyalty Challenges inventory:

* [Create challenges](create-challenges.md) - Learn how to build your first challenge and configure tasks
* [Create tasks](create-tasks.md) - Learn how to define reusable tasks for challenges
* [Manage challenges](manage-challenges.md) - Learn how to edit, monitor, and optimize challenges
