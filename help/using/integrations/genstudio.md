---
solution: Journey Optimizer
product: journey optimizer
title: Work with GenStudio for Performance Marketing into Journey Optimizer
description: Learn to work with GenStudio for Performance Marketing in Journey Optimizer
feature: Content Assistant, Integrations
topic: Content Management, Artificial Intelligence
badge: label="Limited availability" type="Informative"
role: User
level: Beginner, Intermediate
exl-id: c22a44a8-e4e2-453a-9ca2-b80f7c0edc19
---
# Work with GenStudio for Performance Marketing {#ajo-genstudio}

>[!CONTEXTUALHELP]
>id="ajo_genstudio_button"
>title="Use a template built with GenStudio"
>abstract="Thanks to the seamless integration with Adobe GenStudio for Performance Marketing, you can easily import a GenStudio template enhanced with the Adobe AI technology."

## Get started with GenStudio {#gs-genstudio}

[Adobe GenStudio for Performance Marketing](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/home){target="_blank"} is a generative AI-first application that lets marketing teams create their own ads and emails to drive impactful, personalized marketing campaigns that adhere to your brand standards and complies with your enterprise policies. By leveraging Adobe AI technology, it provides a comprehensive suite of tools that simplify the complexities of content creation and management so that creatives can focus on innovation.

>[!AVAILABILITY]
>
>* The GenStudio integration in [!DNL Adobe Journey Optimizer] is currently unavailable for use with the **Healthcare Shield** or **Privacy and Security Shield** add-on offerings.
>
>* This capability is available for the email channel only.

To enhance marketing efficiency and to maintain brand consistency, you can seamlessly integrate [!DNL **GenStudio for Performance Marketing**] experiences with [!DNL **Adobe Journey Optimizer**]. This enables you to leverage [!DNL GenStudio]'s AI-powered content creation alongside [!DNL Journey Optimizer]'s advanced orchestration capabilities.

![Import a GenStudio content into Adobe Journey Optimizer](../rn/assets/do-not-localize/genstudio.gif)

>[!INFO]
>
>To go further, check out this [overview](https://business.adobe.com/products/genstudio-for-performance-marketing.html#watch-overview){target="_blank"} and a [demo](https://business.adobe.com/products/genstudio-for-performance-marketing.html#demo){target="_blank"} of [!DNL Adobe GenStudio for Performance Marketing].

➡️ [Discover this feature in video](#video)

## Prerequisites {#genstudio-prerequisites}

To use the [!DNL GenStudio for Performance Marketing] integration with [!DNL Journey Optimizer], ensure the following requirements are met:

* Your organization must have an active license for [!DNL GenStudio for Performance Marketing].

* Both [!DNL GenStudio for Performance Marketing] and [!DNL Adobe Journey Optimizer] must belong to the same IMS organization.

* Users must have at least the **Collaborator** role or higher in [!DNL GenStudio for Performance Marketing] to utilize the integration features. [Learn more about user roles in GenStudio](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/intro/user-roles){target="_blank"}


<!--
To access the GenStudio integration in [!DNL Adobe Journey Optimizer] feature, users need to be granted the **xxx** permission. [Learn more](../administration/permissions.md)

>[!IMPORTANT]
>
>* Before starting using this capability, read out related [Guardrails and Limitations](#generative-guardrails).
-->



<!--
Guardrails and limitations {#genstudio-guardrails}

General guidelines for using the GenStudio integration in [!DNL Adobe Journey Optimizer] for email generation are listed below:

See if guidelines/limitations such as the ones listed [here](../content-management/gs-generative.md#generative-guardrails) for AI Assistant can apply.

The following limitations apply to GenStudio integration in [!DNL Adobe Journey Optimizer]:
-->


## Leverage GenStudio capabilities in Journey Optimizer {#use-genstudio}

The [!DNL GenStudio for Performance Marketing] and [!DNL Journey Optimizer] integration enables you to have marketers from your company work better together to streamline processes.

For example, a technical marketer, who uses [!DNL Journey Optimizer] to develop and automate email campaigns, can collaborate with a performance marketer who creates content using [!DNL GenStudio].

With this integration, both can work together to easily integrate on-brand content from [!DNL GenStudio] into [!DNL Journey Optimizer], delivering engaging emails that target specific customer segments and drive sales.

### Key capabilities {#genstudio-capabilities}

This integration unlocks powerful capabilities for your marketing organization:

* **AI-powered content generation**: Leverage Adobe's generative AI to create multiple on-brand email variations efficiently, with intelligent copy suggestions and design elements.

* **Seamless workflow integration**: Export Journey Optimizer email templates to GenStudio, create variations with AI prompts, and import them back into Journey Optimizer in a streamlined process.

* **Centralized asset management**: Access GenStudio's ContentHub, powered by Adobe Experience Manager Assets, to organize, store, and retrieve all digital assets in one centralized location.

* **Content experimentation**: Import multiple GenStudio email variations into Journey Optimizer and leverage experimentation capabilities to test and identify the best-performing content.

* **Performance-driven insights**: Track campaign performance with AI-powered analytics to understand which creative elements resonate with your audience and optimize future campaigns.

### Common use cases {#genstudio-use-cases}

The integration between [!DNL GenStudio for Performance Marketing] and [!DNL Journey Optimizer] supports various marketing scenarios:

* **Product launch campaigns**: Quickly generate multiple email variants for product announcements, test them with different audience segments, and scale the winning version across your customer base.

* **Holiday and seasonal promotions**: Produce time-sensitive campaign content at scale using GenStudio templates, ensuring brand consistency while meeting tight deadlines.

* **A/B testing at scale**: Create numerous content variations in GenStudio and systematically test them in Journey Optimizer to continuously improve email performance.

* **Multi-segment personalization**: Generate tailored content for different customer personas in GenStudio, then deploy each variation to its corresponding segment in Journey Optimizer for maximum relevance.

## Use the GenStudio integration {#how-to-use}

The integration workflow consists of two main steps: exporting a template from Journey Optimizer to GenStudio, and importing GenStudio experiences back into Journey Optimizer.

### Export an HTML template from Journey Optimizer to GenStudio {#export-from-ajo-to-genstudio}

Start by exporting a [!DNL Journey Optimizer] HTML template including your brand's guidelines to [!DNL GenStudio for Performance Marketing]. Follow the steps below.

1. In [!DNL Journey Optimizer], access the content of your email in a journey or campaign. [Learn how](../email/get-started-email-design.md#key-steps)

1. In the Email Designer, select **[!UICONTROL Export HTML]** from the **[!UICONTROL More]** button.

    ![](assets/genstudio-export-template.png){zoomable="yes"}

1. Upload this HTML exported template into [!DNL GenStudio for Performance Marketing]. <!--Make sure you detect the fields that the generative AI uses to insert content in order to create an actionable template.-->

    >[!NOTE]
    >
    >Learn how to upload an HTML template into [!DNL GenStudio] in the [Adobe GenStudio for Performance Marketing User Guide](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/content/templates/use-templates#templates-from-ajo-and-marketo){target="_blank"} dedicated section.

1. In GenStudio, use this template to create several email variations with AI prompts and save them.

    >[!NOTE]
    >
    >Learn how to create email experiences in the GenStudio dedicated [section](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/create/create-email-experience){target="_blank"}.
 
### Leverage GenStudio experiences in Journey Optimizer {#leverage-genstudio-experiences}

Once you have created email variations in GenStudio, import them back into [!DNL Journey Optimizer] to use in your campaigns. Follow the steps below.

1. In [!DNL Journey Optimizer], [add an email](../email/create-email.md) to a campaign.

1. From the campaign configuration screen, go through the [Edit content screen](../email/create-email.md#define-email-content) and click **[!UICONTROL Edit email body]** to open the Email Designer. [Learn how](../email/get-started-email-design.md#key-steps)

1. On the Email Designer home page, select **[!UICONTROL Import HTML]** and click the **[!UICONTROL Adobe GenStudio for Performance Marketing]** button.

    ![](assets/genstudio-pem-import-email.png){zoomable="yes"}

1. Browse the GenStudio experiences to start building your content. You can filter the experiences on several criteria such as products, personas, brands, or even colors.

    <!--![](assets/genstudio-filter-experiences.png){zoomable="yes"}-->

1. Select an experience and click **[!UICONTROL Use]**.

    ![](assets/genstudio-use-experience.png){zoomable="yes"}

1. Select the folder where you want to import the GenStudio experience.

    ![](assets/genstudio-choose-destination.png){zoomable="yes"}

1. The selected content displays in the Email Designer.

    ![](assets/genstudio-email-content.png){zoomable="yes"}

    >[!NOTE]
    >
    >GenStudio experiences [created from a [!DNL Journey Optimizer] template](#export-from-ajo-to-genstudio) are imported directly into the Email Designer with full editing capabilities. GenStudio experiences created without a [!DNL Journey Optimizer] template are imported into [compatibility mode](../email/existing-content.md), which may have limited editing functionality.

1. Use the [email content editing tools](../email/content-from-scratch.md) and [personalization fields](../personalization/personalize.md) to edit your email as needed. Save your content.

1. Go back to the campaign summary page, and click **[!UICONTROL Create experiment]** to use experimentation. [Learn how to create a content experiment](../content-management/content-experiment.md)

    <!--![](assets/genstudio-create-experiment.png){zoomable="yes"}-->

1. Create several treatments and repeat the steps above to import and quickly leverage the other email experience variations that you created in [!DNL GenStudio].

    ![](assets/genstudio-define-treatments.png){zoomable="yes"}

1. Save your changes and [activate](../campaigns/review-activate-campaign.md) the campaign.

1. After running the experiment, track how your campaign treatments are performing with the [experimentation campaign report](../reports/campaign-global-report-cja-experimentation.md). You can then interpret the results of your experiment. [Learn how](../content-management/get-started-experiment.md#interpret-results)

## Frequently asked questions {#genstudio-faq}

Find answers to common questions about the [!DNL GenStudio for Performance Marketing] integration with [!DNL Journey Optimizer].

+++Can I use the GenStudio integration for channels other than email?

Currently, the [!DNL GenStudio for Performance Marketing] integration is available for the email channel only. Support for additional channels may be added in future releases.
+++

+++Is the GenStudio integration available for all Journey Optimizer customers?

The integration is currently unavailable for organizations using the **Healthcare Shield** or **Privacy and Security Shield** add-on offerings.
+++

+++Can I edit GenStudio content after importing it into Journey Optimizer?

Yes, after importing GenStudio experiences into [!DNL Journey Optimizer], you can use the Email Designer's [content editing tools](../email/content-from-scratch.md) and add [personalization fields](../personalization/personalize.md) to further customize your email content.
+++

+++What happens to GenStudio experiences created without a Journey Optimizer template?

GenStudio experiences created from a [!DNL Journey Optimizer] template are imported directly into the Email Designer. GenStudio experiences created without a [!DNL Journey Optimizer] template are imported into [compatibility mode](../email/existing-content.md).
+++

+++Can I test multiple GenStudio email variations in Journey Optimizer?

Yes, you can create several content treatments by importing different GenStudio email variations and use Journey Optimizer's [content experimentation](../content-management/content-experiment.md) feature to test which variation performs best with your audience.
+++

+++How does GenStudio ensure brand consistency?

GenStudio uses AI-powered brand checks to ensure all generated content adheres to your brand standards and guidelines. When you upload templates that include your brand elements, GenStudio applies these standards to all content variations created within the platform.
+++

+++Can I collaborate with other team members on GenStudio experiences?

Yes, GenStudio is designed for collaboration. Multiple team members with appropriate permissions can work together on creating and refining email experiences before importing them into [!DNL Journey Optimizer].
+++

## How-to video {#video}

Discover the process of exporting an email template from Journey Optimizer to GenStudio for Performance Marketing, crafting brand-compliant emails using the template in GenStudio, and importing them seamlessly back into Journey Optimizer.

>[!VIDEO](https://video.tv.adobe.com/v/3456038/?quality=12)