---
solution: Journey Optimizer
product: journey optimizer
title: Get started with the AI Assistant for Content Accelerator 
description: Learn to access and work with Journey Optimizer's AI Assistant for Content Accelerator 
feature: Content Assistant
topic: Content Management
role: User
level: Beginner
exl-id: 6e291ce3-f324-4e5d-975b-5229dea4d581
---
# Get started with the AI Assistant for Content Accelerator {#gs-content-assistant}

>[!CONTEXTUALHELP]
>id="ajo_ai_generation_settings"
>title="AI Assistant for Content Accelerator "
>abstract="Once you have crafted and personalized your delivery, you can use the AI Assistant for Content Accelerator to enhance your content. This feature simplifies the process of personalization and content improvement by allowing you to fine-tune the content by describing what you want to generate."

>[!CONTEXTUALHELP]
>id="ajo_ai_generation_context"
>title="Upload brand asset"
>abstract="The Upload brand asset menu enables you to add any brand asset containing content that can provide additional context for the AI Assistant for Content Accelerator, or to select a previously uploaded asset. This option ensures that the AI Assistant has access to all necessary materials to enhance its functionality and relevance."

>[!CONTEXTUALHELP]
>id="ajo_ai_generation_start"
>title="Adobe Generative AI terms"
>abstract="Access to this feature is subject to your agreement to the Adobe Experience Cloud Generative AI User Guidelines. Please review any output from this feature for accuracy and ensure it is appropriate for your use case."
>additional-url="https://www.adobe.com/legal/licenses-terms/adobe-gen-ai-user-guidelines.html" text="Adobe Generative AI User Guidelines"

>[!WARNING]
>
>The AI Assistant for Content Accelerator is currently unavailable to Healthcare Shield and Privacy and Security Shield customers.


The AI Assistant for Content Accelerator in Adobe Journey Optimizer, powered by Microsoft Azure OpenAI and Adobe Firefly, brings proactive content variation suggestions for text and images. It is available for email, Push and SMS channels. This new capability provides a prompt based text and image generation. Image generation is managed with Adobe Firefly.

Use the AI Assistant for Content Accelerator in Journey Optimizer to optimize your message's impact by experimenting with different main titles and images. Generate multiple variant and build an experiment to compare them. Leveraging Journey Optimizer Content Experiment, you can define multiple message treatments in order to measure which one performs best for your target audience. You can choose to vary the delivery content, or subject. The message audience is randomly allocated to each treatment to determine which one works best in terms of the specified metric. Learn more about Content Experiment in [this section](../content-management/content-experiment.md).

## Guardrails and limitations {#generative-guardrails}

General guidelines for using the AI Assistant for Content Accelerator in Journey Optimizer for email generation are listed below:

* The quality of the generated content is strongly influenced by the marketing objective / prompt you define. Use well defined prompt for the GenAI model to accurately interpret. 
* Upload brand asset to have accurate, on brand content. Else, content is based on publicly available info. The uploaded content can be in the following formats: PDF, JPEG, PNG, or ZIP files (with supported file formats).
* The maximum size for uploaded brand asset is 50MB. Larger files or lots of images can work but the processing time is increased.
* Use an Adobe Campaign authored email templates, preferably [built-in email templates](../email/use-email-templates.md), a brand specific template or custom template to create your email content. Email template with up to 8-10 images is recommended.
* Make sure to report any problematic outputs using the thumb up, thumb down or flag icons when selecting variants.
* Your use of the AI assistant is subject to the Adobe Experience Cloud Generative AI User Guidelines. [Learn more](https://www.adobe.com/legal/licenses-terms/adobe-gen-ai-user-guidelines.html)

The following limitations apply to AI Assistant for Content Accelerator in Journey Optimizer:

* Supported language is English only. Non-English inputs may produce inconsistent or erroneous results. Issues arising from non-English responses will not be addressed or improved at the present time.
* Only available for the email, push and SMS channels.
* GenAI content might not always be accurate: please share your feedback so that our engineers can refine the models.
* You may upload multiple brand assets, but can leverage only one for a specific generation.



<table style="table-layout:fixed"><tr style="border: 0;">
<td>
<a href="generative-email.md">
<img alt="Email generation" src="assets/do-not-localize/text-genai.jpeg">
</a>
<div>
<a href="generative-email.md"><strong>Email generation</strong></a>
</div>
<p>
</td>
<td>
<a href="generative-sms.md">
<img alt="SMS generation" src="assets/do-not-localize/image-genai.jpeg">
</a>
<div><a href="generative-sms.md"><strong>SMS generation</strong>
</div>
<p>
</td>
<td>
<a href="generative-push.md">
<img alt="Push generation" src="assets/do-not-localize/email-genai.jpeg">
</a>
<div>
<a href="generative-push.md"><strong>Push notification generation</strong></a>
</div>
<p></td>
</tr></table>
