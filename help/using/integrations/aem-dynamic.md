---
solution: Journey Optimizer
product: journey optimizer
title: Dynamic media
description: Use Dynamic media with Journey Optimizer
topic: Content Management
role: User
level: Beginner
exl-id: 3e777cc5-a935-4e68-9de7-60b241e78f63
---
# Work with Dynamic Media {#aem-dynamic}

## Get started with Dynamic Media {#gs-aem-dynamic}

The Asset selector now supports Dynamic media allowing you to seamlessly select and use approved dynamic media renditions within Journey Optimizer. Changes made to assets in Adobe Experience Manager are instantly reflected in your Journey Optimizer content, ensuring the most up-to-date versions are always in use without requiring manual updates.

Note that this integration is only available for customers using Dynamic Media Manager as a Cloud Service.

To learn more about Dynamic Media in Adobe Experience Manager as a Cloud Service, refer to [Experience Manager documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media){target="_blank"}.

>[!AVAILABILITY]
>
>For Healthcare customer, the integration is enabled only upon licensing the Journey Optimizer Healthcare Shield and Adobe Experience Manager Enhanced Security add-on offerings.


## Add and manage Dynamic media {#dynamic-media}

>[!IMPORTANT]
>
>Ensure that Dynamic Media with OpenAPI is enabled in Adobe Experience Manager as a Cloud Service. [Learn more](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media-open-apis/dynamic-media-open-apis-overview#enable-dynamic-media-open-apis)

Enhance and optimize your content for any screen or browser by inserting dynamic media from Adobe Experience Manager as a Cloud Service directly into your Journey Optimizer content.  You can then resize, crop, enhance, and make other adjustments as needed.

Note that Dynamic media is available for both Dynamic Media [Scene7 mode](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/dynamic/config-dms7){target="_blank"} and [with OpenAPI](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media-open-apis/dynamic-media-open-apis-overview){target="_blank"}.

>[!AVAILABILITY]
>
>Older versions of Outlook (including 2016) do not support rendering of content with Dynamic Media.  We are actively working on a permanent fix to enhance compatibility. In the meantime, apply the following guidelines:
>
>* For Dynamic Media Scene7 URLs: Append `?bfc=on` to the image URL. This enables automatic format negotiation, ensuring the most compatible image format is delivered based on the client's capabilities.
>
>* For Dynamic Media with Open API: Use the `.avif` format. This format includes built-in fallback mechanisms to deliver a compatible format when necessary.
>

To add an Adobe Experience Manager asset in your HTML content, follow these steps:

1. Drag and drop an **[!UICONTROL HTML component]** into your content.

1. Select **[!UICONTROL Show the source code]**.

    ![](assets/dynamic-media-1.png)

1. In the **[!UICONTROL Edit HTML]** menu, navigate to **[!UICONTROL Assets]** then click **[!UICONTROL Open asset selector]**.

    Alternatively, you can copy and paste the URL of your asset.

    ![](assets/dynamic-media-2.png)

1. Browse your AEM assets and select the one you wish to add to your content.

1. Adjust the image parameters (e.g., height, width, rotate, flip, brightness, hue, etc.) as needed to match your asset requirements.

    For a comprehensive list of image parameters that can be added to the URL, refer to  [Experience Manager documentation](https://experienceleague.adobe.com/en/docs/dynamic-media-developer-resources/image-serving-api/image-serving-api/http-protocol-reference/command-reference/c-command-reference){target="_blank"}.

    ![](assets/dynamic-media-3.png)

1. Click **[!UICONTROL Save]**.

Your content now includes dynamic media. Any updates you make in Experience Manager will automatically appear in Journey Optimizer.

## Personalize your Text overlay {#text-overlay}

Easily customize any dynamic media by replacing the existing text overlay with new text of your choice, allowing for seamless updates and personalization.

For example, using the experimentation functionality, you can update the existing text overlay by replacing it with a different text for each treatment, ensuring it is customized for each profile when they open their messages.

![](assets/dynamic-media-layout-1.png)

Note that **Text overlay personalization** is available exclusively in Dynamic Media [Scene7 mode](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/dynamic/config-dms7){target="_blank"}. Since Scene7 mode is not accessible for Healthcare customers, content is rendered using a Journey Optimizer binary copy of the image. For any exceptions, please contact your Adobe repressentative.

To personalize your text overlay, follow these steps:

1. Drag and drop an **[!UICONTROL HTML component]** into your content.

1. Select **[!UICONTROL Show the source code]**.

1. From the **[!UICONTROL Edit HTML]** menu, access **[!UICONTROL Assets]** then **[!UICONTROL Open asset selector]**.

    You can also simply copy and paste your assets URL.

1. Browse through your AEM assets and select the one you want to add to your content.

1. Replace the overlay with the desired text.

    ![](assets/do-not-localize/dynamic_media_layout.gif)

1. Update the images parameters:

    * **Layer**: enter the base element where your text is placed.
    * **Size**: update the size of your text block.
    * **TextAttr**: adjust the size of your text font.
    * **Pos**: set the position of your text in the image.

    >[!WARNING]
    >
    >The Layer parameter is required to update your dynamic media.

    ![](assets/dynamic-media-layout-2.png)

1. Click **[!UICONTROL Save]**.

Your content now includes your updated text overlay.

![](assets/dynamic-media-layout-3.png)

## Add and manage your Dynamic media template {#dynamic-media-template}

Easily add your Dynamic Media template in Journey Optimizer and update your media content whenever needed. You can now incorporate personalization fields into your media, allowing you to create more customized and engaging content within Journey Optimizer.

Note that **Dynamic media template** is available exclusively in Dynamic Media [Scene7 mode](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/dynamic/config-dms7). Since Scene7 mode is not accessible for Healthcare customers, content will not be rendered. For any exceptions, please contact Experience Manager support.

Learn more about [Dynamic media template](https://experienceleague.adobe.com/en/docs/dynamic-media-classic/using/template-basics/quick-start-template-basics){target="_blank"}.

### With image component {#image-component}

You can insert your dynamic template directly into your content using the Image component:

1. Open your campaign or journey and access your content.

1. Drag and drop an **Image component** into your layout. 

    For more information on Image component, refer to [this page](../email/content-components.md).

    ![](assets/dynamic-media-template-1.png)

1. Browse through your AEM assets and select the Dynamic media template you want to add to your content.

    ![](assets/dynamic-media-template-2.png)

1. In the **Image settings**, navigate to access the parameters of your dynamic media template.

    The available fields depend on the parameters added during the [template creation](https://experienceleague.adobe.com/en/docs/dynamic-media-classic/using/template-basics/creating-template-parameters#creating_template_parameters){target="_blank"} in Adobe Experience Manager.

    ![](assets/dynamic-media-template-3.png)

1. Fill in the different fields and use the personalization editor to add personalized content. You can use any attribute, such as the profile name, city, or other relevant details, to create a more customized experience.

    Learn more about personalization on [this page](../personalization/personalize.md).

    ![](assets/do-not-localize/dynamic_media_template.gif)

1. Conditional content can be applied to the Dynamic Media component to generate different variants of the content. [Learn more](../personalization/dynamic-content.md)

1. Click **[!UICONTROL Save]**.

Once you have performed your tests and validated the content, you can send your message to your audience. 

### With HTML component {#html-component}

You can insert your dynamic template directly into your content using the HTML component:

1. Open your campaign or journey and access your content.

1. Drag and drop an **HTML component** into your layout. 

    ![](assets/dynamic-media-template-4.png)

1. Select **[!UICONTROL Show the source code]**.

    ![](assets/dynamic-media-template-5.png)

1. From the **[!UICONTROL Edit HTML]** menu, access **[!UICONTROL Assets]** then **[!UICONTROL Open asset selector]**.

    You can also simply copy and paste your assets URL.

1. Adjust the image text parameters as needed to match your asset requirements.

    ![](assets/do-not-localize/dynamic_media_template_html.gif)

1. Click **[!UICONTROL Save]**.

Once you have performed your tests and validated the content, you can send your message to your audience. 

<!--
## Personalization with Text Overlay

Easily customize any dynamic media by replacing the existing text overlay with new text of your choice, allowing for seamless updates and personalization.

In this example, our goal is to update the existing text overlay by replacing it with a new validity date and adding a personalization block, ensuring it is customized for each profile when they open their messages.

1. Drag and drop an **[!UICONTROL HTML component]** into your content.

1. Select **[!UICONTROL Show the source code]**.

1. From the **[!UICONTROL Edit HTML]** menu, access **[!UICONTROL Assets]** then **[!UICONTROL Open asset selector]**.

    You can also simply copy and paste your assets URL.

1. Browse through your AEM assets and select the one you want to add to your content.

1. Replace the overlay with the desired text.

    Here we change the validity date from 31st December 2024 to the 1st July 2025.

1. Add the required personalization fields to your image.

1. Click **[!UICONTROL Save]**.

Your content now includes your updated text overlay and personalization.

## Add Dynamic media conditional content

Enable conditional content in your dynamic media to better target your audience and deliver a more personalized experience.

1. Drag and drop an **[!UICONTROL HTML component]** into your content.

1. Select **[!UICONTROL Show the source code]**.

1. From the **[!UICONTROL Edit HTML]** menu, access **[!UICONTROL Assets]** then **[!UICONTROL Open asset selector]**.

    You can also simply copy and paste your assets URL.

1. Browse through your AEM assets and select the one you want to add to your content.

1. Once your dynamic media is inserted to your content, select **[!UICONTROL Enable conditional]** content from your HTML component toolbar to create your different user experiences. 

1. From the Variant - 1, click **[!UICONTROL Select condition]** to fine tune your audience.

1. Choose your condition or create a new one if needed and click **[!UICONTROL Select]**.

    [Learn more about conditions](../personalization/create-conditions.md)

1. Select your **[!UICONTROL Component]** and access the **[!UICONTROL Settings]** menu.

1. In the **[!UICONTROL Custom Attributes]** menu, populate the Dynamic Media text and personalization fields to customize the content for your audience.

-->

## How-to video {#video}

Learn how to integrate Adobe Experience Manager Dynamic Media with Adobe Journey Optimizer to enable real-time content updates and personalization.

This tutorial covers how to modify images directly within AJO, add text overlays using HTML mode, create dynamic media templates in AEM for hyper-personalization, and personalize campaigns by tailoring content for different audience segments. This integration allows marketers to efficiently create engaging and personalized campaigns without switching between applications.

>[!VIDEO](https://video.tv.adobe.com/v/3457695/?learn=on&enablevpops=&autoplay=true)

