---
solution: Journey Optimizer
product: journey optimizer
title: Release notes
feature: Release Notes
topic: Content Management
description: Adobe Journey Optimizer Release notes
exl-id: 06fa956a-b500-416e-9d42-b683c328e837
---
# Release notes {#release-notes}

>[!CONTEXTUALHELP]
>id="ajo_homepage_card1"
>title="What's new?"
>abstract="**Adobe Journey Optimizer** continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated on the last week of each month in these release notes."

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated on the last week of each month in these release notes. [!DNL Adobe Journey Optimizer] is built natively on [!DNL Adobe Experience Platform] and inherits from its latest innovations and improvements. Learn more about these changes in [Adobe Experience Platform Release Notes](https://experienceleague.adobe.com/docs/experience-platform/release-notes/latest.html){target="_blank"}.


## Campaign Orchestration 

**Availability date**: August 4, 2025

Journey Optimizer now includes **Campaign Orchestration**, a new capability purpose-built for brand-initiated, batch campaigns. This release introduces a campaign orchestration canvas and enhanced data modeling, working together to let marketers plan, target, and deliver personalized cross-channel campaigns.

>[!IMPORTANT]
>
>To access Campaign Orchestration, your license must include either the **Journey Optimizer – Campaigns & Journeys** or the **Journey Optimizer - Campaigns** package. Contact your Adobe representative to confirm your license and update if needed.

![Campaign Orchestration GIF](assets/do-not-localize/release.gif)

It includes [Relational Schemas & Datasets](#oc-relational) and [Campaign Canvas](#oc-canvas). Together, these two innovations unlock a new standard for orchestrating batch campaigns in Journey Optimizer. Key capabilities are listed below.

### Key Capabilities {#oc-capabilities}

* **Multi-step workflows**

  Drive sophisticated multi-channel batch campaigns with the new, purpose-built campaign orchestration canvas. 

* **On-demand audiences**

  Segment audiences on-demand for immediate activation.  

* **Multi-entity segmentation**

  Build audiences using business context (non-people dimensions) such as product, stores, renewals, reservations, and more.  

* **Pre-send visibility** 

  Review, refine, and optimize audiences and campaigns prior to launch and while campaigns are running  

### Campaign Canvas {#oc-canvas}

A brand-new visual orchestration interface purpose-built for batch campaigns. This canvas enables: 

* Visual planning of multi-step, multi-channel campaign flows 

* Support for on-demand audiences built from relational queries 

* Advanced audience splitting, waits, and conditional logic 

* Precise pre-send counts after applying business rules and filters 

### Relational Schemas & Datasets {#oc-relational}

Adobe Journey Optimizer now supports relational entities (e.g., products, stores, bookings, contracts) linked to people-based profiles. This allows segmentation and personalization across multi-dimensional data structures, enabling use cases like: 

* One message per booking, subscription, or contract 

* Segmentation based on related entity attributes (e.g., product category or store location) 

* Enhanced addressability (e.g., send to all known contacts tied to an entity) 

### Why it matters 

This release gives marketers full control over brand-initiated, audience-based batch marketing, combining flexible data modeling with a purpose-built orchestration experience. It is specifically designed for batch campaign orchestration from real-time journeys, while offering advanced personalization and scalability. 

### Learn more

Learn more in the [Campaign orchestration documentation](../orchestrated/gs-orchestrated-campaigns.md).

<!--
## August '25 pre release notes {#25-7-rn}

**Pre release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published at the release date.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: August 19, 2025


### New capabilities {#Aug-25-8-features}

New capabilities coming with this release are detailed below.

### Improvements {#Aug-25-8-improv}

Improvements coming with this release are listed below.
-->

## August '25 updates {#25.8-rn}

<table>
<thead>
<tr>
<th><strong>Optimization in campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now empowers you with the tools to deliver personalized and optimized content to your campaigns' audience, allowing you to run content experiments, create rule-based targeting, and use advanced combinations of both, to maximize the effectiveness of your campaigns.</p>
<p>With Optimization, you can:</p>
<ul>
<li>Test multiple content variations to identify the most effective messaging.</li>
<li>Deliver personalized content based on user attributes and contextual data.</li>
<li>Combine targeting and experimentation for advanced campaign strategies.</li>
<li>Filter out users that do not match variant criteria.</li>
<li>Ensure fallback mechanisms to maintain user engagement.</li>
</ul>
<P>Once the campaign is live, profiles are evaluated against the defined criteria, and based on matching criteria, they are delivered with the appropriate experience or content from the campaign.</p>
<p><img src="assets/do-not-localize/campaign-optimization.gif"/></p>
<p>Release date: August 8, 2025</p>
<p>For more information, refer to the <a href="../campaigns/campaigns-message-optimization.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>



## July '25 release notes {#25-7-rn}

**Release date**: July 29, 2025

### New capabilities {#features-25-7}

New capabilities coming with this release are detailed below.

#### Features

<table>
<thead>
<tr>
<th><strong>Brands</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create and customize your own Brands to clearly define your visual and verbal identity across communications. With the Brand alignment score, you can receive real-time feedback on how well your content reflects your brand's tone, style, and guidelines, helping you stay consistently on-brand with every message you send.</p>
<p>Previously released in Beta, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/brand-score.gif"/></p>
<p>For more information, refer to the <a href="../content-management/brands.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Use Decisioning in email channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add Decision policies into email journeys and campaigns. Decision policies are containers for your offers that leverage the Decisioning engine to dynamically return the best content to deliver for each audience member.</p>
<p>This capability is available in Limited Availability. Contact your Adobe representative to gain access.</p>
For more information, refer to the <a href="../experience-decisioning/create-decision.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>LINE channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer has expanded its cross-channel capabilities to include support for the LINE channel. This enhancement allows you to create, edit, and preview LINE experiences enabling more personalized and engaging interactions. With LINE, you can connect with more customers, send relevant content, and improve your engagement.</p>
<p>Previously available only request, LINE channel is now available to all users (General Availability).</p>
<p>For more information, refer to the <a href="../line/get-started-line.md">detailed documentation</a>.</p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Dry Run</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Dry run is a special journey publication mode in Adobe Journey Optimizer that allows journey practitioners to test a journey using real production data without contacting real customers or updating profile information. This feature helps journey practitioners gain confidence in their journey design and audience targeting before publishing it live.</p>
<img src="assets/do-not-localize/DryRun.gif">
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../building-journeys/journey-dry-run.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Supplemental ID for journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now trigger journeys using a profile ID along with another identifier, such as an order ID, subscription ID, or prescription ID, allowing the same profile to be in the same journey multiple times at once. This enables scenarios like managing multiple orders or subscriptions in parallel, with each instance following its own path through the journey.</p>
<p>Previously released in Limited Availability, the use of supplemental IDs in journeys is now available to all environments. With this General Availability release, the feature now includes support for Read audience journeys.</p>
<p><img src="assets/do-not-localize/gif-supplemental.gif"/></p>
<p>For more information, refer to the <a href="../building-journeys/supplemental-identifier.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>

### In-product alerts 

You can now subscribe to **email and in-product alerts** for Journey Optimizer product releases. 

To subscribe:

* Navigate to **Adobe Experience Cloud Preferences**
* Under **Notifications**, find **Journey Optimizer New releases**
* Enable In-app and email notifications

![](assets/do-not-localize/pulse-notif.png){width="70%" align="left"}


### Change in journey conditions {#ee-change@}

Starting July 8th, in new customer organizations, creating expressions using experience events is no longer supported in the expression editor used in journey conditions. As a result, experience events in the [Experience Platform data source](../datasource/adobe-experience-platform-data-source.md) cannot be used for creating expressions. Alternative approaches and best practices for creating expressions/logic with experience events are referenced [here](../building-journeys/exp-event-lookup.md).

There is no change to how journey context event data is accessed in unitary journeys. In the expression and personalization editors, users can continue to access data passed in with the initial journey event. 

Learn more [in this FAQ](../building-journeys/exp-event-lookup.md#faq-ee).

### Improvements {#25-7-improv}

Improvements coming with this release are listed below.

* **Campaigns**

  * **Multiple inbound actions in campaigns** - To simplify your campaign orchestration, you can now define several inbound actions in a single campaign. This capability enables you to deliver multiple code-based experiences, In-app messages, Content Cards or web actions to different locations at the same time, each action containing a specific content.
  [Read more](../campaigns/campaign-action.md#multi-action)

  * **Campaign inventory reorganization** - Scheduled and API-triggered campaigns are now split into separate tabs in the campaigns inventory for easier navigation and management.
 
  [Read more](../campaigns/modify-stop-campaign.md)

* **Data Management**
  * **Decision Management system datasets update** - The deleted Personalised and Fallback offers are now marked as archived in the "decision_object_repository_personalized_offers" and "decision_object_repository_fallback_offers" datasets. The existing records in the dataset are not changed.

  [Read more](../offers/export-catalog/access-dataset.md)

* **Journeys**
  * **Journey Sandbox Tooling Enhancements** - When copying journeys across multiple sandboxes using the package export and import capabilities, the following capabilities are now also available:
    * Selecting an existing event at the destination
    * Copying over an event independently of a journey
    * Detecting field group / data source relationships, linking to them at the destination if they exist, creating them if they don't.
  
  [Read more](../configuration/copy-objects-to-sandbox.md)

* **Channel - In-app**
  * **In-app Key/Value pairs** - With In-app messages, you can define Key and Value pairs to include custom variables in the message payload. These key-value pairs enable you to pass additional data based on your specific configuration and use case. [Read more](../in-app/design-in-app.md)

* **Channel - Content Card**

  * **Rule-Based Campaign Disqualification** - When editing additional delivery rules, the previous Delivery rules option has been replaced with three distinct rule types to better control message timing and visibility:
    * Show message if: Conditions that determine when the content card is shown.
    * Dismiss message if: Conditions that temporarily hide the content card. It can reappear if show conditions are met again.
    * Disqualify message if: Conditions that permanently prevent the content card from being shown again.
  
    [Read more](../content-card/design-content-card.md)
  
* **Decisioning**
  * **Migration tooling APIs** - The Journey Optimizer team is currently working on migration tooling APIs to migrate Decision management entities to Decisioning. This tooling enables seamless migration between sandboxes with dependency resolution and rollback capabilities. If interested, reach out to your Adobe representative.

* **Personalization**
  * A new helper function, "SHA256", has been added to the personalization editor. This function is used to calculate and return the sha256 hash of a string.

  [Read more](../personalization/functions/string.md#sha256)
