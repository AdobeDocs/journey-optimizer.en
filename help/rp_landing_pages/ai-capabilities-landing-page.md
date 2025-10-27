---
solution: Journey Optimizer
product: Journey Optimizer
title: AI Capabilities in Adobe Journey Optimizer
description: AI Capabilities in Adobe Journey Optimizer
hide: yes
hidefromtoc: yes
---
# AI Capabilities in Adobe Journey Optimizer{#section-overview}

Adobe Journey Optimizer harnesses the power of artificial intelligence and machine learning to transform how you create, optimize, and deliver customer experiences. From generating personalized content across channels to predicting the optimal time to engage customers, AI capabilities streamline your workflow and maximize impact. This section explores how AI-powered features work together to help you make smarter decisions, automate complex tasks, and create experiences that truly resonate with your audience. Whether you're leveraging generative AI for content creation, using predictive models for decisioning, or optimizing send times for better engagement, you'll discover practical tools and strategies to unlock the full potential of AI in your customer journey orchestration.

## AI-Powered Features

:::: landing-cards-container
:::
![icon](https://cdn.experienceleague.adobe.com/icons/sparkles.svg)

AI Assistant for Content Generation

Leverage generative AI to create and personalize content across emails, SMS, push notifications, web pages, and landing pages.

[Explore AI Assistant](ai-assistant-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/clock.svg)

Send-Time Optimization

Use AI to predict the optimal time to send messages and maximize customer engagement based on historical behavior.

[Learn About Send-Time Optimization](../using/building-journeys/send-time-optimization.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/data.svg)

AI Models for Decisioning

Create auto-optimization and personalized optimization models to rank and deliver the best offers to your customers.

[Discover AI Models](ai-models-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/help.svg)

AI Assistant Product Knowledge

Get instant answers and operational insights about Adobe Journey Optimizer using conversational AI.

[Work with AI Assistant](../using/start/ai-assistant.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/experiment.svg)

Content Experimentation with AI

Generate multiple content variations and run experiments to identify the best-performing content for your audience.

[Learn About AI Experimentation](../using/content-management/generative-experimentation.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/user-group.svg)

Customer AI Integration

Integrate with Adobe Intelligent Services to predict customer behavior and use churn and conversion scores in your journeys.

[Explore Intelligent Services](../using/building-journeys/ai-services-overview.md)
:::

::::


## Additional Resources

- **[Brand Alignment Scoring](../using/content-management/brands-score.md)** - Evaluate how well your AI-generated content aligns with your brand guidelines using AI-powered scoring.
- **[Experiment Accelerator](../using/content-management/experiment-accelerator-gs.md)** - Accelerate your content experimentation process with AI-driven insights and recommendations.
- **[AI-Powered APIs](../using/configuration/ajo-apis.md)** - Access Journey Optimizer's AI and machine learning capabilities programmatically through APIs.

## Frequently Asked Questions

+++**What permissions are required to use AI capabilities?**

To use AI Assistant for content generation, users must be granted the **Generate Content** permission. This permission is assigned through the AI Assistant resource in the Permissions product. To use AI Assistant for product knowledge and operational insights, users must agree to the Adobe Experience Cloud Generative AI User Guidelines.

[Learn more about permissions](../using/administration/ootb-permissions.md)

+++

+++**Which channels support AI Assistant content generation?**

AI Assistant for content generation is available for **Email**, **Push**, **SMS**, and **Web** channels. It is not currently available for Direct Mail, Content Cards, LINE, or WhatsApp channels.

+++

+++**What are the best practices for using AI Assistant?**

- **Use well-defined prompts** - The quality of generated content is strongly impacted by your marketing objective and prompt. Be specific and clear.
- **Upload brand assets** - Provide brand assets in PDF, JPEG, PNG, or ZIP format (max 50MB) for accurate, on-brand content.
- **Use custom templates** - Leverage brand-specific email templates with up to 8-10 images for optimal results.
- **Provide feedback** - Report problematic outputs using thumb up, thumb down, or flag icons to help refine the models.
- **Leverage only one brand asset per generation** - While you can upload multiple assets, use only one for each specific generation.

[Learn more about AI Assistant guardrails](../using/content-management/gs-generative.md#generative-guardrails)

+++

+++**What are the best practices for Send-Time Optimization?**

- **Wait 30 days** - Use Email and Push actions for at least 30 days before enabling Send-Time Optimization to ensure sufficient data collection.
- **Choose optimal wait times** - Set maximum wait time between 6-24 hours for best results. Shorter durations limit optimization potential; longer ones may result in outdated messages.
- **Optimize for the right metric** - For emails, optimize for Clicks when driving action, or Opens for informational content. Push messages are always optimized for Opens.
- **Avoid for time-sensitive messages** - Do not use Send-Time Optimization for urgent operational messages like order confirmations, password resets, or flight notifications. Best suited for marketing communications like promotions and newsletters.
- **Schedule morning sends for Push** - To avoid nighttime notifications, schedule batch Push sends in the morning with shorter durations (e.g., 9 AM send with 8-hour wait time).

[Learn more about Send-Time Optimization](../using/building-journeys/send-time-optimization.md)

+++

+++**What are the limitations of Send-Time Optimization?**

- **Channels** - Only available for Email and Push notification channels in Journeys. Not available in Campaigns or through custom actions.
- **Availability** - Must be enabled by Adobe Customer Care or your Adobe representative.
- **Training period** - Requires at least 30 days of historical Email or Push data before use.
- **Model training** - Models are initially trained weekly using the last 16 weeks of data, then retrained monthly.
- **Exploration vs. Optimization** - 5% of messages receive random exploration send times; 95% receive optimized send times.

+++

+++**What are the limitations for AI models in Decisioning?**

- **Maximum AI models** - Up to 5 AI ranking models per organization.
- **Dataset requirements** - At least 2 offers must have 100+ display events and 5+ click events within the last 14 days for Auto-optimization models.
- **Feedback events** - Must be sent as experience events; not automatically collected in Journey Optimizer channels.
- **API limitations** - Auto-optimization models do not work with the Batch Decisioning API (Decision management only).

[Learn more about AI models](../using/experience-decisioning/ranking/ai-models.md)

+++

+++**What guardrails apply to AI-powered decisioning?**

| Component | Limit |
|-----------|-------|
| AI Ranking Models | 5 per organization |
| Decision requests (Code-based with Edge segmentation) | 1,500 per second |
| Decision requests (Code-based without Edge segmentation) | 5,000 per second |
| Items collections | 10,000 total |
| Offer items per collection | 500 |
| Selection strategies per decision policy | 10 |
| Offer items returned per decision policy | 30 |
| Eligibility rules + ranking formulas | 10,000 combined |
| Profile attributes per rule | 25 |
| Context data attributes per rule | 30 |

[Learn more about Decisioning guardrails](../using/experience-decisioning/decisioning-guardrails.md)

+++

+++**Do I need to agree to any terms to use AI features?**

Yes, you must agree to the [Adobe Experience Cloud Generative AI User Guidelines](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html) before using AI Assistant in Journey Optimizer. Contact your Adobe representative for more information. Additionally, Adobe applies Content Credentials to Firefly-generated assets as part of its commitment to transparency in generative AI use.

+++

+++**Is AI-generated content always accurate?**

No. Generative AI content might not always be accurate. Always review AI-generated outputs for accuracy and ensure they are appropriate for your use case. Share feedback using the provided rating tools to help engineers refine the models.

+++

