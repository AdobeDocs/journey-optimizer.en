---
solution: Journey Optimizer
product: journey optimizer
title: Get started with Loyalty Challenges
description: Learn how to create and manage loyalty challenges in Adobe Journey Optimizer to create engaging loyalty programs.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
---

# Get started with Loyalty Challenges {#get-started-loyalty-challenges}

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* **Get started with Loyalty Challenges** ◀︎ **You are here** - Overview, workflow, prerequisites
* [Access Loyalty Challenges](access-loyalty-challenges.md) - Inventory and filtering
* [Create challenges](create-challenges.md) - Build and configure challenges
* [Create tasks](create-tasks.md) - Define challenge tasks
* [Manage challenges](manage-challenges.md) - Edit, monitor, optimize

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. To request access, contact your Adobe representative. Learn more about [availability labels](../rn/releases.md#availability-labels).

## Overview {#overview}

Loyalty Challenges provide a complete solution for creating loyalty programs at scale, from defining tasks and milestones to delivering content and tracking performance across channels.

You can create three types of challenge experiences:

* **Standard challenges**: Customers complete any specified number of tasks in any order
* **Streak challenges**: Customers complete the same task multiple times consecutively
* **Sequential challenges**: Customers complete tasks in a defined order

With Loyalty Challenges, you can configure rewards, send multi-channel notifications at key lifecycle stages, and monitor performance through automatically generated journeys—all while maintaining integration with your external loyalty management system.

<!-- SCREENSHOT: High-level diagram showing Loyalty Challenges architecture with: Data ingestion from source connectors -> Challenge creation in JO -> Content cards & messaging -> Customer device -> Journey tracking -->

## How it works {#how-it-works}

<!-- SCHEMA: Visual workflow diagram showing the 8 steps in the loyalty challenge creation process with icons for each step -->

Creating and launching a loyalty challenge follows this workflow:

1. **Set up data ingestion** - Configure Experience Platform source connectors (such as the Capillary connector) to ingest loyalty event data that tracks customer actions and progress. This data powers challenge tracking and task completion.

1. **Create a challenge** - Define the basic challenge properties including name, type (Standard, Streak, or Sequential), audience, and date range. See [Create challenges](create-challenges.md) for detailed steps.

1. **Add tasks** - Define the specific actions customers must complete, including task types (purchase, spend, visit, engagement, custom events), quantities, product filters, and rewards. See [Create tasks](create-tasks.md) for detailed instructions.

1. **Design content cards** - Create the visual representation of your challenge using Journey Optimizer [content cards](../content-card/get-started-content-card.md) that display on customer devices. Content cards show challenge information, progress, and rewards.

1. **Configure messaging** (Optional) - Set up multi-channel messages ([in-app](../in-app/get-started-in-app.md), [email](../email/get-started-email.md), [push](../push/get-started-push.md)) for key lifecycle stages: launch, in-progress, and completion.

1. **Review and publish** - Test your challenge with [test profiles](../test-approve/test-profiles.md), then publish it to make it available to your target audience.

1. **Activate journey** - When you publish a challenge, Journey Optimizer automatically creates a [journey](../building-journeys/journey-gs.md) in Draft status that orchestrates content card delivery and messaging. Navigate to the Journeys inventory, locate the auto-generated journey (named "Challenge: [Challenge Name]"), and [activate it](../building-journeys/publishing-the-journey.md) to make the challenge available to your customers.

1. **Monitor performance** - Track participation, completion rates, rewards distribution, and message engagement through built-in reports and the journey canvas. See [Manage challenges](manage-challenges.md) for monitoring details.

## Prerequisites {#prerequisites}

Before using Loyalty Challenges, ensure you have:

+++Data ingestion setup

Loyalty Challenges rely on data ingested through Experience Platform source connectors to track customer progress and task completion.

1. **Configure a supported source connector**: Currently, the Capillary connector is generally available. Additional connectors are planned for future releases.

1. **Validate data ingestion**: Ensure that loyalty events and customer data are flowing into Experience Platform and available in Journey Optimizer. Verify that the data schema includes the necessary fields for tracking customer actions and progress.

For detailed instructions, see:

* [Experience Platform sources documentation](https://experienceleague.adobe.com/en/docs/experience-platform/sources/home)
* [Configure source connectors in Journey Optimizer](../start/get-started-sources.md)

+++

+++Required permissions

To use Loyalty Challenges, you need appropriate permissions in Journey Optimizer. Required permissions include:

* Access to the **[!UICONTROL Loyalty challenges]** feature
* Permissions to create and manage journeys
* Permissions to create and manage content cards
* Permissions to create and manage audiences

Contact your administrator if you cannot access the feature or need additional permissions.

+++

+++Target audiences

Create target audiences in Experience Platform before creating challenges. These audiences define which customers are eligible to participate in your loyalty challenges. For more information on how to create audiences, refer to [Get started with audiences](../audience/about-audiences.md).

+++

## Next steps {#next-steps}

<table style="table-layout:fixed">
<tr style="border: 0;">
  <td>
    <a href="access-loyalty-challenges.md">
    <!--<img alt="Access" src="../assets/do-not-localize/learn-more-button.svg">-->
    </a>
    <div>
    <a href="access-loyalty-challenges.md"><strong>Access Loyalty Challenges</strong></a>
    </div>
    <p>
    <em>Learn how to access the inventory and filter challenges</em>
    </p>
  </td>
  <td>
    <a href="create-challenges.md">
      <!--<img alt="Create" src="../assets/do-not-localize/start-button.svg">-->
    </a>
    <div>
    <a href="create-challenges.md"><strong>Create challenges</strong></a>
    </div>
    <p>
    <em>Build and configure your first loyalty challenge</em>
    </p>
  </td>
  <td>
    <a href="create-tasks.md">
    <!--<img alt="Tasks" src="../assets/do-not-localize/start-button.svg">-->
    </a>
    <div>
    <a href="create-tasks.md"><strong>Create tasks</strong></a>
    </div>
    <p>
    <em>Define actions and rewards for challenges</em>
    </p>
  </td>
  <td>
    <a href="manage-challenges.md">
    <!--<img alt="Manage" src="../assets/do-not-localize/monitor-button.svg">-->
    </a>
    <div>
    <a href="manage-challenges.md"><strong>Manage challenges</strong></a>
    </div>
    <p>
    <em>Edit, monitor, and optimize challenges</em>
    </p>
  </td>
</tr>
</table>
