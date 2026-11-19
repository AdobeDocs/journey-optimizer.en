---
solution: Journey Optimizer
product: journey optimizer
title: Coworker for Orchestrated campaigns
description: Discover the CX Enterprise Coworker skills available for finding and inspecting Orchestrated campaigns in Adobe Journey Optimizer, with sample prompts.
feature: Campaigns
topic: Artificial Intelligence
role: User
level: Beginner
version: Campaign Orchestration
mini-toc-levels: 1
exl-id: 4e155d9d-4f5d-4acf-af3c-5b0b50e885ef
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b423a773-0a58-4a77-b65d-3dd4ae6ef841
    internal-label: Campaign Orchestration
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---

# Coworker for Orchestrated campaigns {#orchestrated-campaigns-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Explore Coworker capabilities in Adobe Journey Optimizer for finding Orchestrated campaigns and inspecting their details, history, and activity graph.

>[!ENDSHADEBOX]

Coworker brings natural-language tools into Adobe Journey Optimizer to help you find and inspect your Orchestrated campaigns. Use Orchestrated Campaign List to browse, search, and filter your campaigns, Orchestrated Campaign Get to retrieve the details of a single campaign, and Orchestrated Campaign Workflow Renderer to render a workflow graph as a visual diagram. You get live visibility into your campaign data without using the API or navigating the Journey Optimizer UI.

These skills are read-only. Creating or editing Orchestrated campaigns through Coworker is not supported by the current toolset.

Learn more:

* [Coworker skills for Journey Optimizer](../start/ai-features.md#cx-coworker-skills) — overview of Coworker skills across Journeys, Loyalty, Content Management, Decisioning, Channels, and Orchestrated campaigns in Journey Optimizer.
* [Coworker documentation](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/overview){target="_blank"} — overview of Coworker's Campaigns, Chat, and Projects capabilities.
* [Coworker Chat UI guide](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide){target="_blank"} — how to access and navigate Coworker Chat.

## Orchestrated Campaign List {#orchestrated-campaign-list}

Orchestrated Campaign List (`orchestrated-campaign-list`) lets you list, browse, filter, search, count, or get an overview of your Orchestrated campaigns, without asking for the full details, lifecycle history, execution history, or activity graph of a specific campaign. Coworker renders the results as a rich dashboard with metric cards, charts, and a campaign table.

For the details, lifecycle history, execution history, or graph of a single named campaign, use [Orchestrated Campaign Get](#orchestrated-campaign-get).

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>List and browse your Orchestrated campaigns</strong><br>Get an overview of your Orchestrated campaigns, as a dashboard with metric cards, charts, and a campaign table.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"List all my orchestrated campaigns."<br><br>"Browse orchestrated campaigns in the prod sandbox."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Filter and search campaigns</strong><br>Filter or search campaigns, for example by status or by creator.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Show me the LIVE orchestrated campaigns."<br><br>"Filter orchestrated campaigns by status DRAFT."<br><br>"Show orchestrated campaigns created by xavier."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Count campaigns</strong><br>Count the campaigns that match a criterion, such as the channel they use.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"How many orchestrated campaigns use email?"</td></tr>
</table>

### Limitations

* Orchestrated Campaign List does not return the full details, lifecycle history, execution history, or graph of a specific campaign. Use [Orchestrated Campaign Get](#orchestrated-campaign-get) instead.
* Creating or editing Orchestrated campaigns is not supported by the current toolset.
* Orchestrated campaign analytics and performance reporting are not supported.

<!-- TO CONFIRM (PM/dev): required permissions for Orchestrated Campaign List, and availability. -->

## Orchestrated Campaign Get {#orchestrated-campaign-get}

Orchestrated Campaign Get (`orchestrated-campaign-get`) retrieves and presents everything about a specific Orchestrated campaign that you identify by name or ID: its details, status, metadata, lifecycle history, and execution history. It can also visualize the campaign's activity graph. It does one thing: it works on a single, named or identified campaign.

For listing, browsing, or searching multiple campaigns, use [Orchestrated Campaign List](#orchestrated-campaign-list).

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Inspect a campaign</strong><br>Retrieve the details, status, and metadata of a specific campaign, such as who published it.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Show me the details of the Summer Re-engagement orchestrated campaign."<br><br>"Who published the Welcome Series OC?"</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Review the lifecycle history</strong><br>See how a campaign evolved over time.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Show the lifecycle history of my Q3 campaign."</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Check the execution history</strong><br>See how many times a campaign ran and whether it failed.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"How many times did the Holiday Promo orchestrated campaign run?"<br><br>"Did the Cart Abandonment orchestrated campaign fail?"</td></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Visualize the campaign graph</strong><br>Draw or visualize the activity graph of a campaign.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Draw / visualize the graph for the Onboarding OC."</td></tr>
</table>

### Limitations

* Orchestrated Campaign Get works on one campaign at a time. To list or browse multiple campaigns, use [Orchestrated Campaign List](#orchestrated-campaign-list).
* Creating or editing Orchestrated campaigns is not supported by the current toolset.
* Orchestrated campaign analytics and performance reporting are not supported.

<!-- TO CONFIRM (PM/dev): required permissions and availability. Sample prompts are drawn from the skill descriptions; validate them against the skills' actual behavior in Coworker. -->

## Orchestrated Campaign Workflow Renderer {#orchestrated-campaign-workflow-renderer}

Orchestrated Campaign Workflow Renderer renders a workflow or orchestration graph that you supply as a JSON payload, containing `nodes[]` and `edges[]`, as a visual diagram. Use it only when the graph payload is already present in the conversation.

To fetch and draw the graph of an Orchestrated campaign by name or ID, without supplying a graph payload, use [Orchestrated Campaign Get](#orchestrated-campaign-get).

### Key use cases

<table style="table-layout: fixed; width: 100%; border-collapse: collapse; border: 1px solid #d9d9d9;">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<tr><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Use Case</th><th style="padding: 12px; border: 1px solid #d9d9d9; background-color: #f5f5f5; text-align: left; vertical-align: top;">Sample Prompts</th></tr>
<tr><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;"><strong>Render a supplied workflow graph</strong><br>Turn a workflow or orchestration graph payload (JSON with nodes and edges) into a visual diagram.</td><td style="padding: 12px; border: 1px solid #d9d9d9; vertical-align: top;">"Render this workflow graph as a diagram."<br><br>"Visualize this orchestration graph."</td></tr>
</table>

### Limitations

* Orchestrated Campaign Workflow Renderer only renders a graph payload that is already in the conversation. To draw the graph of a campaign by name or ID, use [Orchestrated Campaign Get](#orchestrated-campaign-get).

<!-- TO CONFIRM (PM/dev): skill name as displayed in Coworker, required permissions, availability, and the sample prompts (written from the skill description; validate them in Coworker). -->

{{$include /help/_includes/do-not-localize/orchestrated/ai-augmented-orchestrated-campaigns-coworker-skills.md}}
