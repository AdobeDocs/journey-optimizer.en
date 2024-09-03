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
>id="ajo_admin_app_id"
>title="App ID"
>abstract="Provide the App ID for accurate identification and configuration within the app's operational environment, ensuring seamless integration and functionality."

>[!CONTEXTUALHELP]
>id="ajo_admin_location"
>title="Location on page"
>abstract="The Location or path inside the app field specifies the exact destination within the app you want users to access. This could be a particular section or page deep within the app's navigation structure."

>[!CONTEXTUALHELP]
>id="ajo_admin_surface_uri"
>title="Surface URI"
>abstract="A Surface URI serves as a precise identifier directing to distinct user interface elements or components within an application."

>[!CONTEXTUALHELP]
>id="ajo_admin_default_mobile_url"
>title="Default authoring and preview URL"
>abstract="This field ensures that the pages generated or matched by the rule have a designated URL, essential for both creating and previewing content effectively."

>[!CONTEXTUALHELP]
>id="ajo_admin_default_web_url"
>title="Default authoring and preview URL"
>abstract="This field ensures that the pages generated or matched by the rule have a designated URL, essential for both creating and previewing content effectively."

>[!CONTEXTUALHELP]
>id="ajo_admin_mobile_url_preview"
>title="Preview URL"
>abstract="This field is essential for enabling the simulation and preview of your content directly on your device within your application."

## Create a channel configuration {#reatte-code-based-configuration}

To create a channel configuration, follow these steps:

1. Access the **[!UICONTROL Channels]** > **[!UICONTROL General settings]** > **[!UICONTROL Channel configurations]** menu, then click **[!UICONTROL Create channel configuration]**.

    ![](assets/code_config_1.png)

1. Enter a name and a description (optional) for the configuration.

    >[!NOTE]
    >
    > Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore `_`, dot`.` and hyphen `-` characters.

1. To assign custom or core data usage labels to the configuration, you can select **[!UICONTROL Manage access]**. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md).

1. Select **[!UICONTROL Marketing action]**(s) to associate consent policies to the messages using this configuration. All consent policies associated with the marketing action are leveraged in order to respect the preferences of your customers. [Learn more](../action/consent.md#surface-marketing-actions)

1. Select **Code-based experience** channel.

    ![](assets/code_config_2.png)

1. Select the platform for which the code-base experience will be applied.

1. For Web:

    * Specify a **[!UICONTROL Page URL]** to apply changes to a single page exclusively.

    * Or create a **[!UICONTROL Pages matching rule]** to target multiple URLs that match the specified rule. For instance, this could be used to apply changes universally across a website, such as updating a hero banner across all pages or adding a top image to display on every product page. [Learn more](../web/web-configuration.md)

1. For iOS and Android:

    * Enter your **[!UICONTROL App id]** and **[!UICONTROL Location or path inside the app]**.

        ![](assets/code_config_3.png){width="500"}

1. Select Other as the platform if your implementation is not for Web, iOS, or Android, or if you need to target specific URIs. When choosing multiple platforms or adding multiple URIs, the content will be delivered to all the selected pages or apps.

    * Enter the **[!UICONTROL Surface URI]**.

    >[!CAUTION]
    >
    >Make sure the surface URI used in your code-based campaign matches the one used in your own implementation. Otherwise, the changes will not be delivered.

1. Fill in the **[!UICONTROL Preview URL]** field to enable on-device previews. This URL informs the preview service of the specific URL to use when triggering a preview.

    * For Web:

        * If a single page URL is entered, that URL will be used for the preview.
        * If a page matching rule is selected, you must enter a default preview URL that will be used to preview the experience in the browser.
 
    * For Mobile platforms (iOS / Android):

        * Preview URL is a deeplink configured by the app developer within your app. This ensures that any URLs matching the deeplink scheme will open within the app instead of in a mobile web browser. Contact your app developer to obtain the deeplink scheme configured for your app.

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

1. Choose the format expected by the application at that particular location. This will be used when authoring the code-based experience in campaings and journeys.

1. Submit your changes.

You can now select your configuration when creating your code-based experience.


## What is a surface? {#surface-definition}

>[!CONTEXTUALHELP]
>id="ajo_code_based_surface"
>title="Define a code-based experience configuration"
>abstract="A code-based configuration defines the path and location inside your application, uniquely identified by an URI in the application implementation, where the content will be delivered and consumed."

A **code-based experience surface** is any entity designed for user or system interaction, which is uniquely identified by an URI. The surface is specified in the application implementation and it should correspond to the one composed in the Code-based experience channel configuration.

When creating a code-based experience channel configuration - for Web, iOS and Android platforms, you need to the enter a path and location to compose the surface, while if the platform is Other you will need to enter the full URI, like in the examples below.

In other words, a surface can be seen as a container at any level of hierarchy with an entity (touchpoint) that exists.<!--good idea to illustrate how it can be seen, but to clarify-->

* It can be a web page, a mobile app, a desktop app, a specific content location within a larger entity (for example a `div`), or a non-standard display pattern (for example, a kiosk or a desktop app banner).<!--In retail, a kiosk is a digital display or small structure that businesses often place in high-traffic areas to engage customers.-->

* It can also extend to specific pieces of content containers for non-display or abstracted-display purposes (for example, JSON blobs delivered to services).

* It can also be a wildcard surface that matches a variety of client-surface definitions (for example, a hero image location on every page of your website could translate in a surface URI like: web://mydomain.com/*#hero_image).

Basically a surface URI is composed of multiple sections:
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
