---
solution: Journey Optimizer
product: journey optimizer
title: Previous Release notes (2021)
description: Journey Optimizer 2021 Release notes
feature: Release Notes
topic: Content Management
role: User
level: Beginner, Intermediate
hidefromtoc: yes
exl-id: 0e43be98-f471-4860-be84-8f99ab93e983
---
# Release Notes 2021 {#release-notes-2021}

This page lists all the features and improvements for [!DNL Journey Optimizer] released in 2021. 

## November 2021 Release {#november-2021-release}

<table>
<thead>
<tr>
<th><strong>CNAME subdomain delegation</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adobe Journey Optimizer now supports CNAMEs. A CNAME, or Canonical Name record, is a record that points to another domain address rather than an IP address. CNAME subdomain delegation enables you to create a subdomain and use CNAMEs to point to Adobe-specific records. Using this configuration, both you and Adobe share responsibility for maintaining DNS in order to setup environment for sending, rendering and tracking emails.</p>
<p>This method is recommended if your organization's policies restrict the full subdomain delegation method.</p>
<p>Learn more on CNAME subdomain delegation in the <a href="../configuration/delegate-subdomain.md#cname-subdomain-delegation">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


## October 2021 Release {#oct-2021-release}

### New capabilities 

<table>
<thead>
<tr>
<th><strong>Decision Management - Offer Simulations</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now simulate which offers will be delivered to a test profile for a given placement in the Journey Optimizer UI. This allows you to validate your decisioning logic including eligibility constraints and ranking algorithms easily before you put them in production. This capability allows non-technical and technical users to quickly test decision management and troubleshoot potential problems.</p>
<p>For more information, refer to the <a href="../offers/offer-activities/simulation.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Decision Management - Personalize your offers</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now personalize the content of your offers using Adobe Experience Platform profile attributes and audiences, using the same expression editor component found throughout Journey Optimizer UI. </p>
<p>For more information, refer to the <a href="../offers/offer-library/creating-personalized-offers.md#custom-text">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


See also [Adobe Experience Platform October Release Notes](https://experienceleague.adobe.com/docs/experience-platform/release-notes/2021/october-2021.html){target="_blank"} for more changes.

### Improvements

**Journeys**

* **Expression editor** - As a power user, you can now use functions to work with maps. This capability can be leveraged with the subscription lists. As an example, from an audience, you can now get an email address from a subscription list. [Learn more in this sample](../building-journeys/message-to-subscribers-uc.md)

* **Monitoring** - Step events for live journeys and test mode have been enhanced. [New fields](../reports/sharing-field-list.md#serviceevents) have been added related to profile export jobs. For a better user experience, step event fields are now organized in different categories. All previous step events fields are still available in the [stepEvents](../reports/sharing-legacy-fields.md) category. 
* **Accessibility** - Accessibility enhancements have been implemented in journeys. 
* **Collections** - Arrays of objects containing sub-objects are now supported. [Read more](../building-journeys/collections.md)
* **Lists** - Lists screens have been improved for journeys, events, actions, data sources.

**Reporting**

* **Data format in Global view** - You can now toggle between numbers and percentages in the **Global view** of the **Execution** tab.


**Administration**

* **Edit message presets** - You can now edit message presets and monitor their update status. [Learn more](../configuration/channel-surfaces.md#edit-channel-surface)
* **Edit PTR records** - You can now edit PTR records and monitor their update status. [Learn more](../configuration/ptr-records.md#edit-ptr-record)

**Personalization**

* **New helper function for date formatting** - You can now specify how a date string should be represented. [Learn more](../personalization/functions/dates.md#format-date)
 

**Decision Management**

* **Evaluation sequencing** - The new and improved decision creation flow enables you to not only navigate between decision objects more seamlessly, but also gives you a complete control of how offer collections are evaluated by the decision engine. This includes which collections are evaluated together vs separately, and in what order the collections should be evaluated. [Learn more](../offers/offer-activities/create-offer-activities.md#add-decision-scopes)

### Fixes 

* Fixed an issue which prevented the Journey list, Message list and Email designer from being displayed when the browser language was not English.
* Fixed a syntax error which occured when adding personalization using an expression in the Email designer: characters were wrongly escaped.
* Fixed an issue which led to a 404 error when navigating in the **Administration** menu.
* Fixed an issue which triggered other live journeys when testing a journey using a business event.


## September 2021 Release {#september-2021-release}

### New capabilities

<table>
<thead>
<tr>

<th><strong>Reporting - Better insight to targeted audience</strong><br/></th>
</thead>
<tbody>
<tr>
<td>
<p>New metrics are available in reporting: Targeted and Excluded for email & push messages are visible in both live and global reports. </br> To have access to the latest metrics, please note that you will have to reset the different reporting dashboards for each channel and reporting type. For more information on dashboard customization, refer to the <a href="../reports/live-report.md">detailed documentation.</a></p>
<p>A new column in the message execution list displays the number of targeted profiles for each message execution. </p>
<p>For more information, refer to the <a href="../reports/global-report.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>

<th><strong>Pass lists of data dynamically using custom actions</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now pass collections or a list of data in your custom action parameters that will be dynamically populated at runtime. Two kinds of collections are supported: simple collections and object collections. Previously created custom actions will continue working. </p>
<p>For more information on collections, refer to the <a href="../building-journeys/collections.md">detailed documentation</a>. </p>
<p>The filter and intersect functions have been added to the list of functions available in the advanced expression editor. This offers more possibilities for collection filtering and comparing.</p>
<p>Consult the documentation on the <a href="../building-journeys/functions/functionfilter.md">filter</a> and <a href="../building-journeys/functions/functionintersect.md">intersect</a> functions.</p>
</td>
</tr>
</tbody>
</table>

### Improvements

**Journeys**

* System generated schemas and datasets that have been created during provisioning for step events are now in read-only mode, safeguarding against any inadvertent modifications to critical schemas. [Learn more](../reports/sharing-overview.md) 
* Cleanly label the **Wait** activity with a label that will be displayed in the canvas. The label is also used in reporting and test mode logs to clearly identify what you are doing. [Learn more](../building-journeys/about-journey-activities.md#best-practices) 
* Find your events and actions faster by filtering elements in the **Events** and **Action** categories using search. Orchestration activities are no longer filtered. [Learn more](../building-journeys/using-the-journey-designer.md)
* When defining an event ID condition in a rule-based or business event, the "contains" operator is now available for string types of fields. [Learn more](../event/about-creating.md)

**Email configuration**

* When an IP pool has been associated with a message preset, you can now edit it, the update being asynchronous. You can also check each IP pool update status. [Learn more](../configuration/ip-pools.md#edit-ip-pool)


## August 2021 Release {#august-2021-release}

### New capabilities

<table>
<thead>
<tr>

<th><strong>Send messages at the best time - Send-Time Optimization</strong><br/></th>
</thead>
<tbody>
<tr>
<td>
<p>Automatically send your push or email at the best time for every customer you engage with Adobe Journey Optimizer. Send-Time Optimization, powered by Adobe's AI services, predicts the best time to send an email or push message to maximize engagement based on historical open and click rates out of the box.</p>
<p>This feature is currently in beta version and only available to beta customers. To join the beta program, contact Adobe Customer Care.</p>
<p>For more information, refer to the <a href="../building-journeys/journeys-message.md#send-time-optimization">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>

<th><strong>Leverage schema relationships in business events - Lookup table management</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now leverage relationships between schemas when configuring a business events. This comes in addition to the ability to leverage fields from  linked tables when configuring a unitary event, when using conditions in a journey, in message personalization, and in custom action personalization.</p>
<p>For more information, refer to the <a href="../event/experience-event-schema.md#leverage_schema_relationships">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Personalized URLs</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Personalized URLs take recipients to specific pages of a website, or to a personalized microsite, depending on the profile attributes. In Adobe Journey Optimizer, you can now add personalization to URLs in your message content. URL personalization can be applied to text and images, and use profile data or contextual data.</p>
<p>For more information, refer to the <a href="../personalization/personalization-syntax.md#perso-urls">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Make sure your emails get to your users - Email Retry</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now define the retry period on a per preset basis to ensure that retry attempts are not performed anymore when no longer needed. For example, you may set the retry period to 24 hours for a password-reset transactional message containing a link valid for only a day. Note that retry settings only apply to the email channel.</p>
<p>For more information, refer to the <a href="../configuration/retries.md#retry-duration">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Define addresses to exclude from sending - Suppression list</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Adding email addresses and domains into the suppression list is now available from the user interface, either one by one, either in bulk mode through a CSV file upload.</p>
<p>For more information, refer to the <a href="../configuration/manage-suppression-list.md#add-addresses-and-domains">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


### Improvements

**Journeys**

* **Dynamic headers** - You can now pass dynamic data in HTTP header parameters. These parameters can be used by the integration systems that receive the journey action HTTP calls, for example timestamp or tracking ID. [Learn more](../action/about-custom-action-configuration.md#url-configuration)
* **Dynamic URL paths** - You can now set up dynamic URL paths for custom actions. [Learn more](../action/about-custom-action-configuration.md#url-configuration)
* The overall throttling rate for read audiences has been changed from 17,000 to 20,000 messages per second. [Learn more](../building-journeys/read-audience.md#configuring-segment-trigger-activity)

**User interface**

* **Search** - On every page, you can now search business objects and help articles directly from the Unified Experience Cloud search field. [Learn more](../start/user-interface.md#unified-search)
* **Recents** - The display of recents elements from Adobe Journey Optimizer home page is now extended to additional business objects. With this update, shortcuts to your recently accessed include Messages, Journeys, Audiences, Schemas, Datasets, Data Sources, Events, Actions, Sources, and Destinations. [Learn more](../action/about-custom-action-configuration.md#passing-collection)

**Content Design**

* **Background** - Background images are now supported in live preview. [Learn more](../content-management/preview-test.md)
<!--* **One-click opt-out link** - You can insert a new type of link into your email content: the **Opt-out** link allows users to unsubscribe from receiving your communications in just one click, without being redirected to a landing page to confirm opting out. [Learn more](../privacy/opt-out.md#one-click-opt-out-link)-->

**Personalization**

* **Expression editor** - You can now easily add a fall-back value when defining personalization: when personalization field is empty for a profile, the fall-back value will display. [Learn more](../personalization/functions/helpers.md)

**Email configuration**

* **Allowed list** - The allowed list can now be enabled and disabled on a non-production sandbox through an API call. [Learn more](../configuration/allow-list.md#enable-allow-list)
* **Navigation** - The suppression list, which was accessible under the **Administration > Channels > Email configuration > General** menu, has been moved to the new **Suppression list** submenu, which gathers all related capabilities for easier access. [Learn more](../configuration/manage-suppression-list.md#access-suppression-list)

**Decision management**

* The way you add and configure representations when creating an offer has been updated for improved user experience. In particular, the Asset library is now displayed only when you define image-type content for a representation. [Learn more](../offers/offer-library/creating-personalized-offers.md#representations)

### Fixes 

* Fixed an accessibility issue in message tab navigation.
* Fixed a localization issue in the email designer labels.
* Fixed an issue when selecting more than one node in a journey and clicking 'Delete' on the property pane.
* Fixed an issue which prevented from adding a new header to an action used in a journey.
* You can now find out the reason why a message preset creation failed through a more explicit warning in the user interface.


## July 2021 Release {#july-2021-release}

### New capabilities

<table>
<thead>
<tr>
<th><strong>Use metadata in your messages - Lookup table management</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Enrich your experiences with reference data you've loaded into Journey Optimizer. Examples include looking up metadata on a reservation ID in an experience event, or finding product information from a sku in an experience event for use in the canvas. </p>
<p>You can now leverage relationships between schemas in order to use one dataset as a lookup table for another. You can then leverage all the fields from the linked tables when configuring a unitary event, when using conditions in a journey, in message personalization, and in custom action personalization.</p>
<p>For more information, refer to the <a href="../event/experience-event-schema.md#leverage_schema_relationships">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Allowed list</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now define a define a specific sending-safe list at the sandbox level, to have a safe environment for testing purpose. On a non-production instance, where mistakes can occur, the allowed list ensures you have no risk of sending out unwanted messages to your customers. This feature is enabled by leveraging Suppression APIs.</p>
<p>For more information, refer to the <a href="../configuration/allow-list.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

### Improvements

**Journeys**

* The overall throttling rate of all the read audiences that run simultaneously in the same sandbox is limited to 17,000 messages per second. [Read more](../building-journeys/read-audience.md#configuring-segment-trigger-activity)
* The **Cache duration** field has been removed from the data source configuration pane. [Read more](../datasource/about-data-sources.md)
* For external data sources, a capping rule of 15 calls per second is now automatically defined. [Read more](../configuration/external-systems.md#capping)
* For live journeys, the journey properties screen now displays the publication date and the name of the user who published the journey. [Read more](../building-journeys/journey-gs.md#change-properties)
* In the journey list screen, the journey type filter has been added. [Read more](../start/user-interface.md#filter-lists)
* The **[!UICONTROL Throttling rate]** parameter has been added in the Read audience activity. [Read more](../building-journeys/read-audience.md#configuring-segment-trigger-activity)

**Preview and test**

* Identity and namespace are now visible in the **[!UICONTROL Preview]** screen. [Read more](../content-management/preview-test.md#preview-your-messages)
* The number of test emails for proofs is now restricted to 10.
* Characters allowed for the **Subject line prefix** in proofs are now limited. [Read more](../content-management/preview-test.md#send-proofs)

**Personalization expression editor**

* The helper drop-down list has been renamed and reordered.

### Fixes 

* Fixed an issue which was causing duplicate messages being delivered for batch email delivery.
* Events are now generated accordingly when email sending is not performed once the retry period is over.
* Fixed an issue where IP information was missing in PTR Records screen.
* Localization in offer rail within Expression editor is now implemented.
* Fixed incorrect spacing in information popups.
* Fixed an issue in the Email designer when uploading an HTML file where internal style sheet with `background-image` property was not supported.
