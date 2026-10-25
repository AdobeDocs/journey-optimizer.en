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

Adobe Journey Optimizer publishes pre-release notes ahead of each monthly release to give you an early look at the new capabilities and improvements planned for that release. After the release, all changes are consolidated in the [release notes](release-notes.md).

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
<p>Email header fields and delivery settings can now be overridden at the journey or campaign action level, without requiring a separate channel configuration. From name, From email prefix, Reply-To, recipient address, and list-unsubscribe values can each be set using profile attributes or contextual data.</p><p>This change allows each individual journey or campaign to carry its own sender identity, useful when the same channel configuration serves multiple programs, regions, or teams that each need a distinct From address or reply routing.</p>
<!-- GIF placeholder: TBD -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Self-serve setup for High throughput email</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>If you have purchased the High throughput transactional messaging add-on, you can now set up High throughput for API-triggered email campaigns yourself in the product UI. Create a dedicated High throughput IP pool, then create a High throughput email channel configuration that uses it, without requesting a manual setup for each resource. </p>
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Honor tracking consent without blocking email delivery</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>To support compliance with open-tracking consent requirements such as the CNIL guidance in France, you can now honor a recipient's tracking consent without excluding them from an otherwise eligible email send. Tracking consent is stored in the Adobe Experience Platform profile and evaluated for each recipient at send time. A new <strong>Disable open tracking</strong> option in the email settings removes the Journey Optimizer open-tracking pixel for recipients who have not consented. Email delivery, content, and unsubscribe links are unaffected.</p>
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Suppression list override at Email action level** - Journey Optimizer now includes a per-action toggle that allows delivery to locally-suppressed addresses for a specific email action in a journey or campaign. This is designed for compliance scenarios where a communication must be demonstrably attempted, such as a required notification to an address that has previously bounced. This capability is available in Limited Availability for a set of customers. Contact your Adobe representative to request access.

<!--
* **Feedback Loop OTP process for custom subdomains** - The Feedback Loop (FBL) custom subdomain configuration process has been improved by surfacing the Yahoo sender hub One-Time Password (OTP) directly within the product UI. Users can now automatically retrieve and display the OTP generated during the Yahoo sender hub domain ownership verification.

  The toggle is off by default and requires explicit confirmation to enable. It applies to the local suppression list only; the global suppression list and all consent and opt-out handling remain unchanged.
-->

* **Reporting webhooks available for custom channels** - You can now define a reporting webhook for a custom outbound channel and attach it to a channel configuration. Use it to enrich your Journey Optimizer reports with interaction events. <!-- Documentation link: TBD -->

### Orchestrated campaigns {#oct-26-orchestrated-campaigns}

The following improvements are coming to orchestrated campaigns in this release.

* **Increased message activity limit for orchestrated campaigns** - Orchestrated campaigns now support up to 25 message actions on a single canvas, up from the previous limit of 10. This allows complex cross-channel orchestrations, spanning email, push, SMS, and other channels, to be built and managed as a single campaign rather than split across multiple smaller ones.

  For enterprise teams running sophisticated multi-step programs, this reduces operational overhead and simplifies publication and rollback handling when managing large campaign launches. <!-- Documentation link: TBD -->

### Coworker {#oct-26-coworker}

The following are new capabilities and improvements that are coming to Coworker in this release cycle.

* **Orchestrated campaigns skills in Coworker** - You can now find and inspect orchestrated campaigns conversationally from the Coworker chat interface. This release covers four read-only capabilities: listing and filtering campaigns by status, channel, tags, or name; pulling a specific campaign's details including its channel configuration and activity structure; visualizing a campaign's canvas as a graph of its activities and connections; and retrieving execution logs to surface errors for troubleshooting. This provides teams with live visibility into campaign data without requiring API access or navigation through the Journey Optimizer user interface. Creating, editing, or publishing campaigns via Coworker is not yet supported. <!-- Documentation link: TBD -->

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

