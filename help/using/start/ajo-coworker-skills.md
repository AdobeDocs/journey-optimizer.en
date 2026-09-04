---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer skills in CX Coworker
description: Discover the Adobe Journey Optimizer skills available in CX Coworker, with in-depth guidance and sample prompts.
feature: Overview
topic: Artificial Intelligence
role: User
level: Beginner
mini-toc-levels: 2
---

# Journey Optimizer skills in CX Coworker {#ajo-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Discover the Adobe Journey Optimizer skills available in CX Coworker — from creating and analyzing journeys to generating channel content and managing content assets — with detailed guidance, example prompts, and best practices for each skill.

>[!ENDSHADEBOX]

## Overview {#overview}

CX Coworker brings AI-powered capabilities to Adobe Journey Optimizer. [CX Coworker](https://experienceleague.adobe.com/en/docs/cx-enterprise-coworker/content/home){target="_blank"} is Adobe's conversational experience that integrates with your business applications to help you work more efficiently.

With its AI-powered skills, CX Coworker enables Journey Optimizer users to create, analyze, and optimize marketing journeys using a natural language interface. With Journey Skills, practitioners can quickly build journeys, detect and resolve schedule or audience conflicts, analyze performance and drop-off points, and identify top-performing journeys to replicate for future campaigns. It empowers practitioners to make data-driven decisions, improve customer engagement, and streamline journey orchestration.

CX Coworker provides various skills for managing Journeys and Loyalty challenges:

**Journey-focused skills:**

* **Journey Create**: Build and configure marketing journeys through natural language prompts
* **Channel Content Create**: Generate, edit, and manage channel-specific content (email, push, SMS) for journeys using AI-powered content generation
* **Content Management**: List, retrieve, create, update, and publish content templates, fragments, landing pages, and journey/campaign inline message content
* **Journey Analyze**: Analyze journeys, detect issues, uncover insights, and optimize journey performance

**Loyalty-focused skills:**

* **Loyalty Challenge Management**: Create and manage loyalty challenges using natural language prompts
* **Loyalty Agent - Data Insight Skill**: Query and analyze loyalty program performance data using natural language

<!--
feedback from Ivan: Need to remove Simulate skill from docs until Nico confirms the release timeline.

In addition, **Journey Simulation** is a Journey Optimizer feature that includes [Journey Simulate](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/simulate-journey/simulate-journey-gs), an in-product agentic skill, non conversational, with three capabilities: 

* Generating simulated users
* Generating event values
* Quick simulation
-->

## Journey skills {#journey-skills}

### Journey Create {#journey-create}

Journey Create enables Journey Optimizer users to build and configure marketing journeys using a natural language interface. With Journey Create, practitioners can quickly create journeys by describing their requirements in conversational prompts. The skill walks users through the different options for creating a journey, allowing marketers to focus on strategy rather than technical configuration.

>[!AVAILABILITY]
>
>You need the following permissions in order to fully use Journey Create features:
>
>**Manage Journeys**: This permission lets you create new journeys directly in CX Coworker.
>
>**View Journey Events, Data Sources and Actions**: This permission ensures that CX Coworker can search through Journey Events and Custom Actions. 
>
>**View Segments**: This permission ensures that CX Coworker can search for audience segments when creating a Journey.
>
>**Manage Segments**: This permission lets you create new audiences directly in CX Coworker.

#### Key use cases

Journey Create offers capabilities that can be leveraged to accelerate marketing execution:

1. **Event-triggered journey creation**

   * Create journeys that activate based on specific customer events.
   * Design automated responses to customer actions in real-time.
   * Build personalized communication flows based on customer behavior.

   **Store visit journey:**
   "Create a journey that starts when a user enters my store location. Send a push notification to welcome users to the store. Wait 2 days and check to see if the user has a valid email address. If the user has a valid email address, send an email survey to ask about their store experience. If the user does not have a valid email address, send a push notification to prompt for registration."

   **Post-purchase journey:**
   "Create a journey that starts when a customer makes a purchase online. Send a push notification to thank them for their purchase. Next, check to see if they are loyalty members. If the user is a loyalty rewards member, send a second push notification with a 10% discount code. If the user is not a loyalty rewards member, send a push inviting them to sign up for the loyalty program. Wait 2 days and send a follow-up push with a survey about their purchase experience."

   **Event-based promotion:**
   "Create a journey triggered when the game score reaches 50. Send an SMS message to loyalty reward members saying that they are eligible for a free slice of pizza from the partner sponsor."

1. **Audience-targeted journey creation**

   * Build journeys targeting specific audience segments.
   * Design multi-step communication sequences with strategic timing.

   **Seasonal campaign:**
   "I want to create a journey targeting an audience of day hikers. I want to send an email alerting this audience to my upcoming holiday sale that includes a variety of hiking essentials. Wait 3 days after sending the first email and send a second email that has a 15% coupon with free shipping. Wait 1 week and then send a 3rd email message to show our new sleeping bag and tent collection. Schedule the journey to start on 12/20."

   **Loyalty appreciation:**
   "Build a loyalty appreciation journey for SUV owners, including a thank you push notification with a free carwash offer and a follow-up push notification reminder if the first notification is not interacted with within 1 day."

1. **Business-event triggered journey creation** 

   * Create journeys that activate based on a particular business event and target a specified audience (e.g. product back in stock or game score change)
   * Trigger timely, context-aware messages when business conditions change.

1. **Audience qualification journey creation** 

   * Create journeys that activate as profiles enter or exit an audience segment definition.
   * Automate entry and exit messaging to support onboarding, retention, and win-back goals.  

1. **Conditional journey flows**

   * Create decision branches based on customer attributes.
   * Design split paths that adapt to customer preferences.

1. **Create journey from image**

    * Upload a reference image into coworker and ask to create a journey using the image as reference
    * Journey creation skill will extract an editable prompt from your reference image

With this skill, natural language requirements are translated into structured journey configurations.

#### In scope skills

The following capabilities are supported by Journey Create:

* **Natural language journey creation**: Allows users to describe journey flow in conversational language.
* **Event-based and audience-based journeys**: Supports both trigger-based and scheduled journey types, also business event and audience qualification.
* **Conditional logic**: Handles decision splits and branching based on customer attributes.
* **Multi-channel messaging**: Supports push notifications, email, and SMS channels.
* **Journey scheduling**: Configures start dates and timing for scheduled journeys.

#### Out of scope skills

The following functionalities are currently not supported:

* Advanced journey analytics 
* Cross-journey orchestration 
* A/B testing configuration 
* InAudience expression generation 
* Dataset lookup nodes 
* Wave sending settings 
* Schedule recurrence options 
* Namespace selection for audiences 
* Custom Action field mapping 
* Complex data transformations 

#### Prompting best practices

To maximize the effectiveness of Journey Create, follow these best practices:

1. **Be Specific**: Provide clear details about your journey goals, target audience, and desired actions. Include information about channels, timing, and conditions.
1. **Specify Timing**: Clearly indicate wait periods between actions and when the journey should start.
1. **Define Conditions**: When using conditional logic, explain the criteria for each branch path.
1. **Include Channels**: Specify which communication channels you want to use (push, email, SMS).
1. **Mention Scheduling**: For scheduled journeys, provide the desired start date and time.
1. **Custom Actions**: If you are using custom actions in your workflow you need to specify that you are using a custom action along with the exact name of the custom action. Example: 
   When a user enters my store location send a welcome message using custom action ExternalPush. Wait 2 days and then send a follow up message using custom action ExternalEmail with a survey on their visit.
1. **Validate Expressions**: Make sure to check and validate any expressions that Journey Skills create to ensure that the correct fields and values are used.

#### Setup best practices

* **Define Clear Objectives**: Before creating journeys, establish clear goals (improving retention, driving conversions, increasing engagement).
* **Prepare Audiences**: Ensure your target audiences are already created and properly segmented.
* **Plan Message Content**: Have your messaging strategy defined before journey creation.
* **Consider Customer Experience**: Design journey flows that respect customer preferences and avoid over-communication.

### Channel Content Create {#channel-content-create}

<!--Ivan : Need to speak with Amar on new options for content generation as this skill has changed. -->

>[!AVAILABILITY]
>
>This feature is available for all customers in Limited Availability. Contact your Adobe representative to gain access.

Channel Content Create enables Journey Optimizer users to generate, edit, and manage channel-specific content for journeys using AI-powered content generation.

#### Key use cases

1. **Channel-specific content generation**: Generate content for email, push notifications, SMS, and other channels using natural language prompts.

   "Generate email content for my welcome journey. Create a welcome email for new customers with a friendly tone and include a 10% discount offer."

   "Generate a push notification for my store visit journey. Create a welcome message that encourages customers to check in and receive a special offer."

   "Generate SMS content for my event-triggered journey. Create a short message notifying customers about a flash sale with a call-to-action."

1. **Template-based content creation**: Browse and select from available templates with preview capabilities.

   "Show me available email templates for my seasonal campaign journey."

   "Select a template for my email that has a modern, clean design."

1. **Multi-channel content management**: Generate and manage content for multiple channels within the same journey workflow.

1. **In-context content editing**: Open generated content in Content Designer for editing and refinement.

   "Open the email content in Content Designer so I can customize the design."

1. **Content refinement and iteration**: Regenerate content with different tones or styles using the Regenerate action.

   "Regenerate the push notification content with a more casual tone."

   "Update the email content to include a promotional code."

1. **Journey canvas integration**: Select journeys from inventory and view associated channels.

#### In scope skills

The following capabilities are supported by Channel Content Create:

* **AI-powered content generation**: Generate content for email, push, SMS, and other channels using natural language prompts.
* **Template management**: Browse and select from available templates with preview capabilities.
* **In-context editing**: Open generated content in Content Designer for editing and refinement.
* **Content regeneration**: Regenerate content with different tones, styles, or messaging using the Regenerate action.
* **Multi-channel support**: Generate and manage content for multiple channels within the same journey workflow.
* **Journey inventory access**: Select journeys from inventory and view associated channels.

#### Out of scope skills

The following functionalities are currently not supported:

* **Brand alignment and content quality checks**
* **Insert content nodes directly into journey canvas**
* **Template import**

#### Prompting best practices

1. **Be Specific**: Provide clear details about the content type, tone, target audience, and key messaging.
1. **Specify Channel**: Clearly indicate which channel you are creating content for (email, push, SMS).
1. **Define Tone**: Specify the desired tone (friendly, formal, casual, urgent).
1. **Iterate and Refine**: Use the regenerate action to refine content until it meets your requirements.

### Content Management {#content-management}

>[!AVAILABILITY]
>
>This feature is available for all customers with access to CX Coworker.

Content Management enables Journey Optimizer users to discover and manage AJO content assets — content templates, fragments, landing pages, and journey/campaign inline message content — directly from CX Coworker using natural language prompts. It lets you go from "tell me about my content" to "go build, update, and publish it," without leaving the conversation.

<!--For RN:
**Content Management skill in CX Coworker** - CX Coworker now includes a new **Content Management** skill, letting you discover and manage AJO content assets directly through natural language prompts. You can list and retrieve content templates, fragments, landing pages, and journey/campaign inline message content, as well as create and import content templates (including from an allowlisted external source such as Figma, via URL or HTML), update templates, and create, update, clone, and publish fragments, and update inline message content on journey or campaign action nodes. [Read more](../start/ajo-coworker-skills.md#content-management)

Availability date: September 2, 2026
-->

#### Key use cases

1. **Browse and inspect content**

   * List available content templates, fragments, or landing pages, and retrieve their structure, metadata, and status.
   * Retrieve the inline message content configured on a journey or campaign action node.

   Sample prompts:
   * "List my email content templates."
   * "Show me the fragments available for my summer campaign."
   * "Get the details of landing page page-123."
   * "What content is configured for the email variant of the action node in campaign camp-789?"

1. **Create and import content templates**

   * Create a new content template for any channel.
   * Import a template from an allowlisted external source, such as a Figma page, via URL or HTML.

   Sample prompts:
   * "Create an email template named Summer Sale from this Figma page URL."
   * "Create a new SMS template called Flash Alert."

1. **Update content templates**

   * Fully replace the content of an existing template.

   Sample prompts:
   * "Update template abc-123 with this new HTML body."

1. **Create, update, clone, and publish fragments**

   * Create a new HTML or expression fragment.
   * Update an existing fragment's content or metadata.
   * Clone an existing fragment under a new name.
   * Submit a draft fragment for publication.

   Sample prompts:
   * "Create an HTML fragment named Promo Banner with this markup."
   * "Update fragment frag-456 to change its name to Promo Banner V2."
   * "Clone fragment abc-123 as Promo Banner - Summer (Variant B)."
   * "Publish fragment frag-456."

1. **Update inline message content**

   * Replace one channel variant on a campaign or journey action node's inline message.
   * List the channel variants defined on a journey or campaign action node.

   Sample prompts:
   * "Update the email variant of the action node in campaign camp-789 with this new content."
   * "What channel variants are defined on this action node?"

#### In scope skills

The following capabilities are supported by Content Management:

* **List and get content templates**: Browse content templates and retrieve their structure and metadata.
* **List and get fragments**: Browse content and expression fragments and retrieve their details.
* **List and get landing pages**: Browse landing pages and retrieve their metadata and page content.
* **Get campaign/journey inline content**: Retrieve the inline message content configured on a campaign or journey action node.
* **Create and import content templates**: Create a new template for any channel, including import from an allowlisted external source (e.g. Figma) via URL or HTML.
* **Update content templates**: Fully replace the content of an existing template.
* **Create, update, clone, and publish fragments**: Create new fragments, update existing ones, clone a fragment under a new name, and submit a draft fragment for publication.
* **Update inline message content**: Replace a channel variant on a campaign/journey action node's inline message, and list the channel variants defined on an action node.

#### Out of scope skills

The following functionalities are currently not supported:

* **Full-text search across templates or fragments**
* **Template or fragment validation** (orphaned references, broken links, deprecated components)
* **Creating or publishing landing pages**
* **Deleting content templates, fragments, or landing pages**

#### Prompting best practices

1. **Reference IDs when known**: Provide the template, fragment, landing page, or campaign/journey ID when asking to get, update, clone, or publish a specific asset.
1. **Be explicit about the channel**: When creating a template or fragment, specify the channel or content type (email, HTML fragment, expression fragment).
1. **Confirm before publishing**: Review a fragment's content after creating or updating it before asking Coworker to publish it.
1. **Provide complete replacement content**: Update operations replace content in full, so include the complete HTML body or variant content in your prompt.

### Journey Analyze {#journey-analyze}

Journey Skills will enable Journey Optimizer users to analyze and optimize journeys using a natural language interface. With Journey Skills, practitioners can quickly identify and resolve schedule and/or audience conflicts, detect points of user abandonment in a journey and provide insights or recommendations. It empowers practitioners to make data-driven decisions, improve customer engagement, and streamline journey orchestration.

>[!AVAILABILITY]
>
>Journey Skills are available for all customers who have access to CX Coworker. However, you will need the following permissions in order to fully use the Journey Skills features:
>
>**View Journeys**: This permission lets you view insights into the journey directly in CX Coworker.
>
>**Manage Journeys**: This permission lets you create new journeys directly in CX Coworker.
>
>**View Segments**: This permission lets you view insights into the audiences directly in CX Coworker.
>
>**Manage Segments**: This permission lets you create new audiences directly in CX Coworker.

#### Key use cases

Journey Analyze offers a range of functionalities that can be leveraged to optimize marketing efforts:

1. **Journey Fallout Analysis**

   * Identify where and why customers drop off during a journey.
   * Detect patterns in customer behavior leading to disengagement.
   * Use insights to refine journey design and improve retention.

   Sample prompts:
   * "I want to analyze the fallout by node for journey Fourth of July Campaign."
   * "Perform a fallout analysis for journey Fourth of July Campaign."
   * "What is profile loss over the course of journey Fourth of July Campaign?"
   * "Show where users are dropping off in journey Fourth of July Campaign."

1. **Journey Audience Overlap Analysis**

   * Analyze audience overlap across multiple journeys.
   * Prevent audience fatigue caused by over-targeting.
   * Optimize segmentation to ensure balanced engagement.

   Sample prompts:
   * "Which audiences are used in more than X journeys?"
   * "List all journeys using the [audience name] audience."
   * "Show me audience overlap conflicts for journey [Journey Name]."
   * "Show overlapping audiences for journey [Journey Name] and other journeys."

1. **Journey Schedule Overlap Analysis**

   * Detect timing conflicts between scheduled journeys targeting the same audience.
   * Avoid over-communication and improve scheduling efficiency.
   * Maximize audience impact by ensuring journeys run at optimal times.

   Sample prompts:
   * "Are there any scheduling conflicts for journey [Journey Name]?"
   * "Check for scheduling conflicts involving journey [Journey Name]."
   * "Highlight scheduling overlaps between journey [Journey Name] and live journeys."
   * "Is journey [Journey Name] running in conflict with any other journey?"

1. **Operational insights** 

   * Prompt-based Journey Insights – Surface operational insights about journeys , i.e. "show me all live journeys."

   Sample prompts:
   * "When was [Journey Name] published?"
   * "When was [Journey Name] stopped?"
   * "List all journeys currently in test mode"
   * "How many live journeys do I have?"
   * "Give me a list of all scheduled recurring journeys and their expected run times."

1. **Journey Custom Action Error Analysis**

   * Identify when custom actions are failing or error rates spike within a journey.
   * Diagnose root causes before failures cascade into broader journey disruption.
   * Use specific remediation steps to restore custom action reliability quickly.

   Sample prompts:
   * "Why are custom actions failing in journey [Journey Name]?"
   * "What is the error rate for custom action [Custom Action Name] in journey [Journey Name]?"
   * "Show me the root cause of custom action failures in journey [Journey Name]."
   * "Are there any custom action errors affecting journey [Journey Name] right now?"

#### In scope skills

The following capabilities are supported by Journey Analyze:

* **Reactive Queries**: Allows users to ask specific questions about journey performance, audience usage, and scheduling conflicts.
* **Integration with Other Skills**: Collaborates with Audience and Data Insights capabilities for deeper analysis.
* **Response structuration**: reasoning (explain the logic), analysis summary (highlight key points), issue details (describe the problem), and recommendation (propose next steps).
* **Custom action error analysis**: Detect and diagnose custom action failures and error spikes within a journey.

#### Out of scope skills

The following functionalities are currently not supported:

* **Automated Journey Creation**
* **Real-Time Anomaly Detection**
* **Channels overlap**
* **Journey entry analysis**
* **Technical issue analysis**
* **Fatigue analysis**

#### Prompting best practices

To maximize the effectiveness of Journey Analyze, follow these best practices:

1. **Be Specific**: Use clear and concise prompts to get targeted insights. For example, instead of asking "What are my journeys?", specify "List all journeys created in the last month."
1. **Combine Insights**: Integrate insights from Audience and Data Insights capabilities for a holistic view of journey performance.
1. **Iterative Refinement**: Use fallout and overlap analysis to iteratively refine journey design and scheduling.

#### Setup best practices

* **Define Clear Objectives**: Before analyzing journeys, establish clear goals (e.g., improving retention, increasing conversions).
* **Monitor Regularly**: Schedule regular reviews of journey performance to identify trends and anomalies.
* **Optimize Segmentation**: Ensure audience segmentation is balanced to avoid fatigue and maximize engagement.

## Loyalty skills {#loyalty-skills}

>[!AVAILABILITY]
>
>Loyalty skills are available in CX Coworker for eligible organizations. Customers with a Loyalty license can access these loyalty skills, even if they do not have an additional CX Coworker license.

Loyalty skills empower loyalty administrators and analysts to create, manage, and analyze loyalty programs using natural language. With these AI-powered skills, you can quickly design engaging loyalty challenges, track performance metrics, and make data-driven decisions to optimize member engagement and program profitability. Whether you're building a new challenge or analyzing loyalty program trends, Loyalty skills streamline the entire loyalty management workflow.

### Loyalty Challenge Management {#loyalty-challenge-management}

Loyalty Challenge Management enables Journey Optimizer users to create and manage loyalty challenges in CX Coworker using natural language prompts. For comprehensive documentation on creating, configuring, and managing loyalty challenges, including detailed setup instructions, refer to the [Loyalty Challenges guide](../loyalty-challenges/get-started.md).

#### Key use cases

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

#### In scope skills

The following capabilities are supported by Loyalty Challenge Management:

* **Challenge creation**: Create challenge configuration from natural language (audience, action criteria, timing, reward, naming).
* **Challenge updates**: Modify challenge details through iterative prompts.
* **Challenge publishing**: Publish supported challenge configurations directly from the conversation.
* **Challenge context visibility**: Retrieve and review challenge information while iterating.

#### Out of scope skills

The following functionalities are currently not supported:

* Challenge deletion
* Loyalty insights and recommendations skills
* Full content authoring automation for challenge messaging in all cases

#### Prompting best practices

1. **Name it**: Give the challenge a clear, memorable title in quotes.
1. **Specify the audience**: Who qualifies (e.g., all members, a tier, a segment, new enrollees, cardholders, subscribers).
1. **Define the action and how much**: What members must do, and the frequency, threshold, or sequence that counts as completion.
1. **Set the time window**: A start date (and end date if fixed-duration) plus the timezone.
1. **State the reward**: Points, miles, statement credits, status extensions, vouchers, or perks granted on completion.
1. **Reference the qualifying event**: Point to the specific SKU, product, account action, or engagement event the challenge tracks.

### Loyalty Agent - Data Insight {#loyalty-data-insight}

Loyalty Agent - Data Insight Skill enables Journey Optimizer users to analyze and query loyalty program performance data using natural language. This skill provides insights into loyalty points, member tiers, redemptions, and revenue metrics, allowing loyalty administrators and analysts to make data-driven decisions about their loyalty programs.

Key use cases :

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

<!--
Feedback from Ivan: Journey simulate is not ready as a skill

## Journey Simulate: Use Cases, Agentic Skills and User Guide

## Overview

>[!BEGINSHADEBOX]

Journey Simulation is available to all Journey Optimizer customers. Journey Simulate, the in-product agentic skill within Journey Simulation, is available to customers that are a part of the Agent Orchestrator Explorer program and requires at least one of the following permissions:

* **Simulate journeys**: Run simulation workflows from the journey canvas.

* **Publish journeys**: Publish journeys, including flows that use simulation before go-live.

* **Approve and Publish journeys**: Approve and publish journeys when your organization uses approval workflows.

To use AI in **[!UICONTROL Simulation]** (**[!UICONTROL Quick simulation]**, generating simulated users with AI, **[!UICONTROL Generate event values]**), users require **[!UICONTROL Generate Content]** permission from the **[!UICONTROL AI Assistant]** capability. 

[Learn more about permissions](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/administration/permissions).

>[!ENDSHADEBOX]

Journey Simulation is a Journey Optimizer feature that enables Journey Optimizer users to safely test and validate marketing journeys before activation. Within Journey Simulation, Journey Simulate is an in-product agentic skill, not a conversational one, that automates and assists the testing process directly from the journey canvas.

Journey Simulate includes three capabilities:

* Generating simulated users
* Generating event values
* Quick simulation. 

Together, they bridge the gap between journey creation and activation, building confidence in journey logic and reducing the risk of post-launch errors.

## Use cases

### Key use cases for Journey Simulate

Journey Simulate offers three capabilities that can be leveraged to reduce testing time and improve journey quality before go-live:

**Generating simulated users**

* Generate simulated users automatically based on journey paths and required attributes.
* Create simulated users that cover all branches and conditions in a journey, including execution addresses (email, push, SMS).
* Update simulated user attributes on demand to refine test scenarios.
* Ensure all journey branches are covered by assigning the right simulated user to each path.

**Generating event values**

* Generate values for events used in a journey to drive test execution through specific paths.
* Define event attribute values that trigger the desired conditions and branches during simulation.

**Quick simulation**

* Start journey simulation and trigger test executions for all simulated users needed to test all paths of a journey, in a single interaction.
* Visualize how simulated users flow through a journey, step by step, including branching paths and conditional logic.
* Identify which simulated user flows through which path, and why, with detailed node-by-node traversal.
* Review simulation reporting at the end of a run in the Journey Optimizer UI to validate outcomes before activation.

## In scope skills and limitations

### **In scope**

The following capabilities are supported by the Journey Simulation feature:

* **Simulated user management**: View, edit, and update simulated user attributes, including execution addresses and personalization data.
* **Simulation control**: Start and stop journey simulation directly through the Journey Simulation in-product experience.
* **Test execution**: Trigger test executions for one or multiple simulated users.
* **Journey flow visualization**: View step-by-step traversal of simulated users through journey nodes, including branching, splits, and user status.
* **Simulation reporting**: View reporting at the end of a simulation run in the Journey Optimizer UI.
* **Multi-user testing**: Run and visualize tests for multiple simulated users simultaneously, covering all journey branches.

In addition to this, the following capabilities are supported by the Journey Simulate skill:

* **Simulated user generation**: Create simulated users based on journey paths, existing test profiles, or specified attributes.
* **Event value generation**: Generate and assign event attribute values to drive test execution through specific journey paths.
* **Quick simulation**: Run a full end-to-end simulation with minimal intervention. The skill automatically generates simulated users, event values, and pre-filled test settings, then executes the journey and surfaces results for review.

### **Limitations**

Simulation may not support every activity, channel, or integration that Test mode or a live journey supports, and behavior may change as the capability matures.

➡️ Learn more about [Simulation limitations](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/simulate-journey/simulate-journey-gs#limitations) in the Journey Optimizer documentation.

-->
