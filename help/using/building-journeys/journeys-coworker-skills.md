---
solution: Journey Optimizer
product: journey optimizer
title: Coworker for journeys
description: Discover the CX Enterprise Coworker skills available for building, generating content for, and analyzing journeys in Adobe Journey Optimizer, with in-depth guidance and sample prompts.
feature: Overview
topic: Artificial Intelligence
role: User
level: Beginner
mini-toc-levels: 1
exl-id: 932218c2-64c1-466e-afc4-120b6d8fe37f
feature_v2:
  - id: baecb07f-ce89-4ebb-9cd9-0f7c053f944f
    internal-label: Journey management
subfeature_v2:
  - id: b15c7c2e-788c-4eb7-86a8-390565b0d2c9
    internal-label: Journey design
---

# Coworker for journeys {#journeys-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Explore Coworker capabilities in Adobe Journey Optimizer for creating journeys, generating channel content, analyzing performance, and simulating journey behavior.

>[!ENDSHADEBOX]

Coworker brings natural-language tools into Adobe Journey Optimizer to help you create and configure journeys, generate channel-specific content, analyze performance, and simulate journey behavior. Use Journey Create to configure flows, Channel Content Create to generate and refine messages, Journey Analyze to investigate performance and operational issues, and Journey Simulation to test journey logic.

Learn more:

* [Coworker skills for Journey Optimizer](../start/ai-features.md#cx-coworker-skills) — overview of Coworker skills across Journeys, Loyalty, Content Management, and Decisioning in Journey Optimizer.
* [Coworker documentation](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/overview){target="_blank"} — overview of Coworker's Campaigns, Chat, and Projects capabilities.
* [Coworker Chat UI guide](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide){target="_blank"} — how to access and navigate Coworker Chat.

## Journey tools {#journey-tools}

<table style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 18%;">
<col style="width: 48%;">
<col style="width: 14%;">
<col style="width: 20%;">
</colgroup>
<tr><th>Use Case</th><th>Description</th><th>Skills</th><th>Sample Prompts</th></tr>
<tr><td>Compare journey versions</td><td>Compare any two journey versions in Coworker Chat. Review a structured diff of added, removed, modified, and moved nodes with field-level details. Identify changed connections, journey-level property changes, and roll-up counts without opening Journey Optimizer. For more details on how to manage journey versions, see <a href="publish-journey.md#journey-versions">Journey versions</a>.</td><td>Journey Version Comparison</td><td>"What changed between version 1.0 and 2.0 of the 'Welcome Series' journey?"<br><br>"Has the wait duration of my wait activity changed between the last two journey versions?"</td></tr>
</table>

## Journey Create {#journey-create}

Journey Create enables Journey Optimizer users to build and configure marketing journeys using a natural language interface. With Journey Create, practitioners can quickly create journeys by describing their requirements in conversational prompts. The skill walks users through the different options for creating a journey, allowing marketers to focus on strategy rather than technical configuration.

>[!AVAILABILITY]
>
>You need the following permissions in order to fully use Journey Create features:
>
>**Manage Journeys**: This permission lets you create new journeys directly in Coworker.
>
>**View Journey Events, Data Sources and Actions**: This permission ensures that Coworker can search through Journey Events and Custom Actions. 
>
>**View Segments**: This permission ensures that Coworker can search for audience segments when creating a Journey.
>
>**Manage Segments**: This permission lets you create new audiences directly in Coworker.

### Key use cases

Journey Create offers capabilities that can be leveraged to accelerate marketing execution:

<table style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 18%">
<col style="width: 48%">
<col style="width: 14%">
<col style="width: 20%">
</colgroup>
<tr><th>Use Case</th><th>Description</th><th>Skills</th><th>Sample Prompts</th></tr>
<tr><td>Event-triggered journey creation</td><td>Create journeys that activate based on specific customer events. Design automated responses to customer actions in real-time. Build personalized communication flows based on customer behavior.</td><td>Journey Create</td><td><strong>Store visit journey:</strong> Create a journey that starts when a user enters my store location. Send a push notification to welcome users to the store. Wait 2 days and check to see if the user has a valid email address. If the user has a valid email address, send an email survey to ask about their store experience. If the user does not have a valid email address, send a push notification to prompt for registration.<br><br><strong>Post-purchase journey:</strong> Create a journey that starts when a customer makes a purchase online. Send a push notification to thank them for their purchase. Next, check to see if they are loyalty members. If the user is a loyalty rewards member, send a second push notification with a 10% discount code. If the user is not a loyalty rewards member, send a push inviting them to sign up for the loyalty program. Wait 2 days and send a follow-up push with a survey about their purchase experience.<br><br><strong>Event-based promotion:</strong> Create a journey triggered when the game score reaches 50. Send an SMS message to loyalty reward members saying that they are eligible for a free slice of pizza from the partner sponsor.</td></tr>
<tr><td>Audience-targeted journey creation</td><td>Build journeys targeting specific audience segments. Design multi-step communication sequences with strategic timing.</td><td>Journey Create</td><td><strong>Seasonal campaign:</strong> I want to create a journey targeting an audience of day hikers. I want to send an email alerting this audience to my upcoming holiday sale that includes a variety of hiking essentials. Wait 3 days after sending the first email and send a second email that has a 15% coupon with free shipping. Wait 1 week and then send a 3rd email message to show our new sleeping bag and tent collection. Schedule the journey to start on 12/20.<br><br><strong>Loyalty appreciation:</strong> Build a loyalty appreciation journey for SUV owners, including a thank you push notification with a free carwash offer and a follow-up push notification reminder if the first notification is not interacted with within 1 day.</td></tr>
<tr><td>Business-event triggered journey creation</td><td>Create journeys that activate based on a particular business event and target a specified audience (e.g. product back in stock or game score change). Trigger timely, context-aware messages when business conditions change.</td><td>Journey Create</td><td>Create a journey that sends a message when a product is back in stock for a selected audience.<br><br>Build a journey that sends a follow-up when a player's game score changes.</td></tr>
<tr><td>Audience qualification journey creation</td><td>Create journeys that activate as profiles enter or exit an audience segment definition. Automate entry and exit messaging to support onboarding, retention, and win-back goals.</td><td>Journey Create</td><td>Create a welcome journey for profiles as they enter the New Customers audience.<br><br>Build a win-back journey that starts when a profile exits the Active Customers audience.</td></tr>
<tr><td>Conditional journey flows</td><td>Create decision branches based on customer attributes. Design split paths that adapt to customer preferences.</td><td>Journey Create</td><td>Add a conditional split to send a different message to customers based on their preferred channel.<br><br>Branch this journey based on each customer's loyalty tier.</td></tr>
<tr><td>Create journey from image</td><td>Upload a reference image into Coworker and ask to create a journey using the image as reference. Journey creation skill extracts an editable prompt from your reference image.</td><td>Journey Create</td><td>Create a journey from this uploaded journey flowchart image.</td></tr>
</table>


With this skill, natural language requirements are translated into structured journey configurations.

### Prompting best practices

To maximize the effectiveness of Journey Create, follow these best practices:

* **Be Specific**: Provide clear details about your journey goals, target audience, and desired actions. Include information about channels, timing, and conditions.
* **Specify Timing**: Clearly indicate wait periods between actions and when the journey should start.
* **Define Conditions**: When using conditional logic, explain the criteria for each branch path.
* **Include Channels**: Specify which communication channels you want to use (push, email, SMS).
* **Mention Scheduling**: For scheduled journeys, provide the desired start date and time.
* **Custom Actions**: If you are using custom actions in your workflow you need to specify that you are using a custom action along with the exact name of the custom action. Example:
   When a user enters my store location send a welcome message using custom action ExternalPush. Wait 2 days and then send a follow up message using custom action ExternalEmail with a survey on their visit.
* **Validate Expressions**: Make sure to check and validate any expressions that Journey Skills create to ensure that the correct fields and values are used.

### Out of scope skills

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

### Setup best practices

* **Define Clear Objectives**: Before creating journeys, establish clear goals (improving retention, driving conversions, increasing engagement).
* **Prepare Audiences**: Ensure your target audiences are already created and properly segmented.
* **Plan Message Content**: Have your messaging strategy defined before journey creation.
* **Consider Customer Experience**: Design journey flows that respect customer preferences and avoid over-communication.

## Channel Content Create {#channel-content-create}

>[!AVAILABILITY]
>
>This feature is available for all customers in Limited Availability. Contact your Adobe representative to gain access.

Channel Content Create enables Journey Optimizer users to generate, edit, and manage channel-specific content for journeys using AI-powered content generation.

### Key use cases

<table style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 18%">
<col style="width: 48%">
<col style="width: 14%">
<col style="width: 20%">
</colgroup>
<tr><th>Use Case</th><th>Description</th><th>Skills</th><th>Sample Prompts</th></tr>
<tr><td>Channel-specific content generation</td><td>Generate content for email, push notifications, SMS, and other channels using natural language prompts.</td><td>Channel Content Create</td><td>"Generate email content for my welcome journey. Create a welcome email for new customers with a friendly tone and include a 10% discount offer."<br><br>"Generate a push notification for my store visit journey. Create a welcome message that encourages customers to check in and receive a special offer."<br><br>"Generate SMS content for my event-triggered journey. Create a short message notifying customers about a flash sale with a call-to-action."</td></tr>
<tr><td>Template-based content creation</td><td>Browse and select from available templates with preview capabilities.</td><td>Channel Content Create</td><td>"Show me available email templates for my seasonal campaign journey."<br><br>"Select a template for my email that has a modern, clean design."</td></tr>
<tr><td>Multi-channel content management</td><td>Generate and manage content for multiple channels within the same journey workflow.</td><td>Channel Content Create</td><td>"Create email and SMS content for the welcome journey, tailored to new customers."<br><br>"Generate coordinated email, push, and SMS content for my event-triggered journey."</td></tr>
<tr><td>In-context content editing</td><td>Open generated content in Content Designer for editing and refinement.</td><td>Channel Content Create</td><td>"Open the email content in Content Designer so I can customize the design."</td></tr>
<tr><td>Content refinement and iteration</td><td>Regenerate content with different tones or styles using the Regenerate action.</td><td>Channel Content Create</td><td>"Regenerate the push notification content with a more casual tone."<br><br>"Update the email content to include a promotional code."</td></tr>
<tr><td>Journey canvas integration</td><td>Select journeys from inventory and view associated channels.</td><td>Channel Content Create</td><td>"Show me the channels used in my Welcome journey."<br><br>"Select the Spring Sale journey and show its associated channels."</td></tr>
</table>

### Prompting best practices

* **Be Specific**: Provide clear details about the content type, tone, target audience, and key messaging.
* **Specify Channel**: Clearly indicate which channel you are creating content for (email, push, SMS).
* **Define Tone**: Specify the desired tone (friendly, formal, casual, urgent).
* **Iterate and Refine**: Use the regenerate action to refine content until it meets your requirements.

## Journey Analyze {#journey-analyze}

Journey Skills will enable Journey Optimizer users to analyze and optimize journeys using a natural language interface. With Journey Skills, practitioners can quickly identify and resolve schedule and/or audience conflicts, detect points of user abandonment in a journey and provide insights or recommendations. It empowers practitioners to make data-driven decisions, improve customer engagement, and streamline journey orchestration.

>[!AVAILABILITY]
>
>Journey Skills are available for all customers who have access to Coworker. However, you will need the following permissions in order to fully use the Journey Skills features:
>
>**View Journeys**: This permission lets you view insights into the journey directly in Coworker.
>
>**Manage Journeys**: This permission lets you create new journeys directly in Coworker.
>
>**View Segments**: This permission lets you view insights into the audiences directly in Coworker.
>
>**Manage Segments**: This permission lets you create new audiences directly in Coworker.

### Key use cases

Journey Analyze offers a range of functionalities that can be leveraged to optimize marketing efforts:

<table style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 18%">
<col style="width: 48%">
<col style="width: 14%">
<col style="width: 20%">
</colgroup>
<tr><th>Use Case</th><th>Description</th><th>Skills</th><th>Sample Prompts</th></tr>
<tr><td>Journey Fallout Analysis</td><td>Identify where and why customers drop off during a journey. Detect patterns in customer behavior leading to disengagement. Use insights to refine journey design and improve retention.</td><td>Journey Analyze</td><td>"I want to analyze the fallout by node for journey Fourth of July Campaign."<br><br>"Perform a fallout analysis for journey Fourth of July Campaign."<br><br>"What is profile loss over the course of journey Fourth of July Campaign?"<br><br>"Show where users are dropping off in journey Fourth of July Campaign."</td></tr>
<tr><td>Journey Audience Overlap Analysis</td><td>Analyze audience overlap across multiple journeys. Prevent audience fatigue caused by over-targeting. Optimize segmentation to ensure balanced engagement.</td><td>Journey Analyze</td><td>"Which audiences are used in more than X journeys?"<br><br>"List all journeys using the [audience name] audience."<br><br>"Show me audience overlap conflicts for journey [Journey Name]."<br><br>"Show overlapping audiences for journey [Journey Name] and other journeys."</td></tr>
<tr><td>Journey Schedule Overlap Analysis</td><td>Detect timing conflicts between scheduled journeys targeting the same audience. Avoid over-communication and improve scheduling efficiency. Maximize audience impact by ensuring journeys run at optimal times.</td><td>Journey Analyze</td><td>"Are there any scheduling conflicts for journey [Journey Name]?"<br><br>"Check for scheduling conflicts involving journey [Journey Name]."<br><br>"Highlight scheduling overlaps between journey [Journey Name] and live journeys."<br><br>"Is journey [Journey Name] running in conflict with any other journey?"</td></tr>
<tr><td>Operational insights</td><td>Prompt-based Journey Insights – Surface operational insights about journeys , i.e. "show me all live journeys."</td><td>Journey Analyze</td><td>"When was [Journey Name] published?"<br><br>"When was [Journey Name] stopped?"<br><br>"List all journeys currently in test mode"<br><br>"How many live journeys do I have?"<br><br>"Give me a list of all scheduled recurring journeys and their expected run times."</td></tr>
<tr><td>Journey Custom Action Error Analysis</td><td>Identify when custom actions are failing or error rates spike within a journey. Diagnose root causes before failures cascade into broader journey disruption. Use specific remediation steps to restore custom action reliability quickly.</td><td>Journey Analyze</td><td>"Why are custom actions failing in journey [Journey Name]?"<br><br>"What is the error rate for custom action [Custom Action Name] in journey [Journey Name]?"<br><br>"Show me the root cause of custom action failures in journey [Journey Name]."<br><br>"Are there any custom action errors affecting journey [Journey Name] right now?"</td></tr>
<tr><td>Analyze Journey Anomalies</td><td>Detect unexpected spikes, drops, or flatlines in a journey's entry, exit, or message-send counts compared to historical baselines, including when the question is phrased around the number of profiles entering, exiting, or completing the journey. Confirm whether a flagged change is a genuine anomaly using a deterministic statistical check, rather than relying on the raw anomaly flag alone. Run bounded, read-only diagnostics against journey-execution data to identify a likely root cause, surfacing what each check looked for and found alongside the recommendation. Investigate anomaly alerts that reference a specific journey version and timestamp.</td><td>Journey Analyze</td><td>"Why did entries drop for my Welcome journey yesterday?"<br><br>"Did exits spike for the Cart Abandonment journey this week?"<br><br>"Sends look low for the Renewal Reminder journey today — what happened?"<br><br>"Why was there a sudden drop in the number of profiles entering my Member Anniversary Thank You journey in the last 30 days?"<br><br>"Fewer profiles than usual are completing my Renewal Reminder journey this month — why?"<br><br>"An anomaly alert was triggered for journey [Journey Version ID] at [timestamp] — investigate."</td></tr>
<tr><td>Business Performance Analysis</td><td>Analyze journey performance and identify concrete optimization opportunities for underperforming journeys. Surface trends, bottlenecks, and likely drivers behind lower results so you can improve engagement and conversion. Get actionable recommendations to adjust journey design, targeting, or messaging strategy based on business performance insights.</td><td>Journey Analyze</td><td>"Analyze the performance of journey [Journey Name] and recommend optimizations."<br><br>"Why is journey [Journey Name] underperforming compared with last month?"<br><br>"What should I change to improve the performance of journey [Journey Name]?"<br><br>"Which parts of journey [Journey Name] are likely limiting conversion or engagement?"</td></tr>
</table>

### Prompting best practices

To maximize the effectiveness of Journey Analyze, follow these best practices:

* **Be Specific**: Use clear and concise prompts to get targeted insights. For example, instead of asking "What are my journeys?", specify "List all journeys created in the last month."
* **Combine Insights**: Integrate insights from Audience and Data Insights capabilities for a holistic view of journey performance.
* **Iterative Refinement**: Use fallout and overlap analysis to iteratively refine journey design and scheduling.

### Setup best practices

* **Define Clear Objectives**: Before analyzing journeys, establish clear goals (e.g., improving retention, increasing conversions).
* **Monitor Regularly**: Schedule regular reviews of journey performance to identify trends and anomalies.
* **Optimize Segmentation**: Ensure audience segmentation is balanced to avoid fatigue and maximize engagement.

## Journey Simulation {#journey-simulation}

Journey Simulation skill brings AI-driven Quick Simulation into the chat interface, letting users validate a journey's logic conversationally. Through Coworker, users can generate simulated test data, run and manage a simulation, and review the results.

### Key use cases

<table style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 18%">
<col style="width: 48%">
<col style="width: 14%">
<col style="width: 20%">
</colgroup>
<tr><th>Use Case</th><th>Description</th><th>Skills</th><th>Sample Prompts</th></tr>
<tr><td>Run a quick simulation</td><td>Start a quick simulation, generating the minimum simulated users and event data needed so that each path is tested. Check the status of a simulation run. List the simulated users included in a run. Retrieve run logs.</td><td>Journey Simulation</td><td>"Simulate my onboarding journey"</td></tr>
<tr><td>Review simulation results</td><td>Return detailed results, including step-by-step path traversal. Return branch outcomes for the simulated run.</td><td>Journey Simulation</td><td>"Can you summarise this simulation run?"<br><br>"What are the results of this simulation"</td></tr>
</table>

### Limitations

This feature currently only supports the Quick Simulation flow, and does not fully replace the Journey Optimizer manual simulation experience. Use Quick Simulation for a fast, automated sanity check of a journey's logic. For granular control over simulated users and scenarios, use the [manual simulation experience in Journey Optimizer](simulate-journey-gs.md).

As part of this Quick Simulation experience, users cannot:

* Choose an existing saved simulated user for a run.
* Edit a simulated user before rerunning a simulation.
* Create, browse, update, or delete persistent simulated users through chat.
* Target a specific path or custom test case.


{{$include /help/_includes/do-not-localize/start/ai-augmented-journeys-coworker-skills.md}}
