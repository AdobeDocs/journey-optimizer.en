---
solution: Journey Optimizer
product: journey optimizer
title: Release notes
feature: Release Notes
topic: Content Management
description: Journey Optimizer Release notes
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

## May Updates {#may-updates}

**Availability date**: May 7, 2024

<table>
<thead>
<tr>
<th><strong>Experience Decisioning - Limited Availability</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Experience Decisioning simplifies personalization by offering a centralized catalog of marketing offers known as 'decision items' and a sophisticated decision engine. This engine leverages rules and ranking criteria to select and present the most relevant decision items to each individual.</p>
<p>These decision items are seamlessly integrated into a wide range of inbound surfaces through the new code-based experience channel, now accessible within Journey Optimizer campaigns. Experience Decisioning decision policies are available for use in code-based experience campaigns only.</p>
<p>Experience Decisioning is currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<img src="assets/do-not-localize/gif-exd.gif"/>
<p>For more information, refer to the <a href="../experience-decisioning/gs-experience-decisioning.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

From beta to LA, the following improvements have been added:

* **Experience Decisioning + Code-based experiences (LA)**: You can now leverage the Experience decisioning feature to use decision items in your code-based campaigns. Note: The Code-based experience channel and Experience decisioning are not available for organizations that have purchased the Adobe Healthcare Shield and Privacy and Security Shield add-on offerings. [Read more](../code-based/get-started-code-based.md)
* You can now leverage context data from Adobe Experience Platform in your decision rules and rankign formulas. [Read more](../experience-decisioning/context-data.md)
* A new "Manage Experience decisions" permission is now available for the Decision Management resource. It allows you to manage rights related to Experience Decisioning. [Read more](../experience-decisioning/gs-experience-decisioning.md)
* You can now add multiple capping rules for a given decision item in Experience Decisioning. This allows you to increase the level of control over the way offers are sent. [Read more](../experience-decisioning/items.md#capping)
* You can now create custom reporting dashboards of Experience Decisioning campaigns using [!DNL Customer Journey Analytics]. [Read more](../experience-decisioning/cja-reporting.md)

## April 2024 release notes {#apr-2024}

**Release date**: May 2, 2024

### New capabilities {#apr-features}

<!--table>
<thead>
<tr>
<th><strong>Business rules - Private Beta</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>It is now possible to create and apply rule sets to your marketing communications.  </p>
</td>
</tr>
</tbody>
</table-->

<!--table>
<thead>
<tr>
<th><strong>Personalization - Local Lookups - Multi-Entity Support - Beta</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>TBD</p>
</td>
</tr>
</tbody>
</table-->

This release brings the new capabilities detailed below.

<table>
<thead>
<tr>
<th><strong>Multimedia Message Service (MMS) - all providers</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With the SMS Channel, you can now enhance your communication by sending Multimedia Message Service (MMS) messages, enabling the sharing of images, GIFs, or videos with your customers. Initialy only available with Sinch, MMS is now also available with Infobip and Twilio.</p>
<img src="assets/do-not-localize/mms.gif"/>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Improved Journey Designer and live reporting</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>This release comes with an improved canvas user interface for journeys, and provides a more intuitive and efficient user experience. Activities are clearer and present more information on the journey canvas with fewer clicks.</p>
<img src="assets/new-canvas3.gif"/>
<p>Alongside the improved journey canvas design, we're introducing the ability to see last 24 hours reporting metrics directly in the journey canvas. </p>
<img src="assets/new-canvas6bis.png"/>
<p><strong>Note</strong>: These changes will be gradually rolled out to all environments starting April release.</p>
<p>For more information, refer to the <a href="new-canvas.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<!-- table>
<thead>
<tr>
<th><strong>AI Assistant - Experience Variant Generation - Beta</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Once you have created and personalized your message, take your content to the next level with the AI assistant. You can now use the AI assistant to optimize your message's impact by experimenting with different main titles, and images. Each variant is managed as a unique Treatment, to measure and compare which title effectively generates more clicks.</p>
</td>
</tr>
</tbody>
</table-->

<!--table>
<thead>
<tr>
<th><strong>IP Warmup Workflow - LA</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now easily perform IP warmup workflows directly from the Journey Optimizer interface in a standardized and efficient way that follows the best practices for optimal deliverability.</p>
</td>
</tr>
</tbody>
</table-->

<!--table>
<thead>
<tr>
<th><strong>Email Surface Personalization - Private beta </strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now define dynamic subdomains and personalized header parameters when creating email channel surfaces, for increased flexibility and control over your email settings.</p>
</td>
</tr>
</tbody>
</table-->

### Improvements {#apr-improvements}

This release comes with the improvements listed below.

<!--
* **Expression Fragments supported for Web and In-App**: Expression fragments are now available for the Web and In-app channels. 
-->


<!--
* **DULE for AJO Channel Surface**: It is now possible to apply a label on certain profile attributes to restrict their usage inside a channel surface through marketing actions.
-->


<!--
* **List-Unsubscribe updates**: Following on the recent Gmail and Yahoo announcements for bulk senders, Journey Optimizer supports the "post/1-click" List-Unsubscribe option. 
-->

**Configuration**

* You can now select a marketing action at the channel surface level. When used in a surface, all consent policies associated with that marketing action are leveraged in order to respect the preferences of your customers. [Read more](../action/consent.md#surface-marketing-actions)
* The use of Object Level Access Control is now available for channel surfaces. [Read more](../configuration/channel-surfaces.md#create-channel-surface)
* While enabling list unsubscribe in a channel surface, you can now define the consent level to align with how you manage consent from all other sources. [Read more](../email/email-settings.md#list-unsubscribe)

**Content management**

* You can now simulate content templates for all channels. [Read more](../content-management/content-templates.md#test-templates)

**Personalization**

* The new **toInt** helper function is available in the Expression Editor. It allows you to convert any of these types (number, double, int, long, float, short, byte, boolean, string) into an integer. [Read more](../personalization/functions/math.md#to-int)
