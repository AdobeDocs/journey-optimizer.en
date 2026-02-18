---
solution: Journey Optimizer
product: journey optimizer
title: Release notes 2026
description: Journey Optimizer 2026 Release notes
feature: Release Notes
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: 65ca94cf-8e17-4a25-90f3-238083f81477
---
# Release Notes 2026 {#release-notes-2026}

This page lists all the features and improvements for [!DNL Journey Optimizer] released in 2026.

## January '26 release notes {#jan-26-rn}

<!--**Release date**: January 27-28, 2026-->

The [Features](#jan-26-01-features) and [Improvements](#jan-26-01-improv) sections cover capabilities already available, while [Coming soon](#jan-26-01-coming-soon) lists items scheduled for a later availability date.

### New capabilities {#jan-26-01-features}


<table>
<thead>
<tr>
<th><strong>Decisioning support in Push channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now personalize and optimize the content of your <strong>Push notifications</strong> with <strong>Decisioning</strong>. Use Priority Scores, Formulas, or AI Models to display the best content to your customers.</p>
<p>Experience Decisioning with push notifications requires a specific version of the Mobile SDK. Before implementing this feature, check the <a href="https://developer.adobe.com/client-sdks/home/release-notes/" target="_blank">release notes</a> to identify the required version and ensure you have upgraded accordingly. You can also view all available SDK versions for your platform in <a href="https://developer.adobe.com/client-sdks/home/current-sdk-versions/" target="_blank">this section</a>.</p>
<p>For more information, refer to the <a href="../experience-decisioning/create-decision.md">detailed documentation</a>.</p>
<p>Availability date: January 30, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Direct mail channel in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Previously limited to Campaigns, <strong>Direct Mail</strong> channel is now available on the journey canvas, enabling you to incorporate Direct Mail into your journeys. Direct Mail can now be used in both <strong>batch and 1:1 journey scenarios</strong>, with support for file extraction configuration and time-based frequency settings.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/dm-journey.gif"/></p>
<p>For more information, refer to the <a href="../direct-mail/get-started-direct-mail.md">detailed documentation</a>.</p>
<p>Availability date: January 29, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Quiet hours (time-based exclusions)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Quiet hours</strong> let you define time-based exclusions for Email, SMS, Push, and WhatsApp channels. They ensure that no messages are sent during specific periods of time, helping you respect customer preferences and compliance requirements. You can apply quiet hours through <strong>rule sets</strong>, which can be assigned to individual actions in campaigns or journeys for precise control.</p>
<p>Previously released in Limited Availability, this feature is now available to all environments. With this General Availability release, the feature now includes the ability for customer to queue a campaign action until the completion of Quiet Hours, and the ability to preview the activated Quiet Hours rule.</p>
<p><img src="assets/do-not-localize/quiet-hour-ga.gif"/></p>
<p>For more information, refer to the <a href="../conflict-prioritization/quiet-hours.md">detailed documentation</a>.</p>
<p>Availability date: January 29, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Message export</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Message Export</strong> capability is now available for email and SMS channels. This feature allows you to automatically export sent message content to a dedicated Experience Platform dataset, enabling you to:</p>
<ul>
<li>Meet regulatory compliance requirements (such as HIPAA)</li>
<li>Archive messages for legal claims and customer care inquiries</li>
<li>Retain copies of personalized content sent to individuals</li>
</ul>
<p>Records are retained in the AJO Message Export Dataset for 7 calendar days from ingestion. During this retention period, you can export them to your own storage via Experience Platform destinations. The feature is enabled at the channel configuration level, giving you <strong>granular control</strong> over which messages are exported.</p>
<p>This capability is only available for the email and SMS channel, for organizations that have purchased the Message Export add-on offering. For more information, contact your Adobe representative.</p>
<p><img src="assets/do-not-localize/message-export.gif"/></p>
<p>For more information, refer to the <a href="../configuration/message-export.md#message-export">detailed documentation</a>.</p>
<p>Availability date: January 28, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Direct mail channel in orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Direct mail channel is now available in orchestrated campaigns. The <strong>Direct mail activity</strong> facilitates direct mail sending within your Orchestrated campaign, for both one-time and recurring messages. It serves to automate the process of generating the <strong>extraction file</strong> required by direct mail providers. You can combine channel activities into the Orchestrated campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data.</p>
<p><img src="assets/do-not-localize/dm-oc.gif"/></p>
<p>For more information, refer to the <a href="../orchestrated/activities/channels.md#channel">detailed documentation</a>.</p>
<p>Availability date: January 28, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Agent - Create a Journey</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Agent now offers creation capabilities, enabling Journey Optimizer users to build and configure marketing journeys through a <strong>natural language interface</strong>. With these new skills, practitioners can quickly create journeys by simply describing their requirements in <strong>conversational prompts</strong>. This innovation streamlines the journey creation process, allowing marketers to concentrate on strategy rather than technical configuration.</p>
<p>For more information, refer to the <a href="../start/ai-features.md#journey-agent">detailed documentation</a>.</p>
<p>Availability date: January 12, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Action campaign retrieval API</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new Journey Optimizer API is now available, enabling you to programmatically retrieve and inspect <strong>campaign-related data</strong> such as details, versions, and configurations.</p>
<p>For more information, refer to the <a href="https://developer.adobe.com/journey-optimizer-apis/references/campaigns-retrieve/" target="_blank">detailed documentation</a>.</p>
<p>Availability date: November 24, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Email Designer themes</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now quickly apply <strong>pre-approved themes</strong> to ensure <strong>brand consistency</strong> across all emails, speed up your campaign creation process, and independently produce high-quality emails while reducing dependency on design teams.</p>
<p><img src="assets/do-not-localize/themes.gif"/></p>
<p>Previously released in beta version, this capability is now available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../email/apply-email-themes.md">detailed documentation</a>.</p>
<p>Availability date: November 5, 2025</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#jan-26-01-improv}

#### AI

* **AI Assistant Content Quality Checks** - In addition to brand alignment, you can now evaluate overall <strong>content quality</strong> to uncover potential issues with <strong>readability</strong>, cohesiveness, and effectiveness, independent of your brand guidelines. These automated checks help identify unclear messaging, inconsistent tone, or structural gaps. [Read more](../content-management/brands-score.md#validate-quality). 
  
  [Discover this feature in video](https://video.tv.adobe.com/v/3470544/?learn=on).

#### Journeys

* **Combine native and Adobe Campaign message actions** - Journey Optimizer now lets you combine <strong>Adobe Campaign v7/v8</strong> message actions with <strong>native channel actions</strong> in the same journey. [Read more](../building-journeys/using-adobe-campaign-v7-v8.md)

  Availability date: January 27, 2026.

* **Custom action error response payload** - You can now define an optional <strong>error response payload</strong> for custom actions. When a call fails, the error payload is exposed in the journey context (under the action's errorResponse node) and is available in the <strong>timeout/error branch</strong>, alongside `jo_status_code`, to support richer fallback logic and debugging. [Read more](../action/about-custom-action-configuration.md#define-the-message-parameters)

  Availability date: January 27, 2026.

* **Journey payload size validation in journeys** - Journey Optimizer now validates <strong>payload sizes</strong> to help ensure optimal performance and system stability. When building or publishing journeys, you receive clear <strong>warnings and errors</strong> if payload sizes approach or exceed recommended limits, along with actionable guidance to optimize your journey configuration. This proactive validation helps you identify potential issues early and maintain journey performance. [Read more](../start/guardrails.md#journey-payload-size)

  Availability date: January 27, 2026.


* **Journey alerts** - New <strong>pre-configured alerts</strong> are available for journeys.
  * <strong>Profile Discard Rate Exceeded</strong> - Ratio of profile discards to entered profiles over the last 5 mins exceeded threshold
  * <strong>Custom Action Error Rate Exceeded</strong> - Ratio of custom action errors to successful HTTP calls over the last 5 mins exceeded threshold
  * <strong>Profile Error Rate Exceeded</strong> - Ratio of profiles-in-error to entered profiles over the last 5 mins exceeded threshold

  For more information, refer to the [detailed documentation](../reports/alerts.md).

  Availability date: October 14, 2025.

#### Orchestrated campaigns

* **Data usage label inheritance for audiences** - Labels applied in Adobe Experience Platform now automatically carry over when saving <strong>audiences</strong> in orchestrated campaigns, reducing manual <strong>DULE tagging</strong>. [Read more](../orchestrated/activities/save-audience.md)

* **Predefined filters with parameters** - You can now create <strong>predefined filters</strong> with <strong>parameters</strong> in orchestrated campaigns for reusable, editable rules. [Read more](../orchestrated/predefined-filters.md)

* **Select attributes and copy distribution values** - You can now <strong>select or copy values</strong> directly from the <strong>distribution of values</strong> view in orchestrated campaigns. [Read more](../orchestrated/build-query.md)

* **Message confirmation before send** - A <strong>confirmation step</strong> is now enabled by default before sending orchestrated campaigns to reduce accidental sends. [Read more](../orchestrated/activities/channels.md#confirm-message-sending)

* **Predefined retargeting filters** - To support easier retargeting for orchestrated campaign use cases, this release introduces new <strong>campaign feedback filters</strong>. These filters let you directly target audiences based on <strong>message engagement</strong>, such as sent, opened only, opened or clicked, or opened and clicked, and select the specific campaign or in-transition campaign you want to retarget. [Read more](../orchestrated/retarget.md)

* **Rate control support** - Orchestrated campaigns now support <strong>rate control</strong> to help you pace deliveries and align with <strong>volume constraints</strong>. [Read more](../orchestrated/activities/channels.md#rate-control)

* **Restart button** - Orchestrated campaigns now include a <strong>restart button</strong> so you can quickly <strong>re-launch runs</strong> when needed before publishing the campaign. [Read more](../orchestrated/start-monitor-campaigns.md)

* **User-generated metadata support** - The <strong>executionMetadata helper function</strong> is now available in the personalization editor for Orchestrated campaigns, enabling you to attach contextual information to any native action and store it in a dataset for export to external systems. [Read more](../personalization/functions/helpers.md#execution-metadata)

  Availability date: January 27, 2026.

* **Revert live campaigns to draft status** - You can now revert live orchestrated campaigns to draft status when they encounter execution errors or when you need to modify scheduled campaigns before they start executing. This option is available until the first message is sent. [Read more](../orchestrated/start-monitor-campaigns.md#back-to-draft)

#### Campaigns

* **Schedule Campaign using Profile Time Zone** - Campaign scheduling can now use each profile's <strong>time zone</strong> to deliver messages at the intended local time. [Read more](../campaigns/campaign-schedule.md)

  **Note**: This improvement is only be available for a set of organizations (Limited Availability).

  Availability date: January 27, 2026.

#### Permissions

* **Prevent self-approval for journeys and campaigns** - Added an option when creating or setting <strong>Approval Policy</strong> to prevent journey or campaign creators from <strong>approving their own objects</strong>. [Read more](../test-approve/approval-policies.md)

  Availability date: January 27, 2026.
