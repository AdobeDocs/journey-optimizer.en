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
<th><strong>File-based targeting in Orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Orchestrated campaigns now support loading a <strong>CSV or TXT file</strong> directly into the campaign canvas as the targeting audience, without first ingesting the file into Adobe Experience Platform. The file data is consumed at execution time and is not persisted as an Adobe Experience Platform dataset. During file setup, you can define column mappings, data types, NULL handling, and per-column error policies. Rows that fail validation are rejected and logged before the campaign runs, keeping the audience clean without manual pre-processing. This is particularly suited for ad-hoc sends or partner list campaigns where building a full ingestion pipeline is not practical.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>

* **Loop-based personalization for relational data in Orchestrated campaigns** - The personalization editor now supports a **Loop block** that iterates over relational collections, such as orders, accounts, or bookings, and renders one content block per record inside a single email or SMS. Collections are configured through the data picker using personalization tokens, with no expression writing required. You can preview how looped blocks render against sample data before the campaign goes live, including handling of empty collections.

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

* **Dynamic offer attributes** - Offer attributes in Decisioning can now be personalized at delivery time using profile, contextual, and audience data. This removes the need to maintain duplicate offers for minor content variations, allowing marketers to manage fewer, more flexible decision items.

* **Placement-level frequency capping in Decisioning** - Frequency capping rules in Decisioning can now be scoped to individual placements, giving you finer control over how often an offer is shown in a given surface. Two modes are available:

  * Placement-specific capping: define a cap that applies only when the offer is displayed in a selected placement.
  * Per-placement capping: apply a cap independently across every placement where the offer appears, so each placement maintains its own capping counter.

### Email {#june-26-email}

The following capabilities and improvements are coming to the email channel in this release.

<table>
<thead>
<tr>
<th><strong>Content quality checks in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now includes content quality scoring directly in the Email Designer that analyzes your email across three dimensions before launch: spelling, grammar, and punctuation; readability and tone, including flags for long sentences, passive voice, and jargon; and subject line and CTA effectiveness, scored for clarity, urgency, and structure. Each check surfaces actionable suggestions, allowing teams to catch and resolve issues without leaving the authoring interface.</p>
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
<p>Journey Optimizer now includes an option to reduce the size of your email's HTML by stripping unnecessary whitespace, comments, and redundant code — without affecting how the email renders. This can improve deliverability by avoiding size thresholds that some email providers use to flag or reject messages and may reduce load time for recipients.</p>
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
<p>You can now add rich text to customizable fragments that are used in your emails content. For example, when using the Text component as an editable field in the Email Designer, you can directly format the content (for example, bold and italics) and insert hyperlinks.</p>
</td>
</tr>
</tbody>
</table>

* **Enhanced Image to HTML converter** - A new version of the Image to HTML converter feature is now available, bringing improved accuracy for HTML generation. This update leverages higher-tier LLM models to deliver more precise and reliable HTML output from image inputs.

+++ Coming soon — **Information below is subject to change**

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
<p>Availability date: June 22, 2026</p>
</td>
</tr>
</tbody>
</table>

+++

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

<!--
### Campaigns {#june-26-campaigns}

The following improvement is coming to campaigns in this release.

* **Override the default execution field in campaigns** - Previously available at the journey level, you can now override the default **execution field** set globally for your Email, SMS and WhatsApp deliveries in the campaign parameters.
-->

### Reporting {#june-26-reporting}

The following improvements are coming to reporting in this release.

* **Estimated clicks for Email and SMS reporting** — A new **Estimated Clicks** metric is now available in Journeys, Campaigns, and Channel reports for email and SMS. This metric excludes identified bot and non-human interaction (NHI) traffic to provide a clearer view of genuine customer engagement. The existing Clicks metric remains available and continues to report total clicks.

+++ Coming soon — **Information below is subject to change**

* **New Estimated Click Metrics for Email and SMS Reporting** - To provide a more accurate view of real customer engagement, new estimated metric are now available across Journeys, Campaigns, and Channel reports. These metrics help filter out non-human interactions (NHI) and bot clicks from reporting data:

  * Estimated CTR: Estimated Clicks relative to total deliveries.
  * Estimated CTOR for email only: Estimated Clicks relative to Estimated Opens.
  
  Availability date: Late June, 2026

+++

### Configuration {#june-26-configuration}

The following improvements are coming to configuration and administration in this release.

* **Dataset moving from streaming to batch mode** - The AJO Message Feedback Event Dataset is transitioning from streaming to **batch ingestion mode**. This change ensures that data ingestion does not exceed streaming ingestion limits. If you use this dataset in Customer Journey Analytics reports or run queries against it, expect an increase in data latency of up to 2 hours going forward.

+++ Coming soon — **Information below is subject to change**

* **Web Application Firewall (WAF) IP whitelisting** - Adobe Journey Optimizer now supports Web Application Firewall (WAF) IP whitelisting for landing pages, enabling organizations to enforce that all incoming requests are routed exclusively through their configured WAF infrastructure. With this enhancement, customers can configure Journey Optimizer to reject any direct requests that bypass the WAF layer, ensuring that security policies defined in tools such as Imperva are consistently applied. This capability strengthens the security posture for enterprises with strict network access requirements, giving them full control over the traffic flow to their AJO-hosted landing pages.
  
  Availability date: Late June, 2026

+++

### Usability improvements {#june-26-usability}

The following usability improvement is coming in this release.

* **Folders for Journeys & Campaigns** - You can now organize your journeys and campaigns into **folders** to improve navigation and management in the interface.
