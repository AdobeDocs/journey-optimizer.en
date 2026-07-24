---
title: Author single-page applications
description: Learn how to author SPAs and apply modifications to different views in Journey Optimizer
feature: Web Channel
topic: Content Management
role: User
level: Intermediate
exl-id: b33e4bca-d2e9-4610-9f04-008d47f686d0
TQID: https://experienceleague.adobe.com/clX0VeCEzwDOgxyFrzVaBIx-eH90KEYaHGTMzf2xvQc
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: c618a0dc-1818-4c6d-9916-0d92e6796f24
    internal-label: Web channel
  - id: d056adbe-402d-4f42-9746-f3d424e598b1
    internal-label: Web SDK
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: bcc5edb5-84c3-4940-9f84-ed88b6c16274
    internal-label: Experimentation
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: e9001ce2-5245-4a8e-8601-dd958009072f
    internal-label: Web experience
---
# Author single-page applications {#web-author-spas}

>[!BEGINSHADEBOX]

**On this page:** Learn how to author single-page applications in Adobe Journey Optimizer by defining views in the Web SDK implementation, discovering them in the web designer with browse mode, and applying modifications to selected views.

>[!ENDSHADEBOX]

## About views {#about-views}

>[!CONTEXTUALHELP]
>id="ajo_web_designer_modifications_views"
>title="Apply changes to selected views"
>abstract="The changes will be applied only for selected views. Views can be discovered using the **Browse** mode and navigate to them. Can't find the view you are looking for?"
>additional-url="https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/overview.html" text="Learn more"

**Single-page applications** (SPAs) can now be authored in the web designer visual editor. This allows you to select which specific **views** you want to apply your web page modifications to.

[Learn how to author single-page applications in this video](#video)

A view can be defined as a whole site or a group of visual elements on a site, such as the home page, the entirety of the products site or the delivery preferences frame on all the checkout pages.

One-time developer setup is needed to define the views in the Adobe Experience Platform Web SDK implementation. This enables you to create and run Adobe Journey Optimizer web campaigns on SPAs.

## Define views in the Web SDK implementation {#define-views}

XDM views can be leveraged in Adobe [!DNL Journey Optimizer] to empower marketers to run web personalization and experimentation campaigns on SPAs via the web visual editor. [Learn more](web-spa-implementation.md)

To be able to access and author views in the [!DNL Journey Optimizer] user interface, make sure you follow the steps listed in [this section](web-spa-implementation.md#implement-xdm-views).

## Discover views in the web designer {#discover-views}

Once SPAs setup is done in the Adobe Experience Platform Web SDK implementation, you need to navigate through all the views of your website that you want to apply modifications to. Follow the steps below.

1. [Create a web journey or campaign](create-web.md) and access the [web designer](web-visual-editor.md).

    The view you are currently in is displayed on top left.

    ![](assets/web-designer-view-home.png)

1. Swap to **[!UICONTROL Browse]** mode. [Learn more](web-visual-editor.md#browse-mode)

    ![](assets/web-designer-view-browse.png)

1. Navigate between the different pages of the website to discover them all. The view name displayed on top changes when you go through another page.

    ![](assets/web-designer-other-view.png)

## Apply modifications to other views {#apply-modifications-views}

Once you added a modification while being in a specific view, you can apply it to other selected views. Follow the steps below.

>[!CAUTION]
>
>If you have not discovered views using the **[!UICONTROL Browse]** mode, you will not be able to select them for applying your modifications. [Learn more](#discover-views)

1. Select the **[!UICONTROL Modifications]** icon to display the corresponding pane on the left.

    ![](assets/web-designer-view-modifications-pane.png)

1. Select any modification and click the **[!UICONTROL More actions]** button next to it. Select **[!UICONTROL Apply to more views]**.

    ![](assets/web-designer-modifications-more-actions.png)

1. Select the views you want to apply your changes to.

    ![](assets/web-designer-modifications-apply-to.png)

1. Click **[!UICONTROL Apply]**.

1. Swap to **[!UICONTROL Browse]** mode to check the modifications are applied on the desired pages.

    ![](assets/web-designer-modifications-applied-view.png)

## How-to video{#video}

This video explains how to:

* Discover SPA views using **[!UICONTROL Browse]** mode
* Perform authoring on the current view
* Apply website modifications to multiple views or to all views that were discovered
* Do bulk actions on modifications

>[!VIDEO](https://video.tv.adobe.com/v/3424536/?quality=12&learn=on)
