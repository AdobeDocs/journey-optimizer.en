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


## May '25 early release notes {#25-5-rn}


**Early release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published at the release date.

**Release date**: May 20-21, 2025


### New capabilities {#25-04-features}

New capabilities coming with this release are detailed below.

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
<img src="assets/do-not-localize/themes.gif">
<p>This capability is currently in beta version and only available to beta customers. To join the beta program, contact your Adobe representative.</p>
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
<p>Previously available for a limited set of organizations (LA), this capability is now GA with the following enhancements:</p>
<ul>
<li>Create offers by directly selecting an AEM Content Fragment.</li>
<li>Define placeholders and map personalization values within the fragment signature using the Editor mode.</li>
</ul>
</td>
</tr>
</tbody>
</table>

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
<p>This change is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
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
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p>
</td>
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
<li>Enhanced Reporting: Reports now indicate which specific rule excluded a profile from a journey or campaign, providing greater transparency and actionable insights.</li>
</ul>
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
<p>Previously available in beta, content variations simulation is now generally available (GA). It allows you to preview different variations of your content using sample input data uploaded from a CSV or JSON file or added manually. All the attributes used in your content for personalization are automatically detected by the system and can be used for your tests to create multiple variants.</p>
<p>Previously released in Limited Availability, this capability is now available to all environments. With this General Availability release, the feature now includes support for multilingual content and content experiments, enabling you to test variations across different languages and treatments. Additionally, it now supports contextual attributes (in addition to profile attributes), allowing for even more dynamic and situational content testing.</p>
<img src="assets/do-not-localize/variants.gif">
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Scale your Experimentation winner</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Scale the Winner enables you to automatically or manually roll out the winning variation of an experiment to your full audience. This feature ensures that, once a top performer is identified, you can maximize its reach and effectiveness without constant manual oversight.</p>
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
<p>Previously released in Limited Availability, this capability is now available to all environments (General Availability).</p></td>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Supplemental ID for event triggered journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now trigger journeys using a profile ID along with another identifier, such as an order ID, subscription ID, or prescription ID, allowing the same profile to be in the same journey multiple times at once. This enables scenarios like managing multiple orders or subscriptions in parallel, with each instance following its own path through the journey.</p>
<p>This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>



### Improvements {#25-05-improv}

Improvements coming with this release are listed below.


* **New objets support for sandbox copy**

  * **Campaigns** - Availability date: May 15, 2025

    When copying campaigns across multiple sandboxes using the package export and import capabilities, the following dependencies are now also copied: channel configurations, experiment variants and settings, decision policies and items. [Read more](../configuration/copy-objects-to-sandbox.md)

  * **Decisioning** - Availability date: May 16, 2025

    Decisioning objects can now be copied between sandboxes, streamlining testing and deployment workflows. [Read more](../configuration/copy-objects-to-sandbox.md#decisioning)
  
* **Folders for landing pages**  - Availability date: May 9, 2025
  To easily manage your landing pages, you can now use folders to organize them more effectively into a structured hierarchy. [Read more](../landing-pages/manage-lp.md)

* **Direct Mail: SSH Key support for SFTP connections** - Availability date: May 5, 2025

  In the Direct Mail file routing configuration, in addition to the existing SFTP with password authentication type, you can now export your direct mail file to an SFTP server with SSH key authentication.

* **Pills activation for personalization** - Availability date: May 5, 2025

  A new "Pills" button has been added to the personalization editor. When enabled, profile and contextual attributes display as pills, enhancing the readability of your code. [Read more](../personalization/personalization-build-expressions.md#options)

  >[!AVAILABILITY]
  >
  >This capabilitity will be gradually rolled out to all environments over the next 30 days.

* **Click tracking in email templates**  
  Click tracking on `<area>` elements within image maps in email templates is now natively supported in Journey Optimizer. This is to ensure that image map areas receive the same tracking wrapping, tracking data, and appended parameters as standard hyperlinks.

* **Decisioning - Leverage Adobe Experience Platform datasets**  
  Journey Optimizer now allows you to leverage Adobe Experience Platform datasets in the following Decisioning objects: eligibility rules, ranking formulas, and capping rules.

* **Folders for templates and fragments**  
  Folders let you organize your content templates and fragments more easily and effectively into a structured hierarchy. Previously available for a set of organizations (LA), folders are now available to all users (GA) to manage their content templates and fragments. 


* **'Redirect to URL' support in Web channel**  
  The Journey Optimizer Web channel now enables you to redirect visitors to another existing URL rather than authoring a new variation in the visual editor. This capability can be used to run experiments comparing two completely different pages instead of just changing a few elements within a page.

* **Right rail in campaigns list**  
  In the campaign list, selecting a campaign now opens a pane displaying its details.

* **Form fields in code-based experience content**  
  In content templates, you can now define specific JSON or HTML fields which enable non-technical users to easily edit content in code-based experiences without the need to manipulate code.

* **Decision item attribute support for decisioning rules**  
  You can now leverage decision item attributes to create decisioning rules.

<!--
* **Subdomains - 'Custom delegation' method**  
  In addition to the full delegation and the CNAME method, a new subdomain configuration method is now available: the Custom delegation method, which enables you to fully own controlling and maintaining all aspects of DNS that are required for delivering, rendering, and tracking messages.-->


## April '25 release notes {#25-4-rn}

**Release date**: April 29-30, 2025

### New capabilities {#25-04-features}

New capabilities coming with this release are listed below.

<table>
<thead>
<tr>
<th><strong>Personalization Editor - Learn by Doing</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A personalization playground is now available, where you can experiment with personalization expressions. It allows you to explore sample templates and payloads to help you get started and try out your own personalization expressions.</p>
<p>For more information, refer to the <a href="../personalization/personalize.md#playground">detailed documentation</a>.</p>
<p>Availability date: April 24, 2025</p>
<img src="assets/do-not-localize/templating-playground.gif"/>
</td>
</tr>
</tbody>
</table>

<!--table>
<thead>
<tr>
<th><strong>Adobe Experience Manager as a Cloud Service integration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The integration between Adobe Journey Optimizer and Adobe Experience Manager as a Cloud Service is now released in General Availability (GA). This integration enables seamless content sourcing and management for personalized customer journeys.</p>
<p>For more information, refer to the <a href="../integrations/aem-templates.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table-->

<!--<table>
<thead>
<tr>
<th><strong>Simulate content variations (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Previously available in beta, content variations simulation is now generally available (GA). It allows you to preview different variations of your content using sample input data uploaded from a CSV or JSON file or added manually. All the attributes used in your content for personalization are automatically detected by the system and can be used for your tests to create multiple variants.</p>
<p>With the General Availability release, the feature now includes support for multilingual content and content experiments, enabling you to test variations across different languages and treatments. Additionally, it now supports contextual attributes (in addition to profile attributes), allowing for even more dynamic and situational content testing.</p>
<img src="assets/do-not-localize/variants.gif">
</td>
</tr>
</tbody>
</table>-->

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
<p>The LINE channel is enabled for Adobe Journey Optimizer customers upon request. Contact Adobe Customer Care or your Adobe representative to activate the feature for your organization.</p>
<p>For more information, refer to the <a href="../line/get-started-line.md">detailed documentation</a>.</p></td>
</tr>
</tbody>
</table>


<!--table>
<thead>
<tr>
<th><strong>Custom SMS provider (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports custom SMS providers, allowing you to integrate your preferred SMS services for enhanced communication flexibility.</p>
<p>For more information, refer to the <a href="../sms/sms-configuration-custom.md">detailed documentation</a>.</p></td>
</tr>
</tbody>
</table-->


<table>
<thead>
<tr>
<th><strong>Journey metrics</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey metrics are now available, allowing you to measure the impact of your activities across the key metrics of your business and to provide clearer insights into your performance.</p>
</br>
<img src="assets/do-not-localize/success-metric.gif"/>
<p>For more information, refer to the <a href="../building-journeys/success-metrics.md">detailed documentation</a>.</p>
<p>Availability date: April 9, 2025</p>
</td>
</tr>
</tbody>
</table>



<!--<table>
<thead>
<tr>
<th><strong>Calendar view for campaign and journey inventory (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>A new calendar view is now available for campaigns and journey activations. This feature provides a visual representation of scheduled activities, allowing you to view and manage your campaigns and journeys more effectively. Selecting a calendar item opens a right rail with detailed information. This feature is currently in Limited Availability.</p>
<img src="assets/do-not-localize/calendar.gif">
</td>
</tr>
</tbody>
</table>-->

<table>
<thead>
<tr>
<th><strong>Adobe Express integration (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now integrates with Adobe Express, enabling you to seamlessly connect your creative assets with journey orchestration. This integration simplifies the process of designing and deploying personalized content across campaigns. </p>
<p>This integration is currently unavailable for use with Healthcare Shield or Privacy and Security Shield.</p>
<img src="assets/do-not-localize/express_resize.gif">
<p>For more information, refer to the <a href="../integrations/express.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Trigger daily journey runs after batch segmentation completion (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>For daily-scheduled journeys, a new option allows you to define a time window of up to 6 hours to wait for audience data from batch segmentation jobs, ensuring journeys run with the most up-to-date data or are skipped if not ready. The Trigger after batch audience evaluation option is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../building-journeys/read-audience.md#schedule">detailed documentation</a>.</p>
<img src="assets/do-not-localize/trigger-journeys.gif">
</td>
</tr>
</tbody>
</table>

<!--table>
<thead>
<tr>
<th><strong>Themes in the Email Designer (Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now quickly apply pre-approved styling themes to your email content to ensure brand consistency across all emails, speed up your campaign creation process and independently produce hight-quality emails while reducing dependency on design teams.</p>
<p>This capability is currently in beta version and only available to beta customers. To join the beta program, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../content-management/brands-score.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/themes.gif">
<p>Availability date: May 5, 2025</p>
</td>
</tr>
</tbody>
</table-->

<table>
<thead>
<tr>
<th><strong>Brand alignment score (Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The Brand alignment score feature offers clear feedback directly in the email designer, helping you see whether your content aligns with your brand's tone, style, and guidelines. This feature is available in Beta.</p>
<p>For more information, refer to the <a href="../content-management/brands-score.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/brand-score.gif">
</td>
</tr>
</tbody>
</table>

<!--
<table>
<thead>
<tr>
<th><strong>Decisioning - New AI formula builder</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create specific Decisioning ranking formulas by defining and combining criteria from a new improved interface. Ranking formulas allow you to define rules that will determine which decision items should be presented first, rather than taking into account the priority scores.</p>
<p>For more information, refer to the <a href="../content-management/brands-score.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/formula-builder.gif">
<p>Availability date: May 5, 2025</p>
</td>
</tr>
</tbody>
</table>
-->

### Improvements {#25-04-improv}

**Campaigns preview API**

  New APIs are available to preview campaigns, in addition to existing proof-sending capabilities. [Read more](https://developer.adobe.com/journey-optimizer-apis/references/simulations/#operation/createCampaignPreview){target="_blank"}.

**Sandbox Tooling**

* **Sandbox tooling for custom actions**  

  Custom actions are now included in the list of Adobe Journey Optimizer objects that can be copied using the sandbox tooling feature, streamlining testing and deployment. [Read more](../configuration/copy-objects-to-sandbox.md)

* **Sandbox tooling for campaigns** - Availability date: April 3, 2025

    You can now copy campaigns across multiple sandboxes by using package export and import capabilities. Campaigns are copied along with all items related to the profile, audience, schema, inline messages, and dependent objects. Some items are not copied, such as decision items, data usage labels, and language settings. [Read more](../configuration/copy-objects-to-sandbox.md#custom-actions)

**Personalization**

* **New contextual attribute**  

  A new contextual attribute, **Message Profile Id**, is now available to select from the personalization editor. This is a message-oriented attribute identifying uniquely each message sent to each targeted profile in a delivery. This unique identifier can be used for example as a URL tracking parameter to distinguish each link opened or clicked by recipients.

* **Populated attributes in attributes pane** - Availability date: April 2, 2025

    The attributes pane in the personalization editor now shows only populated attributes by default. To view all attributes, use the settings button to toggle off the **[!UICONTROL Show only populated attributes]** option. [Read more](../personalization/personalization-build-expressions.md)

**Email channel**

* **Personalized URL tracking** - Availability date: April 30, 2025

  For increased flexibility and control over your email settings, you can now personalize all your URL tracking parameters at once at the email channel configuration level, instead of doing it in the Email designer for each link in your content. [Read more](../email/surface-personalization.md#personalize-url-tracking)

* **Email Designer** - Availability date: April 1, 2025

    To enhance accessibility in Journey Optimizer, two new fields are now available in the Email Designer: they correspond to the `<title>` element and `lang` attribute in the `<html>` element of your email content. You can define these settings in addition to the **[!UICONTROL Preheader]** field, in the email **[!UICONTROL Body]** section. [Read more](../email/email-metadata.md)

**Use case playbooks**

* **Playbooks authoring and sharing (Private beta)** - You can now create, manage, and share your own use case playbooks. This capability is currently only available for a set of organizations as a private beta. To gain access, contact your Adobe representative. [Read more](../start/playbooks.md)

**Navigation**

* **Content management** - Availability date: April 2, 2025

    To easily manage your content templates and fragments, you can now use folders to organize them more effectively into a structured hierarchy. Learn more in the [Content templates](../content-management/access-content-templates.md#folders) and [Fragments](../content-management/manage-fragments.md#folders) sections.

    >[!AVAILABILITY]
    >
    >This improvement is only available for a set of organizations (Limited Availability).

<!--- **Folders for content templates and fragments** - Availability date: May 5, 2025

  Previously available for a set of organizations (LA), folders are now available to all users (GA) to manage their content templates and fragments. Folders let you organize your content templates and fragments more easily and effectively into a structured hierarchy.



<!--- **Right rail in campaigns list**  

  A right rail has been added to the campaigns list, providing detailed information when a campaign is selected.-->

<!--**Playbooks**

- **Create your own playbooks (Beta)**
  
  You can now create your own playbooks in Adobe Journey Optimizer, enabling greater customization and flexibility in journey planning.-->




