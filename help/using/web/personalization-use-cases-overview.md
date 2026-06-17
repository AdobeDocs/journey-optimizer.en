---
title: Personalization use cases overview
description: Learn how to implement personalization use cases using the Adobe Experience Platform Web SDK, including patterns for rendering content and tracking display.
feature: Web Channel, Channel Configuration
topic: Content Management
role: Developer
level: Intermediate
---
# Personalization use cases overview {#personalization-use-cases-overview}

>[!BEGINSHADEBOX]

**On this page:** Learn how to implement personalization use cases using the Adobe Experience Platform Web SDK, including patterns for rendering content and tracking display on sites that deliver Adobe Journey Optimizer web experiences.

>[!ENDSHADEBOX]

The Adobe Experience Platform Web SDK enables a wide variety of personalization use cases for web properties. It supports flexible architectures (client-side, server-side, and hybrid) so you can request decisions and render content in ways that match your site's needs.

Before you implement these patterns for the web channel, complete the [web channel prerequisites](web-prerequisites.md).

## Render personalized content {#render-personalized-content}

The Web SDK can retrieve personalization decisions (also known as _propositions_) and help you render them on the page. Rendering is asynchronous, so avoid assuming a specific timing for when content is applied.

Pick the rendering pattern that matches the proposition items you receive:

1. **Automatically render DOM action propositions**: Use when propositions include `dom-action` items with selectors and action types that Web SDK can apply automatically. [Learn more on automatically rendering DOM action propositions](https://experienceleague.adobe.com/en/docs/experience-platform/collection/use-cases/personalization/render-auto-pers-content){target="_blank"}
1. **Render HTML offers without selectors using applyPropositions**: Use when you receive HTML content, but you must provide where and how to apply it (selector + action type) via metadata. [Learn more on rendering HTML offers without selectors](https://experienceleague.adobe.com/en/docs/experience-platform/collection/use-cases/personalization/render-html-offers){target="_blank"}
1. **Manually render propositions**: Use when you need full control over rendering logic (for example, composing UI from JSON or applying custom business rules). [Learn more on manually rendering propositions](https://experienceleague.adobe.com/en/docs/experience-platform/collection/use-cases/personalization/render-manual-propositions){target="_blank"}

>[!TIP]
>
>These patterns can be combined. For example, you can enable automatic DOM action rendering while also manually rendering content from specific decision scopes.

## Common companion topics {#common-companion-topics}

Most personalization implementations involve these common topics:

* **Prevent flicker** (optional): Hide and reveal containers during personalization. [Learn more on managing flicker](https://experienceleague.adobe.com/en/docs/experience-platform/collection/use-cases/personalization/manage-flicker){target="_blank"}
* **Track what was displayed**: Record display events for rendered content. [Learn more on managing display events](https://experienceleague.adobe.com/en/docs/experience-platform/collection/use-cases/personalization/display-events){target="_blank"}
* **Top-of-page fetch / bottom-of-page metrics**: Request decisions early, then include measurement later. [Learn more on configuring top and bottom of page events](https://experienceleague.adobe.com/en/docs/experience-platform/collection/use-cases/personalization/top-bottom-page-events){target="_blank"}

## Web SDK samples {#web-sdk-samples}

In addition to the documentation linked above, Adobe maintains a repository of sample applications that you can reference. See [Web SDK samples on GitHub](https://github.com/adobe/alloy-samples/){target="_blank"} for additional personalization scenarios, including:

* Client-side personalization
* Server-side personalization
* Hybrid personalization
* Personalization in single-page applications

For SPA-specific implementation in Journey Optimizer, see [Author single-page applications](web-spa.md).
