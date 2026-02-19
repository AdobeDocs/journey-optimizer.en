---
solution: Journey Optimizer
product: journey optimizer
title: Convert images to HTML templates
description: Learn how to use the AI-powered image to HTML converter to convert image designs into editable HTML email templates
feature: Email Design
topic: Content Management, Artificial Intelligence
role: User
level: Beginner
badge: label="Limited availability" type="Informative"
keywords: email, template, image, HTML, AI, design, converter
exl-id: d13467b7-2f3c-4707-a7e0-9b46cb6cafb1
---
# Convert images to HTML templates {#image-to-html}

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

[!DNL Journey Optimizer] helps you dramatically speed up email creation by converting static image designs into fully customizable, modular HTML email content templates.

By leveraging generative AI technology, an integrated tool analyzes the layout, typography, colors, and visual elements in your image and generates clean, modular HTML code that maintains design fidelity while ensuring full editability with the [Email Designer](../email/get-started-email-design.md). 

This no-code capability enables marketers to transform visual assets from graphic designers or design tools into responsive, editable email templates that can be saved and reused across multiple journeys and campaigns—without requiring technical expertise.

The main key benefits are as follows:

* **Faster than hand-coding** - The converter turns images into editable HTML in minutes, so you can skip the manual time-consuming mockup-to-HTML workflow.
* **No technical skills needed** - Marketers can produce and adjust templates without design or development support.
* **Reusable across campaigns** - Save templates to your library and use them in any journey or campaign.
* **Stays true to the design** - Output matches your layout and styling while being fully compatible with the Email Designer.

<!--* **Design fidelity**: Maintain visual consistency with your original design while creating fully editable content
* **Email compatibility**: Generate HTML that works seamlessly with the Email Designer and across email clients-->

+++ Common use cases

The image to HTML converter is ideal for:

* **Platform migration**: Migrating from another email marketing platform? Convert your existing email designs into [!DNL Journey Optimizer]-ready HTML templates without rebuilding from scratch.
* **Design mockup conversion**: Transform design mockups from tools like Photoshop, Figma, or other design software into functional email templates.
* **Quick template creation**: Generate email templates rapidly for time-sensitive campaigns without waiting for developer resources.
* **Building template libraries**: Create a comprehensive library of brand-consistent templates that non-technical team members can customize and deploy.
* **Reducing technical dependencies**: Enable marketers to create and iterate on email templates independently, speeding up campaign execution.

+++

## Guardrails and recommendations {#limitations}

Be aware of the following limitations when converting images to HTML content templates.

* **AI interpretation**: The AI generates HTML based on visual interpretation of your image. Complex or unusual designs may require manual adjustments after conversion.

* **Text accuracy**: While the AI attempts to recognize and reproduce text accurately, always verify text content and make corrections as needed.

* **Dynamic content**: The conversion process creates static HTML based on your image. You'll need to add personalization, dynamic content, and tracking manually after conversion.

* **Complex layouts**: Highly complex designs with intricate layering, unusual shapes, or non-standard elements may not convert perfectly. Simpler designs generally yield better results.

* **Processing time**: The conversion process can take up to 5 minutes depending on the complexity and size of your image. The AI processing happens in the background, allowing you to work on other tasks without keeping the screen open. The template is automatically saved as a draft once the conversion is complete.

* **Limited Availability**: As a Limited Availability feature, the image to HTML convertor is continuously being improved. Functionality and accuracy may vary, and your feedback helps enhance the feature.

>[!NOTE]
>
>The image to HTML converter is designed to provide a strong starting point for email creation. The generated HTML should be reviewed and refined using the Email Designer to ensure it meets your exact requirements.

## Convert an image to an HTML template {#convert-image}

To convert an image design into a fully customizable HTML email template, follow the steps below.

1. Ensure you have an image file in JPEG or PNG format containing your email design.

    >[!NOTE]
    >
    >For best results, use high-quality images with clear visual elements and readable text. Images should ideally be between 600-800 pixels wide to match standard email dimensions.

1. Access the content template list by selecting **[!UICONTROL Content Management]** > **[!UICONTROL Content templates]** from the left menu.

1. Click **[!UICONTROL Create template]**.

1. Fill in the template details and select **[!UICONTROL Email]** as the channel and click **[!UICONTROL Create]**.

1. In the **[!UICONTROL Convert image to template]** section, perform the following steps:

   * (Optional) If your organization has brand themes defined in Journey Optimizer, you can select a theme as input so that the generated HTML is styled according to your brand theme parameters. [Learn more about themes](../email/apply-email-themes.md)

        Styling such as background color, button color, fonts, line spacing, margins, and padding will be applied to the generated template, reducing additional design work and producing a template that is ready to use with minimal edits.

    * To be able to upload an image, make sure it does not contain any personally identifiable information (PII) or other sensitive data, and check the corresponding option to acknowledge that you have reviewed the file.

   * Click the **[!UICONTROL Upload image]** button to select your image file.

        ![](../email/assets/email_designer_convert_img.png)
    
        >[!CAUTION]
        >
        >When you upload an image for conversion, all content currently added in the email will be deleted and replaced with the generated template.


1. After selecting the image, click **[!UICONTROL Open]** to start the AI-powered conversion process.

    >[!NOTE]
    >
    >The generation process can take up to 5 minutes depending on the complexity and size of your image design. You can navigate away from this screen and work on other tasks while the conversion is in progress.

1. Once the conversion is complete, your content template is automatically saved as a draft.

    ![](../email/assets/email_designer_converted_img.png)

1. Click **[!UICONTROL Edit email body]**. The converted template opens in the [Email Designer](../email/get-started-email-design.md) with full editing capabilities. You can now:

    * Review, edit text content and apply personalization
    * Modify images and add links
    * Adjust colors, fonts, and styling
    * Add, remove, or rearrange content components
    * Leverage all Email Designer features as with any other template

    ![](../email/assets/email_designer_html_components.png)

1. Make any necessary adjustments to refine the template and match your brand guidelines.

1. Once satisfied with your template, click **[!UICONTROL Save]**.

Your template is now available in the content template library and can be used when creating emails in journeys or campaigns. [Learn how to use content templates](../email/use-email-templates.md)

## Best practices {#best-practices}

To achieve optimal results when converting images to HTML content templates, follow these recommendations.

+++Before you start

* **Save existing content**: Converting an image to HTML will replace all existing content in your email. Always save your current work before using this feature.
* **Plan your workflow**: Use the image to HTML converter at the beginning of your email creation process, or ensure you're ready to replace all current content.

+++

+++Image preparation

* **Resolution**: Use high-resolution images (at least 1200px wide) for better text recognition and element detection
* **Clarity**: Ensure text is clearly readable and visual elements are well-defined
* **Width**: Design images at standard email widths (600-800px) to match typical email client requirements
* **File format**: Use JPEG or PNG format - avoid compressed or low-quality images
* **Complete design**: Include the full email design in a single image, from header to footer

+++

+++Design considerations

* **Simple layouts**: Simpler, well-structured layouts convert more accurately than highly complex designs
* **Standard elements**: Use common email design patterns (header, body sections, CTAs, footer)
* **Text legibility**: Ensure sufficient contrast between text and backgrounds
* **Web-safe fonts**: Designs using common web-safe fonts will have better fidelity
* **Avoid overlapping elements**: Keep design elements clearly separated for better structure recognition

+++

+++After conversion

* **Review your draft**: Once conversion is complete, your template is automatically saved as a draft. Take time to carefully review the generated HTML for accuracy
* **Test thoroughly**: Test the email across different email clients and devices
* **Refine manually**: Make adjustments as needed using the Email Designer's full editing capabilities
* **Brand alignment**: Verify colors, fonts, and styling match your brand guidelines
* **Personalization**: Add dynamic content and personalization tokens as required
* **Accessibility**: Review and enhance accessibility features if needed

+++

## Frequently asked questions {#faq}

+++What happens to my existing email content when I use the image to HTML converter?

All existing content in your email will be deleted and replaced with the newly generated template when you upload an image for conversion. Make sure to save any important content before using this feature. It's best to use the image to HTML converter at the beginning of your email creation process.

+++

+++What file formats are supported?

The image to HTML converter supports JPEG (.jpg, .jpeg) and PNG (.png) image formats.

+++

+++How long does the conversion process take?

The conversion can take up to 5 minutes, depending on the complexity and size of your image design. The AI processing happens in the background, so you can navigate away and work on other tasks - you don't need to keep the screen open. Once the conversion is complete, your file will be automatically saved as a draft for you to review and edit.

+++

+++Can I edit the generated template?

Yes! The generated HTML template opens in the Email Designer with full editing capabilities. You can modify all aspects of the template, including text, images, styling, layout, and structure.

+++

+++What happens if the conversion doesn't match my design exactly?

The AI does its best to accurately interpret your design, but some manual refinement may be needed. Use the Email Designer to adjust any elements that need fine-tuning.

+++

+++Can I use this feature for landing pages or other content types?

The image to HTML converter is currently designed specifically for email templates. For other content types, use the standard design and import options available in the Email Designer.

+++

+++Do I need special permissions to use this feature?

The image to HTML converter is available in Limited Availability. You need Limited Availability access (contact your Adobe representative to gain access) and standard Email Designer permissions to use this feature.

+++

+++Can I reuse converted templates across multiple campaigns?

Yes! Templates created with the image to HTML converter are automatically saved to the Content Templates library. You can access and reuse them in any email across your journeys and campaigns. [Learn more](content-templates.md)

+++

+++Can I use this for platform migration?

Yes! The image to HTML converter is ideal for migrating from other email marketing platforms. Simply export or screenshot your existing email designs from your previous platform, and convert them into AJO-ready HTML templates without needing to rebuild them from scratch.

+++

## Related topics {#related-topics}

* [Get started with content templates](content-templates.md)
* [Create content templates](create-content-templates.md)
* [Use email templates](../email/use-email-templates.md)
* [Leverage email themes](../email/apply-email-themes.md)
* [Get started with email design](../email/get-started-email-design.md)
* [Import your email content](../email/existing-content.md)
* [Design content from scratch](../email/content-from-scratch.md)
