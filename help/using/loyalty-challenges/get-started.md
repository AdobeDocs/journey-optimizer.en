---
solution: Journey Optimizer
product: journey optimizer
title: Get started with Loyalty Challenges
description: Learn how to create and manage loyalty challenges in Adobe Journey Optimizer to build engaging loyalty programs.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: true
badge: label="Private beta" type="Informative"
mini-toc-levels: 1
exl-id: 1c84d9d0-cef7-4764-9f72-5428597a7203
---
# Get started with Loyalty Challenges {#get-started-loyalty-challenges}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* **Get started with Loyalty Challenges** ◀︎ **You are here**
* [Access & manage challenges and tasks](access-loyalty-challenges.md)
* [Create challenges](create-challenges.md)
* [Create tasks](create-tasks.md)
* [Loyalty Challenges API reference](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges/){target="_blank"}

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta**. For full details about the release cycle and availability phases, see [Journey Optimizer release cycle](../rn/releases.md).

## Overview {#overview}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_inventory"
>title="Loyalty challenges"
>abstract="Loyalty Challenges enable you to create engaging, gamified loyalty programs that drive customer behavior and deepen brand relationships. Build challenges that reward customers for specific actions—from making purchases and writing reviews to engaging on social media and referring friends."

Loyalty Challenges enable you to create engaging, gamified loyalty programs that drive customer behavior and deepen brand relationships. Build challenges that reward customers for specific actions—from making purchases and writing reviews to engaging on social media and referring friends.

With Loyalty Challenges, you can:

* **Design flexible challenge types**: Create Standard, Streak, or Sequential challenges to match your business goals
* **Configure rewards strategically**: Deliver points at task milestones or upon full completion to maintain engagement
* **Personalize the experience**: Use content cards and multi-channel messaging to create immersive, branded experiences
* **Integrate seamlessly**: Connect with your existing loyalty providers and leverage Experience Platform data
* **Track automatically**: Monitor customer progress through auto-generated journeys without custom development

![](assets/challenges-gs.png)

You can create three types of challenge experiences:

* **Standard challenges**: Customers complete any specified number of tasks in any order. Use this type when you want flexibility and multiple paths to completion.  
  *Example: "Summer Wellness Challenge" - Complete 3 out of 5 tasks: buy health products, share on social media, refer a friend, write a review, or attend a virtual event*

* **Streak challenges**: Customers complete the same task multiple times consecutively. Use this type to encourage consistent, repeated behavior over time.  
  *Example: "Coffee Lover's Week" - Purchase coffee products for 7 consecutive days to unlock a free drink reward*

* **Sequential challenges**: Customers complete tasks in a defined order. Use this type to guide customers through a specific journey or onboarding process.  
  *Example: "New Member Journey" - Sign up for emails → Make your first purchase → Write a product review → Refer a friend (complete in this exact order)*

## How it works {#how-it-works}

Creating and launching a loyalty challenge follows this workflow:

1. **Create a challenge** - Define the basic challenge properties, including name, type (Standard, Streak, or Sequential), and date range.

1. **Add tasks** - Define the specific actions customers must complete, including task types (purchase, spend), quantities, product filters, and rewards.

1. **Design content cards** - Create the visual representation of your challenge using Journey Optimizer content cards that display on customer devices. Content cards show challenge information, progress, and rewards.

1. **Configure messaging** (optional) - Set up multi-channel messages (in-app, email, push) for key lifecycle stages: launch, in-progress, and completion.

1. **Select target audience** - Define which customers can participate in your challenge by selecting an audience from Adobe Experience Platform.

1. **Launch the challenge** - Publish the challenge, then generate a journey. Journey Optimizer automatically creates the journey for your challenge. Publish the auto-generated journey to make the challenge available to customers.

For detailed step-by-step instructions, see [Create challenges](create-challenges.md).

## Prerequisites {#prerequisites}

Before using Loyalty Challenges, ensure you have:

+++Required permissions

To use Loyalty Challenges, you need appropriate permissions in Journey Optimizer and Adobe Experience Platform.

**Journey Optimizer:**

* `journeys.read`
* `journeys.write`
* `journeys.delete`
* `journeys.publish`
* `journeys_events.read`
* `journeys_events.write`
* `journeys_events.delete`
* `journeys_report.read`
* `messages.read`
* `messages_report.read`

**Adobe Experience Platform:**

* `segments.read`
* `profiles.read`
* `identity_namespace.read`

Contact your administrator if you cannot access the feature or need additional permissions.

+++

+++Target audience

Ensure the target audience you need exists in Adobe Experience Platform before creating your challenge. During challenge configuration, you will select the audience that defines which customers are eligible to participate. [Learn how to work with audiences](../audience/about-audiences.md).

+++

## Let's dive deeper {#lets-dive-deeper}

Now that you know what Loyalty Challenges are and how they work, it's time to dive into the details. Explore the following topics to access the interface, create your first challenge, and define the tasks your customers will complete.

<table style="table-layout:fixed">
<tr style="border: 0;">
  <td>
    <a href="access-loyalty-challenges.md">
      <img alt="Access" src="assets/do-not-localize/icon-access.png" width="200"/>
    </a>
    <div>
    <a href="access-loyalty-challenges.md"><strong>Access & manage challenges and tasks</strong></a>
    </div>
    <p>
    <em>Learn how to access the inventory and manage challenges and tasks</em>
    </p>
  </td>
  <td>
    <a href="create-challenges.md">
      <img alt="Create" src="assets/do-not-localize/icon-challenge.png" width="200"/>
    </a>
    <div>
    <a href="create-challenges.md"><strong>Create challenges</strong></a>
    </div>
    <p>
    <em>Learn how to build and configure your first loyalty challenge</em>
    </p>
  </td>
  <td>
    <a href="create-tasks.md">
      <img alt="Tasks" src="assets/do-not-localize/icon-task.png" width="200"/>
    </a>
    <div>
    <a href="create-tasks.md"><strong>Create tasks</strong></a>
    </div>
    <p>
    <em>Learn how to define tasks that customers complete for challenges</em>
    </p>
  </td>
</tr>
</table>

## API reference {#api-reference}

To manage loyalty challenges programmatically, use the [Loyalty Challenges API](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges/){target="_blank"}. The API lets you create, update, and manage challenges and tasks via REST endpoints.
