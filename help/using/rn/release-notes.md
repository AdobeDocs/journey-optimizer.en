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

[!DNL Adobe Journey Optimizer] follows a continuous delivery model, allowing Adobe to deliver new features, enhancements, and fixes on an ongoing basis. This approach enables a scalable, phased rollout of capabilities to ensure performance and stability across all environments.

Because of this model, release notes are updated between monthly releases.  A dedicated [Latest updates](#updates-rn) section highlights new capabilities and improvements as they are deployed to production—so you are always informed of all changes in real time. <!--For full details about the release cycle and availability phases, see [Journey Optimizer release cycle](#releases.md).-->

[!DNL Adobe Journey Optimizer] is built natively on [!DNL Adobe Experience Platform] and inherits from its latest innovations and improvements. Learn more about these changes in [Adobe Experience Platform Release Notes](https://experienceleague.adobe.com/docs/experience-platform/release-notes/latest.html){target="_blank"}.

## October '25 pre-release notes {#oct-25-10-rn}

**The pre-release notes below are subject to change without prior notice until the release date**. Links, screens and updated documentation are published in the release notes, at the release date.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: October 22, 2025

### New capabilities {#oct-25-10-features}

<table>
<thead>
<tr>
<th><strong>Quiet Hours / Time Based Exclusions</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Quiet hours let you define time-based exclusions for Email, SMS, Push, and WhatsApp channels. They ensure that no messages are sent during specific periods of time, helping you respect customer preferences and compliance requirements.</p>
<p>You can apply quiet hours through rule sets, which can be assigned to individual actions in campaigns or journeys for precise control. By streamlining these processes.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Custom action monitoring and reporting</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>This capability provides better visibility into journey health and execution, including lifecycle status and performance alerts. You can now quickly understand when, where, and why an anomalous situation is occurring in a custom action.</p>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
</td>
</tr>
</tbody>
</table>

<!--table>
<thead>
<tr>
<th><strong>RCS Basic Messaging</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With the new RCS Basic add-on offering, you can now deliver basic Rich Communication Services (RCS) messaging in Journey Optimizer, enabling the following enhanced messaging capabilities subject to provider and geographical support:</p>
<ul>
<li><strong>Branded and verified sender support:</strong> Send messages using verified business profiles with branding elements (logo, sender name, etc.).</li>
<li><strong>Message delivery insights:</strong> Receive detailed delivery reports including message status updates (e.g., sent, delivered, read).</li>
<li><strong>Link tracking:</strong> Embed and track URLs within RCS messages for engagement analytics.</li>
<li><strong>Fallback to SMS:</strong> Automatic fallback to SMS when the recipient's device does not support RCS or is temporarily unreachable via RCS.</li>
<li><strong>Basic message composition:</strong> Send basic text-based RCS messages.</li>
</ul>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
<!--/td>
</tr>
</tbody>
</table-->

<!--table>
<thead>
<tr>
<th><strong>Direct mail channel in Orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Direct mail channel is now available in orchestrated campaigns. The Direct mail activity facilitates direct mail sending within your Orchestrated campaign, for both one-time and recurring messages. It serves to automate the process of generating the extraction file required by direct mail providers. You can combine channel activities into the Orchestrated campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data.</p>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
<!--/td>
</tr>
</tbody>
</table-->

<!--table>
<thead>
<tr>
<th><strong>Direct Mail channel in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Previously limited to Campaigns, Direct Mail channel is now available on the journey canvas, enabling you to incorporate Direct Mail into your journeys. Direct Mail can now be used in both batch and 1:1 journey scenarios, with support for file extraction configuration and time-based frequency settings.</p>
<p> Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
<!--/td>
</tr>
</tbody>
</table-->

<table>
<thead>
<tr>
<th><strong>New API to retrieve Action Campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new Journey Optimizer API is now available, enabling you to programmatically retrieve and inspect campaign-related data such as details, versions, and configurations.</p>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>New source connectors for loyalty apps</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>New source connectors are now available in Adobe Experience Platform for the Talon.One, Capillary and Kobie loyalty Apps. These connectors let you seamlessly stream loyalty data into Adobe Experience Platform and leverage these data in Journey Optimizer.</p>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Decisioning support in email channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add Decision policies into email journeys and campaigns. Decision policies are containers for your offers that leverage the Decisioning engine to dynamically return the best content to deliver for each audience member.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>High throughput mode for API triggered email campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new High throughput mode is now available in API triggered campaigns. This mode is designed for large-scale, real-time messaging (up to 5000 transactions per second) and provides higher availability with lower latency.</p>
<p>This capability is only available for the email channel, for organizations that have purchased the Adobe High throughput transactional messaging add-on offering. Contact your Adobe representative for more details.</p>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Reusable targeting rules</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows you to create rules from a dedicated UI menu and leverage them when building targeting, either as part of content Optimization in a campaign or a journey, either in the Optimize journey activity.</p>
<p>Targeting rules are currently available to organizations that have purchased the Decisioning add-on offering, and they are available on demand for the other organizations (Limited Availability).</p>
<p>This capability will be progressively rolled out to all customers. In the meantime, contact your Adobe representative to gain access.</p>
<!--img src="assets/do-not-localize/FILE.gif"-->
<!-- p>For more information, refer to the <a href="../FILE.md">detailed documentation</a>.</p -->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Themes in the Email Designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now quickly apply pre-approved themes to ensure brand consistency across all emails, speed up your campaign creation process, and independently produce high-quality emails while reducing dependency on design teams.</p>
<p>Previously released in beta version, this capability is now available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<img src="assets/do-not-localize/themes.gif">
<p>For more information, refer to the <a href="../email/apply-email-themes.md">detailed documentation</a>.</p>
<!--p>Availability date: October 22, 2025</p-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>New Journey Alerts</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>New pre-configured alerts are available to monitor your journey execution:</p>
<ul><li><a href="../reports/alerts.md#alert-discard-rate">Profile Discard Rate Exceeded</a>: Ratio of profile discards to entered profiles over the last 5 mins exceeded threshold</li>
<li><a href="../reports/alerts.md#alert-custom-action-error-rate">Custom Action Error Rate Exceeded</a>: Ratio of custom action errors to successful HTTP calls over the last 5 mins exceeded threshold</li>
<li><a href="../reports/alerts.md#alert-profile-error-rate">Profile Error Rate Exceeded</a>: Ratio of profiles-in-error to entered profiles over the last 5 mins exceeded threshold.</li></ul> <p>You can modify threshold values and subscribe to individual journey-level alerts vs globally.</p>
<p>For more information, refer to the <a href="../reports/alerts.md">detailed documentation</a></p>
<p>Availability date: October 14, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Execution Metadata helper</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new `executionMetadata` helper function is available in the personalization editor. It allows you to append contextual information to any native action and capture it in a dataset for export to external systems.</p>
<p>This capability is available in Limited Availability. Contact your Adobe representative to gain access.</p>
<p>For more information, refer to the <a href="../personalization/functions/helpers.md#execution-metadata">detailed documentation</a></p>
<p>Availability date: October 13, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Experimentation Agent is here!</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Powered by <a href="https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/agent-orchestrator.html" target="_blank">Adobe Experience Platform Agent Orchestrator</a>, Experimentation Agent is available in Journey Optimizer. </p>
<p>The Experimentation Agent is an AI-powered tool that modernizes how you can run and manage digital experiments across websites, emails, push messages, and applications. It helps you run experiments more efficiently, organize business goals, and generate actionable insights, highlighting what worked, what did not, and where to experiment next.</p>
<p>For more information, refer to the <a href="https://experienceleague.adobe.com/docs/experience-cloud-ai/experience-cloud-ai/agents/agent-experiment.html" target="_blank">detailed documentation</a></p>
<p>Availability date: October 10, 2025</p>
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
<li>For any additional size or volume, you can purchase the PDF Attachments add-on. For more details, contact your Adobe representative.</li>
</ul>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><img src="assets/do-not-localize/pdf-attachments.gif"/></p>
<p>For more information, refer to the <a href="../email/pdf-attachments.md">detailed documentation</a></p>
<p>Availability date: Sept 30, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Public API to retrieve journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new Journey Optimizer API is now available to retrieve journeys and their associated objects such as campaigns and surfaces.</p>
<p>For more information, refer to the <a href="https://developer.adobe.com/journey-optimizer-apis/references/journeys-retrieve/">detailed documentation</a></p>
<p>Availability date: Sept 25, 2025</p>
</td>
</tr>
</tbody>
</table>




<!--
## Latest updates {#updates-rn}

New capabilities and improvements released in the past weeks are listed below, with their availability date. They will be grouped with the next release notes content at the end of the month. See also the latest [release notes below](#latest-rn).
-->

### Improvements {#updates-improvements}

**Execution field for WhatsApp Channel**  

In addition to Email and SMS, you can know update the default execution field for your WhatsApp deliveries at the sandbox level. It is also possible to override the execution field set globally by changing it in the WhatsApp journey activity advanced parameters or in the WhatsApp channel configuration. <!-- [Read more](../FILE.md) -->

**Custom attributes support for Mailto (unsubscribe) address**

With Journey Optimizer, if you are managing consent outside of Adobe, you can set external custom endpoints by defining your own one-click unsubscribe link and a custom unsubscribe email address in the email configuration. When your recipients click the unsubscribe link, Journey Optimizer appends some default profile-specific parameters to the consent update event. 

To further personalize your custom endpoints, you can now define custom attributes that will be also appended to the consent event. [Read more](../email/list-unsubscribe.md#custom-attributes)

>[!AVAILABILITY]
>
>This capability has already been available for the custom **[!UICONTROL One-click Unsubscribe URL]** since August '25 and is now released for the **[!UICONTROL Mailto (unsubscribe)]** option in Limited Availability. Contact your Adobe representative to gain access.

Availability date: October 6, 2025

## September '25 release notes {#latest-rn}

**Release date**: September 23-24, 2025

### New capabilities {#sept-25-9-features}

<table>
<thead>
<tr>
<th><strong>Journey Optimizer Experimentation Accelerator</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer Experimentation Accelerator is an AI-first product designed to take your experimentation to the next level. Built for Adobe Journey Optimizer and Adobe Target users, it unifies experiment management, delivers AI-powered insights and opportunities, and introduces a new experimentation agent.</p>
<p>You can look forward to:</p>
<ul>
<li><strong>Unified Experiment Inventory:</strong> Quickly view, filter, and manage all experiments from Adobe Journey Optimizer and Adobe Target in one central workspace.</li>
<li><strong>AI Experiment Insights & Opportunities:</strong> Go beyond statistical readouts with GenAI-driven insights and recommendations. Each experiment now surfaces actionable opportunities, complete with supporting rationale, so teams can more confidently decide what to test next.</li>
<li><strong>Multi-Armed Bandit (MAB) Support in Journey Optimizer:</strong> Maximize impact while reducing wasted traffic with Multi-Armed Bandit experiments. Instead of splitting audiences evenly, MAB automatically allocates more visitors to the best-performing variations in real time so you can deliver better experiences to more customers while still learning what works.</li></ul>
<p><img src="assets/do-not-localize/experimentation-accelerator.gif"/></p>
<p>For more information, refer to the <a href="../content-management/experiment-accelerator.md">detailed documentation</a></p>
<p>Availability date: Oct 3, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Agent is here!</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Powered by <a href="https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/agent-orchestrator" target="_blank">Adobe Experience Platform Agent Orchestrator</a>, Journey Agent is available in Journey Optimizer. It enables you to analyze journeys through a natural language interface. The agent will detect audience or schedule conflicts and profile drop-offs in a journey to help you take steps to resolve them. Soon, you will be able to create journeys with agentic support.</p>
<p>For more information, refer to the <a href="https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/ajo-agent-analyze" target="_blank">detailed documentation</a></p>
<p>Availability date: Sept 24, 2025</p>
</td>
</tr>
</tbody>
</table>

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
<p><img src="assets/do-not-localize/custom-delegation.gif"/></p>
<p>For more information, refer to the <a href="../configuration/delegate-custom-subdomain.md">detailed documentation</a></p>
<p>Availability date: Sept 4, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Use Adobe Experience Platform data for personalization and decisioning</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Previously released in public beta, this capability is now available to all environments. With this release, the following enhancements have been introduced:</p>
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


### Improvements {#sept-25-9-improvements}

* **Webhook support for API triggered campaigns**  
  API triggered campaigns now support webhooks. Configure a webhook URL to receive real-time status updates for every message, improving observability and enabling seamless monitoring and automation. [Read more](../configuration/feedback-webhooks.md)

  Availability date: Sept 29, 2025

* **mTLS Support for SMS Channel**
  When setting up a custom SMS provider, you now have the option to enable mutual TLS (mTLS) authentication, which requires both the client and the server to confirm each other's identities before a secure connection is established. [Read more](../sms/sms-configuration-custom.md) - Availability date: Sept 23, 2025 

* **Model-based Schemas**  
  Model-based schemas can now be used by to support your relational modeling needs in Orchestrated campaigns. [Read more](../orchestrated/gs-schemas.md) - Availability date: Sept 23,2025 

* **Dataset lookup support in journeys**  
  A new activity in journeys, **Dataset lookup**, allows you to dynamically retrieve data from Adobe Experience Platform record datasets during runtime. By leveraging this capability, you can access data that may not reside in the profile or event payload, ensuring your customer interactions are both relevant and timely. [Read more](../building-journeys/dataset-lookup.md) - Availability date: Sept 23,2025 

  This activity is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

* **Redirect Support in Journey Custom Actions**  
  Redirects (302) are now supported in Journey Custom Actions. - Availability date: Sept 23,2025 

* **Channel configuration monitoring alerts** - You can now subscribe to receive system alerts, either by email or in the Journey Optimizer notification center, in case an email channel configuration error using the custom subdomain delegation type happens. [Read more](../reports/alerts.md#alert-channel-config-failure) - Availability date: Sept 23, 2025

* **One-click unsubscribe requests** - We have introduced improvements that further strengthen the handling of one-click unsubscribe requests configured under Adobe Managed, ensuring reliable and consistent processing. - Availability date: Sept 23,2025 

* **Nested JSON body params now supported in custom authentication**  
  When configuring custom authentication for a custom action, nested JSON objects (e.g., sub-objects within `bodyParams`) are now supported. [Read more](../datasource/external-data-sources.md#custom-authentication-mode) - Availability date: Sept 18, 2025 

* **Hourly reset capping frequency** - You can now apply capping on an hourly basis for channel rule sets. Previously available in Limited Availability, this capability is now available to all environments and allows you to choose 1 hour (previously 3 hours). [Read more](../conflict-prioritization/channel-capping.md) - Availability date: Sept 17,2025 

* **Simulating content variations for all inbound channels**  
  Previously only available for the Email, SMS, and Push notification channels, simulating content variations now also applies to all inbound channels. [Read more](../test-approve/simulate-sample-input.md) - Availability date: Sept 17,2025 

* **Expression for Decisioning capping rules** - You can now build your own expressions to define the threshold of a capping rule for a decision item. [Read more](../experience-decisioning/items.md#capping) - Availability date: Sept 16, 2025

* **Dynamic domain support** - Journey Optimizer now supports complete/base URL personalization for predefined domains accepted by Adobe. [Read more](../personalization/personalization-build-expressions.md#where) - Availability date: Sept 12, 2025

  This capability is available in Limited Availability for a set of customers.

* **Webhooks** - This release introduces the following enhancements for Webhooks when configuring a custom SMS provider:

  * You can now define your webhook's purpose, either Inbound or Feedback, depending on the type of data you want to capture. [Read more](../sms/sms-configuration-custom.md#webhook) - Availability date: Sept 23, 2025

  * The interface for configuring keywords has been improved for easier setup. [Read more](../sms/sms-configuration-custom.md#webhook) - Availability date: Sept 23, 2025

* **SMS**

  * When setting up a custom SMS provider, you can now define a **Default** keyword used when an incoming SMS contains an unrecognized keyword. You can also create **Custom** keywords for specific actions. [Read more](../sms/sms-configuration-custom.md) - Availability date: Sept 23, 2025

  * You can now access undefined inbound keywords responses that are sent via an SMS messag, including typos, words, or sentences that are not explicitly defined in the configuration. They are stored in the **AJO Email Tracking Experience Event** dataset, under **InboundMessage** for 13 months. Only available with Sinch, Infobip, and custom SMS provider. - Availability date: Sept 23, 2025

<!--
* **Approval policy permissions**
  Added an option when creating or setting Approval Policy to prevent Journey/Campaign creators from approving their own objects. [Read more](../test-approve/approval-policies.md) - Availability date: Sept 23, 2025-->

<!--
### Coming soon {#sept-25-9-soon}

In the next few days, the following capabilities and enhancements are scheduled for release. **Information is subject to change**. Updated links, screens, and documentation will be shared once these updates are live in production.

<table>
<thead>
<tr>
<th><strong>New Web Push notifications channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports Web Push notifications, expanding the push channel beyond mobile. You can seamlessly deliver notifications to both mobile and desktop browsers, enabling you to reach customers directly on their devices without requiring an app.</p>
<p>This enhancement allows you to engage users with timely, personalized messages in real time, leveraging the same authoring workflows and targeting capabilities already available for mobile push.</p>
<p>For more information, refer to the <a href="../FILE.md">detailed documentation</a></p>
<p>Availability date: Sept XX, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Custom action monitoring and reporting</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Custom action monitoring and reporting is now available. This capability provides better visibility into journey health and execution, including lifecycle status and performance alerts. You can now quickly understand when, where, and why an anomalous situation is occurring in a custom action.</p>
<p>For more information, refer to the <a href="../FILE.md">detailed documentation</a></p>
<p>Availability date: Sept XX, 2025</p>
</td>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>New source connectors for loyalty apps</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>New source connectors are now available in Adobe Experience Platform for the Talon.One, Capillary, and Kobie loyalty apps. These connectors let you seamlessly stream loyalty data into Adobe Experience Platform and leverage these data in Journey Optimizer.</p>
</td>
</tr>
</tbody>
</table>


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
<p>This capability is available in Limited Availability. Contact your Adobe representative to gain access.</p>
<p><img src="assets/do-not-localize/forms.gif"/></p>
<p>For more information, refer to the <a href="../landing-pages/lp-forms.md">detailed documentation</a></p>
<p>Availability date: Sept XX, 2025</p>
</td>
</tr>
</tbody>
</table>
-->
