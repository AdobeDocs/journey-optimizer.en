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

### Journeys {#july-26-journeys}

The following capabilities and improvements have been added to journeys in this release.

A **new user interface** has been introduced for the journey canvas, delivering improved performance for large journeys, automatic layout for better readability, and a guided authoring experience.

![](../building-journeys/assets/journey-new-canvas.png)

To switch to the new UI, click the **[!UICONTROL New experience]** button. This setting is saved at the journey level, so the journey reopens in the new experience by default. To revert, click **[!UICONTROL Old experience]**. [Learn more](../building-journeys/using-the-journey-designer.md#canvas-capabilities)

![](../building-journeys/assets/journey-new-experience-switch.png)

Availability date: July 16, 2026

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

* **AJO MCP server new tools** - The [!DNL Adobe Journey Optimizer] MCP server now exposes five additional read-only **channel configuration tools**, enabling you to query channel configurations, supporting resources, and marketing actions directly from your AI assistant. You can now use **List Channel Configurations** (across all AJO channels), **Get Channel Configuration**, **List Configuration Resources**, **Get Configuration Resource**, and **List Marketing Actions**. [Read more](../integrations/ajo-mcp.md#mcp-tools)

  Availability date: July 9, 2026

### Administration {#july-26-administration}

The following improvements have been added to administration and data management in this release.

* **Dataset Time-to-live (TTL) guardrail — existing sandboxes** - The time-to-live (TTL) guardrail for Journey Optimizer system-generated datasets (90 days in the profile store, 13 months in the data lake) will be enforced on **existing customer sandboxes and organizations** starting **October 1, 2026**. [Learn more](../data/datasets-ttl.md#ttl-guardrail)


