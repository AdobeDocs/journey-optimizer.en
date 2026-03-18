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

## March '26 pre-release notes {#march-26-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the release notes, at the release date.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: March 26, 2026

### New capabilities {#march-26-features}

<table>
<thead>
<tr>
<th><strong>LLM email optimizer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now optimize your email content for deliverability using large language model (LLM) technology. The LLM email optimizer analyzes your email content and provides actionable recommendations to improve sender reputation, avoid spam filters, and enhance overall deliverability performance.</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-14340">DOCAC-14340</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Convert images to email content templates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now convert images into email content templates directly in Journey Optimizer. Use AI-powered analysis to automatically generate structured HTML templates from visual references, significantly reducing email design time.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-14324">DOCAC-14324</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Incremental query activity in Orchestrated Campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Incremental query</strong> activity is now available in Orchestrated Campaigns. This activity queries only new or updated records since the last workflow execution, significantly reducing processing time and improving efficiency for recurring campaigns targeting large datasets.</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-14262">DOCAC-14262</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Transactional messages in Orchestrated Campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Orchestrated Campaigns now support <strong>transactional messaging</strong>, enabling you to trigger real-time, event-driven messages—such as order confirmations, booking notifications, and account updates—directly within your campaign workflow.</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-14233">DOCAC-14233</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Test activity in Orchestrated Campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Test</strong> activity is now available in Orchestrated Campaigns. This activity routes workflow execution to different branches based on defined conditions, enabling you to validate campaign logic and configurations before activating live deliveries.</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-14115">DOCAC-14115</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Custom forms in landing pages</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create <strong>custom forms</strong> in landing pages to collect specific subscriber data beyond standard opt-in fields. Define your own form fields, validation rules, and submission behaviors to support a wider range of subscription and profile enrichment use cases.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-13963">DOCAC-13963</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Agent: Create Orchestrated Campaign use case</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Journey Agent</strong>, powered by Adobe Experience Platform Agent Orchestrator, can now create complete <strong>Orchestrated Campaign</strong> use cases through a natural language interface. Describe your campaign goal and requirements in plain language, and Journey Agent configures the campaign structure, activities, and targeting for you.</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-13768">DOCAC-13768</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>New profile acquisition in landing pages</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Landing pages now support <strong>new profile acquisition</strong> workflows, enabling you to capture and onboard new audience members directly from your landing page experiences. Configure acquisition forms to collect profile data and automatically provision new profiles in Adobe Experience Platform.</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-13757">DOCAC-13757</a></p>
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
<p><strong>Journey path optimization</strong> uses AI to analyze historical journey performance and automatically select the best path for each customer, maximizing conversion and engagement outcomes.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-13492">DOCAC-13492</a></p>
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
<p>You can now use <strong>Decisioning</strong> to personalize and optimize the content of your email messages. Leverage Priority Scores, Formulas, or AI Models to display the most relevant offers and content to each recipient.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-13182">DOCAC-13182</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Message inbox</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Message Inbox</strong> is now available in Adobe Journey Optimizer, providing a centralized view of received in-app, push, and SMS messages. Recipients can access and interact with all their messages in one place, enabling richer engagement and re-engagement scenarios.</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-11382">DOCAC-11382</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Native channel action activities deprecated</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Following the General Availability of the <strong>Action activity</strong> in February 2026, legacy native channel action activities (Email, SMS, Push, In-App, etc.) in the journey canvas are now deprecated. Existing journeys using legacy channel activities continue to function without any changes or migration required.</p>
<p>Documentation JIRA task: <a href="https://jira.corp.adobe.com/browse/DOCAC-14144">DOCAC-14144</a></p>
</td>
</tr>
</tbody>
</table>

### Improvements {#march-26-improv}

Improvements coming with this release are listed below.

#### Journeys

* **Dataset lookup support in journeys** - You can now look up data from Adobe Experience Platform datasets directly within journey conditions, expressions, and actions, enriching personalization with catalog data, reference tables, and other structured datasets. Previously released in Limited Availability, this capability is now available to all environments (General Availability).
  Documentation JIRA task: [DOCAC-14351](https://jira.corp.adobe.com/browse/DOCAC-14351)

* **Journey Arbitration - AI Models** - In addition to ranking formulas, AI models can now be used with Journey Arbitration to automatically rank and prioritize journey entry for customers, using machine learning to determine the most relevant journey for each profile based on historical behavior and contextual signals. This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

  Availability date: February 26, 2026
  Documentation JIRA task: [DOCAC-14295](https://jira.corp.adobe.com/browse/DOCAC-14295)

#### Reporting

* **Exclude bot clicks for email and SMS reporting** - Email and SMS reporting now automatically filters out bot clicks from click metrics, providing more accurate engagement data and preventing automated traffic from inflating your performance figures.
  Documentation JIRA task: [DOCAC-14354](https://jira.corp.adobe.com/browse/DOCAC-14354)

* **Send-Time Optimization: updated controls location and new lift report** - Send-Time Optimization (STO) controls have been relocated from the Action left rail to the Action configuration. Additionally, a new lift report is now available in Journeys reports to measure the impact of STO on your campaign performance metrics.

  Availability date: March 10, 2026
  Documentation JIRA task: [DOCAC-14335](https://jira.corp.adobe.com/browse/DOCAC-14335)

#### Email Designer

* **Open-time personalization using Dynamic Media (Beta)** - You can now personalize email content at open time using Adobe Dynamic Media assets, enabling real-time, recipient-specific images and visuals that are generated dynamically based on each recipient's attributes at the moment of email opening. This capability is currently in Beta.
  Documentation JIRA task: [DOCAC-14353](https://jira.corp.adobe.com/browse/DOCAC-14353)

* **Email Designer displayed in Unified Shell** - The Email Designer is now displayed within the Unified Shell experience, providing a consistent navigation and header experience that aligns with other Adobe applications.
  Documentation JIRA task: [DOCAC-14254](https://jira.corp.adobe.com/browse/DOCAC-14254)

* **Text mode support in fragments** - Fragments now support text mode editing, allowing you to create and manage plain text versions of your content fragments for use in text-based email workflows and multi-channel scenarios.
  Documentation JIRA task: [DOCAC-14204](https://jira.corp.adobe.com/browse/DOCAC-14204)

#### Decisioning

* **Expression Fragment Reference change feed support in Edge Decisioning** - This enhancement allows changes in fragment references to automatically be reflected in all items that reference fragments, without needing to refresh anything manually (republishing the campaign or decision policy).
  Documentation JIRA task: [DOCAC-14350](https://jira.corp.adobe.com/browse/DOCAC-14350)

* **Optional fragments in decision items** - Fragments attached to decision items can now be configured as optional, providing greater flexibility in content composition when not all decision item renderings require a specific fragment.
  Documentation JIRA task: [DOCAC-14309](https://jira.corp.adobe.com/browse/DOCAC-14309)

#### Configuration

* **URL parameters encryption** - URL parameters in tracking links and landing pages can now be encrypted, providing an additional layer of security for sensitive parameter data. This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.
  Documentation JIRA task: [DOCAC-14349](https://jira.corp.adobe.com/browse/DOCAC-14349)

* **Folders for journeys and campaigns** - You can now organize your journeys and campaigns into folders, enabling structured navigation and easier management for teams working with large volumes of content. This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.
  Documentation JIRA task: [DOCAC-14038](https://jira.corp.adobe.com/browse/DOCAC-14038)

#### Orchestrated campaigns

* **Global variables in Orchestrated Campaigns** - Orchestrated Campaigns now support global variables that can be defined once and reused across all activities within a workflow, simplifying configuration and ensuring consistency in dynamic values, expressions, and content personalization.
  Documentation JIRA task: [DOCAC-14113](https://jira.corp.adobe.com/browse/DOCAC-14113)

* **Target dimension simplification in Orchestrated Campaigns** - The target dimension configuration in Orchestrated Campaigns has been simplified, reducing the steps and complexity required when defining audience targeting for your campaign workflows.
  Documentation JIRA task: [DOCAC-13554](https://jira.corp.adobe.com/browse/DOCAC-13554)

<!--
## February '26 pre-release notes {#feb-26-01-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the release notes, at the release date.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: February 17, 2026

### New capabilities {#feb-26-01-features}

<table>
<thead>
<tr>
<th><strong>Wave sending of outbound messages</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can schedule outbound messages from <strong>campaigns</strong> or <strong>journeys</strong> to be delivered in controlled <strong>batches</strong> over time.</p>
<p>Wave sending offers the following benefits:</p>
<ul>
<li>Better <strong>deliverability</strong> – Spread sends over time to help maintain a strong <strong>sender reputation</strong> and reduce the risk of being flagged as spam.</li>
<li><strong>Load control</strong> – Avoid overwhelming downstream systems (e.g. call centers, landing pages) by limiting how many messages go out at once.</li>
<li>High-volume and time-sensitive use cases – Suited to large audiences or when you need to control timing (e.g. call center capacity, ramp-up, or time-bound offers).</li>
</ul>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey arbitration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now use <strong>formulas</strong> and <strong>AI models</strong> to automatically boost <strong>journey priority scores</strong> based on customer profile attributes and contextual factors, ensuring customers enter the most relevant journeys.</p>
<p>This capability is only available for a set of organizations (<strong>Limited Availability</strong>). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Journey Agent: Channel Content Create</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Powered by <strong>Adobe Experience Platform Agent Orchestrator</strong>, <strong>Journey Agent</strong> is available in Journey Optimizer and enables you to analyze journeys through a <strong>natural language interface</strong>. You can now also generate and manage channel-specific content directly in Journey Agent, creating content for channels such as email and push, applying and previewing templates, refining tone and style through prompts, and opening content in <strong>Content Designer</strong> for in-context editing.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Mobile Live Activities</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Live Activities</strong> provide <strong>real-time updates</strong> and interactive experiences within mobile apps, allowing users to stay informed about ongoing events or tasks directly on their device's screen. This feature enhances engagement by delivering live information, such as progress tracking, event updates, or interactive content, without requiring users to open the app.</p>
<p>Previously released in beta, this capability is now available to all environments (<strong>General Availability</strong>).</p>
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
<p>Journey Optimizer supports a new generic <strong>Action activity</strong> that enables you to configure both single actions and <strong>multi-action inbound action groups</strong>, allowing for streamlined action configuration within the <strong>journey canvas</strong>. In particular, this new feature allows for:</p>
<ul>
<li>A simplified native action configuration within the journey canvas.</li>
<li>The capacity to create multi-action inbound action groups.</li>
<li>The ability to add <strong>optimization</strong> to any built-in channel action.</li>
<li>The ability to add both <strong>experimentation</strong> and <strong>multilingual</strong> options to any action.</li>
</ul>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Web Push notifications channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports <strong>Web Push notifications</strong>, expanding the push channel beyond mobile. You can seamlessly deliver notifications to both mobile and desktop browsers, enabling you to reach customers directly on their devices without requiring an app. This enhancement allows you to engage users with timely, personalized messages in real time, leveraging the same <strong>authoring workflows</strong> and <strong>targeting capabilities</strong> already available for mobile push.</p>
<p>Previously released in beta, this capability is now available to all environments (<strong>General Availability</strong>).</p>
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
<p>A new <strong>Content decision activity</strong> is now available in the <strong>journey canvas</strong> for integrating <strong>personalized offers</strong> directly into your customer journeys. This activity enables you to deliver decision-based content and reference those offers throughout your journey—in conditions for creating eligibility-based branching, in custom actions for passing offer data to external systems, and in other activities for building fully personalized customer experiences.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (<strong>General Availability</strong>).</p>
<p><img src="assets/do-not-localize/content-decision.gif"/></p>
<p>For more information, refer to the <a href="../building-journeys/content-decision.md">detailed documentation</a>.</p>
<p>Availability date: February 11, 2026</p>
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
<p><strong>Migration tooling APIs</strong> are now available to programmatically migrate <strong>Decision management</strong> entities to <strong>Decisioning</strong>, featuring:</p>
<ul>
<li>Flexible migration scopes (<strong>sandbox</strong>, <strong>offer</strong>, or <strong>decision</strong> level)</li>
<li>Automated <strong>dependency analysis</strong> and validation</li>
<li><strong>Rollback support</strong> for completed migrations</li>
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
<p>Gain deeper insight into the health and performance of your <strong>custom action endpoints</strong> with a new <strong>monitoring dashboard</strong> and enriched <strong>journey step event data</strong>. Track successful calls, errors, throughput, response times, and queue wait times to quickly understand when, where, and why anomalies occur.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (<strong>General Availability</strong>).</p>
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
<p>You can now personalize and optimize the content of your <strong>SMS messages</strong> with <strong>Decisioning</strong>. Use <strong>Priority Scores</strong>, <strong>Formulas</strong>, or <strong>AI Models</strong> to display the best content to your customers.</p>
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


* **Subdomain delegation method switching** - You can now switch from one <strong>subdomain delegation</strong> method to another. This enables you to migrate domains using the <strong>CNAME delegation</strong> mode to the <strong>custom delegation</strong> method to adhere to your company's security policies.

  **Note**: This capability is only available for a set of organizations (<strong>Limited Availability</strong>). To gain access, contact your Adobe representative.


#### Email Designer

* **Use a brand theme to convert an image to an email template** - When converting an image to an email template in Journey Optimizer, you can now use a <strong>theme</strong> as input so the generated HTML follows your <strong>brand parameters</strong>. Styling such as background color, button color, fonts, line spacing, margins, and padding is applied automatically, reducing manual design work and delivering a template that is ready to use with minimal edits.


* **Update brands with new color tab** - <strong>Brand guidelines</strong> help ensure your brand is presented consistently across all touchpoints. The new <strong>Colors section</strong> defines the standards for your brand's color system, outlining how colors are selected, organized, and applied across experiences. It ensures consistent use of primary, secondary, accent, and neutral colors to support a cohesive, accessible, and recognizable brand identity.


#### AI

* **Integration of custom Firefly models and third-party image generation models** - Enable seamless integration of standard and custom <strong>Firefly models</strong>, along with approved <strong>third-party image models</strong> (e.g., NanoBanana), to provide greater flexibility, control, and brand alignment when generating images. This allows you to select the best model for each use case: standard Firefly for general needs, custom Firefly for on-brand generation, or approved third-party models for specialized or experimental scenarios.


#### Experience Decisioning

* **Edge inbound support for using Adobe Experience Platform data in Decisioning** - Decisioning support of <strong>Experience Platform data lookup</strong> now includes <strong>edge inbound</strong> channel use cases. The capability remains in Limited Availability; General Availability of the underlying data lookup feature is not yet announced (AEP/product dependency).

  **Note**: This capability is only available for a set of organizations (<strong>Limited Availability</strong>). To gain access, contact your Adobe representative.


* **Experience Decisioning preview in Code-based Experience channel** - You can now preview <strong>decision items</strong> when configuring <strong>Experience Decisioning</strong> with the <strong>Code-based Experience</strong> channel. Preview is available directly in the authoring interface before going live.


* **Offer Ranking AI Model Observability** - Journey Optimizer now allows you to monitor the <strong>health</strong>, <strong>training status</strong>, and <strong>performance</strong> of your <strong>AI models</strong> in Decisioning—so you can verify training success, troubleshoot failures, and understand impact on your outcomes. This capability is available for personalized optimization models only (not auto-optimization).


* **Attach fragments to decision items** - Journey Optimizer now provides the ability to attach <strong>fragments</strong> to <strong>decision items</strong> which can be leveraged in code-based experience campaigns through <strong>decision policies</strong>.

  **Note**: Previously released in Limited Availability, this capability is now available to all environments (General Availability).

  Availability date: February 12, 2026.


#### Journeys

* **Multiple inbound actions in journeys** - To simplify your journey orchestration, you can now define several <strong>inbound actions</strong> in a single journey. Previously available in campaigns, this capability enables you to deliver multiple <strong>code-based experiences</strong>, <strong>in-app messages</strong>, <strong>content cards</strong>, or <strong>web actions</strong> to different locations at the same time, each action containing specific content.

  **Note**: Previously released in Limited Availability, this capability is now available to all environments (General Availability).


* **SMS Webhooks** - <strong>Webhooks</strong> are now supported across all SMS providers. You can configure each webhook based on its intended purpose: <strong>Inbound webhooks</strong> to capture incoming messages and <strong>Feedback webhooks</strong> to receive delivery receipts, status updates, and other message-related events. [Read more](../sms/sms-webhook.md)

  Availability date: February 2, 2026.

-->
<!--
## January '26 pre-release notes {#jan-26-01-rn}

**The pre-release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the release notes, at the release date.

See also [Adobe Experience Platform Pre-release notes](https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/pre-release-notes){target="_blank"}.

**Release date**: January 27, 2026

### New capabilities {#jan-26-01-features}

<table>
<thead>
<tr>
<th><strong>Action activity in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer supports a new generic <strong>Action activity</strong> that enables you to configure both single actions and <strong>multi-action inbound action groups</strong>, allowing for streamlined action configuration within the journey canvas. In particular, this new feature allows for:</p>
<ul>
<li>A simplified native action configuration within the journey canvas.</li>
<li>The capacity to create multi-action inbound action groups.</li>
<li>The ability to add optimization to any built-in channel action.</li>
<li>The ability to add both experimentation and multi-lingual options to any action.</li>
</ul>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-111916">Link to PRODUCT JIRA task</a></p>
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
<p>Gain deeper insight into the health and performance of your custom action endpoints with a new <strong>monitoring dashboard</strong> and enriched journey step event data. Track successful calls, errors, throughput, response times, and queue wait times to quickly understand when, where, and why anomalies occur.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-126869">Link to PRODUCT JIRA task</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Quiet Hours / Time Based Exclusions</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Quiet hours let you define <strong>time-based exclusions</strong> for Email, SMS, Push, and WhatsApp channels. They ensure that no messages are sent during specific periods of time, helping you respect customer preferences and compliance requirements. You can apply quiet hours through <strong>rule sets</strong>, which can be assigned to individual actions in campaigns or journeys for precise control.</p>
<p>Previously released in Limited Availability, this feature is now available to all environments. With this General Availability release, the feature now includes the ability for customer to queue a campaign action until the completion of Quiet Hours, and the ability to preview the activated Quiet Hours rule.</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-63912">Link to PRODUCT JIRA task</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Direct Mail channel in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Previously limited to Campaigns, the <strong>Direct Mail channel</strong> is now available on the <strong>journey canvas</strong>, enabling you to incorporate Direct Mail into your journeys. Direct Mail can now be used in both batch and 1:1 journey scenarios, with support for file extraction configuration and time-based frequency settings.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-38399">Link to PRODUCT JIRA task</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Web Push notifications channel</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports <strong>Web Push notifications</strong>, expanding the push channel beyond mobile. You can seamlessly deliver notifications to both mobile and desktop browsers, enabling you to reach customers directly on their devices without requiring an app. This enhancement allows you to engage users with timely, personalized messages in real time, leveraging the same authoring workflows and targeting capabilities already available for mobile push.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-37866">Link to PRODUCT JIRA task</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Decisioning support in Push and SMS channels</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now add <strong>Decision policies</strong> into push and SMS journeys and campaigns. Decision policies are containers for your offers that leverage the Decisioning engine to dynamically return the best content to deliver for each audience member.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-55817">Link to PRODUCT JIRA task</a> | <a href="https://jira.corp.adobe.com/browse/CJM-55818">Link to PRODUCT JIRA task</a></p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Direct mail channel in Orchestrated campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Direct mail channel is now available in orchestrated campaigns. The <strong>Direct mail activity</strong> facilitates direct mail sending within your Orchestrated campaign, for both one-time and recurring messages. It serves to automate the process of generating the <strong>extraction file</strong> required by direct mail providers. You can combine channel activities into the Orchestrated campaign canvas to create cross-channel campaigns that can trigger actions based on customer behavior and data.</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-82584">Link to PRODUCT JIRA task</a></p>
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
<p>New <strong>source connectors</strong> are now available in Adobe Experience Platform for the Talon.One, Capillary and Kobie loyalty Apps. These connectors let you seamlessly stream loyalty data into Adobe Experience Platform and leverage these data in Journey Optimizer.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Message Export</strong><br/></th>
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
<p>Records are retained in the AJO Message Export Dataset for <strong>7 calendar days from ingestion</strong>. During this retention period, you can export the data to your own storage via Experience Platform destinations. The feature is enabled at the channel configuration level, giving you granular control over which messages are exported.</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-105313">Link to PRODUCT JIRA task</a></p>
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
<p>Journey Create Agent enables Journey Optimizer users to build and configure marketing journeys using a natural language interface. With Journey Create Agent, practitioners can quickly create journeys by describing their requirements in conversational prompts. The agent streamlines journey creation, allowing marketers to focus on strategy rather than technical configuration.</p>
<p><a href="https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/ajo-agent#journey-create-agent-skill-overview-and-user-guide" target="_blank">Learn more</a></p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-95142">Link to PRODUCT JIRA task</a></p>
<p>Availability date: January 12, 2026</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>New API to retrieve Action Campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new <strong>Journey Optimizer API</strong> is now available, enabling you to programmatically retrieve and inspect campaign-related data such as details, versions, and configurations.</p>
<p>For more information, refer to the <a href="https://developer.adobe.com/journey-optimizer-apis/references/campaigns-retrieve/">detailed documentation</a>.</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-96195">Link to PRODUCT JIRA task</a></p>
<p>Availability date: November 24, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>New journey alerts</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Three new <strong>journey alerts</strong> are now available to help you monitor and track journey lifecycle events and custom action performance:</p>
<ul>
<li><strong>Journey Published</strong>: Receive notifications when a journey is published by a practitioner in the journey canvas.</li>
<li><strong>Journey Finished</strong>: Get alerts when a journey has finished, with specific definitions based on journey type (Read Audience or Event-triggered).</li>
<li><strong>Custom Action Capping Triggered</strong>: Be notified when capping is activated on a custom action endpoint.</li>
</ul>
<p>These alerts can be subscribed to at the organization level or for specific journeys.</p>
<p>For more information, refer to the <a href="../reports/alerts.md#journey-alerts">detailed documentation</a>.</p>
<p>Availability date: November 5, 2025</p>
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
<p>You can now quickly apply <strong>pre-approved themes</strong> to ensure brand consistency across all emails, speed up your campaign creation process, and independently produce high-quality emails while reducing dependency on design teams.</p>
<p>Previously released in beta version, this capability is now available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<img src="assets/do-not-localize/themes.gif">
<p>For more information, refer to the <a href="../email/apply-email-themes.md">detailed documentation</a>.</p>
<p><a href="https://jira.corp.adobe.com/browse/NEO-88838">Link to PRODUCT JIRA task</a></p>
<p>Availability date: November 5, 2025</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#jan-26-01-improv}

Improvements coming with this release are listed below.

#### AI

* **AI Assistant Content Quality Checks** - In addition to brand alignment, you can now evaluate overall <strong>content quality</strong> to uncover potential issues with readability, cohesiveness, and effectiveness, independent of your brand guidelines. These automated checks help identify unclear messaging, inconsistent tone, or structural gaps.
  <a href="https://jira.corp.adobe.com/browse/CJM-103238">Link to PRODUCT JIRA task</a>
* **Update brands with new color tab** - Brand guidelines help ensure your brand is presented consistently across all touchpoints. The new <strong>Colors section</strong> defines the standards for your brand's color system, outlining how colors are selected, organized, and applied across experiences. It ensures consistent use of primary, secondary, accent, and neutral colors to support a cohesive, accessible, and recognizable brand identity.
  <a href="https://jira.corp.adobe.com/browse/CJM-121183">Link to PRODUCT JIRA task</a>

#### Campaigns

* **Schedule Campaign using Profile Time Zone** - Campaign scheduling can now use each profile's <strong>time zone</strong> to deliver messages at the intended local time.

  **Note**: This improvement is only available for a set of organizations (Limited Availability).
  <a href="https://jira.corp.adobe.com/browse/CJM-43782">Link to PRODUCT JIRA task</a>

#### Channels

* **SMS Webhooks: Phase II** - Description to be provided.
  <a href="https://jira.corp.adobe.com/browse/CJM-93914">Link to PRODUCT JIRA task</a>

#### Email Designer

* **In-place corrections in the Email designer** - <strong>AI-powered automatic content suggestions</strong> are now available in the Email Designer when violations are detected during content validation. If content is flagged as misaligned with brand guidelines or fails quality criteria, the system proactively generates corrected alternatives that can be reviewed and applied inline, improving compliance and accelerating production.
  <a href="https://jira.corp.adobe.com/browse/CJM-95365">Link to PRODUCT JIRA task</a>

#### Experience Decisioning

* **Self-service migration tooling APIs** - A new set of <strong>migration tooling APIs</strong> is available to migrate Offer management entities to Experience Decisioning. The tooling enables seamless migration between sandboxes with dependency resolution and rollback capabilities.
  <a href="https://jira.corp.adobe.com/browse/CJM-109695">Link to PRODUCT JIRA task</a>

* **Attach fragments to decision items** - Journey Optimizer now provides the ability to attach <strong>fragments</strong> to decision items which can be leveraged in code-based experience campaigns through decision policies.

  **Note**: Previously released in Limited Availability, this improvement is now available to all environments (General Availability).
  <a href="https://jira.corp.adobe.com/browse/CJM-110282">Link to PRODUCT JIRA task</a>

#### Journeys

* **Leverage a failure response payload in journey Custom Actions** - You can now define an optional <strong>error response payload</strong> for custom actions. When a call fails, the error payload is exposed in the journey context and is available in the timeout/error branch to support richer fallback logic and debugging.
  <a href="https://jira.corp.adobe.com/browse/CJM-113125">Link to PRODUCT JIRA task</a>

* **Combine native and Adobe Campaign message actions** - Journey Optimizer now lets you combine Adobe Campaign v7/v8 message actions with native channel actions in the same journey.
  <a href="https://jira.corp.adobe.com/browse/CJM-113103">Link to PRODUCT JIRA task</a>

* **Journey payload size validation in journeys** - Journey Optimizer now provides <strong>payload size validation</strong> to help ensure optimal performance and system stability. When building or publishing journeys, you receive clear warnings and errors if payload sizes approach or exceed recommended limits, along with actionable guidance to optimize your journey configuration. This proactive validation helps you identify potential issues early and maintain journey performance.
  <a href="https://jira.corp.adobe.com/browse/CJM-122236">Link to PRODUCT JIRA task</a>

* **Multiple inbound actions in journeys** - To simplify your journey orchestration, you can now define <strong>multiple inbound actions</strong> in a single journey. Previously available in campaigns, this capability enables you to deliver multiple code-based experiences, In-app messages, Content Cards or web actions to different locations at the same time, each action containing a specific content.

  **Note**: Previously released in Limited Availability, this improvement is now available to all environments (General Availability).
  <a href="https://jira.corp.adobe.com/browse/CJM-111916">Link to PRODUCT JIRA task</a>

#### Orchestrated campaigns

* **Select attributes and copy distribution values** - You can now select or copy values directly from the distribution of values view in orchestrated campaigns.
  <a href="https://jira.corp.adobe.com/browse/CJM-105244">Link to PRODUCT JIRA task</a>

* **Data usage label inheritance for audiences** - <strong>Data usage labels</strong> applied in Adobe Experience Platform now automatically carry over when saving audiences in orchestrated campaigns, reducing manual DULE tagging.
  <a href="https://jira.corp.adobe.com/browse/CJM-120769">Link to PRODUCT JIRA task</a>

* **Predefined retargeting filters** - To support easier retargeting for orchestrated campaign use cases, this release introduces new <strong>retargeting filters</strong>. These filters let you directly target audiences based on message engagement, such as sent, opened only, opened or clicked, or opened and clicked, and select the specific campaign or in-transition campaign you want to retarget.
  <a href="https://jira.corp.adobe.com/browse/CJM-116701">Link to PRODUCT JIRA task</a>

* **Predefined filters with parameters** - You can now create <strong>filters with parameters</strong> in orchestrated campaigns for reusable, editable rules.
  <a href="https://jira.corp.adobe.com/browse/CJM-115431">Link to PRODUCT JIRA task</a>

* **Message confirmation before send** - A <strong>confirmation step</strong> is now enabled by default before sending orchestrated campaigns to reduce accidental sends.
  <a href="https://jira.corp.adobe.com/browse/CJM-87219">Link to PRODUCT JIRA task</a>

* **User-generated metadata support** - The <strong>executionMetadata helper function</strong> is now available in the personalization editor for Orchestrated Campaigns, enabling you to attach contextual information to any native action and store it in a dataset for export to external systems.
  <a href="https://jira.corp.adobe.com/browse/CJM-112697">Link to PRODUCT JIRA task</a>

* **Restart button** - Orchestrated campaigns now include a <strong>restart button</strong> so you can quickly re-launch runs when needed before publishing the campaign.
  <a href="https://jira.corp.adobe.com/browse/CJM-106020">Link to PRODUCT JIRA task</a>

* **Rate control support** - Orchestrated campaigns now support <strong>rate control</strong> to help you pace deliveries and align with volume constraints.
  <a href="https://jira.corp.adobe.com/browse/CJM-113254">Link to PRODUCT JIRA task</a>

#### Permissions

* **Prevent self-approval for journeys and campaigns** - You can now require that creators cannot approve their own journeys or campaigns, improving <strong>separation of duties</strong> in approval workflows.
  <a href="https://jira.corp.adobe.com/browse/CJM-99957">Link to PRODUCT JIRA task</a> | <a href="https://jira.corp.adobe.com/browse/CJM-95676">Link to PRODUCT JIRA task</a>

## Coming soon {#jan-26-01-coming-soon}

In the next few days, the following capabilities and enhancements are scheduled for release. **Information is subject to change**. Updated links, screens, and documentation will be shared once these updates are live in production.

<table>
<thead>
<tr>
<th><strong>Content generation within Journey Agent</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Powered by Adobe Experience Platform Agent Orchestrator, <strong>Journey Agent</strong> is available in Journey Optimizer and enables you to analyze journeys through a natural language interface. You can now also generate and manage channel-specific content directly in Journey Agent, creating content for channels such as email and push, applying and previewing templates, refining tone and style through prompts, and opening content in Content Designer for in-context editing.</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-111882">Link to PRODUCT JIRA task</a></p>
<p>Availability date: February 2, 2026</p>
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
<p>You can now include <strong>personalized offers</strong> in your journeys through a dedicated Content decision activity in the journey canvas, and use them in journey activities, including conditions and custom actions.</p>
<p><a href="https://jira.corp.adobe.com/browse/CJM-99223">Link to PRODUCT JIRA task</a></p>
<p>Availability date: February 3, 2026</p>
</td>
</tr>
</tbody>
</table>
-->
