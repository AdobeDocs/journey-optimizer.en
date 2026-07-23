---
solution: Journey Optimizer
product: journey optimizer
title: Pre release notes for Journey Optimizer
description: Adobe Journey Optimizer Pre Release notes
feature: Release Notes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
TQID: https://experienceleague.adobe.com/951PJzmmITN1nSUapVomlYnPws9pS0TosI1Gl3R9yL4
hide: true
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

<!--
## June '26 pre-release notes {#june-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production. While most changes are delivered on the release date, a few may roll out later — refer to the Availability Date listed for each entry for details.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: June 16-17, 2026

### Journeys {#june-26-journeys}

The following capabilities and improvements are coming to journeys in this release.




### Orchestrated campaigns {#june-26-oc}

The following capabilities and improvements are coming to orchestrated campaigns in this release.

-->

## July '26 pre-release notes {#july-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production. While most changes are delivered on the release date, a few may roll out later.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: July 28, 2026

### Loyalty {#july-26-loyalty}

Journey Optimizer introduces Loyalty, a new capability in this release.

<table>
<thead>
<tr>
<th><strong>Loyalty Challenges</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Loyalty Challenges turn loyalty initiatives into engaging, gamified experiences that motivate customers to take valuable actions, such as making purchases, writing reviews, or engaging on social media.</p>
<p>Administrators can use the Loyalty admin menu to connect Journey Optimizer with your loyalty ecosystem, including reward fulfillment APIs, event definitions, product inventory, exclusions, and identity settings. Marketers can then design standard, streak, or sequential challenges, define tasks and rewards, deliver branded content cards and messages, and monitor performance with built-in reporting dashboards. Journey Optimizer generates the journeys that orchestrate each challenge in the background, so teams can focus on the customer experience and business goals.</p>
<p>Loyalty also introduces a Coworker skill that lets teams perform key challenge operations more efficiently, including creating challenges, setting challenge properties, managing audiences and related configuration, and reviewing insights to monitor challenge participation and reward performance.</p>
<!-- GIF placeholder: to be added -->
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-14019">DOCAC-14019</a></p>
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

<!--

### Onboarding {#july-26-onboarding}

Journey Optimizer introduces the Onboarding Assistant, a new capability in this release.

<table>
<thead>
<tr>
<th><strong>Onboarding Assistant</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Transitioning to Adobe Journey Optimizer from another marketing platform is easier with guided capabilities that help you move existing email content and journeys into Journey Optimizer. A dedicated workspace lets you reuse what you have instead of rebuilding from scratch.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<GIF placeholder: to be added>
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-15180">DOCAC-15180</a></p>
<Documentation link: TBD>
</td>
</tr>
</tbody>
</table>

-->

### Journeys {#july-26-journeys}

The following capabilities and improvements have been added to journeys in this release.

<table>
<thead>
<tr>
<th><strong>Channel optimization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now configure a journey action to include multiple outbound channels (Email, Push, SMS) and let Journey Optimizer automatically deliver through the best channel for each customer. Three optimization modes are available:</p>
<ul>
<li>Manual ranking: specify your preferred channel order.</li>
<li>Customer preference: use the customer's preferred channel from their profile (Experience Data Model Consents & Preferences attribute).</li>
<li>AI model-based ranking: use machine learning propensity scores to infer the most effective channel per customer.</li>
</ul>
<p>When the top-ranked channel is unavailable (not opted-in, frequency-capped, or not configured), the system falls back to the next available channel.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-14900">DOCAC-14900</a></p>
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Document support of external audiences Federated Audience Composition in Journey Simulation** - Journey Simulation now supports External Audiences. When simulating journeys targeting Federated Audience Composition audiences, you can mock enrichment attributes from those audiences directly through the UI form or a JSON import. The UI dynamically displays only the specific enrichment attributes used in your journey logic, enabling precise validation of decision branches and personalization rules prior to going live. ([DOCAC-15074](https://jira.corp.adobe.com/browse/DOCAC-15074)) <!-- Documentation link: TBD -->

* **Start and end dates in the journey header** - When start and/or end dates are configured on a live journey, they are now surfaced in the journey header next to the live status badge. The displayed label adapts based on whether each date is upcoming or has already passed. ([DOCAC-14702](https://jira.corp.adobe.com/browse/DOCAC-14702)) <!-- Documentation link: TBD -->

### Orchestrated campaigns {#july-26-oc}

The following improvement has been added to orchestrated campaigns in this release.

* **View Orchestrated Campaign Transitions permission** - Added a new **View Orchestrated Campaign Transitions** permission to replace the legacy **View File in Orchestrated Campaigns** option. This change allows you to hide preview results within campaign transitions to support personally identifiable information compliance. ([DOCAC-14924](https://jira.corp.adobe.com/browse/DOCAC-14924))

<!--
<table>
<thead>
<tr>
<th><strong>Quiet Hours support for orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now apply quiet hours to Orchestrated campaigns. Quiet hours let you define time-based exclusions to prevent messages from being sent during specific periods, helping you respect customer preferences and compliance requirements across campaign orchestration use cases.</p>
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-14054">DOCAC-14054</a></p>
<Documentation link: TBD>
</td>
</tr>
</tbody>
</table>

* **Ability to Manage Profile Target Dimensions** - You can now delete a Profile Target Dimension or edit and swap its configured identity namespace, providing greater control and flexibility over your data setups. ([DOCAC-15018](https://jira.corp.adobe.com/browse/DOCAC-15018)) 

* **Support for Line** - You can now add LINE actions directly into your Orchestrated campaigns. This new activity allows you to build and deliver highly personalized content, including text, stickers, images, videos, location data, and rich Flex Messages, to engage your customers seamlessly on the LINE platform. This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative. ([DOCAC-14905](https://jira.corp.adobe.com/browse/DOCAC-14905))

* **New Orchestrated campaigns public APIs** - New API specifications are now available for Orchestrated campaigns. These APIs allow you to programmatically create, manage, and trigger orchestrated campaigns, enabling deeper integration with external systems and automation pipelines. ([DOCAC-14308](https://jira.corp.adobe.com/browse/DOCAC-14308))

* **Personalize email sender details per recipient and campaign** - Orchestrated campaigns now support personalization of email header fields, including From name, From address, and Reply-To, using profile attributes or relational data. This allows sender details to reflect the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address. Header values can be set at the channel level and overridden per campaign using contextual data for more precise control. ([DOCAC-13761](https://jira.corp.adobe.com/browse/DOCAC-13761)) Documentation link: TBD 

* **Target dimension simplification in Orchestrated campaigns** - The active targeting dimension is now shown on the workflow canvas, so you can see which dimension is used by a channel activity. The multi-entity segmentation flow is simpler as you no longer need a separate "Change dimension" activity. Moreover, you can now choose explicitly whether messages are sent at the profile level or at a secondary dimension level. ([DOCAC-13554](https://jira.corp.adobe.com/browse/DOCAC-13554))

-->

### Campaigns {#july-26-campaigns}

The following capabilities and improvements have been added to campaigns in this release.

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
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-15186">DOCAC-15186</a></p>
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Inbound experience simulation in Action campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now simulate inbound channel actions in Action campaigns before going live. Use simulation mode to test your configuration with simulated users and preview the rendered experience, including a generated URL and QR code, so you can validate rules, decisioning, and content rendering end-to-end.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<GIF placeholder: to be added>
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-15166">DOCAC-15166</a></p>
<Documentation link: TBD>
</td>
</tr>
</tbody>
</table>

* **Folders for Campaigns** - You can now organize your campaigns into folders to improve navigation and management in the interface. ([DOCAC-15098](https://jira.corp.adobe.com/browse/DOCAC-15098)) <!-- Documentation link: TBD -->

* **Override the default execution field in campaigns** - Previously available at the journey level, you can now override the default execution field set globally for your Email, SMS and WhatsApp deliveries in the campaign parameters. ([DOCAC-14718](https://jira.corp.adobe.com/browse/DOCAC-14718)) <!-- Documentation link: TBD -->

* **Brand alignment score in Campaign dashboard** - You can now assess your brand alignment score directly within your Campaign dashboard to ensure content stays on-brand. This allows you to verify guidelines at a glance without having to open the content designer. ([DOCAC-14516](https://jira.corp.adobe.com/browse/DOCAC-14516)) <!-- Documentation link: TBD -->

### Decisioning {#july-26-decisioning}

The following improvements have been added to Decisioning in this release.

* **Decisioning rules creation from natural language expression** - You can now describe the Decisioning rule you want to create in plain language and let AI generate it for you. This capability is available to customers with access to Adobe AI capabilities. ([DOCAC-15231](https://jira.corp.adobe.com/browse/DOCAC-15231)) <!-- Documentation link: TBD -->

* **Decisioning rules and ranking formulas simulation** - You can now simulate your Decisioning rules and ranking formulas directly from the rule or formula editor. Add manual test variants or generate them using AI, then run the expression against your test data to validate eligibility and review ranked results, all before deploying to production. Variants generation is available to customers with access to Adobe AI capabilities. ([DOCAC-15227](https://jira.corp.adobe.com/browse/DOCAC-15227)) <!-- Documentation link: TBD -->

* **Personalization at the offer level** - Decision item custom attributes can now be personalized at delivery time using profile, contextual, and audience data. This removes the need to maintain duplicate offers for minor content variations, allowing marketers to manage fewer, more flexible decision items. ([DOCAC-14899](https://jira.corp.adobe.com/browse/DOCAC-14899)) <!-- Documentation link: TBD -->

<!--
* **Placement-level frequency capping in Decisioning** - Frequency capping rules in Decisioning can now be scoped to individual placements, giving you finer control over how often an offer is shown in a given surface. Two modes are available: placement-specific capping (define a cap that applies only when the offer is displayed in a selected placement) and per-placement capping (apply a cap independently across every placement where the offer appears, so each placement maintains its own capping counter). ([DOCAC-14980](https://jira.corp.adobe.com/browse/DOCAC-14980)) Documentation link: TBD
-->

### Content management {#july-26-content}

The following improvements have been added to content management in this release.

* **Expression fragments support in `<head>` of email templates** - Expression fragments can now be used in the `<head>` of email templates. This allows you to centralize styling or any custom code in a single fragment and reuse it across multiple templates. When a fragment is updated and republished, all emails built from templates referencing it automatically inherit the latest code — eliminating the need to manually update each email individually. ([DOCAC-15257](https://jira.corp.adobe.com/browse/DOCAC-15257)) <!-- Documentation link: TBD -->

* **"AI Assistant" renamed to "Generate content"** - AI Assistant has been renamed to Generate Content throughout Adobe Journey Optimizer. This update is limited to naming and terminology; no functional changes have been introduced. Navigation labels, buttons, menus, and dialogs for content generation, image generation, personalization expressions, and content experimentation have been renamed from "AI Assistant" to "Generate Content." ([DOCAC-15230](https://jira.corp.adobe.com/browse/DOCAC-15230)) <!-- Documentation link: TBD -->

* **Flexible Image Sourcing for AI Content Generation** - Generating content in Journey Optimizer now sources brand-approved images directly from Adobe Experience Manager Assets Essentials and up. Three modes control the balance: Assets (Digital Asset Management-sourced, default), Balanced (Digital Asset Management-first, AI fills gaps), and Creative (AI-first). This ensures every visual is accurate, brand-compliant, and production-ready for journeys and campaigns. ([DOCAC-14761](https://jira.corp.adobe.com/browse/DOCAC-14761)) <!-- Documentation link: TBD -->

* **Multilingual improvements** - Language Settings can now be duplicated from an existing active setting, so you no longer need to fully rebuild a configuration to make changes. You can also copy a condition from one locale to another while authoring Language Settings, streamlining setup for sites with many languages.
([DOCAC-15268](https://jira.corp.adobe.com/browse/DOCAC-15268)) 

<!--
### Integrations {#july-26-integrations}

The following improvements have been added to integrations in this release.

* **Real-time countdown timers for Adobe Experience Manager Dynamic Media integration** - Marketers can now build countdown timers as Dynamic Media templates in Adobe Experience Manager and pull them directly into Journey Optimizer. Timers render live at the moment of open, so every recipient sees an accurate countdown, not a static image. Configure dates, styling, and fallback values right within the Journey Optimizer editor to power flash sales and limited-time offers. ([DOCAC-13801](https://jira.corp.adobe.com/browse/DOCAC-13801)) [Documentation link: TBD]
-->

### Email channel {#july-26-email}

The following capabilities have been added to the email channel in this release.

<table>
<thead>
<tr>
<th><strong>Modules in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Email Designer now includes a library of ready-to-use layout modules — such as headers, product cards, information blocks, and footers — that you can drag and drop directly into your email canvas. Each module comes pre-configured with editable properties (image, title, text, button, links) and can be fully customized through the WYSIWYG interface, speeding up email creation without requiring you to build structures from scratch.</p>
<!-- GIF placeholder: to be added -->
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-14877">DOCAC-14877</a></p>
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

### Personalization {#july-26-personalization}

The following improvements have been added to personalization in this release.

* **Manage domains for complete/base URL personalization** - You can now create and manage approved domains for complete and base URL personalization directly from the Administration settings in Adobe Journey Optimizer, without having to contact Adobe Support. ([DOCAC-15187](https://jira.corp.adobe.com/browse/DOCAC-15187)) <!-- Documentation link: TBD -->

* **New helper functions in personalization expressions** - New helper functions are now available in personalization expressions:

  * `appendQueryParams`: Appends a query parameter to a URL, or replaces it if the key already exists.
  * `dateBetween`: Checks whether a date falls within a start and end date range (inclusive).
  * `equalsAnyIgnoreCase`: Returns true when a string matches any provided value, ignoring case.
  * `getUrlFragment`: Extracts the fragment portion of a URL (the part after #).
  * `join`: Concatenates array elements into a single string using a separator.
  * `decode64`: Decodes a Base64-encoded string. If the input is not valid Base64, the original input string is returned unchanged.
  * `parseJson`: Parses a JSON string into a structured variable that can be used in the template.
  * `valueAtPath`: Assigns a value from a data path to a template variable, with optional indexing to extract a specific element from arrays or collections.

  The `concat` function has also been enhanced and now supports two or more arguments.

  In addition, the following Template Migration Functions are now available to assist with migrating existing templates to Journey Optimizer:

  * `ampCompare`: Compares two values using the specified comparison operator.
  * `ampSubstr`: Returns a portion of a string between the specified start and end indices.
  * `compareTo`: Compares two strings lexicographically.

  ([DOCAC-15099](https://jira.corp.adobe.com/browse/DOCAC-15099)) <!-- Documentation link: TBD -->

### Channels {#july-26-channels}

The following capabilities and improvements have been added to channels in this release.

<table>
<thead>
<tr>
<th><strong>Custom outbound channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now introduces Custom channels, a new capability that lets administrators bring any outbound HTTP-based messaging channel — such as WeChat, Kakao Talk, Messenger, or a proprietary provider — directly into Journey Optimizer through a no-code Channel Builder. Once configured, custom channels are available across Campaigns, Journeys, and Orchestrated Campaigns, with the same full set of capabilities as native channels: personalization with the expression editor, content experimentation, preview and proof, out-of-the-box reporting, and consent and governance enforcement. This fills a gap previously addressed by Custom Actions, which are limited only to Journeys and lack dedicated channel capabilities.</p>
<p>Custom outbound channels is currently available as Limited Availability. To gain access, contact your Adobe representative.</p>
<!-- GIF placeholder: to be added -->
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-11381">DOCAC-11381</a></p>
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **WhatsApp Channel: Support WhatsApp Flow templates** - You can now send WhatsApp Flow templates in Adobe Journey Optimizer to deliver interactive multi-screen experiences like surveys and lead capture. Responses are captured upon submission and stored as raw JSON payloads in the new Journey Optimizer Channel Tracking Event Dataset. ([DOCAC-15223](https://jira.corp.adobe.com/browse/DOCAC-15223)) <!-- Documentation link: TBD -->

* **Performance Add-on for throughput - Push** - A new high throughput transactional messaging mode is available in API-triggered campaigns. This mode is designed for large-scale, real-time transactional messaging and supports up to 5,000 transactions per second with higher availability. Previously only available for the email channel, this capability is now also available for the push channel, for organizations that have purchased the Adobe High Throughput Transactional Messaging add-on offering. Contact your Adobe representative for more details. ([DOCAC-14717](https://jira.corp.adobe.com/browse/DOCAC-14717)) <!-- Documentation link: TBD -->

* **Enhanced Custom Provider Integrations - Mobile** - Custom provider integrations now offer expanded flexibility with key messaging and header updates:

  * Header Customization: You can now edit the default Content-Type header value and add up to 10 custom header parameters.

  * SMS Payload Support: Added support for Adobe Journey Optimizer helper functions within the SMS payload, including encode64.

  ([DOCAC-15269](https://jira.corp.adobe.com/browse/DOCAC-15269))

### Administration {#july-26-administration}

The following capabilities have been added to administration in this release.

<table>
<thead>
<tr>
<th><strong>Web Application Firewall IP whitelisting</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports Web Application Firewall IP whitelisting for landing pages, enabling organizations to enforce that all incoming requests are routed exclusively through their configured Web Application Firewall infrastructure. With this enhancement, customers can configure Journey Optimizer to reject any direct requests that bypass the Web Application Firewall layer, ensuring that security policies defined in tools such as Imperva are consistently applied.</p>
<p>This capability strengthens the security posture for enterprises with strict network access requirements, giving them full control over the traffic flow to their Journey Optimizer-hosted landing pages.</p>
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-14814">DOCAC-14814</a></p>
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>
