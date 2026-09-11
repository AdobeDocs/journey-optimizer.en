---
solution: Journey Optimizer
product: journey optimizer
title: Personalize your email background
description: Learn how to personalize your email background
feature: Email Design
topic: Content Management
role: User
level: Beginner, Intermediate
keywords: background, email, color, editor
exl-id: 09a2e892-8c6f-460d-8b12-5026582c6ed0
TQID: https://experienceleague.adobe.com/8kFppIm3Q-zHDqalE0Vt0CK5Z1ts9fGspVu476TapSk
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: ee5bb250-0884-4d71-86eb-d8489e8bcadd
    internal-label: Email design
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
  - id: c41e8697-e629-4c38-96b3-564faaa17acf
    internal-label: Dynamic content
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Personalize your email background {#backgrounds}

>[!BEGINSHADEBOX]

**On this page:** Learn how to set background colors and images at the body, viewport, structure, and column levels of your email in the Email Designer.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ac_edition_backgroundimage"
>title="Background settings"
>abstract="You can personalize the background color or background image for your content. Note that background image is not supported by all email clients." 

Backgrounds help you reinforce your brand identity and draw attention to key areas of your email. In the Email Designer, you can set a background color or image at different levels of your content — from the overall body down to individual structures and columns — giving you precise control over how backgrounds render throughout your email.

Keep the following best practices in mind when setting backgrounds in the Email Designer:

* Apply a background color to the body only if your design requires it.
* Prefer setting background colors at the column level whenever possible.
* Avoid using background colors on image or text components, as they are harder to manage.

The following settings let you apply a background color or image at any level of your email content, from the body down to individual structures and columns.

## Set a background color {#background-color}

1. **Body background color** - Set a **[!UICONTROL Background color]** for the whole email. Make sure you select **[!UICONTROL Body]** in the **[!UICONTROL Navigation tree]** accessible from the left palette and use the dedicated option from the **[!UICONTROL Styles]** tab on the right.

    ![](assets/background_1.png)

1. **Viewport background color** - Set a **[!UICONTROL Viewport color]** to apply the same background color across all structure components, independently of the body's background color.

    ![](assets/background_2.png)

1. **Structure background color** - To apply a background color to a single structure component, select it directly in the canvas or from the left palette, and set a specific color for that structure.

    ![](assets/background_3.png)

    >[!TIP]
    >
    >In that case, make sure you do not set a viewport background color as it may hide the structure background colors.

1. **Column background color** - Set a background color at the column level. Again, make sure you select the desired column from the left palette, and set a specific color for that column.

    ![](assets/background_5.png)

    >[!TIP]
    >
    >This is the most common use case and a best practice, since it gives you more flexibility when editing the rest of your email content.

## Set a background image {#background-image}

You can also set a **[!UICONTROL Background image]** for the content of a structure or column component. This is most commonly used at the structure level; setting one at the column level is possible but rarely used.

>[!NOTE]
>
>Some email programs do not support background images. When not supported, the row background color will be used instead. Make sure you select an appropriate fallback background color in case the image cannot be displayed.

Once a background image is set, use the **[!UICONTROL Image placement]** dropdown to control how the image fills the structure or column:

**Scale to fill, centered:**

* **[!UICONTROL Fit]** - Stretches the image to fill the container on both axes, without preserving its aspect ratio.
* **[!UICONTROL Full Width]** - Scales the image proportionally to the container's width and centers it vertically.
* **[!UICONTROL Full Height]** - Scales the image proportionally to the container's height and centers it horizontally.

**Scale to fill, anchored to an edge:**

* **[!UICONTROL Full Width - Top]** - Same as **[!UICONTROL Full Width]**, anchored to the top of the container. Overflow is cropped at the bottom.
* **[!UICONTROL Full Width - Bottom]** - Same as **[!UICONTROL Full Width]**, anchored to the bottom of the container. Overflow is cropped at the top.
* **[!UICONTROL Full Height - Left]** - Same as **[!UICONTROL Full Height]**, anchored to the left of the container. Overflow is cropped on the right.
* **[!UICONTROL Full Height - Right]** - Same as **[!UICONTROL Full Height]**, anchored to the right of the container. Overflow is cropped on the left.

**Tile:**

* **[!UICONTROL Repeat]** - Tiles the image at its original size to fill the container.

**Position without scaling:**

* **[!UICONTROL Left]**, **[!UICONTROL Right]**, **[!UICONTROL Center]**, **[!UICONTROL Top]**, **[!UICONTROL Bottom]** - Positions the image at its original size, anchored to the corresponding edge or center of the container.

![](assets/background_4.png)

>[!NOTE]
>
>The edge-anchored options give you more control over which part of the image stays in view when it doesn't match the structure's proportions, compared to the centered options above.

{{$include /help/_includes/do-not-localize/email/ai-augmented-backgrounds.md}}
