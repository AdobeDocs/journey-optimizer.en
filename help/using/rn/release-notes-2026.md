---
solution: Journey Optimizer
product: journey optimizer
title: Release notes 2026
description: Journey Optimizer 2026 Release notes
feature: Release Notes
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: 65ca94cf-8e17-4a25-90f3-238083f81477
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
---
# Release Notes 2026 {#release-notes-2026}

This page lists all the features and improvements for [!DNL Journey Optimizer] released in 2026.


## May '26 release notes {#may-26-rn}

### Journeys {#may-26-journeys}

The following capabilities and improvements have been added to journeys in this release. Additional changes are also expected in the upcoming days or weeks.

<table>
<thead>
<tr>
<th><strong>Journey Fragments (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create <strong>Journey Fragments</strong> in Adobe Journey Optimizer. Journey Fragments are reusable sets of journey nodes that you can build once and drop into any journey across your sandbox. Whether it's an eligibility check, a preferred channel routing logic, or a welcome sequence, fragments help teams move faster and stay consistent, without rebuilding the same logic from scratch every time.</p>
<p>Once created, fragments are stored in a dedicated <strong>Fragment Inventory</strong> and can be inserted into any journey using the <strong>Journey fragments</strong> activity.</p>
<!--<p><img src="assets/do-not-localize/journey-fragments.gif"></p>-->
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../building-journeys/journey-fragments.md">detailed documentation</a>.</p>
<p>Availability date: May 13, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey simulation (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now set your journey to <strong>Simulation</strong>. This mode allows you to validate your logic using <strong>simulated users</strong>. These are temporary profiles created specifically for the simulation, allowing you to test freely without needing to manage persistent test profiles in Adobe Experience Platform.</p>
<p>This capability is available to all customers as a Limited Availability with essential capabilities.</p>
<p><img src="assets/do-not-localize/simulate-user.gif"></p>
<p>For more information, refer to the <a href="../building-journeys/simulate-journey.md">detailed documentation</a>.</p>
<p>Availability date: May 5, 2026</p>
</td>
</tr>
</tbody>
</table>

<!--
<table>
<thead>
<tr>
<th><strong>Journey path optimization – Targeting (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Use the new <strong>Optimize</strong> node to target specific audiences to determine the best path to meet your business-centric KPIs.</p>
<p>This tool allows you to develop more effective marketing campaigns that are more likely to resonate at the 1:1 level, improve marketing personalization efforts for customers and enhance critical customer engagement KPIs, such as conversions and revenue.</p>
<p>Previously available in Limited Availability, this capability is now available to all environments.</p>
<p>Availability date: June 1, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Arbitration – ranking formulas (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now use formulas to automatically boost journey priority scores based on customer profile attributes and contextual factors, ensuring customers enter the most relevant journeys.</p>
<p>Previously available in Limited Availability, this capability is now available to all environments.</p>
<p>Availability date: June 1, 2026</p>
</td>
</tr>
</tbody>
</table>
-->

### Orchestrated campaigns {#may-26-oc}

The following capabilities and improvements have been added to orchestrated campaigns in this release. Additional changes are also expected in the upcoming days or weeks.

<table>
<thead>
<tr>
<th><strong>Chained orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Orchestrated campaigns can now be linked together by triggering an orchestrated campaign directly from another orchestrated campaign's <strong>End activity</strong>.</p>
<p>This makes it possible to break complex orchestration logic into smaller, reusable flows that can be called from multiple parent campaigns rather than rebuilt each time. The payload passed at runtime is available for segmentation and personalization in the downstream campaign, so each linked campaign can behave based on the context it receives.</p>
<p><img src="assets/do-not-localize/oc-trigger.gif"></p>
<p>For more information, refer to the <a href="../orchestrated/trigger-orchestrated-campaign.md#signal-end">detailed documentation</a>.</p>
<p>Availability date: May 20, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Add links in Enrichment activity** - The Add Link functionality is now available in the Enrichment Activity for Orchestrated Campaigns. This allows you to create a direct relationship between your working table data and your existing database tables.

  Availability date: May 20, 2026

<!--
+++ Coming soon — **Information below is subject to change.**

The following orchestrated campaign capability is expected in the upcoming days or weeks.

<table>
<thead>
<tr>
<th><strong>File-based targeting for orchestrated campaigns (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Orchestrated campaigns now support loading a CSV or TXT file directly into the campaign canvas as the targeting audience, without first ingesting the file into Adobe Experience Platform. The file data is consumed at execution time and is not persisted as an Adobe Experience Platform dataset. During file setup, you can define column mappings, data types, NULL handling, and per-column error policies. This supports ad-hoc sends or partner list campaigns where building a full ingestion pipeline is not practical.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>Availability date: June 1, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Loop-based personalization for relational data** - The personalization editor now supports a Loop block that iterates over relational collections, such as orders, accounts, or bookings, and renders one content block per record inside a single email or SMS. Collections are configured through the data picker using personalization tokens, with no expression writing required.

  Availability date: Early June, 2026

* **Personalize email sender details per recipient and campaign** - Orchestrated campaigns now support personalization of email header fields, including From name, From address, and Reply-To, using profile attributes or relational data. This allows sender details to reflect the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address.

  Header values can be set at the channel level and overridden per campaign using contextual data for more precise control.

  Availability date: Early June, 2026

+++
-->

### Decisioning {#may-26-decisioning}

The following capabilities and improvements have been added to Decisioning in this release. Additional changes are also expected in the upcoming days or weeks.

<table>
<thead>
<tr>
<th><strong>Decisioning rules and ranking formula AI optimization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>[!DNL Adobe Journey Optimizer] now uses AI to detect Decisioning rules and ranking formulas that can be simplified. In the inventory, a red indicator appears on any rule for which the AI has identified an optimization opportunity. Clicking the indicator displays the original expression alongside the AI-suggested version. From there, you can download a file to review how simulated profiles are evaluated by each version and confirm they behave identically, then replace the expression with the optimized one.</p>
<p><img src="assets/do-not-localize/rule-ai.gif"></p>
<p>For more information, refer to the <a href="../start/ai-features.md#decisioning-optimization">detailed documentation</a>.</p>
<p>Availability date: May 5, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Adobe Experience Manager content fragments in Decisioning** - You can now map Adobe Experience Manager content fragments to decision items in Decisioning and leverage them inside decision policies to deliver the right fragment to the right customer at the right time. [Read more](../integrations/aem-fragments.md#aem-decisioning)

  This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

  Availability date: May 20, 2026

* **Decision policy details from campaign summary** - From the campaign summary page, you can now review the full structure of each decision policy—including selection strategies, decision items, andfallback offers—without duplicating or editing the campaign. You can also copy a JSON summary to the clipboard for troubleshooting with Adobe Support or your engineering team. [Read more](../experience-decisioning/use-decision-policy.md#decision-policy-summary)

  Availability date: May 20, 2026 

* **Decisioning migration workflow APIs** - The API contract for creating dependency analysis and migration workflows has been updated: pass **`request-level`** as a **query parameter** on the request URL (`sandbox`, `offer`, or `decision`). Request level must no longer be sent in the JSON body. [Read more](../experience-decisioning/decisioning-migration-api.md)

  Availability date: May 6, 2026

### Email channel {#may-26-email}

The following capabilities and improvements have been added to the email channel in this release. Additional changes are also expected in the upcoming days or weeks.

<table>
<thead>
<tr>
<th><strong>Deep links in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>It is now possible to add deep links to your email content through a dedicated option in the Email Designer. This ensures users are taken directly to the right in-app content instead of being redirected to browsers or app stores, preserving context and engagement.</p>
<p>Note that although the Deeplink option is available to all customers, deep links only work if you have completed the required configuration and mobile app implementation steps.</p>
<p><img src="assets/do-not-localize/deeplinks.gif"></p>
<p>For more information, refer to the <a href="../email/deeplinks.md">detailed documentation</a>.</p>
<p>Availability date: May 12, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Restrict inheritance breaking in fragments** - When creating or editing a fragment, you can now choose whether it can be modified when used in emails. Locking a fragment ensures it stays synchronized everywhere it appears, preventing local edits that could break brand standards or compliance requirements. This setting can be updated later, applying to future usages. [Read more](../content-management/create-fragments.md#lock-visual-fragment)

  Availability date: May 21, 2026

### Mobile messaging (SMS, MMS & RCS) {#may-26-mobile}

The following capabilities and improvements have been added to mobile messaging in this release.

<table>
<thead>
<tr>
<th><strong>New Mobile Message channel and Enhanced RCS messaging</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>SMS, MMS, and RCS are now unified under a single <strong>Mobile Message</strong> action in Adobe Journey Optimizer, making it easier to manage all mobile message types from one place. As part of this update, you can now author rich media RCS messages, including images, carousels, and suggested actions, directly in Journey Optimizer through a new native authoring experience.</p>
<p>For more information, refer to the <a href="../mobile/get-started-mobile.md">detailed documentation</a>.</p>
<p>Availability date: May 20, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Character Count** - In Adobe Journey Optimizer, you can now use the Character Count to monitor the length of your SMS messages in real time. It helps you see when a message will be split into multiple segments to better manage formatting and avoid unexpected increases in sending costs. [Read more](../mobile/create-mobile-message.md)

* **SMS inbounds to a custom dataset** - In **SMS API credentials**, route **inbound SMS** to a **custom, profile-enabled Experience Event dataset** you select instead of only the default tracking dataset. [Read more](../mobile/mobile-webhook.md)

* **Webhook interface enhancement** - When configuring SMS webhooks, the user interface now includes a built-in setup guide with practical examples, making it easier to align provider payloads and troubleshoot issues without leaving the configuration flow. [Read more](../mobile/mobile-webhook.md)

* **Deep links in SMS content** - It is now possible to add deep links to your SMS content using the Url helper function. This ensures that the recipients are taken directly to the intended in-app content, without routing them through a web browser or an app store - provided you have completed the required configuration and mobile app implementation steps. [Read more](../email/deeplinks.md)

### WhatsApp channel {#may-26-whatsapp}

The following improvements have been added to the WhatsApp channel in this release.

* **WhatsApp button support and tracking** - WhatsApp templates now support **Quick reply**, **Call to action – URL**, and **Call to action – phone**, **Copy code** is not supported. Journey Optimizer sends supported buttons and tracks interactions alongside your other channel reporting.

* **WhatsApp channel context data** - Journey Optimizer now captures additional interaction data returned from the WhatsApp channel and stores it in the **AJO EmailTrackingExperienceEvent Dataset** under the `whatsAppChannelContext` field group. [Read more](../whatsapp/send-whatsapp.md#whatsapp-channel-context)

  +++ The following fields are captured and can be used to build audiences and analyze WhatsApp engagement

  * **`messageType`** – WhatsApp message type (e.g. `templateBased`, `response`)
  * **`inboundMessage`** – Inbound reply content (e.g. `stop`, `start`, `subscribe`)
  * **`inboundNumber`** – Sender ID where the inbound message was received
  * **`channelType`** – Channel category (`Utility`, `Marketing`, or `Promotional`)
  * **`profileNumber`** – Phone number from which the inbound message was received
  * **`origTimestamp`** – Original timestamp from Meta / WhatsApp
  * **`status`** – Delivery status including standardized provider feedback (`sent`, `delivered`, `bounce`, `error`, `delay`, `duplicate`, `denylist`, `exclude`, or `unknown`) and the raw provider status message
  * **`reactionEvent`** – Content of the user response: emoji for reactions, or message text for replies to a specific message
  * **`reactionMessageID`** – ID of the original message being responded to
  * **`reactionActionName`** – Type of response action (`react`, `unreact`, or `reply`)
  * **`interactiveSelectedTitle`** – User-selected title from a WhatsApp interactive message
  * **`interactiveType`** – Interactive message type (`list reply`, `button reply`, or `button`)
  * **`interactiveSelectedDescription`** – Description of the selected WhatsApp interactive option
  * **`interactiveSelectedID`** – ID of the selected option from WhatsApp
  
  +++

### Content & Integrations {#may-26-content}

The following capabilities and improvements have been added to content management and integrations in this release.

<table>
<thead>
<tr>
<th><strong>Content Advisor Selector</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now uses the <strong>Content Advisor selector</strong>, a unified modal for selecting both Experience Manager Assets and Content Fragments. The new selector includes:</p>
<ul>
<li><strong>Browsing, searching, and filtering </strong>across all assets and fragments.</li>
<li><strong>AI semantic search</strong>: describe what you need in plain language, e.g. "coffee in the mountains", to surface contextually relevant assets based on meaning and content, not just text matches. Multi-lingual queries are also supported.</li>
<li><strong>Brief upload</strong>: upload a marketing brief to automatically surface assets that align with your campaign context based on its content and requirements.</li>
<li><strong>Dynamic Media renditions</strong>: pick and apply image renditions for dynamic assets without leaving the selector.</li>
</ul>
<p>For more information, refer to the <a href="../integrations/aem-content-advisor.md">detailed documentation</a>.</p>
<p>Availability date: May 19, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Integrations</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The <b>Integrations</b> feature allows you to connect third-party data sources directly to Adobe Journey Optimizer. By simplifying how you pull in external data and <b>composable content</b>, this feature makes it easier to deliver personalized, dynamic messaging across all your channels.</p>
<p>Previously released in Beta, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../integrations/integrations.md">detailed documentation</a>.</p>
<p>Availability date: May 4, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Cross-organization repository access in the Assets Selector** - You can now seamlessly select assets from repositories across multiple organizations directly within the Adobe Experience Manager Asset Selector.

<!--
+++ Coming soon — **Information below is subject to change.**

* **Message Feedback Event Dataset moving to batch ingestion** - The `AJO Message Feedback Event Dataset` is transitioning from streaming to batch ingestion mode. This change ensures that data ingestion does not exceed streaming ingestion limits. If you use this dataset in Customer Journey Analytics reports or run queries against it, expect an increase in data latency of up to 2 hours going forward.

  Availability date: June 1, 2026

+++
-->

### Usability improvements {#may-26-usability}

The following usability improvements were also released in May 2026.

#### Lists

* **Bulk actions** - You can now select multiple items at once in the **Campaigns**, **Fragments**, and **Templates** lists and perform bulk operations from a single action bar, including adding items to a package, moving them to a folder, editing tags, managing access, and archiving or deleting them. [Learn more](../start/search-filter-categorize.md#bulk-actions)

  ![](../start/assets/bulk-actions-campaigns.png)

* **Sorting and column resizing** - The **Campaigns**, **Fragments**, and **Templates** lists now support sorting by clicking any column header. In the Campaigns folders view, sorting and filtering by **[!UICONTROL Priority]** and **[!UICONTROL Channel configuration]** is also available. Column widths in the **Fragments** and **Templates** lists are also resizable — drag the column border to fit the data you care about most. [Learn more](../start/search-filter-categorize.md#filter-lists)

#### Content authoring

* **Inline profile attribute editing** - Inline profile attribute editing in the Email Designer was initially released in April. As part of the May release, this capability has been decoupled from AI Assistant and extended to the Push channel editor. [Learn more](../personalization/personalize.md#inline-personalization)

  ![](../personalization/assets/inline-profile-attributes.png)

* **Link URL tooltip in Push channel editor** - When a URL in any link or media field is too long to display, a tooltip icon is always visible next to the field — hover over it to see the complete URL. [Learn more](../push/design-push.md#on-click-behavior)

  ![](../rn/assets/do-not-localize/push-link-tooltip.png)

<!--
#### Simulation & Preview

* **Redesigned preview experience** - The content preview screen has been redesigned with a side-by-side layout that lets you compare how your content renders across multiple profiles at a glance, enabling quicker and more confident reviews before sending. [Learn more](../test-approve/simulate-sample-input.md#preview)

  ![](../test-approve/assets/simulation-preview-redesign.png)
-->

<!--
+++ Coming soon — **Information below is subject to change.**

* **Folders for journeys and campaigns** - You can now organize your journeys and campaigns into folders to improve navigation and management in the interface.

  Availability date: Early June, 2026

+++
-->



## April '26 release notes {#april-26-rn}

### New capabilities {#april-26-features}

The following capabilities were released in April 2026.

<table>
<thead>
<tr>
<th><strong>Incremental query activity in Orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Orchestrated campaigns</strong> now support an <strong>Incremental query</strong> activity that targets only profiles or events that are newly eligible since the last execution.

This keeps recurring campaigns focused on net-new audiences (new sign-ups, newly qualified loyalty members, and similar segments) while reducing query workloads and avoiding redundant sends over time.</p>
<p>For more information, refer to the <a href="../orchestrated/activities/incremental-query.md#incremental-query-configuration">detailed documentation</a>.</p>
<p>Availability date: April 30, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Sender parameters in email header</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With Journey Optimizer, you can now send emails where the transmitting entity (Sender) differs from the authoring entity (From). Email clients that support this will typically render it as "Sender on behalf of From" or show a "via" indicator. Fill in the optional <strong>Sender headers</strong> fields in the email channel settings to configure this capability.</p>
<p><img src="assets/do-not-localize/sender-headers.gif"></p>
<p>For more information, refer to the <a href="../email/header-parameters.md#sender-header">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>CC field in email channel settings</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now configure an optional CC (carbon copy) field in your email channel settings. Unlike BCC, CC recipients are visible to the primary recipient, enabling transparent communication and clearer ownership.</p>
<p>This allows you to automatically copy the right stakeholder on each message—such as a relationship manager or account owner—while ensuring the customer knows who to contact for follow-up.</p>
<p>The CC field supports personalization, so a single configuration can dynamically route copies based on profile data, making it scalable across multiple use cases without additional setup.</p>
<p><img src="../configuration/assets/email-config-cc.png"></p>
<p>For more information, refer to the <a href="../configuration/cc-email-field.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Copy orchestrated campaigns across sandboxes</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Sandbox Tooling now supports packaging and copying orchestrated campaigns from one sandbox to another. This eliminates the need to manually rebuild campaigns in each environment. When a campaign is packaged, its core dependent objects such as merge policies, messages, are automatically included, so the imported campaign arrives ready to configure and validate. To protect production environments, all imported campaigns land in draft status in the target sandbox, giving teams a review and approval step before any campaign goes live.</p>
<p><img src="assets/do-not-localize/oc-sandbox.gif"></p>
<p>For more information, refer to the <a href="../configuration/copy-objects-to-sandbox.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Optimizer AI Agent Integration via MCP</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now provides an <strong>MCP (Model Context Protocol) server</strong> that surfaces campaign, channel configuration, and sandbox operations directly inside any MCP-compatible application. With this integration, different personas can collaborate around the same orchestration data. Instead of writing queries against the Adobe Journey Optimizer REST API or navigating multiple UI screens, you can describe your intent conversationally and let the LLM invoke the appropriate MCP tools. This capability is currently available in Claude Web and Desktop.</p>
<p>This capability is available to all customers in Public Beta.</p>
<p>For more information, refer to the <a href="../integrations/ajo-mcp.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Arbitration – AI Models</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now use <strong>AI models</strong> in your ranking formulas to automatically boost journey priority scores based on customer profile attributes and contextual factors, ensuring customers enter the most relevant journeys.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p><img src="assets/do-not-localize/journey-arbitration-ai-models.gif"></p>
<p>For more information, refer to the <a href="../conflict-prioritization/journey-ai-models.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Adobe Express integration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The <b>Adobe Express integration</b> in Adobe Journey Optimizer lets you use Adobe Express's editing tools directly during content creation, enabling you to resize, remove backgrounds, crop, and convert assets to JPEG or PNG.
</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/express_resize.gif"></p>
<p>For more information, refer to the <a href="../integrations/express.md">detailed documentation</a>.</p>
<p>Availability date: April 23, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Optimize email for AI inboxes</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now includes a new capability that ensures your emails are optimally structured for AI-powered inboxes such as Apple Intelligence and Google Gemini in Gmail.</p>
<p>As AI assistants increasingly control how recipients read and act on email, this feature helps you generate and author content that performs well across downstream AI tasks including summarization, triage, prioritization, and intent extraction.</p>
<p><img src="assets/do-not-localize/optimize-for-ai.gif"></p>
<p>For more information, refer to <a href="../email/llm-email-optimizer.md">Optimize email for AI inboxes</a>.</p>
<p>Availability date: April 17, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>AI Assistant for Personalization Expressions</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>[!DNL Adobe Journey Optimizer] now includes <strong>AI Assistant</strong> directly in the personalization editor and the Email Designer that converts natural-language prompts into valid personalization expressions and conditional logic, no syntax expertise required. Describe the personalization you want to achieve, and AI generates ready-to-use code you can apply immediately or refine through follow-up prompts.</p>
<p>The assistant also works in reverse. Select any existing expression and ask it to explain the logic, identify issues, or suggest improvements. This makes it useful not just for authoring new expressions, but for reviewing and debugging existing ones across your team.</p>
<p><img src="assets/do-not-localize/assistant-perso.gif"></p>
<p>For more information, refer to <a href="../content-management/generative-personalization-expressions.md">AI Assistant for Personalization Expressions</a>.</p>
<p>Availability date: April 13, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey path experimentation</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Use the new <strong>Optimize</strong> node to run A/B tests or multi-armed bandit experiments to determine the best path to meet your business-centric KPIs. This tool allows you to test, vary, and customize communications, sequencing, and timing to best reach your customers.
</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>As part of the General Availability, this release introduces <strong>experiment type</strong> selection (A/B or multi-armed bandit) and <strong>Scale the winner</strong> for unitary journeys.</p>
<p><img src="assets/do-not-localize/optimize-experiment.gif"></p>
<p>For more information, refer to the <a href="../building-journeys/path-experimentation.md">detailed documentation</a>.</p>
<p>Availability date: April 7, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Inbox</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Inbox</strong> is a mobile functionality, available with Content Cards, that enables customers to create a centralized location within their app or website to display messages sent to their users. This extends the lifetime of marketing communications by ensuring messages remain accessible even after they are dismissed.</p>
<p><img src="assets/do-not-localize/inbox.gif"/></p>
<p>For more information, refer to the <a href="../inbox/inbox-gs.md">detailed documentation</a>.</p>
<p>Availability date: April 7, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Decisioning support in email channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now use <strong>Decisioning</strong> to personalize and optimize the content of your email messages. Leverage Priority Scores, Formulas, or AI Models to display the most relevant offers and content to each recipient.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability). With this General Availability release, mirror pages are now supported.</p>
<p><img src="assets/do-not-localize/exd-email.gif"></p>
<p>For more information, refer to the <a href="../experience-decisioning/create-decision-policy.md">detailed documentation</a>.</p>
<p>Availability date: April 6, 2026</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#april-26-improv}

The following improvements were also released in April 2026.

#### AI

<!--
* **Brand alignment score in Campaign dashboard** - You can now assess your brand alignment score directly within your Campaign dashboard to ensure content stays on-brand. This allows you to verify guidelines at a glance without having to open the content designer.
-->

* **Prompt Assistant enhancement** - Prompt Assistant enhances AI content generation by analyzing user prompts in real time and identifying gaps in clarity, completeness, and context. It suggests improved rewrites and provides actionable guidance to enrich prompts with key details like audience, tone, and intent. The feature also asks targeted clarifying questions to help users refine their inputs before generation. This results in more accurate, high-quality outputs with fewer iterations. [Learn more](../content-management/ai-assistant-prompting-guide.md#prompt-assistant)

  Availability date: May 5, 2026

#### Push

* **Personalize App id in channel settings** - In the Push channel configuration settings, you can now personalize the **App id** field so that each recipient can receive a push notification from the appropriate brand based on their profile information. [Read more](../push/push-configuration.md#app-id-personalization)

#### Decisioning

* **Decisioning migration workflow APIs** - The API contract for creating dependency analysis and migration workflows has been updated: pass **`request-level`** as a **query parameter** on the request URL (`sandbox`, `offer`, or `decision`). Request level must no longer be sent in the JSON body. [Read more](../experience-decisioning/decisioning-migration-api.md)

  Availability date: May 6, 2026

* **Attach fragments to decision items** - Journey Optimizer now provides the ability to attach fragments to decision items which can be leveraged in code-based experience and email campaigns through decision policies. [Read more](../experience-decisioning/fragments-decision-policies.md)

  Previously released in Limited Availability, this capability is now available to all environments (General Availability).

* **Temporarily unavailable fragments are skipped** - When using fragments in decision items, if a fragment is temporarily unavailable on Edge, it is skipped and the journey or campaign continues rendering instead of failing. [Read more](../experience-decisioning/fragments-decision-policies.md#temporary-unavailable-fragments)

  Availability date: April 14, 2026

#### Adobe Experience Manager Integrations

* **Adobe Experience Manager Content Fragment Variation Support** - You can select **Content Fragment variations** (for example language or channel variants) when inserting Adobe Experience Manager Content Fragments, with improved handling for locale and multilingual scenarios. [Read more](../integrations/aem-fragments.md#aem-variations)

  Previously released in Limited Availability, this capability is now available to all environments (General Availability).

* **Adobe Experience Manager Content Fragment context while authoring** - Your Content Fragment selection stays active as you move between text fields and content blocks, so you can add more fragment fields without reopening **Open AEM Content advisor** each time. [Read more](../integrations/aem-fragments.md)

  Previously released in Limited Availability, this capability is now available to all environments (General Availability).

#### Email design

* **Advanced HTML editor for email content** - Advanced HTML mode lets you edit the HTML source of your content in the Email Designer, add advanced expressions (such as conditions) in the source, and toggle between HTML view and Desktop view without losing your changes.

  Previously available for email content templates only, this capability is now deployed to **email** content in the Email Designer (for example, emails authored in journeys and campaigns), in addition to email content templates. It is currently in Limited Availability — contact your Adobe representative to gain access. [Read more](../email/email-expert-mode.md)

  Availability date: April 9, 2026

#### Journeys

* **Current journey payload size visible in journey properties** - The journey properties panel now displays the current size of the journey payload compared to the configured limit — for example, *1.5 MB (out of 4 MB)*. This read-only indicator helps you monitor journey complexity before publishing and avoid errors caused by the payload size limit being exceeded. [Read more](../building-journeys/journey-properties.md#journey-payload-size)

  Availability date: April 30, 2026

#### Journey Path Optimization

* **Experiment type** - You can now choose between A/B experiment (fixed split at the start) or Multi-armed bandit (automatic split with weekly weight updates) when configuring a path experiment. [Read more](../building-journeys/path-experimentation.md)

  Availability date: April 7, 2026

* **Path experimentation: Scale the Winner** - You can now automatically or manually roll out the winning path of an experiment to your full audience. Once a winner is determined, you can amplify its reach and effectiveness without constantly monitoring the experiment. [Read more](../building-journeys/path-experimentation.md#scale-winner)

  This capability is available only in unitary journeys (event-triggered and Audience qualifications). It is not available for Read audience journeys.

  Availability date: April 7, 2026

* **Conditions** - The [Optimize](../building-journeys/optimize.md) activity is the new vehicle for creating conditional paths in journeys. It replaces the former **Condition** activity, which has been removed from the UI. All conditional logic is retained and is now handled through the **Optimize** activity's conditions. [Read more](../building-journeys/conditions.md)

  Previously released in Limited Availability, this capability is now available to all environments (General Availability).

  Availability date: April 7, 2026

#### Orchestrated campaigns

* **Global variables in Orchestrated Campaigns** - Orchestrated Campaigns now support global variables that can be defined once and reused across all activities within a workflow, simplifying configuration and ensuring consistency in dynamic values, expressions, and content personalization. [Read more](../orchestrated/global-variables.md)
* **Data Modeler enhancements** - Orchestrated relational schemas now support composite keys spanning multiple fields. Loading a schema from a DDL file also brings in enumerations, and loading from either a DDL or Excel file automatically creates composite relationships between tables. In the entity relationship view, composite links now display the full set of field pairings between tables after a file is uploaded. [Read more](../orchestrated/gs-schemas.md)


## March '26 release notes {#march-26-rn}

The [New capabilities](#march-26-features) and [Improvements](#march-26-improv) sections cover capabilities already available. <!--The [Coming soon](#coming-soon) section lists features and improvements scheduled for release later in March.-->

<!--
**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the release notes, at the release date.

See also [Adobe Experience Platform pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.
-->

**Release date**: March 24-25, 2026

### New capabilities {#march-26-features}

<table>
<thead>
<tr>
<th><strong>URL parameter encryption</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>URL parameters in tracking and landing page links added to your email messages can now be encrypted, providing an additional layer of security for sensitive parameter data.</p>
<ul>
<li>Register and manage encryption keys in the dedicated <strong>Administration</strong> registry.</li>
<li>Use the new `Encrypt` helper function in expressions to encrypt sensitive data in URLs for the query parameters you want to protect at render time.</li>
</ul>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p><img src="assets/do-not-localize/encrypt-helper.gif"></p>
<p>For more information, refer to the <a href="../personalization/url-parameter-encryption.md">detailed documentation</a>.</p>
<p>Availability date: March 31, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Convert images to email content templates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now convert images into email content templates directly in Journey Optimizer. Use AI-powered analysis to automatically generate structured HTML templates from visual references, significantly reducing email design time.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/image-converter.gif"></p>
<p>For more information, refer to the <a href="../content-management/image-to-html.md">detailed documentation</a>.</p>
<p>Availability date: March 31, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Landing page custom forms</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With [!DNL Journey Optimizer], you can capture profile attributes through your landing pages.</p>
<p>Create, design and manage custom forms tailored to your needs based on a specific dataset. You can then leverage these forms in landing pages to add the profile attributes of your choice into the dataset defined for each form.</p>
<p>Previously released in Limited Availability for customers in the United States and Australia, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/forms.gif"/></p>
<p>For more information, refer to the <a href="../landing-pages/lp-forms.md">detailed documentation</a>.</p>
<p>Availability date: March 26, 2026.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Test activity in Orchestrated Campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Test</strong> activity is now available in Orchestrated Campaigns. This activity routes workflow execution to different branches based on defined conditions, enabling you to validate campaign logic and configurations before activating live deliveries.</p>
<p><img src="../orchestrated/assets/test-1.png"></p>
<p>For more information, refer to the <a href="../orchestrated/activities/test.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Dataset lookup support in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Dataset lookup</strong> activity in journeys lets you dynamically retrieve data from Adobe Experience Platform record datasets at runtime — giving you access to information that is not part of the profile or event payload, so customer interactions stay relevant and timely.</p>
<p>Previously released in Limited Availability to a restricted set of organizations, the Dataset lookup activity in journeys is now available to all customers entitled to [dataset lookup](../data/lookup-aep-data.md), while remaining in Limited Availability.</p>
<p><img src="../building-journeys/assets/aep-data-activity.png"></p>
<p>For more information, refer to the <a href="../building-journeys/dataset-lookup.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Action activity replaces channel-specific journey activities</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Following the General Availability of the <strong>Action activity</strong> in February 2026, legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) in the journey canvas are now deprecated.</p>
<p>You must now use the single Action activity to configure all channel actions, replacing the need for separate channel-specific nodes.</p>
<p>Existing journeys using legacy channel activities continue to function without any changes or migration required.</p>
<p><img src="assets/do-not-localize/action-activity.gif"></p>
<p>For more information, refer to the <a href="../building-journeys/journey-action.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Advanced HTML editor for email templates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Advanced HTML mode for email content templates lets you edit the HTML source of your content in the Email Designer, add advanced expressions (such as conditions) in the source, and toggle between HTML view and Desktop view without losing your changes.</p>
<p>This capability is available in content templates for the Email channel only. It is currently in Limited Availability — contact your Adobe representative to gain access.</p>
<p><img src="assets/do-not-localize/expert-mode.gif"/></p>
<p>For more information, refer to the <a href="../email/email-expert-mode.md">detailed documentation</a>.</p>
<p>Availability date: March 10, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Integration of custom Firefly models and third-party image generation models</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Enable seamless integration of standard and custom Firefly models, along with approved third-party image models, to provide greater flexibility, control, and brand alignment when generating images.</p>
<p>Choose the right model for your needs:</p>
<ul><li> <strong>Adobe model</strong> (powered by Firefly Image Model 4) for immediate image generation without additional setup</li><li> <strong>Partner model</strong> (powered by Gemini 2.5 Flash) for specialized capabilities</li><li><strong>Custom models</strong> (brand-specific models trained on your own assets) for on-brand generation that aligns precisely with your brand identity, style, and visual guidelines.</li></ul>
<p>For more information, refer to the <a href="../content-management/generative-models.md">detailed documentation</a>.</p>
<p>Availability date: March 2, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Live Activity for iOS</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Bring real-time experiences directly to your customers' Lock Screens and Dynamic Island with <strong>iOS Live Activity</strong> in Adobe Journey Optimizer. Deliver live updates, from order tracking and flight status to event countdowns, live scores and delivery progress, without requiring users to open your app. Keep your audience informed and engaged at exactly the right moment, right where they are.</p>
<p>Previously released in beta, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../mobile-live/get-started-mobile-live.md">detailed documentation</a>.</p>
<p>Availability date: March 3, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Agent: Channel content create</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Powered by <strong>Adobe Experience Platform Agent Orchestrator</strong>, <strong>Journey Agent</strong> is available in Journey Optimizer and enables you to analyze journeys through a natural language interface. You can now also generate and manage channel-specific content directly in Journey Agent, creating content for channels such as email and push, applying and previewing templates, refining tone and style through prompts, and opening content in <strong>Content Designer</strong> for in-context editing.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="https://experienceleague.adobe.com/docs/experience-cloud-ai/experience-cloud-ai/agents/ajo-agent.html" target="_blank">detailed documentation</a>.</p>
<p>Availability date: March 4, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>AI model monitoring</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows you to monitor the health, training status, and performance of your Decisioning AI models. This allows you to verify training success, troubleshoot failures, and understand impact on your outcomes in order to select the best offers for each customer using AI. Note that this capability is available for <strong>Decisioning</strong> only (not for legacy Decision Management models).</p>
<p>This capability is currently available for <strong>personalized optimization</strong> models only (not auto-optimization).</p>
<p><img src="assets/do-not-localize/ai-model-observability.gif"/></p>
<p>For more information, refer to the <a href="../experience-decisioning/ranking/ai-model-observability.md">detailed documentation</a>.</p>
<p>Availability date: March 9, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Trigger Orchestrated campaigns using a signal</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Orchestrated campaigns can now be triggered via an <strong>API signal</strong>. To set this up, configure the target campaign as <strong>Triggered by a signal</strong>, publish it, then fire it using an API call. Any parameters included in the API call are available as variables within the running campaign. Note that signal-triggered orchestrated campaigns remain <strong>batch</strong> campaigns and are distinct from API-triggered campaigns.</p>
<p><img src="assets/do-not-localize/oc-triggered.gif"></p>
<p>For more information, refer to the <a href="../orchestrated/trigger-orchestrated-campaign.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Transactional category in Orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>In Orchestrated campaigns, you can now set a channel activity to the <strong>Transactional</strong> category. This applies transactional channel configurations to that activity and is useful when business rules should not apply or when customers' opt-in is not required.</p>
<p><img src="assets/do-not-localize/oc-transactional.gif"></p>
<p>For more information, refer to the <a href="../orchestrated/activities/channels.md#add">detailed documentation</a>.</p>
<p>This capability will be gradually rolled out to all regions over the next few days.</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#march-26-improv}

Improvements coming with this release are listed below.

#### Personalization

* **Complete/base URL personalization** - You can personalize destination URLs using profile attributes (for example, for the domain or path). To enable this capability, provide Adobe with your list of accepted domains. [Read more](../personalization/personalization-build-expressions.md#where)

  Previously released in Limited Availability for use in journeys, this capability is now available to all environments (General Availability).

  Availability date: April 1, 2026

#### Reporting

* **Send-Time Optimization: updated controls location and new lift report** - Send-Time Optimization (STO) controls have been relocated to the Action configuration menu. Additionally, a new lift report is now available in Journeys reports to measure the impact of STO on your campaign performance metrics. [Read more](../reports/channel-report-cja.md#optimization-models)
  
  Availability date: March 27, 2026

<!--
* **Exclude bot clicks for email and SMS reporting** - Email and SMS reporting now automatically filters out bot clicks from click metrics, providing more accurate engagement data and preventing automated traffic from inflating your performance figures.

#### Email Designer

* **Email Designer displayed in Unified Shell** - The Email Designer is now displayed within the Unified Shell experience, providing a consistent navigation and header experience that aligns with other Adobe applications.

* **Text mode support in fragments** - To support text-based email workflows, you can now create and manage text versions of your visual fragments for optimal use in the plain text version of emails that include that fragment.

  **Caution:** When using a fragment that was created before the current release, the fragment text version may be incorrectly rendered—both in the Email Designer and in the final email delivered to your recipients. For best results with older fragments, edit, save and republish each fragment.
-->

#### Configuration

<!--* **Folders for journeys and campaigns** - You can now organize your journeys and campaigns into folders, enabling structured navigation and easier management for teams working with large volumes of content. This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.-->

* **AJO domain certificates renewal unsuccessful** - You can now subscribe to receive system alerts, either by email or in the Journey Optimizer notification center, when a domain certificate used for email deliverability is nearing expiration or has already expired. [Read more](../reports/alerts.md#alert-certificates-renewal-unsuccessful)

  Availability date: March 26, 2026

* **AJO Secondary Recipient Feedback Event Dataset rename** - The `AJO Email BCC Feedback Event` Dataset has been renamed to `AJO Secondary Recipient Feedback Event` Dataset. The impact varies depending on your situation:

  * **Existing users**: Only the display name is updated. The underlying table name remains unchanged.
  * **New users and sandboxes**: Both the display name and the table name reflect the new name.
  * **Existing users with new sandboxes**: Both the display name and the table name are updated to the new name.

  >[!NOTE]
  >
  >New datasets show the new name immediately. For older dataset names, backfill and reconciliation proceed gradually and may take several weeks to complete.

  Availability date: March 2, 2026


#### Journeys

* **Update Profile action: support for multiple profile attributes** - The **Update Profile** action activity now supports updating up to five profile attributes in a single node. Previously, each action could only update one attribute at a time, requiring multiple nodes to update several attributes. Use the new **Update another field** button to add additional field/value pairs, reducing canvas complexity and improving performance. [Learn more](../building-journeys/update-profiles.md)

* **Wave sending of outbound messages in journeys** - You can now schedule messages from Journey Optimizer journeys to be delivered in controlled batches over time. [Learn more](../building-journeys/send-using-waves.md)

  Previously released in Limited Availability for use in journeys, this capability is now available to all environments (General Availability).

  Availability date: March 16, 2026

* **Pause and resume details in journey technical details** - The journey **technical details** now include additional pause and resume information: the date and time of the last pause and resume, the display name and internal identifier of the user who performed each action, and a full set of paused journey settings such as pause behavior, maximum pause duration, and auto-resume state. [Learn more](../building-journeys/journey-properties.md)

  Availability date: March 2, 2026

#### Decisioning

* **Decisioning migration — offer and context attributes** - The Migration API entity mapping now lists **offer attributes** (`migratedofferattributes` on the Personalized offer item schema) and **context attributes** (`migratedcontextattributes` on the migration dataset schema). [Read more](../experience-decisioning/decisioning-migration-api.md#entity-mapping)

  Availability date: March 31, 2026
  
<!--
## Coming soon {#coming-soon}

The features and improvements below are planned for release later in March/early April. Release dates and scope are **subject to change without prior notice**.


WAITING RELEASE DATE CONFIRMATION * **Target dimension simplification in Orchestrated Campaigns** - The active targeting dimension is now shown on the workflow canvas, so you can see which dimension is used by a channel activity. The multi-entity segmentation flow is simpler as you no longer need a separate "Change dimension" activity. Moreover, you can now choose explicitly whether messages are sent at the profile level or at a secondary dimension level.


WAITING RELEASE DATE CONFIRMATION
* **Target dimension simplification in Orchestrated Campaigns** - The active targeting dimension is now shown on the workflow canvas, so you can see which dimension is used by a channel activity. The multi-entity segmentation flow is simpler as you no longer need a separate "Change dimension" activity. Moreover, you can now choose explicitly whether messages are sent at the profile level or at a secondary dimension level.
-->


## February '26 release notes {#feb-26-01-rn}

### New capabilities {#feb-26-01-features}


<table>
<thead>
<tr>
<th><strong>Journey arbitration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now use <strong>ranking formulas</strong> to automatically boost journey priority scores based on customer profile attributes and contextual factors, ensuring customers enter the most relevant journeys.</p>
<p><img src="assets/do-not-localize/journey-arbitration-formulas.gif"/></p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../conflict-prioritization/journey-ranking-formulas.md">detailed documentation</a>.</p>
<p>Availability date: February 24, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Action activity in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer supports a new generic <strong>Action activity</strong> that enables you to configure both single actions and multi-action inbound action groups, allowing for streamlined action configuration within the journey canvas. In particular, this new feature allows for:</p>
<ul>
<li>A simplified native action configuration within the journey canvas.</li>
<li>The capacity to create multi-action inbound action groups.</li>
<li>The ability to add optimization to any built-in channel action.</li>
<li>The ability to add both experimentation and multilingual options to any action.</li>
</ul>
<p><img src="assets/do-not-localize/action-activity.gif"/></p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../building-journeys/journey-action.md">detailed documentation</a>.</p>
<p>Availability date: February 20, 2026</p>
<p><strong>Note:</strong> All native channels are now accessible through the Action journey activity. Legacy native channel activities will be deprecated with the March release. Existing journeys that include legacy actions will continue to function as is—no migration is required.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Wave sending of outbound messages</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now schedule messages from Journey Optimizer campaigns or journeys to be delivered in controlled batches over time.</p>
<p>Wave sending offers the following benefits:</p>
<ul>
<li>Better deliverability – Spread sends over time to help maintain a strong sender reputation and reduce the risk of being flagged as spam.</li>
<li>Load control – Avoid overwhelming downstream systems (e.g. call centers, landing pages) by limiting how many messages go out at once.</li>
<li>High-volume and time-sensitive use cases – Suited to large audiences or when you need to control timing (e.g. call center capacity, ramp-up, or time-bound offers).</li>
</ul>
<p><img src="assets/do-not-localize/waves.gif"/></p>
<p>In <strong>campaigns</strong>, this capability is available to all environments (General Availability). For more information, refer to the <a href="../campaigns/send-using-waves.md">detailed documentation</a>.</p>

<p>In <strong>journeys</strong>, this capability is only available for a set of organizations (Limited Availability) – To gain access, contact your Adobe representative. For more information, refer to the <a href="../building-journeys/send-using-waves.md">detailed documentation</a>.</p>
<p>Availability date: February 19, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Migrate subdomains to custom delegation</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now migrate subdomains using the CNAME delegation mode to custom delegation directly from the interface, so you can meet stricter security policies in line with your company's guidelines without re-creating channel configurations.</p>
<p><img src="assets/do-not-localize/subdomain-migration.gif"/></p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../configuration/custom-subdomain-migration.md">detailed documentation</a>.</p>
<p>Availability date: February 19, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Web push notifications channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports <strong>Web push notifications</strong>, expanding the push channel beyond mobile. You can seamlessly deliver notifications to both <strong>mobile and desktop browsers</strong>, enabling you to reach customers directly on their devices without requiring an app. This enhancement allows you to engage users with timely, personalized messages in real time, leveraging the same authoring workflows and targeting capabilities already available for mobile push.</p>
<p><img src="assets/do-not-localize/web-push.gif"/></p>
<p>Previously released in Beta, this capability will be available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../push/push-configuration-web.md">detailed documentation</a>.</p>
<p>Availability date: February 13, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Content decision activity</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Content decision activity</strong> is now available in the journey canvas for integrating personalized offers directly into your customer journeys. This activity enables you to deliver decision-based content and reference those offers throughout your journey—in conditions for creating eligibility-based branching, in custom actions for passing offer data to external systems, and in other activities for building fully personalized customer experiences.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/content-decision.gif"/></p>
<p>For more information, refer to the <a href="../building-journeys/content-decision.md">detailed documentation</a>.</p>
<p>Availability date: February 10, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Self-service migration tooling APIs</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Migration tooling APIs are now available to programmatically migrate <strong>Decision management</strong> entities to <strong>Decisioning</strong>, featuring:</p>
<ul>
<li>Flexible migration scopes (sandbox, offer, or decision level)</li>
<li>Automated dependency analysis and validation</li>
<li>Rollback support for completed migrations</li>
<li>Detailed migration reports with object mappings</li>
</ul>
<p>For more information, refer to the <a href="../experience-decisioning/decisioning-migration-api.md">detailed documentation</a>.</p>
<p>Availability date: February 3, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Custom action monitoring</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Gain deeper insight into the health and performance of your custom action endpoints with a new monitoring dashboard and enriched journey step event data. Track successful calls, errors, throughput, response times, and queue wait times to quickly understand when, where, and why anomalies occur.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../action/reporting.md">detailed documentation</a>.</p>
<p>Availability date: February 3, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Decisioning support in SMS channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now personalize and optimize the content of your SMS messages with Decisioning. Use Priority Scores, Formulas, or AI Models to display the best content to your customers.</p>
<p>For more information, refer to the <a href="../experience-decisioning/create-decision.md">detailed documentation</a>.</p>
<p>Availability date: February 2, 2026</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#feb-26-01-improv}

Improvements coming with this release are listed below.

#### Configuration

* **Experience event usage in journey expressions** - Starting April 1, 2026, the use of experience event attributes in journey expressions will no longer be supported for organizations that have not used this capability in the last 90 days. This capability has already been unavailable for new customer organizations since July 8, 2025. For alternatives, see [Experience event lookup in journeys](../building-journeys/exp-event-lookup.md).

#### Content Management

<!--
* **Update brands with new color tab** - Brand guidelines help ensure your brand is presented consistently across all touchpoints. The new <strong>Colors</strong> section defines the standards for your brand's color system, outlining how colors are selected, organized, and applied across experiences. It ensures consistent use of primary, secondary, accent, and neutral colors to support a cohesive, accessible, and recognizable brand identity. [Read more](../content-management/brands.md)
-->

* **Use themes to convert images to email templates** - When converting an image to an email template in Journey Optimizer, you can now use a theme as input so the generated HTML follows your brand parameters. Styling such as background color, button color, fonts, line spacing, margins, and padding is applied automatically, reducing manual design work and delivering a template that is ready to use with minimal edits. [Read more](../content-management/image-to-html.md)

  Availability date: February 17, 2026.

<!--* **Text mode for fragments** - You can now create and manage text versions of your fragments, supporting workflows that rely on plain text content and providing the same flexibility as in email content. [Read more](../content-management/create-fragments.md)-->

#### Email Designer

* **Text indentation** - You can now apply customizable left indentation to the first line of paragraphs in text components directly from the properties panel. <!--The new **Indentation** control lets you define indentation in pixels or percentage via a numeric input or slider, with live preview on the canvas. -->This improves readability for long-form content such as editorials and articles. [Read more](../email/get-started-email-style.md)

  Availability date: February 18, 2026.

#### Decisioning

* **Edge inbound support for using Adobe Experience Platform data in Decisioning** - Using Adobe Experience Platform data in Decisioning now supports edge inbound use cases, in addition to email and custom actions in journeys. [Read more](../experience-decisioning/aep-data-exd.md)

  This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

* **Decisioning preview in Code-based Experience channel** - You can now preview decision items when configuring Decisioning with the Code-based Experience channel. Preview is available directly in the authoring interface before going live. [Read more](../code-based/test-code-based.md#preview-code-based)

  Availability date: February 18, 2026
  
<!--
THIS WAS FINALLY NOT RELEASED IN FEBRUARY

* **Attach fragments to decision items** - Journey Optimizer now provides the ability to attach fragments to decision items which can be leveraged in code-based experience campaigns through decision policies. [Read more](../experience-decisioning/fragments-decision-policies.md)

  Previously released in Limited Availability, this capability is now available to all environments (General Availability).

  Availability date: February 12, 2026.
-->

#### Personalization

* **Execution Metadata helper** - The `executionMetadata` helper function is now available to all Journey Optimizer customers. Use it to dynamically append contextual information to any native action and capture it in a dataset for export to external systems. [Read more](../personalization/functions/helpers.md#execution-metadata)

  Previously released in Limited Availability, this capability is now available to all environments (General Availability).

  Availability date: February 20, 2026.

#### SMS

* **SMS Webhooks** - Webhooks are now supported across all SMS providers. You can configure each webhook based on its intended purpose: Inbound webhooks to capture incoming messages and Feedback webhooks to receive delivery receipts, status updates, and other message-related events. [Read more](../mobile/mobile-webhook.md)

  Availability date: February 2, 2026.



## January '26 release notes {#jan-26-rn}

<!--**Release date**: January 27-28, 2026-->

### New capabilities {#jan-26-01-features}


<table>
<thead>
<tr>
<th><strong>Decisioning support in Push channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now personalize and optimize the content of your <strong>Push notifications</strong> with <strong>Decisioning</strong>. Use Priority Scores, Formulas, or AI Models to display the best content to your customers.</p>
<p>Experience Decisioning with push notifications requires a specific version of the Mobile SDK. Before implementing this feature, check the <a href="https://developer.adobe.com/client-sdks/home/release-notes" target="_blank">release notes</a> to identify the required version and ensure you have upgraded accordingly. You can also view all available SDK versions for your platform in <a href="https://developer.adobe.com/client-sdks/home/current-sdk-versions" target="_blank">this section</a>.</p>
<p>For more information, refer to the <a href="../experience-decisioning/create-decision.md">detailed documentation</a>.</p>
<p>Availability date: January 30, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Direct mail channel in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Previously limited to Campaigns, <strong>Direct Mail</strong> channel is now available on the journey canvas, enabling you to incorporate Direct Mail into your journeys. Direct Mail can now be used in both <strong>batch and 1:1 journey scenarios</strong>, with support for file extraction configuration and time-based frequency settings.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/dm-journey.gif"/></p>
<p>For more information, refer to the <a href="../direct-mail/get-started-direct-mail.md">detailed documentation</a>.</p>
<p>Availability date: January 29, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Quiet hours (time-based exclusions)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Quiet hours</strong> let you define time-based exclusions for Email, SMS, Push, and WhatsApp channels. They ensure that no messages are sent during specific periods of time, helping you respect customer preferences and compliance requirements. You can apply quiet hours through <strong>rule sets</strong>, which can be assigned to individual actions in campaigns or journeys for precise control.</p>
<p>Previously released in Limited Availability, this feature is now available to all environments. With this General Availability release, the feature now includes the ability for customer to queue a campaign action until the completion of Quiet Hours, and the ability to preview the activated Quiet Hours rule.</p>
<p><img src="assets/do-not-localize/quiet-hour-ga.gif"/></p>
<p>For more information, refer to the <a href="../conflict-prioritization/quiet-hours.md">detailed documentation</a>.</p>
<p>Availability date: January 29, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Message export</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Message Export</strong> capability is now available for email and SMS channels. This feature allows you to automatically export sent message content to a dedicated Experience Platform dataset, enabling you to:</p>
<ul>
<li>Meet regulatory compliance requirements (such as HIPAA)</li>
<li>Archive messages for legal claims and customer care inquiries</li>
<li>Retain copies of personalized content sent to individuals</li>
</ul>
<p>Records are retained in the AJO Message Export Dataset for 7 calendar days from ingestion. During this retention period, you can export them to your own storage via Experience Platform destinations. The feature is enabled at the channel configuration level, giving you <strong>granular control</strong> over which messages are exported.</p>
<p>This capability is only available for the email and SMS channel, for organizations that have purchased the Message Export add-on offering. For more information, contact your Adobe representative.</p>
<p><img src="assets/do-not-localize/message-export.gif"/></p>
<p>For more information, refer to the <a href="../configuration/message-export.md#message-export">detailed documentation</a>.</p>
<p>Availability date: January 28, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Direct mail channel in orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Direct mail channel is now available in orchestrated campaigns. The <strong>Direct mail activity</strong> facilitates direct mail sending within your Orchestrated campaign, for both one-time and recurring messages. It serves to automate the process of generating the <strong>extraction file</strong> required by direct mail providers. You can combine channel activities into the Orchestrated campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data.</p>
<p><img src="assets/do-not-localize/dm-oc.gif"/></p>
<p>For more information, refer to the <a href="../orchestrated/activities/channels.md#channel">detailed documentation</a>.</p>
<p>Availability date: January 28, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Agent - Create a Journey</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Agent now offers creation capabilities, enabling Journey Optimizer users to build and configure marketing journeys through a <strong>natural language interface</strong>. With these new skills, practitioners can quickly create journeys by simply describing their requirements in <strong>conversational prompts</strong>. This innovation streamlines the journey creation process, allowing marketers to concentrate on strategy rather than technical configuration.</p>
<p>For more information, refer to the <a href="../start/ai-features.md#journey-agent">detailed documentation</a>.</p>
<p>Availability date: January 12, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Action campaign retrieval API</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new Journey Optimizer API is now available, enabling you to programmatically retrieve and inspect <strong>campaign-related data</strong> such as details, versions, and configurations.</p>
<p>For more information, refer to the <a href="https://developer.adobe.com/journey-optimizer-apis/references/campaigns-retrieve" target="_blank">detailed documentation</a>.</p>
<p>Availability date: November 24, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Email Designer themes</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now quickly apply <strong>pre-approved themes</strong> to ensure <strong>brand consistency</strong> across all emails, speed up your campaign creation process, and independently produce high-quality emails while reducing dependency on design teams.</p>
<p><img src="assets/do-not-localize/themes.gif"/></p>
<p>Previously released in beta version, this capability is now available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../email/apply-email-themes.md">detailed documentation</a>.</p>
<p>Availability date: November 5, 2025</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#jan-26-01-improv}

#### AI

* **AI Assistant Content Quality Checks** - In addition to brand alignment, you can now evaluate overall <strong>content quality</strong> to uncover potential issues with <strong>readability</strong>, cohesiveness, and effectiveness, independent of your brand guidelines. These automated checks help identify unclear messaging, inconsistent tone, or structural gaps. [Read more](../content-management/brands-score.md#validate-quality). 
  
  [Discover this feature in video](https://video.tv.adobe.com/v/3470544/?learn=on).

#### Journeys

* **Combine native and Adobe Campaign message actions** - Journey Optimizer now lets you combine <strong>Adobe Campaign v7/v8</strong> message actions with <strong>native channel actions</strong> in the same journey. [Read more](../building-journeys/using-adobe-campaign-v7-v8.md)

  Availability date: January 27, 2026.

* **Custom action error response payload** - You can now define an optional <strong>error response payload</strong> for custom actions. When a call fails, the error payload is exposed in the journey context (under the action's errorResponse node) and is available in the <strong>timeout/error branch</strong>, alongside `jo_status_code`, to support richer fallback logic and debugging. [Read more](../action/about-custom-action-configuration.md#define-the-message-parameters)

  Availability date: January 27, 2026.

* **Journey payload size validation in journeys** - Journey Optimizer now validates <strong>payload sizes</strong> to help ensure optimal performance and system stability. When building or publishing journeys, you receive clear <strong>warnings and errors</strong> if payload sizes approach or exceed recommended limits, along with actionable guidance to optimize your journey configuration. This proactive validation helps you identify potential issues early and maintain journey performance. [Read more](../start/guardrails.md#journey-payload-size)

  Availability date: January 27, 2026.


* **Journey alerts** - New <strong>pre-configured alerts</strong> are available for journeys.
  * <strong>Profile Discard Rate Exceeded</strong> - Ratio of profile discards to entered profiles over the last 5 mins exceeded threshold
  * <strong>Custom Action Error Rate Exceeded</strong> - Ratio of custom action errors to successful HTTP calls over the last 5 mins exceeded threshold
  * <strong>Profile Error Rate Exceeded</strong> - Ratio of profiles-in-error to entered profiles over the last 5 mins exceeded threshold

  For more information, refer to the [detailed documentation](../reports/alerts.md).

  Availability date: October 14, 2025.

#### Orchestrated campaigns

* **Data usage label inheritance for audiences** - Labels applied in Adobe Experience Platform now automatically carry over when saving <strong>audiences</strong> in orchestrated campaigns, reducing manual <strong>DULE tagging</strong>. [Read more](../orchestrated/activities/save-audience.md)

* **Predefined filters with parameters** - You can now create <strong>predefined filters</strong> with <strong>parameters</strong> in orchestrated campaigns for reusable, editable rules. [Read more](../orchestrated/predefined-filters.md)

* **Select attributes and copy distribution values** - You can now <strong>select or copy values</strong> directly from the <strong>distribution of values</strong> view in orchestrated campaigns. [Read more](../orchestrated/build-query.md)

* **Message confirmation before send** - A <strong>confirmation step</strong> is now enabled by default before sending orchestrated campaigns to reduce accidental sends. [Read more](../orchestrated/activities/channels.md#confirm-message-sending)

* **Predefined retargeting filters** - To support easier retargeting for orchestrated campaign use cases, this release introduces new <strong>campaign feedback filters</strong>. These filters let you directly target audiences based on <strong>message engagement</strong>, such as sent, opened only, opened or clicked, or opened and clicked, and select the specific campaign or in-transition campaign you want to retarget. [Read more](../orchestrated/retarget.md)

* **Rate control support** - Orchestrated campaigns now support <strong>rate control</strong> to help you pace deliveries and align with <strong>volume constraints</strong>. [Read more](../orchestrated/activities/channels.md#rate-control)

* **Restart button** - Orchestrated campaigns now include a <strong>restart button</strong> so you can quickly <strong>re-launch runs</strong> when needed before publishing the campaign. [Read more](../orchestrated/start-monitor-campaigns.md)

* **User-generated metadata support** - The <strong>executionMetadata helper function</strong> is now available in the personalization editor for Orchestrated campaigns, enabling you to attach contextual information to any native action and store it in a dataset for export to external systems. [Read more](../personalization/functions/helpers.md#execution-metadata)

  Availability date: January 27, 2026.

* **Revert live campaigns to draft status** - You can now revert live orchestrated campaigns to draft status when they encounter execution errors or when you need to modify scheduled campaigns before they start executing. This option is available until the first message is sent. [Read more](../orchestrated/start-monitor-campaigns.md#back-to-draft)

#### Campaigns

* **Schedule Campaign using Profile Time Zone** - Campaign scheduling can now use each profile's <strong>time zone</strong> to deliver messages at the intended local time. [Read more](../campaigns/campaign-schedule.md)

  **Note**: This improvement is only be available for a set of organizations (Limited Availability).

  Availability date: January 27, 2026.

#### Permissions

* **Prevent self-approval for journeys and campaigns** - Added an option when creating or setting <strong>Approval Policy</strong> to prevent journey or campaign creators from <strong>approving their own objects</strong>. [Read more](../test-approve/approval-policies.md)

  Availability date: January 27, 2026.
