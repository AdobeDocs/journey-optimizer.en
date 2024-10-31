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
<th><strong>Conflict and priority management (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>In Journey Optimizer, managing the volume and timing of campaigns and journeys is essential to avoid overwhelming customers with too many interactions. Journey Optimizer now offers several tools for conflict management and prioritization. <p>For more information, refer to the <a href="../email/surface-personalization.md">detailed documentation</a>.</p></p><p><ul><li><b>Journey frequency capping</b>: You can now create rule sets to apply to your journeys, allowing you to limit the number of journeys for a profile per day, week, or month, as well as control the number of concurrent journeys running simultaneously.</li>
<li><b>Priority score</b>: You can now assign a priority score to a campaign or a journey, ranging from 0 to 100. A higher number indicates a higher priority. When two campaigns or journey actions use the same channel configuration, Journey Optimizer will select the one with the highest priority score. If the campaigns have the same score, the campaign that was least recently modified will be chosen.</li>
<li><b>View potential conflicts</b>: A new "View potential conflicts" button in journeys and campaigns now allows you to identify overlap with other journeys or campaigns such as the start date, the targeted audience, or the selected channel configuration.</li>
<li><b>Journey Arbitration</b>: This new capability enables you to prioritize the most important journeys for your customers. You can create a rule to suppress entry into a lower priority journey when a customer qualifies for an upcoming journey of higher priority.</li>
<li><b>Frequency capping by communication type: </b>With rule sets, you can now set granular rules by communication type (e.g., Sales, Promotional) to prevent overloading customers with similar messages. You can control frequency across multiple channels, automatically excluding over-solicited profiles to ensure a better customer experience.</li></ul>

<p>Conflict and priority management capabilities are available in Limited Availability to a select group of customers. Please note that these features will be gradually rolled out to more users in the future. Reach out to your account team if interested in being added to the waitlist for these features.</p>
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
<li>Accelerate practitioner workflows for Journey Optimizer customers using Da Vinci for authoring and Adobe Journey Optimizer for optimization and delivery</li>
<li>Optimize Da Vinci models with Adobe data.</li></ul></p>
<p>For more information, refer to the <a href="https://movableink.com/adobe-and-movable-ink">Movable Ink Da Vinci documentation</a>.</p>
</tr>
</tbody>
</table>

Previously available for a set of organizations (LA), the following capabilities are now available to all users (GA):

<table>
<thead>
<tr>
<th><strong>Email configuration personalization (General Availability) </strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>For increased flexibility and control over your email settings, you can define dynamic subdomains and personalized header parameters when creating email channel configurations.
</p>
<p>For more information, refer to the <a href="../email/surface-personalization.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/surface-perso.gif"/>
<p>Available since Oct 23, 2024</p>
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
<p>For more information, refer to the <a href="../test-approve/gs-approval.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/approval.gif"/>
<p>Available since Oct 22, 2024</p>
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
<p>For more information, refer to the <a href="../content-management/content-experiment.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


<!--<table>
<thead>
<tr>
<th><strong>Decisioning (General Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Decisioning, previously available for a set of organizations (LA) and known as Experience Decisioning, is now available to all users (GA), including organizations that have purchased the Adobe Healthcare Shield or Privacy and Security Shield add-on offerings.</p><p>Decisioning simplifies personalization by offering a centralized catalog of marketing offers known as 'decision items' and a sophisticated decision engine. This engine leverages rules and ranking criteria to select and present the most relevant decision items to each individual. These decision items are seamlessly integrated into a wide range of inbound surfaces through the code-based experience channel.</p>
<p>For more information, refer to the <a href="../experience-decisioning/gs-experience-decisioning.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>-->

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
<p>For more information, refer to the <a href="../content-management/multilingual-gs.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/multilingual.gif">
</td>
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
<p>Journey Optimizer reporting is now generally available (GA) and comes with an improved interoperability with Customer Journey Analytics capabilities, standardizing reporting across both platforms and improving data consistency and reliability. This seamless integration between Journey Optimizer and Customer Journey Analytics provides a clearer view of performance metrics, enabling users to make more informed decisions.</p>
<p>With General Availability, four new features are introduced: the ability to create simple metrics, create and publish audiences, ask ad-hoc questions using Insight Builder, and schedule reports to be automatically emailed to key recipients.</p>
<p>For more information, refer to the <a href="../reports/report-cja-manage.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/ajo-cja.gif">
<p>Important: The current reporting experience will be retired as of January 2025. After this date, the new reporting experience will become the standard. We recommend familiarizing yourself with the new features and functionalities to ensure a smooth transition. <a href="../reports/report-gs-cja.md">Learn how to get started with Journey Optimizer new Reporting interface</a></p>
<p>Available since Oct 16, 2024</p>
</tr>
</tbody>
</table>


<!--The following capabilities are available to all customers in public beta:

<table>
<thead>
<tr>
<th><strong>Test your content using sample input data (Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey optimizer now allows you to test different variants of your email content by previewing it and sending proofs using sample input data uploaded from a file or added manually. All the profiles attributes used in your content for personalization are automatically detected by the system and can be used for your tests to create multiple variants.</p>
<p>This capability is currently available to all customers as a public beta.</p>
<p>For more information, refer to the <a href="../email/surface-personalization.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>-->

<!--<table>
<thead>
<tr>
<th><strong>Use Adobe Experience Platform data for personalization (Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Leverage data from Adobe Experience Platform in the personalization editor to personalize your content. To do this, datasets needed for lookup personalization must first be enabled through an API call. Once done, you can use their data to personalize your content into [!DNL Journey Optimizer].</p>
<p>This capability is currently available to all customers as a public beta.</p>
<p>For more information, refer to the <a href="../personalization/lookup-aep-data.md"</a>.</p>
</td>
</tr>
</tbody>
</table>-->

### Improvements {#24-10-improvements}

This release comes with the improvements listed below.

**SMS channel**

SMS enhancements have been introduced to improve your messaging capabilities:

* You can define and manage unique keywords for your SMS campaigns and journeys, enabling more personalized and efficient communication.

* You can create and deliver a default SMS message when a keyword is not recognized.

* You can now edit or delete an SMS API Channel Configuration.

Learn more about these improvements in the SMS configuration documentation for [Infobip](../sms/sms-configuration-infobip.md) and [Sinch](../sms/sms-configuration-sinch.md).

<!--**Journeys**-->

<!--* **Path experiment in journeys** - With the journey path experiment, you can now define and track key metrics for your journey paths, allowing you to measure the impact of your activities and to provide clearer insights into your performance. -->

<!--* **Max number of Live journeys** - Journey Optimizer now has a guardrail of 500 live journeys on production sandboxes, instead of 100. The number of live journeys is visible in the journey canvas. <!-- DOCAC-10977-->

**Web channel**

* **Non-visual editing mode for the web designer** - As an alternative to the Journey Optimizer web designer, you can now add modifications to your website using a non-visual editor. It allows you to enter your changes manually without opening the pages in the visual editor. This non-visual editing mode is useful if you cannot install browser extensions such as the Adobe Experience Cloud Visual Helper, which is required to load your pages in the web designer. [Learn more](../web/web-non-visual-editor.md)


**Datasets**

* **Send and open events** - Starting November 1st, 2024, streaming segmentation will no longer support the use of send and open events from Journey Optimizer tracking and feedback datasets. This change will apply to all customer sandboxes and organizations. [Learn more](../data/datasets-ttl.md#segmentation-update)
 
* **Dataset Time-to-live (TTL)** - Starting in February 2025, a time-to-live (TTL) guardrail will be rolled out to Journey Optimizer system-generated datasets in new sandboxes and new orgs as follows:

    * 90 days for data in the profile store
    * 13 months for data in the data lake
    
    This change will be rolled out to existing customer sandboxes in a subsequent phase. [Learn more](../data/datasets-ttl.md#ttl)

* **Parameters in custom actions** (Availability date: Oct 3, 2024) - NULL and optional parameters are now supported in custom actions. [Learn more](../action/about-custom-action-configuration.md#define-the-message-parameters)

**Reporting**

* **Experience Decisioning reporting** is now available, offering essential insights into how your visitors interact with your experiences. [Learn more](../reports/campaign-global-report-cja-code.md##decisioning-kpis)

**Data governance & Consent policies** - Availability date: Oct 7, 2024
  
* **Data governance policies** enforcement now takes place across all channels in Journey Optimizer. For customers that have created policies in Adobe Experience Platform, these are applied to marketing actions as part of the channel configurations setup. When you create content using a configuration, the system checks all the personalization fields for any data governance violations. If a violation is found, publishing a journey or campaign will not be possible. [Learn more](../action/action-privacy.md)

* **Custom consent policies** now apply to all Journey Optimizer channels. On enforcement before a message is sent or an inbound experience is delivered, the system checks that the user has given consent to use personalization fields in the content that they will receive. If no consent is given, the experience will not be displayed. [Learn more](../action/consent.md)

    >[!NOTE]
    >
    >Consent policies are currently only available for organizations that have purchased the Adobe **Healthcare Shield** or **Privacy and Security Shield** add-on offerings.

**Audiences** -  Availability date: Oct 8, 2024

* When targeting a CSV file audience, you can now use attributes from the file in the personalization editor and in journeys and campaigns rule builer. [Learn more](../audience/about-audiences.md)

* The use of audiences and attributes from custom upload (CSV file) is now available for use with Healthcare Shield or Privacy and Security Shield.

**Configuration** - Availability date: Oct 23, 2024

* When using a personalized configuration in a campaign or a journey, you can now preview your email content to check for potential errors with the dynamic settings you defined. [Learn more](../email/surface-personalization.md#check-configuration)

**Code-based channel**

* Content templates are now available. You can speed up authoring your code-based experiences starting from a content template built by your developers. Using a content template will allow the marketer to just modify some values or fields, instead of composing the whole HTML or JSON content payload. [Learn more](../content-management/content-templates.md)

**Decisioning**

<!--* [Adobe Customer Journey Analytics](https://experienceleague.adobe.com/docs/analytics-platform/using/cja-overview/cja-overview.html) users can now choose custom models to optimize on when setting up an AI model in Decisioning (formerly known as Experience Decisioning). This allows you, for example, to optimize on a custom "purchases" table rather than defined constraints such as clickthrough rate."-->

* When adding a decision policy to a code-based campaign with Experience Decisioning, you can now manually select single decision items, in addition to selection strategies. In addition, you can now select more than one fallback offers. This guarantees that there are a certain number of decision items returned. [Learn more](../experience-decisioning/create-decision.md)
