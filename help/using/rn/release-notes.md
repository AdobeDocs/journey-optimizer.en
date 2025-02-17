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

## February '25 release {#25-02-rn}

**Release date**: February 18-19, 2025


### New capabilities {#25-02-features}

New capabilities coming with this release are detailed below.

<table>
<thead>
<tr>
<th><strong>Create and manage business rules</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create business rules using rule sets. Rule sets are groups of rule that help you limit sent messages within campaigns and journey actions across channels, and to control profiles entries into journeys.<p>
<p><ul><li>Create channel rule sets to restrict the number of messages sent across one or multiple channels. Apply them to campaigns or journey actions to enforce the rules defined in the rule set. Channel rule set allows you to apply capping rules based on communication types. For example, set a rule set to limit "promotional messages" and another for "newsletters". Apply the appropriate rule set in your campaign or journey action depending on type of communication you are sending.</li>
<li> Create journey rule sets to control profile entries into journeys. Limit how often a profile can enter a journey within a given period or the number of journeys a profile can be enrolled in simultaneously. Apply these at the journey level to ensure proper entry management.</li></p>
<p>Previously available for a set of organizations (LA), business rules are now available to all users (GA).</p>
<!--p>For more information, refer to the <a href="../configuration/business-rules.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Generate Landing pages with the AI Assistant</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now craft compelling content for your landing pages, including full-page designs, personalized text, and customized visuals, with the help of the AI assistant.</p>
<img src="assets/do-not-localize/ai-lp.gif">
<!--p>For more information on AI Assistant, refer to the <a href="../email/generative-lp.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Brand guidelines (beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now set your own Brand guidelines to define your brand's visual and verbal identity. Note that Brands feature is released as a private beta to a limited set of customers. It will be progressively available to all customers in future releases.</p>
<!--p>For more information, refer to the <a href="../content-management/brands.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Create and manage business rules</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create business rules using rule sets. Rule sets are groups of rule that help you limit sent messages within campaigns and journey actions across channels, and to control profiles entries into journeys.<p>
<p><ul><li>Create channel rule sets to restrict the number of messages sent across one or multiple channels. Apply them to campaigns or journey actions to enforce the rules defined in the rule set. Channel rule set allows you to apply capping rules based on communication types. For example, set a rule set to limit "promotional messages" and another for "newsletters". Apply the appropriate rule set in your campaign or journey action depending on type of communication you are sending.</li>
<li> Create journey rule sets to control profile entries into journeys. Limit how often a profile can enter a journey within a given period or the number of journeys a profile can be enrolled in simultaneously. Apply these at the journey level to ensure proper entry management.</li></p>
<p>Previously available for a set of organizations (LA), business rules are now available to all users (GA).</p>
<!--p>For more information, refer to the <a href="../configuration/business-rules.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Generate Landing pages with the AI Assistant</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now craft compelling content for your landing pages, including full-page designs, personalized text, and customized visuals, with the help of the AI assistant.</p>
<img src="assets/do-not-localize/ai-lp.gif">
<!--p>For more information on AI Assistant, refer to the <a href="../email/generative-lp.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Brand guidelines (beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now set your own Brand guidelines to define your brand's visual and verbal identity. Note that Brands feature is released as a private beta and will be progressively available to all customers in future releases.</p>
<!--p>For more information, refer to the <a href="../content-management/brands.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>



<table>
<thead>
<tr>
<th><strong>Flexible Audience Evaluation (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Flexible audience evaluation lets you run a segmentation job on demand for selected audiences, ensuring that you always have the most up-to-date audience data before targeting them into Journey Optimizer journeys and campaigns.</p>
<img src="assets/do-not-localize/flexible-audience.gif">
<p>For more information, refer to the <a href="../audience/about-audiences.md#flexible">detailed documentation</a>.</p>
<p> Flexible audience evaluation is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>Availability date: Jan 28, 2025</p>
</tr>
</tbody>
</table>
</table>


### Improvements {#25-02-improvements}

The improvements below come with the February update.

* **Journeys** - You can now test your custom actions by sending API calls from the administration section. This new capability helps you troubleshoot your custom actions before or after using them in a journey.

* **Dataset Time-to-live (TTL)** - Starting this month, a time-to-live (TTL) guardrail will be rolled out to Journey Optimizer system-generated datasets in new sandboxes and new orgs as follows:

    * 90 days for data in the profile store
    * 13 months for data in the data lake

    This change will be rolled out to existing customer sandboxes in a subsequent phase.

    Learn more about this update in [the dedicated FAQ](../data/datasets-ttl.md#frequently-asked-questions).

<!--* **Playbooks** - You can now create and publish your own Use Case Playbooks in Journey Optimizer.-->

* **Direct mail** - A new server type, Data landing zone, is now supported for file routing  in the direct mail channel configuration.   

* **SMS** - You can now manage SMS message delivery from multi-regional endpoints by overriding delivery, feedback, inbound, and callback URLs. To support this, a new field Override URL has been added to API Credentials configuration. This change is available with Sinch provider only. [Read more](../sms/sms-configuration-sinch.md)

* **Personalization** (Availability date: Jan 29, 2025) - New date/time helper functions are available for use in the personalization editor. [Read more](../personalization/functions/dates.md)


<!--
* The personalization editor has been enhanced with new capabilities such as Auto-complete, Search, and filtering options. You can also show or hide deprecated attributes.--> 


* **Email configuration** - If you are managing consent outside of Adobe, you can now set a custom unsubscribe email address and a custom one-click unsubscribe URL as part of your email channel configuration settings. [Read more](../email/list-unsubscribe.md#custom-managed)

    ![](../email/assets/surface-list-unsubscribe-custom.png){width="80%"}

* **Decisioning** (Availability date: Jan 28, 2025) - Decisioning now supports Object data types when editing the item catalog's schema. [Read more](../experience-decisioning/catalogs.md)


## October '24 release {#24-10-rn}

**Release date**: October 29-30, 2024

### New capabilities {#24-10-features}

This release brings the new capabilities detailed below:

<table>
<thead>
<tr>
<th><strong>Email Content Locking</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows you to lock content in email templates, either by locking the entire template or specific structures and component. This allows you to prevent unintentional edits or deletions, giving you greater control over template customization, and improving the efficiency and reliability of your email campaigns.</p>
<p>For more information, refer to the <a href="../content-management/content-locking.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/gif-content-locking.gif">
<p>Available since Oct 24, 2024</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Code-based experiences in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With the Code-based experience channel, Adobe Journey Optimizer allows you to do advanced personalization and testing for any of your inbound properties, enabling seamless delivery of tailored experiences across diverse touchpoints such as web apps, mobile apps, desktop apps, video consoles, TV connected devices, smart TVs, kiosks, ATMs, IoT devices, and more. The Code-based experience channel is now available in the journey canvas.</p>
<p>For more information, refer to the <a href="../code-based/create-code-based.md">detailed documentation</a>.</p>
<img src="../assets/do-not-localize/code-based-journey.gif"/>
<p>Available since Oct 1, 2024</p>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Web experiences in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With the Web channel, Adobe Journey Optimizer allows you to personalize the web experience you deliver to your customers through inbound web journeys. The Web channel is now available in the journey canvas.</p>
<p>For more information, refer to the <a href="../web/create-web.md">detailed documentation</a>.</p>
<img src="../assets/do-not-localize/web-journey.gif"/>
<p>Available since Oct 1, 2024</p>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Customer Journey Analytics templates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You now have the option to enhance your Journey Optimizer reports by leveraging Customer Journey Analytics templates. This new feature allows you to streamline your reporting process with pre-designed templates tailored to your analytics needs.
</p>
<img src="assets/do-not-localize/cja-templates.gif">
<p>For more information, refer to the <a href="../reports/report-cja-manage.md#cja-template">detailed documentation</a>.</p>
<p>Availability date: starting Jan 15, 2025</p>
</tr>
</tbody>
</table>




### Improvements {#25-02-improvements}

The improvements below come with the February update.

* **Journeys** - You can now test your custom actions by sending API calls from the administration section. This new capability helps you troubleshoot your custom actions before of after using them in a journey.

* **Dataset Time-to-live (TTL)** - Starting this month, a time-to-live (TTL) guardrail will be rolled out to Journey Optimizer system-generated datasets in new sandboxes and new orgs as follows:

    * 90 days for data in the profile store
    * 13 months for data in the data lake

    This change will be rolled out to existing customer sandboxes in a subsequent phase.

    Learn more about this update in [this dedicated FAQ](../data/datasets-ttl.md#frequently-asked-questions).

<!--* **Playbooks** - You can now create and publish your own Use Case Playbooks in Journey Optimizer.-->

* **Direct mail** - A new server type, Data landing zone, is now supported for file routing  in the direct mail channel configuration.

**SMS** - You can now manage SMS message delivery from multi-regional endpoints by overriding delivery, feedback, inbound, and callback URLs. To support this, a new field Override URL has been added to API Credentials configuration. This change is available with Sinch provider only. [Read more](../sms/sms-configuration-sinch.md)

**Personalization** 

<!--
* The personalization editor has been enhanced with new capabilities such as Auto-complete, Search, and filtering options. You can also show or hide deprecated attributes.--> 

* Availability date: Jan 29, 2025 - New date/time helper functions are available for use in the personalization editor. [Read more](../personalization/functions/dates.md)

**Email configuration** - Availability date: Feb 12, 2025

* If you are managing consent outside of Adobe, you can now set a custom unsubscribe email address and a custom one-click unsubscribe URL as part of your email channel configuration settings. [Read more](../email/list-unsubscribe.md#custom-managed)

    ![](../email/assets/surface-list-unsubscribe-custom.png){width="80%"}

**Decisioning** - Availability date: Jan 28, 2025

* Decisioning now supports Object data types when editing the item catalog's schema. [Read more](../experience-decisioning/catalogs.md)