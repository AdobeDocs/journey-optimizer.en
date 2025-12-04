---
title: Migrate from Decision management to Decisioning
description: Learn about the benefits of migrating from Decision management to Decisioning
feature: Decisioning
topic: Integrations
role: User
level: Experienced

---
# Migrate from Decision management to Decisioning {#migrate-to-decisioning}

## What is Decisioning? {#what-is-decisioning}

Journey Optimizer Decisioning is an expansion of decisioning functionality that lays the groundwork for decisioning on other objects (like journeys) in the future. This new capability unifies key workflow concepts for streamlined authoring and management, introduces experimentation into decisioning, and shifts decisioning items into a schema-based approach for dynamic item rendering.

The next generation decisioning framework and feature set in Adobe Journey Optimizer allows brands to use available data, intelligence, and the context of a customer to determine the best experience for each customer to optimize business value. [Learn more](gs-experience-decisioning.md)

## Why migrate to Decisioning? {#why-migrate}

Decisioning offers significant capabilities and benefits over the legacy Decision management framework:

### AI and machine learning capabilities

* **Custom metrics**: Ability to use custom optimization metrics for AI models. This provides reporting interoperability with [Customer Journey Analytics](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-overview/cja-overview){target="_blank"}, standardizes reporting across both platforms, and improves data consistency and reliability. The seamless integration provides a clearer view of performance metrics and adds new capabilities such as creating simple metrics, publishing audiences, asking ad-hoc questions using Insight Builder, and scheduling reports.

* **Lift measurement**: Ability to visualize explore vs exploit traffic in AI models. This enables marketers and data scientists to quantify how AI exploration improves long-term model performance and discoverability of new winning offers. Transparency into traffic allocation builds trust in AI decisions and empowers teams to optimize for both learning and performance over time. [Learn more](ranking/auto-optimization-model.md#lift)

* **AI formula builder**: Ability to apply AI model score outputs to existing formula capabilities. This empowers marketers to seamlessly combine AI outputs with deterministic rules and weights for more nuanced optimization strategies, increasing control and flexibility while still leveraging machine-learning intelligence. [Learn more](ranking/ranking-formulas.md)

### Experimentation

Ability to experiment on offers, aspects of a given offer, and/or ranking methods. This allows marketers to run controlled experiments on creative, eligibility, and ranking logic to identify high-performing variants, accelerating learning cycles and driving continuous optimization of the decisioning system.

### Enhanced reporting

Dashboard documenting performance of decision items and selection strategies against key elements of the engagement funnel. An intuitive, out-of-the-box decisioning dashboard quickly shows the value of campaign and journey performance for key KPIs across offer and content delivery, display and click engagement, fallback usage rates, and lift from AI and machine-learning ranking models. [Learn more](cja-reporting.md)

### Operational efficiency

* **Sandbox copy**: Ability to copy over objects between sandboxes (e.g., Dev to Prod). This simplifies deployment and testing workflows by enabling seamless migration of decision logic, offers, and configuration objects between environments, reducing setup time and minimizing human error. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/landing/sandboxes/sandbox-tooling){target="_blank"}

* **Schema-based item catalog management**: Ability to define and manage decision items directly to schema-linked datasets, enabling dynamic updates and simplified governance. This streamlines catalog management by syncing decision items with underlying data sources, ensuring content accuracy, enabling faster updates, and supporting governance at scale. [Learn more](items.md)

* **Location-agnostic decisioning**: Ability to make decision logic reusable across placements/locations, decoupling decision selection from delivery. This promotes reusability and efficiency by allowing a single decision model to power multiple placements or surfaces (e.g., web, app, email), centralizing logic and accelerating cross-channel personalization efforts. [Learn more](selection-strategies.md)

* **Reusable content fragments**: Ability to define JSON or HTML content blocks (e.g., titles, headers, footers, CTAs) once and reference them within multiple offer objects. This streamlines content authoring and governance by allowing shared components to be centrally managed and automatically updated across offers. [Learn more](../content-management/fragments.md)

### Upcoming capabilities

* **Channel decisioning**: Ability to use decision logic to determine the best channel for engagement (e.g., email vs. push vs. web), rather than just the best offer within a single channel. This enhances customer experience by optimizing where a message is delivered, not just what is delivered.

* **Message optimization**: Ability to use AI or rule-based approaches to optimize message content for each profile, improving engagement and conversion outcomes. This enables marketers to tailor tone, imagery, and layout dynamically based on audience attributes and performance data.

* **Journey path optimization**: Ability to determine which journey path a profile should follow, based on experimental results, real-time context, rules, and/or propensity to convert. This allows teams to intelligently route profiles through the optimal journey branch, ensuring the right cadence and content for each user.

* **Journey decisioning**: Ability to arbitrate between multiple journeys when a profile qualifies for more than one, ensuring the most valuable or relevant journey is selected. This prevents message conflicts and over-messaging by ranking and selecting the highest-priority journey for each profile.

### Additional features

* **Policy enforcement**: Business user empowerment to use features like [Data Usage Labeling & Enforcement (DULE)](https://experienceleague.adobe.com/en/docs/experience-platform/data-governance/labels/overview){target="_blank"} and [Consent](../action/consent.md) within Decisioning, enabling privacy shield protection across the decisioning workflow. This ensures decisions automatically respect data usage policies and customer consent preferences.

* **Native messaging channel support**: Integrated messaging and decisioning within a single framework across multiple channels ([Code-based experience](../code-based/get-started-code-based.md) and [Email](../email/get-started-email.md) currently available, other channels coming in H1 2026). Intuitive UI support allows users to insert decisioning components directly in message authoring workflows.

* **AEP dataset lookup**: Ability to upload and reference [Adobe Experience Platform datasets](https://experienceleague.adobe.com/en/docs/experience-platform/catalog/datasets/overview){target="_blank"} directly within Offer Selection Rules, Ranking, and Personalized Offer Content. This expands flexibility for personalization and targeting by allowing decision logic to use dynamic external data sources. [Learn more](context-data.md)

* **Scalability & performance**: Architectural enhancement that moves decision computation from the hub to the edge, significantly reducing latency and improving throughput for high-traffic use cases.

## Example use cases {#use-cases}

| Use Case | Decision Management | Decisioning |
|----------|---------------------|-------------|
| **Multi-placement strategy** | A single strategy powers both homepage and mobile app | Decision logic tied to a specific placement (e.g., web or email location) |
| **Consistent offer attributes** | A marketer defines "discountType" and "offerValue" once; every offer inherits these fields automatically | Each offer manages its own attributes manually; no schema-level consistency |
| **Dynamic AI ranking** | A marketer can adjust weighting (e.g., 60% AI conversion score + 40% profit margin) to balance revenue and engagement goals | Rankings rely solely on model output or static rules |
| **A/B testing strategies** | A team can A/B test whether "AI + business rules" outperforms "priority-based ranking" | No built-in experimentation support |
| **Custom AI metrics** | Retailer trains a "likelihood to purchase" model and monitors lift across new vs. known products | Optimizes only against click propensity; no visibility into model exploration or lift |
| **Content reusability** | Updating a header or CTA propagates automatically to hundreds of offers | Each offer stores full content independently |
| **Integrated authoring** | A marketer inserts personalized offers into an email without leaving the message editor | Decisioning and messaging live in separate frameworks with limited integration |
| **Privacy compliance** | A marketer builds an offer rule knowing that consent preferences automatically exclude certain profiles | Requires manual coordination with engineering and data teams for enforcement |
| **Real-time inventory** | Use a product inventory dataset to suppress offers for out-of-stock items in real time | Static data; limited flexibility to use external or contextual datasets |
| **Scale performance** | Real-time personalization for millions of incoming requests under 100ms response time | Decisions made in the hub with higher latency |

## Migration tooling {#migration-tooling}

The Journey Optimizer team is currently working on migration tooling APIs to migrate Decision management entities to Decisioning. This tooling enables seamless migration between sandboxes with dependency resolution and rollback capabilities. If interested, reach out to your Adobe representative.

## Related topics {#related-topics}

* [Get started with Decisioning](gs-experience-decisioning.md)
* [Decisioning guardrails and limitations](decisioning-guardrails.md)
* [Decisioning FAQ](decisioning-faq.md)

