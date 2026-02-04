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
* [Manage challenges](manage-challenges.md) - Edit, monitor, optimize

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_loyalty_challenges_overview"
>title="About Loyalty Challenges"
>abstract="Loyalty Challenges enables you to create personalized engagement offers that motivate customers to complete specific actions and earn rewards."

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. Contact your Adobe representative to gain access.

## Overview {#overview}

Loyalty Challenges provides a complete solution for creating loyalty programs at scale, from defining tasks and milestones to delivering content and tracking performance across channels. You can create three types of challenge experiences, configure rewards, send multi-channel notifications at key lifecycle stages, and monitor performance through automatically generated journeys—all while maintaining integration with your external loyalty management system.

## Key capabilities {#key-capabilities}

Use Loyalty Challenges to:

* **Create three types of challenges**:
  * **Standard**: Customers complete any number of tasks in any order to earn rewards
  * **Streak**: Customers complete the same task multiple times consecutively
  * **Sequential**: Customers complete tasks in a specific order

* **Design challenge content**: Use Journey Optimizer content cards to create the visual representation of your challenge on customer devices. Content cards display the challenge information, progress, and rewards.

* **Set up task requirements**: Define what customers must do to earn rewards, including:
  * Task types (purchase, spend amount, visit, engagement, custom events)
  * Quantity requirements
  * Product inclusions/exclusions using SKUs, categories, or attributes
  * Custom attributes and conditions

* **Configure rewards**: Define rewards that customers earn either at task completion (progressive rewards) or after completing the entire challenge (final rewards).

* **Send multi-channel notifications**: Deliver messages across multiple channels (in-app, email, push) at key stages:
  * **Launch**: When the challenge starts
  * **In progress**: When customers are partway through
  * **Complete**: When customers finish the challenge

* **Track performance**: Monitor automatically generated journeys and review challenge performance through built-in reports.

## How it works {#how-it-works}

Creating and launching a loyalty challenge follows this workflow:

1. **Set up data ingestion** - Configure Experience Platform source connectors (like Capillary) to ingest loyalty event data that tracks customer actions and progress.

2. **Create a challenge** - Define the basic challenge properties including name, type (Standard, Streak, or Sequential), audience, and date range.

3. **Add tasks** - Define the specific actions customers must complete, including task types (purchase, spend, visit, etc.), quantities, product filters, and rewards.

4. **Design content cards** - Create the visual representation of your challenge using Journey Optimizer content cards that display on customer devices.

5. **Configure messaging** (Optional) - Set up multi-channel messages (in-app, email, push) for key stages: launch, in-progress, and completion.

6. **Review and publish** - Test your challenge with test profiles, then publish it to make it available to your target audience.

7. **Auto-generated journey** - When you publish, Journey Optimizer automatically creates a journey that orchestrates content card delivery and messaging.

8. **Activate journey** - The auto-generated journey activates on your challenge start date and manages all customer interactions.

9. **Monitor performance** - Track participation, completion rates, rewards distribution, and message engagement through built-in reports and the journey canvas.

>[!NOTE]
>
>The auto-generated journey appears in your journey inventory and can be customized if needed. However, changes made directly to the journey do not sync back to the challenge configuration.

## Prerequisites {#prerequisites}

Before using Loyalty Challenges, ensure you have:

### Data ingestion setup {#data-ingestion}

Loyalty Challenges relies on data ingested through Experience Platform source connectors to track customer progress and task completion.

1. **Configure a supported source connector**: Currently, the Capillary connector is generally available. Additional connectors are planned.

2. **Validate data ingestion**: Ensure that loyalty events and customer data are flowing into Experience Platform and available in Journey Optimizer.

For detailed instructions, see:

* [Experience Platform sources documentation](https://experienceleague.adobe.com/en/docs/experience-platform/sources/home)
* [Configure source connectors in Journey Optimizer](../start/get-started-sources.md)

### Required permissions {#required-permissions}

To use Loyalty Challenges, you need appropriate permissions in Journey Optimizer. Contact your administrator if you cannot access the feature.

### Target audiences {#target-audiences}

Create target audiences in Experience Platform before creating challenges. You can select existing audiences but cannot create new audiences from the Loyalty Challenges UI.

## Important limitations {#limitations}

* **No ledger system**: Loyalty Challenges does not track monetary values or point balances. When customers complete a challenge and earn a reward, Journey Optimizer calls your external loyalty management system to handle point allocation.

* **Audience selection only**: You can select existing audiences but cannot create new audiences from the Loyalty Challenges UI.

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
    <p>
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
    <p>
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
    <p>
  </td>
</tr>
</table>
