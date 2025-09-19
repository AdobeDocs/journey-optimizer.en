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

<!--
## September '25 pre-release notes {#25-9-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the release notes, at the release date.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: September 23-24, 2025

### New capabilities {#sept-25-9-features}

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
<th><strong>Journey Agent is here!</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>AI Assistant now includes foundational Journey Agent skills for Journey Optimizer, enabling practitioners to analyze journeys through a natural language interface. With these new skills, users can analyze and create (coming soon) journeys to detect and resolve potential schedule or audience conflicts.</p>
</td>
</tr>
</tbody>
</table>

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
<li><strong>Multi-Armed Bandit (MAB) Support in Journey Optimizer:</strong> Maximize impact while reducing wasted traffic with Multi-Armed Bandit experiments. Instead of splitting audiences evenly, MAB automatically allocates more visitors to the best-performing variations in real time so you can deliver better experiences to more customers while still learning what works.</li>
</ul>
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

### Improvements

- **Approval policy permissions**
  Added an option when creating or setting Approval Policy to prevent Journey/Campaign creators from approving their own objects.

- **New Journey Alerts**  
  New pre-configured alerts are available for journeys:  
  - Profile Discard Rate Exceeded: Ratio of profile discards to entered profiles over the last 5 mins exceeded threshold.  
  - Custom Action Error Rate Exceeded: Ratio of custom action errors to successful HTTP calls over the last 5 mins exceeded threshold.  
  - Profile Error Rate Exceeded: Ratio of profiles-in-error to entered profiles over the last 5 mins exceeded threshold.

- **Nested JSON body params now supported in custom authentication**  
  When configuring custom authentication for a custom action, nested JSON objects (e.g., sub-objects within `bodyParams`) are now supported.

- **Attach fragments to decision items**  
  Journey Optimizer now provides the ability to attach fragments to decision items which can be leveraged in code-based experience campaigns through decision policies.

- **Custom attributes support with One-click unsubscribe URL**  
  With Journey Optimizer, if you are managing consent outside of Adobe, you can set an external custom endpoint by defining your own one-click unsubscribe link in the email configuration. When your recipients click the unsubscribe link, Journey Optimizer appends some default profile-specific parameters to the consent update event. 

  To further personalize the unsubscribe email address, you can now define custom attributes that will be appended to the consent event. This capability has already been available for the custom one-click unsubscribe link since the August 25 release.

- ***mTLS Support for SMS Channel**
  When setting up a custom SMS provider, you now have the option to enable mutual TLS (mTLS) authentication, which requires both the client and the server to confirm each other's identities before a secure connection is established.

- **Model-based Schemas**  
  For a clearer and more intuitive experience, Relational Schemas are now referred to as Model-based Schemas in Orchestrated campaigns.

- **Dataset lookup support in journeys**  
  A new activity in journeys, **Dataset lookup**, allows you to dynamically retrieve data from Adobe Experience Platform record datasets during runtime. By leveraging this capability, you can access data that may not reside in the profile or event payload, ensuring your customer interactions are both relevant and timely.

- **Simulating content variations for all inbound channels**  
  Previously only available for the Email, SMS, and Push notification channels, simulating content variations now also applies to all inbound channels.

- **Webhook support for API triggered campaigns**  
  API triggered campaigns now support webhooks. Configure a webhook URL to receive real-time status updates for every message, improving observability and enabling seamless monitoring and automation.

- **Redirect Support in Journey Custom Actions**  
  Redirects (302) are now supported in Journey Custom Actions.

- **High throughput mode for API triggered email campaigns**  
  A new High throughput mode is now available in API triggered campaigns. This mode is designed for large-scale, real-time messaging (up to 5000 transactions per second) and provides higher availability with lower latency.  
  This capability is only available for the email channel, for organizations that have purchased the Adobe High throughput transactional messaging add-on offering. Contact your Adobe representative for more details.


- **Hourly reset capping frequency** - You can now apply capping on an hourly basis for channel rule sets. Previously available in Limited Availability, this capability is now available to all environments and allows you to choose 1 hour (previously 3 hours). [Read more](../conflict-prioritization/channel-capping.md). Availability date: September 17
-->