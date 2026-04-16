---
solution: Journey Optimizer
product: journey optimizer
title: AEM Content Fragments
description: Learn how to access & manage AEM Content Fragments
topic: Content Management
role: User
level: Beginner
exl-id: c36a53a4-c324-4082-838e-ed27bd3b2e90
---
# Get started with Adobe Experience Manager content fragments {#aem-fragments}

>[!AVAILABILITY]
>
>For Healthcare customers, the integration is enabled only upon licensing the Journey Optimizer Healthcare Shield and Adobe Experience Manager Enhanced Security add-on offerings.

By integrating Adobe Experience Manager as a Cloud Service with Adobe Journey Optimizer, you can now seamlessly incorporate your AEM Content Fragments into your Journey Optimizer content. This streamlined connection simplifies the process of accessing and leveraging AEM content, enabling the creation of personalized and dynamic campaigns and journeys.

To learn more about AEM Content Fragments, refer to [Working with Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-with-journey-optimizer){target="_blank"} in the Experience Manager documentation.

## Content Fragment lifecycle

![](assets/do-not-localize/AEM_CF.png)

Content Fragments follow different lifecycle stages depending on the Adobe Experience Manager tier in which they exist. [Learn more in Adobe Experience Manager documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/author-publish)

Content is created and managed on the **Author tier**, where fragments can have statuses such as New, Draft, Published, Modified, or Unpublished. These statuses apply only on the **Author tier** and support content creation and review.

When a Content Fragment is published, a copy is created on the **Publish tier** and exposed through a public, unauthenticated endpoint. Journey Optimizer integrates exclusively with this **Publish tier**.

As a result, Journey Optimizer surfaces only Published or Modified Content Fragments and always uses the latest published version. Any changes made after publication are not reflected in Journey Optimizer until the Content Fragment is republished.
