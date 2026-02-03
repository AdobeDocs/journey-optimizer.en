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

>[!AVAILABILITY]
>
>This feature is currently in **private beta** and may not be available in your environment. Contact your Adobe representative to gain access.

Loyalty Challenges enables you to create personalized engagement offers for your customers, helping you orchestrate loyalty programs at scale. You can design challenges with specific tasks and milestones, reward customers for completing them, and deliver the experience through Adobe Journey Optimizer channels.

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* **Get started with Loyalty Challenges** ◀︎ **You are here** - Quick overview and next steps
* [Understand Loyalty Challenges](get-started.md) - Features, workflow, prerequisites
* [Create challenges](create-challenges.md) - Build and configure challenges
* [Manage challenges](manage-challenges.md) - Edit, monitor, optimize

>[!ENDSHADEBOX]

## Quick overview {#quick-overview}

Use Loyalty Challenges to:

* **Create three types of challenges**: Standard (any tasks), Streak (repeated tasks), or Sequential (ordered tasks)
* **Design challenge content**: Use content cards to display challenges on customer devices  
* **Set up task requirements**: Define actions like purchases, visits, or custom events with rewards
* **Send multi-channel notifications**: Deliver messages via in-app, email, and push at key stages
* **Track performance**: Monitor through auto-generated journeys and built-in reports

## How it works {#how-it-works-overview}

Creating a loyalty challenge follows this workflow:

1. **Set up data ingestion** - Configure source connectors to track customer actions
2. **Create a challenge** - Define type, audience, and dates
3. **Add tasks** - Configure actions and rewards
4. **Design content** - Create content cards and optional messaging
5. **Publish** - Journey Optimizer auto-generates and activates a journey
6. **Monitor** - Track participation and performance

>[!NOTE]
>
>The auto-generated journey appears in your journey inventory and can be customized if needed. However, changes made directly to the journey do not sync back to the challenge configuration.

## Prerequisites {#prerequisites-overview}

Before using Loyalty Challenges:

* Configure Experience Platform source connectors (e.g., Capillary) to ingest loyalty event data
* Ensure you have appropriate permissions in Journey Optimizer
* Create target audiences in Experience Platform

For detailed prerequisites, see [Understand Loyalty Challenges](get-started.md#prerequisites).

## Important limitations {#limitations-overview}

* **No ledger system**: Loyalty Challenges does not track monetary values or point balances. Journey Optimizer calls your external loyalty management system to handle point allocation.
* **Audience selection only**: You can select existing audiences but cannot create new audiences from the Loyalty Challenges UI.

## Next steps {#next-steps}

<table style="table-layout:fixed">
<tr style="border: 0;">
  <td>
    <a href="get-started.md">
    <img alt="Understand" src="../assets/do-not-localize/learn-more-button.svg">
    </a>
    <div>
    <a href="get-started.md"><strong>Understand Loyalty Challenges</strong></a>
    </div>
    <p>
    <em>Learn about features, workflow, and capabilities</em>
    <p>
  </td>
  <td>
    <a href="create-challenges.md">
      <img alt="Create" src="../assets/do-not-localize/start-button.svg">
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
    <img alt="Manage" src="../assets/do-not-localize/monitor-button.svg">
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
