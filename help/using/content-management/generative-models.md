---
solution: Journey Optimizer
product: journey optimizer
title: Manage brand
description: Learn how to create and manage your generative models
topic: Content Management
role: User
level: Beginner, Intermediate
exl-id: 9ef6b02c-0a17-4b46-bcd3-8e922eef059a
---
# Create and manage generative models {#generative-models}

Expand your AI image creation capabilities with built-in models, custom Firefly models, and third-party image generation providers to meet your specific needs and improve brand alignment.

Choose the right model for your needs:

- **[!UICONTROL Adobe model]**, powered by Firefly Image Model 4, is provided out of the box and ready to use for immediate image generation without additional setup.
- **[!UICONTROL Partner model]**, powered by Gemini 2.5 Flash, offers specialized capabilities for specific use cases. For a step-by-step workflow that uses **Gemini** with **text overlays** on images in AI Assistant, see [Use Gemini as generative model for text-overlay image](generative-uc.md#generative-gemini).
- **[!UICONTROL Custom models]** are brand-specific models trained on your own assets and added by your organization.

    Learn more on **[!UICONTROL Custom models]** in [Adobe Firefly documentation](https://helpx.adobe.com/firefly/web/work-with-enterprise-features/train-custom-models/custom-models-overview.html)

Once configured, you can select any of your generative models when creating images in your content. [Learn more about generating images](generative-image.md).

## Manage generative models

Manage your generative models from a centralized location. View all available models, filter and search to find specific ones, and configure their settings for your brands.

1. From the **[!UICONTROL Brands]** menu, select the **[!UICONTROL Generative models]** tab.

    ![](assets/gen-model-manage-1.png){zoomable="yes"}

1. Click the ![](assets/do-not-localize/Smock_Filter_18_N.svg) icon to access the filter menu. Filter models by **[!UICONTROL Type]** or **[!UICONTROL Status]**.

    ![](assets/gen-model-manage-2.png){zoomable="yes"}

1. Use the search bar to find a specific generative model by name.

1. Click the ![](assets/do-not-localize/Smock_More_18_N.svg) icon to access the advanced menu, where you can enable or disable your model, or delete it.

    Note that only **[!UICONTROL Custom models]** can be deleted.

    ![](assets/gen-model-manage-6.png){zoomable="yes"}

1. Click **[!UICONTROL Add model]** to create a new generative model from scratch.

You can now select any of your generative models when creating images in your content. [Learn more about generating images](generative-image.md).

## Add a generative model

>[!IMPORTANT]
>
>Creating custom Firefly models requires a Firefly ETLA agreement. 

Custom Firefly models are brand-specific AI models trained on your own assets, enabling you to generate images that align precisely with your brand identity, style, and visual guidelines. 

By creating custom Firefly model providers, you can expand your AI capabilities beyond the default models and ensure that generated content consistently reflects your brand's unique aesthetic and requirements.

➡️ [Learn how to train your custom model](https://helpx.adobe.com/firefly/web/work-with-enterprise-features/train-custom-models/train-firefly-custom-models.html)

1. From the **[!UICONTROL Brands]** menu, access the **[!UICONTROL Generative Models]** tab and click **[!UICONTROL Add model]**.

    ![](assets/gen-model-manage-4.png){zoomable="yes"}

1. Enter a **[!UICONTROL Name]** for your model.

1. Enter your **[!UICONTROL Model ID]**.

    +++ Find your Firefly model ID

    1. Access the Firefly website and navigate to your trained models.
    1. Access the [Preview & test](https://helpx.adobe.com/firefly/web/work-with-enterprise-features/train-custom-models/train-firefly-custom-models.html#preview-and-test) menu.
    1. In the URL, locate the value after `customModelId=`. Copy this value to use as your model ID.

    For more information, refer to the [Firefly custom models documentation](https://helpx.adobe.com/firefly/web/work-with-enterprise-features/train-custom-models/manage-custom-models.html). 
    
    ![](assets/gen-model-manage-10.png){zoomable="yes"}

    +++

    </br>

    ![](assets/gen-model-manage-5.png){zoomable="yes"}

1. Optionally, enter a **[!UICONTROL Description]** to help identify the model.

1. Click **[!UICONTROL Test connection]** to verify the model configuration.

1. Once the connection test is successful, click **[!UICONTROL Save]** to save your model configuration.

     ![](assets/gen-model-manage-7.png){zoomable="yes"}

1. After saving, your custom model is added to your models list. You can disable or delete it at any time.

     ![](assets/gen-model-manage-8.png){zoomable="yes"}

<!--
1. Once the connection test is successful, choose whether to enable the model for selected brands.

1. Enable or disable the option to connect the model to all brands.

    If disabled, select which brands this model should be applied to.
-->

Once configured, you can select any of your custom generative models when creating images in your content. [Learn more about generating images](generative-image.md).

![](assets/gen-model-manage-9.png){zoomable="yes"}
