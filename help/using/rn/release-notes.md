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

## February 2024 release notes {#feb-2024}

**Release date**: Feb 21-22, 2024

### New capabilities{#feb-features}

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
<p>For more information, refer to the <a href="../in-app/create-in-app-web.md">detailed documentation</a>.<br></br></p>
<img src="assets/do-not-localize/web_inapp.gif">
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Multi-channel content templates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>In addition to Email, content templates are now available for the following channels: Push, In-app, SMS and Direct mail, each channel having dedicated template types. For Email, you can now select the Content type, which allows you to save the subject line as part of your email template. <br/><br/></p>
<p>For more information, refer to the <a href="../content-management/content-templates.md">detailed documentation</a>.<br></br></p>
<img src="assets/do-not-localize/multi-chan-templates.gif">
</tr>
</tbody>
</table>


### Improvements {#feb-improvements}

This release comes with the improvements listed below.

**Audiences**

* **Seed lists** - Variants are now supported when using **seed lists**. The seed addresses receive a copy of all the variants of the same message (such as the different treatments of a content experiment). [Read more](../configuration/seed-lists.md)

Previously available as Beta, the following improvements are now available to all users:

* You can now target **audiences created through audience composition** and leverage enrichment attributes in Journeys. [Learn more](../building-journeys/read-audience.md)

* You can now target **audiences uploaded from a CSV file** into journeys and campaigns. [Learn more](../audience/about-audiences.md#segments-in-journey-optimizer)

   >[!AVAILABILITY]
   >
   >* The use of audiences and attributes from audience composition and custom upload (CSV file) is currently unavailable for use with Healthcare Shield or Privacy and Security Shield.
   >* The **audience upload from a CSV file** improvement is being rolled out gradually over the course of several days following the initial release. While some users have immediate access, others may experience a delay before it becomes available in their environment.

**Journeys**

* **Filter your journeys** - You can now use **custom dates to filter the journeys** inventory, in addition to the existing predefined date filters. This allows you to refine the list by displaying journeys created or published on a specific date, within a particular month, throughout an entire year, or within specified time ranges. [Read more](../building-journeys/journey-gs.md#filter)
* **Custom actions** - You can now update the **content-type** header. This new **content-type** should reference JSON content. [Read more](../action/about-custom-action-configuration.md#url-configuration)
* **Configuration** - The identityMap attribute in stepEvents is now pre-filled. The primary identity is defined as "primary = true". [Read more](../reports/sharing-field-list.md)
* **User interface** - The top bar, in journey screens, has been reorganised for an improved experience. Among the different updates, notice that the "pencil" icon that allows you to access the journey properties is now displayed on the left of the top bar, next to the journey's name. [Read more](../building-journeys/journey-gs.md#change-properties)

**SMS channel**

* **Opt-in/opt-out keywords** - When configuring your SMS channel, you can now customize the **Opt-in and Opt-out keywords** as per your preferences. Journey Optimizer triggers the response based on these specified keywords. [Learn more](../sms/sms-configuration.md#create-api)

**Campaigns**

* **API-triggered campaigns** - The cURL code generated after activating an API-triggered campaign has been enhanced. It now includes all personalizaton (profile and context) variables used in the message. [Read more](../campaigns/api-triggered-campaigns.md#execute) 

**Frequency rules**

* In addition to Email and Push, you can now create Frequency rules for SMS and Direct Mail channels. Frequency rules automatically exclude over-solicited profiles from messages and actions when the frequency cap is reached. [Read more](../configuration/frequency-rules.md)

<!--**Decision management**

* **Capping rules** - You can now add **multiple capping rules** for one offer. This allows you to increase the level of control over the way offers are sent.-->

<!--
**Content templates**

* **Thumbnails** - A **Grid view** is now available for content templates for improved visual access.

   >[!AVAILABILITY]
   >
   >This capability is released in Limited Availability (LA) for a small set of customers.
-->


## January 2024 release notes {#jan-2024}

**Release date**: Jan 30-31, 2024

### New capabilities{#jan24-features}

This release brings the new capabilities listed below.

<table>
<thead>
<tr>
<th><strong>Deliverability Updates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now supports the DMARC authentication technology.</p>
<p>Starting February 1st, 2024, Google and Yahoo! are requiring that you have a DMARC record for any domain you use to send email to them. Make sure that you have DMARC record set up for all the subdomains that you have delegated or are delegating to Adobe in Journey Optimizer.</p>
<p>For more information, refer to the <a href="../configuration/dmarc-record-update.md">detailed documentation</a>.</p>
<br/><img src="assets/do-not-localize/dmarc.gif"/>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Use Case Playbooks</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Leverage a catalog of industry-specific use case playbooks in Real-Time CDP and Journey Optimizer to address common use cases that you can perform using Adobe Experience Platform and Adobe Journey Optimizer.</p><p>Once you have chosen the playbook that best fits your needs, you can enable it to generate the assets needed to support your use case such as journeys, messages, schemas or segments, and customize them to your schema for faster time to value.</p>
<p>For more information, refer to the <a href="../start/playbooks.md">detailed documentation</a>.</p>
<br/><img src="assets/do-not-localize/playbooks.gif"/>
</tr>
</tbody>
</table>

### Improvements {#jan24-improvements}

This release comes with the improvements listed below.

**Reporting**
 
* **New domain based breakdown widgets** - New widgets have been added to enhance your Campaign and Journey reports. The **Bounce Reasons by domain**, **Sent & delivered by domains**, **Opens & Clicks by domain** and **Bounce & errors by domain** widgets provide a detailed breakdown at the domain level for key email delivery and tracking metrics. [Learn more](../reports/channel-report.md) 

**SMS Channel**

* **Double Opt-In** - The Double Opt-In workflow for SMS guarantees that users explicitly opt-in to receive messages when the request is initiated from their device. Users initiate the consent process by sending an inbound SMS message. Upon confirming their consent, a follow-up message is sent, requesting final verification. If a user profile does not exist, it is created upon successful confirmation. [Learn more](../sms/sms-configuration.md#create-api) 

   Note that this capability is available with Sinch and Infobip SMS providers.

**Journeys**

* **Reaction events duration** - The maximum duration that you can define in the **Reaction events** is now 29 days instead of 30. [Learn more](../building-journeys/reaction-events.md)

<!--* **Date filters** - You can now use custom dates to filter the journeys inventory, in addition to the existing predefined date filters. This allows you to refine the list by displaying journeys published on a specific date, within a particular month, throughout an entire year, or within specified time ranges. [Learn more](../building-journeys/journey-gs.md#filter)-->

* **Read audience**  - The **Read Audience** activity now relies on the profile snapshot dataset for batch segments, which is only generated once a day after the scheduled daily batch job is run, hence the data will be fresh up to that last daily batch job. [Learn more](../building-journeys/read-audience.md)

* **Field Groups** - This release fixes an issue which was blocking Field Groups from being saved in certain cases.

* Support of `<listObject>` has been modified in multiple functions.

**Frequency Rules**

* **Weekly and daily frequency cap** - You can now specify the maximum number of messages sent to a customer profile in a week or a day, in addition to month. The frequency cap is based on the selected calendar period and reset at the beginning of the corresponding time frame. [Learn more](../configuration/frequency-rules.md#create-new-rule)


**Decision management**

* **Frequency capping on Edge** - The frequency capping counter is now updated and available in an Edge Decisioning API decision in less than 3 seconds. [Learn more](../offers/api-reference/offer-delivery-api/start-offer-delivery-apis.md)
