---
solution: Journey Optimizer
product: journey optimizer
title: Release notes 2024
description: Journey Optimizer 2024 Release notes
feature: Release Notes
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: bae533c5-1bfc-48bf-9f8d-1145383c040c
---
# Release Notes 2024 {#release-notes-2024}

This page lists all the features and improvements for [!DNL Journey Optimizer] released in 2024. 

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
<p>In Journey Optimizer, managing the volume and timing of campaigns and journeys is essential to avoid overwhelming customers with too many interactions. Journey Optimizer now offers several tools for conflict management and prioritization. <p>For more information, refer to the <a href="../conflict-prioritization/gs-conflict-prioritization.md">detailed documentation</a>.</p></p><p><ul><li><b>Journey frequency capping</b>: You can now create rule sets to apply to your journeys, allowing you to limit the number of journeys for a profile per day, week, or month, as well as control the number of concurrent journeys running simultaneously.</li>
<li><b>Priority score</b>: You can now assign a priority score to a campaign or a journey, ranging from 0 to 100. A higher number indicates a higher priority. When two campaigns or journey actions use the same channel configuration, Journey Optimizer will select the one with the highest priority score. If the campaigns have the same score, the campaign that was least recently modified will be chosen.</li>
<li><b>View potential conflicts</b>: A new "View potential conflicts" button in journeys and campaigns now allows you to identify overlap with other journeys or campaigns such as the start date, the targeted audience, or the selected channel configuration.</li>
<li><b>Journey Arbitration</b>: This new capability enables you to prioritize the most important journeys for your customers. You can create a rule to suppress entry into a lower priority journey when a customer qualifies for an upcoming journey of higher priority.</li>
<li><b>Frequency capping by communication type: </b>With rule sets, you can now set granular rules by communication type (e.g., Sales, Promotional) to prevent overloading customers with similar messages. You can control frequency across multiple channels, automatically excluding over-solicited profiles to ensure a better customer experience.</li></ul>

<img src="assets/do-not-localize/gif-conflict.gif">

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


<table>
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

<!--The following capabilities are available to all customers in public beta:-->

<table>
<thead>
<tr>
<th><strong>Test your content using sample input data (Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey optimizer now allows you to test different variants of your content by previewing it and sending email proofs using sample input data uploaded from a file or added manually. All the profiles attributes used in your content for personalization are automatically detected by the system and can be used for your tests to create multiple variants.</p>
<p>This capability is currently available to all customers as a public beta, for the Email, SMS and Push notfication channels.</p>
<p>For more information, refer to the <a href="../test-approve/simulate-sample-input.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/gif-simulate.gif">
</td>
</tr>
</tbody>
</table>


<table>
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
<p>For more information, refer to the <a href="../personalization/lookup-aep-data.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#24-10-improvements}

This release comes with the improvements listed below.

**SMS channel**

* You can now edit or delete an SMS API Channel Configuration. [Learn more](../sms/sms-configuration.md)

* The following enhancements have been introduced to improve your SMS messaging capabilities with Infobip and Sinch:

    * You can define and manage unique keywords for your SMS campaigns and journeys, enabling more personalized and efficient communication.

    * You can create and deliver a default SMS message when a keyword is not recognized.

    Learn more about these improvements in the SMS configuration documentation for [Infobip](../sms/sms-configuration-infobip.md) and [Sinch](../sms/sms-configuration-sinch.md). 


<!--**Journeys**-->

<!--* **Path experiment in journeys** - With the journey path experiment, you can now define and track key metrics for your journey paths, allowing you to measure the impact of your activities and to provide clearer insights into your performance. -->

<!--* **Max number of Live journeys** - Journey Optimizer now has a guardrail of 500 live journeys on production sandboxes, instead of 100. The number of live journeys is visible in the journey canvas. (DOCAC-10977) --> 

**Web channel**

* **Non-visual editing mode for the web designer** - As an alternative to the Journey Optimizer web designer, you can now add modifications to your website using a non-visual editor. It allows you to enter your changes manually without opening the pages in the visual editor. This non-visual editing mode is useful if you cannot install browser extensions such as the Adobe Experience Cloud Visual Helper, which is required to load your pages in the web designer. [Learn more](../web/web-non-visual-editor.md)


**Datasets**

* **Send and open events** - Starting November 1st, 2024, streaming segmentation will no longer support the use of send and open events from Journey Optimizer tracking and feedback datasets. This change will apply to all customer sandboxes and organizations. [Learn more](../data/datasets-ttl.md#segmentation-update)
 
* **Dataset Time-to-live (TTL)** - Starting in February 2025, a time-to-live (TTL) guardrail will be rolled out to Journey Optimizer system-generated datasets in new sandboxes and new orgs as follows:

    * 90 days for data in the profile store
    * 13 months for data in the data lake
    
    This change will be rolled out to existing customer sandboxes in a subsequent phase. [Learn more](../data/datasets-ttl.md#ttl)

* **Parameters in custom actions** - Availability date: Oct 3, 2024 - NULL and optional parameters are now supported in custom actions. [Learn more](../action/about-custom-action-configuration.md#define-the-message-parameters)

**Reporting**

* **Decisioning reporting** is now available, offering essential insights into how your visitors interact with your experiences. [Learn more](../reports/campaign-global-report-cja-code.md#decisioning-kpis)

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

* [Adobe Customer Journey Analytics](https://experienceleague.adobe.com/docs/analytics-platform/using/cja-overview/cja-overview.html) users can now choose custom models to optimize on when setting up an AI model in Decisioning (formerly known as Experience Decisioning). This allows you, for example, to optimize on a custom "purchases" table rather than defined constraints such as clickthrough rate. [Learn more](../experience-decisioning/ranking.md)

* When adding a decision policy to a code-based campaign with Decisioning, you can now manually select single decision items, in addition to selection strategies. In addition, you can now select more than one fallback offers. This guarantees that there are a certain number of decision items returned. [Learn more](../experience-decisioning/create-decision.md)



## September '24 release {#24-9-rn}

<!--
>[!CAUTION]
>
>**Early release notes below are subject to change without prior notice until the release date**. Links, screens and updated documentation are published at the release date.
>
-->

**Release date**: September 24-26, 2024

### New capabilities {#24-9-features}

This release brings the new capabilities detailed below.

<table>
<thead>
<tr>
<th><strong>Content Cards for mobile apps and websites</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Content cards are a new digital messaging feature in Adobe Journey Optimizer that delivers personalized and engaging content directly within mobile apps and websites. Unlike traditional push notifications, Content Cards integrate seamlessly into the user interface, offering persistent, non-intrusive updates that enhance user interaction and experience.</p>
<p>This feature enables marketers to present relevant, rich media content to users, driving higher engagement and ensuring important messages are seen without disrupting the user journey.</p>
<p>For more information, refer to the <a href="../content-card/get-started-content-card.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/content-card.gif"/>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Approvals in journeys and campaigns (LA)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With approval policies, you can now set up an approval process within Journey Optimizer that allows marketing teams to ensure campaigns and journeys are reviewed and signed off by the appropriate stakeholders before they go live.</p>
<p>Approval policies are currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../test-approve/gs-approval.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/approval.gif"/>
</td>
</tr>
</tbody>
</table>

<!--<table>
<thead>
<tr>
<th><strong>Email Content Locking</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now allows you to lock content in email templates, either by locking the entire template or specific structures and component. This allows you to prevent unintentional edits or deletions, giving you greater control over template customization, and improving the efficiency and reliability of your email campaigns.</p>
<p>For more information, refer to the <a href="../content-management/gs-generative.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/gif-content-locking.gif">
</td>
</tr>
</tbody>
</table>-->

<table>
<thead>
<tr>
<th><strong>Global Exit Criteria in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Now you define exit criteria at a journey level. By adding exit criteria, you make the profiles exit the journey as soon as an event happen (eg: Purchase) or they qualify for an audience. This will prevent the user from getting any further communications from the journey.</p>
<p>For more information, refer to the <a href="../building-journeys/journey-properties.md#exit-criteria">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>AI Assistant</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Once you have created and personalized your message, take your content to the next level with the AI Assistant in Journey Optimizer. You can now use the AI Assistant to optimize your message's impact by experimenting with different main titles, and images. Each variant is managed as a unique Treatment, to measure and compare which title effectively generates more clicks.</p>
<p>Immerse yourself in a hands-on experience with <a href="https://experienceleague.adobe.com/en/apps/journey-optimizer/ai-assistant-content-accelerator">our live feature preview</a>, designed to let you explore its features firsthand and fully understand its capabilities.</a>.</p>
<p>For more information, refer to the <a href="../content-management/gs-generative.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/ai-content.gif"/>
<p>Availability date: Sept 12, 2024</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Guided Channel Setup</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Guided Channel Setup enables you to automate and validate channel setup in a unified experience, speeding up the process of getting started with Journey Optimizer. This new guided setup streamlines rapid channel configuration, ensuring all necessary resources are readily installed and working within Experience Platform, Journey Optimizer, and Data Collection. This enables marketing, product and data engineering teams to quickly begin with campaign and journey creation.</p>
<p>For more information, refer to the <a href="../configuration/set-mobile-config.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/guided-setup.gif"/>
<p>Availability date: Sept 3, 2024</p>
</br>
</td>
</tr>
</tbody>
</table>


### Improvements {#24-9-improvements}

This release comes with the improvements listed below.

**Audiences** - Availability date: Sept 17, 2024

**License usage** - The License usage dashboard now shows the Engageable Profiles, instead of Engageable Audiences. [Learn more](../audience/license-usage.md)

**Content management**

You can now export content templates and fragments between sandboxes. [Learn more](../configuration/copy-objects-to-sandbox.md)

**Journeys** 

* **Live reporting enhancements** - Live Reporting provides insights into the performance of your journeys over the past 24 hours. We've enhanced it by adding new metrics (entered, exited, discarded profiles and profiles in error) allowing you to gain a deeper understanding of user behavior and performance directly from the Journey canvas. [Learn more](../building-journeys/report-journey.md)


* (Availability date: Sept 10) **Automatic retries on Read Audience** - Retries are now applied by default on audience-triggered journeys (starting with a **Read Audience** or a **Business Event**) while retrieving the export job. If an error occurs during the export job creation, retries will be made every 10mn, for 1 hour max. After that, we will consider it as a failure. Those types of journeys can therefore be executed up to 1 hour after the scheduled time. [Learn more](../building-journeys/read-audience.md#retries)

**Email channel**

* **Message header in sent email and BCC copy** - A new header has been added to all email messages. This header's value is unique to each sent email and to its corresponding BCC email copy. This header is also stored in the message and BCC feedback datasets, which allows to reconcile the BCC copy and the corresponding sent email information. [Read more](../configuration/archiving-support.md#bcc-header)

* **Spam scoring** (GA)- You can now check your content spam scoring in a dedicated **Spam report**. Using SpamAssassin, Adobe Journey Optimizer can now test your email content and give it a score to indicate if ISPs or Mailbox providers will consider it as a spam or not. [Read more](../content-management/spam-report.md)

**SMS channel**

* **Edit API Credentials** - You can now edit settings in SMS API Credentials, including updates to opt-in/out keywords and replies.

**APIs**

* **Campaign Simulation API** - Use this API to trigger proof job of a Campaign. Sending Campaign proof is an async process, the API will return a proofJobId which can be used to check the status of the proof. [Learn more](https://developer.adobe.com/journey-optimizer-apis/references/simulations/){target="_blank"}

* (Availability date: Sept 10) The [Adobe Journey Optimizer API documentation](https://developer.adobe.com/journey-optimizer-apis/references/simulations/){target="_blank"} is now interactive. Explore the API endpoints directly from the documentation pages to get immediate feedback and speed up your technical implementation. 


    All the API reference pages now have a **Try it** functionality that you can use to test API calls directly on the documentation website page. [Get the required authentication credentials](https://developer.adobe.com/journey-optimizer-apis/references/authentication/){target="_blank"} and start using the functionality to explore the API endpoints. 

    Use this new functionality to explore the requests to and the responses from API endpoints, to get immediate feedback and speed up your technical implementation. 

    >[!CAUTION]
    >
    >Be aware that by using the interactive API functionality on the documentation pages, you are making real API calls to the endpoints. Keep this in mind when experimenting with production sandboxes.

**Configuration**

* **IP warmup plans** - This capability is now available to all customers, including organizations that have purchased the Adobe **Healthcare Shield** or **Privacy and Security Shield** add-on offerings. [Learn more](../configuration/ip-warmup-gs.md)

<!--
![Newsletter](../assets/do-not-localize/nl-icon.png) Sign up for the [Adobe Journey Optimizer quarterly newsletter](https://www.adobe.com/subscription/Adobe_Journey_Optimizer_NL.html){target="_blank"} today, and receive the latest product updates, exciting stories, use cases, tips and more delivered directly to your inbox every quarter.-->



## August '24 release {#8-2024}

**Release date**: August 20-21, 2024

### New capabilities {#8-features}

This release brings the new capabilities detailed below.

<!--
<table>
<thead>
<tr>
<th><strong>Content Cards (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Content cards are a new digital messaging feature in Adobe Journey Optimizer that delivers personalized and engaging content directly within mobile apps and websites. Unlike traditional push notifications, Content Cards integrate seamlessly into the user interface, offering persistent, non-intrusive updates that enhance user interaction and experience.</p>
<p>This feature enables marketers to present relevant, rich media content to users, driving higher engagement and ensuring important messages are seen without disrupting the user journey.</p>
</br>
<p>Content card are currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table-->

<table>
<thead>
<tr>
<th><strong>Improved Channel Configurations</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The current channel surface capabilities have been enhanced for a consistent approach across all channels. You can now define, manage, and reuse these configurations for any of your channels, including Web, In-app messaging, or Code-based experience.</p>
<p><ul>
<li>Channel surfaces are now renamed to <strong>Channel configurations</strong></li>
<li>You can attach one or multiple marketing actions to enforce consent and data governance policies</li>
<li>Object level access control (OLAC) is now available for each channel configuration, allowing you to decide which of your users are allowed to create or use specific configurations</li>
<li>For some channels, you can create channel configurations that target multiple platforms. An example here would be an In-app messaging channel configuration that can target a web page, an iOS app and an Android app.</li>
</ul></p>
<p>For more information, refer to the <a href="../configuration/channel-surfaces.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Marketo Engage Custom Action</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now integrate Adobe Journey Optimizer with Adobe Marketo Engage to build your B2B use cases. From a journey, a new custom action allows you to ingest data into Marketo.</p>
<p>For more information, refer to the <a href="../action/marketo-engage.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Variables in Content Fragments</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Fragment global variables enhance the existing fragment functionality to improve efficiency for content reusability & scripting use cases. Fragments can now use input variables and create output variables usable in campaign and journey content. Fragments are able to consume input variables, both in <a href="../personalization/use-expression-fragments.md">expression fragments</a> and <a href="../email/use-visual-fragments.md">visual fragments</a>. You can use those variables to personalize your messages content and parameters, in your campaigns and journeys.</p>
<p>For more information, refer to the <a href="../personalization/use-expression-fragments.md">detailed documentation</a>.</p>
</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>IP Warmup Workflow</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Availability date: Aug, 13</p>
<p>If you are sending email on a brand new IP address, you can now easily perform IP warmup workflows directly from the user interface. Adobe Journey Optimizer offers a standardized and efficient way to warm up your IP adresses that follows the best practices for optimal deliverability.</p>
<p>For more information, refer to the <a href="../configuration/ip-warmup-gs.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#8-improvements}

This release brings the improvements listed below.

**Journeys**

* In the **Condition** activity, by default, the **[!UICONTROL Time condition]** is now set by hour, from 00:00 to 12:00. [Read more](../building-journeys/condition-activity.md#time_condition)
* When building your journeys, alerts are now displayed from the **Alerts** button, to align with other alerts and bring a consistent user experience. [Read more](../building-journeys/troubleshooting.md#checking-for-errors-before-testing)
* Zoom options in the journey toolbar have been improved: the zoom percentage is now visible and you can now more easily reset the zoom value.

**Push channel**

* You can now add your mobile application push credentials inside Adobe Journey Optimizer channel configuration settings. Creating an App surface in Adobe Experience Platform Data Collection is no longer required.

### Other changes {#changes}

**Reporting**

* New use cases have been added to the new reporting experience:

    * Create custom calculated metrics directly within your reports.
    * Create an Audience from reporting data.
    * Use the Exploratory Analysis tool to easily create tables and visualizations from your selected **[!UICONTROL Dimensions]** and **[!UICONTROL Metrics]**.

    For more information, refer to the [detailed documentation](../reports/report-cja-manage.md).



## July '24 release {#24-7-2024}

**Release date**: July 30-31, 2024

### New capabilities {#27-4-features}

This release brings the new capabilities listed below.

<table>
<thead>
<tr>
<th><strong>SMS channel with any provider (Beta)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now configure additional SMS providers within Journey Optimizer, in addition of the default providers Sinch, Infobip, and Twilio.</p>
<img src="assets/do-not-localize/byo_sms.gif"/>
<p>For more information, refer to the <a href="../sms/sms-configuration-custom.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Federated Audience Composition (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Federated Audience Composition is now available in Adobe Journey Optimizer. It allows enterprises to compose data for better utilization across various use cases. With this new approach, as a Adobe Real-Time Customer Data Platform and/or Adobe Journey Optimizer user, you can federate datasets directly from your existing data warehouse to build and enrich Adobe Experience Platform audiences and attributes all in one system.</p>
<p>For more information, refer to the <a href="https://experienceleague.adobe.com/en/docs/federated-audience-composition/using/home"  target="_blank">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

### Improvements {#27-4-improvements}

This release comes with the improvements listed below.

**Journeys**

* (Availability date: July 8) **Advanced expression editor in journey event configuration** - You can now leverage the advanced expression editor while configuring an event, allowing you to define more complex expressions or use functions in the Event ID condition. [Learn more](../event/about-creating.md#adv-exp-editor)



## June '24 release {#24-6-2024}

**Release date**: June 18-19, 2024

### New capabilities {#june-24-features}

This release brings the new capabilities detailed below.

<table>
<thead>
<tr>
<th><strong>Content Fragments customization</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now define specific fields in a fragment that can be edited when the fragment is added to a campaign or journey. This allows for the adjustment of content portions at the time of use, providing flexibility to override default values with context-specific details.</p>
<img src="../content-management/assets/do-not-localize/gif-fragments.gif"/>
<p>For more information, refer to the <a href="../content-management/customizable-fragments.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Reporting with Customer Journey Analytics (Limited availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer reporting comes with an improved interoperability with Customer Journey Analytics capabilities, standardizing reporting across both platforms and improving data consistency and reliability. This seamless integration between Journey Optimizer and Customer Journey Analytics provides a clearer view of performance metrics, enabling users to make more informed decisions.</p>
<img src="assets/do-not-localize/ajo-cja.gif"/>
<p>For more information, refer to the <a href="../reports/report-gs-cja.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>AI Assistant in Adobe Journey Optimizer</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>The AI Assistant is a user interface feature that you can use to navigate and understand Adobe concepts and get operational insights for your specific environment. It is available in several products across Adobe Experience Cloud, including Adobe Journey Optimizer.</p>
<p>For more information, refer to the <a href="../start/ai-assistant.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Multilingual messages in journeys and campaigns (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now effortlessly create content in multiple languages within a single campaign or journey. With this feature, you can switch between languages when editing your campaign or your journey, streamlining the entire editing process and improving your capability to efficiently manage multilingual content.</p>
<p>Multilingual content is currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Experimentation in journeys (Limited Availability)</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Already available in campaigns, Adobe Journey Optimizer now supports experiments in journeys. Experiments are randomized trials, which in the context of online testing, means that you expose some randomly selected users to a given variation of a message, and another randomly selected set of users to some other variation or treatment. After exposure, you can then measure the outcome metrics you are interested in, such as opens of emails, subscriptions, or purchases.</p>
<p>Experimentation in journeys is currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
</td>
</tr>
</tbody>
</table>

<!--table>
<thead>
<tr>
<th><strong>Extended personalization data - Beta</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now lookup and fetch data values within Adobe Experience Platform datasets, and use these values to build conditions in Adobe Journey Optimizer. You can leverage data from a lookup dataset when a relationship has been defined using an attribute inside of an array of objects. You can specify non-profile enabled datasets for lookup. Once enabled, you can use a profile attribute as a join key to the specified dataset to retrive further data for personalization.</p>
<p>This capability is currently available as a public beta.</p>
</td>
</tr>
</tbody>
</table-->

### Improvements {#june24-improvements}

This release comes with the improvements listed below.

#### Decision Management

* **Multi-rule support in Decision Management** - You can now add up to 10 capping rules for a given offer in Decision Management. This allows you to increase the level of control over the way offers are sent. [Learn more](../offers/offer-library/add-constraints.md#capping)

<!--* **Audits** - The **Change log** tab allowing you to see all the changes that have been made to an offer or a decision has been removed. Changes related to offers and decisions can now be seen in the **Audits** menu. -->

#### Content fragments

>[!AVAILABILITY]
>
>Please note that these enhancements will be rolled out gradually over the course of several days following the initial release. While some users will have immediate access, others may experience a delay before it becomes available in their environments.

* Fragments can now be edited, and changes can be propagated across all live journeys and campaigns where they are used.
* New statuses for content fragments have been introduced: **Draft**, **Live**, **Publishing**, and **Archived**. 
* To use a fragment in a journey or campaign, it must now be in the **Live** status. A new step has been added to the fragment creation process, allowing the fragment to be published and made available for use in journeys and campaigns. Note that fragment publishing requires a new permission.
   
   **CAUTION** - Since **Draft** and **Live** statuses have been introduced with Journey Optimizer June release, all fragments created before this release have the **Draft** status, even if they are used in a journey or campaign. If you make any change to these fragments, you need to [publish them](../content-management/create-fragments.md#publish) to make them "Live" and propagate the changes to the associated campaigns and journeys. You also need to create a new journey/campaign version and publish it.

Read more in the [content fragment](../content-management/fragments.md) documentation.

#### Journeys

* Global timeout of Journeys has been extended to 91 days. [Read more](../building-journeys/journey-properties.md#global_timeout)

    Any new journeys created will have this new timeout reflected. Please refer to this [FAQ section](../building-journeys/journey-properties.md#timeout-faq) to learn more. Please note these changes will be rolled out gradually over the course of the month of June.


* Adobe Journey Optimizer now supports privacy delete/access requests as well as data life cycle management requests. [Read more](../privacy/requests.md)
* You can now resize the columns in the journey inventory.
<!--* **Advanced expression editor in Event configuration** is now GA - You can now leverage the advanced expression editor while configuring an event, allowing you to define more complex expressions or use functions in the event id condition. This capability is released in Limited Availability for selected customers. [Read more](../event/about-creating.md)-->
* **Merge policies** are now GA - Merge policies used by a Journey are now visible and consistent throughout the journey. [Read more](../building-journeys/journey-properties.md#merge-policies)


#### Campaigns

* When creating a campaign in Adobe Journey Optimizer, you can now choose the campaign type (scheduled or triggered) in a new modal. [Read more](../campaigns/create-campaign.md)

#### Email channel

* **List-unsubscribe** - Following on the recent Gmail and Yahoo announcements for bulk senders, Journey Optimizer supports the "post/1-click" List-Unsubscribe option. Refer to the following pages: [Email opt-out management](../email/email-opt-out.md#unsubscribe-header) and [Configure email settings](../email/email-settings.md#list-unsubscribe).

    **NOTE** - For any new channel surface, by default the list unsubscribe header option is activated. For existing surfaces, by default the One-click unsubscribe URL option in the channel surface settings is unchecked. If you were using a one-click opt out URL in the body of the email previously, this setting is still valid. If the One-click unsubscribe URL in the channel surface settings is checked, Adobe Journey Optimizer will rather use the default generated One-click unsubscribe URL in the channel surface settings.

#### SMS channel

* You can now add unique short codes for each sandbox with a single API configuration, making the process more efficient and streamlined. [Learn more](../sms/sms-configuration.md)

* After creation, the **API Token** field on the **API credential details** page is now masked.

<!--* You can now modify existing SMS configurations.-->

#### In-app channel

<!--* **Expression fragment** - Expression fragments are now available for the **In-app channel**. [Read more](../personalization/use-expression-fragments.md)-->

* You can now use the Edge Delivery plugin to get information needed to understand and troubleshoot your inbound implementations. [Learn more on Edge Delivery view](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/view/edge-delivery){target="_blank"}.


#### Direct mail channel

* Direct mail channel is now available for all customers. [Read more](../direct-mail/get-started-direct-mail.md)



## May '24 release {#may-2024}

**Release date**: May 21-22, 2024

### New capabilities {#e-features}

This release brings the new capabilities detailed below.

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
<p>These decision items are seamlessly integrated into a wide range of inbound configurations through the new code-based experience channel, now accessible within Journey Optimizer campaigns. Experience Decisioning decision policies are available for use in code-based experience campaigns only.</p>
<p>Experience Decisioning is currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<img src="assets/do-not-localize/gif-exd.gif"/>
<p>For more information, refer to the <a href="../experience-decisioning/gs-experience-decisioning.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Email configuration personalization - Limited Availability</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now define dynamic subdomains and personalized header parameters when creating email channel configurations, for increased flexibility and control over your email settings.</p>
<p>Email configuration personalization is currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../email/surface-personalization.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table>

<!--table>
<thead>
<tr>
<th><strong>IP Warmup Workflow</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>If you are sending email on a brand new IP address, you can now easily perform IP warmup workflows directly from the user interface. Adobe Journey Optimizer offers a standardized and efficient way to warm up your IP adresses that follows the best practices for optimal deliverability.</p>
<p>For more information, refer to the <a href="../configuration/ip-warmup-gs.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table-->

<!--table>
<thead>
<tr>
<th><strong>Business rules - Beta</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now create granular frequency capping rules, and apply them to different types of marketing communications through rule sets. This new capability lets you control how often your audiences receive a message by setting cross-channel rules, that automatically exclude over-solicited profiles from messages and actions.</p>
<p>Business rules capability is currently available as a beta. To join the beta program, contact your Adobe representative.</p>
<p>For more information, refer to the <a href="../configuration/business-rules.md">detailed documentation</a>.</p>
</td>
</tr>
</tbody>
</table-->


<!--table>
<thead>
<tr>
<th><strong>Extended personalization data - Beta</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now lookup and fetch data values within Adobe Experience Platform datasets, and use these values to build conditions in Adobe Journey Optimizer. You can leverage data from a lookup dataset when a relationship has been defined using an attribute inside of an array of objects. You can specify non-profile enabled datasets for lookup. Once enabled, you can use a profile attribute as a join key to the specified dataset to retrive further data for personalization.</p>
<p>This capability is currently available as a public beta.</p>
</td>
</tr>
</tbody>
</table-->

### Improvements {#e-improvements}

This release comes with the improvements listed below.

**Experience Decisioning** (Limited Availability)

From beta to this release, the following improvements have been added:

* **Experience Decisioning + Code-based experiences** - You can now leverage the Experience decisioning feature to use decision items in your code-based campaigns. Note: The Code-based experience channel and Experience decisioning are not available for organizations that have purchased the Adobe Healthcare Shield and Privacy and Security Shield add-on offerings. [Read more](../code-based/get-started-code-based.md)
* **Context data** - You can now leverage context data from Adobe Experience Platform in your decision rules and rankign formulas. [Read more](../experience-decisioning/context-data.md)
* **New permission** - A new 'Manage Experience decisions' permission is now available for the Decision Management resource. It allows you to manage rights related to Experience Decisioning. [Read more](../experience-decisioning/gs-experience-decisioning.md)
* **Capping rules** - You can now add multiple capping rules for a given decision item in Experience Decisioning. This allows you to increase the level of control over the way offers are sent. [Read more](../experience-decisioning/items.md#capping)
* **Reporting** - You can now create custom reporting dashboards of Experience Decisioning campaigns using [!DNL Customer Journey Analytics]. [Read more](../experience-decisioning/cja-reporting.md)


<!--**Decision Management**

* **Multi-rule support** - You can now add up to 10 capping rules for a given offer in Decision Management. This allows you to increase the level of control over the way offers are sent.
* **Audits** - The **Change log** tab allowing you to see all the changes that have been made to an offer or a decision has been removed. Changes related to offers and decisions can now be seen in the **Audits** menu. -->


**Email channel**

<!--
* **List-unsubscribe** - Following on the recent Gmail and Yahoo announcements for bulk senders, Journey Optimizer supports the "post/1-click" List-Unsubscribe option. Refer to the following pages: [Email opt-out management](../email/email-opt-out.md#unsubscribe-header) and [Configure email settings](../email/email-settings.md#list-unsubscribe)
-->

* **Spam scoring** (Beta) - You can now check your content spam scoring in a dedicated Spam report. Using SpamAssassin, Adobe Journey Optimizer can now test your email content and give it a score to indicate if ISPs or Mailbox providers will consider it as a spam or not. [Read more](../content-management/spam-report.md)

   >[!AVAILABILITY]
   >
   >This capability is currently in beta version and only available to beta customers. To join the beta program, contact your Adobe representative.

<!--
**Audiences**

* The use of audiences and attributes from audience composition and custom upload (CSV file) is now available for use with Healthcare Shield or Privacy and Security Shield.-->

<!--**Personalization**

* **Expression fragment** - Expression fragments are now available for the **In-app channel**. [Read more](../personalization/use-expression-fragments.md)-->

**Journeys**

<!--* **Merge policies** (Limited Availability)- Merge policies used by a journey are now visible and consistent throughout the journey.-->
* **mTLS support** - mTLS authentication is now supported in custom actions. There is no additional configuration required in the custom action or journey to activate mTLS; it occurs automatically when an mTLS-enabled endpoint is detected. [Read more](../action/about-custom-action-configuration.md#mtls-protocol-support)
* **Lookup tables in events** - You can now leverage data from a lookup dataset when a relationship has been defined using an attribute inside of an array of objects. The lookup values will be available in journeys (conditions, custom actions, etc.) and message personalization. [Read more](../event/experience-event-schema.md#relationships_limitations)
* **Advanced expression editor in Event configuration** (LA) - You can now leverage the advanced expression editor while configuring an event, allowing you to define more complex expressions or use functions in the event id condition. This capability is released in Limited Availability for selected customers. [Read more](../event/about-creating.md#adv-exp-editor)
* **Merge policies** (LA) - Merge policies used by a Journey are now visible and consistent throughout the journey. This capability is released in Limited Availability for selected customers. [Read more](../building-journeys/journey-properties.md#merge-policies)

**Globalization**

As part of our ongoing effort to deliver a unified user experience, we harmonize the terminology used in the Adobe Experience Cloud products and apps. This affects the German term "Titel" which is changed to "Label" when it relates to the name of an object. The changes will be progressively rolled out in the UI and documentation.


## April '24 release {#apr-2024}

**Release date**: May 2, 2024

### New capabilities {#apr-features}

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
<p>Once you have created and personalized your message, take your content to the next level with the AI Assistant. You can now use the AI Assistant to optimize your message's impact by experimenting with different main titles, and images. Each variant is managed as a unique Treatment, to measure and compare which title effectively generates more clicks.</p>
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
<p>You can now define dynamic subdomains and personalized header parameters when creating email channel configurations, for increased flexibility and control over your email settings.</p>
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
* **DULE for AJO channel configuration**: It is now possible to apply a label on certain profile attributes to restrict their usage inside a channel configuration through marketing actions.
-->


<!--
* **List-Unsubscribe updates**: Following on the recent Gmail and Yahoo announcements for bulk senders, Journey Optimizer supports the "post/1-click" List-Unsubscribe option. 
-->

**Configuration**

* You can now select a marketing action at the channel configuration level. When used in a configuration, all consent policies associated with that marketing action are leveraged in order to respect the preferences of your customers. [Read more](../action/consent.md#surface-marketing-actions)
* The use of Object Level Access Control is now available for channel configurations. [Read more](../configuration/channel-surfaces.md#create-channel-surface)
* While enabling list unsubscribe in a channel configuration, you can now define the consent level to align with how you manage consent from all other sources. [Read more](../email/email-settings.md#list-unsubscribe)

**Content management**

* You can now simulate content templates for all channels. [Read more](../content-management/content-templates.md#test-templates)

**Personalization**

* The new **toInt** helper function is available in the Expression Editor. It allows you to convert any of these types (number, double, int, long, float, short, byte, boolean, string) into an integer. [Read more](../personalization/functions/math.md#to-int)



## March '24 release {#mar-2024}

**Release date**: March 19-20, 2024

### New capability {#mar-features}

This release brings the new capability detailed below.

<table>
<thead>
<tr>
<th><strong>Code-based experiences</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With the new Code-based experience channel, Adobe Journey Optimizer allows you to do advanced personalization and testing for any of your inbound properties, enabling seamless delivery of tailored experiences across diverse touchpoints such as web apps, mobile apps, desktop apps, video consoles, TV connected devices, smart TVs, kiosks, ATMs, IoT devices, and more.</p>
<P>Key capabilities include:</p>
<ul><li> Universal personalization: extend personalized experiences across all touchpoints, ensuring a cohesive and tailored user journey</li>
<li>Granular editing precision: edit specific content at individual locations within your apps or web pages</li>
<li>Versatile implementation: support for server-side, API-based, or SDK-based implementation methods to seamlessly integrate with your development environment.</li></ul></p>
<p>For more information, refer to the <a href="../code-based/get-started-code-based.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/code-based.gif"> 
</tr>
</tbody>
</table>

### Improvements {#mar-improvements}

This release comes with the improvements listed below.

**Content templates**

* **Thumbnails** - A **Grid view** mode is now available for content templates, displaying thumbnails for improved visual access. Currently only email HTML templates are supported. [Learn more](../content-management/content-templates.md#template-thumbnails)

   >[!AVAILABILITY]
   >
   >This capability is released in Limited Availability (LA) for a small set of customers.

**Journeys**

New intermediate statuses have been added to the journey authoring lifecycle:

* **Publishing** status between the **Draft** status and the **Live** status
* **Stopping** status between the **Live** status and the **Stopped** status
* **Activating test mode** or **Deactivating test mode** statuses between the **Draft** status and the **Draft (test)** status

When a journey is in an intermediate state, it is read-only. [Learn more](../building-journeys/journey-gs.md#filter)

## February '24 release {#feb-2024}

**Release date**: Feb 21-22, 2024

### New capabilities{#feb-features}

This release brings the new capabilities listed below.


<table>
<thead>
<tr>
<th><strong>Web In-App Messaging</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>You can now use the new Web In-App messaging capability to display personalized content directly on websites, through modal-overlay messages. This feature enables you to engage effectively with web visitors, enhancing user interaction, retention, and conversion rates.<br/><br/></p>
<p>For more information, refer to the <a href="../in-app/create-in-app-web.md">detailed documentation</a>.<br></br></p>
<img src="assets/do-not-localize/web_inapp.gif">
</tr>
</tbody>
</table>


<table>
<thead>
<tr>
<th><strong>Multi-channel content templates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>In addition to Email, content templates are now available for the following channels: Push, In-app, SMS and Direct mail, each channel having dedicated template types. For Email, you can now select the Content type, which allows you to save the subject line as part of your email template. <br/><br/></p>
<p>For more information, refer to the <a href="../content-management/content-templates.md">detailed documentation</a>.<br></br></p>
<img src="assets/do-not-localize/multi-chan-templates.gif"> 
</tr>
</tbody>
</table>


### Improvements {#feb-improvements}

This release comes with the improvements listed below.

**Audiences**

* **Seed lists** - Variants are now supported when using **seed lists**. The seed addresses receive a copy of all the variants of the same message (such as the different treatments of a content experiment). [Read more](../configuration/seed-lists.md)

Previously available as Beta, the following improvements are now available to all users:

* You can now target **audiences created through audience composition** and leverage enrichment attributes in Journeys. [Learn more](../building-journeys/read-audience.md)

* You can now target **audiences uploaded from a CSV file** into journeys and campaigns. [Learn more](../audience/about-audiences.md#segments-in-journey-optimizer)

   >[!AVAILABILITY]
   >
   >* The use of audiences and attributes from audience composition and custom upload (CSV file) is currently unavailable for use with Healthcare Shield or Privacy and Security Shield.
   >* The **audience upload from a CSV file** improvement is being rolled out gradually over the course of several days following the initial release. While some users have immediate access, others may experience a delay before it becomes available in their environment.

**Journeys**

* **Filter your journeys** - You can now use **custom dates to filter the journeys** inventory, in addition to the existing predefined date filters. This allows you to refine the list by displaying journeys created or published on a specific date, within a particular month, throughout an entire year, or within specified time ranges. [Read more](../building-journeys/journey-gs.md#filter)
* **Custom actions** - You can now update the **content-type** header. This new **content-type** should reference JSON content. [Read more](../action/about-custom-action-configuration.md#url-configuration)
* **Configuration** - The identityMap attribute in stepEvents is now pre-filled. The primary identity is defined as "primary = true". [Read more](../reports/sharing-field-list.md)
* **User interface** - The top bar, in journey screens, has been reorganised for an improved experience. Among the different updates, notice that the "pencil" icon that allows you to access the journey properties is now displayed on the left of the top bar, next to the journey's name. [Read more](../building-journeys/journey-properties.md)

**SMS channel**

* **Opt-in/opt-out keywords** - When configuring your SMS channel, you can now customize the **Opt-in and Opt-out keywords** as per your preferences. Journey Optimizer triggers the response based on these specified keywords. [Learn more](../sms/sms-configuration.md)

**Campaigns**

* **API-triggered campaigns** - The cURL code generated after activating an API-triggered campaign has been enhanced. It now includes all personalizaton (profile and context) variables used in the message. [Read more](../campaigns/api-triggered-campaigns.md#execute) 

**Frequency rules**

* In addition to Email and Push, you can now create Frequency rules for SMS and Direct Mail channels. Frequency rules automatically exclude over-solicited profiles from messages and actions when the frequency cap is reached. [Read more](../configuration/rule-sets.md) 

<!--**Decision management**

* **Capping rules** - You can now add **multiple capping rules** for one offer. This allows you to increase the level of control over the way offers are sent.-->


## January '24 release {#jan-2024}

**Release date**: Jan 30-31, 2024

### New capabilities{#jan24-features}

This release brings the new capabilities listed below.

<table>
<thead>
<tr>
<th><strong>Deliverability Updates</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Journey Optimizer now supports the DMARC authentication technology.</p>
<p>Starting February 1st, 2024, Google and Yahoo! are requiring that you have a DMARC record for any domain you use to send email to them. Make sure that you have DMARC record set up for all the subdomains that you have delegated or are delegating to Adobe in Journey Optimizer.</p>
<p>For more information, refer to the <a href="../configuration/dmarc-record-update.md">detailed documentation</a>.</p>
<br/><img src="assets/do-not-localize/dmarc.gif"/>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Use Case Playbooks</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Leverage a catalog of industry-specific use case playbooks in Real-Time CDP and Journey Optimizer to address common use cases that you can perform using Adobe Experience Platform and Adobe Journey Optimizer.</p><p>Once you have chosen the playbook that best fits your needs, you can enable it to generate the assets needed to support your use case such as journeys, messages, schemas or segments, and customize them to your schema for faster time to value.</p>
<p>For more information, refer to the <a href="../start/playbooks.md">detailed documentation</a>.</p>
<br/><img src="assets/do-not-localize/playbooks.gif"/>
</tr>
</tbody>
</table>

### Improvements {#jan24-improvements}

This release comes with the improvements listed below.

**Reporting**
 
* **New domain based breakdown widgets** - New widgets have been added to enhance your Campaign and Journey reports. The **Bounce Reasons by domain**, **Sent & delivered by domains**, **Opens & Clicks by domain** and **Bounce & errors by domain** widgets provide a detailed breakdown at the domain level for key email delivery and tracking metrics. [Learn more](../reports/channel-report-cja.md) 

**SMS Channel**

* **Double Opt-In** - The Double Opt-In workflow for SMS guarantees that users explicitly opt-in to receive messages when the request is initiated from their device. Users initiate the consent process by sending an inbound SMS message. Upon confirming their consent, a follow-up message is sent, requesting final verification. If a user profile does not exist, it is created upon successful confirmation. [Learn more](../sms/sms-configuration.md) 

   Note that this capability is available with Sinch and Infobip SMS providers.

**Journeys**

* **Reaction events duration** - The maximum duration that you can define in the **Reaction events** is now 29 days instead of 30. [Learn more](../building-journeys/reaction-events.md)

<!--* **Date filters** - You can now use custom dates to filter the journeys inventory, in addition to the existing predefined date filters. This allows you to refine the list by displaying journeys published on a specific date, within a particular month, throughout an entire year, or within specified time ranges. [Learn more](../building-journeys/journey-gs.md#filter)-->

* **Read audience**  - The **Read Audience** activity now relies on the profile snapshot dataset for batch segments, which is only generated once a day after the scheduled daily batch job is run, hence the data will be fresh up to that last daily batch job. [Learn more](../building-journeys/read-audience.md)

* **Field Groups** - This release fixes an issue which was blocking Field Groups from being saved in certain cases.

* Support of `<listObject>` has been modified in multiple functions.

**Frequency Rules**

* **Weekly frequency cap** - You can now specify the maximum number of messages sent to a customer profile per week, in addition to month. The frequency cap is based on the selected calendar period and reset at the beginning of the corresponding time frame. [Learn more](../configuration/rule-sets.md) 

   >[!NOTE]
   >
   >Daily frequency cap is also available on demand. Contact your Adobe representative.

**Decision management**

* **Frequency capping on Edge** - The frequency capping counter is now updated and available in an Edge Decisioning API decision in less than 3 seconds. [Learn more](../offers/api-reference/offer-delivery-api/start-offer-delivery-apis.md)
