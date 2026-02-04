---
solution: Journey Optimizer
product: journey optimizer
title: Create tasks for loyalty challenges
description: Learn how to create and configure tasks for loyalty challenges in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
---

# Create tasks {#create-tasks}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](get-started.md) - Overview, workflow, prerequisites
* [Access Loyalty Challenges](access-loyalty-challenges.md) - Inventory and filtering
* [Create challenges](create-challenges.md) - Build and configure challenges
* **Create tasks** ◀︎ **You are here** - Define challenge tasks
* [Manage challenges](manage-challenges.md) - Edit, monitor, optimize

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. To request access, contact your Adobe representative. Learn more about [availability labels](../rn/releases.md#availability-labels).

## Overview {#overview}

Tasks define the specific actions or milestones that customers must complete to earn rewards in a loyalty challenge. You can configure task types, quantities, product requirements, and reward values to create engaging and personalized loyalty experiences.

Each task represents a measurable action that contributes toward challenge completion. Tasks are reusable components that can be created independently and then added to one or more challenges, or created directly within a challenge.

### How tasks work in different challenge types {#task-overview}

<!-- VISUAL: Diagram showing how task completion works differently for Standard, Streak, and Sequential challenges with examples -->

Depending on your challenge type (Standard, Streak, or Sequential), customers complete tasks differently:

* **Standard challenges**: Customers complete any specified number of tasks in any order
* **Streak challenges**: Customers complete the same task multiple times consecutively
* **Sequential challenges**: Customers complete tasks in a defined order

## Create a task {#create-task}

<!-- SCREENSHOT: Two screenshots side by side showing the two entry points: Tasks tab with "Create task" button, and challenge editor with "Add task" button -->

You can create tasks from two entry points. The configuration process is the same regardless of where you start.

+++From the Tasks inventory

1. Navigate to **[!UICONTROL Loyalty challenges]** in Journey Optimizer.

1. Select the **[!UICONTROL Tasks]** tab.

1. Select **[!UICONTROL Create task]**.

Tasks created from the inventory are saved and available for reuse across multiple challenges.

+++

+++From within a challenge

1. Open an existing challenge or create a new one.

1. Navigate to the **[!UICONTROL Tasks]** section.

1. Select **[!UICONTROL Add task]**, then choose **[!UICONTROL Create new task]**.

Tasks created this way are automatically added to your challenge and also saved to the Tasks inventory for reuse in other challenges.

+++

### Define task properties {#define-task-properties}

<!-- SCREENSHOT: Task properties form showing Task name and Task description fields -->

Configure the basic task information:

* **Task name**: Enter a descriptive name for the task. This name is visible to you and your team but may not be shown to customers depending on your content card design.
* **Task description**: (Optional) Add details about the task purpose or requirements.

### Choose customer activity {#choose-activity}

<!-- SCREENSHOT: Activity type selection showing Purchase and Spend options with radio buttons -->

Select the type of customer activity that customers must perform to complete this task:

* **[!UICONTROL Purchase]**: Customers must purchase one or more items to complete this task
* **[!UICONTROL Spend]**: Customers must spend a specified amount to complete this task

Select the customer activity that best aligns with your outcome goals. Each activity type has specific configurable attributes to further define and shape the task requirements.

### Define attributes {#define-attributes}

<!-- SCREENSHOT: Attributes form for Purchase activity showing Quantity field, Eligible items & exclusions field, and parameters icon for optional attributes -->

Configure the task attributes based on your selected activity type:

+++For Purchase activity

Configure the following attributes:

* **Quantity**: Enter the number of items that must be purchased to complete this task
* **Eligible items & exclusions**: Define items or item groups that count toward task completion and those that don't. Learn more about [defining eligible items and exclusions](#eligible-items-exclusions)

**Optional attributes** (configure via the parameters icon):

* **Minimum spend value amount**: Set a minimum purchase amount requirement
* **Maximum number of transactions**: Limit how many transactions can be used to complete the task

+++

+++For Spend activity

Configure the following attributes:

* **Amount**: Enter the total spend amount required to complete the task
* **Maximum number of transactions**: Specify how many transactions are allowed to meet the spend requirement. You can deactivate this attribute from the parameters icon if you don't want to limit the number of transactions
* **Eligible items & exclusions**: (Optional) Define items or item groups that count toward task completion and those that don't. Learn more about [defining eligible items and exclusions](#eligible-items-exclusions)

+++

After configuring all attributes, select **[!UICONTROL Create]** to save the task. The task is saved to your Tasks inventory and, if created from within a challenge, is automatically added to that challenge.

## Define eligible items and exclusions {#eligible-items-exclusions}

<!-- SCREENSHOT: Eligible items & exclusions popup showing the two sections: "Eligible task purchases are limited to the following" and "The following are excluded from this task" with text input fields -->

For both Purchase and Spend activities, you can define eligible items and groups, and also exclude items and groups. This allows you to target specific products, categories, or locations to align with your challenge goals.

**Use cases:**

* Create a task that rewards customers for purchasing coffee items but excludes clearance products
* Limit a spending task to specific product categories
* Exclude gift cards or promotional items from counting toward task completion

### Configure eligible items {#configure-eligible-items}

To define eligible items, use the **[!UICONTROL Eligible task purchases are limited to the following]** section:

* Enter specific item IDs, categories, or destination IDs, separated by commas
* Example: `SKU001, SKU002, CategoryA, StoreLocation123`
* **Tip**: Enter `*` to make all purchases eligible (default behavior if left empty)

### Configure exclusions {#configure-exclusions}

To exclude items from the task, use the **[!UICONTROL The following are excluded from this task]** section:

* Enter specific item IDs, categories, or destination IDs that should not count toward task completion
* Example: `CLEARANCE01, GIFTCARD, SALE_CATEGORY`
* Common exclusions: sale or clearance items, gift cards, promotional items

>[!NOTE]
>
>Exclusions take precedence over eligible items. If an item matches both an eligible item and an exclusion, it will be excluded from the task.

## Next steps {#next-steps}

Now that you know how to create and configure tasks:

* [Create challenges](create-challenges.md) - Learn how to build complete challenges and configure rewards
* [Manage challenges](manage-challenges.md) - Learn how to edit, monitor, and optimize challenges
