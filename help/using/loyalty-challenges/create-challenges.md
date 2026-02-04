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
* [Access Loyalty Challenges](access-loyalty-challenges.md) - Inventory and filtering
* **Create challenges** ◀︎ **You are here** - Build and configure challenges
* [Create tasks](create-tasks.md) - Define challenge tasks
* [Manage challenges](manage-challenges.md) - Edit, monitor, optimize

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. To request access, contact your Adobe representative. Learn more about [availability labels](../rn/releases.md#availability-labels).

## How it works {#how-it-works}

Creating and launching a loyalty challenge follows this workflow:

1. **[Create the challenge](#create-the-challenge)** - Choose the challenge type (Standard, Streak, or Sequential) that best fits your loyalty program goals.

1. **[Configure the challenge structure](#structure)** - Define the challenge properties, schedule, tasks that customers must complete, and rewards they will earn.

1. **[Configure content cards](#configure-content-cards)** - Design content cards to visually represent your challenge on customer devices, displaying challenge information, progress, and rewards.

1. **[Configure messaging](#configure-messaging)** (Optional) - Set up multi-channel messages (in-app, email, push) for key stages: launch, in-progress, and completion.

1. **[Select the challenge audience](#audience)** - Define which customers are eligible to participate in the challenge.

1. **[Generate and activate the journey](#review-and-publish)** - Generate the associated journey and activate it to make the challenge available to your target audience.

## Create the challenge {#create-the-challenge} 

1. Navigate to **[!UICONTROL Loyalty Challenges (Beta)]** in Journey Optimizer.

1. Select the **[!UICONTROL Challenges]** tab and select **[!UICONTROL Create challenge]**.

   ![](assets/challenge-create.png)

1. Choose the challenge type:

   * **[!UICONTROL Standard]**: Customers complete any specified number of tasks in any order
   * **[!UICONTROL Streak]**: Customers complete the same task multiple times consecutively
   * **[!UICONTROL Sequential]**: Customers complete tasks in a defined order

## Configure the challenge structure {#structure}

The Structure tab is where you define how your challenge is organized: its properties, schedule, the tasks to complete and rewards to give.

### Define the challenge properties and use custom metadata {#properties}

1. In the Challenge properties pane, configure the challenge properties:

   ![](assets/challenge-create-properties.png)

   **Name**: Enter a descriptive name for your challenge. This name appears in the challenges inventory and helps you identify the challenge.

   **Description**: Enter a description for your challenge.

1. Use the **[!UICONTROL Custom metadata]** section to add custom metadata using key/value pairs. This metadata can be used for tracking, segmentation, or integration with external systems.

### Schedule the challenge {#schedule}

Schedule the challenge by selecting the ![](assets/do-not-localize/schedule-icon.svg) **[!UICONTROL Open schedule]** icon.

* **Start date and time**: Set when the challenge becomes available to customers (format: mm/dd/yyyy, ––:–– AM/PM).

* **End date and time**: Set when the challenge expires and no longer accepts new completions (format: mm/dd/yyyy, ––:–– AM/PM).

* **Time zone**: The challenge uses the recipient's local timezone by default.

* **Tasks must be completed**: Choose when customers can complete tasks:

   * **[!UICONTROL Any time during challenge]**: Customers can complete tasks at any time between the challenge start and end dates
   * **[!UICONTROL During specific hours of the day]**: Restrict task completion to specific daily hours by setting the **[!UICONTROL Start Time]** and **[!UICONTROL End Time]**

The challenge schedule is now configured. You can now add the tasks that customers need to complete.

### Add tasks {#add-tasks}

Tasks define the specific actions or milestones that customers must complete to earn rewards. You configure task types (purchase, spend, visit, engagement, custom events), quantities, product filters, and rewards.

Depending on your challenge type, customers complete tasks differently:

* **Standard challenges**: Complete any specified number of tasks in any order
* **Streak challenges**: Complete the same task multiple times consecutively
* **Sequential challenges**: Complete tasks in a defined order

To add tasks to your challenge, follow these steps:

1. In the **[!UICONTROL Tasks]** section, select **[!UICONTROL Add task]**.

   ![](assets/challenge-create-add-task.png)

1. The Tasks inventory opens. Select one or more tasks from the list and select **[!UICONTROL Add]**. To create a new task, select **[!UICONTROL New]**.

   For detailed instructions on creating and configuring tasks, see [Create tasks](create-tasks.md).

1. In the **[!UICONTROL Task completion requirement]** section, specify when the challenge should be considered completed:

   * **[!UICONTROL Customer chooses 1 task to complete]**: The customer can select and complete any single task from the challenge to earn rewards
   * **[!UICONTROL Customer completes specific number of tasks]**: The customer must complete a defined number of tasks. Enter the required number of task completions.

1. By default, challenges allow customers to complete tasks across multiple transactions. To require all tasks to be completed in a single transaction, select the ![](assets/do-not-localize/settings-icon.svg) **[!UICONTROL Settings]** icon and toggle on the **[!UICONTROL Single transaction]** option.

   ![](assets/challenge-create-single-transaction.png)

### Configure rewards {#rewards}

Rewards are the loyalty points or benefits customers receive for completing challenges. Configure how and when rewards are delivered to motivate customer participation.

1. In the **[!UICONTROL Reward delivery]** dropdown, choose when rewards should be delivered:

   * **[!UICONTROL Deliver rewards when challenge is completed]**: Award all rewards when the customer completes the entire challenge
   * **[!UICONTROL Deliver rewards at task completion milestones as challenge progress is made]**: Award rewards incrementally as customers complete individual tasks (only available when the challenge requires completing more than one task)

1. Select your reward provider from the dropdown. This is your loyalty solution that manages customer points and rewards.

1. Configure the reward amounts based on your selected delivery method:

   +++Deliver rewards when challenge is completed

   In the **Number of [loyalty points] on challenge completion** field, specify the total reward amount to give when the customer completes the entire challenge.

   The field name displays your loyalty points name as defined in the selected provider. For example, if your provider uses "Luma points", the field displays "Number of Luma points on challenge completion".

   ![](assets/challenge-create-reward-total.png)

   **Example**: In the screenshot above, customers are awarded 100 points when completing the challenge.

   +++

   +++Deliver rewards at task completion milestones

   Specify reward amounts for task completion milestones. This option allows you to create progressive rewards that increase customer motivation as they progress through the challenge.

   For any task where you want to deliver a reward, toggle on the reward option and specify how many points to award when customers complete that specific task. You can choose to reward only certain task completions—for example, if you have 10 tasks, you might reward only tasks 1, 5, and 10.

   ![](assets/challenge-create-reward-milestones.png)

   **Example**: In the screenshot above, customers are awarded 10 points when completing the first task, and then 50 additional points after completing the second task, for a total of 60 points when the challenge is completed.

   >[!TIP]
   >
   >Consider increasing reward values for later tasks to maintain customer engagement throughout the challenge.

   +++

The challenge structure is now configured with tasks and rewards. You can now design the content cards to display the challenge to customers.

## Configure content cards {#configure-content-cards}

Content cards provide the visual representation of your challenge on customer devices, displaying challenge information, progress, and rewards. Learn more about [content cards](../content-card/create-content-card.md).

To configure content cards for your challenge:

1. In the challenge editor, navigate to the **[!UICONTROL Content]** tab.

1. Enter a **[!UICONTROL Name]** for the content card.

1. Select the associated **[!UICONTROL Channel configuration]**. Channel configurations define how and where your content is delivered to customers. For more information, see [Channel configurations](../configuration/channel-surfaces.md).

1. Select **[!UICONTROL Edit content]** to design your content card.

   ![](assets/challenge-create-content.png)

For more information on designing and personalizing content cards, see [Design content cards](../content-card/design-content-card.md).

The content card is now configured. You can now set up messaging to engage customers throughout the challenge lifecycle.

### Configure messaging {#configure-messaging}

Set up multi-channel messages to engage customers at key stages of the challenge lifecycle.

1. Navigate to the **[!UICONTROL Messaging]** tab.

1. Configure messages for each lifecycle stage:

   ![](assets/challenge-create-messaging.png)

   * **Launch messages**: Notify customers when the challenge starts and provide initial details
   * **In-progress messages**: Keep customers engaged during the challenge with reminders, progress updates, and encouragement to continue
   * **Completion messages**: Celebrate success, confirm reward allocation, and suggest next challenges or actions

1. For each stage, select **[!UICONTROL Add *stage* message]** to create a message for that stage.

1. Choose your desired channel: **[!UICONTROL In-app]**, **[!UICONTROL Email]**, or **[!UICONTROL Push notification]** and select the associated channel configuration.

1. Select the ![](assets/do-not-localize/Smock_More_18_N.svg) icon and choose **[!UICONTROL Edit]** to design your message content.

   For more information on creating messages for specific channels, refer to:

   * [In-app messages documentation](../in-app/get-started-in-app.md)
   * [Email messages documentation](../email/get-started-email.md)
   * [Push notifications documentation](../push/get-started-push.md)

1. Repeat these steps for each stage and channel as needed.

The messaging configuration is now complete. You can now define which customers are eligible to participate in the challenge.

## Select the challenge audience {#audience}

Define which customers are eligible to participate in your loyalty challenge.

1. Navigate to the **[!UICONTROL Audience]** tab and click the **[!UICONTROL Select audience]** button.

   ![](assets/challenge-create-audience.png)

1. All available Adobe Experience Platform audiences are displayed. Select the desired audience from the list.

1. Select **[!UICONTROL Add audience]** to confirm your selection.

Your challenge configuration is now complete. You can now generate the journey that will orchestrate the challenge delivery.

## Generate and activate the journey {#review-and-publish}

When your challenge configuration is complete, generate the associated journey that will orchestrate the challenge delivery and customer interactions. To do so, select **[!UICONTROL Generate Journey]**.

   ![](assets/challenge-create-generate-journey.png)

Journey Optimizer automatically creates a [journey](../building-journeys/journey-gs.md) in Draft status. The auto-generated journey appears in your journey inventory with the name format "Challenge: [Challenge Name]".

Review the journey configuration if needed, then [activate the journey](../building-journeys/publish-journey.md) to make the challenge available to customers.

The journey will start automatically on your specified challenge start date and deliver content and messages according to your configuration.

>[!NOTE]
>
>The auto-generated journey can be customized if needed to add additional logic or messaging. However, changes made directly to the journey do not sync back to the challenge configuration. If you edit the challenge later, any journey customizations will be lost when the journey is regenerated.

## Next steps {#next-steps}

* [Manage challenges](manage-challenges.md) - Learn how to edit, monitor, and optimize challenges
* [Understand Loyalty Challenges](get-started.md) - Review features and capabilities
