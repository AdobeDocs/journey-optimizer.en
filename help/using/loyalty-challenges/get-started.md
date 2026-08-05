---
solution: Journey Optimizer
product: journey optimizer
title: Get started with Loyalty Challenges
description: Learn how to create and manage loyalty challenges in Adobe Journey Optimizer to build engaging, rewarding loyalty programs.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
exl-id: 1c84d9d0-cef7-4764-9f72-5428597a7203
feature_v2: []
subfeature_v2:
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
---
# Get started with loyalty challenges {#get-started-loyalty-challenges}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_inventory"
>title="Loyalty challenges"
>abstract="Loyalty Challenges enable you to create engaging, gamified loyalty programs that drive customer behavior and deepen brand relationships. Build challenges that reward customers for specific actions—from making purchases and writing reviews to engaging on social media and referring friends."

>[!AVAILABILITY]
>
>Journey Optimizer Loyalty is not currently available to Healthcare Shield and Privacy and Security Shield customers. Availability for Healthcare Shield and Privacy and Security Shield customers will be updated upon future feature readiness.

## Overview {#overview}

Loyalty Challenges enable you to create engaging, gamified loyalty programs that drive customer behavior and deepen brand relationships. Build challenges that reward customers for specific actions—from making purchases and writing reviews to engaging on social media and referring friends.

With Loyalty Challenges, you can:

* **Design flexible challenge types**: Create Standard, Streak, or Sequential challenges to match your business goals
* **Configure rewards strategically**: Deliver points at task milestones or upon full completion to maintain engagement
* **Personalize the experience**: Use content cards and multi-channel messaging to create immersive, branded experiences
* **Integrate seamlessly**: Connect with your existing loyalty providers and leverage Experience Platform data
* **Track automatically**: Monitor customer progress through auto-generated journeys without custom development
* **Measure performance**: Use built-in reporting dashboards to track program KPIs, challenge results, and task-level metrics

![](assets/challenges-gs.png)

You can create these types of challenge experiences:

* **Standard challenges**: Customers complete any specified number of tasks in any order. Use this type when you want flexibility and multiple paths to completion.  
  *Example: "Summer Wellness Challenge" - Complete 3 out of 5 tasks: buy health products, share on social media, refer a friend, write a review, or attend a virtual event*

* **Streak challenges**: Customers complete the same task multiple times consecutively. Use this type to encourage consistent, repeated behavior over time.  
  *Example: "Coffee Lover's Week" - Purchase coffee products for 7 consecutive days to unlock a free drink reward*

* **Sequential challenges**: Customers complete tasks in a defined order. Use this type to guide customers through a specific journey or onboarding process.  
  *Example: "New Member Journey" - Sign up for emails → Make your first purchase → Write a product review → Refer a friend (complete in this exact order)*

* **Bring your own data challenges** (restricted availability): The challenge framework (tasks and rewards) is assembled from your Loyalty Challenges data integration. You configure Settings, Content, and Messaging as you would for any other challenge type.

>[!TIP]
>You can also create and manage loyalty challenges using **Loyalty Challenge Management** in [CX Coworker Journey Skills](../start/ajo-coworker-skills.md#loyalty-challenge-management) with natural language prompts for faster challenge creation.

➡️ [Watch an overview of the feature](#video)

## How it works {#how-it-works}

Using Loyalty Challenges involves three broad phases — setup, execution, and measurement — typically shared across admin and practitioner roles.

**1. Set up your program** *(admin)*

Before challenges can be authored, an administrator configures the program foundations: reward providers, event definitions that map customer actions to task completions, product inventory, and exclusion lists. [Learn how to configure loyalty challenges](loyalty-admin.md).

**2. Author and launch challenges** *(practitioner)*

Marketers create challenges by selecting a type (Standard, Streak, Sequential, or Bring your own data), configuring settings (audience, schedule, rules), and defining tasks and rewards. They can optionally surface the challenge on member-facing interfaces using a **content card** or **code-based experience**, and set up channel notifications for key moments across the challenge lifecycle. Once configured, they publish the challenge, generate the auto-built journey, and publish it to make the challenge live. [Learn how to create challenges](create-challenges.md).

**3. Monitor performance** *(practitioner / analyst)*

Once a challenge is live, built-in reporting dashboards provide challenge-level metrics: audience funnel performance, task completion rates, reward issuance, and revenue impact. The AI-powered insights engine also surfaces contextual recommendations to help optimize program performance. [Learn about loyalty reporting](loyalty-reporting.md).

## Prerequisites {#prerequisites}

Before using Loyalty Challenges, ensure you have:

+++Required permissions

To use Loyalty Challenges, you must be assigned to a Loyalty role. Default roles are available for administrators, practitioners, and analysts in the Prod sandbox. For non-Prod sandboxes, your administrator must create a custom role with the required Loyalty permissions.

Contact your administrator if you cannot access the feature or need additional permissions. [Learn how to configure Loyalty Challenges permissions](loyalty-permissions.md).

+++

+++Configure the loyalty program (administrators)

Administrators configure reward providers, event definitions, product inventory, exclusions, and global settings in the **[!UICONTROL Loyalty configurations]** menu. Marketers who only create challenges do not need access to this menu. [Learn how to configure loyalty challenges](loyalty-admin.md)

Contact your administrator if the **[!UICONTROL Loyalty configurations]** menu is not visible in the left navigation.

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
  <td>
    <a href="loyalty-reporting.md">
      <img alt="Reports" src="assets/do-not-localize/icon-reporting.png" width="200"/>
    </a>
    <div>
    <a href="loyalty-reporting.md"><strong>Monitor performance</strong></a>
    </div>
    <p>
    <em>Track program KPIs, challenge results, and task metrics with built-in dashboards</em>
    </p>
  </td>
  <!--
    <a href="loyalty-admin.md"><strong>Configure the loyalty program</strong></a>
  <td>
    <a href="loyalty-admin.md">
    <em>Set up reward providers, event definitions, and org settings for fulfillment</em>
    </a>
    <div>
-->
    <a href="loyalty-admin.md"><strong>Configure loyalty challenges</strong></a>
    </div>
    <p>
    <em>Set up reward providers, event definitions, and org settings</em>
    </p>
  </td>
</tr>
</table>

## Developer resources {#developer-resources}

Loyalty Challenges exposes REST APIs that let you programmatically manage challenges and track profile participation:

* **[Loyalty challenge metadata API](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges){target="_blank"}** — Create, retrieve, update, publish, archive, and duplicate challenges.
* **[Loyalty challenge state API](https://developer.adobe.com/journey-optimizer-apis/references/loyalty-challenges-state){target="_blank"}** — Query and update challenge participation state for individual profiles.

For authentication and required headers, see the [authentication tutorial](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"}.

## How-to video {#video}

**New to Loyalty Challenges?** Watch this overview to understand the capabilities and benefits:

>[!VIDEO](https://video.tv.adobe.com/v/3496441?quality=12)

