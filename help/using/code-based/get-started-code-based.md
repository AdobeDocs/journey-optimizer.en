---
title: Get started with code-based experiences
description: Learn about code-based experiences in Journey Optimizer
feature: Code-based Experiences
topic: Content Management
role: User, Developer, Admin
level: Experienced
exl-id: 987de2bf-cebe-4753-98b4-01eb3fded492
---
# Get started with code-based channel {#get-sarted-code-based}

>[!AVAILABILITY]
>
>For now, the Code-based experience channel is not available for organizations that have purchased the Adobe **Healthcare Shield** and **Privacy and Security Shield** add-on offerings.

[!DNL Journey Optimizer] allows you to personalize and test the experiences you want to deliver to your customers across all your touchpoints like: web apps, mobile apps, desktop apps, video consoles, TV connected devices, smart TVs, kiosks, ATMs, voice assistants, IoT devices, etc.

With the **code-based experience** capability, you can define inbound experiences using a simple and intuitive non-visual editor. It allows you to insert and edit specific elements at individual and more granular locations of your apps or web pages, no matter the type of applications you have - rather than applying modifications to an entire content.

<!--[!DNL Journey Optimizer] allows you to compose and deliver content on any inbound surface in a developer-focused workflow. You can leverage all the personalization capabilities, and preview what will be published. The content can be static (images, text, JSON, HTML) or dynamic (offers, decisions, recommendations). You can also insert custom content actions in your omni-channel journeys.-->

>[!CAUTION]
>
>Currently in [!DNL Journey Optimizer] you can only create code-based experiences using **campaigns**.

When you [create a campaign](../campaigns/create-campaign.md#configure), select **Code-based experience** as your action and define basic settings.

>[!NOTE]
>
>If this is your first time creating a code-based experience, make sure you follow the prerequisites described in [this section](code-based-prerequisites.md).

<!--Discover the detailed steps to create a code-based campaign in this video.-->

<table style="table-layout:fixed"><tr style="border: 0;">
<td>
<a href="#how-it-works">
<img alt="Lead" src="../assets/do-not-localize/privacy-audit.jpeg">
</a>
<div><a href="#how-it-works"><strong>How it works</strong>
</div>
<p>
</td>
<td>
<a href="code-based-prerequisites.md">
<img alt="Validation" src="../assets/do-not-localize/web-prerequisites.jpg">
</a>
<div>
<a href="code-based-prerequisites.md"><strong>Prerequisites</strong></a>
</div>
<p>
</td>
<td>
<a href="create-code-based.md#create-code-based-campaign">
<img alt="Infrequent" src="../assets/do-not-localize/web-create.jpg">
</a>
<div>
<a href="create-code-based.md#create-code-based-campaign"><strong>Create a code-based experience</strong></a>
</div>
<p></td>
<td>
<a href="code-based-implementation-samples.md">
<img alt="Validation" src="../assets/do-not-localize/web-design.jpg">
</a>
<div>
<a href="code-based-implementation-samples.md"><strong>Implementation samples</strong></a>
</div>
<p>
</td>
</tr></table>

<!--[Learn how to create a code-based campaign in this video](#video)-->

## When to use code-based vs. other channels {#code-based-vs-other-channels}

### Code-based vs. other channels

When to use the code-based channel rather than the other [!DNL Journey Optimizer] channels?

* You can consider using code-based experiences any time when your digital property is not accessed through a web browser or a mobile app – cases in which you can probably better use the [!DNL Journey Optimizer] [web channel](../web/get-started-web.md){target="_blank"} or the [!DNL Journey Optimizer] [in-app messaging](../in-app/get-started-in-app.md){target="_blank"} channel.

* You can use the code-based channel as an alternative to the [!DNL Journey Optimizer] web channel if your website cannot be loaded into the [web designer](../web/edit-web-content.md#work-with-web-designer){target="_blank"} visual editor or if you cannot use the [browser extension](../web/web-prerequisites.md#visual-authoring-prerequisites){target="_blank"} that powers visual authoring for web channel.

* You can also use the code-based channel as an alternative to the [!DNL Journey Optimizer] web or in-app channels in case you have an API-based, headless or server-side implementation.

### Code-based vs. web channel

To execute web use cases, you can use either the web channel or code-based experience, but depending on your context one would be more appropriate than the other. The main differences are listed below so you can make an informed decision on what to use when.

**Web**
* Edit your content using the [web designer](../web/edit-web-content.md#work-with-web-designer){target="_blank"} visual editor.
* You need the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/overview.html){target="_blank"} implementation and the [Adobe Experience Cloud Visual Editing Helper](https://chrome.google.com/webstore/detail/adobe-experience-cloud-vi/kgmjjkfjacffaebgpkpcllakjifppnca){target="_blank"} extension installed on your web browser. [Learn more](../web/web-prerequisites.md){target="_blank"}
* The web channel lets you modify everything on your page and has a pre-defined list of actions you can use to make changes. [Learn more](../web/edit-web-content.md#work-with-web-designer){target="_blank"}
* It is easy to set up and get going fast.
* It is marketer-persona focused.

**Code-based experience**
* Edit your content using the [Expression editor](create-code-based.md#edit-code).
* The code-based experience requires previous development work on your implementation to make sure that your surfaces can interpret and deliver the content published on the edge by [!DNL Journey Optimizer] for these surfaces. [Learn more](#surface-definition)
* It requires more planning and it can change only the things that developers specify. Therefore, it is essential to identify the components (home banner, hero image, menu bar, etc.) on the surfaces that need to be modified for personalization or testing, and work with your development team to build the implementation needed for handling these changes.  
* It allows you to use JSON code content.
* It is developer-persona focused.

## How it works {#how-it-works}

>[!CAUTION]
>
>This feature is for developer persona and/or experienced users. It can be used by marketers with some code-writing skills, as long as the surface implementations and initial setup are handled by the your development team.

To edit your content using the [!DNL Journey Optimizer] code-based experience feature, your pages or apps need to be instrumented. To do so, you must declare upfront the specific individual locations (called "[surfaces](#surface-definition)") where you want to insert or replace content<!--HOW??-->.

>[!NOTE]
>
>Currently the content associated with a surface can only be HTML or JSON. <!--WILL COME LATER: text, image or another format depending on the application-->

The key steps to implement a code-based campaign are as follows.

1. Define a [surface](#surface-definition), which is basically the location where you want to add your code-based experience, and create a campaign in [!DNL Journey Optimizer] using this surface. [Learn how](create-code-based.md#create-code-based-campaign)

1. Compose an experience by specifying content for the selected surface using the [!DNL Journey Optimizer] Expression editor. [Learn how](create-code-based.md#edit-code)

1. Your app implementation team makes explicit API or SDK calls to fetch content for the named surfaces, such as "Banner Text" or "Recommendations Tray 1", or non-UI-related decision points in an application, such as "search algorithm parameters". In this case, the implementation team is responsible for rendering or otherwise interpreting and acting on the returned content.<!--TBC with Robert - should link to a new section with API/SDK call samples-->

## What is a surface? {#surface-definition}

>[!CONTEXTUALHELP]
>id="ajo_code_based_surface"
>title="Define a code-based experience surface"
>abstract="A code-based surface is any entity designed for user or system interaction, which is uniquely identified by an URI."

A **code-based experience surface** is any entity designed for user or system interaction<!--ask Robert to explain further-->, which is uniquely identified by an **URI**.

In other words, a surface can be seen as a container at any level of hierarchy with an entity (touchpoint) that exists.<!--good idea to illustrate how it can be seen, but to clarify-->

* It can be a web page, a mobile app, a desktop app, a specific content location within a larger entity (for example a `div`), or a non-standard display pattern (for example, a kiosk or a desktop app banner).<!--In retail, a kiosk is a digital display or small structure that businesses often place in high-traffic areas to engage customers.-->

* It can also extend to specific pieces of content containers for non-display or abstracted-display purposes (for example, JSON blobs delivered to services).

* It can also be a wildcard surface that matches a variety of client-surface definitions (for example, a hero image location on every page of your website could translate in a surface URI like: web://mydomain.com/*#hero_image).

Basically a surface URI is composed of multiple sections:
1. **Type**: web, ios, android, atm, kiosk, tvcd, service, etc.
1. **Property**: page URL or app bundle
1. **Container**: location on the page/app activity 

The tables below list some surface URI definition examples for various devices.

**Web and mobile**

| Type | URI | Description |
| --------- | ----------- | ------- | 
| Web | web://domain.com/path/page.html | Represents an individual path and page of a website. |
| Web | web://domain.com/path/page.html#element | Represents an individual element within a specific page of a specific domain. |
| Web | web://domain.com/*#element | Wildcard surface - represents an individual element in each of the pages under a specific domain. |
| iOS app | mobileapp://com.vendor.bundle | Represents a specific mobile application for a single platform - in this case iOS app. |
| iOS app | mobileapp://com.vendor.bundle/activity | Represents a specific activity (view) within a mobile application. |
| iOS app | mobileapp://com.vendor.bundle/activity#element | Represents a specific element within an activity, such as a button or other view element. |
| Android app | mobileapp://com.vendor.bundle | Represents a specific mobile application for a single platform - in this case Android app. |

**Other device types**

| Type | URI | Description |
| --------- | ----------- | ------- | 
| Desktop | desktop://com.vendor.bundle | Represents a specific desktop application. |
| Desktop | desktop://com.vendor.bundle#element | Represents a specific element within an application, such as a button, menu, hero banner, etc. |
| tvOS app | tvos://com.vendor.bundle | Represents a specific tvOS app. |
| TV app | tvcd://com.vendor.bundle | Represents a specific smart TV or TV connected device app - bundle ID. |
| Service | service://servicename | Represents a server-side process or other manual entity. |
| Kiosk | kiosk://location/screen | Example of potential additional surface types that can be added easily. |
| ATM | atm://location/screen | Example of potential additional surface types that can be added easily. |

**Wildcard surfaces**

| Type | URI | Description |
| --------- | ----------- | ------- | 
| Wildcard web | wildcard:web://domain.com/`*`#element | Wildcard surface - represents an individual element in each of the pages under a specific domain. |
| Wildcard web | wildcard:web://`*`domain.com/`*`#element | Wildcard surface - represents an individual element in each of the pages under all domains that end with "domain.com". |



