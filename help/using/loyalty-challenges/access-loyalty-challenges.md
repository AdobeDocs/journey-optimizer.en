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
* [Manage challenges](manage-challenges.md) - Edit, monitor, optimize

>[!ENDSHADEBOX]

## Access the Loyalty Challenges inventory {#access-inventory}

To access Loyalty Challenges:

1. In Adobe Journey Optimizer, select **[!UICONTROL Loyalty challenges]** in the left navigation menu under the **[!UICONTROL Customer journeys]** section.

2. The Loyalty Challenges page displays with two tabs:
   * **[!UICONTROL Challenges]**: View and manage all loyalty challenges
   * **[!UICONTROL Tasks]**: View and manage all tasks that can be reused across challenges

By default, the **[!UICONTROL Challenges]** tab is selected, showing all existing challenges in your organization.

## Challenges tab {#challenges-tab}

The Challenges tab displays all challenges sorted by last modified date, with the most recently modified challenges appearing first.

### Understanding the challenges inventory {#inventory-overview}

The Challenges inventory displays all challenges with the following information:

* **[!UICONTROL Challenge name]**: The name you assigned to the challenge
* **[!UICONTROL Status]**: Current state of the challenge (see status descriptions below)
* **[!UICONTROL Type]**: Challenge type (Standard, Streak, or Sequential)
* **[!UICONTROL Start date]**: When the challenge becomes active
* **[!UICONTROL End date]**: When the challenge expires
* **[!UICONTROL Created by]**: User who created the challenge
* **[!UICONTROL Last modified]**: Date and time of last modification
* **[!UICONTROL Tags]**: Any tags applied to the challenge for organization

### Challenge statuses {#challenge-statuses}

Challenges can have the following statuses:

* **[!UICONTROL Draft]**: Challenge is being created or edited but not yet published
* **[!UICONTROL Scheduled]**: Challenge is published and scheduled to start at a future date
* **[!UICONTROL Live]**: Challenge is currently active and available to the target audience
* **[!UICONTROL Completed]**: Challenge has passed its end date or all objectives have been met
* **[!UICONTROL Stopped]**: Challenge was manually stopped before completion
* **[!UICONTROL Archived]**: Challenge has been archived for organizational purposes

### Search and filter challenges {#search-challenges}

Use the search functionality to quickly find specific challenges by name or description.

You can also apply filters to narrow down the challenge list based on specific criteria. You can combine multiple filters to refine your search.

You can filter challenges by their current status, by their challenge type, based on their start or end dates, or by tags you've applied for organization.

### Take actions on challenges {#inventory-actions}

From the Challenges tab, you can perform quick actions on challenges:

* **View challenge details**: Select a challenge name to open its details page
* **Edit a challenge**: Select the more actions menu (three dots) and choose **[!UICONTROL Edit]**
* **Duplicate a challenge**: Select the more actions menu and choose **[!UICONTROL Duplicate]**
* **Stop a live challenge**: Select the more actions menu and choose **[!UICONTROL Stop]**
* **Archive a challenge**: Select the more actions menu and choose **[!UICONTROL Archive]**
* **Delete a draft challenge**: Select the more actions menu and choose **[!UICONTROL Delete]** (only available for drafts)

### Create a new challenge {#create-from-inventory}

To create a new challenge from the Challenges tab:

1. Select **[!UICONTROL Create challenge]** in the top-right corner.

2. The challenge creation workflow begins.

For detailed instructions, see [Create challenges](create-challenges.md).

## Tasks tab {#tasks-tab}

The Tasks tab displays all reusable tasks that can be used across multiple challenges. Tasks created here become available for selection when creating or editing any challenge.

### Understanding the tasks inventory {#tasks-inventory-overview}

The Tasks inventory displays all tasks with the following information:

* **[!UICONTROL Task name]**: The name you assigned to the task
* **[!UICONTROL Task type]**: Type of action (Purchase, Spend amount, Visit, Engagement, Custom event)
* **[!UICONTROL Description]**: Brief description of what the task requires
* **[!UICONTROL Created by]**: User who created the task
* **[!UICONTROL Last modified]**: Date and time of last modification
* **[!UICONTROL Used in challenges]**: Number of challenges currently using this task

### Create tasks from the Tasks tab {#create-tasks-from-tab}

You can create tasks in two ways:

1. **From the Tasks tab** (recommended for reusable tasks):
   * Navigate to the **[!UICONTROL Tasks]** tab
   * Select **[!UICONTROL Create task]**
   * Configure the task properties (name, type, quantity, product filters, rewards)
   * Save the task to make it available for use in any challenge

2. **When creating a challenge** (for challenge-specific tasks):
   * During challenge creation, select **[!UICONTROL Add task]** in the Tasks section
   * Choose **[!UICONTROL Create new task]** or select from existing tasks
   * Tasks created this way are also saved to the Tasks inventory and can be reused

>[!TIP]
>
>Creating tasks from the Tasks tab is recommended when you plan to use the same task across multiple challenges. This ensures consistency and makes it easier to update task definitions centrally.

### Take actions on tasks {#tasks-actions}

From the Tasks tab, you can perform actions on tasks:

* **View task details**: Select a task name to view full configuration
* **Edit a task**: Select the more actions menu (three dots) and choose **[!UICONTROL Edit]**
* **Duplicate a task**: Select the more actions menu and choose **[!UICONTROL Duplicate]**
* **Delete a task**: Select the more actions menu and choose **[!UICONTROL Delete]** (only if not used in any active challenges)
* **View usage**: See which challenges are currently using the task

## Next steps {#next-steps}

Now that you know how to access and navigate the Loyalty Challenges inventory:

* [Create challenges](create-challenges.md) - Learn how to build your first challenge
* [Manage challenges](manage-challenges.md) - Learn how to edit and monitor challenges
