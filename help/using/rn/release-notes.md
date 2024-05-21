---
solution: Journey Optimizer
product: journey optimizer
title: Release notes
feature: Release Notes
topic: Content Management
description: Journey Optimizer Release notes
exl-id: 06fa956a-b500-416e-9d42-b683c328e837
---
# Release notes {#release-notes}

>[!CONTEXTUALHELP]
>id="ajo_homepage_card1"
>title="What's new?"
>abstract="**Adobe Journey Optimizer** continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated on the last week of each month in these release notes."

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated on the last week of each month in these release notes. 

[!DNL Adobe Journey Optimizer] is built natively on [!DNL Adobe Experience Platform] and inherits from its latest innovations and improvements. Learn more about these changes in [Adobe Experience Platform Release Notes](https://experienceleague.adobe.com/docs/experience-platform/release-notes/latest.html){target="_blank"}.

![Newsletter](../assets/do-not-localize/nl-icon.png) Sign up for the [Adobe Journey Optimizer quarterly newsletter](https://www.adobe.com/subscription/Adobe_Journey_Optimizer_NL.html){target="_blank"} today, and receive the latest product updates, exciting stories, use cases, tips and more delivered directly to your inbox every quarter.


## May 2024 release notes {#may-2024}

**Release date**: May 21-22, 2024

### New capabilities {#e-features}

This release brings the new capabilities detailed below.


<table>
<thead>
<tr>
<th><strong>Experience Decisioning - Limited Availability</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Experience Decisioning simplifies personalization by offering a centralized catalog of marketing offers known as 'decision items' and a sophisticated decision engine. This engine leverages rules and ranking criteria to select and present the most relevant decision items to each individual.</p>
<p>These decision items are seamlessly integrated into a wide range of inbound surfaces through the new code-based experience channel, now accessible within Journey Optimizer campaigns. Experience Decisioning decision policies are available for use in code-based experience campaigns only.</p>
<p>Experience Decisioning is currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<img src="assets/do-not-localize/gif-exd.gif"/>
<p>For more information, refer to the <a href="../experience-decisioning/gs-experience-decisioning.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>IP Warmup Workflow</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>If you are sending email on a brand new IP address, you can now easily perform IP warmup workflows directly from the user interface. Adobe Journey Optimizer offers a standardized and efficient way to warm up your IP adresses that follows the best practices for optimal deliverability.</p>
<p>For more information, refer to the <a href="../configuration/ip-warmup-gs.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<!--table>
<thead>
<tr>
<th><strong>Business rules - Beta</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create granular frequency capping rules, and apply them to different types of marketing communications through rule sets. This new capability lets you control how often your audiences receive a message by setting cross-channel rules, that automatically exclude over-solicited profiles from messages and actions.</p>
<p>Business rules capability is currently available as a beta. To join the beta program, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../configuration/business-rules.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table-->


<!--table>
<thead>
<tr>
<th><strong>Extended personalization data - Beta</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now lookup and fetch data values within Adobe Experience Platform datasets, and use these values to build conditions in Adobe Journey Optimizer. You can leverage data from a lookup dataset when a relationship has been defined using an attribute inside of an array of objects. You can specify non-profile enabled datasets for lookup. Once enabled, you can use a profile attribute as a join key to the specified dataset to retrive further data for personalization.</p>
<p>This capability is currently available as a public beta.</p>
</td>
</tr>
</tbody>
</table-->

### Improvements {#e-improvements}

This release comes with the improvements listed below.

**Experience Decisioning** (Limited Availability)

From beta to this release, the following improvements have been added:

* **Experience Decisioning + Code-based experiences** - You can now leverage the Experience decisioning feature to use decision items in your code-based campaigns. Note: The Code-based experience channel and Experience decisioning are not available for organizations that have purchased the Adobe Healthcare Shield and Privacy and Security Shield add-on offerings. [Read more](../code-based/get-started-code-based.md)
* **Context data** - You can now leverage context data from Adobe Experience Platform in your decision rules and rankign formulas. [Read more](../experience-decisioning/context-data.md)
* **New permission** - A new 'Manage Experience decisions' permission is now available for the Decision Management resource. It allows you to manage rights related to Experience Decisioning. [Read more](../experience-decisioning/gs-experience-decisioning.md)
* **Capping rules** - You can now add multiple capping rules for a given decision item in Experience Decisioning. This allows you to increase the level of control over the way offers are sent. [Read more](../experience-decisioning/items.md#capping)
* **Reporting** - You can now create custom reporting dashboards of Experience Decisioning campaigns using [!DNL Customer Journey Analytics]. [Read more](../experience-decisioning/cja-reporting.md)


**Decision Management**

* **Multi-rule support** - You can now add up to 10 capping rules for a given offer in Decision Management. This allows you to increase the level of control over the way offers are sent.
* **Audits** - The **Change log** tab allowing you to see all the changes that have been made to an offer or a decision has been removed. Changes related to offers and decisions can now be seen in the **Audits** menu. 


**Email channel**

<!--
* **List-unsubscribe** - Following on the recent Gmail and Yahoo announcements for bulk senders, Journey Optimizer supports the "post/1-click" List-Unsubscribe option. Refer to the following pages: [Email opt-out management](../email/email-opt-out.md#unsubscribe-header) and [Configure email settings](../email/email-settings.md#list-unsubscribe)
-->

* **Spam scoring** (Beta) - You can now check your content spam scoring in a dedicated Spam report. Using SpamAssassin, Adobe Journey Optimizer can now test your email content and give it a score to indicate if ISPs or Mailbox providers will consider it as a spam or not. [Read more](../content-management/spam-report.md)

   >[!AVAILABILITY]
   >
   >This capability is currently in beta version and only available to beta customers. To join the beta program, contact Adobe Customer Care.

<!--
**Audiences**

* The use of audiences and attributes from audience composition and custom upload (CSV file) is now available for use with Healthcare Shield or Privacy and Security Shield.-->

**Personalization**

* **Expression fragment** - Expression fragments are now available for the **In-app channel**. [Read more](../personalization/use-expression-fragments.md)

**Journeys**

<!--* **Merge policies** (Limited Availability)- Merge policies used by a journey are now visible and consistent throughout the journey.-->
* **mTLS support** - mTLS authentication is now supported in custom actions. There is no additional configuration required in the custom action or journey to activate mTLS; it occurs automatically when an mTLS-enabled endpoint is detected.
* **Lookup tables in events** - You can now leverage data from a lookup dataset when a relationship has been defined using an attribute inside of an array of objects. The lookup values will be available in journeys (conditions, custom actions, etc.) and message personalization. [Read more](../event/experience-event-schema.md#relationships_limitations)
* **Advanced expression editor in Event configuration** - You can now leverage the advanced expression editor while configuring an event, allowing you to define more complex expressions or use functions in the event id condition. This capability is released in Limited Availability (LA) for selected customers.
<!--[Read more](../event/about-creating.md)-->
* **Merge policies** - Merge policies used by a Journey are now visible and consistent throughout the journey. This capability is released in Limited Availability (LA) for selected customers. [Read more](../building-journeys/journey-gs.md#merge-policies)

**Globalization**

As part of our ongoing effort to deliver a unified user experience, we harmonize the terminology used in the Adobe Experience Cloud products and apps. This affects the German term "Titel" which is changed to "Label" when it relates to the name of an object. The changes will be progressively rolled out in the UI and documentation.



