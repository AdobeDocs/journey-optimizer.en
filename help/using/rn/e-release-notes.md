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

## August '26 pre-release notes {#august-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production. While most changes are delivered on the release date, a few may roll out later.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: August 18-19, 2026

### Onboarding {#august-26-onboarding}

The following capability has been added to onboarding in this release.

<table>
<thead>
<tr>
<th><strong>Guided capabilities for onboarding emails and journeys (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Transitioning to Adobe Journey Optimizer from another marketing platform is easier with guided capabilities that help you move existing email content and journeys into Journey Optimizer. A dedicated workspace lets you reuse what you have instead of rebuilding from scratch.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15330">DOCAC-15330</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

### Journeys {#august-26-journeys}

The following capabilities and improvements have been added to journeys in this release.

<table>
<thead>
<tr>
<th><strong>Journey-level holdout</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now configure a holdout group for your journeys directly from journey properties. A holdout is a configurable percentage of your target audience that is excluded from entering the journey and receives no communication. By comparing holdout profiles against active profiles in Customer Journey Analytics reporting, you can measure the incremental lift - the true impact - that your journey delivers.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15162">DOCAC-15162</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Add new dateDiff function in journey expression editor** - The journey expression editor now includes the `dateDiff` function, which calculates the difference between two dates in number of days. This function is useful for time-based logic such as creating deadlines, calculating customer lifecycle durations, or building countdown timers in journey conditions. <a href="https://jira.corp.adobe.com/browse/DOCAC-15293">DOCAC-15293</a> <!-- Documentation link: TBD -->

* **Start and end dates in the journey header** - When start and/or end dates are configured on a journey, they are now surfaced in the journey header next to the status badge. The displayed label adapts based on whether each date is upcoming or has already passed. <a href="https://jira.corp.adobe.com/browse/DOCAC-14702">DOCAC-14702</a> <!-- Documentation link: TBD -->

### Campaigns {#august-26-camp}

The following capabilities and improvements have been added to campaigns in this release.

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
<p>This capability is currently in private beta and available to a limited set of organizations. Contact your Adobe representative for more information.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15166">DOCAC-15166</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Folders for Campaigns** - You can now organize your campaigns into folders to improve navigation and management in the interface. <a href="https://jira.corp.adobe.com/browse/DOCAC-15098">DOCAC-15098</a> <!-- Documentation link: TBD -->

* **Brand alignment score in Campaign dashboard** - You can now assess your brand alignment score directly within your Campaign dashboard to ensure content stays on-brand. This allows you to verify guidelines at a glance without having to open the content designer. <a href="https://jira.corp.adobe.com/browse/DOCAC-14516">DOCAC-14516</a> <!-- Documentation link: TBD -->

* **Override the default execution field in campaigns** - Previously available at the journey level, you can now override the default execution field set globally for your Email, SMS and WhatsApp deliveries in the campaign parameters. <a href="https://jira.corp.adobe.com/browse/DOCAC-14718">DOCAC-14718</a> <!-- Documentation link: TBD -->

### Orchestrated campaigns {#august-26-oc}

The following capabilities and improvements have been added to orchestrated campaigns in this release.

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
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-14054">DOCAC-14054</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Ability to Manage Profile Target Dimensions** - You can now delete a Profile Target Dimension or edit and swap its configured identity namespace, providing greater control and flexibility over your data setups. <a href="https://jira.corp.adobe.com/browse/DOCAC-15018">DOCAC-15018</a> <!-- Documentation link: TBD -->

* **Support for Line (Limited Availability)** - You can now add LINE actions directly into your Orchestrated campaigns. This new activity allows you to build and deliver highly personalized content, including text, stickers, images, videos, location data, and rich Flex Messages, to engage your customers seamlessly on the LINE platform. This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative. <a href="https://jira.corp.adobe.com/browse/DOCAC-14905">DOCAC-14905</a> <!-- Documentation link: TBD -->

* **New Orchestrated campaigns public APIs** - New API specifications are now available for Orchestrated campaigns. These APIs allow you to programmatically create, manage, and trigger orchestrated campaigns, enabling deeper integration with external systems and automation pipelines. <a href="https://jira.corp.adobe.com/browse/DOCAC-14308">DOCAC-14308</a> <!-- Documentation link: TBD -->

* **Personalize email sender details per recipient and campaign** - Orchestrated campaigns now support personalization of email header fields, including From name, From address, and Reply-To, using profile attributes or relational data. This allows sender details to reflect the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address. Header values can be set at the channel level and overridden per campaign using contextual data for more precise control. <a href="https://jira.corp.adobe.com/browse/DOCAC-13761">DOCAC-13761</a> <!-- Documentation link: TBD -->

* **Target dimension simplification in Orchestrated campaigns** - The active targeting dimension is now shown on the workflow canvas, so you can see which dimension is used by a channel activity. The multi-entity segmentation flow is simpler as you no longer need a separate "Change dimension" activity. Moreover, you can now choose explicitly whether messages are sent at the profile level or at a secondary dimension level. <a href="https://jira.corp.adobe.com/browse/DOCAC-13554">DOCAC-13554</a> <!-- Documentation link: TBD -->

* **Send using waves in orchestrated campaigns** - You can now schedule outbound messages from orchestrated campaigns to be delivered in controlled batches over time. Ideal for high-volume or time-sensitive campaigns, wave sending also supports better deliverability and helps maintain a strong sender reputation by reducing the risk of being flagged as spam. <a href="https://jira.corp.adobe.com/browse/DOCAC-13990">DOCAC-13990</a> <!-- Documentation link: TBD -->

### Channels {#august-26-channels}

The following capabilities and improvements have been added to channels in this release.

<table>
<thead>
<tr>
<th><strong>Decisioning support in Web Channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Decisioning is now available for the Web channel. You can use decision policies directly in the web visual editor to deliver the most relevant offers to each visitor.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-11548">DOCAC-11548</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Personalized PDF attachments in API-triggered emails</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now supports attaching up to five recipient-specific PDFs per email in API-triggered campaigns. PDF files are fetched securely from Data Landing Zone and attached at send time, with each file's location passed directly in the API payload. This allows existing upstream document generation systems to remain in place, with Journey Optimizer handling delivery.</p>
<p>Supported use cases include invoices, statements, tickets, contracts, shipping labels, and similar documents that vary per recipient. Personalized PDF attachments are available in API-triggered campaigns only and are not supported in journeys or orchestrated campaigns.</p>
<p>Larger attachment volumes and sizes are supported via the PDF attachment add-on; for information, contact your Adobe representative.</p>
<p><a href="https://jira.corp.adobe.com/browse/DOCAC-15186">DOCAC-15186</a></p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **LINE Channel - Authoring changes** - The LINE channel UI has been upgraded with advanced message authoring capabilities. This release introduces support for multiple message formats, including Text, Image, Imagemap, Carousel, and Flex (JSON Editor), alongside real-time device previews. Users can now manage grouped messages of up to five ordered messages (with add, remove, and reorder controls) and leverage the integrated personalization editor for validated, dynamic messaging. <a href="https://jira.corp.adobe.com/browse/DOCAC-14869">DOCAC-14869</a> <!-- Documentation link: TBD -->

* **Performance Add-on for throughput - Push** - A new high throughput transactional messaging mode is available in API-triggered campaigns. This mode is designed for large-scale, real-time transactional messaging and supports up to 5,000 transactions per second with higher availability. Previously only available for the email channel, this capability is now also available for the push channel, for organizations that have purchased the Adobe High Throughput Transactional Messaging add-on offering. Contact your Adobe representative for more details. <a href="https://jira.corp.adobe.com/browse/DOCAC-14717">DOCAC-14717</a> <!-- Documentation link: TBD -->

### Decisioning {#august-26-decisioning}

The following improvement has been added to Decisioning in this release.

* **Placement-level frequency capping in Decisioning** - Frequency capping rules in Decisioning can now be scoped to individual placements, giving you finer control over how often an offer is shown in a given surface. Two modes are available: placement-specific capping, which defines a cap that applies only when the offer is displayed in a selected placement, and per-placement capping, which applies a cap independently across every placement where the offer appears, so each placement maintains its own capping counter. Note that placement-related capping does not apply to offers capped using rules based on Adobe Experience Platform data. <a href="https://jira.corp.adobe.com/browse/DOCAC-14980">DOCAC-14980</a> <!-- Documentation link: TBD -->

### Email Designer {#august-26-email}

The following improvement has been added to the Email Designer in this release.

* **New Table component in the Email Designer** - The Email Designer now includes a built-in Table component, allowing you to structure content in rows and columns directly within your email. Drag and drop the component onto your canvas, customize the number of rows and columns, and style each cell independently to create clear, organized layouts without relying on custom HTML. <a href="https://jira.corp.adobe.com/browse/DOCAC-15093">DOCAC-15093</a> <!-- Documentation link: TBD -->

### Administration {#august-26-administration}

The following improvement has been added to administration in this release.

* **Feedback Loop OTP process for custom subdomains** - The Feedback Loop (FBL) custom subdomain configuration process has been improved by surfacing the Yahoo sender hub One-Time Password (OTP) directly within the product UI. Users can now automatically retrieve and display the OTP generated during the Yahoo sender hub domain ownership verification. <a href="https://jira.corp.adobe.com/browse/DOCAC-14815">DOCAC-14815</a> <!-- Documentation link: TBD -->

### Usability improvements {#august-26-usability}

The following improvements have been added to usability in this release.

* **New content simulation experience for content variants** - The **Simulate content** workflow introduces a redesigned experience: all variants now render together in a single scrollable grid (side-by-side, stacked, or wrapped layouts), replacing the one-variant-at-a-time view. A single bottom action bar consolidates navigating between test variants, zoom, viewport switching (desktop/mobile), locale switching, adding sample inputs, generating variants with AI, picking and saving simulated users, and importing or exporting variants. Removing the left rail and collapsing extra header layers gives previews significantly more room. A **Switch to classic experience** option in the bottom action bar lets you revert to the previous experience at any time. <a href="https://jira.corp.adobe.com/browse/DOCAC-15285">DOCAC-15285</a> <!-- Documentation link: TBD -->

* **Bulk operations in journey inventory** - You can now perform new bulk actions directly from the journey inventory list, making it faster to manage multiple journeys at once. Select several journeys and apply any of the following new actions in a single step: add to package, delete, move to folder, edit tags, or manage access. This reduces the need to repeat the same action one journey at a time, streamlining journey management for teams working with large numbers of journeys. <a href="https://jira.corp.adobe.com/browse/DOCAC-15358">DOCAC-15358</a> <!-- Documentation link: TBD -->

<!--
## June '26 pre-release notes {#june-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production. While most changes are delivered on the release date, a few may roll out later — refer to the Availability Date listed for each entry for details.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: June 16-17, 2026

### Journeys {#june-26-journeys}

The following capabilities and improvements are coming to journeys in this release.

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


### Campaigns {#july-26-campaigns}

The following capabilities and improvements have been added to campaigns in this release.

<!--
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
</td>
</tr>
</tbody>
</table>
-->

### Orchestrated campaigns {#july-26-oc}

The following improvements have been added to orchestrated campaigns in this release.

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

* **Send messages in waves** - You can now schedule outbound messages from orchestrated campaigns to be delivered in controlled batches over time. Ideal for high-volume or time-sensitive campaigns, wave sending also supports better deliverability and helps maintain a strong sender reputation by reducing the risk of being flagged as spam.

-->

### Channels {#july-26-channels}

The following capabilities and improvements have been added to channels in this release.

### Decisioning {#july-26-decisioning}

The following improvements have been added to Decisioning in this release.

<!--
* **Placement-level frequency capping in Decisioning** - Frequency capping rules in Decisioning can now be scoped to individual placements, giving you finer control over how often an offer is shown in a given surface. Two modes are available: placement-specific capping (define a cap that applies only when the offer is displayed in a selected placement) and per-placement capping (apply a cap independently across every placement where the offer appears, so each placement maintains its own capping counter). Documentation link: TBD
-->

### Content management {#july-26-content}

The following improvements have been added to content management in this release.

<!--
### Integrations {#july-26-integrations}

The following improvements have been added to integrations in this release.

* **Real-time countdown timers for Adobe Experience Manager Dynamic Media integration** - Marketers can now build countdown timers as Dynamic Media templates in Adobe Experience Manager and pull them directly into Journey Optimizer. Timers render live at the moment of open, so every recipient sees an accurate countdown, not a static image. Configure dates, styling, and fallback values right within the Journey Optimizer editor to power flash sales and limited-time offers. [Documentation link: TBD]
-->

### Personalization {#july-26-personalization}

The following improvements have been added to personalization in this release.


### Email Designer {#july-26-email}

The following capabilitiy has been added to the email channel in this release.


### Administration {#july-26-administration}

The following capabilities have been added to administration in this release.


### Usability improvements {#july-26-usability}

The following usability improvements are coming in this release.

* **Quick launch shortcuts for SMS, Push, In-App, and Codebase channels in Content Templates** - The **More actions** button in the Content Templates list now provides additional channel-specific shortcuts. For SMS templates, quickly edit the message or check the character count/segments. For Push templates, edit the title, body, or media. For In-App templates, edit the message header, message body, or media URL. For Codebase channel templates, edit the code directly. These shortcuts extend the Email channel quick launch shortcuts already available. <!-- Documentation link: TBD -->
