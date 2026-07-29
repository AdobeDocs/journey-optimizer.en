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

<table>
<thead>
<tr>
<th><strong>Channel optimization (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add multiple outbound channels (Email, Push, SMS) to a single journey action and let Journey Optimizer automatically deliver through the best channel for each customer. Three optimization modes are available: manual ranking, customer profile preference (XDM attribute), and AI model-based ranking using propensity scores. When the top-ranked channel is unavailable, the system falls back to the next available channel.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../building-journeys/channel-optimization.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

* **Increased live journey limit and new guardrails** - You can now have up to **200 active journeys**, increased from the previous limit of 100.



### Orchestrated campaigns {#june-26-oc}

The following capabilities and improvements are coming to orchestrated campaigns in this release.

-->

## July '26 pre-release notes {#july-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production. While most changes are delivered on the release date, a few may roll out later.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: July 28-29, 2026

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
<Documentation link: TBD>
</td>
</tr>
</tbody>
</table>

-->

### Journeys {#july-26-journeys}

The following improvement has been added to journeys in this release.

* **External audiences in Journey Simulation** - Journey Simulation now supports External Audiences. When simulating journeys targeting CSV or Federated Audience Composition audiences, you can mock enrichment attributes from those audiences directly through the UI form or a JSON import. The UI dynamically displays only the specific enrichment attributes used in your journey logic, enabling precise validation of decision branches and personalization rules prior to going live. <!-- Documentation link: TBD -->

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
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Folders for Campaigns** - You can now organize your campaigns into folders to improve navigation and management in the interface. This capability is available for Action and API-triggered campaigns only. <!-- Documentation link: TBD -->

* **Override the default execution field in campaigns** - Previously available at the journey level, you can now override the default execution field set globally for your Email, SMS and WhatsApp deliveries in the campaign parameters. <!-- Documentation link: TBD -->

* **Brand alignment score in Campaign dashboard** - You can now assess your brand alignment score directly within your Campaign dashboard to ensure content stays on-brand. This allows you to verify guidelines at a glance without having to open the content designer. <!-- Documentation link: TBD -->

### Orchestrated campaigns {#july-26-oc}

The following improvements have been added to orchestrated campaigns in this release.

* **View Orchestrated Campaign Transitions permission** - Added a new **View Orchestrated Campaign Transitions** permission to replace the legacy **View File in Orchestrated Campaigns** option. This change allows you to hide preview results within campaign transitions to support personally identifiable information compliance.

<!--
* **Send messages in waves** - You can now schedule outbound messages from orchestrated campaigns to be delivered in controlled batches over time. Ideal for high-volume or time-sensitive campaigns, wave sending also supports better deliverability and helps maintain a strong sender reputation by reducing the risk of being flagged as spam.
-->

<!--
### Optimization {#july-26-optimization}

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
</td>
</tr>
</tbody>
</table>
-->

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
<Documentation link: TBD>
</td>
</tr>
</tbody>
</table>

* **Ability to Manage Profile Target Dimensions** - You can now delete a Profile Target Dimension or edit and swap its configured identity namespace, providing greater control and flexibility over your data setups.

* **Support for Line** - You can now add LINE actions directly into your Orchestrated campaigns. This new activity allows you to build and deliver highly personalized content, including text, stickers, images, videos, location data, and rich Flex Messages, to engage your customers seamlessly on the LINE platform. This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

* **New Orchestrated campaigns public APIs** - New API specifications are now available for Orchestrated campaigns. These APIs allow you to programmatically create, manage, and trigger orchestrated campaigns, enabling deeper integration with external systems and automation pipelines.

* **Personalize email sender details per recipient and campaign** - Orchestrated campaigns now support personalization of email header fields, including From name, From address, and Reply-To, using profile attributes or relational data. This allows sender details to reflect the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address. Header values can be set at the channel level and overridden per campaign using contextual data for more precise control. Documentation link: TBD

* **Target dimension simplification in Orchestrated campaigns** - The active targeting dimension is now shown on the workflow canvas, so you can see which dimension is used by a channel activity. The multi-entity segmentation flow is simpler as you no longer need a separate "Change dimension" activity. Moreover, you can now choose explicitly whether messages are sent at the profile level or at a secondary dimension level.

-->

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
<p>Journey Optimizer now introduces Custom channels, a new capability that lets administrators bring any outbound HTTP-based messaging channel — such as WeChat, Kakao Talk, Messenger, or a proprietary provider — directly into Journey Optimizer through a no-code Channel Builder.</p >
<p>Once configured, custom channels are available across campaigns, journeys, and orchestrated campaigns, with the same full set of capabilities as native channels: personalization with the expression editor, content experimentation, preview and proof, out-of-the-box reporting, and consent and governance enforcement.</p>
<p>This fills a gap previously addressed by custom actions, which are limited only to journeys and lack dedicated channel capabilities.</p>
<p>Custom outbound channels are currently available as Limited Availability. To gain access, contact your Adobe representative.</p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **WhatsApp Channel: Support WhatsApp Flow templates** - You can now send WhatsApp Flow templates in Adobe Journey Optimizer to deliver interactive multi-screen experiences like surveys and lead capture. Responses are captured upon submission and stored as raw JSON payloads in the new Journey Optimizer Channel Tracking Event Dataset. <!-- Documentation link: TBD -->

* **Performance Add-on for throughput - Push** - A new high throughput transactional messaging mode is available in API-triggered campaigns. This mode is designed for large-scale, real-time transactional messaging and supports up to 5,000 transactions per second with higher availability. Previously only available for the email channel, this capability is now also available for the push channel, for organizations that have purchased the Adobe High Throughput Transactional Messaging add-on offering. Contact your Adobe representative for more details. <!-- Documentation link: TBD -->

* **Enhanced Custom Provider Integrations - Mobile** - Custom provider integrations now offer expanded flexibility with key messaging and header updates:

  * Header Customization: You can now edit the default Content-Type header value and add up to 10 custom header parameters.

  * SMS Payload Support: Added support for Adobe Journey Optimizer helper functions within the SMS payload, including encode64.

### Decisioning {#july-26-decisioning}

The following improvements have been added to Decisioning in this release.

* **Personalization at the offer level** - Decision item custom attributes can now be personalized at delivery time using profile, contextual, and audience data. This removes the need to maintain duplicate offers for minor content variations, allowing marketers to manage fewer, more flexible decision items. <!-- Documentation link: TBD -->

<!--
* **Placement-level frequency capping in Decisioning** - Frequency capping rules in Decisioning can now be scoped to individual placements, giving you finer control over how often an offer is shown in a given surface. Two modes are available: placement-specific capping (define a cap that applies only when the offer is displayed in a selected placement) and per-placement capping (apply a cap independently across every placement where the offer appears, so each placement maintains its own capping counter). Documentation link: TBD
-->

### Content management {#july-26-content}

The following improvements have been added to content management in this release.

* **Expression fragments support in `<head>` of email templates** - Expression fragments can now be used in the `<head>` of email templates. This allows you to centralize styling or any custom code in a single fragment and reuse it across multiple templates. When a fragment is updated and republished, all emails built from templates referencing it automatically inherit the latest code — eliminating the need to manually update each email individually. <!-- Documentation link: TBD -->

* **"AI Assistant" renamed to "Generate content"** - AI Assistant has been renamed to Generate Content throughout Adobe Journey Optimizer. This update is limited to naming and terminology; no functional changes have been introduced. Navigation labels, buttons, menus, and dialogs for content generation, image generation, personalization expressions, and content experimentation have been renamed from "AI Assistant" to "Generate Content." <!-- Documentation link: TBD -->

* **Flexible Image Sourcing for AI Content Generation** - Generating content in Journey Optimizer now sources brand-approved images directly from Adobe Experience Manager Assets Essentials and up. Three modes control the balance: Assets (Digital Asset Management-sourced, default), Balanced (Digital Asset Management-first, AI fills gaps), and Creative (AI-first). This ensures every visual is accurate, brand-compliant, and production-ready for journeys and campaigns. <!-- Documentation link: TBD -->

* **Multilingual improvements** - Language Settings can now be duplicated from an existing active setting, so you no longer need to fully rebuild a configuration to make changes. You can also copy a condition from one locale to another while authoring Language Settings, streamlining setup for sites with many languages.

<!--
### Integrations {#july-26-integrations}

The following improvements have been added to integrations in this release.

* **Real-time countdown timers for Adobe Experience Manager Dynamic Media integration** - Marketers can now build countdown timers as Dynamic Media templates in Adobe Experience Manager and pull them directly into Journey Optimizer. Timers render live at the moment of open, so every recipient sees an accurate countdown, not a static image. Configure dates, styling, and fallback values right within the Journey Optimizer editor to power flash sales and limited-time offers. [Documentation link: TBD]
-->

### Personalization {#july-26-personalization}

The following improvements have been added to personalization in this release.

* **Manage domains for complete/base URL personalization** - You can now create and manage approved domains for complete and base URL personalization directly from the Administration settings in Adobe Journey Optimizer, without having to contact Adobe Support. <!-- Documentation link: TBD -->

<!-- Documentation link: TBD -->

### Email Designer {#july-26-email}

The following capabilitiy has been added to the email channel in this release.

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
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>


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
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

### Usability improvements {#july-26-usability}

The following usability improvements are coming in this release.

* **Quick launch shortcuts for SMS, Push, In-App, and Codebase channels in Content Templates** - The **More actions** button in the Content Templates list now provides additional channel-specific shortcuts. For SMS templates, quickly edit the message or check the character count/segments. For Push templates, edit the title, body, or media. For In-App templates, edit the message header, message body, or media URL. For Codebase channel templates, edit the code directly. These shortcuts extend the Email channel quick launch shortcuts already available. <!-- Documentation link: TBD -->

* **New Content Simulation experience for content testing** - The **Simulate content** workflow introduces a redesigned experience: all variants now render together in a single scrollable grid (side-by-side, stacked, or wrapped layouts), replacing the one-variant-at-a-time view. A single bottom action bar consolidates navigating between test variants, zoom, viewport switching (desktop/mobile), locale switching, adding sample inputs, generating variants with AI, picking and saving simulated users, and importing or exporting variants. Removing the left rail and collapsing extra header layers gives previews significantly more room. A **Switch to classic experience** option in the bottom action bar lets you revert to the previous experience at any time. <!-- Documentation link: TBD -->
