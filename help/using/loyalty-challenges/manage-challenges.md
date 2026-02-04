---
solution: Journey Optimizer
product: journey optimizer
title: Manage loyalty challenges
description: Learn how to manage, monitor, and optimize loyalty challenges in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
---

# Manage challenges {#manage-challenges}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](get-started.md) - Overview, workflow, prerequisites
* [Access Loyalty Challenges](access-loyalty-challenges.md) - Inventory and filtering
* [Create challenges](create-challenges.md) - Build and configure challenges
* [Create tasks](create-tasks.md) - Define challenge tasks
* **Manage challenges** ◀︎ **You are here** - Edit, monitor, optimize

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. To request access, contact your Adobe representative. Learn more about [availability labels](../rn/releases.md#availability-labels).

## Manage challenges {#manage-challenges-section}

### Challenge lifecycle {#challenge-lifecycle}

<!-- VISUAL: Flowchart diagram showing challenge lifecycle with status transitions: Draft → Scheduled → Live → Completed/Stopped/Archived -->

Challenges move through different statuses during their lifecycle:

* **Draft**: Challenge is being created or edited and is not yet available to customers
* **Published**: Challenge is active, the associated journey has been created.

### Edit challenges {#edit-challenges}

You can edit challenges by opening them in the Challenges inventory. The editing behavior differs depending on the challenge status:

**Draft challenges**: You have full editing capability. All properties, tasks, content, and messaging can be modified without restrictions.

**Published challenges**: When you open a published challenge for editing, you first need to revert it to Draft status.

* Any customizations made directly to the auto-generated journey will be lost
* The challenge returns to Draft state
* After making your changes, you must save and publish the challenge again
* You must reactivate the associated journey to make the updated challenge available to customers

>[!IMPORTANT]
>
>Reverting a published challenge to draft cannot be undone. Consider the impact on your active journey before proceeding.

### Duplicate challenges {#duplicate-challenges}

Duplicating a challenge creates an exact copy with all tasks, content, and messaging intact, allowing you to quickly create new versions without starting from scratch.

To duplicate a challenge:

1. Navigate to the **[!UICONTROL Challenges]** tab and locate the challenge you want to duplicate.

1. Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon next to that challenge and choose **[!UICONTROL Duplicate]**.

1. A copy of the challenge is created. Open the duplicated challenge and modify the necessary properties.

1. Save the duplicated challenge and generate the associated journey.

### Monitor performance {#monitor-performance}

<!-- SCREENSHOT: Challenge Performance tab showing key metrics dashboard with participation, completion, reward, and engagement metrics -->

Track challenge performance through key metrics:

* **Participation metrics**:
  * Enrollment: Number of customers who joined the challenge
  * Active participants: Customers currently engaged with the challenge
* **Completion metrics**:
  * Completion rates: Percentage of enrolled customers who completed the challenge
  * Average completion time: Mean time taken to complete all tasks
* **Reward metrics**:
  * Total rewards distributed: Aggregate value of all rewards given
  * Rewards by type: Breakdown of rewards by reward category
* **Engagement metrics**:
  * Content card impressions: Number of times challenge content cards were displayed
  * Message delivery: Count of messages successfully sent across all channels

To access performance data:

1. Navigate to the **[!UICONTROL Challenges]** tab in the Loyalty Challenges inventory.

1. Select the challenge you want to monitor.

1. Open the **[!UICONTROL Performance]** tab to view real-time metrics and analytics.

<!-- SCREENSHOT: Journey report showing challenge performance data with graphs and tables -->

You can also access detailed performance data in the [auto-generated journey reports](../reports/journey-global-report-cja.md), which provide additional insights and historical trends.

## Manage tasks {#manage-tasks}

Tasks are reusable components that can be used across multiple challenges. Managing tasks effectively ensures consistency across your loyalty program and makes it easier to update task definitions centrally. Tasks created in one challenge can be reused in other challenges, reducing duplication and maintaining standardization.

### Edit tasks {#edit-tasks}

You can edit existing tasks from the Tasks inventory. Consider the following:

* **Tasks not used in active challenges**: Can be edited freely - all properties can be modified without impact
* **Tasks used in live challenges**: Exercise caution, as changes affect all challenges using the task - modifications apply immediately to all referencing challenges

To edit a task:

1. Navigate to the **[!UICONTROL Tasks]** tab in the Loyalty Challenges inventory.

1. Locate the task you want to edit.

1. Select the task name to open it in edit mode.

1. Modify the task properties as needed:
   * Update task name or description
   * Change activity type or attributes
   * Adjust eligible items and exclusions
   * Modify quantity or amount requirements

1. Save your changes.

>[!WARNING]
>
>When editing a task that's actively used in live challenges, consider creating a duplicate with a new version rather than modifying the original. This prevents unintended changes to active challenges and allows you to test modifications before applying them.

### Delete tasks {#delete-tasks}

Tasks can only be deleted if they are not currently used in any challenges. Before deleting a task:

* Check the **[!UICONTROL Used in challenges]** count in the Tasks inventory
* Ensure no draft, scheduled, or live challenges reference the task

To delete a task:

1. Navigate to the **[!UICONTROL Tasks]** tab in the Loyalty Challenges inventory.

1. Locate the task you want to delete.

1. Verify the **[!UICONTROL Used in challenges]** count shows 0. If the count is greater than 0, you must first remove the task from all challenges before deletion.

1. Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon next to the task.

1. Choose **[!UICONTROL Delete]**.

1. Confirm the deletion in the dialog box.

>[!NOTE]
>
>If a task is used in any challenge (draft, scheduled, or live), you must first remove it from all challenges before you can delete it. Consider archiving or duplicating tasks instead of deleting them if you may need them in the future.
