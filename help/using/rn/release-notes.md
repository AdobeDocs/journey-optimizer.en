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

## July '26 updates {#july-26-updates}

### New capabilities {#july-26-new-capabilities}

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

### Improvements {#july-26-improvements}

* **AJO MCP server new tools** - The [!DNL Adobe Journey Optimizer] MCP server now exposes five additional read-only **channel configuration tools**, enabling you to query channel configurations, supporting resources, and marketing actions directly from your AI assistant. You can now use **List Channel Configurations** (across all AJO channels), **Get Channel Configuration**, **List Configuration Resources**, **Get Configuration Resource**, and **List Marketing Actions**. [Read more](../integrations/ajo-mcp.md#mcp-tools)

  Availability date: July 9, 2026

* **Dataset Time-to-live (TTL) guardrail — existing sandboxes** - The time-to-live (TTL) guardrail for Journey Optimizer system-generated datasets (90 days in the profile store, 13 months in the data lake) will be enforced on **existing customer sandboxes and organizations** starting **October 1, 2026**. [Learn more](../data/datasets-ttl.md#ttl-guardrail)


### Usability improvements {#july-26-usability}

The following usability improvements were released in July 2026.

#### Content management

* **Quick launch shortcuts in Fragments inventory** - You can now quickly access common actions from the Fragments list using the **[!UICONTROL More actions]** button. Available shortcuts include editing the fragment, opening its details, and discarding the draft version. [Learn more](../content-management/manage-fragments.md#quick-launch-fragments)

  ![](../content-management/assets/fragment-quick-launch.png)

* **Quick launch shortcuts in Templates inventory** - The **[!UICONTROL More actions]** button in the Content Templates list now provides quick access to common actions: editing template details, simulating content, and deleting a template. For email templates, additional shortcuts let you edit the subject line and email body, view or send a proof, run a spam report, and render the email. [Learn more](../content-management/access-content-templates.md#quick-launch-templates)

  ![](../content-management/assets/content-template-quick-launch.png)

#### Journeys

A **new user interface** has been introduced for the journey canvas, delivering improved performance for large journeys, automatic layout for better readability, and a guided authoring experience.

![](../building-journeys/assets/journey-new-canvas.png)

To switch to the new UI, click the **[!UICONTROL New experience]** button. This setting is saved at the journey level, so the journey reopens in the new experience by default. To revert, click **[!UICONTROL Old experience]**. [Learn more](../building-journeys/using-the-journey-designer.md#canvas-capabilities)

![](../building-journeys/assets/journey-new-experience-switch.png)

Availability date: July 16, 2026


## June '26 release notes {#june-26-rn}

### Journeys {#june-26-journeys}

The following capabilities and improvements have been added to journeys in this release. Additional changes are also expected in the upcoming days or weeks.


<table>
<thead>
<tr>
<th><strong>Journey Simulation (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now set your journey to Simulation. This mode allows you to validate your logic using simulated users. These are temporary profiles created specifically for the simulation, allowing you to test freely without needing to manage persistent test profiles in Adobe Experience Platform. </p>
<p>Previously released in Limited Availability, Journey Simulation is now available to all environments. With this General Availability release, you can now use Journey Agent to generate simulated users and events directly in the Simulation menu.</p>
<p><img src="assets/do-not-localize/journey-simulation.gif"></p>
<p>For more information, refer to the <a href="../building-journeys/simulate-journey-gs.md">detailed documentation</a>.</p>
<p>Availability date: June 9, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Fragments (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create <strong>Journey Fragments</strong> in Adobe Journey Optimizer. Journey Fragments are reusable sets of journey nodes that you can build once and drop into any journey across your sandbox. Whether it's an eligibility check, a preferred channel routing logic, or a welcome sequence, fragments help teams move faster and stay consistent, without rebuilding the same logic from scratch every time.</p>
<p>Once created, fragments are stored in a dedicated <strong>Fragment Inventory</strong> and can be inserted into any journey using the <strong>Journey fragments</strong> activity.</p>
<p>Previously available in Limited Availability, this capability is now generally available to all customers. Journey fragments also support <strong>Sandbox tooling</strong>, allowing you to package and export fragments across sandboxes.</p>
<p>For more information, refer to the <a href="../building-journeys/journey-fragments.md">detailed documentation</a>.</p>
<p>Availability date: June 9, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey path optimization - Targeting (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The <strong>Optimize activity</strong> now supports <strong>Targeting rules</strong> which enable you to define specific criteria that customers must meet to qualify for a particular journey path, based on audience segments or profile attributes.</p>
<p>Unlike experimentation, where customers are assigned to paths randomly, targeting uses deterministic logic to ensure that the appropriate audience or customer profile is routed to the intended path.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/optimize.gif"></p>
<p>For more information, refer to the <a href="../building-journeys/path-targeting.md">detailed documentation</a>.</p>
<p>Availability date: June 8, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>AI Assistant for Journey Expressions (Public Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>AI Assistant now operates in the journey advanced expression editor to convert natural-language prompts into valid expressions and conditional logic. Describe the expression you want to build, and AI Assistant generates ready-to-use code you can apply immediately or refine through follow-up prompts.</p>
<p>This capability is available to all customers as a Public Beta.</p>
<p><img src="assets/do-not-localize/expression-assistant.gif"></p>
<p>For more information, refer to the <a href="../building-journeys/expression/generate-expression.md">detailed documentation</a>.</p>
<p>Availability date: June 3, 2026</p> 
</td>
</tr>
</tbody>
</table>


* [!BADGE Deprecation]{type=Negative} **Batch audiences deprecated in Audience Qualification node** - Starting **August 2026**, Journey Optimizer will block publication for any journey using a batch audience in an **Audience Qualification** node. A validation warning is already surfaced in the journey canvas. Existing live journeys are not affected. New, draft, and duplicated journeys that include this configuration must be updated before August 2026. Use a streaming audience in the Audience Qualification node, or switch to a **Read Audience** activity. [Learn how to migrate your journeys](../building-journeys/aq-batch-audiences-migration.md)

* **Stop a paused journey directly** - You can now stop a journey directly from the **Paused** state. Previously, a paused journey had to be resumed to **Live** before it could be stopped. [Read more](../building-journeys/journey-pause.md#stop-close-paused)

  Availability date: June 18-22, 2026

* **Supplemental identifier support for external audiences** - Supplemental identifiers in journeys are now supported for external audiences, including audiences imported from a CSV file and audiences created with Federated Audience Composition. You can designate any non-identity attribute or non-person identity attribute from the audience as the supplemental ID, no schema labeling is required. [Read more](../building-journeys/supplemental-identifier.md)

  Availability date: June 11, 2026

* **Automatic stop for non-recurring Read Audience journeys** - Non-recurring **Read Audience** journeys now automatically transition to **Stopped** status once the last active profile exits. Previously, these journeys remained **Live** until the 91-day global timeout expired — even when no profiles were flowing through them anymore. With this improvement, journey status reflects actual execution state as soon as it completes, keeping your journey inventory accurate without manual intervention.

  Note that this behavior does not apply to journeys that include nodes causing waiting periods, such as Wait nodes, Reaction nodes, or event-triggered transitions. These journeys remain subject to the standard 91-day global timeout. [Learn more](../building-journeys/end-journey.md#auto-stop-non-recurring)

  Availability date: June 9, 2026

* **Certificate-Based Custom Authentication in custom actions** - Custom actions now support Certificate-Based Custom Authentication. By adding `subType: "certificateCredential"` to a custom authorization configuration, Journey Optimizer uses Adobe's managed certificate to sign a JWT client assertion and exchange it for an access token — no client secret required. Designed for enterprise APIs that enforce certificate-based identity verification, such as Microsoft Entra ID. [Learn more](../datasource/external-data-sources.md#certificate-credential)

  Availability date: June 4, 2026

* **Increased live journey limit and new guardrails** - You can now have up to **200 active journeys**, increased from the previous limit of 100. [Read more](../start/guardrails.md#journeys-guardrails-journeys)

  Availability date: June 18, 2026. This capability is being gradually rolled out to all regions over the next few days.


+++ Coming soon — **Information below is subject to change.**

* **Start and end dates in the journey header** - When start and/or end dates are configured on a live journey, they are now surfaced in the **journey header** next to the live status badge. The displayed label adapts based on whether each date is upcoming or has already passed.

+++

### Orchestrated campaigns {#june-26-oc}

The following capabilities and improvements are coming to orchestrated campaigns in this release.

* **Loop-based personalization for relational data** - The personalization editor now supports a Loop block that iterates over relational collections, such as orders, accounts, or bookings, and renders one content block per record inside a single email or SMS. Collections are configured through the data picker using personalization tokens, with no expression writing required. [Read more](../orchestrated/add-personalization.md#enrichment-collections)

  Availability date: June 26, 2026

### Decisioning {#june-26-decisioning}

The following capabilities and improvements have been added to Decisioning in this release.

<table>
<thead>
<tr>
<th><strong>Decisioning support in Direct Mail channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add Decision policies into Direct Mail journeys and campaigns. Decision policies are containers for your offers that leverage the Decisioning engine to dynamically return the best content for each audience member. Direct Mail decisioning also supports batch decisioning use cases, enabling you to export the corresponding offer items for every profile in a given Adobe Experience Platform audience. </p>
<p><img src="assets/do-not-localize/exd-dm.gif"></p>
<p>For more information, refer to the <a href="../experience-decisioning/use-decision-policy.md">detailed documentation</a>.</p>
<p>Availability date: June 3, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Leverage Adobe Experience Manager content fragments in Decisioning** - You can now map Adobe Experience Manager content fragments to decision items in Decisioning and leverage them inside decision policies to deliver the right fragment to the right customer at the right time. Previously released in Limited Availability, this capability is now available to all environments (General Availability). [Read more](../experience-decisioning/fragments-decision-policies.md)

  Availability date: June 18, 2026

### Content management {#june-26-content}

The following capabilities and improvements have been added to content management in this release.

<table>
<thead>
<tr>
<th><strong>Simulate content variations — updated experience and AI variant generation</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Two updates are now available to the <strong>Simulate content</strong> workflow:</p>
<ul>
<li><strong>New default path</strong> — Clicking <strong>Simulate content</strong> now opens the <strong>Simulate content variations</strong> experience by default. From a single screen, you can add sample input manually or from a CSV/JSON file, reuse simulated users, preview rendering, and send proofs. To preview with Adobe Experience Platform test profiles, send proofs with test profile data, or check email inbox rendering and spam reports, click <strong>Simulate content</strong>, then select <strong>Simulate content (AEP profiles)</strong> from the dropdown.</li>
<li><strong>AI-generated content variants</strong> — In the <strong>Simulate content variations</strong> experience, click <strong>Generate</strong> to use AI to automatically create content variants. The system analyzes your message, detects personalization fields and conditional branches, and fills in realistic values so you can validate rendering without building every variant by hand.</li>
</ul>
<p>For more information, refer to the <a href="../test-approve/simulate-sample-input.md">detailed documentation</a>.</p>
<p>Availability date: June 9, 2026</p>
</td>
</tr>
</tbody>
</table>


### Email channel {#june-26-email}

The following improvements have been added to the email channel in this release.

* **URL parameter encryption** - You can now encrypt URL parameters in tracking and landing page links added to your email messages. This provides an additional layer of security for sensitive parameter data. Previously released in Limited Availability, this capability is now available to all environments (General Availability). [Read more](../personalization/url-parameter-encryption.md)

  Availability date: June 1, 2026

* **New permissions for key registry** - Two new permissions are now required to access and manage the keys needed for URL parameter encryption: **Manage Key Registry** and **View Key Registry**. [Read more](../administration/high-low-permissions.md#administration-permissions)

  Availability date: June 1, 2026

<table>
<thead>
<tr>
<th><strong>Email size optimization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now includes an option to reduce the size of your email's HTML by stripping unnecessary whitespace, comments, and redundant code — without affecting how the email renders.</p>
<p>This can improve deliverability by avoiding size thresholds that some email providers use to flag or reject messages and may reduce load time for recipients.</p>
<p><img src="assets/do-not-localize/email-size-optimization.gif"></p>
<p>For more information, refer to the <a href="../email/create-email.md#optimize-html-size">detailed documentation</a>.</p>
<p>Availability date: June 26, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Rich text in editable fields for fragments</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add rich text to customizable fragments that are used in your emails content.</p>
<p>For example, when using the Text component as an editable field in the Email Designer, you can directly format the content (for example, bold and italics) and insert hyperlinks.</p>
<p><img src="assets/do-not-localize/rich-text-editable-fields.gif"></p>
<p>For more information, refer to the <a href="../content-management/customizable-fragments.md#rich-text-visual">detailed documentation</a>.</p>
<p>Availability date: June 19, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Content check in the Email Designer (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now includes automated technical validation directly in the Email Designer, helping you catch HTML and CSS issues before sending.</p>
<p>Checks cover unsupported elements such as <code>&lt;script&gt;</code> and <code>&lt;base&gt;</code> tags, empty divs that can break layout in Microsoft Outlook, HTML meta refresh tags, and CSS or HTML size thresholds that trigger rendering failures in Gmail.</p>
<p>Results are surfaced as errors, warnings, or informational notices directly in the authoring panel, with contextual details and one-click fixes where available, so issues can be resolved without leaving the editor.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p><img src="assets/do-not-localize/content-check.gif"></p>
<p>For more information, refer to the <a href="../email/content-check.md">detailed documentation</a>.</p>
<p>Availability date: June 18, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Enhanced Image to HTML converter** - A new version of the Image to HTML converter feature is now available, bringing improved accuracy for HTML generation. This update leverages higher-tier LLM models to deliver more precise and reliable HTML output from image inputs.

  Availability date: June 18, 2026

### Content & Integrations {#june-26-integration}

The following capabilities and improvements are coming to content management and integrations in this release.

<table>
<thead>
<tr>
<th><strong>Improvements to Adobe Experience Manager Content Fragments in Journey Optimizer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>This release brings several enhancements to make <strong>Adobe Experience Manager Content Fragments</strong> more usable, more governable, and more production-ready within Journey Optimizer authoring workflows:</p>
<ul>
<li>Journey Optimizer now supports fetching Content Fragments from multiple Adobe Experience Manager configurations, including author, publish and authenticated publish tiers.</li>
<li>Once a fragment is selected, its context is preserved throughout the message, enabling authors to reuse fragment fields across content blocks without reselecting.</li>
<li>A new dedicated Content Fragments listing page has been introduced in Journey Optimizer for improved lifecycle management; users can identify out-of-sync fragments and trigger manual syncs to stay current.</li>
<li>Locale and variation support now allows marketers to work with alternate versions of the same Content Fragment more deliberately.</li>
<li>You now have flexibility in how Adobe Journey Optimizer accesses your Adobe Experience Manager content. This release introduces the ability to <strong>switch the source repository</strong> for Content Fragments used in your journeys and campaigns.</li>
<li>Now compatible with <b>Managed Services</b>, you can view, access, and use Adobe Experience Manager Content Fragments directly in Journey Optimizer for personalization. Simply add your Adobe Experience Manager Managed Services repository URL in the configuration settings as a one-time setup.</li>
</ul>
<p>For more information, refer to the <a href="../integrations/aem-fragments-gs.md">detailed documentation</a>.</p>
<p>Availability date: June 18, 2026</p>
</td>
</tr>
</tbody>
</table>

<!--
+++ Coming soon — **Information below is subject to change.**

<table>
<thead>
<tr>
<th><strong>AI assistant integration with Adobe Experience Manager Asset Essentials</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The AI Assistant now automatically fetches <b>brand-approved images</b> directly from your Adobe Experience Manager Assets when generating Emails, Web pages, and Push notifications. This eliminates the need to manually search the Assets or rely on generic AI fallbacks, ensuring every visual is perfectly accurate and brand-compliant.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>AI Assistant for content generation enhancements</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>This release improves the <strong>AI Assistant</strong> content generation experience with stronger image editing, more reliable brand extraction, and content authenticity support in the image flow:</p>
<ul>
<li><strong>AI image editing</strong> is now available in the image generation flow, including Firefly third-party model support, so you can refine source images without leaving the assistant.</li>
<li><strong>Brand signal extraction</strong> delivers higher-quality results. When selected pages lack sufficient signal, improved fallbacks now populate colors, typography, writing guidelines, and other brand attributes.</li>
<li><strong>Web-based brand extraction</strong> is more reliable. Improved timeout handling helps prevent slow pages, popups, and cookie banners from blocking extraction.</li>
<li><strong>Content authenticity (CAI)</strong> is now supported in the image flow. This release also fixes reference image upload issues and improves handling for images without an existing C2PA manifest.</li>
</ul>
</td>
</tr>
</tbody>
</table>

+++
-->

### Reporting {#june-26-reporting}

The following improvements have been added to reporting in this release.

* **New Estimated Click Metrics for Email Reporting** - To provide a more accurate view of real customer engagement, new estimated metric are now available across Journeys, Campaigns, and Channel reports.

  * **Estimated CTR** (Click-through rate): Calculated as estimated clicks relative to the total number of delivered messages.

  * **Estimated CTOR** (Click-to-open rate): Calculated as estimated clicks relative to the total number of estimated opens.
  
  Availability date: June 25, 2026

### Administration {#june-26-administration}

The following improvements have been added to administration and data management in this release.

* [!BADGE Important]{type=Informative} **AJO Message Feedback Event Dataset moving to batch ingestion** - The **AJO Message Feedback Event Dataset** is moving from streaming ingestion to batch ingestion. As a result, expect a data latency of up to 2 hours for this dataset. If you have built reports in Customer Journey Analytics or run queries using this dataset, account for this increased latency going forward. [Read more](../data/datasets-query-examples.md#message-feedback-event-dataset)

  Availability date: June 10, 2026

* **Customer alerts for campaign lifecycle events** - New system alerts now notify you of key lifecycle events for Action and API-triggered campaigns. Subscribe at the sandbox level. [Read more](../reports/alerts.md)

  Availability date: June 1, 2026

<!--
+++ Coming soon — **Information below is subject to change**

* **Web Application Firewall (WAF) IP whitelisting** - Adobe Journey Optimizer now supports Web Application Firewall (WAF) IP whitelisting for landing pages, enabling organizations to enforce that all incoming requests are routed exclusively through their configured WAF infrastructure. With this enhancement, customers can configure Journey Optimizer to reject any direct requests that bypass the WAF layer, ensuring that security policies defined in tools such as Imperva are consistently applied. This capability strengthens the security posture for enterprises with strict network access requirements, giving them full control over the traffic flow to their AJO-hosted landing pages.
  
  Availability date: Late June, 2026

+++
-->

### Mobile messaging (SMS, MMS, RCS & LINE) {#june-26-mobile}

The following improvements are coming to mobile messaging in this release.

* **Unique Clicks for SMS reports** - A new **Unique Clicks** module has been introduced to SMS reports, bringing the same level of granular performance tracking to SMS that is currently available for Email reports.

* **SMS - Display Usage Metrics** - For customers purchasing SMS directly through Adobe Journey Optimizer, a new **SMS usage dashboard** has been introduced. You can now view and track your last 90 days of message sending metrics, categorized by Mobile Originated (MO) and Mobile Terminated (MT) messages. This data is also available for download via CSV, providing greater visibility and control over your SMS spend. [Learn more](../mobile/sms-usage-report.md)

* **Estimated Clicks for SMS report** - A new Estimated Clicks metric is now available in Journeys, Campaigns, and Channel reports for email and SMS. This metric excludes identified bot and non-human interaction (NHI) traffic to provide a clearer view of genuine customer engagement. The existing Clicks metric remains available and continues to report total clicks.

+++ Coming soon — **Information below is subject to change.**

* **LINE Channel - Authoring changes** - The LINE channel UI has been upgraded with advanced message authoring capabilities. This release introduces support for **multiple message formats**, including Text, Image, Imagemap, Carousel, and Flex (JSON Editor), alongside real-time device previews. Users can now manage grouped messages of up to five ordered messages (with add, remove, and reorder controls) and leverage the integrated personalization editor for validated, dynamic messaging.

+++

### Usability improvements {#june-26-usability}

* **Folders for Journeys** - You can now organize your journeys into **folders** to improve navigation and management in the interface. [Read more](../building-journeys/journey-ui.md#journeys-folders)

  Availability date: June 30, 2026

<!--
+++ Coming soon — **Information below is subject to change.**

* **Override the default execution field in campaigns** - Previously available at the journey level, you can now override the default execution field set globally for your Email, SMS and WhatsApp deliveries in the campaign parameters.

  Availability date: Early June, 2026

+++
-->

