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

## January 2024 early release notes {#jan-2024}

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
<p>Leverage a catalog of industry-specific use case playbooks in Real-Time CDP and Journey Optimizer to address common use cases that you can perform using Adobe Experience Platform and Adobe Journey Optimiser.</p><p>Once you have chosen the playbook that best fits your needs, you can enable it to generate the assets needed to support your use case such as journeys, messages, schemas or segments, and customize them to your schema for faster time to value.</p>
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