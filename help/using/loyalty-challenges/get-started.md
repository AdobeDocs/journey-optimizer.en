---
solution: Journey Optimizer
product: journey optimizer
title: Get started with Loyalty Challenges
description: Learn how to create and manage loyalty challenges in Adobe Journey Optimizer to build engaging loyalty programs.
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
* [Access and manage Loyalty Challenges](access-loyalty-challenges.md) - Inventory, challenges and tasks management
* [Create challenges](create-challenges.md) - Build and configure challenges
* [Create tasks](create-tasks.md) - Define challenge tasks

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

## How it works {#how-it-works}

Creating and launching a loyalty challenge follows this workflow:

1. **Set up data ingestion** - Configure Experience Platform source connectors (such as the [Capillary connector](https://experienceleague.adobe.com/en/docs/experience-platform/sources/home#loyalty)) to ingest loyalty event data that tracks customer actions and progress. This data powers challenge tracking and task completion.

1. **Select target audience** - Define which customers can participate in your challenge by selecting an audience from Adobe Experience Platform.

1. **Create a challenge** - Define the basic challenge properties, including name, type (Standard, Streak, or Sequential), and date range.

1. **Add tasks** - Define the specific actions customers must complete, including task types (purchase, spend, visit, engagement, custom events), quantities, product filters, and rewards.

1. **Design content cards** - Create the visual representation of your challenge using Journey Optimizer content cards that display on customer devices. Content cards show challenge information, progress, and rewards.

1. **Configure messaging** (Optional) - Set up multi-channel messages (in-app, email, push) for key lifecycle stages: launch, in-progress, and completion.

1. **Publish journey** - Journey Optimizer automatically generates a journey for your challenge. Navigate to the Journeys inventory and publish the auto-generated journey to make the challenge available to customers.

For detailed step-by-step instructions, see [Create challenges](create-challenges.md).

## Prerequisites {#prerequisites}

Before using Loyalty Challenges, ensure you have:

+++Data ingestion setup

Loyalty Challenges rely on data ingested through Experience Platform source connectors to track customer progress and task completion.

1. **Configure a supported source connector**: Currently, the Capillary connector is available. Additional connectors are planned for future releases. [Learn about loyalty source connectors](https://experienceleague.adobe.com/en/docs/experience-platform/sources/home#loyalty).

1. **Validate data ingestion**: Ensure that loyalty events and customer data are flowing into Experience Platform and available in Journey Optimizer. Verify that the data schema includes the necessary fields for tracking customer actions and progress.

For detailed instructions, see [Experience Platform sources overview](https://experienceleague.adobe.com/en/docs/experience-platform/sources/home)

+++

+++Required permissions

To use Loyalty Challenges, you need appropriate permissions in Journey Optimizer. Required permissions include:

* Access to the **[!UICONTROL Loyalty Challenges (Beta)]** feature
* Permissions to create and manage journeys
* Permissions to create and manage content cards
* Permissions to create and manage audiences

Contact your administrator if you cannot access the feature or need additional permissions.

+++

+++Target audience

Define a target audience that specifies which customers are eligible to participate in your loyalty challenges. You can select existing audiences or create new ones directly from the challenge creation interface. [Learn how to work with audiences](../audience/about-audiences.md).

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
