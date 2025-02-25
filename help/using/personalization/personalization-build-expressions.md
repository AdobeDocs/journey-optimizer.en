---
solution: Journey Optimizer
product: journey optimizer
title: About the personalization editor
description: Learn how to work with the personalization editor.
feature: Personalization
topic: Personalization
role: Data Engineer
level: Intermediate
keywords: expression, editor, about, start
exl-id: 1ac2a376-a3a8-41ae-9b04-37886697f0fc
---
# Get started with the personalization editor {#build-personalization-expressions}

>[!CONTEXTUALHELP]
>id="ajo_perso_editor"
>title="About the personalization editor"
>abstract="The personalization editor allows you to select, arrange, customize and validate all the data to create a customized personalization for your content."

>[!CONTEXTUALHELP]
>id="ajo_perso_editor_autocomplete"
>title="Auto complete"
>abstract="Toggling on this option allows the system to automatically complete your code and make suggestions while you are typing your expression. This option is available for HTML and Text formats only."

The personalization editor is the centerpiece of the personalization in [!DNL Journey Optimizer]. It is available in every context where you need to define personalization like emails, push and offers.

In the personalization editor interface, you will select, arrange, customize and validate all the data to create a customized personalization for your content.

 ![](assets/perso_ee1.png)

## Available personalization sources {#sources}

The left part of the screen displays a domain selector that lets you select the source for personalization. Available sources are:

* **[!UICONTROL Profile attributes]** : lists all the references associated to the profile schema described in [Adobe Experience Platform Data Model (XDM) documentation](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}.
* **[!UICONTROL Audiences]** : lists all the audiences created in Adobe Experience Platform Segmentation service. More information on segmentation available [here](https://experienceleague.adobe.com/docs/experience-platform/segmentation/home.html){target="_blank"}.
* **[!UICONTROL Offer decisions]** : lists all the offers associated to a specific placement. Select the placement then insert the offers in your content. For a complete documentation on how to manage offers, refer to [this section](../offers/get-started/starting-offer-decisioning.md).
* **[!UICONTROL Contextual attributes]** : when a channel action activity (Email, push, SMS) is used in a journey or campaign, contextual attributes related to events and properties are available for personalization. An exemple of personalization leveraging contextual attributes is presented in [this section](personalization-use-case.md).
* **[!UICONTROL Helper functions]** : lists all the helper functions available to perform operations on data, such as calculations, data formatting or conversions, conditions, and manipulate them in the context of personalization. Learn more in [this section](functions/functions.md).

## Add personalization attributes {#add}

Click the + button to add an attribute into your personalization expression.

The ellipsis menu next to the "+" icon allows you to get more details for each variable and to add your most frequently used attributes to favorites. [Learn how to add attributes to favorites](personalization-favorites.md)

>[!NOTE]
>
>If you are targeting an audience with enrichment attributes generated using a composition workflow, you can leverage these enrichment attributes to personalize your message. [Learn how  to use audiences enrichment attributes](../audience/about-audiences.md#enrichment)

Additionally, you can define default fallback text that will display if a string-type profile attribute is empty. To do this, click the ellipsis button next to the attribute and select **[!UICONTROL Insert with fallback text]**. Write the text that should display by default if the attribute's value is empty for a profile then click **[!UICONTROL Add]**.

![](assets/attribute-details.png)

In the following example, the personalization editor lets you select the profiles that have their birthday today then complete the customization by inserting a specific offer corresponding to this day.

 ![](assets/perso_ee2.png)

Once your personalization expression is ready, you need to have it validated by the personalization editor. Learn more in [this section](personalization-validation.md).
