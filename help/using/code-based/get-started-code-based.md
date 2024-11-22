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

[!DNL Journey Optimizer] allows you to personalize and test the experiences you want to deliver to your customers across all your touchpoints like: web apps, mobile apps, desktop apps, video consoles, TV connected devices, smart TVs, kiosks, ATMs, voice assistants, IoT devices, etc.

With the **code-based experience** capability, you can define inbound experiences using a simple and intuitive non-visual editor. It allows you to insert and edit specific elements at individual and more granular locations of your apps or web pages, no matter the type of applications you have - rather than applying modifications to an entire content.

<!--[!DNL Journey Optimizer] allows you to compose and deliver content on any inbound device in a developer-focused workflow. You can leverage all the personalization capabilities, and preview what will be published. The content can be static (images, text, JSON, HTML) or dynamic (offers, decisions, recommendations). You can also insert custom content actions in your omni-channel journeys.-->

>[!IMPORTANT]
>
>Specific guardrails and recommendations for code-based experiences are detailed in [this page](code-based-prerequisites.md).
 

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
<a href="code-based-prerequisites.md"><strong>Guardrails and prerequisites</strong></a>
</div>
<p>
</td>
<td>
<a href="code-based-configuration.md">
<img alt="Validation" src="../assets/do-not-localize/web-design.jpg">
</a>
<div>
<a href="code-based-implementation-samples.md"><strong>Code-based channel configuration</strong></a>
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
</tr></table>

<!--[Learn how to create a code-based campaign in this video](#video)-->

## When to use code-based vs. other channels {#code-based-vs-other-channels}

### Code-based vs. other channels

When to use the code-based channel rather than the other [!DNL Journey Optimizer] channels?

* You can consider using code-based experiences any time when your digital property is not accessed through a web browser or a mobile app – cases in which you can probably better use the [!DNL Journey Optimizer] [web channel](../web/get-started-web.md){target="_blank"} or the [!DNL Journey Optimizer] [in-app messaging](../in-app/get-started-in-app.md){target="_blank"} channel.

<!--* You can use the code-based channel as an alternative to the [!DNL Journey Optimizer] web channel if your website cannot be loaded into the [web designer](../web/web-visual-editor.md){target="_blank"} visual editor or if you cannot use the [browser extension](../web/web-prerequisites.md#visual-authoring-prerequisites){target="_blank"} that powers visual authoring for web channel.-->

* You can use the code-based channel as an alternative to the [!DNL Journey Optimizer] web or in-app channels in case you have an API-based, headless or server-side implementation.

* You can also leverage the code-based channel on native mobile applications as an alternative to the in-app channel if you want to modify the content inside your native app instead of showing modals, popups or overlays.

### Code-based vs. web channel {#code-based-vs-web}

To execute web use cases, you can use either the web channel or code-based experience, but depending on your context one would be more appropriate than the other. The main differences are listed below so you can make an informed decision on what to use, and when.

**Web**

* Edit your content using the [web designer](../web/web-visual-editor.md){target="_blank"} visual editor or the web [non-visual editor](../web/web-non-visual-editor.md).
* You need the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/overview.html){target="_blank"} – a client-side implementation.
<!--* You need the [Adobe Experience Cloud Visual Editing Helper](https://chrome.google.com/webstore/detail/adobe-experience-cloud-vi/kgmjjkfjacffaebgpkpcllakjifppnca){target="_blank"} extension installed on your web browser. [Learn more](../web/web-prerequisites.md){target="_blank"}-->
* The web channel lets you modify everything on your page and has a pre-defined list of actions you can use to make changes. [Learn more](../web/web-visual-editor.md){target="_blank"}
* It is easy to set up and get going fast.
* It is marketer-persona focused.

**Code-based experience**

* Edit your content using the [personalization editor](create-code-based.md#edit-code).
* You need either the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/overview.html){target="_blank"} – client-side implementation, or the the [AEP Edge Network Server API](https://experienceleague.adobe.com/docs/experience-platform/edge-network-server-api/data-collection/interactive-data-collection.html){target="_blank"} – server-side implementation.
* The code-based experience requires previous development work on your implementation to make sure that your applications can interpret and deliver the content published on the edge by [!DNL Journey Optimizer] for these locations. [Learn more](code-based-surface.md)
* It requires more planning and it can change only the things that developers specify. Therefore, it is essential to identify the components (home banner, hero image, menu bar, etc.) on the applications that need to be modified for personalization or testing, and work with your development team to build the implementation needed for handling these changes.  
* It allows you to use JSON code content.
* It is developer-persona focused.

## How it works {#how-it-works}

>[!CAUTION]
>
>This feature is for developer persona and/or experienced users. It can be used by marketers with some code-writing skills, as long as the channel configurations and initial setup are handled by your development team.

To edit your content using the [!DNL Journey Optimizer] code-based experience feature, your pages or apps need to be instrumented. To do so, you must declare upfront the specific individual locations (called "[surfaces](code-based-surface.md)") where you want to insert or replace content.

>[!NOTE]
>
>Currently the content associated with a configuration can only be HTML or JSON. 

The key steps to create and deliver a code-based experience are as follows.

1. Make sure you follow the channel-specific prerequisites. [Learn more](code-based-prerequisites.md)

1. Define a [surface](code-based-surface.md#surface-definition) in your application implementation, which is basically the location where you want to add your experience.

1. Create a code-based channel configuration that references that location. [Learn how](code-based-configuration.md#create-code-based-configuration)

1. Create a journey or campaign in [!DNL Journey Optimizer] using this configuration. [Learn how](create-code-based.md#create-code-based-campaign)

1. Compose an experience by specifying content for the selected configuration using the [!DNL Journey Optimizer] personalization editor. [Learn how](create-code-based.md#edit-code)

1. Test your code-based experience. [Learn how](test-code-based.md)

1. Publish it. [Learn how](publish-code-based.md)

1. Once your code-based experience journey or campaign is live, the app or page implementation that requests content for the surface must be in place for the content to be retrieved and displayed.

    >[!INFO]
    >
    >To ensure this, your app implementation team makes explicit API or SDK calls to fetch content for the surface defined in the code-based configuration, such as "Banner Text" or "Recommendations Tray 1", or non-UI-related decision points in an application, such as "search algorithm parameters". <!--In this case, the implementation team is responsible for rendering or otherwise interpreting and acting on the returned content.--> [Learn more](code-based-implementation-samples.md)



