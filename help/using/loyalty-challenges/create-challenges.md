---
solution: Journey Optimizer
product: journey optimizer
title: Create loyalty challenges
description: Learn how to create and configure loyalty challenges in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
---

# Create challenges {#create-challenges}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](get-started.md) - Overview, workflow, prerequisites
* [Access and manage Loyalty Challenges](access-loyalty-challenges.md) - Inventory, challenges and tasks management
* **Create challenges** ◀︎ **You are here** - Build and configure challenges
* [Create tasks](create-tasks.md) - Define challenge tasks

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. To request access, contact your Adobe representative. Learn more about [availability labels](../rn/releases.md#availability-labels).

## Create the challenge {#create-the-challenge}

1. Navigate to **[!UICONTROL Loyalty Challenges (Beta)]** in Journey Optimizer.

1. Select the **[!UICONTROL Challenges]** tab and select **[!UICONTROL Create Challenge]**.

   ![](assets/challenge-create.png)

1. Choose the challenge type:

   * **[!UICONTROL Standard]**: Customers complete any specified number of tasks in any order  
     *Example: Complete 3 out of 5 available tasks*

   * **[!UICONTROL Streak]**: Customers complete the same task multiple times consecutively  
     *Example: Make a purchase on 7 consecutive days*

   * **[!UICONTROL Sequential]**: Customers complete tasks in a defined order  
     *Example: Purchase → Review → Share (must be completed in this sequence)*

## Configure the challenge structure {#structure}

In the **[!UICONTROL Structure]** tab, define how your challenge is organized: its properties, schedule, tasks to complete, and rewards to deliver.

### Define the challenge properties and use custom metadata {#properties}

1. In the **[!UICONTROL Challenge properties]** pane, define global settings for the challenge:

   * **[!UICONTROL Name]**: Enter a descriptive name for your challenge. This name appears in the challenges inventory.
   * **[!UICONTROL Description]**: Enter a description that explains the challenge's purpose and goals.

   ![](assets/challenge-create-properties.png)

1. Use the **[!UICONTROL Custom metadata]** section to add custom metadata using key/value pairs. This metadata can be used for tracking or integration with external systems.

### Schedule the challenge {#schedule}

Configure when your challenge runs by selecting the **[!UICONTROL Open schedule]** icon:

![](assets/challenge-create-schedule.png)

* **[!UICONTROL Start date and time]**: Set when the challenge becomes available to customers.
* **[!UICONTROL End date and time]**: Set when the challenge expires and no longer accepts new completions.
* **[!UICONTROL Time zone]**: The challenge uses the recipient's local time zone by default.
* **[!UICONTROL Tasks must be completed]**: Choose when customers can complete tasks:

   * **[!UICONTROL Any time during challenge]**: Customers can complete tasks at any time between the challenge start and end dates.
   * **[!UICONTROL During specific hours of the day]**: Restrict task completion to specific daily hours by setting the **[!UICONTROL Start Time]** and **[!UICONTROL End Time]**.

The challenge schedule is now configured. Next, add the tasks that customers need to complete.

### Add tasks {#add-tasks}

Tasks define the specific actions customers must complete to earn rewards. You can configure task types (purchase, spend), quantities, product filters, and other attributes.

To add tasks to your challenge, follow these steps:

1. In the **[!UICONTROL Tasks]** section, select **[!UICONTROL Add task]**.

   ![](assets/challenge-create-add-task.png)

1. The **[!UICONTROL Tasks Inventory]** opens. Select one or more tasks from the list and select **[!UICONTROL Add]**. To create a new task, select **[!UICONTROL New]**. [Learn how to create and configure tasks](create-tasks.md).

1. Specify when the challenge is considered completed. Available settings depend on the challenge type:

   +++Standard challenges

   **[!UICONTROL Task completion requirement]** - Choose between:

      * **[!UICONTROL Customer chooses 1 task to complete]**: Customers can select and complete any single task to earn rewards
      * **[!UICONTROL Customer completes specific number of tasks]**: Customers must complete a defined number of tasks. Specify the required number - *Example: Complete 3 out of 5 tasks*

   +++

   +++Streak challenges

   * **[!UICONTROL Streak type]**:

      * **Consecutive**: Customers must complete the task on consecutive days without breaks - *Example: Purchase on Monday, Tuesday, Wednesday - missing a day breaks the streak*

      * **Non-consecutive**: Customers can complete the task with gaps between completions - *Example: Complete 7 purchases over 30 days, with breaks allowed*

   * **[!UICONTROL Streak length]**: Specify how many times the task must be completed - *Example: Set to 7 for a "7-day purchase streak"*

   +++

   +++Sequential challenges

   **[!UICONTROL Task completion requirement]** - Choose between:

      * **[!UICONTROL Customer chooses 1 task to complete]**: Customers can select and complete any single task to earn rewards
      * **[!UICONTROL Customer completes specific number of tasks]**: Customers must complete a defined number of tasks in the exact order you define. Missing or skipping a task breaks the sequence. Specify the required number (e.g., complete 3 out of 5 tasks)

      *Example: Task 1 (Purchase) → Task 2 (Review) → Task 3 (Share) - must be completed in this order*

   +++

1. By default, standard and sequential challenges allow customers to complete tasks across multiple transactions. To require all tasks to be completed in a single transaction, select the ![](assets/do-not-localize/settings-icon.svg) **[!UICONTROL Settings]** icon and toggle on the option below.

   ![](assets/challenge-create-single-transaction.png)

After adding tasks to your challenge, configure the rewards customers will earn for completing them.

### Configure rewards {#rewards}

Rewards are the loyalty points or benefits customers receive for completing challenges. Configure when and how rewards are delivered.

1. In the **[!UICONTROL Reward delivery]** dropdown, choose when to deliver rewards:

   * **[!UICONTROL Deliver rewards when challenge is completed]**: Award rewards when customers complete the entire challenge  
     *Example: Award 100 points after completing all 5 tasks*

   * **[!UICONTROL Deliver rewards at task completion milestones as challenge progress is made]**: Award rewards incrementally as customers complete individual tasks (only available for challenges requiring more than one task)  
     *Example: Award 10 points after task 1, 20 points after task 2, and 50 points after task 3*

1. Select your reward provider. This is your loyalty solution that manages customer points and rewards.

1. Configure the reward amounts based on your selected delivery method:

   +++Deliver rewards when challenge is completed

   Specify the total reward amount to give when customers complete the entire challenge.

   ![](assets/challenge-create-reward-total.png)

   **Example**: Customers are awarded 100 points when completing the challenge.

   +++

   +++Deliver rewards at task completion milestones

   Specify reward amounts for task completion milestones. This option allows you to create progressive rewards that increase customer motivation as they progress through the challenge.

   For any task where you want to deliver a reward, toggle on the reward option and specify how many points to award when customers complete that specific task. You can choose to reward only certain task completions—for example, if you have 10 tasks, you might reward only tasks 1, 5, and 10.

   ![](assets/challenge-create-reward-milestones.png)

   **Example**: Customers are awarded 10 points when completing the first task, then 50 additional points after completing the second task, for a total of 60 points when the challenge is completed.

   >[!TIP]
   >
   >Consider increasing reward values for later tasks to maintain customer engagement throughout the challenge.

   +++

After configuring the challenge structure with tasks and rewards, design the content cards to display the challenge to customers.

## Configure content cards {#configure-content-cards}

Content cards visually represent your challenge on customer devices, displaying challenge information, progress, and rewards. [Learn more about content cards](../content-card/create-content-card.md).

To configure content cards for your challenge:

1. Navigate to the **[!UICONTROL Content]** tab and enter a **[!UICONTROL Name]** for the content card.

1. Select the **[!UICONTROL Channel configuration]**. Channel configurations contain all the technical parameters for sending messages, such as header parameters, subdomain, mobile apps, etc. [Learn more about channel configurations](../configuration/channel-surfaces.md).

1. Select **[!UICONTROL Edit content]** to design your content card. [Learn how to design and personalize content cards](../content-card/design-content-card.md).

   ![](assets/challenge-create-content.png)

After configuring the content card, set up messaging to engage customers throughout the challenge lifecycle.

### Configure messaging {#configure-messaging}

Set up multi-channel messages to engage customers at key stages of the challenge lifecycle. Messaging is optional but recommended to maximize customer engagement.

1. Navigate to the **[!UICONTROL Messaging]** tab and configure messages for each lifecycle stage:

   * **Launch** message: Notify customers when the challenge starts
   * **In-progress** message: Keep customers engaged with reminders and progress updates
   * **Completion** message: Celebrate success and confirm reward allocation

1. For each stage, select **[!UICONTROL Add [stage] message]** (where [stage] represents Launch, In-progress, or Completion) to create a message for that stage.

1. Choose your desired channel: **[!UICONTROL In-app]**, **[!UICONTROL Email]**, or **[!UICONTROL Push notification]** and select the associated channel configuration.

1. Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Edit]** to design your message content.

   ![](assets/challenge-create-messaging.png)

Learn how to create messages for specific channels:

* [In-app messages](../in-app/get-started-in-app.md)
* [Email messages](../email/get-started-email.md)
* [Push notifications](../push/get-started-push.md)

After completing the messaging configuration, define which customers are eligible to participate in the challenge.

## Select the challenge audience {#audience}

Define which customers can participate in your loyalty challenge.

1. Navigate to the **[!UICONTROL Audience]** tab and select the **[!UICONTROL Select audience]** button.

   ![](assets/challenge-create-audience.png)

1. Select your target audience from the list of available Adobe Experience Platform audiences. [Learn how to work with audiences](../audience/about-audiences.md).

1. Select **[!UICONTROL Add audience]**.

Your challenge is now fully configured with its structure, content, messaging, and target audience. The final step is to generate and publish the journey.

## Generate and publish the journey {#review-and-publish}

Generate the journey that will orchestrate your challenge delivery and customer interactions. To do so, select **[!UICONTROL Generate Journey]**.

![](assets/challenge-create-generate-journey.png)

Journey Optimizer automatically creates a [journey](../building-journeys/journey-gs.md) in Draft status. The auto-generated journey appears in your journey inventory with the name format "Challenge: [Challenge Name]".

![](assets/challenge-create-journey.png)

Review the journey configuration if needed, then publish the journey to make the challenge available to customers. [Learn how to publish a journey](../building-journeys/publish-journey.md).

The journey will start automatically on your specified challenge start date and deliver content and messages according to your configuration.

>[!NOTE]
>
>The auto-generated journey can be customized to add additional logic or messaging. However, changes made directly to the journey do not sync back to the challenge configuration. If you edit the challenge later, any journey customizations will be lost when the journey is regenerated.
