---
solution: Journey Optimizer
product: journey optimizer
title: Early release notes
description: Journey Optimizer early Release notes
feature: Release Notes
topic: Content Management
hide: yes
hidefromtoc: yes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
---
# Early release notes {#e-release-notes}

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md). 

**Early release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the [release notes](release-notes.md), at the release date.


## May '25 early release notes {#25-5-rn}


**Early release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published at the release date.

**Release date**: May 20-21, 2025


### New capabilities {#25-04-features}

New capabilities coming with this release are detailed below.

<table>
<thead>
<tr>
<th><strong>Synchronize read audience schedule with batch segmentation job</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now trigger daily journey runs after batch segmentation completion. This option is now available in daily-scheduled journeys to all customers. It allows you to define for a time window of up to 6 hours to wait for audience data from batch segmentation jobs, ensuring journeys run with the most up-to-date data or are skipped if not ready.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Decisioning - New AI formula builder</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create specific Decisioning ranking formulas by defining and combining criteria from a new improved interface. Instead of relying only on a static offer priority, you can define custom ranking formulas that combine AI model scores, offer priorities, profile attributes, offer attributes, and contextual signals through a guided interface.</p>
<img src="assets/do-not-localize/formula-builder.gif">
<p>For more information, refer to the <a href="../experience-decisioning/exd-ranking-formulas.md">detailed documentation</a>.</p>
<p>Availability date: May 14, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Adobe Experience Manager Content fragment integration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With the integration of Adobe Experience Manager and Adobe Journey Optimizer, you can now effortlessly use Adobe Experience Manager Content Fragments within your Journey Optimizer content. This seamless connection makes it easier to access and use your AEM content directly in Journey Optimizer.</p>
<p>Previously available for a limited set of organizations (LA), this capability is now GA with the following enhancements:</p>
<ul>
<li>Create offers by directly selecting an AEM Content Fragment.</li>
<li>Define placeholders and map personalization values within the fragment signature using the Editor mode.</li>
</ul>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Calendar View for Campaign and Journey inventory</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A calendar view is now available in the journeys and campaigns lists. It allows you to visualize all journeys and campaigns activations in the respective lists.</p>
<p>This change is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Adobe Experience Manager Dynamic media integration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Dynamic media assets are now directly available and accessible in Journey Optimizer. This integration enables you to:</p>
<ul>
<li>Centrally manage assets with real-time updates.</li>
<li>Modify your assets settings such as width and height instantly.</li>
<li>Customize Dynamic Media templates by updating your content and adding personalization fields.</li>
</ul>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Themes in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now quickly apply pre-approved themes to ensure brand consistency across all emails, speed up your campaign creation process, and independently produce high-quality emails while reducing dependency on design teams.</p>
<img src="assets/do-not-localize/themes.gif">
<p>This capability is currently in beta version and only available to beta customers. To join the beta program, contact your Adobe representative.</p>
<p>Availability date: May 14, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Conflict & prioritization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>In Journey Optimizer, managing the volume and timing of campaigns and journeys is essential to avoid overwhelming customers with too many interactions. Journey Optimizer now offers several tools for conflict management and prioritization - previously available only to limited-access (LA) organizations - that are now generally available (GA).</p>
<p>Previously released in Limited Availability, this capability is now available to all environments. With this General Availability release, the following enhancements have been introduced:</p>
<ul>
<li>Expanded Support: Conflict management tools now support both Unitary Journeys and Audience Qualification Journeys, in addition to Read audience journeys.</li>
<li>Improved Troubleshooting: Two new step event fields are now available in the Query Service, enabling you to analyze why a profile was rejected from a journey or campaign.</li>
<li>Enhanced Reporting: Reports now indicate which specific rule excluded a profile from a journey or campaign, providing greater transparency and actionable insights.</li>
</ul>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Simulate content variations</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Previously available in beta, content variations simulation is now generally available (GA). It allows you to preview different variations of your content using sample input data uploaded from a CSV or JSON file or added manually. All the attributes used in your content for personalization are automatically detected by the system and can be used for your tests to create multiple variants.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments. With this General Availability release, the feature now includes support for multilingual content and content experiments, enabling you to test variations across different languages and treatments. Additionally, it now supports contextual attributes (in addition to profile attributes), allowing for even more dynamic and situational content testing.</p>
<img src="assets/do-not-localize/variants.gif">
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Scale your Experimentation winner</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Scale the Winner enables you to automatically or manually roll out the winning variation of an experiment to your full audience. This feature ensures that, once a top performer is identified, you can maximize its reach and effectiveness without constant manual oversight.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Custom SMS provider</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows you to configure additional SMS providers beyond the default options: Sinch, Infobip, and Twilio. With custom SMS provider configuration, you can integrate third-party providers directly, leverage advanced payload customization for dynamic messaging, and manage consent preferences (opt-in/opt-out) to ensure compliance.</p>
<p>For more information, refer to the <a href="../sms/sms-configuration-custom.md">detailed documentation</a>.</p></td>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Content decisions in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add offers to your journeys through a dedicated decisioning action in the journey canvas, and use them in your custom actions.</p>
</td>
</tr>
</tbody>
</table>


### Improvements {#25-05-improv}

Improvements coming with this release are listed below.

* **Pills activation for personalization** - Availability date: May 5, 2025

  A new "Pills" button has been added to the personalization editor. When enabled, profile and contextual attributes display as pills, enhancing the readability of your code. [Read more](../personalization/personalization-build-expressions.md#options)

  >[!AVAILABILITY]
  >
  >This capabilitity will be gradually rolled out to all environments over the next 30 days.

* **Folders for landing pages**  - Availability date: May 9, 2025
  To easily manage your landing pages, you can now use folders to organize them more effectively into a structured hierarchy. [Read more](../landing-pages/manage-lp.md)

* **Click tracking in email templates**  
  Click tracking on `<area>` elements within image maps in email templates is now natively supported in Journey Optimizer. This is to ensure that image map areas receive the same tracking wrapping, tracking data, and appended parameters as standard hyperlinks.

* **Decisioning - Leverage Adobe Experience Platform datasets**  
  Journey Optimizer now allows you to leverage Adobe Experience Platform datasets in the following Decisioning objects: eligibility rules, ranking formulas, and capping rules.

* **Folders in templates and fragments (General Availability)**  
  Previously available for a set of organizations (LA), folders are now available to all users (GA) to manage their content templates and fragments. Folders let you organize your content templates and fragments more easily and effectively into a structured hierarchy.

* **New campaign objects support for sandbox copy** <!-- - Availability date: -->

  When copying campaigns across multiple sandboxes using the package export and import capabilities, the following dependencies are now also copied: channel configurations, experiment variants and settings, decision policies and items. [Read more](../configuration/copy-objects-to-sandbox.md)

* **'Redirect to URL' support in Web channel**  
  The Journey Optimizer Web channel now enables you to redirect visitors to another existing URL rather than authoring a new variation in the visual editor. This capability can be used to run experiments comparing two completely different pages instead of just changing a few elements within a page.

* **Sandbox tooling - New Campaigns objects support**  
  When copying campaigns across multiple sandboxes using the package export and import capabilities, the following dependencies are now also copied: channel configurations, experiment variants and settings, decision policies, and items.

* **Right rail in campaigns list**  
  In the campaign list, selecting a campaign now opens a pane displaying its details.

* **Form fields in code-based experience content**  
  In content templates, you can now define specific JSON or HTML fields which enable non-technical users to easily edit content in code-based experiences without the need to manipulate code.

* **Decision item attribute support for decisioning rules**  
  You can now leverage decision item attributes to create decisioning rules.

* **Multiple Journey Re-Entrance**  
  You can now trigger journeys using a profile ID along with another identifier, such as an order ID, subscription ID, or prescription ID, allowing the same profile to be in the same journey multiple times at once. This enables scenarios like managing multiple orders or subscriptions in parallel, with each instance following its own path through the journey.

* **Subdomains - 'No delegation' method**  
  In addition to the full delegation and the CNAME method, a new subdomain configuration method is now available: the No delegation method, which enables you to fully own controlling and maintaining all aspects of DNS that are required for delivering, rendering, and tracking messages.

* **Support for Custom Data sources in Personalization**  
  You can now build a query and grab data from an external source (i.e., not stored in Adobe Experience Platform) to use in Journey Optimizer inbound and outbound surfaces for personalization and journey orchestration.