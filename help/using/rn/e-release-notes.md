---
solution: Journey Optimizer
product: journey optimizer
title: Pre release notes for Journey Optimizer
description: Adobe Journey Optimizer Pre Release notes
hide: true
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
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-14718" target="_blank">DOCAC-14718</a></p>
</td>
</tr>
</tbody>
</table>

* **Reporting webhooks available for custom channels** - You can now define a reporting webhook for a custom outbound channel and attach it to a channel configuration. Use it to enrich your Journey Optimizer reports with interaction events. <!-- Documentation link: TBD --> Jira: [DOCAC-15966](https://jira.corp.adobe.com/browse/DOCAC-15966){target="_blank"}

* **Feedback Loop OTP process for custom subdomains** - The Feedback Loop (FBL) custom subdomain configuration process has been improved by surfacing the Yahoo sender hub One-Time Password (OTP) directly within the product UI. Users can now automatically retrieve and display the OTP generated during the Yahoo sender hub domain ownership verification. <!-- Documentation link: TBD --> Jira: [DOCAC-14815](https://jira.corp.adobe.com/browse/DOCAC-14815){target="_blank"}

* **Automated provisioning for High-Throughput API-triggered campaigns** - [TBC] High Throughput transactional campaigns now include automated safeguards. Adobe Journey Optimizer validates that an organization is entitled for the High Throughput add-on before a High Throughput API-triggered campaign can be published, and the campaign's surface picker now shows only High Throughput-enabled surfaces when High Throughput mode is selected. These changes reduce the manual checks previously required to configure and validate High Throughput campaigns. <!-- Documentation link: TBD --> Jira: [DOCAC-15938](https://jira.corp.adobe.com/browse/DOCAC-15938){target="_blank"}

* **Suppression List Override at Email Action Level** - Journey Optimizer now lets you override suppression list behavior directly at the email action level in journeys and campaigns. This gives teams more flexibility for operational or compliance-critical communications that require a dedicated sending configuration, while preserving existing global suppression list controls for all other sends. This enhancement helps organizations handle exception scenarios with precision without changing their broader suppression governance model. <!-- Documentation link: TBD --> Jira: [DOCAC-15734](https://jira.corp.adobe.com/browse/DOCAC-15734){target="_blank"}

* **Channel Builder skill for creating a new custom channel** - Channel Builder skill in Coworker now helps administrators create custom channels faster. The skill guides users through the required setup steps, such as channel configuration, authentication, throttling, and payload definition, making it easier to launch new messaging integrations with less manual effort. <!-- Documentation link: TBD --> Jira: [DOCAC-15511](https://jira.corp.adobe.com/browse/DOCAC-15511){target="_blank"}

### Orchestrated campaigns {#oct-26-orchestrated-campaigns}

The following improvements are coming to orchestrated campaigns in this release.

* **Increase AJO message activity limit to 25** - An orchestrated campaign can now contain up to 25 message actions, such as email, push notification, or SMS sends, on its canvas. You can now build a larger campaign as one campaign instead of splitting it into several smaller ones. <!-- Documentation link: TBD --> Jira: [DOCAC-16143](https://jira.corp.adobe.com/browse/DOCAC-16143){target="_blank"}

* **Personalize email list unsubscribe in orchestrated campaigns (Limited Availability)** - Orchestrated campaigns now support personalization of list unsubscribe email parameters, using profile attributes or relational data. Header values can be set at the channel level and overridden per campaign using contextual data for more precise control. This capability is available in Limited Availability. Contact your Adobe representative to request access. <!-- Documentation link: TBD --> Jira: [DOCAC-15544](https://jira.corp.adobe.com/browse/DOCAC-15544){target="_blank"}

### Coworker {#oct-26-coworker}

The following improvements are coming to Coworker in this release.

* **Decisioning rule generation from Coworker** - The AI-assisted decisioning rule generation experience, previously available via the right rail, is now accessible through Coworker, which replaces the right rail as the way to build rules with AI. <!-- Documentation link: TBD --> Jira: [DOCAC-15290](https://jira.corp.adobe.com/browse/DOCAC-15290){target="_blank"}

* **Orchestrated campaigns skills in Coworker** - You can now interact with Orchestrated campaigns in natural language from the Coworker chat interface, for example to list your orchestrated campaigns and filter them by status (draft, live, completed, paused, stopped), date range, channel, and tags. <!-- Documentation link: TBD --> Jira: [DOCAC-14925](https://jira.corp.adobe.com/browse/DOCAC-14925){target="_blank"}

### Landing pages {#oct-26-landing-pages}

The following capability is coming to landing pages in this release.

<table>
<thead>
<tr>
<th><strong>New profile acquisition with landing pages</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows you to create landing pages accessible to anyone and from there capture data from completely unknown visitors in order to create or enrich new customer profiles in Experience Platform.</p>
<!-- GIF placeholder: TBD -->
<!-- Documentation link: TBD -->
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-13757" target="_blank">DOCAC-13757</a></p>
</td>
</tr>
</tbody>
</table>

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
<!-- GIF placeholder: TBD -->
<!-- Documentation link: TBD -->
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-15988" target="_blank">DOCAC-15988</a></p>
</td>
</tr>
</tbody>
</table>

* **Support Inbound action simulation in Journeys** - \<TBC\> <!-- Documentation link: TBD --> Jira: [DOCAC-15445](https://jira.corp.adobe.com/browse/DOCAC-15445){target="_blank"}

### Decisioning {#oct-26-decisioning}

The following improvement is coming to Decisioning in this release.

* **Use audience enrichment attributes in Decisioning rules (Limited Availability)** - You can now reference an audience's enrichment attributes as a data source in Decisioning eligibility rules. Enrichment attributes are additional, audience-specific data - such as the product or item IDs that qualified a profile for inclusion - defined through an Enrich activity in an audience composition. This lets your eligibility logic take into account exactly what triggered a customer's audience membership, without building and maintaining separate audiences for each product or item variation. Enrichment attributes were already available in journey conditions, custom actions, and message personalization; this release extends them to Decisioning. This capability is available in Limited Availability. Contact your Adobe representative to request access. <!-- Documentation link: TBD --> Jira: [DOCAC-15576](https://jira.corp.adobe.com/browse/DOCAC-15576){target="_blank"}

### Email Designer {#oct-26-email-designer}

The following improvement is coming to the Email Designer in this release.

* **Define fallback fonts for custom fonts used in email themes** - You can now define a fallback font for any custom (web) font applied through email themes. If a subscriber's email client does not support the custom font, Adobe Journey Optimizer automatically displays the specified fallback font instead of leaving the choice to the email client's default. This keeps email typography closer to your brand guidelines and reduces font-rendering inconsistencies across email clients. <!-- Documentation link: TBD --> Jira: [DOCAC-15662](https://jira.corp.adobe.com/browse/DOCAC-15662){target="_blank"}

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
<p>Jira: <a href="https://jira.corp.adobe.com/browse/DOCAC-16114" target="_blank">DOCAC-16114</a></p>
</td>
</tr>
</tbody>
</table>

* **Custom metadata for reporting and decisioning (Limited Availability)** - You can now attach custom key/value metadata to journeys, Action Campaign actions, and orchestrated campaign actions, in addition to the existing Adobe Experience Platform Unified Tags. This metadata is available for reporting, both in Journey Optimizer's built-in reports and in Customer Journey Analytics, so teams can measure and analyze action performance using their own custom dimensions. This capability is only available for a set of organizations (Limited Availability); contact your Adobe representative for more information. <!-- Documentation link: TBD --> Jira: [DOCAC-15667](https://jira.corp.adobe.com/browse/DOCAC-15667){target="_blank"}
