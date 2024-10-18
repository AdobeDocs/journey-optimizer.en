---
title: Code-based configuration
description: Create code-based configuration
feature: Code-based Experiences, Channel Configuration
topic: Content Management
role: Admin
level: Experienced
exl-id: 1aff2f6f-914c-4088-afd8-58bd9edfe07d
---
# Configure your code-based experience {#code-based-configuration}

>[!CONTEXTUALHELP]
>id="ajo_code_based_surface"
>title="Define a code-based experience configuration"
>abstract="A code-based configuration defines the path and location inside your application, uniquely identified by an URI in the application implementation, where the content will be delivered and consumed."

Before [building your experience](create-code-based.md), you need to create a code-based experience configuration in which you define where the content will be delivered and consumed inside your application.

A code-based experience configuration must reference the surface, which is basically the location where you want to render your changes. According to the selected platform, you need to enter a location/path, or the full surface URI. [Learn more](#surface-definition)

## Create a code-based experience configuration {#create-code-based-configuration}

>[!CONTEXTUALHELP]
>id="ajo_admin_location"
>title="Indicate the specific location inside your page or app"
>abstract="This field specifies the exact destination inside a page or within the app you want users to access. It can be a particular section inside a web page, or a page deep within the app's navigation structure."

>[!CONTEXTUALHELP]
>id="ajo_admin_default_mobile_url"
>title="Define a URL for content creation and preview"
>abstract="This field ensures that the pages generated or matched by the rule have a designated URL, essential for both creating and previewing content effectively."

To create a code-based experience channel configuration, follow these steps:

1. Access the **[!UICONTROL Channels]** > **[!UICONTROL General settings]** > **[!UICONTROL Channel configurations]** menu, then click **[!UICONTROL Create channel configuration]**.

    ![](assets/code_config_1.png)

1. Enter a name and a description (optional) for the configuration.

    >[!NOTE]
    >
    > Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore `_`, dot`.` and hyphen `-` characters.

1. To assign custom or core data usage labels to the configuration, you can select **[!UICONTROL Manage access]**. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md)

1. Select **[!UICONTROL Marketing action]**(s) to associate consent policies to the messages using this configuration. All consent policies associated with the marketing action are leveraged in order to respect the preferences of your customers. [Learn more](../action/consent.md#surface-marketing-actions)

1. Select the **Code-based experience** channel.

    ![](assets/code_config_2.png)

1. Select the platform for which the code-base experience will be applied:

   * [Web](#web)
   * [iOS and/or Android](#mobile)
   * [Other](#other)

   >[!NOTE]
   >
   >You can select several platforms. When choosing multiple platforms, the content is delivered to all the selected pages or apps.

1. Choose the format expected by the application for this particular location. This will be used when authoring the code-based experience in campaings and journeys.

    ![](assets/code_config_4.png)

1. Click **[!UICONTROL Submit]** to save your changes.

You can now select this configuration when [creating a code-based experience](create-code-based.md) in your campaigns and journeys.

>[!NOTE]
>
>Your app implementation team is responsible for making explicit API or SDK calls to fetch content for the surfaces defined in the selected code-based experience configuration. Learn more on the different customer implementations in [this section](code-based-implementation-samples.md).

### Web platforms {#web}

>[!CONTEXTUALHELP]
>id="ajo_admin_default_web_url"
>title="Define a URL for content authoring and preview"
>abstract="This field ensures that the pages generated or matched by the rule have a designated URL, essential for both creating and previewing content effectively."

To define the code-based experience configuration settings for web platforms, follow the steps below.

1. Select one of the following options:

   * **[!UICONTROL Single page]** - If you want to apply the changes to a single page exclusively, enter a **[!UICONTROL Page URL]**.

      ![](assets/code_config_single_page.png)

   * **[!UICONTROL Pages matching rule]** - To target multiple URLs matching the same rule, build one or more rules. [Learn more](../web/web-configuration.md#web-page-matching-rule)

       <!--This could be used to apply changes universally across a website, such as updating a hero banner across all pages or adding a top image to display on every product page.-->

       For example, if you want to edit elements that are displayed on all the women product pages of your Luma website, select **[!UICONTROL Domain]** > **[!UICONTROL Starts with]** > `luma` and **[!UICONTROL Page]** > **[!UICONTROL Contains]** > `women`.

       ![](assets/code_config_matching_rules.png)

1. The following applies for the preview URL:

    * If a single page URL is entered, that URL will be used for the preview - no need to enter another URL.
    * If a [pages matching rule](../web/web-configuration.md#web-page-matching-rule) is selected, you must enter a **[!UICONTROL Default authoring and preview URL]** that will be used to preview the experience in the browser. [Learn more](../code-based/create-code-based.md#preview-on-device)

        ![](assets/code_config_matching_rules_preview.png)

1. The **[!UICONTROL Location on page]** field specifies the exact destination inside the page you want users to access. It can be a particular section on a page within the site's navigation structure, such as 'hero-banner' or 'product-rail'.

    ![](assets/code_config_location_on_page.png)

### Mobile platforms (iOS and Android) {#mobile}

>[!CONTEXTUALHELP]
>id="ajo_admin_app_id"
>title="Provide your app ID"
>abstract="Enter the app ID for accurate identification and configuration within the application's operational environment, ensuring seamless integration and functionality."

>[!CONTEXTUALHELP]
>id="ajo_admin_mobile_url_preview"
>title="Enter the URL for previewing content"
>abstract="This field is essential for enabling the simulation and preview of your content directly on your device within your application."

To define the code-based experience configuration settings for mobile platforms, follow the steps below.

1. Enter your **[!UICONTROL App id]**. This allows for accurate identification and configuration within the app's operational environment, and ensures seamless integration and functionality.
    
1. Provide the **[!UICONTROL Location or path inside the app]**. This field specifies the exact destination within the app you want users to access. It can be a particular section or page deep within the app's navigation structure, such as 'hero-banner' or 'product-rail'.

    ![](assets/code_config_3.png){width="500"}

1. Fill in the **[!UICONTROL Preview URL]** field to enable on-device previews. This URL informs the preview service of the specific URL to use when triggering preview on device. [Learn more](../code-based/create-code-based.md#preview-on-device)

   The preview URL is a deep link configured by the app developer within your app. This ensures that any URLs matching the deep link scheme will open within the app instead of in a mobile web browser. Contact your app developer to obtain the deep link scheme configured for your app.

    +++  The following resources can assist you in configuring deep links for your app implementation

    * For Android:

        * [Create Deep Links to App Context](https://developer.android.com/training/app-links/deep-linking)

    * For iOS: 

        * [Defining a Custom URL Scheme for Your App](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app)

        * [Supporting Universal Links in Your App](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)

    +++

    >[!NOTE]
    >
    >If you encounter issues while previewing the experience, please refer to [this documentation](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/troubleshooting#app-does-not-open-link).

### Other platforms {#other}

To define the code-based experience configuration settings for other platforms (such as video consoles, TV connected devices, smart TVs, kiosks, ATMs, voice assistants, IoT devices, etc.), follow the steps below.

1. Select **[!UICONTROL Other]** as the platform if your implementation is not for Web, iOS or Android, or if you need to target specific URIs.

1. Enter the **[!UICONTROL Surface URI]**. A surface URI is a unique identifier corresponding to the entity where you want to deliver your experience. [Learn more](#surface-definition)

    ![](assets/code_config_5.png)

    >[!CAUTION]
    >
    >Make sure you enter a surface URI that matches the one used in your own implementation. Otherwise, the changes cannot be delivered.

1. **[!UICONTROL Add another surface URI]** if needed. You can add up to 10 URIs.

   >[!NOTE]
   >
   >When adding multiple URIs, the content is delivered to all the listed components.

## What is a surface? {#surface-definition}

>[!CONTEXTUALHELP]
>id="ajo_admin_surface_uri"
>title="Add the surface URI for your component"
>abstract="If your implementation is not for Web, iOS, or Android, or if you need to target specific URIs, enter a surface URI, which is a unique identifier directing to the entity where you want to deliver your experience. Make sure you enter a surface URI that matches the one used in your own implementation."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/code-based-experience/code-based-configuration#other" text="Create a code-based experience configuration for Other platforms"

A code-based experience **surface** is any entity designed for user or system interaction, which is uniquely identified by an **URI**. The surface is specified in the application implementation and must match the surface referenced in your code-based experience channel configuration.

A surface can be seen as a container at any level of hierarchy with an entity (touchpoint) that exists.

* It can be a web page, a mobile app, a desktop app, a specific content location within a larger entity (for example a `div`), or a non-standard display pattern (for example, a kiosk or a desktop app banner).<!--In retail, a kiosk is a digital display or small structure that businesses often place in high-traffic areas to engage customers.-->

* It can also extend to specific pieces of content containers for non-display or abstracted-display purposes (for example, JSON blobs delivered to services).

* It can also be a wildcard surface that matches a variety of client-surface definitions (for example, a hero image location on every page of your website could translate in a surface URI like: web://mydomain.com/*#hero_image).

When creating a code-based experience channel configuration, you have two ways to specify the surface according to the selected platform:

* For **[!UICONTROL Web]**, **[!UICONTROL iOS]** and **[!UICONTROL Android]** platforms, you need to the enter a **location or path** to compose the surface.

* If the platform is **[!UICONTROL Other]**, you need to enter the full **surface URI**, like in the examples below.

A surface URI serves as a precise identifier directing to distinct user interface elements or components within an application. Basically, a surface URI is composed of multiple sections:

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
