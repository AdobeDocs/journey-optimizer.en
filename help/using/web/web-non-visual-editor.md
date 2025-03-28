---
title: Edit content using the non-visual editor
description: Learn how to author a web page and edit its content using the Journey Optimizer non-visual editor
feature: Web Channel
topic: Content Management
role: User
level: Experienced
exl-id: 00d2fc73-3ac8-421c-982a-0f3ec7e3dacd
---
# Use the web non-visual editor {#web-non-visual-editor}

In addition to the [!DNL Journey Optimizer] visual [web designer](web-visual-editor.md), you can also add modifications to your web pages using a **non-visual editor**.

This can be useful if you cannot, or are not allowed to, install browser extensions such as the [Adobe Experience Cloud Visual Helper](web-prerequisites.md#visual-authoring-prerequisites), which is required to load your pages in the web designer.

In certain cases, you may also find it easier to use a non-visual editor to apply modifications on a particular CSS selector, without the risk to modify other elements on a web page or to change the page structure.
 
To author your web experiences with the non-visual editor, follow the steps below.

1. From the **[!UICONTROL Edit content]** screen in the journey or campaign, unselect the **[!UICONTROL Visual editor]** option.

1. Click **[!UICONTROL Add a modification]** to start editing your web content.

    ![](assets/web-campaign-add-modification-button.png)

1. The non-visual editor displays. You can add your first modification using the left pane.

    ![](assets/web-non-visual-editor.png)

1. In the drop-down list, select the modification type. 
    
    Two types are available. They come with different options. See the links below for more details:

    * **[!UICONTROL CSS Selector]** - [Learn more](manage-web-modifications.md#css-selector)
    * **[!UICONTROL Page `<head>`]** - [Learn more](manage-web-modifications.md#page-head)

1. Click the **[!UICONTROL Add personalization]** button. The personalization editor opens.

    You can leverage the [!DNL Journey Optimizer] personalization editor with all its personalization and authoring capabilities. [Learn more](../personalization/personalization-build-expressions.md)

1. Enter your content and **[!UICONTROL Save]** your changes.

    ![](assets/web-non-visual-editor-ex-save.png)

1. Your first modification displays on top of the **[!UICONTROL Modifications]** pane.

    Click the **[!UICONTROL More actions]** button next to your modification and select **[!UICONTROL Info]** to display its details. You can also **[!UICONTROL Delete the modification]** if needed.

    ![](assets/web-non-visual-editor-ex-more.png){width="50%" align="left"}

    >[!NOTE]
    >
    >The **[!UICONTROL Modifications]** pane is the same as when using the [web designer](web-visual-editor.md). All the actions you can perform with it are detailed in [this section](manage-web-modifications.md#use-modifications-pane).

1. Click the **[!UICONTROL Add]** button on top of the **[!UICONTROL Modifications]** pane to add another modification, and repeat the steps above. 


1. In addition, you can select any element of your website and track the clicks on that element. To enable click tracking, and define the actions to track, click the second icon on the left rail, as shown below:
    
    ![](assets/web-campaign-click.png){width="50%" align="left"}

    Use the **Add Component** button to select a new action to track. Learn more about click tracking usage in [this section](monitor-web-experiences.md#use-click-tracking).


1. Click the arrow on top left of the screen to browse back to the journey or campaign edition screen. You can see the current number of changes and add more modifications.

    ![](assets/web-campaign-modifications.png)

    You can also switch to the web designer if desired. All your modifications will be preserved.
