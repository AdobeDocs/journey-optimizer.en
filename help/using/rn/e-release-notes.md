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
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
subfeature_v2:
  - id: a7b2bfc5-be71-4740-b371-76fa6be8df02
    internal-label: Journey Optimizer release notes
---

# Pre-release notes {#e-release-notes}

Adobe Journey Optimizer continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md).

## September '26 pre-release notes {#sep-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published once changes are live in production. While most changes are delivered on the release date, a few may roll out later — refer to the Availability Date listed for each entry for details.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: September 22-23, 2026


<!--
### Onboarding {#sep-26-onboarding}

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
<p>Transitioning to Adobe Journey Optimizer from another marketing platform is easier with guided capabilities that help you move existing email content and journeys into Journey Optimizer. A <strong>dedicated workspace</strong> lets you reuse what you have instead of rebuilding from scratch.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
</td>
</tr>
</tbody>
</table>

-->

### Journeys {#sep-26-journeys}

The following capabilities and improvements are coming to journeys in this release.

* **Reduced step events for wait and event activities** - Step events are no longer generated for **wait** activities and **event** activities when the profile was not actually processed at that activity. <!-- DRAFT: pending DOCAC sub-task under DOCAC-15691, see CJM-165835 -->
<!-- Documentation link: TBD -->

### Channels {#sep-26-channels}

The following capabilities and improvements are coming to channels in this release.

<table>
<thead>
<tr>
<th><strong>Custom outbound channel (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Custom outbound channels</strong> let administrators bring any outbound HTTP-based messaging channel — such as WeChat, Kakao Talk, Messenger, or a proprietary provider — directly into Journey Optimizer through a no-code Channel Builder. Once configured, custom channels are available across campaigns, journeys, and orchestrated campaigns, with the same full set of capabilities as native channels: personalization with the expression editor, content experimentation, preview and proof, out-of-the-box reporting, and consent and governance enforcement.</p>
<p>With this release, custom outbound channels also gain several new capabilities:</p>
<ul>
<li>Use Journey Optimizer Decisioning in the custom channel payload through the Personalization Editor, the same way as in code-based experiences.</li>
<li>Apply business rules to custom channels, the same way you already can on native channels.</li>
<li>Select custom channels in the channel list for API-triggered campaigns, which was not previously possible.</li>
<li>Define a reporting webhook for a custom channel and attach it to a channel configuration, so you can enrich your Journey Optimizer reports with interaction events.</li>
</ul>
</td>
</tr>
</tbody>
</table>

### Email channel {#sep-26-email-channel}

The following capabilities and improvements are coming to the Email channel in this release.

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
<p>This lets you personalize the email header fields (<strong>From name</strong>, <strong>From email prefix</strong>, <strong>Reply to name</strong>, and <strong>Reply to email</strong>), the execution address, and the list-unsubscribe values, using profile attributes or contextual data for more precise control. In particular, this allows sender details to reflect the relevant advisor, location, or branch for each recipient, rather than routing all sends through a single corporate address.</p>
</td>
</tr>
</tbody>
</table>

* **Suppression list override at email action level** - Journey Optimizer now lets you override suppression list behavior directly at the email action level in journeys and campaigns. This gives teams more flexibility for operational or compliance-critical communications that require a dedicated sending configuration, while preserving existing global suppression list controls for all other sends. This enhancement helps organizations handle exception scenarios with precision without changing their broader suppression governance model.

* **URL syntax validation in email authoring** - Journey Optimizer now validates URLs earlier in the email authoring flow and surfaces clearer guidance when malformed syntax is detected. This helps authors catch issues before finalization, reduce publishing errors, and improve delivery confidence.

### Email Designer {#sep-26-email-designer}

The following capabilities and improvements are coming to the Email Designer in this release.

<table>
<thead>
<tr>
<th><strong>Dark mode support for email theme variants</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Email themes now support dark mode, so each color variant can render with a look tailored to recipients viewing your email in a dark mode-enabled client.</p>
<p>When enabled, a default dark palette is generated automatically for every variant, and you can further customize it with a different palette or your own custom colors — independently from the light mode design, so changes made in one mode do not affect the other.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Import Dynamic Media templates directly from PSD files in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Email Designer's Dynamic Media component now lets you import a Photoshop (PSD) file directly as a new template, in addition to browsing existing Dynamic Media templates. Drag and drop a PSD file into the component, and Adobe Journey Optimizer automatically converts it into a Dynamic Media template stored in Dynamic Media — no manual conversion or round-trip through Adobe Experience Manager needed. Once imported, you edit the template using the built-in Dynamic Media editor, the same experience used for Adobe Express content in the Email Designer.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>New table component in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Email Designer now includes a built-in <strong>Table component</strong>, allowing you to structure content in rows and columns directly within your email. Drag and drop the component onto your canvas, customize the number of rows and columns, and style each cell independently to create clear, organized layouts without relying on custom HTML.</p>
</td>
</tr>
</tbody>
</table>

* **Fallback fonts for custom fonts in email themes** - You can now define a fallback font for any custom (web) font applied through email themes. If a subscriber's email client does not support the custom font, Adobe Journey Optimizer automatically displays the specified fallback font instead of leaving the choice to the email client's default. This keeps email typography closer to your brand guidelines and reduces font-rendering inconsistencies across email clients.
