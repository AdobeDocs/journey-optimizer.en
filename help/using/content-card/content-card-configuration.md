---
title: Content cards configuration
description: Content cards channel configuration
feature: Channel Configuration
topic: Content Management
role: Admin
level: Experienced
exl-id: 50e47e83-4b9e-4088-aa09-dea76393c035
---
# Configure Content cards {#content-card-configuration}

## What is a configuration? {#surface-definition}

A **content card experience configuration** is any entity designed for user or system interaction, which is uniquely identified by an **URI**.

In other words, a surface can be seen as a container at any level of hierarchy with an entity (touchpoint) that exists.

* It can be a web page, a mobile app, a desktop app, a specific content location within a larger entity (for example a `div`), or a non-standard display pattern (for example, a kiosk or a desktop app banner).

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

## Create a content card configuration {#create-config}

1. Access the **[!UICONTROL Channels]** > **[!UICONTROL Branding]** > **[!UICONTROL Channel configurations]** menu, then click **[!UICONTROL Create channel configuration]**.

    ![](assets/content_card_config_1.png)

1. Enter a name and a description (optional) for the configuration.

    >[!NOTE]
    >
    > Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore `_`, dot`.` and hyphen `-` characters.

1. To assign custom or core data usage labels to the configuration, you can select **[!UICONTROL Manage access]**. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md).

1. Select **[!UICONTROL Content card]** channel.

    ![](assets/content_card_config_2.png)

1. Select **[!UICONTROL Marketing action]**(s) to associate consent policies to the messages using this configuration. All consent policies associated with the marketing action are leveraged in order to respect the preferences of your customers. [Learn more](../action/consent.md#surface-marketing-actions)

1. Select the platform for which the content card experience will be applied.

    ![](assets/content_card_config_3.png)

1. For Web:

    * Specify a **[!UICONTROL Page URL]** to apply changes to a single page exclusively.

    * Or create a **[!UICONTROL Pages matching rule]** to target multiple URLs that match the specified rule. For instance, this could be used to apply changes universally across a website, such as updating a hero banner across all pages or adding a top image to display on every product page. [Learn more](../web/web-configuration.md)

1. For iOS and Android:

    * Enter or select your **[!UICONTROL App id]**, **[!UICONTROL Location or path inside the app]** and **[!UICONTROL Preview URL]**.

1. Submit your changes.

You can now select your configuration when creating your Content card experience.
