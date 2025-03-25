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


## March '25 early release notes {#25-3-rn}


**Early release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published at the release date.

**Release date**: March 26-27, 2025


### New capabilities {#25-03-features}

New capabilities coming with this release are detailed below.


<table>
<thead>
<tr>
<th><strong>Integration with Adobe Express</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Adobe Express integration in Adobe Journey Optimizer lets you use Adobe Express's editing tools directly during content creation, enabling you to resize, remove backgrounds, crop, and convert assets to JPEG or PNG.<p>
<!--p>For more information, refer to the <a href="../configuration/rule-sets.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey metrics</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey metrics will allow you to measure the impact of your activities across the metrics most important to your business and to provide clearer insights into your performance.</p>
<!--p>For more information, refer to the <a href="../configuration/rule-sets.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Calendar view for journeys (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A calendar view is now allows you to visualize all journeys activations. This capability is released as a Limited Availability to a select group of customers.<p>
<p>This change is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<!--p>For more information, refer to the <a href="../configuration/rule-sets.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Integration with Dynamic Media (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Dynamic media assets are now directly available and accessible in Journey Optimizer. This integration enables you to:
<ul>
<li>Centrally manage assets with real-time updates</li>
<li>Modify your assets settings such as width and height instantly</li>
<li>Personalize your content using images with text overlays</li>
<li>Customize Dynamic Media templates by updating your content and adding personalization fields</li>
</ul>
<p>
<p>This integration is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<!--p>For more information, refer to the <a href="../configuration/rule-sets.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>



<table>
<thead>
<tr>
<th><strong>Integration with Adobe GenStudio (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>To enhance marketing efficiency and to maintain brand consistency, you can now seamlessly integrate GenStudio for Performance Marketing experiences with Journey Optimizer. This enable you to leverage GenStudio's AI-power content creation alongside Journey Optimizer's advanced orchestration capabilities.<p>
<p>The use of the GenStudio integration in Journey Optimizer is currently unavailable for use with the Healthcare Shield or Privacy and Security Shield (Limited Availability).</p>
<!--p>For more information, refer to the <a href="../configuration/rule-sets.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>LINE channel (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer has expanded its cross-channel capabilities to include support for the LINE channel. This enhancement allows you to create, edit, and preview LINE experiences enabling more personalized and engaging interactions. With LINE, you can connect with more customers, send relevant content, and improve your engagement.<p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<!--p>For more information, refer to the <a href="../configuration/rule-sets.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

### Improvements {#25-03-improv}

**Personalization editor** (availability date: March 12)

The Journey Optimizer personalization editor has been updated with new capabilities:

* **Updated Code Editor Design** – A cleaner, modern interface for improved usability and focus.
* **Search and Replace** – Added functionality to quickly find and replace content within the editor.
* **Undo and Redo Support** – Allows you to easily revert or reapply changes.
* **Customizable Font Size** – Enables adjustment of the editor's font size for better readability.
* **Inline JSON Validation** – Provides real-time client-side validation for JSON content to speed up error detection.
* **Auto-Complete for Profile and Context Attributes** – Offers smart suggestions to streamline content creation.
* **Enhanced Syntax Highlighting** – Improves readability by making code structure more visually distinct.

![Video showing new feature in the Personalization Editor](assets/do-not-localize/personalization-editor.gif)

For more information, refer to the [detailed documentation](../personalization/personalization-build-expressions.md).


**Campaigns**

* In the campaign list, selecting a campaign now opens a pane displaying its details.
* You can now copy your campaigns from a sandbox to another.

**Personalization**

A new "Pills" button has been to the personalization editor. When enabled, profile and contextual attributes display as pills, enhancing the readability of your code.

**Approvals**

When defining the conditions for an approval policy, you now have the option to filter by Tag and/or Object Category.

**Channel configuration**

You can now assign Adobe Experience Platform Unified Tags to channel configurations. This allows you to easily classify them, and improve search and navigation in all lists.

**Deliverability**

You can now delegate subdomains with DMARC being managed from the parent side.    

**Business rules**

You can now use daily frequency capping in journeys and campaigns with batch segmentation. To ensure accuracy for daily frequency capping rules, make sure you choose the highest priority namespace while authoring a campaign or journey. Learn more on namespace priority in the [Platform Identity Service guide](https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/identity-graph-linking-rules/namespace-priority){target="_blank"}

**Content management**

To easily manage your fragments and your content templates, you can now use folders to organize them more effectively into a structured hierarchy.
