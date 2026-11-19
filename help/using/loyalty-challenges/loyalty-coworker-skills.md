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
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
subfeature_v2:
  - id: d595a60b-bcf5-4a63-a189-66a0be755cc7
    internal-label: Templates
  - id: fdac7813-bd56-47ae-9f6d-fa94ad1c5dee
    internal-label: Overview
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---

# Coworker for Loyalty {#loyalty-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Explore Coworker capabilities in Adobe Journey Optimizer for creating loyalty challenges and analyzing loyalty program performance.

>[!ENDSHADEBOX]

Loyalty capabilities in Adobe Journey Optimizer help you create and manage loyalty challenges and analyze loyalty program performance through natural-language prompts. Use Loyalty Challenge Management to define challenge audiences, actions, timing, and rewards. Use Loyalty Insights to explore loyalty points, member tiers, redemptions, revenue, and discount trends.

Learn more:

* [Coworker skills for Journey Optimizer](../start/ai-features.md#cx-coworker-skills) — overview of Coworker skills across Journeys, Loyalty, Content Management, and Decisioning in Journey Optimizer.
* [Coworker documentation](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/overview){target="_blank"} — overview of Coworker's Campaigns, Chat, and Projects capabilities.
* [Coworker Chat UI guide](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide){target="_blank"} — how to access and navigate Coworker Chat.

>[!AVAILABILITY]
>
>Loyalty skills are available in Coworker for eligible organizations. Customers with a Loyalty license can access these loyalty skills, even if they do not have an additional Coworker license.

Loyalty skills empower loyalty administrators and analysts to create, manage, and analyze loyalty programs using natural language. With these AI-powered skills, you can quickly design engaging loyalty challenges, track performance metrics, and make data-driven decisions to optimize member engagement and program profitability. Whether you're building a new challenge or analyzing loyalty program trends, Loyalty skills streamline the entire loyalty management workflow.

## Loyalty Challenge Management {#loyalty-challenge-management}

Loyalty Challenge Management enables Journey Optimizer users to create and manage loyalty challenges in Coworker using natural language prompts. For comprehensive documentation on creating, configuring, and managing loyalty challenges, including detailed setup instructions, refer to the [Loyalty Challenges guide](get-started.md).

➡️ [Discover this feature in video](#loyalty-challenge-management-videos)

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Multi-step onboarding challenge</strong><br>Create a challenge that rewards members for completing a series of steps in order, such as opening an account, funding it, and downloading the app.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Build a challenge called "New Account Kickstart" for newly enrolled customers that requires them to complete these steps in order: open a checking account, fund it with at least $500, and download the mobile app. When all steps are done, reward them with 5,000 bonus points. Run it from September 1 to October 31, Eastern timezone.</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Cumulative activity threshold challenge</strong><br>Reward members once their total activity, such as spend, reaches a target within a set period.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Create a challenge called "Spend &amp; Earn Summer" for cardholders where members earn a $50 statement credit once they spend $1,500 on their credit card during the third quarter. Start it July 1, Eastern timezone.</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Frequency streak challenge</strong><br>Reward members for repeating an action a set number of times over consecutive periods, such as three flights per month for two months in a row.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Create a challenge called "Frequent Flyer Sprint" for elite tier members that requires 3 flights per month for two consecutive months. Reward completion with a tier-status extension and 10,000 bonus miles. Start the first of next month, Pacific timezone.</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Single qualifying action challenge</strong><br>Reward members for completing a specific action, such as enrolling in autopay, within a defined time window.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Set up a challenge named "Go Paperless" that rewards postpaid subscribers with 500 bonus points after they enroll in autopay and switch to paperless billing within 30 days. Begin on the first of next month, Central timezone.</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Engagement / consumption goal challenge</strong><br>Reward members for reaching an engagement goal, such as completing a number of activities across several categories during a month.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Create a challenge called "Explorer Badge" for members that requires them to complete 5 activities across at least 3 different categories during the month of August. Reward them with 1,000 points and an "Explorer" badge on completion. Start August 1, Mountain timezone.</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Daily action challenge</strong><br>Reward members for performing an action every day over a set period, such as buying a specific product each day for a week.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Help me create a challenge for matcha lovers that requires them to come into the store every day this week and buy a matcha drink. Their reward should be an extra 200 points if they complete the challenge. Call it "Mad about Matcha", use SKU matcha-001, start it Monday next week, Eastern timezone.</td></tr>
</table>


### Prompting best practices

* **Name it**: Give the challenge a clear, memorable title in quotes.
* **Specify the audience**: Who qualifies (e.g., all members, a tier, a segment, new enrollees, cardholders, subscribers).
* **Define the action and how much**: What members must do, and the frequency, threshold, or sequence that counts as completion.
* **Set the time window**: A start date (and end date if fixed-duration) plus the timezone.
* **State the reward**: Points, miles, statement credits, status extensions, vouchers, or perks granted on completion.
* **Reference the qualifying event**: Point to the specific SKU, product, account action, or engagement event the challenge tracks.

### Out of scope skills

The following functionalities are currently not supported:

* Challenge deletion
* Full content authoring automation for challenge messaging in all cases

### How-to videos {#loyalty-challenge-management-videos}

Learn how Coworker creates, manages, and optimizes loyalty challenges in this video.

>[!VIDEO](https://video.tv.adobe.com/v/3496528?quality=12)

## Loyalty Insights {#loyalty-data-insight}

Loyalty Insights enables Journey Optimizer users to analyze and query loyalty program performance data using natural language. This skill provides insights into loyalty points, member tiers, redemptions, and revenue metrics, allowing loyalty administrators and analysts to make data-driven decisions about their loyalty programs.

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Loyalty points analysis</strong><br>Analyze loyalty points granted, earned, and redeemed over specific periods. Compare loyalty point activities across different loyalty tiers and programs. Track loyalty points balance by member segment.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">How many loyalty points were granted during August 2026?<br><br>How many loyalty points were gained by members in each loyalty tier during August 2026?<br><br>Show me the total loyalty points redeemed by member loyalty status—not loyalty tier—during August 2026.<br><br>Show the total loyalty points balance broken down by loyalty tier during August 2026.</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Revenue and discount analysis</strong><br>Analyze order revenue and loyalty discount trends by tier and program. Compare revenue generation across loyalty programs and time periods. Track discount impact on revenue and member engagement.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">What was the total order revenue for each loyalty tier during August 2026?<br><br>How much in loyalty discounts was applied to each loyalty tier during August 2026?<br><br>Show the total loyalty discounts broken down by loyalty program during August 2026.<br><br>What was the total order revenue generated by each loyalty program during August 2026?</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Program performance insights</strong><br>Analyze daily, weekly, and monthly program performance metrics. Compare performance across product categories and discount strategies. Identify trends in member engagement and redemption patterns.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Show the loyalty program's total revenue broken down by day during August 2026.<br><br>Show the total loyalty discounts broken down by product category during August 2026.<br><br>Show me the loyalty program performance report for Q3 2026.</td></tr>
</table>


## Loyalty Opportunities {#loyalty-opportunities}

Loyalty Opportunities enables marketers to request grounded, specific challenge opportunities through natural language conversations in CX Coworker. Opportunities use loyalty program trends and performance data and can focus on increasing member spend, winning back inactive members, improving underperforming challenges, focusing on products or categories, or addressing points expiry.

Marketers can narrow opportunities to the goals they care about and pass an opportunity to the Loyalty Challenge Management skill to create or edit a live challenge without leaving the conversation.

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Get recommended challenges</strong><br>Ask what you should do to improve your loyalty program, or request an overview of recommended challenges. Coworker surfaces grounded, specific challenge opportunities based on loyalty program trends and performance data.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">What should we do to grow our loyalty program?<br><br>Show me recommended challenges.</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Focus opportunities on a goal</strong><br>Narrow opportunities to a specific goal, such as increasing member spend, winning back inactive members, improving underperforming challenges, promoting products or categories, addressing points expiry, or onboarding new members. You can ask about product or category promotion without naming a specific product.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Show me opportunities to increase member spend.<br><br>Which challenges could help win back inactive members?<br><br>Show me opportunities to address points expiry.<br><br>What challenges could promote a product category?</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Review an opportunity and its rationale</strong><br>Open the <strong>Opportunities</strong> tab and select <strong>View details</strong> to review the proposed challenge and its rationale.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Why is this opportunity recommended?<br><br>Show me the rationale for this opportunity.</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Implement an opportunity as a live challenge</strong><br>Select <strong>Create with AI</strong> to pass the opportunity to the Loyalty Challenge Management skill. Continue the conversation to provide missing details and create or edit the challenge without leaving Coworker Chat.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">Create a challenge from this opportunity.</td></tr>
</table>

<!-- TO CONFIRM (PM): the skill description in Coworker says it identifies stored challenge opportunities and does not generate new ones or create or edit challenges. Confirm this wording, and validate the sample prompts, which are drafted from that description. -->

After the challenge is created or edited, review the challenge details and journey in challenge authoring before publishing.

{{$include /help/_includes/do-not-localize/loyalty-challenges/ai-augmented-loyalty-coworker-skills.md}}
