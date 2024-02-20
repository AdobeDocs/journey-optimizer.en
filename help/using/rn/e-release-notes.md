---
solution: Journey Optimizer
product: journey optimizer
title: Release notes
description: Journey Optimizer early Release notes
feature: Release Notes
topic: Content Management
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
---
# Early release notes {#e-release-notes}

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated on the last week of each month in the [release notes](release-notes.md). 

Early release notes below are subject to change without prior notice until the release availability date. Links, screens and updated documentation are published in the [release notes](release-notes.md), at the release date.

## February 2024 early release notes {#e-2024}

**Release date**: Feb 21-22, 2024

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
<img src="assets/do-not-localize/web_inapp.gif">
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Frequency Rules for SMS and Direct Mail</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create Frequency rules for SMS and Direct Mail channels. Frequency rules automatically exclude over-solicited profiles from messages and actions when the frequency cap is reached. <br/><br/></p>
<img src="assets/do-not-localize/sms-dm-rules.gif">
</tr>
</tbody>
</table>

### Improvements {#e-improvements}

This release comes with the improvements listed below.

**Audiences**

* **Seed lists** - Variants are now supported when using **seed lists**. Like each profile from the targeted audience, the seed addresses receive a copy of all the variants of the same message (such as the different treatments of a content experiment).

Previously available as Beta, the following improvements are now available to all users:

* You can now target **audiences created through audience composition** and leverage enrichment attributes in Journeys. [Learn more](../building-journeys/read-audience.md)

* You can now target **audiences uploaded from a CSV file** into journeys and campaigns. [Learn more](../audience/about-audiences.md#segments-in-journey-optimizer)

   >[!AVAILABILITY]
   >
   >* The use of audiences and attributes from audience composition and custom upload (CSV file) is currently unavailable for use with Healthcare Shield or Privacy and Security Shield.
   >* Please note that the audience upload from a CSV file improvement will be rolled out gradually over the course of several days following the initial release. While some users will have immediate access, others may experience a delay before it becomes available in their accounts.

**Journeys**

* **Filter your journeys** - You can now use **custom dates to filter the journeys** inventory, in addition to the existing predefined date filters. This allows you to refine the list by displaying journeys published on a specific date, within a particular month, throughout an entire year, or within specified time ranges.
* **Custom actions** - You can now update on the "content-type" header in **custom actions**.
* **Configuration** - The identityMap attribute in stepEvents is now pre-filled. The primary identity is defined as "primary = true".
* **User interface** - The top bar, in journey screens, has been reorganised for an improved experience. Among the different updates, notice that the "pencil" icon that allows you to access the journey properties is now displayed on the left of the top bar, next to the journey's name.

**SMS channel**

* **Opt-in/opt-out keywords** - When configuring your SMS channel, you can now customize the **Opt-in and Opt-out keywords** as per your preferences. Journey Optimizer triggers the response based on these specified keywords.    

**Campaigns**

* **API-triggered campaigns** - The cURL code generated after activating an API-triggered campaign has been enhanced. It now includes all personalizaton (profile and context) variables used in the message. 

**Decision management**

* **Capping rules** - You can now add **multiple capping rules** for one offer. This allows you to increase the level of control over the way offers are sent.

**Content templates**

* **Thumbnail** - A **thumbnail view** is now available for content templates and fragments for improved visual access.

   >[!AVAILABILITY]
   >
   >This capability is progressively rolled out to customers environments starting this release.

* **Multi-channel templates** - Content templates are now available for **all channels**, except Web. For Email, you can now select the type (HTML or Content).
