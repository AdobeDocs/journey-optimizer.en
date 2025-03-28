---
solution: Journey Optimizer
product: journey optimizer
title: Access & manage content templates
description: Learn how to access & manage content templates
topic: Content Management
role: User
level: Beginner
exl-id: ef6110c4-1aa6-4835-b0b0-b3c4fe0e7024
---
# Access and manage content templates {#access-manage-templates}

## Access content templates {#access}

To access the content template list, select **[!UICONTROL Content Management]** > **[!UICONTROL Content Templates]** from the left menu.

![](assets/content-template-list.png)

All the templates that were created on the current sandbox - either from a journey or a campaign using the **[!UICONTROL Save as template]** option, either from the **[!UICONTROL Content Templates]** menu - are displayed. [Learn how to create templates](#create-content-templates)

You can sort content templates by:
* Type
* Channel
* Creation or modification date
* Tags - [Learn more on tags](../start/search-filter-categorize.md#tags)

You can also choose to display only the items that yourself created or modified.

![](assets/content-template-list-filters.png)

## Edit and delete content templates {#edit}

* To edit a template content, click the desired item from the list and make the desired changes. You can also edit the content template properties by clicking the edit button next to the template's name.

    ![](assets/content-template-edit.png)

* To delete a template, select the **[!UICONTROL More actions]** button next to the desired template and select **[!UICONTROL Delete]**.

    ![](assets/content-template-list-delete.png)

>[!NOTE]
>
>When a template is edited or deleted, campaigns or journeys including content created using this template are not impacted.

## [!BADGE Limited Availability]{type=Informative} Display templates as thumbnails {#template-thumbnails}

Select the **[!UICONTROL Grid view]** mode to display each template as a thumbnail.

>[!AVAILABILITY]
>
>This capability is released in Limited Availability (LA) for a small set of customers.

![](assets/content-template-grid-view.png)

>[!NOTE]
>
>Currently proper thumbnails can only be generated for HTML-type email content templates.

When you update a content, you may have to wait a few seconds before the changes are reflected in the thumbnail.

## Export content templates to another sandbox {#export}

Journey Optimizer allows you to copy a content template from one sandbox to another. For example, you can copy a template from your Stage sandbox environment to your Production sandbox.

The copy process is carried via a **package export and import** between the source and target sandboxes. Detailed information on how to export objects and import them into a target sandbox are available in this section: [Copy objects to another sandbox](../configuration/copy-objects-to-sandbox.md)
