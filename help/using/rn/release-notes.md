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

## August '26 updates {#aug-26-updates}

### Content Management

<table>
<thead>
<tr>
<th><strong>Flexible Image Sourcing for AI Content Generation</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Generating content in Journey Optimizer now sources brand-approved images directly from Adobe Experience Manager Assets Essentials and up. Three modes control the balance: Balanced (Digital Asset Management-first, AI fills gaps, default), Assets (Digital Asset Management-sourced), and Creative (AI).</p>
<p><img src="../content-management/assets/image-mode-3.png"></p>
<p>For more information, refer to the <a href="../content-management/generative-uc.md#image-mode">detailed documentation</a>.</p>
<p> Availability date: August 5, 2026</p>
</td>
</tr>
</tbody>
</table>


* **Start and end dates in the journey header** - When start and/or end dates are configured on a journey, they are now surfaced in the journey header next to the status badge. The displayed label adapts based on whether each date is upcoming or has already passed. [Read more](../building-journeys/journey-properties.md#dates)

Availability date: August 10, 2026

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
<p>Administrators can use the Loyalty configurations menu to connect Journey Optimizer with your loyalty ecosystem, including reward fulfillment APIs, event definitions, product inventory, exclusions, and identity settings. Marketers can then design standard, streak, or sequential challenges, define tasks and rewards, deliver branded content cards and messages, and monitor performance with AI-powered reporting dashboards. Journey Optimizer generates the journeys that orchestrate each challenge in the background, so teams can focus on the customer experience and business goals.</p>
<p>Loyalty also introduces Coworker skills that let teams perform key challenge operations more efficiently, including creating challenges, setting challenge properties, managing audiences and related configuration, and reviewing insights to monitor challenge participation and reward performance.</p>
<p><img src="assets/do-not-localize/loyalty.png"></p>
<p>This capability is only available for organizations licensed for Journey Optimizer Loyalty. To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../loyalty-challenges/get-started.md">detailed documentation</a>.</p>
<p> Availability date: July 28, 2026</p>
</td>
</tr>
</tbody>
</table>

### Channels {#july-26-channels}

The following capabilities and improvements have been introduced in this release.

<table>
<thead>
<tr>
<th><strong>Custom outbound channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now introduces Custom channels, a new capability that lets administrators bring any outbound HTTP-based messaging channel — such as WeChat, Kakao Talk, Messenger, or a proprietary provider — directly into Journey Optimizer through a no-code Channel Builder.</p >
<p>Once configured, custom channels are available across campaigns, journeys, and orchestrated campaigns, with the same full set of capabilities as native channels: personalization with the expression editor, content experimentation, preview and proof, out-of-the-box reporting, and consent and governance enforcement.</p>
<p>This fills a gap previously addressed by custom actions, which are limited only to journeys and lack dedicated channel capabilities.</p>
<p>Custom outbound channels are currently available as Limited Availability. To gain access, contact your Adobe representative.</p>
<p><img src="assets/do-not-localize/custom-channel.gif"></p>
<p>For more information, refer to the <a href="../custom-channel/get-started-custom-channel.md">detailed documentation</a>.</p>
<p> Availability date: July 31, 2026</p>
</td>
</tr>
</tbody>
</table>

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

* **WhatsApp Channel: Support WhatsApp Flow templates** - You can now send WhatsApp Flow templates in Adobe Journey Optimizer to deliver interactive multi-screen experiences like surveys and lead capture. Responses are captured upon submission and stored as raw JSON payloads in the new Journey Optimizer Channel Tracking Event Dataset. [Learn more](../data/get-started-datasets.md)

* **Enhanced Custom Provider Integrations - Mobile** - Custom provider integrations now offer expanded flexibility with key messaging and header updates:

  * Header Customization: You can now edit the default Content-Type header value and add up to 10 custom header parameters.

  * SMS Payload Support: Added support for Adobe Journey Optimizer helper functions within the SMS payload, including encode64.

### Administration {#july-26-administration}

The following capabiolities and improvements have been added to administration and data management in this release.

<table>
<thead>
<tr>
<th><strong>Web Application Firewall IP allowlisting</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports Web Application Firewall IP allowlisting for landing pages, enabling organizations to enforce that all incoming requests are routed exclusively through their configured Web Application Firewall infrastructure. With this enhancement, customers can configure Journey Optimizer to reject any direct requests that bypass the Web Application Firewall layer, ensuring that security policies defined in tools such as Imperva are consistently applied.</p>
<p>This capability strengthens the security posture for enterprises with strict network access requirements, giving them full control over the traffic flow to their Journey Optimizer-hosted landing pages.</p>
<p><img src="assets/do-not-localize/allowed-ips.gif"></p>
<p>For more information, refer to the <a href="../configuration/waf-ip-allowlist.md">detailed documentation</a>.</p>
<p>Availability date: July 30, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Manage domains for complete/base URL personalization** - You can now create and manage approved domains for complete and base URL personalization directly from the Administration settings in Adobe Journey Optimizer, without having to contact Adobe support. [Learn more](../email/url-personalization.md#personalize-complete-base-url)

    Availability date: July 30, 2026

* **Dataset Time-to-live (TTL) guardrail — existing sandboxes** - The time-to-live (TTL) guardrail for Journey Optimizer system-generated datasets (90 days in the profile store, 13 months in the data lake) will be enforced on **existing customer sandboxes and organizations** starting **October 1, 2026**. [Learn more](../data/datasets-ttl.md#ttl-guardrail)

### Email Design {#july-26-email}

The following capabilities and improvements have been added to email design in this release.

<table>
<thead>
<tr>
<th><strong>Modules in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Email Designer now includes a library of ready-to-use layout modules — such as headers, product cards, information blocks, and footers — that you can drag and drop directly into your email canvas.</p>
<p>Each module comes pre-configured with editable properties (image, title, text, button, links) and can be fully customized through the WYSIWYG interface, speeding up email creation without requiring you to build structures from scratch.</p>
<p><img src="assets/do-not-localize/email-modules.gif"></p>
<p>For more information, refer to the <a href="../email/email-modules.md">detailed documentation</a>.</p>
<p>Availability date: July 29, 2026</p>
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

* **Expression fragments support in `<head>`** - Expression fragments can now be used in the `<head>` of email templates. This allows you to centralize styling or any custom code in a single fragment and reuse it across multiple templates. When a fragment is updated and republished, all emails built from templates referencing it automatically inherit the latest code — eliminating the need to manually update each email individually. [Learn more](../personalization/use-expression-fragments.md)

  Availability date: July 29, 2026

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

* [!BADGE Deprecation]{type=Negative} **Batch audiences no longer supported in Audience Qualification node and Exit Criteria** - Starting September 2026, Journey Optimizer will block publication for any journey using a batch audience in an Audience Qualification node or in Exit Criteria. A validation warning is already surfaced in the journey canvas.  Existing live journeys are not affected. New, draft, and duplicated journeys that include this configuration must be updated before September 2026. Use a streaming audience in the Audience Qualification node, or switch to a Read Audience activity. For Exit Criteria, use a streaming audience. [Learn how to migrate your journeys](../building-journeys/aq-batch-audiences-migration.md)

* **External audiences in Journey Simulation** - Journey Simulation now supports External Audiences. When simulating journeys targeting CSV or Federated Audience Composition audiences, you can mock enrichment attributes from those audiences directly through the UI form or a JSON import. The UI dynamically displays only the specific enrichment attributes used in your journey logic, enabling precise validation of decision branches and personalization rules prior to going live. [Learn more](../building-journeys/simulate-journey.md)

  Availability date: July 29, 2026

* **Circuit breaker protection for slow custom action endpoints** - For endpoints routed through the slow custom action service, Journey Optimizer now temporarily caps all calls for up to 5 minutes when more than 20% of calls in a 120-second window exceed 10 seconds, if there are at least 200 calls in the 120-second observation window. This helps prevent overloading endpoints that are already slow. [Learn more](../configuration/external-systems.md#response-time)

  Availability date: July 29, 2026. This capability is being gradually rolled out across regions.

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

* **View Orchestrated Campaign Transitions permission** - Added a new **View Orchestrated Campaign Transitions** permission to replace the legacy **View File in Orchestrated Campaigns** option. This change allows you to hide preview results within campaign transitions to support personally identifiable information compliance.

  Availability date: July 29, 2026

  [Learn more](../administration/ootb-permissions.md)

### Decisioning {#decisioning}

* **Decisioning rules creation from natural language expression** - You can now describe the Decisioning rule you want to create in plain language and let AI generate it for you. This capability is available to customers with access to Adobe AI capabilities.

  This capability is available to organizations with access to Adobe AI capabilities. It is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

  Availability date: July 29, 2026

  [Learn more](../experience-decisioning/rules.md#build-rule-with-ai)

* **Decision items' dynamic custom attributes** - Decision item custom attributes can now be personalized at delivery time using profile, contextual, and audience data. This removes the need to maintain duplicate offers for minor content variations, allowing marketers to manage fewer, more flexible decision items. [Learn more](../experience-decisioning/items.md#attributes)

  Availability date: July 27, 2026

* **Decisioning rules and ranking formulas simulation** - You can now simulate your Decisioning rules and ranking formulas directly from the rule or formula editor. Add manual test variants or generate them using AI, then run the expression against your test data to validate eligibility and review ranked results, all before deploying to production. Variants generation is available to customers with access to Adobe AI capabilities.

  This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

  Availability date: July 29, 2026

  [Learn more about rules simulation](../experience-decisioning/rules.md) | [Learn more about ranking formulas simulation](../experience-decisioning/ranking/ranking-formulas.md)

### Content management {#july-26-content}

The following capabilities and improvements have been added to content management in this release.

<table>
<thead>
<tr>
<th><strong>Guided Adoption Capabilities</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Transitioning to Adobe Journey Optimizer from another marketing platform is easier with guided capabilities that help you move existing email content and journeys into Journey Optimizer. A dedicated workspace lets you reuse what you have instead of rebuilding from scratch.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p><img src="assets/do-not-localize/guided-adoption.gif"></p>
<p>For more information, refer to the <a href="../start/migrate-content-and-journeys.md">detailed documentation</a>.</p>
<p> Availability date: July 30, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Quick launch shortcuts in Fragments inventory** - You can now quickly access common actions from the Fragments list using the **[!UICONTROL More actions]** button. Available shortcuts include editing the fragment, opening its details, and discarding the draft version. [Learn more](../content-management/manage-fragments.md#quick-launch-fragments)

  ![](../content-management/assets/fragment-quick-launch.png)

* **Quick launch shortcuts in Templates inventory** - The **[!UICONTROL More actions]** button in the Content Templates list now provides quick access to common actions: editing template details, simulating content, and deleting a template. For email templates, additional shortcuts let you edit the subject line and email body, view or send a proof, run a spam report, and render the email. [Learn more](../content-management/access-content-templates.md#quick-launch-templates)

  ![](../content-management/assets/content-template-quick-launch.png)

* **New helper functions in personalization expressions** - New helper functions are now available in personalization expressions:

  * `appendQueryParams`: Appends a query parameter to a URL, or replaces it if the key already exists.
  * `dateBetween`: Checks whether a date falls within a start and end date range (inclusive).
  * `equalsAnyIgnoreCase`: Returns true when a string matches any provided value, ignoring case.
  * `getUrlFragment`: Extracts the fragment portion of a URL (the part after #).
  * `join`: Concatenates array elements into a single string using a separator.
  * `decode64`: Decodes a Base64-encoded string. If the input is not valid Base64, the original input string is returned unchanged.
  * `parseJson`: Parses a JSON string into a structured variable that can be used in the template.
  * `valueAtPath`: Assigns a value from a data path to a template variable, with optional indexing to extract a specific element from arrays or collections.
  * `abort`: Stops message delivery when reached during rendering.

  The `concat` function has also been enhanced and now supports two or more arguments.

  In addition, the following Template Migration Functions are now available to assist with migrating existing templates to Journey Optimizer:

  * `ampCompare`: Compares two values using the specified comparison operator.
  * `ampSubstr`: Returns a portion of a string between the specified start and end indices.
  * `compareTo`: Compares two strings lexicographically.

  [Learn more about helper functions](../personalization/functions/functions.md)

  Availability date: July 28, 2026

* **"AI Assistant" renamed to "Generate content"** - AI Assistant has been renamed to Generate Content throughout Adobe Journey Optimizer. This update is limited to naming and terminology; no functional changes have been introduced. Navigation labels, buttons, menus, and dialogs for content generation, image generation, personalization expressions, and content experimentation have been renamed from "AI Assistant" to "Generate Content."

  Availability date: July 30, 2026

* **Multilingual improvements** - Language Settings can now be duplicated from an existing active setting, so you no longer need to fully rebuild a configuration to make changes. You can also copy a condition from one locale to another while authoring Language Settings, streamlining setup for sites with many languages.

  Availability date: July 30, 2026
 
### Content & Integrations {#july-26-integration}

The following improvements are coming to content management and integrations in this release.

<table>
<thead>
<tr>
<th><strong>Countdown timer using Dynamic Media</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Journey Optimizer and Adobe Experience Manager Dynamic Media integration</strong> enables open-time personalization for Dynamic Media templates, unlocking hyper-personalized use cases. Customers can create and publish personalized templates in Adobe Experience Manager and use them in Journey Optimizer, with data rendered at open time.</p>
<p>For more information, refer to the <a href="../integrations/aem-dynamic.md#countdown">detailed documentation</a>.</p>
<p> Availability date: July 30, 2026</p>
</td>
</tr>
</tbody>
</table>



* **AJO MCP server new tools** - The [!DNL Adobe Journey Optimizer] MCP server now exposes five additional read-only **channel configuration tools**, enabling you to query channel configurations, supporting resources, and marketing actions directly from your AI assistant. You can now use **List Channel Configurations** (across all AJO channels), **Get Channel Configuration**, **List Configuration Resources**, **Get Configuration Resource**, and **List Marketing Actions**. [Read more](../integrations/ajo-mcp.md#mcp-tools)

  Availability date: July 9, 2026

### Reporting {#july-26-reporting}

The following improvement is coming to reporting in this release.

* **New Estimated Click Metrics for Email Reporting** - To provide a more accurate view of real customer engagement, new estimated metric are now available across Journeys, Campaigns, and Channel Live reports.

  * Estimated CTR (Click-through rate): Calculated as estimated clicks relative to the total number of delivered messages.

  * Estimated CTOR (Click-to-open rate): Calculated as estimated clicks relative to the total number of estimated opens.

    Availability date: July 29, 2026

### Campaigns {#campaigns}

+++ Coming soon

<table>
<thead>
<tr>
<th><strong>Personalized PDF attachments in API-triggered emails</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now supports attaching up to five recipient-specific PDFs per email in API-triggered campaigns. PDF files are fetched securely from Azure or AWS storage and attached at send time, with each file's location passed directly in the API payload. This allows existing upstream document generation systems to remain in place, with Journey Optimizer handling delivery.</p>
<p>Supported use cases include invoices, statements, tickets, contracts, shipping labels, and similar documents that vary per recipient. Personalized PDF attachments are available in API-triggered campaigns only and are not supported in journeys or other campaign types (action, orchestrated).</p>
<p>Larger attachment volumes and sizes are supported via the PDF attachment add-on; for information, contact your Adobe representative.</p>
<p></p>
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Performance Add-on for throughput in API-triggered campaigns - Push** - A new high throughput transactional messaging mode is available in API-triggered campaigns. This mode is designed for large-scale, real-time transactional messaging and supports up to 5,000 transactions per second with higher availability. Previously only available for the email channel, this capability is now also available for the push channel, for organizations that have purchased the Adobe High Throughput Transactional Messaging add-on offering. Contact your Adobe representative for more details. <!-- Documentation link: TBD -->

+++

### Usability improvements {#july-26-usability}

+++Coming soon

* **New Content Simulation experience for content testing** - The **Simulate content** workflow introduces a redesigned experience: all variants now render together in a single scrollable grid (side-by-side, stacked, or wrapped layouts), replacing the one-variant-at-a-time view. A single bottom action bar consolidates navigating between test variants, zoom, viewport switching (desktop/mobile), locale switching, adding sample inputs, generating variants with AI, picking and saving simulated users, and importing or exporting variants. Removing the left rail and collapsing extra header layers gives previews significantly more room. A **Switch to classic experience** option in the bottom action bar lets you revert to the previous experience at any time.

+++