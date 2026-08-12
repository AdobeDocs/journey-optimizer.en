---
solution: Journey Optimizer
product: journey optimizer
title: Dynamic media
description: Use Dynamic media with Journey Optimizer
topic: Content Management
role: User
level: Beginner
exl-id: 3e777cc5-a935-4e68-9de7-60b241e78f63
TQID: https://experienceleague.adobe.com/bgBuZlYcuJ1VpBZIlpGA4WIYZ6ufqNMnxlBoUvPpVqg
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
subfeature_v2:
  - id: c7dc31c0-c4f7-42a7-8cf5-a8c5aeb0de74
    internal-label: Experience Manager Assets integration
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: bcc5edb5-84c3-4940-9f84-ed88b6c16274
    internal-label: Experimentation
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Work with dynamic media {#aem-dynamic}

>[!BEGINSHADEBOX]

**On this page:** Learn how to insert, adjust, and personalize Adobe Experience Manager dynamic media, including text overlays and dynamic media templates, within Journey Optimizer content.

>[!ENDSHADEBOX]

## Get started with dynamic media {#gs-aem-dynamic}
 
The Asset selector now supports Dynamic media allowing you to seamlessly select and use approved dynamic media renditions within Journey Optimizer. Changes made to assets in Adobe Experience Manager are instantly reflected in your Journey Optimizer content, ensuring the most up-to-date versions are always in use without requiring manual updates.

Note that this integration is only available for customers using Dynamic Media Manager as a Cloud Service.

To learn more about Dynamic Media in Adobe Experience Manager as a Cloud Service, refer to [Experience Manager documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media){target="_blank"}.

>[!AVAILABILITY]
>
>For Healthcare customer, the integration is enabled only upon licensing the Journey Optimizer Healthcare Shield and Adobe Experience Manager Extended Security for Healthcare add-on offerings.

## Considerations

* Ensure that Dynamic Media with OpenAPI is enabled in Adobe Experience Manager as a Cloud Service. [Learn more](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media-open-apis/dynamic-media-open-apis-overview#enable-dynamic-media-open-apis){target="_blank"}.

* Dynamic media integration with Adobe Journey Optimizer is available for both Dynamic Media [Scene7 mode](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/dynamic/config-dms7){target="_blank"} and [with OpenAPI](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media-open-apis/dynamic-media-open-apis-overview){target="_blank"}.

* For Dynamic Media Scene7 assets, Journey Optimizer adds default modifiers (`bfc=off&fmt=png-alpha`) at the start of the URL. If your preset also sets `fmt` or `bfc`, it takes precedence, since Scene7 uses the last occurrence of a repeated parameter. To avoid unexpected results, remove `fmt`/`bfc` from the preset, or move it before the default modifiers in the URL.

* By design, the asset selector returns a `/images`-based URL format. If you want to deliver an asset in its original formatm, for example, GIF or SVG, you need to manually update the URL to use the `/content` path instead. Learn more in [Dynamic Media best practices documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dm-journey/dm-best-practices#deliver-gif-images){target="_blank"}.


## Add and manage Dynamic media {#dynamic-media}

Enhance and optimize your content for any screen or browser by inserting dynamic media from Adobe Experience Manager as a Cloud Service directly into your Journey Optimizer content.  You can then resize, crop, enhance, and make other adjustments as needed.


<!--
>[!AVAILABILITY]
>
>Older versions of Outlook (including 2016) do not support rendering of content with Dynamic Media.  We are actively working on a permanent fix to enhance compatibility. In the meantime, apply the following guidelines:
>
>* For Dynamic Media Scene7 URLs: Append `?bfc=on` to the image URL. This enables automatic format negotiation, ensuring the most compatible image format is delivered based on the client's capabilities.
>
>* For Dynamic Media with Open API: Use the `.avif` format. This format includes built-in fallback mechanisms to deliver a compatible format when necessary.
>
-->

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

>[!AVAILABILITY]
>
>**Text overlay personalization** is available exclusively in Dynamic Media [Scene7 mode](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/dynamic/config-dms7){target="_blank"}. Since Scene7 mode is not accessible for Healthcare customers, content is rendered using a Journey Optimizer binary copy of the image. For any exceptions, please contact your Adobe representative.

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

Learn more about [Dynamic media template](https://experienceleague.adobe.com/en/docs/dynamic-media-classic/using/template-basics/quick-start-template-basics){target="_blank"}.


>[!AVAILABILITY]
>
>**Dynamic media template** is available exclusively in Dynamic Media [Scene7 mode](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/assets/dynamic/config-dms7). Since Scene7 mode is not accessible for Healthcare customers, content will not be rendered. For any exceptions, please contact Experience Manager support.


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

## Insert countdown timer {#countdown}

Create urgency and maximize conversions with Dynamic Media countdown timers that update in real-time when recipients open your emails. This feature is ideal for flash sales, limited-time offers, and time-sensitive promotions.

For example, as a marketer for a retail brand, you're running a 48-hour flash sale. By using the countdown timer in your promotional emails:

* Recipients who open immediately see "47 hours remaining"
* Recipients who open 24 hours later see "23 hours remaining"  
* Recipients who open after the sale ends see "Time's up!"

For more information on how to add countdown timers to your Dynamic Media template in Adobe Experience Manager, refer [to this document](assets/do-not-localize/countdown.pdf).


1. In **[!DNL Adobe Experience Manager]**, create a Dynamic Media template and add a countdown timer component to it.

    ![](assets/timer-1.png)

1. In **[!DNL Journey Optimizer]**, create a new campaign or open an existing one, then access the Email Designer.

1. Drag and drop an **HTML** or **Asset** component into your email content.

1. Hover over the component and click **[!UICONTROL Show the source code]** (for HTML components) or **[!UICONTROL Browse]** (for Asset components).

    ![](assets/timer-2.png)

1. From the **[!UICONTROL Edit HTML]** menu, navigate to **[!UICONTROL Assets]** and click **[!UICONTROL Open asset selector]** to browse and select your published Dynamic Media template.

    ![](assets/timer-3.png)

1. Enable the pills experience by toggling Pills to On. This improves readability by hiding long attribute paths.

    ![](assets/timer-6.png)

1. In the **[!UICONTROL Custom attributes]** menu, configure any customizable URL parameters as needed for your template.

    Click **[!UICONTROL Save]** when finished.

    ![](assets/timer-4.png)

1. Alternatively, you can also access the parameters of the Dynamic Media template by selecting the asset in the Email Designer, then accessing the **[!UICONTROL Settings]** menu.

    Configure the following:

    * **Banner text**: The text displayed with your timer
    * **End time**: The date and time when the countdown expires. Enter the time in GMT (Greenwich Mean Time) only. The system does not accept other time zones.
    * **Fallback text**: The message shown after the timer ends

    ![](assets/timer-5.png)

1. Click **[!UICONTROL Preview]** to view the timer with real-time countdown updates and verify your configuration.

When recipients open the email, they see the accurate time remaining for your flash sale. If they reopen the email later, the countdown automatically updates to reflect the current time remaining. After the end date, the default message appears automatically.

## How-to video {#video}

Learn how to integrate Adobe Experience Manager Dynamic Media with Adobe Journey Optimizer to enable real-time content updates and personalization.

This tutorial covers how to modify images directly within AJO, add text overlays using HTML mode, create dynamic media templates in AEM for hyper-personalization, and personalize campaigns by tailoring content for different audience segments. This integration allows marketers to efficiently create engaging and personalized campaigns without switching between applications.

>[!VIDEO](https://video.tv.adobe.com/v/3457695/?learn=on&enablevpops=&autoplay=true)

