---
solution: Journey Optimizer
product: journey optimizer
title: Release notes
description: Journey Optimizer early Release notes
feature: Release Notes
topic: Content Management
hide: yes
hidefromtoc: yes
exl-id: 6e7d1300-8efd-4fdc-90e3-3ccdc3babd2f
---
# Early release notes {#e-release-notes}

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated at the end of each month in the [release notes](release-notes.md). 

**Early release notes below are subject to change without prior notice until the release availability date**. Links, screens and updated documentation are published in the [release notes](release-notes.md), at the release date.

## October 2024 early release notes {#e-2024}

**Release date**: October 29-30, 2024

### New capabilities {#e-features}

This release brings the new capabilities detailed below.

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
<!--p>For more information, refer to the <a href="../content-management/gs-generative.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/ai-content.gif"/-->
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Approvals in journeys and campaigns (General availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With approval policies, you can now set up an approval process within Journey Optimizer that allows marketing teams to ensure campaigns and journeys are reviewed and signed off by the appropriate stakeholders before they go live.</p>
<p>Previously available for a set of organizations (LA), approval policies are now available to all users (GA).</p>
<p>For more information, refer to the <a href="../test-approve/gs-approval.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/approval.gif"/>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Email configuration personalization (General availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now define dynamic subdomains and personalized header parameters when creating email channel configurations, for increased flexibility and control over your email settings.</p><p>Using a personalized configuration in a campaign or a journey allows you to preview your email content to check for potential errors with the dynamic settings you defined.</p>
<p>Previously available for a set of organizations (LA), email configuration personalization is now available to all users (GA).</p>
<p>For more information, refer to the <a href="../email/surface-personalization.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Test your content using sample input data (Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey optimizer now allows you to test different variants of your email content by previewing it and sending proofs using sample input data uploaded from a CSV file or added manually. All the profiles attributes used in your content for personalization are automatically detected by the system and can be used for your tests to create multiple variants.</p>
<p>This capability is currently available as a beta.</p>
<!--<p>For more information, refer to the <a href="../email/surface-personalization.md">detailed documentation</a>.</p>-->
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Conflict and priority management (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>In Journey Optimizer, managing the volume and timing of campaigns and journeys is essential to avoid overwhelming customers with too many interactions. Journey Optimizer now offers several tools for conflict management and prioritization.</p><p><ul><li><b>Journey frequency capping</b>: You can now create rule sets to apply to your journeys, allowing you to limit the number of journeys for a profile per day, week, or month, as well as control the number of concurrent journeys running simultaneously.</li>
<li><b>Priority score</b>: You can now assign a priority score to a campaign or a journey, ranging from 0 to 100. A higher number indicates a higher priority. When two campaigns or journey actions use the same channel configuration, Journey Optimizer will select the one with the highest priority score. If the campaigns have the same score, the campaign that was least recently modified will be chosen.</li>
<li><b>View potential conflicts</b>: A new "View potential conflicts" button in journeys and campaigns now allows you to identify overlap with other journeys or campaigns such as the start date, the targeted audience, or the selected channel configuration.</li>
<li><b>Journey Arbitration</b>: This new capability enables you to prioritize the most important journeys for your customers. You can create a rule to suppress entry into a lower priority journey when a customer qualifies for an upcoming journey of higher priority.</li></ul></p>
<!--<p>For more information, refer to the <a href="../email/surface-personalization.md">detailed documentation</a>.</p>-->
<p>Conflict and priority management capabilities are available in Limited Availability to a select group of customers. Please note that these features will be gradually rolled out to more users in the future. Reach out to your account team if interested in being added to the waitlist for these features.</p>

</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Non-visual editing mode for the web designer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>As an alternative to the Journey Optimizer web designer, you can now add modifications to your website using a non-visual editor. It allows you to enter your changes manually without opening the pages in the visual editor.
This non-visual editing mode is useful if you cannot install browser extensions such as the Adobe Experience Cloud Visual Helper, which is required to load your pages in the web designer.</p>
<!--p>For more information, refer to the <a href="../email/surface-personalization.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Content experimentation in journeys (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Already available in campaigns, Adobe Journey Optimizer now supports experiments in journeys. Experiments are randomized trials, which in the context of online testing, means that you expose some randomly selected users to a given variation of a message, and another randomly selected set of users to some other variation or treatment. After exposure, you can then measure the outcome metrics you are interested in, such as opens of emails, subscriptions, or purchases.</p>
<p>Previously available for a set of organizations (LA), experiments in journeys are now available to all users (GA).</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Decisioning (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Decisioning, previously available for a set of organizations (LA) and known as Experience Decisioning, is now available to all users (GA). It simplifies personalization by offering a centralized catalog of marketing offers known as 'decision items' and a sophisticated decision engine. This engine leverages rules and ranking criteria to select and present the most relevant decision items to each individual. These decision items are seamlessly integrated into a wide range of inbound surfaces through the code-based experience channel.</p>

<p>For now, Decisioning is unavailable for customers who have purchased the Adobe Healthcare Shield and Privacy and Security Shield add-on offerings.</p>

<!--p>For more information, refer to the <a href="../configuration/business-rules.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Rule sets (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create granular frequency capping rules, and apply them to your messages or journeys through rule sets. This new capability lets you control how often your audiences receive a message by setting cross-channel rules, that automatically exclude over-solicited profiles from messages and actions.</p><p>It also allows you to limit the number of journeys per day, week, or month, as well as control the number of concurrent journeys running simultaneously.</p>
<p>Rule sets are available in Limited Availability to a select group of customers. Please note that these features will be gradually rolled out to more users in the future. Reach out to your account team if interested in being added to the waitlist for this feature.</p>
<!--p>For more information, refer to the <a href="../configuration/business-rules.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Multilingual messages in journeys and campaigns (General availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now effortlessly create content in multiple languages within a single campaign or journey. With this feature, you can switch between languages when editing your campaign or your journey, streamlining the entire editing process and improving your capability to efficiently manage multilingual content.</p>
<p>With general availability, multilingual content is now accessible across all channels. </p>
<!--p>For more information, refer to the <a href="../configuration/business-rules.md">detailed documentation</a>.</p-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Movable Ink and Adobe Journey Optimizer integration</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now integrate Movable Ink Da Vinci and Adobe Journey Optimizer. With this new integration you can: </p>
<p><ul><li>Leverage powerful capabilities in Movable Ink's Da Vinci product to assemble and personalize email variations for batch campaigns</li>
<li>Accelerate practitioner workflows for Journey Optimizer customers using Da Vinci for authoring and AJO for optimization and delivery</li>
<li>Optimize Da Vinci models with Adobe data.</li></ul></p>
<!--p>For more information, refer to the <a href="../code-based/get-started-code-based.md">detailed documentation</a>.</p-->
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Updated reporting experience (General availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Available since Oct 16, 2024</p>
<p>Journey Optimizer reporting is now generally available (GA) and comes with an improved interoperability with Customer Journey Analytics capabilities, standardizing reporting across both platforms and improving data consistency and reliability. This seamless integration between Journey Optimizer and Customer Journey Analytics provides a clearer view of performance metrics, enabling users to make more informed decisions.</p>
<p>With general availability, four new features are introduced: the ability to create simple metrics, create and publish audiences, ask ad-hoc questions using Insight Builder, and schedule reports to be automatically emailed to key recipients.</p>
<p>For more information, refer to the <a href="../reports/report-cja-manage.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/ajo-cja.gif">
<p>Important:The current reporting experience will be retired as of January 2025. After this date, the new reporting experience will become the standard. We recommend familiarizing yourself with the new features and functionalities to ensure a smooth transition. <a href="../reports/report-gs-cja.md">Learn how to get started with Journey Optimizer new Reporting interface</a></p>
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
<p>Available since Oct 1, 2024</p>
<p>With the Code-based experience channel, Adobe Journey Optimizer allows you to do advanced personalization and testing for any of your inbound properties, enabling seamless delivery of tailored experiences across diverse touchpoints such as web apps, mobile apps, desktop apps, video consoles, TV connected devices, smart TVs, kiosks, ATMs, IoT devices, and more. The Code-based experience channel is now available in the journey canvas.</p>
<p>For more information, refer to the <a href="../code-based/create-code-based.md">detailed documentation</a>.</p>
<img src="../assets/do-not-localize/code-based-journey.gif"/>
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
<p>Available since Oct 1, 2024</p>
<p>With the Web channel, Adobe Journey Optimizer allows you to personalize the web experience you deliver to your customers through inbound web journeys. The Web channel is now available in the journey canvas.</p>
<p>For more information, refer to the <a href="../web/create-web.md">detailed documentation</a>.</p>
<img src="../assets/do-not-localize/web-journey.gif"/>
</tr>
</tbody>
</table>

### Improvements {#e-improvements}

This release comes with the improvements listed below.

**SMS channel**

>[!AVAILABILITY]
>
>Following enhancements are only available with Sinch and Infobip providers.

SMS enhancements have been introduced to improve your messaging capabilities:

* You can define and manage unique keywords for your SMS campaigns and journeys, enabling more personalized and efficient communication.

* You can create and deliver a default SMS message when a keyword is not recognized.

* You can now edit or delete an SMS API Channel Configuration.

<!--**Journeys**-->

<!--* **Path experiment in journeys** - With the journey path experiment, you can now define and track key metrics for your journey paths, allowing you to measure the impact of your activities and to provide clearer insights into your performance. -->

<!--* **Max number of Live journeys** - Journey Optimizer now has a guardrail of 500 live journeys on production sandboxes, instead of 100. The number of live journeys is visible in the journey canvas. <!-- DOCAC-10977-->

**Datasets**

* **Time-to-live guardrail** - Starting November 1st, 2024, a time-to-live (TTL) guardrail will be rolled out to Journey Optimizer system-generated datasets in new sandboxes and new orgs as follows:
 
    * 90 days for data in the profile store
    * 13 months for data in the data lake
 
    This change will be rolled out to existing customer sandboxes subsequently in a second phase.
 
    Additionally, starting November 1st, streaming segmentation will no longer support the use of send and open events from tracking and feedback datasets. This change will apply to all customer sandboxes and orgs at that time. [Learn more](../data/datasets-ttl.md)

* **Parameters in custom actions** (Availability date: Oct 3, 2024) - NULL and optional parameters are now supported in custom actions. [Learn more](../action/about-custom-action-configuration.md#define-the-message-parameters)

**Reporting**

* **Experience Decisioning reporting** is now available, offering essential insights into how your visitors interact with your experiences.

**Data governance & Consent policies** - Availability date: Oct 7, 2024
  
* **Data governance policies** enforcement now takes place across all channels in Journey Optimizer. For customers that have created  policies in Adobe Experience Platform, these are applied to marketing actions as part of the channel configurations setup. When you create content using a configuration, the system checks all the personalization fields for any data governance violations. If a violation is found, publishing a journey or campaign will not be possible. [Learn more](../action/action-privacy.md)

* **Custom consent policies** now apply to all Journey Optimizer channels. On enforcement before a message is sent or an inbound experience is delivered, the system checks that the user has given consent to use personalization fields in the content that they will receive. If no consent is given, the experience will not be displayed. [Learn more](../action/consent.md)

    >[!NOTE]
    >
    >Consent policies are currently only available for organizations that have purchased the Adobe **Healthcare Shield** or **Privacy and Security Shield** add-on offerings.

**Audiences** -  Availability date: Oct 8, 2024

* When targeting a CSV file audience, you can now use attributes from the file in the personalization editor and in journeys and campaigns rule builer. [Learn more](../audience/about-audiences.md)

* The use of audiences and attributes from custom upload (CSV file) is now available for use with Healthcare Shield or Privacy and Security Shield.

**Code-based channel**

* Content templates are now available. You can speed up authoring your code-based experiences starting from a content template built by your developers. Using a content template will allow the marketer to just modify some values or fields, instead of composing the whole HTML or JSON content payload.

**Decisioning**

[Adobe Customer Journey Analytics](https://experienceleague.adobe.com/docs/analytics-platform/using/cja-overview/cja-overview.html) users can now choose custom models to optimize on when setting up an AI model in Decisioning (formerly known as Experience Decisioning). This allows you, for example, to optimize on a custom "purchases" table rather than defined constraints such as clickthrough rate."
