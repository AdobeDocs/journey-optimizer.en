---
solution: Journey Optimizer
product: journey optimizer
title: Release notes 
feature: Release Notes
role: User
level: Beginner, Intermediate
description: Adobe Journey Optimizer Release notes 
exl-id: 06fa956a-b500-416e-9d42-b683c328e837
TQID: https://experienceleague.adobe.com/YJKQFYUi8Kw7yZZKm8blcM-1G9uYsqcsEsopH0hOMhA
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a7b2bfc5-be71-4740-b371-76fa6be8df02
    internal-label: Release notes
subfeature_v2:
  - id: eac3bd2c-b027-4dfa-80d2-0bd752ae4794
    internal-label: Product updates
  - id: e437f8db-d1f7-44c0-bdc0-b0a361adc4c0
    internal-label: Pre-release notes
  - id: c4e1378f-bb85-43a2-8b7c-1623ad3b14b5
    internal-label: Documentation updates
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Release notes {#release-notes}

>[!CONTEXTUALHELP]
>id="ajo_homepage_card1"
>title="What's new?"
>abstract="**Adobe Journey Optimizer** continuously delivers new capabilities, enhancements to existing capabilities, and bug fixes. All changes are consolidated on the last week of each month in these release notes."
 
[!DNL Adobe Journey Optimizer] follows a continuous delivery model, allowing Adobe to deliver new capabilities, enhancements, and fixes on an ongoing basis. This approach enables a scalable, phased rollout of capabilities to ensure performance and stability across all environments. Because of this model, release notes are updated between monthly releases. For full details about the release cycle and availability phases, see [Journey Optimizer release cycle](releases.md).

[!DNL Adobe Journey Optimizer] is built natively on [!DNL Adobe Experience Platform] and inherits from its latest innovations and improvements. Learn more about these changes in [Adobe Experience Platform Release Notes](https://experienceleague.adobe.com/docs/experience-platform/release-notes/latest.html){target="_blank"}.

>[!NOTE]
>
>Capabilities listed in these release notes include an **Availability date** indicating when each change becomes accessible in your environment. Entries in the **Coming soon** accordions are expected in the upcoming days or weeks. Information in these sections is subject to change. 

## July '26 release notes {#july-26-updates}

### Loyalty Challenges {#july-26-loyalty}

Journey Optimizer introduces Loyalty Challenges, a new capability in this release.

<table>
<thead>
<tr>
<th><strong>Loyalty Challenges</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Loyalty Challenges turn loyalty initiatives into engaging, gamified experiences that motivate customers to take valuable actions, such as making purchases, writing reviews, or any desired behavior.</p>
<p>Administrators can use the Loyalty admin menu to connect Journey Optimizer with your loyalty ecosystem, including reward fulfillment APIs, event definitions, product inventory, exclusions, and identity settings. Marketers can then design standard, streak, or sequential challenges, define tasks and rewards, deliver branded content cards and messages, and monitor performance with AI-powered reporting dashboards. Journey Optimizer generates the journeys that orchestrate each challenge in the background, so teams can focus on the customer experience and business goals.</p>
<p>Loyalty also introduces Coworker skills that let teams perform key challenge operations more efficiently, including creating challenges, setting challenge properties, managing audiences and related configuration, and reviewing insights to monitor challenge participation and reward performance.</p>
<p>This capability is only available for organizations licensed for Journey Optimizer Loyalty. To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../loyalty-challenges/get-started.md">detailed documentation</a>.</p>
<p> Availability date: July 28, 2026</p>
</td>
</tr>
</tbody>
</table>

### Journeys {#july-26-journeys}

The following capabilities and improvements have been added to journeys in this release.
<table>
<thead>
<tr>
<th><strong>New user interface</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A <b>new user interface</b> has been introduced for the journey canvas, delivering improved performance for large journeys, automatic layout for better readability, and a guided authoring experience.</p>
<p><img src="../building-journeys/assets/journey-new-canvas.png"></p>
<p>To switch to the new UI, click the <b>New experience</b> button. This setting is saved at the journey level, so the journey reopens in the new experience by default. To revert, click <b>Old experience</b>. <a href="../building-journeys/using-the-journey-designer.md#canvas-capabilities">Learn more</a>.</p>
<p><img src="../building-journeys/assets/journey-new-experience-switch.png"></p>
<p> Availability date: July 16, 2026</p>
</td>
</tr>
</tbody>
</table>

* [!BADGE Deprecation]{type=Negative} Batch audiences no longer supported in Audience Qualification node - As of August 3, 2026, Journey Optimizer blocks publication for any journey using a batch audience in an Audience Qualification node. This enforcement replaces the canvas warning introduced in June release. Existing live journeys are not affected. Use a streaming audience in the Audience Qualification node, or switch to a Read Audience activity. [Learn how to migrate your journeys](../building-journeys/aq-batch-audiences-migration.md)

### Orchestrated campaigns {#july-26-oc}

The following capabilities and improvements are coming to orchestrated campaigns in this release.

<table>
<thead>
<tr>
<th><strong>File-based targeting in Orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Orchestrated campaigns now support loading a <strong>CSV or TXT file</strong> directly into the campaign canvas as the targeting audience, without first ingesting the file into Adobe Experience Platform. The file data is consumed at execution time and is not persisted as an Adobe Experience Platform dataset. During file setup, you can define column mappings, data types, NULL handling, and per-column error policies. Rows that fail validation are rejected and logged before the campaign runs, keeping the audience clean without manual pre-processing. This is particularly suited for ad-hoc sends or partner list campaigns where building a full ingestion pipeline is not practical.</p>
<p>For more information, refer to the <a href="../orchestrated/activities/load-file.md">detailed documentation</a>.</p>
<p> Availability date: July, 6 2026</p>
</td>
</tr>
</tbody>
</table>

### Content management {#july-26-content}

The following capabilities and improvements have been added to content management in this release.

* **Quick launch shortcuts in Fragments inventory** - You can now quickly access common actions from the Fragments list using the **[!UICONTROL More actions]** button. Available shortcuts include editing the fragment, opening its details, and discarding the draft version. [Learn more](../content-management/manage-fragments.md#quick-launch-fragments)

  ![](../content-management/assets/fragment-quick-launch.png)

* **Quick launch shortcuts in Templates inventory** - The **[!UICONTROL More actions]** button in the Content Templates list now provides quick access to common actions: editing template details, simulating content, and deleting a template. For email templates, additional shortcuts let you edit the subject line and email body, view or send a proof, run a spam report, and render the email. [Learn more](../content-management/access-content-templates.md#quick-launch-templates)

  ![](../content-management/assets/content-template-quick-launch.png)

### Email channel {#july-26-email}

The following improvements have been added to the email channel in this release.

<table>
<thead>
<tr>
<th><strong>Channel optimization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now configure a journey or campaign action to include multiple outbound channels (Email, Push, SMS) and let Journey Optimizer automatically deliver through the best channel for each customer. Three optimization modes are available:</p>
<ul>
<li>Manual ranking: specify your preferred channel order.</li>
<li>Customer preference: use the customer's preferred channel from their profile (Experience Data Model Consents & Preferences attribute).</li>
<li>AI model-based ranking: use machine learning propensity scores to infer the most effective channel per customer.</li>
</ul>
<p>When the top-ranked channel is unavailable (not opted-in, frequency-capped, or not configured), the system falls back to the next available channel.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p><img src="assets/do-not-localize/channel-optimization.gif"></p>
<p>For more information, refer to the <a href="../building-journeys/channel-optimization.md">detailed documentation</a>.</p>
<p>Availability date: July 22, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Content check in the Email Designer (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now includes automated technical validation directly in the Email Designer, helping you catch HTML and CSS issues before sending.</p>
<p>Checks cover unsupported elements such as <code>&lt;script&gt;</code> and <code>&lt;base&gt;</code> tags, empty divs that can break layout in Microsoft Outlook, HTML meta refresh tags, and CSS or HTML size thresholds that trigger rendering failures in Gmail.</p>
<p>Results are surfaced as errors, warnings, or informational notices directly in the authoring panel, with contextual details and one-click fixes where available, so issues can be resolved without leaving the editor.</p>
<p>Previously available in Limited Availability, this capability is now generally available to all customers.</p>
<p><img src="assets/do-not-localize/content-check.gif"></p>
<p>For more information, refer to the <a href="../email/content-check.md">detailed documentation</a>.</p>
<p>Availability date: July 16, 2026</p>
</td>
</tr>
</tbody>
</table>

### Content & Integrations {#july-26-integration}

The following capabilities and improvements are coming to content management and integrations in this release.

* **Decision items' dynamic custom attributes** - Decision item custom attributes can now be personalized at delivery time using profile, contextual, and audience data. This removes the need to maintain duplicate offers for minor content variations, allowing marketers to manage fewer, more flexible decision items. [Read more](../experience-decisioning/items.md#attributes)

  Availability date: July 27, 2026

* **AJO MCP server new tools** - The [!DNL Adobe Journey Optimizer] MCP server now exposes five additional read-only **channel configuration tools**, enabling you to query channel configurations, supporting resources, and marketing actions directly from your AI assistant. You can now use **List Channel Configurations** (across all AJO channels), **Get Channel Configuration**, **List Configuration Resources**, **Get Configuration Resource**, and **List Marketing Actions**. [Read more](../integrations/ajo-mcp.md#mcp-tools)

  Availability date: July 9, 2026

### Administration {#july-26-administration}

The following improvements have been added to administration and data management in this release.

* **Dataset Time-to-live (TTL) guardrail — existing sandboxes** - The time-to-live (TTL) guardrail for Journey Optimizer system-generated datasets (90 days in the profile store, 13 months in the data lake) will be enforced on **existing customer sandboxes and organizations** starting **October 1, 2026**. [Learn more](../data/datasets-ttl.md#ttl-guardrail)


