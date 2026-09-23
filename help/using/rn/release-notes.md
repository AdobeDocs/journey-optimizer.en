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
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
subfeature_v2:
  - id: a7b2bfc5-be71-4740-b371-76fa6be8df02
    internal-label: Journey Optimizer release notes
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

## September '26 release notes {#sep-26-updates}

### Content Management {#sep-26-content-management}

<table>
<thead>
<tr>
<th><strong>Content Management MCP tools in CX Coworker</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>CX Coworker now has a new set of <strong>Content Management MCP tools</strong>, letting you discover and manage Journey Optimizer content assets through natural language prompts. Ask it to list or retrieve content templates, fragments, landing pages, and journey/campaign inline message content. It can also create content, update templates, and create, update, clone, and publish fragments — plus update inline channel action content directly in journey and campaign.</p>
<p>For more information, refer to the <a href="../content-management/content-management-coworker-skills.md#content-management">detailed documentation</a>.</p>
<p>Availability date: September 3, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Mandatory consent checkbox for landing pages** - You can now make a checkbox mandatory in the landing page form component, requiring visitors to select it (for example, to give consent) before they can submit the form. [Learn more](../landing-pages/lp-content.md#use-form-component)

  Availability date: September 4, 2026 

* **Additional reserved keywords in personalization syntax** - The list of reserved keywords in Profile Query Language (PQL) has been expanded to include general keywords, time units, and boolean/logical operators. If your XDM schema contains a field name that matches one of these keywords, wrap it in backticks to reference it in a personalization expression. [Learn more](../personalization/personalization-syntax.md#reserved-keywords)

  Availability date: September 1, 2026

### Loyalty {#sep-26-loyalty}

<table>
<thead>
<tr>
<th><strong>Loyalty event mapping updates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Creating or editing an Event Mapping now uses a new **visual mapping builder**: select a schema, pick fields from a searchable field selector, map each field to a loyalty event field with per-row connection status, and preview the auto-generated JSONata expression, with the option to switch to manual JSONata editing at any time.</p><p>In addition, "Event Definitions" in Loyalty admin have been renamed to "Event Mappings", with a refreshed list view that shows the human-readable Experience event schema name.</p>
<p>For more information, refer to the <a href="../loyalty-challenges/loyalty-admin.md#event-mappings">detailed documentation</a>.</p>
<p>Availability date: September 22, 2026</p>
</td>
</tr>
</tbody>
</table>

* **"Forever" Loyalty challenges** - Loyalty challenges can now run indefinitely. Set **Challenge end** to **No end date** when configuring the schedule, and the challenge never expires. [Learn more](../loyalty-challenges/create-challenges.md#schedule)

  Availability date: September 1, 2026

* **Loyalty available for Healthcare Shield and Privacy and Security Shield customers** - Journey Optimizer Loyalty is now available to Healthcare Shield and Privacy and Security Shield customers. [Learn more](../loyalty-challenges/get-started.md)

  Availability date: September 15, 2026

+++ Coming soon — **Information below is subject to change.**

* **Per-member Loyalty challenge completion deadlines** - Loyalty challenges now support per-member completion deadlines: choose "Within a number of days after opt-in" under Completion requirements so each member's deadline is calculated from their own opt-in date rather than a fixed program-wide end date. If both a challenge end date and this opt-in window are set, each member's deadline is whichever comes first. <!-- Documentation link: TBD -->

+++

### Journeys {#sep-26-journeys}

<table>
<thead>
<tr>
<th><strong>Journey Simulation in Coworker</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The <strong>Journey Simulation skill</strong> in Coworker automates end-to-end journey validation and lets you easily interpret the results. Note that this feature currently supports only the Quick Simulation flow and does not fully replace the Journey Optimizer manual simulation experience.</p>
<p>For more information, refer to the <a href="../building-journeys/journeys-coworker-skills.md#journey-simulation">detailed documentation</a>.</p>
<p>Availability date: September 23, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey-level holdout (Limited availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now configure a holdout group for your journeys directly from journey properties. A holdout is a configurable percentage of your target audience that is excluded from entering the journey and receives no communication. By comparing holdout profiles against active profiles in Customer Journey Analytics reporting, you can measure the incremental lift - the true impact - that your journey delivers.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative. For full details about the release cycle and availability phases, see <a href="releases.md">Journey Optimizer release cycle</a>.</p>
<p>For more information, refer to the <a href="../building-journeys/journey-properties.md#performance-management">detailed documentation</a>.</p>
<p>Availability date: September 1, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Generate expressions with AI in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The journey advanced expression editor now integrates AI-powered expression generation: describe the expression you want to build in natural language, and the editor generates ready-to-use code you can apply immediately or refine through follow-up prompts.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../building-journeys/expression/generate-expression.md">detailed documentation</a>.</p>
<p>Availability date: September 1, 2026</p>
</td>
</tr>
</tbody>
</table>


* **Support for Jump activities in Audience Qualification journeys** - You can now use Jump activities in journeys that start with an Audience Qualification node to jump to event-based journeys. This capability is being progressively rolled out to organizations. If you don't see this in your environment, it may be because you're still using batch audiences in Audience Qualifications. [Learn more](../building-journeys/jump.md)

  Availability date: September 22, 2026.

* **Trigger after batch audience evaluation** - For recurring journeys that target batch audiences, you can configure a wait window of up to 6 hours for a fresh batch evaluation before the journey runs. If an evaluation is in progress, the journey waits for it to complete; if the latest snapshot was used by the previous run, it waits for a newer batch. If no fresh audience is available by the end of the wait window, that occurrence is skipped. [Learn more](../building-journeys/read-audience.md)

  Availability date: September 18, 2026

* **Decisioning in Journey simulation** - Path Experimentation, as part of the **Optimize** activity, is now supported in Simulation. Routing is handled by Decisioning and is random and non-deterministic per simulated user.

  [Learn more](../building-journeys/simulate-journey-gs.md)

  Availability date: September 15, 2026

* **New Journey Anomaly Detected alert** - A new system alert now warns you when a live journey's daily traffic deviates from its own historical baseline, or drops to zero unexpectedly, across Journey Entries, Journey Exits, and Event Sends. This alert is currently available in production sandboxes only.

  [Learn more](../reports/alerts.md)

  Availability date: September 15, 2026

* **Decisioning in Journey simulation** - You can now simulate journeys that rely on Decisioning, with the following newly supported:

  * Content Decision nodes are now supported in Simulation.
  * The Optimize activity's Targeting rule method is now supported in Simulation.
  * Actions with Adobe Journey Optimizer–decisioned content (e.g., email using a decision policy) are now supported in Simulation.
  * Decision policies using Offer eligibility and ranking by rule, audience, priority, or formula are fully supported. Ranking by AI Model - Personalization is also supported, though returned offers may vary between runs.

  [Learn more](../building-journeys/simulate-journey-gs.md)

  Availability date: September 8, 2026

* **Analyze Journey Anomalies skill** - CX Coworker can now detect unexpected spikes, drops, or flatlines in a journey's entry, exit, or message-send counts against historical baselines using the **Analyze Journey Anomalies** skill. Once a real anomaly is confirmed, the skill runs read-only diagnostics to surface a likely root cause and recommendation. [Learn more](../building-journeys/journeys-coworker-skills.md#journey-analyze)

  Availability date: September 2, 2026

* **New dateDiff function in journey expression editor** - The journey expression editor now includes the `dateDiff` function, which calculates the difference between two dates in number of days. This function is useful for time-based logic such as creating deadlines, calculating customer lifecycle durations, or building countdown timers in journey conditions.  [Learn more](../building-journeys/functions/date-functions.md#dateDiff)

  Availability date: September 1, 2026

+++ Coming soon — **Information below is subject to change.**

<table>
<thead>
<tr>
<th><strong>Content preview in the journey canvas</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Reviewing channel content today requires opening each activity individually, one at a time — slow and error-prone on journeys with many channel activities, especially where personalization means checking multiple treatments or variants per activity. <strong>Content preview</strong> removes that friction by surfacing a content thumbnail for every channel activity directly in the canvas, with a fullscreen modal to inspect and switch between treatments and variants.</p>
<p>Target availability date: September 28, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Hygiene Analysis skill** - CX Coworker can now scan your active and draft journeys for broken configurations, silent failures, and decaying or unused assets — such as stale draft journeys, orphaned data sources, and persistent custom action errors — and surface recommended fixes directly in chat. <!-- Documentation link: TBD -->

+++

### Campaigns {#sep-26-campaigns}

+++ Coming soon — **Information below is subject to change.**

* **Folders for Action Campaigns** - You can now organize your Action Campaigns into folders to improve navigation and management in the interface.

* **Override the default execution fields in Action Campaigns** - Previously available at the journey level, you can now override the default execution fields configured globally for your Email, SMS, and WhatsApp deliveries in the Action Campaign parameters.

+++

### Orchestrated campaigns {#sep-26-orchestrated-campaigns}

<table>
<thead>
<tr>
<th><strong>Alerting for orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Orchestrated campaigns now support <strong>automated alerting</strong> through the same alerting framework used across journeys and campaigns. Alerts are triggered when a campaign execution fails, times out, and each alert includes what happened, when, where, and a direct link to the Canvas to check further details in the logs.</p>
<p>For more information, refer to the <a href="../orchestrated/start-monitor-campaigns.md#alerting">detailed documentation</a>.</p>
<p>Availability date: September 22, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Conditional content with relational data in orchestrated campaigns** - When building conditional content in the Email Designer for orchestrated campaigns, you can now build conditions directly on relational data — such as related records associated with a profile — not just standard profile attributes. [Learn more](../orchestrated/activities/channels.md#add-personalization)

  Availability date: September 22, 2026

### Onboarding {#sep-26-onboarding}

The following improvement is coming to onboarding in this release.

<table>
<thead>
<tr>
<th><strong>Guided capabilities for onboarding emails and journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Guided capabilities for onboarding emails and journeys now include the following improvements:</p>
<ul>
<li>When you migrate an email, [!DNL Journey Optimizer] identifies the content blocks referenced by that email and surfaces them as action items, so you can migrate the content blocks alongside the email.</li>
<li>The interface has been improved to make guided onboarding more intuitive.</li></ul>
<p>For more information, refer to the <a href="../start/onboarding-hub.md">detailed documentation</a>.</p>
<p>Availability date: September 23, 2026</p>
</td>
</tr>
</tbody>
</table>

### Personalization {#sep-26-personalization}

* **Fix syntax with AI** - When a PQL syntax validation error is detected, the Personalization Editor now provides a "Fix with AI" option to help resolve the issue directly from the editor.

  Availability date: September 22, 2026

### Decisioning {#sep-26-decisioning}

* **AEM Content Fragments in Decisioning available for Managed Services customers** - Previously, AEM Content Fragments in Decisioning were available only to customers using **Adobe Experience Manager as a Cloud Service** integration. This capability is now also available to customers using **Adobe Experience Manager Managed Services**. [Learn more](../experience-decisioning/items.md#attributes)

  Availability date: September 23, 2026

* **Support for Adobe Experience Platform profiles in Rule and Ranking formula simulation** - When simulating a Rule or Ranking Formula, you can now select an Adobe Experience Platform profile to automatically fill the attributes of a test-data variant, instead of entering them manually. [Learn more](../experience-decisioning/ranking/ranking-formulas.md#simulate-ranking-formula)

  Availability date: September 22, 2026

+++ Coming soon — **Information below is subject to change.**

<table>
<thead>
<tr>
<th><strong>Decisioning support in Web channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>Decisioning is now available for the Web channel. You can use decision policies directly in the web visual editor to deliver the most relevant offers to each visitor.</p>
<p>For more information, refer to the <a href="../experience-decisioning/use-decision-policy.md">detailed documentation</a>.</p>
<p>Availability date: September 22, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Support for Adobe Experience Platform profiles in Rule and Ranking formula simulation** - When simulating a Rule or Ranking Formula, you can now select an Adobe Experience Platform profile to automatically fill the attributes of a test-data variant, instead of entering them manually. [Learn more](../experience-decisioning/ranking/ranking-formulas.md#simulate-ranking-formula)

  Availability date: September 22, 2026

### Audiences {#sep-26-audiences}

The following reminder applies to audiences in this release.

* **Upcoming change to Audience Composition enrichment audiences** - During the October release (end of October), Journey Optimizer will stop journeys and campaigns that use or reference an Audience Composition audience whose source dataset does not have a **primary identity descriptor**. From that point forward, only Audience Composition audiences built with a primary identity descriptor are supported in journeys and campaigns. If you need these journeys or campaigns to remain active, contact your Adobe representative — our product team can help you migrate. <!-- Documentation link: TBD -->

### Administration {#sep-26-administration}

The following reminder applies to administration in this release.

* **Dataset Time-to-live (TTL) guardrail — existing sandboxes** - The time-to-live (TTL) guardrail for Journey Optimizer system-generated datasets (90 days in the profile store, 13 months in the data lake) will be enforced on existing customer sandboxes and organizations starting October 1, 2026. 

### Usability improvements {#sep-26-usability}

* **AI overview in fragment validation alerts** - The fragment validation alerts dialog now includes an AI overview that summarizes and explains validation issues (for example malformed expressions, missing profile fields, and invalid JSON) so users can troubleshoot faster.

  Availability date: September 22, 2026

* **Easier detach and join branches in the new journey canvas** - You can now detach a branch from the rest of your journey without deleting it, and join it back later at a different point, either by selecting an eligible activity directly on the canvas or by picking it from a list of disconnected or already-used branches. [Learn more](../building-journeys/using-the-journey-designer.md#join-and-detach-branches)

  Availability date: September 1, 2026

