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

+++ Coming soon — **Information below is subject to change.**

The following journey capabilities are expected in the upcoming days or weeks.

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
<!--<p><img src="assets/do-not-localize/expression-assistant.gif"></p>-->
<p>Availability date: June 2, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Simulation (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Previously released in Limited Availability, Journey Simulation is now available to all environments. With this General Availability release, you can now use Journey Agent to generate simulated users and events directly in the Simulation menu.</p>
<p>Availability date: Early June, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Automatic completion for non-recurring Read Audience journeys** - Non-recurring **Read Audience** journeys now automatically transition to **Stopped** status once the last active profile exits. Previously, these journeys remained **Live** until the 91-day global timeout expired — even when no profiles were flowing through them anymore. With this improvement, journey status reflects actual execution state as soon as it completes, keeping your journey inventory accurate without manual intervention.

  Note that this behavior does not apply to journeys that include nodes causing waiting periods, such as Wait nodes, Reaction nodes, or event-triggered transitions. These journeys remain subject to the standard 91-day global timeout.

  Availability date: Early June, 2026

* **Certificate-Based Custom Authentication in custom actions** - Custom actions now support Certificate-Based Custom Authentication. By adding `subType: "certificateCredential"` to a custom authorization configuration, Journey Optimizer uses Adobe's managed certificate to sign a JWT client assertion and exchange it for an access token — no client secret required. Designed for enterprise APIs that enforce certificate-based identity verification, such as Azure Entra ID.

  Availability date: Early June, 2026

* **Supplemental identifier support for external audiences** - Supplemental identifiers in journeys are now supported for external audiences, including audiences imported from a CSV file and audiences created with Federated Audience Composition. You can designate any non-identity attribute or non-person identity attribute from the audience as the supplemental ID, no schema labeling is required.

  Availability date: Early June, 2026

+++

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

### Campaigns {#may-26-campaigns}

* **Customer alerts for campaign lifecycle events** - New system alerts now notify you of key lifecycle events for Action and API-triggered campaigns. Subscribe at the sandbox level. [Read more](../reports/alerts.md)

  Availability date: June 1, 2026

+++ Coming soon — **Information below is subject to change.**

* **Override the default execution field in campaigns** - Previously available at the journey level, you can now override the default execution field set globally for your Email, SMS and WhatsApp deliveries in the campaign parameters.

  Availability date: May 22, 2026

+++

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

+++ Coming soon — **Information below is subject to change.**

The following Decisioning capability is expected in the upcoming days or weeks.

<table>
<thead>
<tr>
<th><strong>Decisioning support in Direct Mail channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add Decision policies into Direct Mail journeys and campaigns. Decision policies are containers for your offers that leverage the Decisioning engine to dynamically return the best content for each audience member. Direct Mail decisioning also supports batch decisioning use cases, enabling you to export the corresponding offer items for every profile in a given Adobe Experience Platform audience.</p>
<!--<p><img src="assets/do-not-localize/exd-dm.gif"></p>-->
<p>Availability date: June 1, 2026</p>
</td>
</tr>
</tbody>
</table>

+++

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

* **WhatsApp channel context data** - Journey Optimizer now captures additional interaction data returned from the WhatsApp channel and stores it in the **AJO EmailTrackingExperienceEvent Dataset** under the `whatsAppChannelContext` field group.

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

### Administration {#may-26-admin}

### URL parameter encryption {#may-26-url-parameter-encryption}

* **URL parameter encryption** - You can now encrypt URL parameters in tracking and landing page links added to your email messages. This provides an additional layer of security for sensitive parameter data. Previously released in Limited Availability, this capability is now available to all environments (General Availability). [Read more](../personalization/url-parameter-encryption.md)

  Availability date: June 1, 2026

+++ Coming soon — **Information below is subject to change.**

* **Message Feedback Event Dataset moving to batch ingestion** - The `AJO Message Feedback Event Dataset` is transitioning from streaming to batch ingestion mode. This change ensures that data ingestion does not exceed streaming ingestion limits. If you use this dataset in Customer Journey Analytics reports or run queries against it, expect an increase in data latency of up to 2 hours going forward.

  Availability date: June 1, 2026

+++

### Reporting {#may-26-reporting}

+++ Coming soon — **Information below is subject to change.**

* **Exclude bot clicks for email and SMS reporting** - New estimated metrics are now available to help filter out non-human (bot) interactions from email and SMS reporting. These include estimated clicks, click-through rates (CTR), and click-to-open rates (CTOR), providing a more accurate view of real customer engagement. Existing metrics remain unchanged, and these new metrics can be used alongside current reporting for improved analysis.

  Availability date: June 1, 2026

+++

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

+++ Coming soon — **Information below is subject to change.**

* **Folders for journeys and campaigns** - You can now organize your journeys and campaigns into folders to improve navigation and management in the interface.

  Availability date: June 2, 2026

+++
