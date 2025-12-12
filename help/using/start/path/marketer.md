---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer Get started for Marketers
description: As a Journey Practitioner, learn more how to work with Journey Optimizer
level: Beginner
feature: Get Started
Role: User
exl-id: 34304142-3ee8-4081-94b9-e914968c75ba
---
# Get started for Marketers {#get-started-marketers}

As a **Marketer** or a **Journey Practitioner**, you are responsible for creating offers and journeys and designing content. You can start working with [!DNL Adobe Journey Optimizer] once the [System Administrator](administrator.md) and the [Data Engineer](data-engineer.md) granted you access and prepared your environment.

## Get started with the essentials

Journey Optimizer empowers you to create personalized, connected customer experiences across email, SMS, push, in-app, web, content cards, and more. Work with your [Administrators](administrator.md) to gain access and with [Data Engineers](data-engineer.md) to set up audiences and data.

Follow these core steps to start building experiences:

1. **Create audiences**. Build audiences through segment definitions, upload CSV files, or use audience composition. Journey Optimizer offers multiple ways to target the right customers. Learn more about [audiences](../../audience/about-audiences.md) and [creating segment definitions](../../audience/creating-a-segment-definition.md).

1. **Design content**. Create compelling messages across channels:
   * Use the **AI Assistant** to generate email content, subject lines, and images based on your brand guidelines. [Learn about AI content generation](../../content-management/gs-generative.md)
   * **Personalize messages** with customer data, dynamic content, and conditional logic. [Learn about personalization](../../personalization/personalize.md)
   * **Iterate over contextual data** to display dynamic lists from events, custom actions, and dataset lookups. [Learn about iterating contextual data](../../personalization/iterate-contextual-data.md)
   * Create reusable **content templates** and **fragments** to maintain brand consistency. [Work with templates](../../content-management/content-templates.md)
   * Manage assets with **Adobe Experience Manager Assets** integration. [Learn about assets](../../integrations/assets.md)

    ![](../assets/perso_ee2.png)

1. **Add offers and decisioning**. Deliver the best offer to each customer at the right time using AI-powered decisioning. Learn about [Decision Management](../../offers/get-started/starting-offer-decisioning.md) and [Experience Decisioning](../../experience-decisioning/gs-experience-decisioning.md).

    ![](../assets/offers-e2e-offers-displayed.png)
    
1. **Test and validate**. Preview and test content before sending:
   * Use **test profiles** to preview personalization and check rendering across devices
   * Test with **sample data** from CSV/JSON files
   * Preview **email rendering** across popular email clients
   * Set up **approval workflows** for campaigns and journeys (requires additional license)
   
   Learn how to [test and validate messages](../../content-management/preview-test.md).

1. **Build customer journeys**. Create real-time, personalized experiences using the journey canvas:

    * Trigger journeys with **events** (customer actions) or **audiences** (batch sends)
    * Add **conditions** to create personalized paths based on customer data
    * Use **wait activities** to create perfect timing between messages
    * Send messages across **multiple channels** within one journey
    * Apply **A/B testing** to optimize journey effectiveness
    * Use **dataset lookup** to enrich journeys with real-time data from Adobe Experience Platform. [Learn about dataset lookup](../../building-journeys/dataset-lookup.md)
    * Leverage **supplemental identifiers** to allow the same profile to enter multiple journey instances (e.g., different orders or bookings). [Learn about supplemental identifiers](../../building-journeys/supplemental-identifier.md)

    ![](../assets/journey-design.png)

    Learn how to [design and execute journeys](../../building-journeys/journey-gs.md) and explore [journey use cases](../../building-journeys/jo-use-cases.md). Understand [entry/exit criteria](../../building-journeys/entry-exit-criteria-guide.md) to control profile flow.

1. **Monitor and optimize**. Track performance and improve results over time:
   * Monitor **live journey** performance and identify bottlenecks
   * Analyze **message delivery** rates and engagement metrics
   * Use **reporting dashboards** with Customer Journey Analytics integration
   * Track **conversion** and business impact
   
   Learn how to [monitor performance](../../reports/report-gs-cja.md).

## Leverage latest capabilities

Journey Optimizer continuously evolves with new features to enhance your marketing effectiveness:

* **Content Cards**: Deliver persistent, non-intrusive messages within mobile apps and websites that users can engage with at their convenience. Unlike push notifications, content cards remain visible until dismissed. [Learn about content cards](../../content-card/get-started-content-card.md)

* **Conflict Management & Prioritization**: Control message frequency and prevent over-communication with advanced capping rules. Set priority scores to ensure the most important messages reach customers first. [Learn about conflict management](../../conflict-prioritization/gs-conflict-prioritization.md)

* **AI-Powered Send-Time Optimization**: Let AI predict the optimal send time for each customer based on their historical engagement patterns, increasing open and click rates by up to 10%. [Learn about send-time optimization](../../building-journeys/send-time-optimization.md)

* **Multi-Armed Bandit Experimentation**: Automatically allocate more traffic to winning variations in real-time while testing, maximizing results without waiting for test completion. [Learn about experimentation](../../content-management/content-experiment.md)

* **Approval Workflows**: Implement review processes for campaigns and journeys before they go live (available with additional license). [Learn about approvals](../../test-approve/gs-approval.md)

## Best practices for success

### Content creation

* **Start with templates**: Use pre-built templates and content fragments to speed up creation and maintain consistency
* **Test early, test often**: Always preview content across devices and use test profiles to validate personalization
* **Leverage AI wisely**: Use AI Assistant for initial drafts and variations, but always review and refine for your brand voice
* **Keep it simple**: Clear, concise messages with strong calls-to-action perform better than complex layouts

### Journey design

* **Define clear goals**: Establish success metrics before building your journey
* **Map the customer experience**: Visualize the entire journey before implementation
* **Use wait activities strategically**: Give customers time to engage before sending follow-ups
* **Plan exit strategies**: Define when and why customers should exit the journey
* **Test in draft mode**: Validate journey logic with dry run before activating

[Learn journey best practices](../../building-journeys/entry-exit-criteria-guide.md#best-practices)

### Audience targeting

* **Segment thoughtfully**: Create specific, actionable audience segments based on clear criteria
* **Refresh regularly**: Ensure audiences stay current by setting appropriate evaluation schedules
* **Balance size and precision**: Target audiences large enough for statistical significance but specific enough for relevance
* **Use enrichment attributes**: Leverage computed attributes and enrichment data for deeper personalization

### Frequency management

* **Respect customer preferences**: Honor opt-outs and communication preferences
* **Set frequency caps**: Use rule sets to prevent message fatigue across channels
* **Coordinate campaigns**: Use conflict management to ensure customers receive the right message at the right time
* **Monitor engagement**: Watch for signs of fatigue (declining open rates, increasing unsubscribes)

[Learn about frequency capping](../../conflict-prioritization/channel-capping.md)

## Explore use cases

Learn from practical examples that demonstrate Journey Optimizer capabilities:

**Popular use cases:**

* **Welcome series**: Onboard new customers with personalized, multi-step journeys. [View use case](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/customer-onboarding)
* **Abandoned cart recovery**: Re-engage customers who left items in their cart. [View use case](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/abandoned-cart)
* **Re-engagement campaigns**: Win back inactive customers with targeted offers. [View use case](https://experienceleague.adobe.com/en/docs/experience-platform/rtcdp/use-cases/personalization-insights-engagement/use-cases-luma)
* **Birthday campaigns**: Send personalized birthday messages with special offers
* **Product recommendations**: Suggest relevant products based on browsing and purchase history
* **Event-driven messaging**: Respond to customer actions in real-time

**Journey patterns:**

* [Send messages to subscribers](../../building-journeys/message-to-subscribers-uc.md): Target subscription lists with personalized content
* [Multi-channel messaging](../../building-journeys/journeys-uc.md): Combine email and push with reaction events
* [Weekday-only emails](../../building-journeys/weekday-email-uc.md): Schedule communications using time-based conditions

Browse the complete [journey use cases library](../../building-journeys/jo-use-cases.md) for more patterns and implementations.

## Collaborate with other roles

Your marketing work connects with other teams:

* **Work with [Data Engineers](data-engineer.md)**: Request new computed attributes, provide feedback on audience quality, and coordinate on data requirements
* **Work with [Developers](developer.md)**: Align on event triggers, test mobile implementations, and validate tracking
* **Work with [Administrators](administrator.md)**: Request channel configurations, report issues with permissions, and coordinate on new feature enablement

## Stay updated

Keep up with the latest Journey Optimizer capabilities and marketing features:

* **[Release Notes](../../rn/release-notes.md)**: Review new features, channel updates, and enhancements released each month
* **[Documentation Updates](../../rn/documentation-updates.md)**: Track recent changes including new use cases, best practices, and feature documentation
* **Product Notifications**: Enable notifications in your [Adobe Experience Cloud profile](https://experience.adobe.com/preferences){target="_blank"} to receive alerts about:
  * New channels and capabilities available to you
  * Upcoming feature launches and beta programs
  * Best practices and training opportunities
  * Important announcements affecting your campaigns
  
  To enable notifications, click your profile icon in the top right of Adobe Experience Cloud, go to **Preferences > Notifications**, and configure your Journey Optimizer notification preferences.

## Next steps

1. **Start small**: Create a simple welcome journey or single-message campaign to learn the platform
2. **Leverage AI**: Use AI Assistant to ask questions and accelerate content creation
3. **Join the community**: Connect with other Journey Optimizer users in the [Experience League Community](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer/ct-p/journey-optimizer){target="_blank"}
4. **Explore tutorials**: Watch step-by-step videos on [Experience League](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/overview.html){target="_blank"}
