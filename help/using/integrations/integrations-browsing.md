---
solution: Journey Optimizer
product: journey optimizer
title: Work with Browsing Integrations
description: Configure Browsing integrations that let marketers search, browse, and select items from external APIs directly in the authoring experience
feature: Integrations
topic: Content Management
role: User
level: Beginner
keywords: integration
---
# Work with Browsing integrations {#Browsing}

>[!BEGINSHADEBOX]

**On this page:** Learn how administrators configure Browsing integrations that let marketers search, browse, and select items from external APIs directly in the authoring experience, and how to link them to Standard integrations.

>[!ENDSHADEBOX]

In addition to Standard integrations, you can create **Browsing** integrations. A Browsing integration lets marketers search, browse, and paginate through items returned by an external API, then select a specific item directly in the authoring experience instead of manually entering a parameter value.

## Create a Browsing integration {#create-browsing}

As an administrator, you create a Browsing integration from the **[!UICONTROL Browsing]** tab of the **[!UICONTROL Integrations]** configuration, using the same [step-by-step instructions](integrations-create.md#configure) as for Standard integrations. 

Once the integration information is provided, configure the following Browsing-specific settings:

1. From the **[!UICONTROL Browsing]** menu, choose the **[!UICONTROL Items path]** where the list of items is located.

    ![](assets/browsing_1.png)

1. In the **[!UICONTROL Search]** drop-down, **[!UICONTROL Enable search]** and select which parameter carries the search query, then provide a description for marketers.

    ![](assets/browsing_2.png)

1. Enable the **[!UICONTROL Pagination]** to choose a pagination type

    ![](assets/browsing_3.png)

1. From the **[!UICONTROL Render]** menu, choose how you want your items to be displayed.

1. Select which fields to display as columns when marketers browse the list of items.

1. Click **[!UICONTROL Test browsing]** to preview the search and pagination behavior with the configured settings.

1. Save the Browsing integration, then click **[!UICONTROL Publish]** and **[!UICONTROL Activate]**.

## Link a Browsing integration to a Standard integration {#use-Browsing}

You can let marketers pick an item from a Browsing integration to populate a parameter value in a Standard integration.

1. While configuring a parameter on a Standard integration, enable **[!UICONTROL Browsing]**.

1. Click the selector button and choose the Browsing integration to link.

    The parameters exposed by the linked Browsing integration are fetched, and you can set default values for them.

1. Set the **[!UICONTROL Reference path]** to the field of the listed item that should be passed as the parameter value, for example an **ID**.

1. Save and publish the Standard integration.

## Select items during authoring {#select-Browsing-items}

When a parameter is linked to a Browsing integration, marketers see a selector in the message or journey editor instead of a plain input field. They can search and browse the paginated list of items returned by the Browsing integration, select the item they want, and confirm their selection. The corresponding **[!UICONTROL Reference path]** value is then automatically inserted into the integration parameter.

![](assets/browsing_4.png)

**See also**

* [Work with Standard integrations](integrations-create.md)
* [Integrations troubleshooting FAQ](vendor-integration-faq.md#troubleshooting)
* [Monitoring & Troubleshooting](../../rp_landing_pages/troubleshoot-journey-landing-page.md)
