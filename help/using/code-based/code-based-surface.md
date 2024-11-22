---
title: Code-based surface
description: Learn what a code-based experience surface is
feature: Code-based Experiences, Channel Configuration
topic: Content Management
role: Admin
level: Experienced
exl-id: 07ec74fb-7fbc-48c6-a8fc-f58f24a60723
---
# Code-based experience surfaces {#code-based-surface}

## What is a surface? {#surface-definition}

>[!CONTEXTUALHELP]
>id="ajo_admin_surface_uri"
>title="Add the surface URI for your component"
>abstract="If your implementation is not for Web, iOS, or Android, or if you need to target specific URIs, enter a surface URI, which is a unique identifier directing to the entity where you want to deliver your experience. Make sure you enter a surface URI that matches the one used in your own implementation."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/code-based-experience/configure-code-based-channel/code-based-configuration#other" text="Create a code-based experience configuration for Other platforms"

A code-based experience **surface** is any entity designed for user or system interaction, uniquely identified by an [URI](#surface-uri). The surface is specified in the [application implementation](code-based-prerequisites.md#implementation-prerequisites) and must match the surface referenced in your [code-based experience channel configuration](code-based-configuration.md).

A surface can be seen as a container at any level of hierarchy with an entity (touchpoint) that exists.

* It can be a web page, a mobile app, a desktop app, a specific content location within a larger entity (for example a `div`), or a non-standard display pattern (for example, a kiosk or a desktop app banner).<!--In retail, a kiosk is a digital display or small structure that businesses often place in high-traffic areas to engage customers.-->

* It can also extend to specific pieces of content containers for non-display or abstracted-display purposes (for example, JSON blobs delivered to services).

* It can also be a wildcard surface that matches a variety of client-surface definitions (for example, a hero image location on every page of your website could translate in a surface URI like: web://mydomain.com/*#hero_image).

## Surface identifier {#surface-uri}

A **surface URI** serves as a precise identifier directing to distinct user interface elements or components within an application. Basically, a surface URI is composed of multiple sections:

1. **Type**: web, mobileapp, atm, kiosk, tvcd, service, etc.
1. **Property**: page URL or app bundle
1. **Container**: location on the page/app activity 

The tables below list some surface URI definition examples for various devices.

**Web and mobile**

| Type | URI | Description |
| --------- | ----------- | ------- | 
| Web | `web://domain.com/path/page.html#element` | Represents an individual element within a specific page of a specific domain, where an element can be a label like in the following examples: hero_banner, top_nav, menu, footer, etc. |
| iOS app | `mobileapp://com.vendor.bundle/activity#element` | Represents a specific element within a native app activity, such as a button or other view element. |
| Android app | `mobileapp://com.vendor.bundle/#element` | Represents a specific element within a native app. |

**Other device types**

| Type | URI | Description |
| --------- | ----------- | ------- | 
| Desktop | `desktop://com.vendor.bundle/#element` | Represents a specific element within an application, such as a button, menu, hero banner, etc. |
| TV app | `tvcd://com.vendor.bundle/#element` | Represents a specific element within a smart TV or TV connected device app - bundle ID. |
| Service | `service://servicename/#element` | Represents a server-side process or other manual entity. |
| Kiosk | `kiosk://location/screen#element` | Example of potential additional surface types that can be added easily. |
| ATM | `atm://location/screen#element` | Example of potential additional surface types that can be added easily. |

**Wildcard surfaces**

| Type | URI | Description |
| --------- | ----------- | ------- | 
| Wildcard web | `wildcard:web://domain.com/*#element` | Wildcard surface - represents an individual element in each of the pages under a specific domain. |
| Wildcard web | `wildcard:web://*domain.com/*#element` | Wildcard surface - represents an individual element in each of the pages under all domains that end with "domain.com". |

## URI composition {#uri-composition}

In [!DNL Journey Optimizer], the code-based experience channel supports two types of customer implementations:

* Based on the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/overview.html){target="_blank"} for your websites, or on the [Adobe Experience Platform Mobile SDK](https://developer.adobe.com/client-sdks/documentation/){target="_blank"} for you mobile apps;
* Server-side or hybrid using [AEP Edge Network Server APIs](https://experienceleague.adobe.com/docs/experience-platform/edge-network-server-api/data-collection/interactive-data-collection.html){target="_blank"}.

>[!NOTE]
>
>Learn more on the implementation prerequisites in [this section](code-based-prerequisites.md#implementation-prerequisites).

Using code-based experiences, you can modify content on granular locations <!--(such as a specific location on a page, or inside a mobile native app)-->which are uniquely identified by [!DNL Journey Optimizer] using [surface URIs](#surface-uri). 

These surface URIs are composed and handled depending on the implementation method:

* **Web/Mobile SDK**: Your web/mobile developer needs to define these granular locations as simple strings, because the Web/Mobile SDK is capable of automatically compose the surface URI based on the current URL/app ID and the location string.

* **Edge Network APIs**: The app/page developer must define full surface URIs that include the full path and location where the content will be consumed, because the full URIs are required in this type of implementation.

This is why, when creating a [code-based experience channel configuration](code-based-configuration.md), you have two ways to specify the surface according to the selected platform:

* For **[!UICONTROL Web]**, **[!UICONTROL iOS]** and **[!UICONTROL Android]** platforms, you need to the enter the **URL/app ID** and a **location or path** to compose the surface. Learn more on configuring code-based experiences for [web](code-based-configuration.md#web) and [mobile](code-based-configuration.md#mobile) platforms

* If the platform is **[!UICONTROL Other]**, you need to enter the full **surface URI**, like in the examples [above](#surface-uri). Learn more on configuring code-based experiences for [other](code-based-configuration.md#other) platforms
