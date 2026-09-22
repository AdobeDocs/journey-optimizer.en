---
solution: Journey Optimizer
product: journey optimizer
title: Pre release notes for Journey Optimizer
description: Adobe Journey Optimizer Pre Release notes
feature: Release Notes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
TQID: https://experienceleague.adobe.com/951PJzmmITN1nSUapVomlYnPws9pS0TosI1Gl3R9yL4
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
subfeature_v2:
  - id: a7b2bfc5-be71-4740-b371-76fa6be8df02
    internal-label: Journey Optimizer release notes
---

# Pre-release notes {#e-release-notes}

Adobe Journey Optimizer continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md).

## September '26 pre-release notes {#sep-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production. While most changes are delivered on the release date, a few may roll out later — refer to the Availability Date listed for each entry for details.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: September 22-23, 2026

>[!BEGINSHADEBOX]

**New in CX Enterprise Coworker this month**

This release brings several new and improved [Coworker](../start/ai-features.md#cx-coworker) features and skills, listed here for visibility. Each one is also detailed in its relevant section below.

* [CE Channel Content plugin](#sep-26-content-management) - A new plugin that brings campaign copy, image, and email HTML skills together in Coworker, from campaign brief to production-ready copy and HTML.
* [Loyalty recommendation skill](#sep-26-loyalty) - Request challenge opportunities directly in Coworker's conversational interface and turn them into live challenges without leaving the chat.
* [Journey Simulation](#sep-26-journeys) - Automate end-to-end journey validation and interpret the results directly in Coworker.
* [Journey creation from the Coworker rail](#sep-26-journeys) - Generate journeys with AI directly from the Coworker right rail, replacing the previous AI Assistant experience.
* [Compare journey versions](#sep-26-journeys) - Get a full-fidelity, structured diff between any two versions of a journey through Coworker Chat.
* [Hygiene Analysis skill](#sep-26-journeys) - Scan active and draft journeys for broken configurations, silent failures, and decaying or unused assets, with recommended fixes.
* [Business Performance Analysis skill](#sep-26-journeys) - Analyze journey performance and get concrete optimization recommendations, right from the chat.

>[!ENDSHADEBOX]

### Content Management {#sep-26-content-management}

The following capability is coming to content management in this release.

<table>
<thead>
<tr>
<th><strong>Channel Content plugin in Coworker</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Channel Content</strong> plugin is now available in Coworker, bringing campaign copy, image, and assembled email HTML skills together under one plugin from strategy to deployment. The following skills are available under the **Channel Content** plugin:</p>
<ul>
<li><strong>Orchestrate Content Authoring</strong>.</li>
<li><strong>Explore Content Strategy</strong></li>
<li><strong>Content Brief</strong></li>
<li><strong>Generate Content</strong></li>
<li><strong>Check Content Readiness</strong></li>
<li><strong>Revise and Regenerate Content</strong></li>
<li><strong>Generate Image</strong></li>
<li><strong>Assess Content Design</strong></li>
<li><strong>Save Channel Content</strong></li>
<li><strong>Build Email from Figma</strong></li>
<li><strong>Brand Lookup</strong> </li>
</ul>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

### Integrations {#sep-26-integrations}

The following capability is coming to integrations in this release.

* **Dynamic token substitution for Experience Manager fragments** - Experience Manager Content Fragment references now support a **tokenSubstitution** attribute. When set to `false`, personalization inside the fragment's fields resolves directly, without a token map in the reference. It defaults to `true`, which keeps the existing behavior.

  This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative. 

### Loyalty {#sep-26-loyalty}

The following capability and improvement are coming to Loyalty in this release.

<table>
<thead>
<tr>
<th><strong>Challenge Opportunities</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Loyalty Performance menu now includes an <strong>Opportunities tab</strong>, which surfaces AI-detected trends and gaps such as tier progression friction or challenge task drop-off, each with a projected impact and a one-click "Create with AI" action to generate a challenge that addresses it.</p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

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
</td>
</tr>
</tbody>
</table>

* **Coworker loyalty recommendation skill** - Marketers can now request **challenge opportunities** directly in Coworker's conversational interface, getting grounded challenge ideas based on real loyalty program trends and turning them into live challenges without leaving the chat. 

* **Challenges domain in the Content Card personalization editor** - The Content Card personalization editor now supports **Challenges** as a domain, letting you access challenge metadata when authoring content card personalization. This makes it easier to create tailored content for each stage of a challenge — Launch, In progress, and End — without custom code.  



### Onboarding {#sep-26-onboarding}

The following capability is coming to onboarding in this release.

<table>
<thead>
<tr>
<th><strong>Guided capabilities for onboarding emails and journeys (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Transitioning to Adobe Journey Optimizer from another marketing platform is easier with guided capabilities that help you move existing email content and journeys into Journey Optimizer. A <strong>dedicated workspace</strong> lets you reuse what you have instead of rebuilding from scratch.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
</td>
</tr>
</tbody>
</table>

### Audiences {#sep-26-audiences}

The following reminder applies to audiences in this release.

* **Upcoming change to Audience Composition enrichment audiences** - During the October release (end of October), Journey Optimizer will stop journeys and campaigns that use or reference an Audience Composition audience whose source dataset does not have a **primary identity descriptor**. From that point forward, only Audience Composition audiences built with a primary identity descriptor are supported in journeys and campaigns. If you need these journeys or campaigns to remain active, contact your Adobe representative — our product team can help you migrate. <!-- Documentation link: TBD -->

### Journeys {#sep-26-journeys}

The following capabilities and improvements are coming to journeys in this release.

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
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey creation from Coworker rail</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Journey creation with AI</strong> is now available directly from the Coworker right rail, replacing the previous AI Assistant experience with a re-branded, integrated entry point for generating journeys.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>AI recommendation cards for journey alerts</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Journey Optimizer home page now surfaces an <strong>AI recommendation card</strong> when a journey alert fires, covering <strong>Journey Custom Action failure</strong> and <strong>Journey Anomaly Detected</strong> alerts. Selecting the card opens the journey with the right rail pre-populated with the analysis already performed.</p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Inbound Activity Deactivation journey activity</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Inbound Activity Deactivation</strong> activity in the journey canvas lets you remove a profile from up to five inbound activities or experiences directly from a journey, decoupling inbound disqualification from journey exit for more advanced cross-channel orchestration.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Content preview in the journey canvas</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Reviewing channel content today requires opening each node individually, one at a time - slow and error-prone on journeys with many channel nodes, especially where personalization means checking multiple treatments or variants per node. <strong>Content preview</strong> removes that friction by surfacing a content thumbnail for every channel node directly in the canvas, with a fullscreen modal to inspect and switch between treatments and variants.</p>
</td>
</tr>
</tbody>
</table>

* **Supplemental ID support in Journey simulation** - **Supplemental ID** is now supported in Journey simulation, allowing you to test complex user scenarios for both read-audience and event-triggered journeys. 

* **Jump support for Audience Qualification journeys** - Journeys that start with an **Audience Qualification** can now use a **Jump** activity to enter an event-based start journey; jumping to an Audience Qualification-based journey remains unsupported.

* **Compare journey versions with Coworker** - Today, reviewing what changed between two versions of a journey requires manually comparing them inside Journey Optimizer node by node - there's no structured diff, which makes change-review, audit, and pre-publish checks slow and error-prone, especially as journeys grow more complex. This capability lets a customer or AI agent compare any two versions of a journey through Coworker Chat and get back a full-fidelity, **structured diff** - added/removed/modified/moved nodes with field-level detail, changed connections, journey-level property changes, and roll-up counts - without opening Journey Optimizer. 

* **Reduced step events for wait and event activities** - Step events are no longer generated for **wait** activities and **event** activities when the profile was not actually processed at that activity. <!-- DRAFT: pending DOCAC sub-task under DOCAC-15691, see CJM-165835 -->
<!-- Documentation link: TBD -->

* **Dry run step-event suppression for custom reports** - As part of step-event optimization, Journey Optimizer now stops generating certain non-reportable step events during Journey Dry Runs. This only affects custom reports built on these dry-run step-event types. If you're impacted, re-trigger the dry run to regenerate data.

* **Hygiene Analysis Coworker skill** - A new Hygiene Analysis skill in Coworker scans your active and draft journeys for broken configurations, silent failures, and decaying or unused assets — such as stale draft journeys, orphaned data sources, and persistent custom action errors — and surfaces recommended fixes, right from the chat. <!-- Documentation link: TBD -->

* **Business Performance Analysis Coworker skill** - A new **Business Performance Analysis** skill in Coworker analyzes how your journeys are performing, explains areas of lower performance, and recommends concrete optimizations, like re-engagement waits, channel escalation, and Send Time Optimization.  <!-- Documentation link: TBD -->

* **Automatic event recovery timeout in Journey Properties** - Journey Properties now includes a **Set event recovery timeout** setting: by default, impacted journey events are automatically replayed for up to 72 hours after a service interruption with no action needed. You can turn this setting on to control the replay window (0–72 hours) for time-sensitive journeys. The existing **Timeout or error** field has also been renamed to **Custom Action / IDS Action timeout** to avoid confusion between the two settings. 

### Channels {#sep-26-channels}

The following capabilities and improvements are coming to channels in this release.

<table>
<thead>
<tr>
<th><strong>Live Activities for Android Live Updates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now expands its real-time mobile personalization capabilities by extending <strong>Live Activity support to Android</strong>. You can deliver real-time progress updates directly to users, such as order tracking, flight statuses, live event updates, and real-time sports scores.</p>
<p>Beyond supporting iOS Live Activities, Journey Optimizer now manages temporary push tokens for Android Live Updates across its platform configurations. It supports both broadcast and transactional update flows using API-triggered campaigns and headless APIs.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Custom outbound channel (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Custom outbound channels</strong> let administrators bring any outbound HTTP-based messaging channel — such as WeChat, Kakao Talk, Messenger, or a proprietary provider — directly into Journey Optimizer through a no-code Channel Builder. Once configured, custom channels are available across campaigns, journeys, and orchestrated campaigns, with the same full set of capabilities as native channels: personalization with the expression editor, content experimentation, preview and proof, out-of-the-box reporting, and consent and governance enforcement.</p>
<p>With this release, custom outbound channels also gain several new capabilities:</p>
<ul>
<li>Use Journey Optimizer Decisioning in the custom channel payload through the Personalization Editor, the same way as in code-based experiences.</li>
<li>Apply business rules to custom channels, the same way you already can on native channels.</li>
<li>Select custom channels in the channel list for API-triggered campaigns, which was not previously possible.</li>
<li>Define a reporting webhook for a custom channel and attach it to a channel configuration, so you can enrich your Journey Optimizer reports with interaction events.</li>
</ul>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Android push notifications templates improvements</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Android push notifications previously rendered with a single, fixed layout: images were always center-cropped, and long body text was truncated. This release introduces a template picker at authoring time, allowing marketers to control the layout of Android push notifications.</p>
<p>Following improvements are available:</p>
<ul>
<li><b>Layout selection</b>: New Push Notification Layout picker (Standard / Expanded) when authoring an Android push.</li>
<li><b>Standard layout with "Show entire image"</b>: Choose cropped-to-fill vs. scaled-to-fit.</li>
<li><b>Expanded layout</b>: Multi-line body text with no truncation, plus optional large-icon thumbnail.</li>
<li><b>Collapsed body (Expanded layout)</b>: Set a separate, shorter body text for the collapsed state.</li>
</ul>
</td>
</tr>
</tbody>
</table>


* **Custom SMS BYOP auth flexibility** - You can now configure **custom authentication headers** when connecting your SMS provider's OAuth setup, including where the token is placed on outgoing messages and how the token request itself is formatted.

* **Direct mail - Split large files automatically** - Direct Mail files can now be split into multiple parts automatically when they exceed roughly 20 GB, or manually by choosing a target file size in the file routing configuration.

* **Direct mail - Increased audience limit** - The Direct Mail channel audience limit has been increased from 3 million to 100 million profiles, letting you target much larger audiences without hitting file-creation errors.

### Email channel {#sep-26-email-channel}

The following capabilities and improvements are coming to the Email channel in this release.

<table>
<thead>
<tr>
<th><strong>Override email channel configuration settings</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>When building your journeys and campaigns, you can now override the email parameters derived from the selected channel configuration directly at the journey or campaign action level.</p>
<p>This lets you personalize the email header fields (<strong>From name</strong>, <strong>From email prefix</strong>, <strong>Reply to name</strong>, and <strong>Reply to email</strong>), the execution address, and the list-unsubscribe values, using profile attributes or contextual data for more precise control. In particular, this allows sender details to reflect the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address.</p>
</td>
</tr>
</tbody>
</table>

* **Suppression list override at email action level** - You can now override local suppression-list behavior at the email action level, so operational or compliance-critical communications can still be sent through a dedicated configuration when needed. Global suppression-list behavior remains unchanged.

* **URL syntax validation in email authoring** - Journey Optimizer now validates URLs earlier in the email authoring flow and surfaces clearer guidance when malformed syntax is detected. This helps authors catch issues before finalization, reduce publishing errors, and improve delivery confidence.

### Email Designer {#sep-26-email-designer}

The following capabilities and improvements are coming to the Email Designer in this release.

<table>
<thead>
<tr>
<th><strong>Dark mode support for email theme variants</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Email themes now support dark mode, so each color variant can render with a look tailored to recipients viewing your email in a dark mode-enabled client.</p>
<p>When enabled, a default dark palette is generated automatically for every variant, and you can further customize it with a different palette or your own custom colors — independently from the light mode design, so changes made in one mode do not affect the other.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Import Dynamic Media templates directly from PSD files in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Email Designer's Dynamic Media component now lets you import a Photoshop (PSD) file directly as a new template, in addition to browsing existing Dynamic Media templates. Drag and drop a PSD file into the component, and Adobe Journey Optimizer automatically converts it into a Dynamic Media template stored in Dynamic Media — no manual conversion or round-trip through Adobe Experience Manager needed. Once imported, you edit the template using the built-in Dynamic Media editor, the same experience used for Adobe Express content in the Email Designer.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>New table component in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Email Designer now includes a built-in <strong>Table component</strong>, allowing you to structure content in rows and columns directly within your email. Drag and drop the component onto your canvas, customize the number of rows and columns, and style each cell independently to create clear, organized layouts without relying on custom HTML.</p>
</td>
</tr>
</tbody>
</table>

* **Fallback fonts for custom fonts in email themes** - You can now define a fallback font for any custom (web) font applied through email themes. If a subscriber's email client does not support the custom font, Adobe Journey Optimizer automatically displays the specified fallback font instead of leaving the choice to the email client's default. This keeps email typography closer to your brand guidelines and reduces font-rendering inconsistencies across email clients.

### Orchestrated campaigns {#sep-26-oc}

The following capabilities and improvements are coming to orchestrated campaigns in this release.

<table>
<thead>
<tr>
<th><strong>OR join activity for orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The <strong>Join activity</strong> in orchestrated campaigns now supports both AND and OR join conditions. With OR logic, a profile that completes any one upstream branch, rather than all of them, continues along a single shared downstream path. This makes it possible to model "if A or B or C, then do this" patterns directly on the canvas without duplicating downstream steps across separate branches.</p>
</td>
</tr>
</tbody>
</table>

* **LINE channel for orchestrated campaigns** - LINE is now available as a native outbound channel in orchestrated campaigns, alongside email, SMS, and push. You can build and deliver LINE messages directly from the campaign canvas, including text, stickers, images, videos, location data, and Flex Messages, supporting promotional, transactional, and ongoing engagement use cases in LINE-dominant markets such as Japan and APAC. Previously released in Limited Availability, this capability is now generally available. 

* **New Orchestrated Campaigns monitoring APIs** - New **API specifications** are now available for orchestrated campaigns, allowing you to programmatically create, manage, and trigger orchestrated campaigns, enabling deeper integration with external systems and automation pipelines.

* **Direct join UX improvements** - When adding an attribute from a related collection, you can now choose between three join modes — a new default that warns you about potential performance impact from cartesian products, plus the existing Aggregate and Advanced modes — making it easier to understand the tradeoffs of your query before you build it. 

* **Campaign Orchestration monitoring** — A new user interface is now available for tracking the ingestion status and freshness of relational store data used by Orchestrated Campaign Segmentation. It gives you direct visibility into the health of the data feeding your batch audiences. A new Campaign Orchestration tab in the Adobe Experience Platform's Monitoring dashboard surfaces the health of relational store dataflows (records ingested/updated/deleted/failed/skipped), with drill-down graphs and a per-dataflow/dataset breakdown including lineage.


### Reporting {#sep-26-reporting}

The following capability is coming to reporting in this release.

<table>
<thead>
<tr>
<th><strong>New inbound monitoring graphs in Data Management</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now monitor inbound data health directly from <strong>Data Management &gt; Monitoring &gt; Edge</strong>, with six new graphs covering throughput, latency, and proposition events:</p>
<ul>
<li><strong>AJO Inbound Throughput</strong> — overall inbound throughput (records per second) over time.</li>
<li><strong>AJO Inbound Throughput Breakdown</strong> — inbound throughput broken down by location.</li>
<li><strong>AJO Inbound Latency</strong> — inbound request latency (in milliseconds), broken down by distribution of values (P50, P90, and more).</li>
<li><strong>AJO Inbound Proposition Events Throughput</strong> — throughput of proposition events (tracking signals generated when a user interacts with, views, or triggers personalized offers) over time.</li>
<li><strong>AJO Inbound Proposition Events Throughput by Channel</strong> — proposition events throughput broken down by inbound channel (CBE, in-app, content cards).</li>
<li><strong>AJO Inbound Proposition Events Throughput by Event Type</strong> — proposition events throughput broken down by event type (dismissed, suppressed, displayed, triggered, interacted, sent).</li>
</ul>
</td>
</tr>
</tbody>
</table>

### Administration {#sep-26-administration}

The following reminder applies to administration in this release.

* **Dataset Time-to-live (TTL) guardrail — existing sandboxes** - The time-to-live (TTL) guardrail for Journey Optimizer system-generated datasets (90 days in the profile store, 13 months in the data lake) will be enforced on existing customer sandboxes and organizations starting October 1, 2026. 

### Usability improvements {#sep-26-usability}

* **Usability improvements in the Content Simulation experience** - The new Content Simulation experience now lets you name and organize your variants for easy comparison, copy or delete variant details directly from each card, view full attribute paths and per-card channel configuration on demand, and upload your own CSV, JSON, or JSONL profiles from a more prominent upload button.

* **Unified calendar for Campaigns, Journeys, and Orchestrated campaigns** - The calendar view for journeys and campaigns now moves out of separate inventories into a unified, left-rail accessible menu that shows both in one combined view.

