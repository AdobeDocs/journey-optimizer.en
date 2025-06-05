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

## June '25 updates {#25-6-rn}

<table>
<thead>
<tr>
<th><strong>Scale your Experimentation winner</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Scale your Experimentation winner enables you to automatically or manually roll out the winning variation of an experiment to your full audience. This feature ensures that, once a top performer is identified, you can maximize its reach and effectiveness without constant manual oversight.</p>
<p>For more information, refer to the <a href="../content-management/content-experiment.md">detailed documentation</a>.</p>
<p>Availability date: June 2nd, 2025</p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Conflict & prioritization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>In Journey Optimizer, managing the volume and timing of campaigns and journeys is essential to avoid overwhelming customers with too many interactions. Journey Optimizer now offers several tools for conflict management and prioritization - previously available only to limited-access (LA) organizations - that are now generally available (GA).</p>
<p>Previously released in Limited Availability, this capability is now available to all environments. With this General Availability release, the following enhancements have been introduced:</p>
<ul>
<li>Expanded Support: Conflict management tools now support both Unitary Journeys and Audience Qualification Journeys, in addition to Read audience journeys.</li>
<li>Improved Troubleshooting: Two new step event fields are now available in the Query Service, enabling you to analyze why a profile was rejected from a journey or campaign.</li>
<li>Enhanced Reporting: Reports now indicate which specific rule excluded a profile from a journey or campaign, providing greater transparency and actionable insights.</li></ul>
<img src="assets/do-not-localize/gif-conflict.gif">
<p>For more information, refer to the <a href="../conflict-prioritization/gs-conflict-prioritization.md">detailed documentation</a>.</p>
<p>Availability date: June 3rd, 2025</p>
</td>
</tr>
</tbody>
</table>

### Improvements

* **Decisioning** - Availability date: June 3rd, 2025

  Decisioning objects can now be copied between sandboxes, streamlining testing and deployment workflows. [Read more](../configuration/copy-objects-to-sandbox.md#decisioning)

* **Decision item attribute support for decisioning rules** - Availability date: June 4th, 2025
  
  You can now leverage decision item attributes to create decisioning rules. [Read more](../experience-decisioning/rules.md#create)

## May '25 release notes {#25-5-rn}

<!--**Release date**: May 20-21, 2025-->

### New capabilities {#25-05-features}

New capabilities coming with this release are detailed below.

<table>
<thead>
<tr>
<th><strong>Calendar View for Campaign and Journey inventory</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A calendar view is now available in the journeys and campaigns lists. It allows you to visualize all journeys and campaigns activations in the respective lists.</p>
<p>This change is currently only available for a set of organizations (Limited Availability). To request access, use <a href="https://forms.cloud.microsoft/r/FC49afuJVi" target="_blank">this form</a>.</p>
<img src="assets/do-not-localize/calendar.gif">
<p>For more information, refer to these sections: <a href="../building-journeys/journey-ui.md">Browse & filter your journeys</a>, <a href="../campaigns/modify-stop-campaign.md">Access campaigns</a>.</p>
<p>Availability date: May 28, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Adobe Experience Manager Content fragment integration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With the integration of Adobe Experience Manager and Adobe Journey Optimizer, you can now effortlessly use Adobe Experience Manager Content Fragments within your Journey Optimizer content. This seamless connection makes it easier to access and use your AEM content directly in Journey Optimizer.</p>
<p>Previously available for a limited set of organizations (LA), this capability is now GA with the following enhancement: you can now define placeholders and map personalization values within the fragment signature using the Editor mode.</p>
<ul>
<!--li>Create offers by directly selecting an AEM Content Fragment.</li>
<li>Define placeholders and map personalization values within the fragment signature using the Editor mode.</li-->
</ul>
</br>
<img src="assets/do-not-localize/content-fragment.gif">
<p>For more information, refer to the <a href="../integrations/aem-fragments.md">detailed documentation</a>.</p>
<p>Availability date: May 23, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Adobe Experience Manager Dynamic media integration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Dynamic media assets are now directly available and accessible in Journey Optimizer. This integration enables you to:</p>
<ul>
<li>Centrally manage assets with real-time updates.</li>
<li>Modify your assets settings such as width and height instantly.</li>
<li>Customize Dynamic Media templates by updating your content and adding personalization fields.</li>
</ul>
</br>
<img src="assets/do-not-localize/dynamic_media_template_html.gif">
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>For more information, refer to the <a href="../integrations/aem-dynamic.md">detailed documentation</a>.</p>
<p>Availability date: May 23, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Supplemental ID for event-triggered journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now trigger journeys using a profile ID along with another identifier, such as an order ID, subscription ID, or prescription ID, allowing the same profile to be in the same journey multiple times at once. This enables scenarios like managing multiple orders or subscriptions in parallel, with each instance following its own path through the journey.</p>
<p>For more information, refer to the <a href="../building-journeys/supplemental-identifier.md">detailed documentation</a>.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>Availability date: May 23, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Simulate content variations</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<!--p>Previously available in beta, content variations simulation is now generally available (GA). It allows you to preview different variations of your content using sample input data uploaded from a CSV or JSON file or added manually. All the attributes used in your content for personalization are automatically detected by the system and can be used for your tests to create multiple variants.</p-->
<p>Previously released in Limited Availability, this capability is now available to all environments. With this General Availability release, the feature now includes support for multilingual content and content experiments, enabling you to test variations across different languages and treatments. Additionally, it now supports contextual attributes (in addition to profile attributes), allowing for even more dynamic and situational content testing.</p>
<img src="assets/do-not-localize/variants.gif">
<p>For more information, refer to the <a href="../test-approve/simulate-sample-input.md">detailed documentation</a>.</p>
<p>Availability date: May 23, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Synchronize read audience schedule with batch segmentation job</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now trigger daily journey runs after batch segmentation completion. This option is now available in daily-scheduled journeys to all customers. It allows you to define for a time window of up to 6 hours to wait for audience data from batch segmentation jobs, ensuring journeys run with the most up-to-date data or are skipped if not ready.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<img src="assets/do-not-localize/trigger-journeys.gif">
<p>For more information, refer to the <a href="../building-journeys/read-audience.md#schedule">detailed documentation</a>.</p>
<p>Availability date: May 20, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Custom SMS provider</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows you to configure additional SMS providers beyond the default options: Sinch, Infobip, and Twilio. With custom SMS provider configuration, you can integrate third-party providers directly, leverage advanced payload customization for dynamic messaging, and manage consent preferences (opt-in/opt-out) to ensure compliance.</p>
<p>For more information, refer to the <a href="../sms/sms-configuration-custom.md">detailed documentation</a>.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
<p>Availability date: May 20, 2025</p>
</td>
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
<p>This capability is currently in beta version and only available to beta customers. To join the beta program, contact your Adobe representative.</p>
<img src="assets/do-not-localize/themes.gif">
<p>For more information, refer to the <a href="../email/apply-email-themes.md">detailed documentation</a>.</p>
<p>Availability date: May 14, 2025</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Decisioning - New AI formula builder</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create specific Decisioning ranking formulas by defining and combining criteria from a new improved interface. Instead of relying only on a static offer priority, you can define custom ranking formulas that combine AI model scores, offer priorities, profile attributes, offer attributes, and contextual signals through a guided interface.</p>
<img src="assets/do-not-localize/formula-builder.gif">
<p>For more information, refer to the <a href="../experience-decisioning/exd-ranking-formulas.md">detailed documentation</a>.</p>
<p>Availability date: May 14, 2025</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#25-05-improv}

Improvements coming with this release are listed below.


* **New campaign objects support for sandbox copy** - Availability date: May 15, 2025

  When copying campaigns across multiple sandboxes using the package export and import capabilities, the following dependencies are now also copied: channel configurations, experiment variants and settings, decision policies and items. [Read more](../configuration/copy-objects-to-sandbox.md)
  
* **Folders for landing pages**  - Availability date: May 9, 2025

  To easily manage your landing pages, you can now use folders to organize them more effectively into a structured hierarchy. [Read more](../landing-pages/manage-lp.md)

* **Direct Mail: SSH Key support for SFTP connections** - Availability date: May 5, 2025

  In the Direct Mail file routing configuration, in addition to the existing SFTP with password authentication type, you can now export your direct mail file to an SFTP server with SSH key authentication. [Read more](../direct-mail/direct-mail-configuration.md)

* **Pills activation for personalization** - Availability date: May 5, 2025

  A new "Pills" button has been added to the personalization editor. When enabled, profile and contextual attributes display as pills, enhancing the readability of your code. [Read more](../personalization/personalization-build-expressions.md#options)

  >[!AVAILABILITY]
  >
  >This capabilitity will be gradually rolled out to all environments over the next 30 days.

* **'Redirect to URL' support in Web channel** - Availability date: May 20, 2025

  The Journey Optimizer Web channel now enables you to redirect visitors to another existing URL rather than authoring a new variation in the visual editor. This capability can be used to run experiments comparing two completely different pages instead of just changing a few elements within a page. [Read more](../web/create-web.md#web-redirect-to-url)

* **Folders for templates and fragments** - Availability date: May 20, 2025

  Folders let you organize your objects more easily and effectively into a structured hierarchy. Previously available for a set of organizations (LA), folders are now available to all users (GA) to manage their content templates and fragments. Read more in the [Content templates](../content-management/access-content-templates.md#folders) and [Fragments](../content-management/manage-fragments.md#folders) sections. 

* **Click tracking in email templates** - Availability date: May 20, 2025

  Click tracking on `<area>` elements within image maps in email content is now natively supported in [!DNL Journey Optimizer]. This is to ensure that image map areas receive the same tracking wrapping, tracking data, and appended parameters as standard hyperlinks. [Learn more on message tracking](../email/message-tracking.md#manage-tracking)

<!--
* **Decisioning - Leverage Adobe Experience Platform datasets** 
  
  Journey Optimizer now allows you to leverage Adobe Experience Platform datasets in the following Decisioning objects: eligibility rules, ranking formulas, and capping rules.-->

* **Right rail in campaigns list** - Availability date: May 20, 2025

  In the campaign list, selecting a campaign now opens a pane displaying its details.

<!--* **Form fields in code-based experience content**

  In content templates, you can now define specific JSON or HTML fields which enable non-technical users to easily edit content in code-based experiences without the need to manipulate code.-->

<!--* **Subdomains - 'Custom delegation' method**  
  In addition to the full delegation and the CNAME method, a new subdomain configuration method is now available: the Custom delegation method, which enables you to fully own controlling and maintaining all aspects of DNS that are required for delivering, rendering, and tracking messages.
  -->

