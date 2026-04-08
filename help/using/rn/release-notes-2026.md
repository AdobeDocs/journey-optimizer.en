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



## February '26 release notes {#feb-26-01-rn}

### New capabilities {#feb-26-01-features}


<table>
<thead>
<tr>
<th><strong>Journey arbitration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now use <strong>ranking formulas</strong> to automatically boost journey priority scores based on customer profile attributes and contextual factors, ensuring customers enter the most relevant journeys.</p>
<p><img src="assets/do-not-localize/journey-arbitration-formulas.gif"/></p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../conflict-prioritization/journey-ranking-formulas.md">detailed documentation</a>.</p>
<p>Availability date: February 24, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Action activity in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer supports a new generic <strong>Action activity</strong> that enables you to configure both single actions and multi-action inbound action groups, allowing for streamlined action configuration within the journey canvas. In particular, this new feature allows for:</p>
<ul>
<li>A simplified native action configuration within the journey canvas.</li>
<li>The capacity to create multi-action inbound action groups.</li>
<li>The ability to add optimization to any built-in channel action.</li>
<li>The ability to add both experimentation and multilingual options to any action.</li>
</ul>
<p><img src="assets/do-not-localize/action-activity.gif"/></p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../building-journeys/journey-action.md">detailed documentation</a>.</p>
<p>Availability date: February 20, 2026</p>
<p><strong>Note:</strong> All native channels are now accessible through the Action journey activity. Legacy native channel activities will be deprecated with the March release. Existing journeys that include legacy actions will continue to function as is—no migration is required.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Wave sending of outbound messages</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now schedule messages from Journey Optimizer campaigns or journeys to be delivered in controlled batches over time.</p>
<p>Wave sending offers the following benefits:</p>
<ul>
<li>Better deliverability – Spread sends over time to help maintain a strong sender reputation and reduce the risk of being flagged as spam.</li>
<li>Load control – Avoid overwhelming downstream systems (e.g. call centers, landing pages) by limiting how many messages go out at once.</li>
<li>High-volume and time-sensitive use cases – Suited to large audiences or when you need to control timing (e.g. call center capacity, ramp-up, or time-bound offers).</li>
</ul>
<p><img src="assets/do-not-localize/waves.gif"/></p>
<p>In <strong>campaigns</strong>, this capability is available to all environments (General Availability). For more information, refer to the <a href="../campaigns/send-using-waves.md">detailed documentation</a>.</p>

<p>In <strong>journeys</strong>, this capability is only available for a set of organizations (Limited Availability) – To gain access, contact your Adobe representative. For more information, refer to the <a href="../building-journeys/send-using-waves.md">detailed documentation</a>.</p>
<p>Availability date: February 19, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Migrate subdomains to custom delegation</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now migrate subdomains using the CNAME delegation mode to custom delegation directly from the interface, so you can meet stricter security policies in line with your company's guidelines without re-creating channel configurations.</p>
<p><img src="assets/do-not-localize/subdomain-migration.gif"/></p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../configuration/custom-subdomain-migration.md">detailed documentation</a>.</p>
<p>Availability date: February 19, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Web push notifications channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports <strong>Web push notifications</strong>, expanding the push channel beyond mobile. You can seamlessly deliver notifications to both <strong>mobile and desktop browsers</strong>, enabling you to reach customers directly on their devices without requiring an app. This enhancement allows you to engage users with timely, personalized messages in real time, leveraging the same authoring workflows and targeting capabilities already available for mobile push.</p>
<p><img src="assets/do-not-localize/web-push.gif"/></p>
<p>Previously released in Beta, this capability will be available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../push/push-configuration-web.md">detailed documentation</a>.</p>
<p>Availability date: February 13, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Content decision activity</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Content decision activity</strong> is now available in the journey canvas for integrating personalized offers directly into your customer journeys. This activity enables you to deliver decision-based content and reference those offers throughout your journey—in conditions for creating eligibility-based branching, in custom actions for passing offer data to external systems, and in other activities for building fully personalized customer experiences.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/content-decision.gif"/></p>
<p>For more information, refer to the <a href="../building-journeys/content-decision.md">detailed documentation</a>.</p>
<p>Availability date: February 10, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Self-service migration tooling APIs</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Migration tooling APIs are now available to programmatically migrate <strong>Decision management</strong> entities to <strong>Decisioning</strong>, featuring:</p>
<ul>
<li>Flexible migration scopes (sandbox, offer, or decision level)</li>
<li>Automated dependency analysis and validation</li>
<li>Rollback support for completed migrations</li>
<li>Detailed migration reports with object mappings</li>
</ul>
<p>For more information, refer to the <a href="../experience-decisioning/decisioning-migration-api.md">detailed documentation</a>.</p>
<p>Availability date: February 3, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Custom action monitoring</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Gain deeper insight into the health and performance of your custom action endpoints with a new monitoring dashboard and enriched journey step event data. Track successful calls, errors, throughput, response times, and queue wait times to quickly understand when, where, and why anomalies occur.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../action/reporting.md">detailed documentation</a>.</p>
<p>Availability date: February 3, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Decisioning support in SMS channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now personalize and optimize the content of your SMS messages with Decisioning. Use Priority Scores, Formulas, or AI Models to display the best content to your customers.</p>
<p>For more information, refer to the <a href="../experience-decisioning/create-decision.md">detailed documentation</a>.</p>
<p>Availability date: February 2, 2026</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#feb-26-01-improv}

Improvements coming with this release are listed below.

#### Configuration

* **Experience event usage in journey expressions** - Starting April 1, 2026, the use of experience event attributes in journey expressions will no longer be supported for organizations that have not used this capability in the last 90 days. This capability has already been unavailable for new customer organizations since July 8, 2025. For alternatives, see [Experience event lookup in journeys](../building-journeys/exp-event-lookup.md).

#### Content Management

<!--
* **Update brands with new color tab** - Brand guidelines help ensure your brand is presented consistently across all touchpoints. The new <strong>Colors</strong> section defines the standards for your brand's color system, outlining how colors are selected, organized, and applied across experiences. It ensures consistent use of primary, secondary, accent, and neutral colors to support a cohesive, accessible, and recognizable brand identity. [Read more](../content-management/brands.md)
-->

* **Use themes to convert images to email templates** - When converting an image to an email template in Journey Optimizer, you can now use a theme as input so the generated HTML follows your brand parameters. Styling such as background color, button color, fonts, line spacing, margins, and padding is applied automatically, reducing manual design work and delivering a template that is ready to use with minimal edits. [Read more](../content-management/image-to-html.md)

  Availability date: February 17, 2026.

<!--* **Text mode for fragments** - You can now create and manage text versions of your fragments, supporting workflows that rely on plain text content and providing the same flexibility as in email content. [Read more](../content-management/create-fragments.md)-->

#### Email Designer

* **Text indentation** - You can now apply customizable left indentation to the first line of paragraphs in text components directly from the properties panel. <!--The new **Indentation** control lets you define indentation in pixels or percentage via a numeric input or slider, with live preview on the canvas. -->This improves readability for long-form content such as editorials and articles. [Read more](../email/get-started-email-style.md)

  Availability date: February 18, 2026.

#### Decisioning

* **Edge inbound support for using Adobe Experience Platform data in Decisioning** - Using Adobe Experience Platform data in Decisioning now supports edge inbound use cases, in addition to email and custom actions in journeys. [Read more](../experience-decisioning/aep-data-exd.md)

  This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

* **Decisioning preview in Code-based Experience channel** - You can now preview decision items when configuring Decisioning with the Code-based Experience channel. Preview is available directly in the authoring interface before going live. [Read more](../code-based/test-code-based.md#preview-code-based)

  Availability date: February 18, 2026
  
<!--
THIS WAS FINALLY NOT RELEASED IN FEBRUARY

* **Attach fragments to decision items** - Journey Optimizer now provides the ability to attach fragments to decision items which can be leveraged in code-based experience campaigns through decision policies. [Read more](../experience-decisioning/fragments-decision-policies.md)

  Previously released in Limited Availability, this capability is now available to all environments (General Availability).

  Availability date: February 12, 2026.
-->

#### Personalization

* **Execution Metadata helper** - The `executionMetadata` helper function is now available to all Journey Optimizer customers. Use it to dynamically append contextual information to any native action and capture it in a dataset for export to external systems. [Read more](../personalization/functions/helpers.md#execution-metadata)

  Previously released in Limited Availability, this capability is now available to all environments (General Availability).

  Availability date: February 20, 2026.

#### SMS

* **SMS Webhooks** - Webhooks are now supported across all SMS providers. You can configure each webhook based on its intended purpose: Inbound webhooks to capture incoming messages and Feedback webhooks to receive delivery receipts, status updates, and other message-related events. [Read more](../sms/sms-webhook.md)

  Availability date: February 2, 2026.



## January '26 release notes {#jan-26-rn}

<!--**Release date**: January 27-28, 2026-->

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
