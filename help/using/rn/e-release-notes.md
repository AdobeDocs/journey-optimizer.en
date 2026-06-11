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

# Pre-release notes {#e-release-notes}

Adobe Journey Optimizer continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md).

## June '26 pre-release notes {#june-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production. While most changes are delivered on the release date, a few may roll out later — refer to the Availability Date listed for each entry for details.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: June 16-17, 2026

### Journeys {#june-26-journeys}

The following capabilities and improvements are coming to journeys in this release.

* **Increased live journey limit and new guardrails** - You can now have up to **200 active journeys**, increased from the previous limit of 100.

* **Start and end dates in the journey header** - When start and/or end dates are configured on a live journey, they are now surfaced in the **journey header** next to the live status badge. The displayed label adapts based on whether each date is upcoming or has already passed.

* **Stop or close a paused journey directly** - You can now **stop a journey or close it to new entrances** directly from the **Paused** state. Previously, a paused journey had to be resumed to Live before it could be stopped or closed.

<!--
* **Supplemental identifier support for external audiences** - Supplemental identifiers in journeys are now supported for external audiences, including audiences imported from a CSV file and audiences created with Federated Audience Composition. You can designate any non-identity attribute or non-person identity attribute from the audience as the supplemental ID, no schema labeling is required.
-->
  
### Orchestrated campaigns {#june-26-oc}

The following capabilities and improvements are coming to orchestrated campaigns in this release.

<table>
<thead>
<tr>
<th><strong>Load file activity in Orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Orchestrated campaigns now support loading a <strong>CSV or TXT file</strong> directly into the campaign canvas as the targeting audience, without first ingesting the file into Adobe Experience Platform. The file data is consumed at execution time and is not persisted as an Adobe Experience Platform dataset. During file setup, you can define column mappings, data types, NULL handling, and per-column error policies. This supports ad-hoc sends or partner list campaigns where building a full ingestion pipeline is not practical.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>

* **Loop-based personalization for relational data in Orchestrated campaigns** - The personalization editor now supports a **Loop block** that iterates over relational collections, such as orders, accounts, or bookings, and renders one content block per record inside a single email or SMS. Collections are configured through the data picker using personalization tokens, with no expression writing required.

* **Personalize email sender details per recipient and campaign** - Orchestrated campaigns now support personalization of **email header fields**, including From name, From address, and Reply-To, using profile attributes or relational data. This allows sender details to reflect the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address. Header values can be set at the channel level and overridden per campaign using contextual data for more precise control.

<!--
* **Target dimension simplification in Orchestrated campaigns** - The active **targeting dimension** is now shown on the workflow canvas, so you can see which dimension is used by a channel activity. The multi-entity segmentation flow is simpler as you no longer need a separate "Change dimension" activity. Moreover, you can now choose explicitly whether messages are sent at the profile level or at a secondary dimension level.
-->

### Decisioning {#june-26-decisioning}

The following capability is coming to Decisioning in this release.

<table>
<thead>
<tr>
<th><strong>Leverage Adobe Experience Manager content fragment in Decisioning</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now map <strong>Adobe Experience Manager content fragments</strong> to <strong>decision items</strong> in Decisioning and leverage them inside decision policies to deliver the right fragment to the right customer at the right time.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
</td>
</tr>
</tbody>
</table>

### Channels {#june-26-channels}

The following capability is introduced in this release.

<table>
<thead>
<tr>
<th><strong>Custom outbound channels</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now introduces <strong>Custom channels</strong>, a new capability that lets administrators bring any outbound HTTP-based messaging channel — such as WeChat, Kakao Talk, Messenger, or a proprietary provider — directly into Journey Optimizer through a no-code channel builder.</p>
<p>Once configured, custom channels are available across campaigns, journeys, and orchestrated campaigns, with the same full set of capabilities as native channels: personalization with the expression editor, content experimentation, preview and proof, out-of-the-box reporting, and consent and governance enforcement. This fills the gap previously addressed by custom actions, which were limited to journeys and lacked dedicated content authoring.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>

### Email {#june-26-email}

The following capabilities and improvements are coming to the email channel in this release.

<!--
<table>
<thead>
<tr>
<th><strong>Advanced Components</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Email Designer now includes a library of ready-to-use layout components — such as Headers, Product Cards (1, 2, or 3 columns), Information blocks, and Footers — that you can drag and drop directly into your email canvas. Each component comes pre-configured with editable properties (image, title, text, button, links) and can be fully customized through the WYSIWYG interface, speeding up email creation without requiring you to build structures from scratch.</p>
</td>
</tr>
</tbody>
</table>
-->

<table>
<thead>
<tr>
<th><strong>Content check in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows users to validate their <strong>email content quality</strong> - including readability, effectiveness, and content cohesiveness - directly within the Email Designer interface.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Enable email size reduction</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>This new option allows to <strong>reduce the size of the HTML</strong> in an email by stripping out unnecessary whitespace, comments, and redundant code — without changing how the email looks. This helps improve deliverability (some email providers reject or flag oversized emails) and can speed up load time for recipients.</p>
<p>Availability date: June 10, 2026</p>
</td>
</tr>
</tbody>
</table>

* **Rich text in editable fields for fragments** - You can now add rich text to customizable fragments that are used in your emails content. For example, when using the Text component as an editable field in the Email Designer, you can directly format the content (for example, bold and italics) and insert hyperlinks.

<!--
* **Text mode support in fragments** - To support text-based email workflows, you can now create and manage text versions of your visual fragments for optimal use in the plain text version of emails that include that fragment. When using a fragment that was created before the current release, the fragment text version may be incorrectly rendered — both in the Email Designer and in the final email delivered to your recipients. For best results with older fragments, edit, save and republish each fragment.
-->

### Mobile messaging (SMS, MMS, RCS & LINE) {#june-26-mobile}

The following improvements are coming to mobile messaging in this release.

* **Unique Clicks for SMS reports** - A new **Unique Clicks** module has been introduced to SMS reports, bringing the same level of granular performance tracking to SMS that is currently available for Email reports.

* **LINE Channel - Authoring changes** - The LINE channel UI has been upgraded with advanced message authoring capabilities. This release introduces support for **multiple message formats**, including Text, Image, Imagemap, Carousel, and Flex (JSON Editor), alongside real-time device previews. Users can now manage grouped messages of up to five ordered messages (with add, remove, and reorder controls) and leverage the integrated personalization editor for validated, dynamic messaging.

* **SMS - Display Usage Metrics** - For customers purchasing SMS directly through Adobe Journey Optimizer, a new **SMS usage dashboard** has been introduced. You can now view and track your last 90 days of message sending metrics, categorized by Mobile Originated (MO) and Mobile Terminated (MT) messages. This data is also available for download via CSV, providing greater visibility and control over your SMS spend.

### Content & Integrations {#june-26-content}

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
</td>
</tr>
</tbody>
</table>

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

### Campaigns {#june-26-campaigns}

The following improvement is coming to campaigns in this release.

* **Override the default execution field in campaigns** - Previously available at the journey level, you can now override the default **execution field** set globally for your Email, SMS and WhatsApp deliveries in the campaign parameters.

### Reporting {#june-26-reporting}

The following improvements are coming to reporting in this release.

* **New Estimated Click Metrics for Email and SMS Reporting** - To provide a more accurate view of real customer engagement, new estimated metrics are now available across Journeys, Campaigns, and Channel reports. These metrics help filter out non-human interactions (NHI) and bot clicks from reporting data:
  * Estimated Clicks: Total clicks counted after removing identified bot and non-human traffic.
  * Estimated CTR: Estimated Clicks relative to total deliveries.
  * Estimated CTOR for email only: Estimated Clicks relative to Estimated Opens.

### Configuration {#june-26-configuration}

The following improvements are coming to configuration and administration in this release.

<!--
* **Web Application Firewall (WAF) IP whitelistings** - Adobe Journey Optimizer now supports WAF IP whitelisting for landing pages, enabling organizations to enforce that all incoming requests are routed exclusively through their configured WAF infrastructure. With this enhancement, customers can configure Journey Optimizer to reject any direct requests that bypass the WAF layer, ensuring that security policies defined in tools such as Imperva are consistently applied. This capability strengthens the security posture for enterprises with strict network access requirements, giving them full control over the traffic flow to their Journey Optimizer-hosted landing pages.

* **Updated batch ending throughput benchmarks with customer-facing scenarios** - Adobe Journey Optimizer's batch sending throughput benchmarks have been updated to reflect production-grade performance across multiple personalization scenarios — from basic sends to complex dynamic content with conditional logic. The refreshed metrics are now available in the product description to help customers accurately plan their messaging volumes.-->

* **Dataset moving from streaming to batch mode** - The AJO Message Feedback Event Dataset is transitioning from streaming to **batch ingestion mode**. This change ensures that data ingestion does not exceed streaming ingestion limits. If you use this dataset in Customer Journey Analytics reports or run queries against it, expect an increase in data latency of up to 2 hours going forward.

### Usability improvements {#june-26-usability}

The following usability improvement is coming in this release.

* **Folders for Journeys & Campaigns** - You can now organize your journeys and campaigns into **folders** to improve navigation and management in the interface.
