---
solution: Journey Optimizer
product: journey optimizer
title: Release notes
description: Journey Optimizer early Release notes
feature: Release Notes
topic: Content Management
role: User
level: Beginner, Intermediate
hide: yes
hidefromtoc: yes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
---
# Early release notes {#e-release-notes}

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated on the last week of each month in the [release notes](release-notes.md). 

Early release notes below are subject to change without prior notice until the release availability date. Links, screens and updated documentation are published in the [release notes](release-notes.md), at the release date.

## Febuary 2024 early release notes {#e-2024}

**Release date**: Feb 20-21, 2024

### New capabilities{#e-features}

This release brings the new capabilities listed below.


<table>
<thead>
<tr>
<th><strong>Web In-App Messaging</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now use the new Web In-App messaging capability to display personalized content directly on websites, through modal-overlay messages. This feature enables you to engage effectively with web visitors, enhancing user interaction, retention, and conversion rates.<br/><br/></p>
<!--img src="assets/do-not-localize/computed-attributes.gif"-->
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Business Rules (beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create Frequency Capping rules which apply to SMS and Direct Mail channels. In addition, you can set frequency capping rules by communication type.<br/><br/></p>
<!--img src="assets/do-not-localize/computed-attributes.gif"-->
</tr>
</tbody>
</table>



### Improvements {#e-improvements}

This release comes with the improvements listed below.

**Audiences**

* **Seed lists** - Variants are now supported when using **seed lists**. Like each profile from the targeted audience, the seed addresses receive a copy of all the variants of the same message (such as the different treatments of a content experiment).

Previously available as Beta, the following improvements are now available to all users:
 
* You can now target **audiences uploaded from a CSV file** into journeys and campaigns. [Learn more](../audience/about-audiences.md#segments-in-journey-optimizer)
* You can now target **audiences created through audience composition** and leverage enrichment attributes in Journeys. [Learn more](../building-journeys/read-audience.md)

**Journeys**

* **Filter your journeys** - You can now use **custom dates to filter the journeys** inventory, in addition to the existing predefined date filters. This allows you to refine the list by displaying journeys published on a specific date, within a particular month, throughout an entire year, or within specified time ranges.
* **Custom actions** - You can now update on the "content-type" header in **custom actions**.
* **Configuration** - The identityMap attribute in stepEvents is now pre-filled. The primary identity is defined as "primary = true".
* **User interface** - The top bar, in journey screens, has been reorganised for an improved experience. Among the different updates, notice that the "pencil" icon that allows you to access the journey properties is now displayed on the left of the top bar, next to the journey's name.

**SMS channel**

* **Opt-in/opt-out keywords** - When configuring your SMS channel, you can now customize the **Opt-in and Opt-out keywords** as per your preferences. Journey Optimizer triggers the response based on these specified keywords.    

**Campaigns**

* **API-triggered campaigns** - Information has been added in the **cURL request** section of **API-triggered campaigns** that are in **Draft** state, to specify that the sample cURL request is visible only once the campaign has been published and executed.    

**Decision management**

* **Capping rules** - You can now add **multiple capping rules** for one offer. This allows you to increase the level of control over the way offers are sent.

**Content templates**

* **Thumbnail** - A **thumbnail view** is now available for content templates and fragments for improved visual access.    
* **Multi-channel templates** - Content templates are now available for **all channels**, except Web.