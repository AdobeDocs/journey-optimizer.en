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

[!DNL Adobe Journey Optimizer] continuously delivers new features, enhancements to existing features, and bug fixes. All changes are consolidated on the last week of each month in these release notes. 

[!DNL Adobe Journey Optimizer] is built natively on [!DNL Adobe Experience Platform] and inherits from its latest innovations and improvements. Learn more about these changes in [Adobe Experience Platform Release Notes](https://experienceleague.adobe.com/docs/experience-platform/release-notes/latest.html){target="_blank"}.

![Newsletter](../assets/do-not-localize/nl-icon.png) Sign up for the [Adobe Journey Optimizer quarterly newsletter](https://www.adobe.com/subscription/Adobe_Journey_Optimizer_NL.html){target="_blank"} today, and receive the latest product updates, exciting stories, use cases, tips and more delivered directly to your inbox every quarter.

## September updates {#9-2024}

>[!IMPORTANT]
>
>The current reporting experience will be retired as of October release. After this date, the new reporting experience will become the standard. We recommend familiarizing yourself with the new features and functionalities to ensure a smooth transition.
> [Get started with Journey Optimizer new Reporting interface](../reports/report-gs-cja.md)

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

**Journeys** 

(Availability date: Sept 10) **Retry capability** - Retries are now applied by default on audience-triggered journeys (starting with a **Read Audience** or a **Business Event**) while retrieving the export job. If an error occurs during the export job creation, retries will be made every 10mn, for 1 hour max. After that, we will consider it as a failure. Those types of journeys can therefore be executed up to 1 hour after the scheduled time. [Learn more](../building-journeys/read-audience.md#retries)

## August 2024 release notes {#8-2024}

**Release date**: August 20-21, 2024

<!--
>[!CAUTION]
>
>**Early release notes below are subject to change without prior notice until the release date**. Links, screens and updated documentation are published at the release date.
>
-->

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

<!--**Audiences and Profiles**-->

<!--* The use of audiences from custom upload (CSV file) is now available for use with Privacy and Security Shield add-on.-->
<!--* When targeting a custom upload (CSV file) audience, you can now use attributes from the file in your campaigns and journeys. These attributes are available in the personalization editor, to personalize your messages, and the journey advanced expression editor.-->
<!--* The License usage dashboard now shows the count of Engageable Profiles. [Read more](../audience/license-usage.md)-->

**Push channel**

* You can now add your mobile application push credentials inside Adobe Journey Optimizer channel configuration settings. Creating an App surface in Adobe Experience Platform Data Collection is no longer required.

### Other changes {#changes}

**Reporting**

* New use cases have been added to the new reporting experience:

    * Create custom calculated metrics directly within your reports.
    * Create an Audience from reporting data.
    * Use the Exploratory Analysis tool to easily create tables and visualizations from your selected **[!UICONTROL Dimensions]** and **[!UICONTROL Metrics]**.

    For more information, refer to the [detailed documentation](../reports/report-cja-manage.md).
