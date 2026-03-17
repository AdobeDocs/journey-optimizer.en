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

## Prerequisites {#prerequisites}

To access and manage content templates, ensure the following:

* **Content Templates permission** — Your role must include the **[!UICONTROL Manage content templates]** permission (under the **Content Management** resource). Without it, the **Content Templates** menu is not visible in the left navigation. [Learn how to manage permissions](../administration/permissions.md)
* **Sandbox scope** — Content templates are sandbox-specific. Templates created in one sandbox are not available in another. Ensure you are in the correct sandbox before searching for a template.
* **HTML templates (deprecated)** — Starting March 2025, HTML-type content templates are deprecated. Existing HTML templates remain accessible but new ones cannot be created.

## Access content templates {#access}

To access the content template list, select **[!UICONTROL Content Management]** > **[!UICONTROL Content Templates]** from the left menu.

![](assets/content-template-list.png)

All the templates created on the current sandbox—either from a journey or a campaign using the **[!UICONTROL Save as template]** option, or from the **[!UICONTROL Content Templates]** menu—are displayed. [Learn how to create templates](#create-content-templates)

The pane on the left allows you to organize content templates into folders. By default, all templates are displayed. When selecting a folder, only the templates and folders included in the selected folder are displayed. [Learn more](#folders)

![](assets/content-template-list-folders.png)

To find a specific item, start typing a name in the search field. When a [folder](#folders) is selected, the search applies to all content templates or folders in the first level of hierarchy of that folder<!--(not nested items)-->.

You can sort content templates by:

* Type
* Channel
* Creation or modification date
* Tags - [Learn more about tags](../start/search-filter-categorize.md#tags)

You can also choose to display only the items created or modified by you.

![](assets/content-template-list-filters.png)

>[!NOTE]
>
>Starting from March 2025, HTML-type content templates are deprecated. You can still access existing HTML content templates previously created in [!DNL Journey Optimizer].

## Use folders to manage content templates {#folders}

To easily navigate your content templates, use folders to organize them more effectively into a structured hierarchy. This enables you to categorize and manage the items according to your organization's needs.

![](assets/content-template-folders.png)

1. Click the **[!UICONTROL All content templates]** button to display all the items previously created without the folder grouping.

1. Click the **[!UICONTROL Root]** folder to display all the folders created.

    >[!NOTE]
    >
    >If you have not created folders yet, all the content templates are displayed.

1. Click any folder inside the **[!UICONTROL Root]** folder to display its content.

1. Upon clicking the **[!UICONTROL Root]** folder or any other folder, the **[!DNL Create folder]** button displays. Select it.

    ![](assets/content-template-create-folder.png)

1. Type a name for the new folder and click **[!UICONTROL Save]**. The new folder displays on top of the content template list inside the **[!UICONTROL Root]** folder, or inside the folder currently selected.

1. You can click the **[!UICONTROL More actions]** button to rename or delete the folder.

    ![](assets/content-template-folder-more-actions.png)

1. Using the **[!UICONTROL More actions]** button, you can also move the content template to another existing folder.

    ![](assets/content-template-folder-moved.png)

1. Navigate to the folder that you just created. Each new content template you [create](create-content-templates.md) from here is saved into the current folder.

    ![](assets/content-template-folder-create.png)

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
>Proper thumbnails can only be generated for HTML-type email content templates.

When you update content, wait a few seconds for the changes to reflect in the thumbnail.

## Troubleshooting {#troubleshooting}

+++I can't see the Content Templates menu in the left navigation

Your role is missing the **Manage content templates** permission. Ask your administrator to add the **Content Management** resource with the **Manage content templates** permission to your role. [Learn more](../administration/permissions.md)

+++

+++A template I created is not showing in the list

Check that you are in the correct sandbox — templates are sandbox-specific. Also verify whether a folder is selected in the left pane; when a folder is selected, only templates within that folder are displayed. Click **[!UICONTROL All content templates]** to display all templates regardless of folder.

+++

+++I edited a template but my campaign or journey content did not update

Editing or deleting a template does not retroactively update campaigns or journeys that were built using it. Content is copied at the time of use. To update existing content, edit the campaign or journey directly.

+++

## Export content templates to another sandbox {#export}

Journey Optimizer allows you to copy a content template from one sandbox to another. For example, you can copy a template from your Stage sandbox environment to your Production sandbox.

The copy process is carried out via a **package export and import** between the source and target sandboxes. Detailed information on how to export objects and import them into a target sandbox is available in this section: [Copy objects to another sandbox](../configuration/copy-objects-to-sandbox.md)

