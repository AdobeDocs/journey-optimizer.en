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

## September 2024 early release notes {#e-2024}

**Release date**: September 24-25, 2024

### New capabilities {#e-features}

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
<!--p>For more information, refer to the <a href="../content-management/gs-generative.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/ai-content.gif"/-->
</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Approvals in journeys and campaigns</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With approval policies, you can now set up an approval process within Journey Optimizer that allows marketing teams to ensure campaigns and journeys are reviewed and signed off by the appropriate stakeholders before they go live.</p>
<!--p>For more information, refer to the <a href="../content-management/gs-generative.md">detailed documentation</a>.</p>
<img src="assets/do-not-localize/ai-content.gif"/-->
</td>
</tr>
</tbody>
</table>


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
<th><strong>Code-based experiences in journeys</strong><br/></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>With the Code-based experience channel, Adobe Journey Optimizer allows you to do advanced personalization and testing for any of your inbound properties, enabling seamless delivery of tailored experiences across diverse touchpoints such as web apps, mobile apps, desktop apps, video consoles, TV connected devices, smart TVs, kiosks, ATMs, IoT devices, and more. The Code-based experience channel is now available in the journey canvas.</p>
<p>For more information, refer to the <a href="../code-based/get-started-code-based.md">detailed documentation</a>.</p>
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
<p>Availability date: Sept 12</p>
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
<p>Availability date: Sept 3</p>
</br>
</td>
</tr>
</tbody>
</table>

>[!IMPORTANT]
>
>The current reporting experience will be retired as of October release. After this date, the new reporting experience will become the standard. We recommend familiarizing yourself with the new features and functionalities to ensure a smooth transition.
> [Get started with Journey Optimizer new Reporting interface](../reports/report-gs-cja.md)


### Improvements {#e-improvements}

This release comes with the improvements listed below.

**Audiences**

* The use of audiences from custom upload (CSV file) is now available for use with Privacy and Security Shield add-on.
* When targeting a custom upload (CSV file) audience, you can now use attributes from the file in your campaigns and journeys. These attributes are available in the personalization editor, to personalize your messages, and the journey advanced expression editor.
* (Availability date: Sept 17) **License usage** - The License usage dashboard now shows the Engageable Profiles, instead of Engageable Audiences. [Learn more](../audience/license-usage.md)

**Data Governance**

* You can now apply data governance policies to Journey Optimizer channels, in addition to custom actions within journeys. This enhancement helps prevent the use of sensitive fields in communications by applying marketing actions directly within your channel configurations.    


**Frequency and priority management**

* **Frequency capping by campaign or journey** - You can now create frequency rules to apply to your journeys, allowing you to limit the number of journeys per day, week, or month, as well as control the number of concurrent journeys running simultaneously.

* **Priority score** - You can now assign a priority score to a campaign or a journey, ranging from 0 to 100. A higher number indicates a higher priority. When two campaigns or journeys use the same surface, Journey Optimizer will select the one with the highest priority score. If the campaigns have the same score, the campaign that was most recently modified will be chosen. Priority score is available for all inbound channels in campaigns, and for the in-app channel in journeys.    

* **View conflicts** - A new **View conflicts** button in journeys and campaigns now allows you to check whenever there's a possibility of overlap with other journeys or campaigns such as the start date, the targeted audience, or the selected channel configuration.

**Journeys** 

* **Global exit criteria** - You can now define and combine exit criteria rules for your journeys.

* **Max number of Live journeys** - Journey Optimizer now has a guardrail of 500 live journeys on production sandboxes, instead of 100. The number of live journeys is visible in the journey canvas.

* **Journey Live reporting** - Live Reporting provides insights into the performance of your journeys over the past 24 hours. We've enhanced it by adding new metrics (entered, exited, discarded profiles and profiles in error) allowing you to gain a deeper understanding of user behavior and performance directly from the Journey canvas.    

* (Availability date: Sept 10) **Retry capability** - Retries are now applied by default on audience-triggered journeys (starting with a **Read Audience** or a **Business Event**) while retrieving the export job. If an error occurs during the export job creation, retries will be made every 10mn, for 1 hour max. After that, we will consider it as a failure. Those types of journeys can therefore be executed up to 1 hour after the scheduled time. [Learn more](../building-journeys/read-audience.md#retries)

**Email channel**

* **BCC message header** - A new header has been added to all email messages. This header's value is unique to each sent email and to its corresponding BCC email copy. This header is also stored in the message and BCC feedback datasets, which allows to reconcile the BCC copy and the corresponding sent email information.

**SMS channel**

* You can now modify existing SMS configurations

**APIs**

* The [Adobe Journey Optimizer API documentation](https://developer.adobe.com/journey-optimizer-apis/references/simulations/){target="_blank"} is now interactive. Explore the API endpoints directly from the documentation pages to get immediate feedback and speed up your technical implementation. 

    All the API reference pages now have a **Try it** functionality that you can use to test API calls directly on the documentation website page. [Get the required authentication credentials](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication){target="_blank"} and start using the functionality to explore the API endpoints. 

    Use this new functionality to explore the requests to and the responses from API endpoints, to get immediate feedback and speed up your technical implementation. 

    >[!CAUTION]
    >
    >Be aware that by using the interactive API functionality on the documentation pages, you are making real API calls to the endpoints. Keep this in mind when experimenting with production sandboxes.


* **Campaign Simulation API** - Use this API to trigger proof job of a Campaign. Sending Campaign proof is an async process, the API will return a proofJobId which can be used to check the status of the proof. [Learn more](https://developer.adobe.com/journey-optimizer-apis/references/simulations/){target="_blank"}

