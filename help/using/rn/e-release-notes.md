---
solution: Journey Optimizer
product: journey optimizer
title: Pre release notes for Journey Optimizer
description: Adobe Journey Optimizer Pre Release notes
hide: true
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

### Content Management {#sep-26-content-management}

The following capability is coming to content management in this release.

<table>
<thead>
<tr>
<th><strong>Message-copy and email-design plugins in CX Coworker</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Two new plugins are now available in CX Coworker to streamline your <strong>messaging and email workflows</strong> from strategy to deployment:</p>
<p><strong>Message copy plugin</strong>:</p>
<ul>
<li>Captures campaign briefs and defines messaging maps, narrative arcs, and channel roles.</li>
<li>Builds a multi-dimensional content matrix tailored across channels, touchpoints, locales, audiences, and variants.</li>
<li>Produces net-new copy and leverages Adobe Firefly to generate, crop, and adapt campaign visuals.</li>
<li>Allows in-place content evaluation and directly syncs approved assets back to Journey Optimizer, Adobe Campaign V8, and Marketo.</li>
</ul>
<p><strong>Email design plugin</strong>:</p>
<ul>
<li>Converts marketing goals, reference screenshots, or Figma design links into custom layout plans and production-ready email HTML.</li>
<li>Manages reusable brand assets, design tokens, and structural email templates.</li>
<li>Audits assembled email code for corporate compliance, visual design quality, and WCAG 2.1 AA accessibility standards.</li>
<li>Exports approved HTML directly into Adobe Journey Optimizer and Adobe Campaign.</li>
</ul>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15642" target="_blank">DOCAC-15642</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15563" target="_blank">DOCAC-15563</a></p>
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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15661" target="_blank">DOCAC-15661</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **CX Coworker loyalty recommendation skill** - Marketers can now request **challenge opportunities** directly in CX Coworker's conversational interface, getting grounded challenge ideas based on real loyalty program trends and turning them into live challenges without leaving the chat. <a href="https://jira.corp.adobe.com/browse/DOCAC-15565" target="_blank">DOCAC-15565</a> <!-- Documentation link: TBD -->

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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15330" target="_blank">DOCAC-15330</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

### Journeys {#sep-26-journeys}

The following capabilities and improvements are coming to journeys in this release.

<table>
<thead>
<tr>
<th><strong>Journey Simulation in CX Coworker (MCP &amp; Chat)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The <strong>Journey Simulation skill</strong> in CX Coworker automates end-to-end journey validation and lets you easily interpret the results. Note that this feature currently supports only the Quick Simulation flow and does not fully replace the Journey Optimizer manual simulation experience.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15374" target="_blank">DOCAC-15374</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Decisioning path experimentation in Journey simulation** - **Path Experimentation**, part of the Optimize activity in Decisioning, is now supported in Journey simulation. <a href="https://jira.corp.adobe.com/browse/DOCAC-15641" target="_blank">DOCAC-15641</a> <!-- Documentation link: TBD -->

* **Supplemental ID support in Journey simulation** - **Supplemental ID** is now supported in Journey simulation, allowing you to test complex user scenarios for both read-audience and event-triggered journeys. <a href="https://jira.corp.adobe.com/browse/DOCAC-15448" target="_blank">DOCAC-15448</a> <!-- Documentation link: TBD -->

<table>
<thead>
<tr>
<th><strong>Journey creation from CX Coworker rail</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Journey creation with AI</strong> is now available directly from the CX Coworker right rail, replacing the previous AI Assistant experience with a re-branded, integrated entry point for generating journeys.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-14898" target="_blank">DOCAC-14898</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Refined batch audience evaluation wait logic** - In the **Read audience activity**, the "Trigger after batch audience evaluation" option in journeys now waits for any batch segmentation that is already in progress to complete, ensuring the journey uses that run's data instead of falling back to an older snapshot. If no batch segmentation is in progress, the journey fires immediately using the latest available audience data. <a href="https://jira.corp.adobe.com/browse/DOCAC-15465" target="_blank">DOCAC-15465</a> <!-- Documentation link: TBD -->

* **Compare journey versions with CX Coworker** - Today, reviewing what changed between two versions of a journey requires manually comparing them inside Journey Optimizer node by node - there's no structured diff, which makes change-review, audit, and pre-publish checks slow and error-prone, especially as journeys grow more complex. This capability lets a customer or AI agent compare any two versions of a journey through CX Coworker Chat and get back a full-fidelity, **structured diff** - added/removed/modified/moved nodes with field-level detail, changed connections, journey-level property changes, and roll-up counts - without opening Journey Optimizer. <a href="https://jira.corp.adobe.com/browse/DOCAC-15297" target="_blank">DOCAC-15297</a> <!-- Documentation link: TBD -->

* **Content preview in the journey canvas** - Reviewing channel content today requires opening each node individually, one at a time - slow and error-prone on journeys with many channel nodes, especially where personalization means checking multiple treatments or variants per node. **Content preview** removes that friction by surfacing a content thumbnail for every channel node directly in the canvas, with a fullscreen modal to inspect and switch between treatments and variants. <a href="https://jira.corp.adobe.com/browse/DOCAC-15456" target="_blank">DOCAC-15456</a> <!-- Documentation link: TBD -->

* **New Journey Anomaly Detected alert** - A new system alert now warns you when a live journey's daily traffic deviates from its own historical baseline, or drops to zero unexpectedly, across Journey Entries, Journey Exits, and Event Sends. This alert is currently available in production sandboxes only. <a href="https://jira.corp.adobe.com/browse/DOCAC-15545" target="_blank">DOCAC-15545</a> <!-- Documentation link: TBD -->

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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15510" target="_blank">DOCAC-15510</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-14037" target="_blank">DOCAC-14037</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-14718" target="_blank">DOCAC-14718</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Custom SMS BYOP auth flexibility** - You can now configure **custom authentication headers** when connecting your SMS provider's OAuth setup, including where the token is placed on outgoing messages and how the token request itself is formatted. <a href="https://jira.corp.adobe.com/browse/DOCAC-15638" target="_blank">DOCAC-15638</a> <!-- Documentation link: TBD -->

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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15020" target="_blank">DOCAC-15020</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Alerting for orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Orchestrated campaigns now support <strong>automated alerting</strong> through the same alerting framework used across journeys and campaigns. Alerts are triggered when a campaign execution fails, times out, or requires confirmation, and each alert includes what happened, when, where, and a direct link to the monitoring view, categorized by severity so teams can prioritize without manual UI checks.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-14886" target="_blank">DOCAC-14886</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **LINE channel for orchestrated campaigns** - LINE is now available as a native outbound channel in orchestrated campaigns, alongside email, SMS, and push. You can build and deliver LINE messages directly from the campaign canvas, including text, stickers, images, videos, location data, and Flex Messages, supporting promotional, transactional, and ongoing engagement use cases in LINE-dominant markets such as Japan and APAC. Previously released in Limited Availability, this capability is now generally available. <a href="https://jira.corp.adobe.com/browse/DOCAC-15102" target="_blank">DOCAC-15102</a> <!-- Documentation link: TBD -->

* **New Orchestrated Campaigns monitoring APIs** - New **API specifications** are now available for orchestrated campaigns, allowing you to programmatically create, manage, and trigger orchestrated campaigns, enabling deeper integration with external systems and automation pipelines. <a href="https://jira.corp.adobe.com/browse/DOCAC-14308" target="_blank">DOCAC-14308</a> <!-- Documentation link: TBD -->

* **Direct join UX improvements** - When adding an attribute from a related collection, you can now choose between three join modes — a new default that warns you about potential performance impact from cartesian products, plus the existing Aggregate and Advanced modes — making it easier to understand the tradeoffs of your query before you build it. <a href="https://jira.corp.adobe.com/browse/DOCAC-15675" target="_blank">DOCAC-15675</a> <!-- Documentation link: TBD -->

* **Conditional content with relational data in orchestrated campaigns** - When building conditional content in the Email Designer for orchestrated campaigns, you can now build conditions directly on **relational data** — such as related records associated with a profile — not just standard profile attributes. This closes a gap from the original release, so marketers can build these conditions visually, without needing engineering help. <a href="https://jira.corp.adobe.com/browse/DOCAC-15679" target="_blank">DOCAC-15679</a> <!-- Documentation link: TBD -->

### Campaigns {#sep-26-campaigns}

The following capabilities and improvements are coming to campaigns in this release.

<table>
<thead>
<tr>
<th><strong>Inbound experience simulation in Action Campaigns (Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now simulate inbound channel actions in Action Campaigns before going live. Use simulation mode to test your configuration with simulated users and preview the rendered experience, including a generated URL and QR code, so you can validate rules, decisioning, and content rendering end-to-end.</p>
<p>This capability is currently in private beta and available to a limited set of organizations. Contact your Adobe representative for more information.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15166" target="_blank">DOCAC-15166</a></p>
</td>
</tr>
</tbody>
</table>

* **Folders for campaigns** - You can now organize your campaigns into **folders** to improve navigation and management in the interface. <a href="https://jira.corp.adobe.com/browse/DOCAC-15098" target="_blank">DOCAC-15098</a> <!-- Documentation link: TBD -->

### Decisioning {#sep-26-decisioning}

The following capabilities and improvements are coming to Decisioning in this release.

<table>
<thead>
<tr>
<th><strong>Decisioning support in Web channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Decisioning is now available for the Web channel. You can use decision policies directly in the web visual editor to deliver the most relevant offers to each visitor.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-11548" target="_blank">DOCAC-11548</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Decisioning rule generation from CX Coworker** - The **AI-assisted decisioning rule generation** experience, previously available via the right rail, is now accessible through CX Coworker, which replaces the right rail as the way to build rules with AI. <a href="https://jira.corp.adobe.com/browse/DOCAC-15290" target="_blank">DOCAC-15290</a> <!-- Documentation link: TBD -->

### Direct mail {#sep-26-direct-mail}

The following capabilities and improvements are coming to Direct Mail in this release.

* **Split large files automatically** - Direct Mail files can now be split into multiple parts automatically when they exceed roughly 20 GB, or manually by choosing a target file size in the file routing configuration. An optional JSON manifest file describes all generated parts. <a href="https://jira.corp.adobe.com/browse/DOCAC-15677" target="_blank">DOCAC-15677</a> <!-- Documentation link: TBD -->

* **Increased audience limit** - The Direct Mail channel audience limit has been increased from 3 million to 100 million profiles, letting you target much larger audiences without hitting file-creation errors. <a href="https://jira.corp.adobe.com/browse/DOCAC-15676" target="_blank">DOCAC-15676</a> <!-- Documentation link: TBD -->

### Email Designer {#sep-26-email-designer}

The following capabilities and improvements are coming to the Email Designer in this release.

<table>
<thead>
<tr>
<th><strong>Independent dark mode styling for email theme variants</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Email themes now support independent styling for dark mode. In the theme builder, you can turn on dark mode for a given variant to generate a dedicated dark mode stylesheet that you edit separately from the light mode styles — changes made in one mode no longer overwrite the other. In the email and template editor, a new preview toggle next to the desktop and mobile view options lets you preview your content in dark mode.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15663" target="_blank">DOCAC-15663</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15664" target="_blank">DOCAC-15664</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15093" target="_blank">DOCAC-15093</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Fallback fonts for custom fonts in email themes** - You can now define a fallback font for any custom (web) font applied through email themes. If a subscriber's email client does not support the custom font, Adobe Journey Optimizer automatically displays the specified fallback font instead of leaving the choice to the email client's default. This keeps email typography closer to your brand guidelines and reduces font-rendering inconsistencies across email clients. <a href="https://jira.corp.adobe.com/browse/DOCAC-15662" target="_blank">DOCAC-15662</a> <!-- Documentation link: TBD -->

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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15680" target="_blank">DOCAC-15680</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

### Administration {#sep-26-administration}

The following reminder applies to administration in this release.

* **Dataset Time-to-live (TTL) guardrail — existing sandboxes** - The time-to-live (TTL) guardrail for Journey Optimizer system-generated datasets (90 days in the profile store, 13 months in the data lake) will be enforced on existing customer sandboxes and organizations starting October 1, 2026. <a href="https://jira.corp.adobe.com/browse/DOCAC-15239" target="_blank">DOCAC-15239</a> <!-- Documentation link: TBD -->

* **Upcoming change to Audience Composition enrichment audiences** - During the October release (end of October), Journey Optimizer will stop journeys that use or reference an Audience Composition audience whose source dataset does not have a **primary identity descriptor**. From that point forward, only Audience Composition audiences built with a primary identity descriptor are supported in journeys. If you need these journeys to remain active, contact your Adobe representative — our product team can help you migrate. <a href="https://jira.corp.adobe.com/browse/DOCAC-15690" target="_blank">DOCAC-15690</a> <!-- Documentation link: TBD -->

### Usability improvements {#sep-26-usability}

* **Usability improvements in the Content Simulation experience** - The new Content Simulation experience now lets you name and organize your variants for easy comparison, copy or delete variant details directly from each card, view full attribute paths and per-card channel configuration on demand, and upload your own CSV, JSON, or JSONL profiles from a more prominent upload button. <a href="https://jira.corp.adobe.com/browse/DOCAC-15570" target="_blank">DOCAC-15570</a>


