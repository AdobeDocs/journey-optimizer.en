---
solution: Journey Optimizer
product: journey optimizer
title: Coworker for Loyalty
description: Discover the CX Enterprise Coworker skills available for creating, managing, and analyzing loyalty challenges in Adobe Journey Optimizer, with in-depth guidance and sample prompts.
feature: Overview
topic: Artificial Intelligence
role: User
level: Beginner
mini-toc-levels: 1
exl-id: 876b7770-9b11-4e3c-b426-5ffb06e093cf
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: d595a60b-bcf5-4a63-a189-66a0be755cc7
    internal-label: Templates
---

# Coworker for Loyalty {#loyalty-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Discover the CX Enterprise Coworker skills available for Loyalty Challenges in Adobe Journey Optimizer — creating and managing challenges, and querying loyalty program performance — with detailed guidance, example prompts, and best practices for each skill.

Learn more:

* [Coworker skills for Journey Optimizer](../start/ai-features.md#cx-coworker-skills) — overview of Coworker skills across Journeys, Loyalty, and Content Management in Journey Optimizer.
* [Coworker documentation](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/overview){target="_blank"} — overview of Coworker's Campaigns, Chat, and Projects capabilities.
* [Coworker Chat UI guide](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide){target="_blank"} — how to access and navigate Coworker Chat.

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>Loyalty skills are available in Coworker for eligible organizations. Customers with a Loyalty license can access these loyalty skills, even if they do not have an additional Coworker license.

Loyalty skills empower loyalty administrators and analysts to create, manage, and analyze loyalty programs using natural language. With these AI-powered skills, you can quickly design engaging loyalty challenges, track performance metrics, and make data-driven decisions to optimize member engagement and program profitability. Whether you're building a new challenge or analyzing loyalty program trends, Loyalty skills streamline the entire loyalty management workflow.

## Loyalty Challenge Management {#loyalty-challenge-management}

Loyalty Challenge Management enables Journey Optimizer users to create and manage loyalty challenges in Coworker using natural language prompts. For comprehensive documentation on creating, configuring, and managing loyalty challenges, including detailed setup instructions, refer to the [Loyalty Challenges guide](get-started.md).

### Key use cases

1. **Multi-step onboarding challenge**

   "Build a challenge called "New Account Kickstart" for newly enrolled customers that requires them to complete these steps in order: open a checking account, fund it with at least $500, and download the mobile app. When all steps are done, reward them with 5,000 bonus points. Run it from September 1 to October 31, Eastern timezone."

1. **Cumulative activity threshold challenge**

   "Create a challenge called "Spend & Earn Summer" for cardholders where members earn a $50 statement credit once they spend $1,500 on their credit card during the third quarter. Start it July 1, Eastern timezone."

1. **Frequency streak challenge**

   "Create a challenge called "Frequent Flyer Sprint" for elite tier members that requires 3 flights per month for two consecutive months. Reward completion with a tier-status extension and 10,000 bonus miles. Start the first of next month, Pacific timezone."

1. **Single qualifying action challenge**

   "Set up a challenge named "Go Paperless" that rewards postpaid subscribers with 500 bonus points after they enroll in autopay and switch to paperless billing within 30 days. Begin on the first of next month, Central timezone."

1. **Engagement / consumption goal challenge**

   "Create a challenge called "Explorer Badge" for members that requires them to complete 5 activities across at least 3 different categories during the month of August. Reward them with 1,000 points and an "Explorer" badge on completion. Start August 1, Mountain timezone."

1. **Daily action challenge**

   "Help me create a challenge for matcha lovers that requires them to come into the store every day this week and buy a matcha drink. Their reward should be an extra 200 points if they complete the challenge. Call it "Mad about Matcha", use SKU matcha-001, start it Monday next week, Eastern timezone."

### In scope skills

The following capabilities are supported by Loyalty Challenge Management:

* **Challenge creation**: Create challenge configuration from natural language (audience, action criteria, timing, reward, naming).
* **Challenge updates**: Modify challenge details through iterative prompts.
* **Challenge publishing**: Publish supported challenge configurations directly from the conversation.
* **Challenge context visibility**: Retrieve and review challenge information while iterating.

### Out of scope skills

The following functionalities are currently not supported:

* Challenge deletion
* Loyalty insights and recommendations skills
* Full content authoring automation for challenge messaging in all cases

### Prompting best practices

1. **Name it**: Give the challenge a clear, memorable title in quotes.
1. **Specify the audience**: Who qualifies (e.g., all members, a tier, a segment, new enrollees, cardholders, subscribers).
1. **Define the action and how much**: What members must do, and the frequency, threshold, or sequence that counts as completion.
1. **Set the time window**: A start date (and end date if fixed-duration) plus the timezone.
1. **State the reward**: Points, miles, statement credits, status extensions, vouchers, or perks granted on completion.
1. **Reference the qualifying event**: Point to the specific SKU, product, account action, or engagement event the challenge tracks.

## Loyalty Insights Skill {#loyalty-data-insight}

Loyalty Insights Skill enables Journey Optimizer users to analyze and query loyalty program performance data using natural language. This skill provides insights into loyalty points, member tiers, redemptions, and revenue metrics, allowing loyalty administrators and analysts to make data-driven decisions about their loyalty programs.

Key use cases:

1. **Loyalty points analysis**

   * Analyze loyalty points granted, earned, and redeemed over specific periods.
   * Compare loyalty point activities across different loyalty tiers and programs.
   * Track loyalty points balance by member segment.

   Sample prompts:
   * "How many loyalty points were granted during August 2026?"
   * "How many loyalty points were gained by members in each loyalty tier during August 2026?"
   * "Show me the total loyalty points redeemed by member loyalty status—not loyalty tier—during August 2026."
   * "Show the total loyalty points balance broken down by loyalty tier during August 2026."

1. **Revenue and discount analysis**

   * Analyze order revenue and loyalty discount trends by tier and program.
   * Compare revenue generation across loyalty programs and time periods.
   * Track discount impact on revenue and member engagement.

   Sample prompts:
   * "What was the total order revenue for each loyalty tier during August 2026?"
   * "How much in loyalty discounts was applied to each loyalty tier during August 2026?"
   * "Show the total loyalty discounts broken down by loyalty program during August 2026."
   * "What was the total order revenue generated by each loyalty program during August 2026?"

1. **Program performance insights**

   * Analyze daily, weekly, and monthly program performance metrics.
   * Compare performance across product categories and discount strategies.
   * Identify trends in member engagement and redemption patterns.

   Sample prompts:
   * "Show the loyalty program's total revenue broken down by day during August 2026."
   * "Show the total loyalty discounts broken down by product category during August 2026."
   * "Show me the loyalty program performance report for Q3 2026."

{{$include /help/_includes/do-not-localize/start/ai-augmented-loyalty-coworker-skills.md}}
