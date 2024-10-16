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

## October '24 updates {#24-10-rn}

Upcoming **release date**: October 28-30, 2024

The [capabilities](#24-10-features) and [improvements](#24-10-improvements) listed below have been released this month.

### New capabilities {#24-10-features}

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
<p>Availability date: Oct 1, 2024</p>
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
<p>Availability date: Oct 1, 2024</p>
</tr>
</tbody>
</table>

### Improvements {#24-10-improvements}

**Journeys** -  Availability date: Oct 3, 2024

* **Parameters in custom actions** - NULL and optional parameters are now supported in custom actions. [Learn more](../action/about-custom-action-configuration.md#define-the-message-parameters)

**Data governance & Consent policies** - Availability date: Oct 7, 2024
  
* **Data governance policies** enforcement now takes place across all channels in Journey Optimizer. For customers that have created  policies in Adobe Experience Platform, these are applied to marketing actions as part of the channel configurations setup. When you create content using a configuration, the system checks all the personalization fields for any data governance violations. If a violation is found, publishing a journey or campaign will not be possible. [Learn more](../action/action-privacy.md)

* **Custom consent policies** now apply to all Journey Optimizer channels. On enforcement before a message is sent or an inbound experience is delivered, the system checks that the user has given consent to use personalization fields in the content that they will receive. If no consent is given, the experience will not be displayed. [Learn more](../action/consent.md)

    >[!NOTE]
    >
    >Consent policies are currently only available for organizations that have purchased the Adobe **Healthcare Shield** or **Privacy and Security Shield** add-on offerings.

**Audiences** -  Availability date: Oct 8, 2024

* When targeting a CSV file audience, you can now use attributes from the file in the personalization editor and in journeys and campaigns rule builer. [Learn more](../audience/about-audiences.md)

* The use of audiences and attributes from custom upload (CSV file) is now available for use with Healthcare Shield or Privacy and Security Shield.

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
<th><strong>AI Assistant Content Accelerator </strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>Once you have created and personalized your message, take your content to the next level with the AI Assistant in Journey Optimizer for Content Acceleration. You can now use the AI assistant to optimize your message's impact by experimenting with different main titles, and images. Each variant is managed as a unique Treatment, to measure and compare which title effectively generates more clicks.</p>
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

>[!IMPORTANT]
>
>The current reporting experience will be retired as of January 2025. After this date, the new reporting experience will become the standard. We recommend familiarizing yourself with the new features and functionalities to ensure a smooth transition.
>
> [Learn how to get started with Journey Optimizer new Reporting interface](../reports/report-gs-cja.md)


### Improvements {#24-9-improvements}

This release comes with the improvements listed below.

**Audiences** - Availability date: Sept 17, 2024

<!--* The use of audiences from custom upload (CSV file) is now available for use with Privacy and Security Shield add-on.-->
* **License usage** - The License usage dashboard now shows the Engageable Profiles, instead of Engageable Audiences. [Learn more](../audience/license-usage.md)

**Content management**

* You can now export content templates and fragments between sandboxes. [Learn more](../configuration/copy-objects-to-sandbox.md)

<!--**Data Governance**

* You can now apply data governance policies to Journey Optimizer channels, in addition to custom actions within journeys. This enhancement helps prevent the use of sensitive fields in communications by applying marketing actions directly within your channel configurations.    -->

<!--
**Conflict and priority management**

* **Priority score** - You can now assign a priority score to a campaign or a journey, ranging from 0 to 100. A higher number indicates a higher priority. When two campaigns or journeys use the same surface, Journey Optimizer will select the one with the highest priority score. If the campaigns have the same score, the campaign that was most recently modified will be chosen. Priority score is available for all inbound channels in campaigns, and for the in-app channel in journeys.    

* **View conflicts** - A new **View conflicts** button in journeys and campaigns now allows you to check whenever there's a possibility of overlap with other journeys or campaigns such as the start date, the targeted audience, or the selected channel configuration.
-->

**Journeys** 

<!-- DOCAC-10977 * **Max number of Live journeys** - Journey Optimizer now has a guardrail of 500 live journeys on production sandboxes, instead of 100. The number of live journeys is visible in the journey canvas.-->

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


![Newsletter](../assets/do-not-localize/nl-icon.png) Sign up for the [Adobe Journey Optimizer quarterly newsletter](https://www.adobe.com/subscription/Adobe_Journey_Optimizer_NL.html){target="_blank"} today, and receive the latest product updates, exciting stories, use cases, tips and more delivered directly to your inbox every quarter.