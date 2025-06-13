---
solution: Journey Optimizer
product: journey optimizer
title: Early release notes
description: Journey Optimizer early Release notes
feature: Release Notes
hide: yes
hidefromtoc: yes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
---
# Early release notes {#e-release-notes}

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md). 

**Early release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the [release notes](release-notes.md), at the release date.


## June '25 early release notes {#25-6-rn}


**Early release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published at the release date.

**Release date**: June 18, 2025


### New capabilities {#25-06-features}

New capabilities coming with this release are detailed below.




<table>
<thead>
<tr>
<th><strong>RCS Messaging</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Rich Communication Services (RCS) messaging is now supported in the Journey Optimizer, enabling the following enhanced messaging capabilities subject to provider and carrier support:</p>
<ul>
<li>Branded and verified sender support: Send messages using verified business profiles with branding elements (logo, sender name, etc.).</li>
<li>Message delivery insights: Receive detailed delivery reports including message status updates (e.g., sent, delivered, read).</li>
<li>Link tracking: Embed and track URLs within RCS messages for engagement analytics.</li>
<li>Fallback to SMS: Automatic fallback to SMS when the profile's device does not support RCS or is temporarily unreachable via RCS.</li>
<li>Basic message composition: Send text-based RCS messages with optional media and rich elements, depending on provider support.</li>
</ul>
<!--p>For more information, refer to the <a href="../sms/sms-configuration.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

<!--table>
<thead>
<tr>
<th><strong>True Multi-Tenant Unitary Delivery</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>No description provided.</p>
</td>
</tr>
</tbody>
</table-->

<table>
<thead>
<tr>
<th><strong>Form fields in code-based experience content</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now define specific editable fields in JSON or HTML content templates which enable non-technical users to easily edit content in a form-view within the code-based experience channel authoring, without the need to manipulate any code. More than that, when defining the code-based experience content templates you can now insert decision policies in the template, increasing reusability and ease of use.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Custom delegation method for subdomains</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>In addition to the full delegation and the CNAME method, a new subdomain configuration method is now available: the Custom delegation method, which enables you to fully own controlling and maintaining all aspects of DNS that are required for delivering, rendering and tracking messages.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Content Decisioning activity in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now include personalized offers in your journeys through a dedicated Content Decisioning activity in the journey canvas, and use them in journey activities, including conditions and custom actions.</p>
<p>This capability is only available for a set of organizations (Limited Availability), and will be rolled out globally in a future release.</p>
</td>
</tr>
</tbody>
</table>


<!--table>
<thead>
<tr>
<th><strong>Experience Decisioning in email channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>No description provided.</p>
</td>
</tr>
</tbody>
</table-->



<table>
<thead>
<tr>
<th><strong>Journey Dry run</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Dry run is a special journey publication mode in Adobe Journey Optimizer that allows journey practitioners to test a journey using real production data without contacting real customers or updating profile information. This feature helps journey practitioners gain confidence in their journey design and audience targeting before publishing it live.</p>
<p>This capability is only available for a set of organizations (Limited Availability), and will be rolled out globally in a future release.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Pause and resume journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now pause and resume your journeys. This capability gives journey practitioners greater control and flexibility by allowing live journeys to be temporarily suspended without disrupting customer experience. When paused, no communications are sent, and profiles remain in a suspended state until the journey is resumed.</p>
<p>You can pause and resume one journey only, or perform bulk pause and resume operations to a group of journeys.</p>
<p>In addition, you can apply global filters to paused journeys to exclude profiles based on their attributes.</p>
<p>This capability is only available for a set of organizations (Limited Availability), and will be rolled out globally in a future release.</p>
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
<p>Scale your Experimentation winner enables you to automatically or manually roll out the winning variation of an experiment to your full audience. This feature ensures that, once a top performer is identified, you can maximize its reach and effectiveness without constant manual oversight.</p>
<p>For more information, refer to the <a href="../content-management/content-experiment.md">detailed documentation</a>.</p>
<p>Availability date: June 2nd, 2025</p></td>
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
<li>Enhanced Reporting: Reports now indicate which specific rule excluded a profile from a journey or campaign, providing greater transparency and actionable insights.</li></ul>
<img src="assets/do-not-localize/gif-conflict.gif">
<p>For more information, refer to the <a href="../conflict-prioritization/gs-conflict-prioritization.md">detailed documentation</a>.</p>
<p>Availability date: June 3rd, 2025</p>
</td>
</tr>
</tbody>
</table>


### Improvements {#25-06-improv}

Improvements coming with this release are listed below.

* **Channel rule sets**

  * **Custom duration window** for capping -  A new **Repeat Count** field is now available in the channel rule sets configuration screen, allowing you to apply frequency capping rules over multiple days, weeks, or months, depending on the specified duration.

  * **Hourly duration** - You can now apply capping on an hourly basis for channel rule sets.    

* **Code-based experiences**

  Decision policies are now available in code-based experience content templates and on the code editor right rail.

* **Email Designer**

  * **Custom CSS support** -  Journey Optimizer now allows you to add custom CSS to your email content directly within the Email designer.
  * **Dark mode support**  - The Journey Optimizer Email designer now offers the ability to switch to dark mode where you can define specific settings. 


* **Decisioning** - Availability date: June 3rd, 2025

  Decisioning objects can now be copied between sandboxes, streamlining testing and deployment workflows. [Read more](../configuration/copy-objects-to-sandbox.md#decisioning)

* **Decision item attribute support for decisioning rules** - Availability date: June 4th, 2025
  
  You can now leverage decision item attributes to create decisioning rules. [Read more](../experience-decisioning/rules.md#create)

* **Interactive Message Execution API update** - Availability date: June 6th, 2025 

  The Interactive Message Execution API now allows you to delete the schedule of upcoming campaigns execution. [Read more](https://developer.adobe.com/journey-optimizer-apis/references/messaging/){target="_blank"}