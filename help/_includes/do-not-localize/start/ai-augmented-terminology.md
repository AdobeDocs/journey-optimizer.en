---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Defines the essential Adobe Journey Optimizer terms and, in a disambiguation guide, separates similar-sounding terms such as Decisioning versus Decision Management and Content Cards versus In-App messages, so you can navigate the platform and collaborate with your team.

**Intents:**

* Look up the essential Journey Optimizer terms and concepts: journey and campaign terms, customer and audience terms, content and personalization terms, decision and offer terms, data and configuration terms, and conflict and prioritization terms.
* Tell Decisioning apart from Decision Management.
* Tell apart the three campaign types, frequency capping and journey arbitration, and Content Cards and In-App messages.
* Identify which foundational concepts are Adobe Experience Platform concepts rather than Journey Optimizer-specific ones.
* Tell Adobe Journey Optimizer apart from Journey Optimizer B2B Edition.

**Glossary:**

* **Journey:** A series of connected steps that guide customers through experiences with your brand over time. Each step occurs based on customer actions or time triggers, enabling sequential, personalized interactions.
* **Campaign:** A coordinated marketing action that delivers content to a specific audience across one or more channels. Unlike journeys, campaigns execute actions simultaneously. Journey Optimizer supports three campaign types: Action campaigns, API-triggered campaigns, and Orchestrated campaigns.
* **Event:** An action or occurrence that triggers or advances a journey. Events can be customer actions (making a purchase, abandoning a cart) or system events (date/time, data change).
* **Audience Qualification:** The automatic process that occurs when a customer joins or leaves an audience. Journey Optimizer can trigger actions when someone enters or exits an audience.
* **Engageable Profiles** *(product-specific)*: The unique customer profiles engaged through journeys, campaigns, or decisioning activities over a rolling 12-month window. This is the key license metric for Journey Optimizer: each profile is counted once per sandbox regardless of how many journeys or campaigns it enters. Monitor the count at Administration > License Usage.
* **Test Profile:** Fictitious profiles used for testing and previewing messages before sending to real customers. Test profiles help verify personalization, content, and journey logic.
* **Fragment:** A reusable content block that can be used across multiple messages to ensure consistency and enable centralized updates.
* **Content experiment:** An A/B testing framework that splits an audience into random groups and delivers different message variants (content, subject line, or offer) to each group, then identifies the best-performing variant based on a defined success metric.
* **Experimentation** *(product-specific)*: The broader capability in Journey Optimizer for testing and optimizing decisions. Content experiments test message variants in campaigns and journeys, while decisioning experimentation tests offer selection strategies. Both use statistical analysis to identify winning approaches.
* **Decisioning** *(product-specific)*: The decision framework in Journey Optimizer that offers schema-based item catalog management (with flexible metadata) and flexible collection rules.
* **Decision Management** *(product-specific)*: The offer decisioning feature in Journey Optimizer. It uses a central library of marketing offers and a rules-based decision engine that applies constraints to real-time customer profiles.
* **Offer:** A marketing message, discount, or promotion that can be presented to customers. Offers include eligibility rules that determine which customers can receive them.
* **Decision Policy:** A set of rules and strategies that determine which offer to show to which customer at what time, based on constraints like eligibility, priority, and capping rules.
* **Channel configuration:** The settings that define how messages are delivered for a specific channel, including sender details, subdomain, IP pool, and message type (marketing or transactional).
* **Sandbox:** An isolated environment in which data, audiences, journeys, campaigns, and settings exist independently. Nothing carries across sandboxes automatically, so teams typically build and test in a development sandbox and send to customers from production.
* **Suppression list:** A list of email addresses and domains automatically excluded from message delivery due to hard bounces, spam complaints, or manual additions. Sending to suppressed addresses is blocked to protect deliverability and sender reputation.
* **Rule set:** A named group of business rules applied to journeys and campaigns to govern messaging behavior. A rule set can combine frequency capping, journey entry limits, and quiet hours into a single reusable policy.
* **Frequency capping:** A rule within a rule set that limits how many messages a profile can receive within a given time period, per channel or communication type (Sales, Promotional, etc.). Profiles that exceed the cap are automatically excluded from delivery.

**Applicability:**

* Decisioning: available for Code-based Experience, Web, Email, Push, Mobile messages, Custom channels, and Direct mail.
* Decision Management: supports Email, In-App, Push, Mobile messages, and Direct mail.

**Terminology:**

* Canonical name: Adobe Journey Optimizer — Acronym: AJO — variants: Journey Optimizer
* Canonical name: Adobe Experience Platform — Acronym: AEP
* Synonyms: "Action campaigns" = "Scheduled campaigns"
* Previous terms: "surface" and "preset" were used in older documentation for Channel configuration.
* Status labels: Decisioning is Current. Decision Management is Legacy, still supported for existing implementations.
* Do not confuse:
    * "Decisioning" ≠ "Decision Management": both capabilities select and deliver offers, but they serve different stages of the product lifecycle. Key differentiator: reusable decision components, experimentation, and a broader channel roadmap for Decisioning; a proven constraints engine for Decision Management.
    * "Action campaigns" ≠ "API-triggered campaigns" ≠ "Orchestrated campaigns": three campaign types that are activated differently and serve distinct use cases.
        * Action campaigns (Scheduled campaigns): activation is manual or scheduled; best for one-off or recurring batch sends (newsletters, promotions); the personalization source is profile attributes.
        * API-triggered campaigns: activation is an external API call; best for real-time, event-driven messaging (order confirmations, password resets); the personalization source is profile attributes plus API payload context.
        * Orchestrated campaigns: activation is a visual workflow canvas; best for complex, multi-step cross-channel programs; the personalization source is profile attributes plus relational data.
    * "Frequency capping" ≠ "Journey arbitration": both are rule-set mechanisms under the Conflict & prioritization toolset, but they address different problems.
        * Frequency capping solves the problem of a profile receiving too many messages over time. It is configured in Rule sets → Frequency capping.
        * Journey arbitration solves the problem of a profile qualifying for multiple journeys simultaneously. Its scope is journey enrollment: the number of concurrent journeys, or which journey wins. It uses priority scores and capping rules to decide which journey a profile enters. It is configured in Rule sets → Journey capping & arbitration.
    * "Content Cards" ≠ "In-App messages": both channels deliver messages inside a mobile or web application, but they have different rendering models and persistence behaviors.
        * Display model: Content Cards are persistent cards embedded in the app UI (feed, inbox, or custom surface); In-App messages are transient overlays, banners, or modals shown on top of the app.
        * Persistence: Content Cards stay visible until explicitly dismissed or expired; In-App messages disappear after the user interacts or closes them.
        * Trigger: for Content Cards, the SDK renders on load and rules control display and dismissal; for In-App messages, a real-time event in the journey or campaign triggers delivery.
        * Best for: Content Cards suit ongoing promotions, loyalty status, and persistent alerts; In-App messages suit onboarding tips, limited-time offers, and transient notifications.
    * "Adobe Journey Optimizer" ≠ "Journey Optimizer B2B Edition": two separate products in the same brand family. Adobe Journey Optimizer targets B2C customer journeys. Journey Optimizer B2B Edition is purpose-built for account-based marketing, working with buying groups and account audiences.
    * Journey Optimizer-specific concepts ≠ Adobe Experience Platform concepts: Journey Optimizer is built on Adobe Experience Platform, and many foundational concepts, such as real-time customer profiles, sandboxes, schemas, and datasets, are Adobe Experience Platform concepts, not Journey Optimizer-specific ones. For definitions of those terms, refer to the Adobe Experience Platform glossary.

**FAQ:**

* **What is the difference between Decisioning and Decision Management?** Both capabilities select and deliver offers, but they serve different stages of the product lifecycle. Decisioning has the status Current and Decision Management has the status Legacy.
* **Which one should new implementations use?** New implementations should use Decisioning. Decision Management is still supported, but it is no longer recommended for new implementations.
* **Which channels are listed for Decisioning and for Decision Management?** Decisioning is available for Code-based Experience, Web, Email, Push, Mobile messages, Custom channels, and Direct mail. Decision Management supports Email, In-App, Push, Mobile messages, and Direct mail.
* **How are Engageable Profiles counted?** They are the unique customer profiles engaged through journeys, campaigns, or decisioning activities over a rolling 12-month window, and each profile is counted once per sandbox regardless of how many journeys or campaigns it enters. Monitor the count at Administration > License Usage.
* **Where can I find definitions of real-time customer profiles, sandboxes, schemas, and datasets?** These are Adobe Experience Platform concepts, not Journey Optimizer-specific ones. For definitions of those terms, refer to the Adobe Experience Platform glossary.
* **How are the three campaign types activated?** Action campaigns are activated manually or on a schedule, API-triggered campaigns by an external API call, and Orchestrated campaigns through a visual workflow canvas.

**Examples:**

* Personalization: inserting a customer's name or showing product recommendations based on browsing history.
* Audience: "customers who purchased in the last 30 days" or "loyalty program members."
* Fragment: a header, footer, or promotional banner.

**Best practices:**

* Decisioning is recommended for all new implementations. Decision Management is no longer recommended for new implementations, and new implementations should use Decisioning instead.

**Related pages:**

* New to Journey Optimizer: five core concepts (start/understanding-ajo.md)
* To see how journeys, campaigns, profiles, and channels fit together in the product architecture: Understanding how Journey Optimizer works (start/understanding-ajo.md)
* To get started with Decisioning: Decisioning (experience-decisioning/gs-experience-decisioning.md)
* To get started with Decision Management: Decision Management (offers/get-started/starting-offer-decisioning.md)
* To compare Decisioning and Decision Management side by side and choose the right approach for your implementation: Get started with decision capabilities (experience-decisioning/gs-decision.md)
* If you are currently using Decision Management and want to switch: migration guide (experience-decisioning/migrate-to-decisioning.md)
* For a full overview of all campaign types and when to use each: Get started with campaigns (campaigns/get-started-with-campaigns.md)
* To get started with Action campaigns: Action campaigns (campaigns/create-campaign.md)
* To get started with API-triggered campaigns: API-triggered campaigns (campaigns/api-triggered-campaigns.md)
* To get started with Orchestrated campaigns: Orchestrated campaigns (orchestrated/gs-orchestrated-campaigns.md)
* For frequency capping by channel: Set frequency capping by channel (conflict-prioritization/channel-capping.md)
* For journey capping and arbitration: Manage journey capping & arbitration (conflict-prioritization/journey-capping.md)
* To learn how to use rule sets, frequency capping, priority scores, and quiet hours to avoid over-messaging: Conflict management & prioritization (conflict-prioritization/gs-conflict-prioritization.md)
* To get started with Content Cards: Content Cards (content-card/create-content-card.md)
* To get started with In-App messages: In-App messages (in-app/get-started-in-app.md)
* To learn how to build event-triggered, sequential customer experiences: Get started with journeys (building-journeys/journey.md)
* To browse all available channels, their prerequisites, and how to configure them: Get started with communication channels (channels/gs-channels.md)

**Personas:**

* **admin:** Can monitor the Engageable Profiles count at Administration > License Usage, the key license metric for Journey Optimizer. The page states that each profile is counted once per sandbox regardless of how many journeys or campaigns it enters. Where: "Customer & audience terms".
* **developer:** Can look up that API-triggered campaigns are activated by an external API call, with profile attributes plus API payload context as personalization source. The page states that many foundational concepts, such as real-time customer profiles, sandboxes, schemas, and datasets, are Adobe Experience Platform concepts, not Journey Optimizer-specific ones. Where: "Terminology".
* **marketer:** Can compare Action campaigns (manual or scheduled), API-triggered campaigns (external API call), and Orchestrated campaigns (visual workflow canvas) by activation. Where: "Campaign types".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Start with the five core concepts if you are new to Journey Optimizer.
* **Previous:** You are new to Journey Optimizer: five core concepts (start/understanding-ajo.md)
* **Next:** Compare Decisioning and Decision Management side by side and choose the right approach for your implementation: Get started with decision capabilities (experience-decisioning/gs-decision.md); Get a full overview of all campaign types and when to use each: Get started with campaigns (campaigns/get-started-with-campaigns.md)

+++

<!-- ai-section-version: 1 | source-hash: 3bd3f8ee -->
