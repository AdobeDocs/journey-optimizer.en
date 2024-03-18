---
solution: Journey Optimizer
product: journey optimizer
title: Release notes
description: Journey Optimizer early Release notes
feature: Release Notes
topic: Content Management
hide: yes
hidefromtoc: yes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
---
# Early release notes {#e-release-notes}

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md). 

Early release notes below are subject to change without prior notice until the release availability date. Links, screens and updated documentation are published in the [release notes](release-notes.md), at the release date.

## March 2024 early release notes {#e-2024}

**Release date**: March 19-20, 2024

### New capability {#e-features}

This release brings the new capability detailed below.

<table>
<thead>
<tr>
<th><strong>Code-based experiences</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With the new Code-based experience channel, Adobe Journey Optimizer allows you to do advanced personalization and testing for any of your inbound properties, enabling seamless delivery of tailored experiences across diverse touchpoints such as web apps, mobile apps, desktop apps, video consoles, TV connected devices, smart TVs, kiosks, ATMs, IoT devices, and more.</p>
<P>Key capabilities include:</p>
<ul><li> Universal personalization: extend personalized experiences across all touchpoints, ensuring a cohesive and tailored user journey</li>
<li>Granular editing precision: edit specific content at individual locations within your apps or web pages</li>
<li>Versatile implementation: support for server-side, API-based, or SDK-based implementation methods to seamlessly integrate with your development environment.</li></ul></p>
<p>For more information, refer to the <a href="../code-based/get-started-code-based.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/code-based.gif">
</tr>
</tbody>
</table>

### Improvements {#e-improvements}

This release comes with the improvements listed below.

**Content templates**

* **Thumbnails** - A **Grid view** mode is now available for content templates, displaying thumbnails for improved visual access. Currently only email HTML templates are supported. [Learn more](../content-management/content-templates.md#template-thumbnails)

   >[!AVAILABILITY]
   >
   >This capability is released in Limited Availability (LA) for a small set of customers.

**Journeys**

New intermediate statuses have been added to the journey authoring lifecycle:

* **Publishing** status between the **Draft** status and the **Live** status
* **Stopping** status between the **Live** status and the **Stopped** status
* **Activating test mode** or **Deactivating test mode** statuses between the **Draft** status and the **Draft (test)** status

When a journey is in an intermediate state, it is read-only.