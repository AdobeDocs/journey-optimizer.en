---
solution: Journey Optimizer
product: journey optimizer
title: Pre release notes for Journey Optimizer
description: Adobe Journey Optimizer Pre Release notes
feature: Release Notes
hide: yes
hidefromtoc: yes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
---
# Pre-release notes {#e-release-notes}

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md). 


## October '25 pre-release notes {#oct-25-10-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the release notes, at the release date.

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


### Improvements

**Execution field for WhatsApp Channel**  

In addition to Email and SMS, you can know update the default execution field for your WhatsApp deliveries at the sandbox level. It is also possible to override the execution field set globally by changing it in the WhatsApp journey activity advanced parameters or in the WhatsApp channel configuration. <!-- [Read more](../FILE.md) -->

**Custom attributes support for Mailto (unsubscribe) address**

With Journey Optimizer, if you are managing consent outside of Adobe, you can set external custom endpoints by defining your own one-click unsubscribe link and a custom unsubscribe email address in the email configuration. When your recipients click the unsubscribe link, Journey Optimizer appends some default profile-specific parameters to the consent update event. 

To further personalize your custom endpoints, you can now define custom attributes that will be also appended to the consent event. [Read more](../email/list-unsubscribe.md#custom-attributes)

>[!AVAILABILITY]
>
>This capability has already been available for the custom **[!UICONTROL One-click Unsubscribe URL]** since August '25 and is now released for the **[!UICONTROL Mailto (unsubscribe)]** option in Limited Availability. Contact your Adobe representative to gain access.

Availability date: October 6, 2025