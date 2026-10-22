---
solution: Journey Optimizer
product: journey optimizer
title: Pre release notes for Journey Optimizer
description: Adobe Journey Optimizer Pre Release notes
feature: Release Notes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
TQID: 'https://experienceleague.adobe.com/951PJzmmITN1nSUapVomlYnPws9pS0TosI1Gl3R9yL4'
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: a7b2bfc5-be71-4740-b371-76fa6be8df02
    internal-label: Release notes
---

# Pre-release notes {#e-release-notes}

Adobe Journey Optimizer continuously delivers new features, enhancements to existing features, and bug fixes. Upcoming changes are listed in the **Coming soon** accordions of the [release notes](release-notes.md), and all changes are consolidated at the end of each month in the same page.

## October '26 pre-release notes {#oct-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: October 28-29, 2026

### Channels {#oct-26-channels}

The following capabilities and improvements are coming to channels in this release.

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
<p>This lets you personalize the email header fields (From name, From email prefix, Reply to name, and Reply to email), the execution address, and the list-unsubscribe values, using profile attributes or contextual data for more precise control. In particular, this allows sender details to reflect the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address.</p>
<!-- GIF placeholder: TBD -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Automated provisioning for High-Throughput API-triggered campaigns** - High Throughput transactional campaigns now include automated safeguards. Adobe Journey Optimizer validates that an organization is entitled for the High Throughput add-on before a High Throughput API-triggered campaign can be published, and the campaign's surface picker now shows only High Throughput-enabled surfaces when High Throughput mode is selected. These changes reduce the manual checks previously required to configure and validate High Throughput campaigns. <!-- Documentation link: TBD -->

<!--* **Feedback Loop OTP process for custom subdomains** - The Feedback Loop (FBL) custom subdomain configuration process has been improved by surfacing the Yahoo sender hub One-Time Password (OTP) directly within the product UI. Users can now automatically retrieve and display the OTP generated during the Yahoo sender hub domain ownership verification.-->

* **Suppression List Override at Email Action Level** - Journey Optimizer now lets you override suppression list behavior directly at the email action level in journeys and campaigns. This gives teams more flexibility for operational or compliance-critical communications that require a dedicated sending configuration, while preserving existing global suppression list controls for all other sends. This enhancement helps organizations handle exception scenarios with precision without changing their broader suppression governance model. <!-- Documentation link: TBD -->

* **Reporting webhooks available for custom channels** - You can now define a reporting webhook for a custom outbound channel and attach it to a channel configuration. Use it to enrich your Journey Optimizer reports with interaction events. <!-- Documentation link: TBD -->

### Orchestrated campaigns {#oct-26-orchestrated-campaigns}

The following improvements are coming to orchestrated campaigns in this release.

* **Increase AJO message activity limit to 25** - An orchestrated campaign can now contain up to 25 message actions, such as email, push notification, or SMS sends, on its canvas. You can now build a larger campaign as one campaign instead of splitting it into several smaller ones. <!-- Documentation link: TBD -->

* **Personalize email list unsubscribe in orchestrated campaigns (Limited Availability)** - Orchestrated campaigns now support personalization of list unsubscribe email parameters, using profile attributes or relational data. Header values can be set at the channel level and overridden per campaign using contextual data for more precise control. This capability is available in Limited Availability. Contact your Adobe representative to request access. <!-- Documentation link: TBD -->

### Coworker {#oct-26-coworker}

The following are new capabilities and improvements that are coming to Coworker in this release cycle.

* **Decisioning rule generation skill in Coworker** - Use natural language in Coworker to generate, simulate, and optimize eligibility rules and ranking formulas for Adobe Journey Optimizer Decisioning. Marketers can create, validate, and test decisioning logic faster, enabling smarter personalization and more time spent optimizing outcomes without requiring PQL syntax expertise. <!-- Documentation link: TBD -->

* **Channel Builder skill in Coworker to create a new custom channel** - This skill helps administrators create custom channels faster by guiding users through the required setup steps, such as channel configuration, authentication, throttling, and payload definition, making it easier to launch new messaging integrations with less manual effort. <!-- Documentation link: TBD -->

* **Orchestrated campaigns skills in Coworker** - You can now find and inspect orchestrated campaigns conversationally from the Coworker chat interface. This release covers four read-only capabilities: listing and filtering campaigns by status, channel, tags, or name; pulling a specific campaign's details including its channel configuration and activity structure; visualizing a campaign's canvas as a graph of its activities and connections; and retrieving execution logs to surface errors for troubleshooting. This provides teams with live visibility into campaign data without requiring API access or navigation through the Journey Optimizer user interface. Creating, editing, or publishing campaigns via Coworker is not yet supported. <!-- Documentation link: TBD -->

### Landing pages {#oct-26-landing-pages}

The following capability is coming to landing pages in this release.

<table>
<thead>
<tr>
<th><strong>Anonymous landing pages (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows you to create public landing pages accessible to anyone, and from there capture data from anonymous visitors into Experience Platform non-profile enabled datasets. You can share the landing page URL anywhere, such as in emails, SMS messages or on your website.</p>
<p>To reuse your existing Journey Optimizer branded subdomains for public landing pages, you need to migrate them to Cloudflare.</p>
<p>This capability is available in Limited Availability. Contact your Adobe representative to request access.</p>
<!-- GIF placeholder: TBD -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

<!--
### Journeys {#oct-26-journeys}

The following capabilities and improvements are coming to journeys in this release.

<table>
<thead>
<tr>
<th><strong>Update documentation on profile cap</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>&lt;TBC&gt;</p>
<GIF placeholder: TBD >
< Documentation link: TBD >
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>AI recommendation cards for journey alerts</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Journey Optimizer home page now surfaces an AI recommendation card when a journey alert fires, covering Journey Custom Action failure and Journey Anomaly Detected alerts. Selecting the card opens the associated conversation history in the full, immersive Coworker chat experience.</p>
<GIF placeholder: TBD >
<Documentation link: TBD >
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey creation from Coworker rail
</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey creation with AI is now available directly from the CX Coworker right rail, replacing the previous AI Assistant experience with a re-branded, integrated entry point for generating journeys.</p>
<GIF placeholder: TBD >
<Documentation link: TBD >
</td>
</tr>
</tbody>
</table>

* **Support Inbound action simulation in Journeys** - \<TBC\> <Documentation link: TBD >
-->

### Administration {#oct-26-administration}

The following capability and improvement are coming to administration in this release.

<table>
<thead>
<tr>
<th><strong>Custom metadata for journeys and campaigns (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Define your own business fields, such as line of business, product or cost center, in the schemas provided for Action campaigns, journeys and Orchestrated campaigns. Select up to 10 fields per entity type, then fill them in from the Metadata fields section of the properties of each journey or campaign. The values are recorded in dedicated datasets that you can use for reporting, exports and audience creation.</p>
<p>This capability is available in Limited Availability for a set of customers. Contact your Adobe representative to request access.</p>
<!-- GIF placeholder: TBD -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>
