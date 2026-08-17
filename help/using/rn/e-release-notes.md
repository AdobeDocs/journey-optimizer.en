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

## August '26 pre-release notes {#august-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production. While most changes are delivered on the release date, a few may roll out later.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: August 18-19, 2026

<!--
### Onboarding {#august-26-onboarding}

The following capability is coming to onboarding in this release.

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
<GIF placeholder: to be added>
<Documentation link: TBD>
</td>
</tr>
</tbody>
</table>

-->

### Journeys {#august-26-journeys}

The following capabilities and improvements are coming to journeys in this release.

<table>
<thead>
<tr>
<th><strong>Journey-level holdout (Limited availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now configure a holdout group for your journeys directly from journey properties. A holdout is a configurable percentage of your target audience that is excluded from entering the journey and receives no communication. By comparing holdout profiles against active profiles in Customer Journey Analytics reporting, you can measure the incremental lift - the true impact - that your journey delivers.</p>
<p> This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Add new dateDiff function in journey expression editor** - The journey expression editor now includes the `dateDiff` function, which calculates the difference between two dates in number of days. This function is useful for time-based logic such as creating deadlines, calculating customer lifecycle durations, or building countdown timers in journey conditions. <!-- Documentation link: TBD -->

* **Start and end dates in the journey header** - When start and/or end dates are configured on a journey, they are now surfaced in the journey header next to the status badge. The displayed label adapts based on whether each date is upcoming or has already passed. <!-- Documentation link: TBD -->

### Campaigns {#august-26-camp}

The following capabilities and improvements are coming to Campaigns in this release.

<table>
<thead>
<tr>
<th><strong>Inbound experience simulation in Action Campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now simulate inbound channel actions in Action Campaigns before going live. Use simulation mode to test your configuration with simulated users and preview the rendered experience, including a generated URL and QR code, so you can validate rules, decisioning, and content rendering end-to-end.</p>
<p>This capability is currently in private beta and available to a limited set of organizations. Contact your Adobe representative for more information.</p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Action Campaign authoring flow redesign** - Adobe Journey Optimizer Action Campaign authoring flow has been redesigned to deliver a significantly more intuitive, efficient, and seamless user experience.

* **Folders for Action Campaigns** - You can now organize your Action Campaigns into folders to improve navigation and management in the interface. <!-- Documentation link: TBD -->

<!--* **Brand alignment score in Action Campaign dashboard** - You can now assess your brand alignment score directly within your Action Campaign dashboard to ensure content stays on-brand. This allows you to verify guidelines at a glance without having to open the content designer.  Documentation link: TBD -->

* **Override the default execution fields in Action Campaigns** - Previously available at the journey level, you can now override the default execution fields configured globally for your Email, SMS, and WhatsApp deliveries in the Action Campaign parameters. <!-- Documentation link: TBD -->

### Orchestrated Campaigns {#august-26-oc}

The following capabilities and improvements are coming to Orchestrated Campaigns in this release.

<table>
<thead>
<tr>
<th><strong>Quiet Hours support</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now apply Quiet Hours. Quiet Hours let you define time-based exclusions to prevent messages from being sent during specific periods, helping you respect customer preferences and compliance requirements across campaign orchestration use cases.</p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>LINE channel support (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With release of Custom outbound channels feature, you can now add LINE actions directly into your campaigns. This new activity allows you to build and deliver highly personalized content, including text, stickers, images, videos, location data, and rich Flex Messages, to engage your customers seamlessly on the LINE platform. This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Ability to Manage Profile Target Dimensions** - You can now delete a Profile Target Dimension or edit and swap its configured identity namespace, providing greater control and flexibility over your data setups. <!-- Documentation link: TBD -->

<!-- * **New public APIs** - New API specifications are now available. These APIs allow you to programmatically create, manage, and trigger orchestrated campaigns, enabling deeper integration with external systems and automation pipelines. Documentation link: TBD -->

* **Personalize email sender details per recipient and campaign (Limited availability)** - Orchestrated campaigns now support personalization of email header fields, including From name, From email prefix, Reply-to name, and Reply-to email, as well as the execution address, using profile attributes or relational data. This allows sender details to reflect the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address. Header values can be set at the channel level and overridden per campaign using contextual data for more precise control.
  This capability is only available for a set of organizations (Limited Availability). 
  <!-- Documentation link: TBD -->

* **Target dimension simplification** - The active targeting dimension is now shown on the workflow canvas, so you can see which dimension is used by a channel activity. The multi-entity segmentation flow is simpler as you no longer need a separate "Change dimension" activity. Moreover, you can now choose explicitly whether messages are sent at the profile level or at a secondary dimension level. <!-- Documentation link: TBD -->

* **Send using waves** - You can now schedule outbound messages to be delivered in controlled batches over time. Ideal for high-volume or time-sensitive campaigns, wave sending also supports better deliverability and helps maintain a strong sender reputation by reducing the risk of being flagged as spam. <!-- Documentation link: TBD -->


### Decisioning {#august-26-decisioning}

The following capabilities and improvements are coming to Decisioning in this release.

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
<!-- GIF placeholder: to be added -->
<!-- Documentation link: TBD -->
</td>
</tr>
</tbody>
</table>

* **Placement-level frequency capping in Decisioning** - Frequency capping rules in Decisioning can now be scoped to individual placements, giving you finer control over how often an offer is shown in a given surface. Two modes are available: placement-specific capping, which defines a cap that applies only when the offer is displayed in a selected placement, and per-placement capping, which applies a cap independently across every placement where the offer appears, so each placement maintains its own capping counter. Note that placement-related capping does not apply to offers capped using rules based on Adobe Experience Platform data. <!-- Documentation link: TBD -->  

* **Mirror pages in Visual Fragments** - You can now insert mirror pages into a Visual Fragment. Decisioning attributes render correctly on the mirror page link, even when the fragment is used in an email campaign that leverages Decisioning. The mirror page must be added to the Visual Fragment before the fragment is published in order for decisioning attributes to display. <!-- Documentation link: TBD -->

### Administration {#august-26-administration}

The following improvement is coming to administration in this release.

* **Feedback Loop OTP process for custom subdomains** - The Feedback Loop (FBL) custom subdomain configuration process has been improved by surfacing the Yahoo sender hub One-Time Password (OTP) directly within the product UI. Users can now automatically retrieve and display the OTP generated during the Yahoo sender hub domain ownership verification. <!-- Documentation link: TBD -->

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


