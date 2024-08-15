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

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated on the last week of each month in these release notes. 

[!DNL Adobe Journey Optimizer] is built natively on [!DNL Adobe Experience Platform] and inherits from its latest innovations and improvements. Learn more about these changes in [Adobe Experience Platform Release Notes](https://experienceleague.adobe.com/docs/experience-platform/release-notes/latest.html){target="_blank"}.

![Newsletter](../assets/do-not-localize/nl-icon.png) Sign up for the [Adobe Journey Optimizer quarterly newsletter](https://www.adobe.com/subscription/Adobe_Journey_Optimizer_NL.html){target="_blank"} today, and receive the latest product updates, exciting stories, use cases, tips and more delivered directly to your inbox every quarter.

## August 2024 early release notes {#e-2024}

**Release date**: August 20-21, 2024

>[!CAUTION]
>
>**Early release notes below are subject to change without prior notice until the release date**. Links, screens and updated documentation are published at the release date.
>

### New capabilities {#e-features}

This release brings the new capabilities detailed below.

<table>
<thead>
<tr>
<th><strong>Guided Channel Setup</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Guided Channel Setup enables you to automate the steps for mobile channel setup in a unified experience to get started faster with Journey Optimizer. This set up facilitates the expeditious configuration of marketing channels, ensuring all required resources are readily available within Experience Platform, Journey Optimizer, and Data Collection. This enables your marketing team to immediately start with campaign and journey creation.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Content Cards</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Content card is a new digital messaging feature in Adobe Journey Optimizer that delivers personalized and engaging content directly within mobile apps and websites. Unlike traditional push notifications, Content Cards integrate seamlessly into the user interface, offering persistent, non-intrusive updates that enhance user interaction and experience.</p>
<p>This feature enables marketers to present relevant, rich media content to users, driving higher engagement and ensuring important messages are seen without disrupting the user journey.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Improved Channel Configurations</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The current channel surface capabilities have been enhanced for a consistent approach across all channels. You can now define, manage, and reuse these configurations for any of your channels.</p>
<p><ul>
<li>Channel surfaces are now renamed to <strong>Channel configurations</strong></li>
<li>From the Channel configurations inventory you can now create reusable channel configurations for all channels, including now Web, In-app messaging, or Code-based experience</li>
<li>Object level access control (OLAC) is now available for each channel configuration, allowing you to decide which of your users are allowed to create or use specific configurations</li>
<li>For some channels, you can create channel configurations that target multiple platforms. An example here would be an In-app messaging channel configuration that can target a web page, an iOS app and an Android app.</li>
</ul></p>
<!--p>For more information, refer to the <a href="../configuration/ip-warmup-gs.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Marketo Engage Custom Action</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now integrate Adobe Journey Optimizer with Adobe Marketo Engage to build your B2B use cases. From a journey, a new custom action allows you to ingest data into Marketo.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Variables in Content Fragments</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Fragments are now able to consume input variables, both in <a href="../personalization/use-expression-fragments.md">expression fragments</a> and <a href="../email/use-visual-fragments.md">visual fragments</a>. You can use those variables to personalize your messages content and parameters, in your campaigns and journeys.</p>
</p>
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
<p>Availability date: Aug, 13</p>
<p>If you are sending email on a brand new IP address, you can now easily perform IP warmup workflows directly from the user interface. Adobe Journey Optimizer offers a standardized and efficient way to warm up your IP adresses that follows the best practices for optimal deliverability.</p>
<p>For more information, refer to the <a href="../configuration/ip-warmup-gs.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


### Improvements {#e-improvements}

This release brings the improvements listed below.

**Journeys**

* In the **Condition** activity, by default, the Time condition is now set by hour, from 00:00 to 12:00. [Read more](../building-journeys/condition-activity.md#time_condition)
* When building your journeys, alerts are now displayed in a drop-down list, to align with campaign alerts and bring a consistent user experience. [Read more](../building-journeys/troubleshooting.md#checking-for-errors-before-testing)
* Zoom options in the journey toolbar have been improved: the zoom percentage is now visible and you can now easily reset the zoom value to 100%.

**Audiences**

* The use of audiences from custom upload (CSV file) is now available for use with Privacy and Security Shield add-on.
* When targeting a custom upload (CSV file) audience, you can now use attributes from the file in your campaigns and journeys. These attributes are available in the personalization editor, to personalize your messages, and the journey advanced expression editor.

## July 2024 release notes {#24-7-2024}

**Release date**: July 30-31, 2024

### New capabilities {#27-4-features}

This release brings the new capabilities detailed below.

<table>
<thead>
<tr>
<th><strong>SMS channel with any provider (Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now configure additional SMS providers within Journey Optimizer, in addition of the default providers Sinch, Infobip, and Twilio.</p>
<img src="assets/do-not-localize/byo_sms.gif"/>
<p>For more information, refer to the <a href="../sms/sms-configuration-custom.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Federated Audience Composition (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Federated Audience Composition is now available in Adobe Journey Optimizer. It allows enterprises to compose data for better utilization across various use cases. With this new approach, as a Adobe Real-Time Customer Data Platform and/or Adobe Journey Optimizer user, you can federate datasets directly from your existing data warehouse to build and enrich Adobe Experience Platform audiences and attributes all in one system.</p>
<p>For more information, refer to the <a href="https://experienceleague.adobe.com/en/docs/federated-audience-composition/using/home"  target="_blank">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#27-4-improvements}

This release comes with the improvements listed below.

**Journeys**

* (Availability date: July 8) **Advanced expression editor in journey event configuration** - You can now leverage the advanced expression editor while configuring an event, allowing you to define more complex expressions or use functions in the Event ID condition. [Learn more](../event/about-creating.md#adv-exp-editor)

## June 2024 release notes {#24-6-2024}

**Release date**: June 18-19, 2024

### New capabilities {#june-24-features}

This release brings the new capabilities detailed below.

<table>
<thead>
<tr>
<th><strong>Content Fragments customization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now define specific fields in a fragment that can be edited when the fragment is added to a campaign or journey. This allows for the adjustment of content portions at the time of use, providing flexibility to override default values with context-specific details.</p>
<img src="../content-management/assets/do-not-localize/gif-fragments.gif"/>
<p>For more information, refer to the <a href="../content-management/customizable-fragments.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Reporting with Customer Journey Analytics (Limited availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer reporting comes with an improved interoperability with Customer Journey Analytics capabilities, standardizing reporting across both platforms and improving data consistency and reliability. This seamless integration between Journey Optimizer and Customer Journey Analytics provides a clearer view of performance metrics, enabling users to make more informed decisions.</p>
<img src="assets/do-not-localize/ajo-cja.gif"/>
<p>For more information, refer to the <a href="../reports/report-gs-cja.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>AI Assistant in Adobe Journey Optimizer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The AI Assistant is a user interface feature that you can use to navigate and understand Adobe concepts and get operational insights for your specific environment. It is available in several products across Adobe Experience Cloud, including Adobe Journey Optimizer.</p>
<p>For more information, refer to the <a href="../start/ai-assistant.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Multilingual messages in journeys and campaigns (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now effortlessly create content in multiple languages within a single campaign or journey. With this feature, you can switch between languages when editing your campaign or your journey, streamlining the entire editing process and improving your capability to efficiently manage multilingual content.</p>
<p>Multilingual content is currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Experimentation in journeys (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Already available in campaigns, Adobe Journey Optimizer now supports experiments in journeys. Experiments are randomized trials, which in the context of online testing, means that you expose some randomly selected users to a given variation of a message, and another randomly selected set of users to some other variation or treatment. After exposure, you can then measure the outcome metrics you are interested in, such as opens of emails, subscriptions, or purchases.</p>
<p>Experimentation in journeys is currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>

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

### Improvements {#june24-improvements}

This release comes with the improvements listed below.

#### Decision Management

* **Multi-rule support in Decision Management** - You can now add up to 10 capping rules for a given offer in Decision Management. This allows you to increase the level of control over the way offers are sent. [Learn more](../offers/offer-library/add-constraints.md#capping)

<!--* **Audits** - The **Change log** tab allowing you to see all the changes that have been made to an offer or a decision has been removed. Changes related to offers and decisions can now be seen in the **Audits** menu. -->

#### Content fragments

>[!AVAILABILITY]
>
>Please note that these enhancements will be rolled out gradually over the course of several days following the initial release. While some users will have immediate access, others may experience a delay before it becomes available in their environments.

* Fragments can now be edited, and changes can be propagated across all live journeys and campaigns where they are used.
* New statuses for content fragments have been introduced: **Draft**, **Live**, **Publishing**, and **Archived**. 
* To use a fragment in a journey or campaign, it must now be in the **Live** status. A new step has been added to the fragment creation process, allowing the fragment to be published and made available for use in journeys and campaigns. Note that fragment publishing requires a new permission.
   
   **CAUTION** - Since **Draft** and **Live** statuses have been introduced with Journey Optimizer June release, all fragments created before this release have the **Draft** status, even if they are used in a journey or campaign. If you make any change to these fragments, you need to [publish them](../content-management/create-fragments.md#publish) to make them "Live" and propagate the changes to the associated campaigns and journeys. You also need to create a new journey/campaign version and publish it.

Read more in the [content fragment](../content-management/fragments.md) documentation.

#### Journeys

* Global timeout of Journeys has been extended to 91 days. [Read more](../building-journeys/journey-properties.md#global_timeout)

    Any new journeys created will have this new timeout reflected. Please refer to this [FAQ section](../building-journeys/journey-properties.md#timeout-faq) to learn more. Please note these changes will be rolled out gradually over the course of the month of June.


* Adobe Journey Optimizer now supports privacy delete/access requests as well as data life cycle management requests. [Read more](../privacy/requests.md)
* You can now resize the columns in the journey inventory.
<!--* **Advanced expression editor in Event configuration** is now GA - You can now leverage the advanced expression editor while configuring an event, allowing you to define more complex expressions or use functions in the event id condition. This capability is released in Limited Availability for selected customers. [Read more](../event/about-creating.md)-->
* **Merge policies** are now GA - Merge policies used by a Journey are now visible and consistent throughout the journey. [Read more](../building-journeys/journey-properties.md#merge-policies)



#### Campaigns

* When creating a campaign in Adobe Journey Optimizer, you can now choose the campaign type (scheduled or triggered) in a new modal. [Read more](../campaigns/create-campaign.md)

#### Email channel

* **List-unsubscribe** - Following on the recent Gmail and Yahoo announcements for bulk senders, Journey Optimizer supports the "post/1-click" List-Unsubscribe option. Refer to the following pages: [Email opt-out management](../email/email-opt-out.md#unsubscribe-header) and [Configure email settings](../email/email-settings.md#list-unsubscribe).

    **NOTE** - For any new channel surface, by default the list unsubscribe header option is activated. For existing surfaces, by default the One-click unsubscribe URL option in the channel surface settings is unchecked. If you were using a one-click opt out URL in the body of the email previously, this setting is still valid. If the One-click unsubscribe URL in the channel surface settings is checked, Adobe Journey Optimizer will rather use the default generated One-click unsubscribe URL in the channel surface settings.

#### SMS channel

* You can now add unique short codes for each sandbox with a single API configuration, making the process more efficient and streamlined. [Learn more](../sms/sms-configuration.md)

* After creation, the **API Token** field on the **API credential details** page is now masked.

<!--* You can now modify existing SMS configurations.-->

#### In-app channel

<!--* **Expression fragment** - Expression fragments are now available for the **In-app channel**. [Read more](../personalization/use-expression-fragments.md)-->

* You can now use the Edge Delivery plugin to get information needed to understand and troubleshoot your inbound implementations. [Learn more on Edge Delivery view](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/view/edge-delivery){target="_blank"}.


#### Direct mail channel

* Direct mail channel is now available for all customers. [Read more](../direct-mail/get-started-direct-mail.md)

