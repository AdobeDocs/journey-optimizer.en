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
* [Access and manage Loyalty Challenges](access-loyalty-challenges.md) - Inventory, challenges and tasks management
* [Create challenges](create-challenges.md) - Build and configure challenges
* **Create tasks** ◀︎ **You are here** - Define challenge tasks

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. To request access, contact your Adobe representative. Learn more about [availability labels](../rn/releases.md#availability-labels).

Tasks define the specific actions or milestones that customers must complete to earn rewards in a loyalty challenge. You can configure task types, quantities, and product requirements to create engaging and personalized loyalty experiences.

Each task represents a measurable action that contributes toward challenge completion. Tasks are reusable components that can be created independently and then added to one or more challenges, or created directly within a challenge.

## Create a task {#create-task}

You can create tasks from two entry points. The configuration process is the same regardless of where you start.

>[!BEGINTABS]

>[!TAB From the Tasks inventory]

Select the **[!UICONTROL Tasks]** tab and select **[!UICONTROL Create Task]**.

![](assets/task-create-inventory.png)

Tasks created from the inventory are saved and available for reuse across multiple challenges.

>[!TAB From within a challenge]

Open an existing challenge or create a new one. Select **[!UICONTROL Add task]** and click the **[!UICONTROL New]** button.

![](assets/task-create-challenge.png)

Tasks created this way are automatically added to your challenge and also saved to the Tasks inventory for reuse in other challenges.

>[!ENDTABS]

## Choose customer activity {#choose-activity}

Select the type of activity that customers must perform to complete this task:

* **[!UICONTROL Purchase]**: Customers must purchase one or more items to complete this task
* **[!UICONTROL Spend]**: Customers must spend a specified amount to complete this task

To select an activity type, click the `+` icon and select the customer activity that best aligns with your outcome goals. Each activity type has specific configurable attributes to further define and shape the task requirements.

![](assets/task-create-activitiy.png)

## Define attributes {#define-attributes}

Configure the task attributes based on your selected activity type:

>[!BEGINTABS]

>[!TAB Purchase activity]

![](assets/task-create-purchase.png)

Configure the following attributes:

* **[!UICONTROL Quantity]**: Enter the number of items that must be purchased to complete this task
* **[!UICONTROL Eligible items & exclusions]**: Define items or item groups that count toward task completion and those that don't. Learn more about [defining eligible items and exclusions](#eligible-items-exclusions)

**Optional attributes** (activated via the parameters icon):

* **[!UICONTROL Minimum spend value amount]**: Set a minimum purchase amount requirement
* **[!UICONTROL Maximum number of transactions]**: Limit how many transactions can be used to complete the task

>[!TAB Spend activity]

![](assets/task-create-spend.png)

Configure the following attributes:

* **[!UICONTROL Amount]**: Enter the total spend amount required to complete the task.
* **[!UICONTROL Maximum number of transactions]**: Specify how many transactions are allowed to meet the spend requirement. You can deactivate this attribute from the parameters icon if you don't want to limit the number of transactions.
* **[!UICONTROL Eligible items & exclusions]**: (Optional) Define items or item groups that count toward task completion and those that don't. Learn more about [defining eligible items and exclusions](#eligible-items-exclusions)

>[!ENDTABS]

## Define eligible items and exclusions {#eligible-items-exclusions}

<!-- SCREENSHOT: Eligible items & exclusions popup showing the two sections: "Eligible task purchases are limited to the following" and "The following are excluded from this task" with text input fields -->

For both **Purchase** and **Spend** activities, you can use the **[!UICONTROL Eligible items & exclusions]** attribute to define which items and groups are eligible and which are excluded. This allows you to target specific products, categories, or locations to align with your challenge goals.

Use cases include: limiting a spending task to specific product categories, or excluding gift cards or promotional items from counting toward task completion.

![](assets/tasks-create-eligible.png)

* To define eligible items, use the **[!UICONTROL Eligible task purchases are limited to the following]** section. Enter specific item IDs, categories, or destination IDs, separated by commas.

   Example: `SKU001, SKU002, CategoryA`

   Enter `*` to make all purchases eligible (default behavior if left empty).

* To exclude items from the task, use the **[!UICONTROL The following are excluded from this task]** section. Enter specific item IDs, categories, or destination IDs that should not count toward task completion.

   Example: `CLEARANCE01, GIFTCARD, SALE_CATEGORY`

   >[!NOTE]
   >
   >Exclusions take precedence over eligible items. If an item matches both an eligible item and an exclusion, it will be excluded from the task.

## Define task properties {#define-task-properties}

In the task **[!UICONTROL Properties]** pane, configure the basic task information:

* **[!UICONTROL Task name]**: Enter a descriptive name for the task. This name is visible to you and your team but may not be shown to customers depending on your content card design.
* **[!UICONTROL Task description]**: The description is automatically generated based on the activity type and attributes you configure for the task. You can disable automatic generation and enter a custom description if needed.

![](assets/tasks-create-properties.png)

After configuring all attributes and properties, select **[!UICONTROL Create]** to save the task. The task is saved to your Tasks inventory and, if created from within a challenge, is automatically added to that challenge.
