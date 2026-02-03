---
solution: Journey Optimizer
product: journey optimizer
title: Understand Loyalty Challenges  
description: Learn about Loyalty Challenges features, workflow, and capabilities in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
---

# Understand Loyalty Challenges {#understand-loyalty-challenges}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_challenges_overview"
>title="About Loyalty Challenges"
>abstract="Loyalty Challenges enables you to create personalized engagement offers that motivate customers to complete specific actions and earn rewards."

Loyalty Challenges enables you to design and deploy personalized engagement offers that motivate customers to complete specific actions and earn rewards.

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](gs-loyalty-challenges.md) - Quick overview and next steps
* **Understand Loyalty Challenges** ◀︎ **You are here** - Features, workflow, prerequisites
* [Create challenges](create-challenges.md) - Build and configure challenges
* [Manage challenges](manage-challenges.md) - Edit, monitor, optimize

>[!ENDSHADEBOX]

## Overview {#overview}

Loyalty Challenges provides a complete solution for creating loyalty programs at scale, from defining tasks and milestones to delivering content and tracking performance across channels. You can create three types of challenge experiences, configure rewards, send multi-channel notifications at key lifecycle stages, and monitor performance through automatically generated journeys—all while maintaining integration with your external loyalty management system.

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

## Key capabilities {#key-capabilities}

Use Loyalty Challenges to:

* **Create three types of challenges**:
  * **Standard**: Customers complete any number of tasks to earn rewards.
  * **Streak**: Customers complete the same task multiple times.
  * **Sequential**: Customers complete tasks in a specific order.

* **Design challenge content**: Use Journey Optimizer content cards to create the visual representation of your challenge on customer devices. Content cards display the challenge information, progress, and rewards on the customer's device.

* **Set up task requirements**: Define what customers must do to earn rewards, including:
  * Task types (purchase, spend amount, visit, etc.)
  * Quantity requirements
  * Product inclusions/exclusions using SKUs
  * Custom attributes and conditions

* **Configure rewards**: Define rewards that customers earn either at task completion or after completing the entire challenge

* **Send notifications**: Deliver messages across multiple channels (in-app, email, push) at key stages:
  * **Launch**: When the challenge starts
  * **In progress**: When customers are partway through
  * **Complete**: When customers finish the challenge

* **Track performance**: Monitor automatically generated journeys and review challenge performance

### Important limitations {#limitations}

* **No ledger system**: Loyalty Challenges does not track monetary values or point balances. When customers complete a challenge and earn a reward, Journey Optimizer calls your external loyalty management system to handle point allocation.

* **Audience selection only**: You can select existing audiences but cannot create new audiences from the Loyalty Challenges UI.

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

## Access Loyalty Challenges {#access}

To access Loyalty Challenges:

1. In Adobe Journey Optimizer, select **[!UICONTROL Loyalty challenges]** in the left navigation menu.

2. The Loyalty Challenges inventory displays all existing challenges with information such as:
   * Challenge name and description
   * Status (Draft, Live, Stopped, etc.)
   * Challenge type (Standard, Streak, Sequential)
   * Start and end dates
   * Last modification date

3. Select **[!UICONTROL Create challenge]** to start creating a new challenge.

### Search and filter challenges {#search-filter}

Use search and filtering capabilities to quickly find specific challenges:

* **Search**: Enter challenge name or keywords in the Search field
* **Filter by status**: Draft, Scheduled, Live, Completed, Stopped, or Archived
* **Filter by type**: Standard, Streak, or Sequential challenges
* **Filter by date**: Challenges within a specific date range
* **Filter by tags**: Challenges with specific tags applied

## Next steps {#next-steps}

Now that you understand Loyalty Challenges, learn how to create your first challenge:

* [Create challenges](create-challenges.md)
* [Manage challenges](manage-challenges.md)
