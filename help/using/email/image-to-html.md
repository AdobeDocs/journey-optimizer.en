---
solution: Journey Optimizer
product: journey optimizer
title: Convert images to HTML templates with the image to HTML converter
description: Learn how to use the AI-powered image to HTML converter to convert image designs into editable HTML email templates
feature: Email Design
topic: Content Management
role: User
level: Beginner
badge: label="Limited availability" type="Informative"
keywords: email, template, image, HTML, AI, design, converter
---
# Convert images to HTML templates with the image to HTML converter {#image-to-html}



## Overview {#overview}

The image to HTML converter is an innovative AI-powered feature available in the **Content Templates** menu that dramatically speeds up email creation by converting static image designs into fully customizable, modular HTML email content templates. This no-code tool enables marketers to transform visual designs from graphic designers or design tools into responsive, editable email templates that can be saved to the Content Templates library and then reused across multiple journeys and campaigns—without requiring technical expertise.

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

By leveraging generative AI technology, the image to HTML converter analyzes the layout, typography, colors, and visual elements in your image and generates clean, modular HTML code that maintains design fidelity while ensuring full editability and compatibility with the Email Designer. This eliminates the manual, time-consuming process of converting mockups to HTML and reduces dependency on development resources.

**Key benefits:**

* **Design to HTML in minutes**: AI-powered, no-code conversion transforms static images into editable, modular templates in minutes, dramatically reducing template creation time
* **Empowers non-technical users**: Reduces dependency on design or development teams — marketers can generate and customize templates with minimal technical knowledge
* **Simplified platform migration**: Convert external templates or designs from other platforms into AJO-ready HTML effortlessly
* **Build a reusable template library**: Create a scalable, brand-consistent template library that can be used across multiple journeys and campaigns
* **Design fidelity**: Maintain visual consistency with your original design while creating fully editable content
* **Email compatibility**: Generate HTML that works seamlessly with the Email Designer and across email clients

## Common use cases {#use-cases}

The image to HTML converter is ideal for:

* **Platform migration**: Migrating from another email marketing platform? Convert your existing email designs into AJO-ready HTML templates without rebuilding from scratch
* **Design mockup conversion**: Transform design mockups from tools like Photoshop, Figma, or other design software into functional email templates
* **Quick template creation**: Generate email templates rapidly for time-sensitive campaigns without waiting for developer resources
* **Building template libraries**: Create a comprehensive library of brand-consistent templates that non-technical team members can customize and deploy
* **Reducing technical dependencies**: Enable marketers to create and iterate on email templates independently, speeding up campaign execution

## Prerequisites {#prerequisites}

Before using the image to HTML converter, ensure you have:

* Access to Adobe Journey Optimizer with the Email Designer
* An image file in JPEG or PNG format containing your email design
* Limited Availability access to the image to HTML converter feature (contact your Adobe representative)

>[!NOTE]
>
>For best results, use high-quality images with clear visual elements and readable text. Images should ideally be between 600-800 pixels wide to match standard email dimensions.

## Convert an image to HTML template {#convert-image}

To convert an image design into a fully customizable HTML email template, follow these steps:

1. Access the Content Templates list by selecting **[!UICONTROL Content Management]** > **[!UICONTROL Content Templates]** from the left menu.

1. Click **[!UICONTROL Create template]**.

1. Fill in the template details and select **[!UICONTROL Email]** as the channel and click **[!UICONTROL Create]**.

1. In the right section, in the **[!UICONTROL Convert image to template]** section, click the **[!UICONTROL Upload image]** button to select your image file.

    ![](assets/email_designer_convert_img.png)
    

    >[!CAUTION]
    >
    >When you upload an image for conversion, **all content currently added in the email will be deleted and replaced** with the generated template. If you have existing content in your email, make sure to save it before proceeding with the image conversion.


1. Choose the image and click **[!UICONTROL Open]** to start the AI-powered conversion process.

    >[!NOTE]
    >
    >The generation process can take up to 5 minutes depending on the complexity and size of your image design. The AI processing happens in the background, so you can navigate away from this screen and work on other tasks while the conversion is in progress. You don't need to keep the screen open.

1. Once the conversion is complete, your content template will be automatically saved as a draft. You can then review and edit the generated HTML template in the Email Designer canvas.

    ![](assets/email_designer_converted_img.png)


1. The converted template opens in the Email Designer with full editing capabilities. You can now:

    * Edit text content and apply personalization
    * Modify images and add links
    * Adjust colors, fonts, and styling
    * Add, remove, or rearrange content components
    * Leverage all Email Designer features as with any other template

    ![](assets/email_designer_html_components.png)

1. Make any necessary adjustments to refine the template and match your brand guidelines.

1. Once satisfied with your template, click **[!UICONTROL Save]** to save the content template.

1. Your template is now available in the Content Templates library and can be used when creating emails in journeys or campaigns. [Learn how to use content templates](use-email-templates.md)

## Use your converted template in emails {#use-template}

Once you've created and saved your content template, you can use it when designing emails in journeys or campaigns:

When creating an email in a journey or campaign, access the Email Designer from the **[!UICONTROL Edit content]** screen.

Learn more about [working with email templates](use-email-templates.md) and [creating content templates](../content-management/content-templates.md).

## Best practices {#best-practices}

To achieve optimal results when using the image to HTML converter, follow these recommendations:

**Before you start**

* **Save existing content**: Converting an image to HTML will replace all existing content in your email. Always save your current work before using this feature.
* **Plan your workflow**: Use the image to HTML converter at the beginning of your email creation process, or ensure you're ready to replace all current content.

**Image preparation**

* **Resolution**: Use high-resolution images (at least 1200px wide) for better text recognition and element detection
* **Clarity**: Ensure text is clearly readable and visual elements are well-defined
* **Width**: Design images at standard email widths (600-800px) to match typical email client requirements
* **File format**: Use JPEG or PNG format - avoid compressed or low-quality images
* **Complete design**: Include the full email design in a single image, from header to footer

**Design considerations**

* **Simple layouts**: Simpler, well-structured layouts convert more accurately than highly complex designs
* **Standard elements**: Use common email design patterns (header, body sections, CTAs, footer)
* **Text legibility**: Ensure sufficient contrast between text and backgrounds
* **Web-safe fonts**: Designs using common web-safe fonts will have better fidelity
* **Avoid overlapping elements**: Keep design elements clearly separated for better structure recognition

**After conversion**

* **Review your draft**: Once conversion is complete, your template is automatically saved as a draft. Take time to carefully review the generated HTML for accuracy
* **Test thoroughly**: Test the email across different email clients and devices
* **Refine manually**: Make adjustments as needed using the Email Designer's full editing capabilities
* **Brand alignment**: Verify colors, fonts, and styling match your brand guidelines
* **Personalization**: Add dynamic content and personalization tokens as required
* **Accessibility**: Review and enhance accessibility features if needed

## Limitations and considerations {#limitations}

Be aware of the following limitations when using the Image to HTML converter:

* **AI interpretation**: The AI generates HTML based on visual interpretation of your image. Complex or unusual designs may require manual adjustments after conversion.

* **Text accuracy**: While the AI attempts to recognize and reproduce text accurately, always verify text content and make corrections as needed.

* **Dynamic content**: The conversion process creates static HTML based on your image. You'll need to add personalization, dynamic content, and tracking manually after conversion.

* **Complex layouts**: Highly complex designs with intricate layering, unusual shapes, or non-standard elements may not convert perfectly. Simpler designs generally yield better results.

* **Processing time**: The conversion process can take up to 5 minutes depending on the complexity and size of your image. The AI processing happens in the background, allowing you to work on other tasks without keeping the screen open. The template is automatically saved as a draft once the conversion is complete.

* **Limited Availability**: As a Limited Availability feature, the image to HTML convertor is continuously being improved. Functionality and accuracy may vary, and your feedback helps enhance the feature.

>[!NOTE]
>
>The image to HTML converter is designed to provide a strong starting point for email creation. The generated HTML should be reviewed and refined using the Email Designer to ensure it meets your exact requirements.

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

Yes! Templates created with the image to HTML converter are automatically saved to the Content Templates library. You can access and reuse them in any email across your journeys and campaigns. [Learn more](../content-management/content-templates.md)

+++

+++Can I use this for platform migration?

Yes! The image to HTML converter is ideal for migrating from other email marketing platforms. Simply export or screenshot your existing email designs from your previous platform, and convert them into AJO-ready HTML templates without needing to rebuild them from scratch.

+++

## Related topics {#related-topics}

* [Get started with content templates](../content-management/content-templates.md)
* [Create content templates](../content-management/create-content-templates.md)
* [Use email templates](use-email-templates.md)
* [Get started with email design](get-started-email-design.md)
* [Import your email content](existing-content.md)
* [Design content from scratch](content-from-scratch.md)

