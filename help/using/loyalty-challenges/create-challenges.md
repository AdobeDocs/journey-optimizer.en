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

<!-- SCHEMA: Visual workflow showing the 5 main steps with icons: Create challenge → Add tasks → Design content cards → Configure messaging → Review and publish -->

Creating and launching a loyalty challenge follows this workflow:

1. **Create a challenge** - Define the basic challenge properties including name, type (Standard, Streak, or Sequential), audience, and date range.

1. **Add tasks** - Define the specific actions customers must complete, including task types (purchase, spend, visit, etc.), quantities, product filters, and rewards.

1. **Design content cards** - Create the visual representation of your challenge using Journey Optimizer content cards that display on customer devices.

1. **Configure messaging** (Optional) - Set up multi-channel messages (in-app, email, push, SMS) for key stages: launch, in-progress, and completion.

1. **Review and publish** - Test your challenge with test profiles, then publish it to make it available to your target audience.

## Create the challenge {#create-challenge}

<!-- SCREENSHOT: Challenge creation screen showing challenge properties form with fields for name, type, audience, dates -->

To create a new loyalty challenge:

1. Navigate to **[!UICONTROL Loyalty challenges]** in Journey Optimizer.

1. Select the **[!UICONTROL Challenges]** tab.

1. Select **[!UICONTROL Create challenge]**.

1. Configure the challenge properties:

   **Challenge name**: Enter a descriptive name for your challenge. This name appears in the challenges inventory and helps you identify the challenge.

   **Challenge type**: Select one of the following types:
   * **[!UICONTROL Standard]**: Customers complete any specified number of tasks in any order
   * **[!UICONTROL Streak]**: Customers complete the same task multiple times consecutively
   * **[!UICONTROL Sequential]**: Customers complete tasks in a defined order

   **Target audience**: Select the audience segment that defines who can participate in this challenge. You must create audiences in Experience Platform before creating challenges. For more information, see [Get started with audiences](../audience/about-audiences.md).

   **Start date**: Set when the challenge becomes available to customers.

   **End date**: Set when the challenge expires and no longer accepts new completions.

<!-- VISUAL: Comparison table or diagram showing the three challenge types (Standard, Streak, Sequential) with examples of each -->

### Add tasks {#add-tasks}

Tasks define the specific actions or milestones that customers must complete to earn rewards. You configure task types (purchase, spend, visit, engagement, custom events), quantities, product filters, and rewards.

Depending on your challenge type, customers complete tasks differently:

* **Standard challenges**: Complete any specified number of tasks in any order
* **Streak challenges**: Complete the same task multiple times consecutively
* **Sequential challenges**: Complete tasks in a defined order

To add tasks to your challenge, select **[!UICONTROL Add task]** in the Tasks section and configure the task properties.

For detailed instructions on creating and configuring tasks, see [Create tasks](create-tasks.md).

### Configure content cards {#configure-content-cards}

<!-- SCREENSHOT: Content cards configuration section in the challenge editor -->

Content cards provide the visual representation of your challenge on customer devices, displaying challenge information, progress, and rewards. Learn more about [content cards](../content-card/create-content-card.md).

<!-- VISUAL: Example content card designs showing different states: challenge start, in-progress with progress bar, completion with reward -->

To configure content cards for your challenge:

1. In the challenge editor, navigate to the **[!UICONTROL Content cards]** section.

1. Select **[!UICONTROL Create content card]** or choose an existing template.

1. Design your content card:
   * Add images, text, and branding elements
   * Include [personalization tokens](../personalization/personalization-syntax.md) to display customer-specific information
   * Show challenge progress indicators
   * Display rewards and incentives

1. Configure when the content card displays:
   * **Challenge start**: Show when the challenge becomes available
   * **In progress**: Display while customers are actively participating
   * **Completion**: Show after customers complete all tasks

1. Preview the content card on different devices to ensure proper display.

1. Save the content card configuration.

For more information on designing and personalizing content cards, see [Design content cards](../content-card/design-content-card.md).

### Configure messaging {#configure-messaging}

<!-- SCREENSHOT: Messaging configuration section showing the three lifecycle stages: Launch, In-progress, Completion -->

Set up multi-channel messages to engage customers at key stages of the challenge lifecycle.

<!-- VISUAL: Timeline diagram showing when each message type is sent during the challenge lifecycle -->

To configure messaging for your challenge:

1. In the challenge editor, navigate to the **[!UICONTROL Messaging]** section.

1. Configure messages for each lifecycle stage:

   **Launch messages** - Notify customers when the challenge starts:
   * Select channels: [In-app](../in-app/get-started-in-app.md), [email](../email/get-started-email.md), [push notification](../push/get-started-push.md), or [SMS](../sms/get-started-sms.md)
   * Design the message with challenge details and call-to-action
   * Set timing: Send immediately when challenge goes live or schedule for a specific time

   **In-progress messages** - Keep customers engaged during the challenge:
   * Define trigger conditions (for example, 50% completion, specific task completed)
   * Create reminder messages to encourage continued participation
   * Include progress updates and next steps

   **Completion messages** - Celebrate success and deliver rewards:
   * Congratulate customers on completing the challenge
   * Confirm reward allocation
   * Provide instructions for claiming rewards
   * Suggest next challenges or actions

For more information on creating messages for specific channels, refer to:

* [In-app messages documentation](../in-app/get-started-in-app.md)
* [Email messages documentation](../email/get-started-email.md)
* [Push notifications documentation](../push/get-started-push.md)
* [SMS messages documentation](../sms/get-started-sms.md)

## Review and publish the challenge {#review-and-publish}

<!-- SCREENSHOT: Review screen showing summary of challenge configuration with all components listed -->

Before publishing your challenge:

1. **Review all components**: Verify challenge properties, tasks, rewards, content cards, and messaging configurations.

1. **Test the experience**: Use [test profiles](../content-management/test-profiles.md) to validate content card display and task trigger behavior.

1. **Publish**: Select **[!UICONTROL Publish]** to make the challenge available for your target audience.

<!-- SCREENSHOT: Journeys inventory showing the auto-generated journey in Draft status with name format "Challenge: [Challenge Name]" -->

When you publish a challenge, Journey Optimizer automatically creates a [journey](../building-journeys/journey-gs.md) in Draft status. The auto-generated journey appears in your journey inventory with the name format "Challenge: [Challenge Name]".

To make the challenge available to customers:

1. Navigate to the **[!UICONTROL Journeys]** inventory in Journey Optimizer.

1. Locate the auto-generated journey (it will have "Challenge:" as a prefix in its name).

1. [Activate the journey](../building-journeys/publish-journey.md).

The journey starts automatically on your specified challenge start date.

>[!NOTE]
>
>The auto-generated journey appears in your journey inventory and can be customized if needed. However, changes made directly to the journey do not sync back to the challenge configuration.

## Next steps {#next-steps}

* [Manage challenges](manage-challenges.md) - Learn how to edit, monitor, and optimize challenges
* [Understand Loyalty Challenges](get-started.md) - Review features and capabilities
  