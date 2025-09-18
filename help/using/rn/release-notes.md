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

## September'25 updates {#sep-updates}

### New capabilities {#Sep-25-features}

<table>
<thead>
<tr>
<th><strong>Dark mode in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Journey Optimizer Email Designer now offers the ability to switch to dark mode view, where you can additionally define specific custom settings that will display only for recipients reading their emails in dark mode.</p>
<p>Note the following:</p>
<ul>
<li>The dark mode final rendering may vary and depends on the recipient's email client.</li>
<li>Not all email clients support custom dark mode. Moreover, some email clients only apply their own default dark mode for all emails that are received. In both cases, the custom settings that you defined in the Email Designer cannot be rendered.</li>
</ul>
<p><img src="assets/do-not-localize/dark-mode.gif"/></p>
<p>For more information, refer to the <a href="../email/dark-mode.md">detailed documentation</a></p>
 <p>Availability date: Sept 16, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey path optimization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Use the new Optimize node to target specific audiences or run A/B tests to determine the best path to meet your business-centric KPIs.</p>
<p>This tool allows you to test and vary, and customize communications, sequencing, and timing to best reach your customers.</p>
<p>This capability is available in Limited Availability. Contact your Adobe representative to gain access.</p>
<p><img src="assets/do-not-localize/optimize.gif"/></p>
<p>For more information, refer to the <a href="../building-journeys/optimize.md">detailed documentation</a></p>
<p>Availability date: Sept 4, 2025</p>
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
<p>This capability is available in Limited Availability. Contact your Adobe representative to gain access.</p>
<p>For more information, refer to the <a href="../configuration/delegate-custom-subdomain.md">detailed documentation</a></p>
<p>Availability date: Sept 4, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Use Adobe Experience Platform data for personalization and decisioning - Limited Availability</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Previously released in public beta, this capability is now available to all environments in Limited Availability. With this release, the following enhancements have been introduced:</p>
<ul><li>Support for dataset lookup personalization in inbound channels.</li>
<li>The "datasetLookup" helper function can now be used within expression fragments. For now, this capability is available for a limited set of customers. To gain access, contact your Adobe representative.</li>
<li>An option in the dataset management interface now allows you to enable record-based datasets for lookup personalization, without having to perform an API call.</li>
<li>Enhanced monitoring to track data ingestion status and know when datasets are ready for lookup.</li>
<li>Updated usage guidelines and guardrails to ensure optimal performance and reliability.</li>
<li>Adobe Experience Platform Datasets can now be leveraged in Decisioning capping rules.</li></ul></p>
<p>For more information, refer to the <a href="../data/lookup-aep-data.md">detailed documentation</a></p>
<p>Availability date: Sept 1, 2025</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#Sep-25-improv}

* **Hourly reset capping frequency** - You can now apply capping on an hourly basis for channel rule sets. Previously available in Limited Availability, this capability is now available to all environments and allows you to choose 1 hour (previously 3 hours). [Read more](../conflict-prioritization/channel-capping.md). AVailability date: September 17

* **Dynamic domain support** - Journey Optimizer now supports complete/base URL personalization for predefined domains accepted by Adobe. [Read more](../personalization/personalization-build-expressions.md#where) <!--Availability date: September 12-->

  >[!NOTE]
  >
  >This capability is available in Limited Availability for a set of customers.

* **Expression for Decisioning capping rules** - You can now build your own expressions to define the threshold of a capping rule for a decision item. [Read more](../experience-decisioning/items.md#capping)

  >[!NOTE]
  >
  >This capability is currently available as a Limited Availability to all users.

* **Channel configuration monitoring alerts** - You can now subscribe to receive system alerts, either by email or in the Journey Optimizer notification center, in case an email channel configuration error using the custom subdomain delegation type happens. [Read more](../reports/alerts.md#alert-dns-record-missing)

## August '25 release notes {#25-8-rn}

**Release date**: August 19, 2025

### New capabilities {#Aug-25-8-features}

New capabilities coming with this release are detailed below.

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
<p><img src="assets/do-not-localize/PauseResume.gif"/></p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../building-journeys/journey-pause.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Calendar view</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A calendar view is now available in the journeys and campaigns lists. It allows you to visualize all journeys and campaigns activations in the respective lists.</p>
<p>Previously available in Limited Availability, this feature is now available to all environments. With this General Availability release, the feature includes:</p>
<ul>
<li>Design improvements for the navigation in dates,</li>
<li>The ability to see draft campaigns if you have set a start and end date,</li>
<li>A new setting to hide and show calendar items running for a long time.</li>
</ul>
<p><img src="assets/do-not-localize/calendar.gif"/></p>
<p>For more information, refer to the <a href="../building-journeys/journey-ui.md#calendar">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>

<!--table>
<thead>
<tr>
<th><strong>Use Adobe Experience Platform data for personalization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Leverage data from [!DNL Adobe Experience Platform] in the personalization editor to personalize your content and decision attributes. In particular, this allows you to extend the definition of your attributes to additional data in datasets for bulk updates that change periodically without having to manually update the attributes one at a time.</p>
<p>With this release, the following enhancements have been introduced:</p>
<ul>
<li>Support of inbound channels,</li>
<li>The "datasetLookup" helper function can now be used within expression and visual fragments to personalize content using data from Adobe Experience Platform datasets,</li>
<li>An option in the dataset now allows you to enable datasets for lookup personalization, without having to perform an API call.</li>
</ul>
<p>This capability is available in Limited Availability. Contact your Adobe representative to gain access.</p>
<p>For more information, refer to the <a href="../personalization/aep-data-perso.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table-->

<!--table>
<thead>
<tr>
<th><strong>Use Decisioning in email channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add Decision policies into email journeys and campaigns. Decision policies are containers for your offers that leverage the Decisioning engine to dynamically return the best content to deliver for each audience member.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/FILE.gif"/></p>
<p><For more information, refer to the <a href="../FILE.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table-->

<table>
<thead>
<tr>
<th><strong>Action activity in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer supports a new generic Action activity that enables you to configure both single actions and multi-action inbound action groups, allowing for streamlined action configuration within the journey canvas. In particular, this new feature allows for:</p>
<ul>
<li>A simplified native action configuration within the journey canvas.</li>
<li>The capacity to create multi-action inbound action groups.</li>
<li>The ability to add optimization to any built-in channel action.</li>
<li>The ability to add both experimentation and multi-lingual options to any action.</li>
</ul>
<p>This capability is available in Limited Availability. Contact your Adobe representative to gain access.</p>
<p><img src="assets/do-not-localize/action-activity.gif"/></p>
<p>For more information, refer to the <a href="../building-journeys/journey-action.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>PDF attachments to emails</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now attach a static PDF file to an email message sent with Journey Optimizer.</p>
<ul>
<li>You can send up to 6 messages with a PDF attachement per profile per year.</li>
<li>The maximum allowed file size for each attachment is 5 MB.</li>
<li>For any additional size or volume, you can purchase an attachment pack add-on. For more details, contact your Adobe representative.</li>
</ul>
<p>This capability is available in Limited Availability. Contact your Adobe representative to gain access.</p>
<p><img src="assets/do-not-localize/pdf-attachments.gif"/></p>
<p>For more information, refer to the <a href="../email/pdf-attachments.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>

<!--
<table>
<thead>
<tr>
<th><strong>Landing page custom forms</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With [!DNL Journey Optimizer], you can now capture profile attributes though your landing pages.</p>
<p>Create, design and manage custom forms tailored to your needs based on a specific dataset. You can then leverage these forms in landing pages to add the profile attributes of your choice into the dataset defined for each form.</p>
<p>This capability is currently in beta version and only available to beta customers. To join the beta program, contact your Adobe representative.</p>
<p><img src="assets/do-not-localize/forms.gif"/></p>
<p>For more information, refer to the <a href="../FILE.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>
-->

<table>
<thead>
<tr>
<th><strong>Optimization in campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now empowers you with the tools to deliver personalized and optimized content to your audience, allowing you to run content experiments, create rule-based targeting, and use advanced combinations of both, to maximize the effectiveness of your campaigns and journeys.</p>
<p>With Optimization, you can:</p>
<ul>
<li>Test multiple content variations to identify the most effective messaging.</li>
<li>Deliver personalized content based on user attributes and contextual data.</li>
<li>Combine targeting and experimentation for advanced strategies.</li>
<li>Filter out users that do not match variant criteria.</li>
<li>Ensure fallback mechanisms to maintain user engagement.</li>
</ul>
<P>Once the journey or campaign is live, profiles are evaluated against the defined criteria, and based on matching criteria, they are delivered with the appropriate experience or content.</p>
<p><img src="assets/do-not-localize/campaign-optimization.gif"/></p>
<p>Previously released on August 8 in campaigns only, this capacity is now also available in journeys starting from August 22.</p>
<p>For more information, refer to the <a href="../campaigns/campaigns-message-optimization.md">detailed documentation</a></p>
</td>
</tr>
</tbody>
</table>

### Improvements {#Aug-25-8-improv}

Improvements coming with this release are listed below.

* **Administration**

  * **Channel configuration monitoring alerts** - You can now subscribe to receive system alerts, either by email or in the Journey Optimizer notification center, in case <!--a channel configuration failure happens or if -->a DNS record is missing. [Read more](../reports/alerts.md#alert-dns-record-missing)

* **AI Assistant**

  * **Content generation in multiple languages** – Content can now be generated in French, Spanish, German, Italian, Japanese, Swedish, Dutch, and Norwegian. [Read more](../content-management/generative-uc.md#languages)

    Availability date: August 25th


* **Campaigns**

  * **Rate control in outbound campaigns** - You can now enable rate control for outbound campaigns (Email, SMS, Push notifications), allowing you to prevent overload on downstream systems, such as landing pages or customer care platforms. [Read more](../campaigns/campaign-schedule.md#rate-control)

  * **Action campaign scheduling** - The campaign daily, weekly, and monthly schedulers have been updated to provide more detailed control over recurring schedules:

    * **Weekly recurrence**: You can now choose to repeat the campaign every week or every two weeks, and select the day(s) of the week on which it should run.

    * **Monthly recurrence**: You can now choose to repeat the campaign every month or every other month, and select the day of the month on which it should run.

    * **Daily, weekly, or monthly schedules**: You can specify if the recurring schedule should stop on a specific date or after a certain number of occurrences.

  * **Scheduled transactional action campaigns** - Scheduled transactional action campaigns are now available for sending batch, audience-based transactional communications via Email, SMS, and Push channels.

* **Channel - Content cards**

  * **Content card layout templates** - The Content card channel now provides OOTB message layouts that will streamline your authoring experience. This release includes Small Image, Large Image, and Image Only layout templates. [Read more](../content-card/design-content-card.md)

* **Channel - Push**

  * **Push notification expiration date** - You can now specify an expiration date for each Push notification, which prevents time-sensitive messages (such as Black Friday Sale) from being sent after a certain date, thus avoids delivering poor experience to your customers.

* **Channel - SMS**

  * **Fuzzy Opt-out** - When enabled, the **Fuzzy Opt-out** option detects inbound messages that closely resemble defined opt-out keywords (e.g., 'CANCIL') and automatically sends a confirmation reply to verify the user's unsubscribe intent. If the user confirms via the defined prompt, they are unsubscribed. [Read more](../sms/sms-configuration-sinch.md)

    >[!NOTE]
    >
    >**Fuzzy Opt-out** is only available with Sinch and Infobip.

  * **Verify SMS Connection** -  You can now easily test and verify your SMS API credentials within Adobe Journey Optimizer by sending a sample message to a designated device. [Read more](../sms/sms-configuration-sinch.md)

* **Configuration**

  * **Custom attributes support with One-click unsubscribe URL** - With Journey Optimizer, if you are managing consent outside of Adobe, you can set an external custom endpoint by defining your own one-click unsubscribe link in the email configuration. When your recipients click the unsubscribe link, Journey Optimizer appends some default profile-specific parameters to the consent update event.
  
    To further personalize your one-click unsubscribe link, you can now define custom attributes that will be also appended to the consent event. [Read more](../email/list-unsubscribe.md#custom-attributes)

* **Datasets**

  * **Experience Decisioning Object Repository - Personalized Offer Items** - Built-in export dataset now captures all offer attributes and lifecycle status, enabling complete personalization and reporting. [Read more](../data/export-datasets.md)

  * Introduced version checking via the `etag` field to improve consistency and track changes to offer items more reliably.

* **Decisioning**

  * **Attach fragments to decision items** - Journey Optimizer now provides the ability to attach fragments to decision items which can be leveraged in code-based experience campaigns through decision policies. This capability is available in Limited Availability for a set of customers. [Read more](../experience-decisioning/create-decision.md#fragments)

* **Journeys**

  * **Journey bulk operations** - From the list of your journeys, you can now select multiple items. Once selected, you can pause or resume up to 10 journeys at a time.

  * **Redirect (302) Support in Custom Actions** - Custom actions can now handle HTTP 302 redirects on a per-request basis. This allows journeys to integrate with APIs that redirect requests to localized or region-specific URLs. Redirects are followed automatically, ensuring the correct content is delivered without extra configuration.

  * **Multiple inbound actions in journeys** - To simplify your journey orchestration, you can now define several inbound actions in a single journey. Previously available in campaigns, this capability enables you to deliver multiple code-based experiences, In-app messages, Content Cards or web actions to different locations at the same time, each action containing a specific content. [Read more](../building-journeys/journey-action.md#multi-action)

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


