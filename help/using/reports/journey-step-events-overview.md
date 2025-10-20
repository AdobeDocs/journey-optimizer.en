---
solution: Journey Optimizer
product: journey optimizer
title: Work with journey step events
description: Learn how to work with journey step events in Adobe Journey Optimizer - understand what they are, why they matter, and how to use them for analytics and optimization
feature: Journeys, Reporting
topic: Content Management
role: Engineer, Admin, User
level: Intermediate, Experienced
keywords: journey, step events, analytics, reporting, monitoring, XDM
hide: yes
hidefromtoc: yes
---
# Work with journey step events {#work-with-journey-step-events}

Journey step events are automatically generated events that capture detailed information about each step a [profile](../audience/get-started-profiles.md) takes as they progress through a [journey](../building-journeys/journey.md) in Adobe Journey Optimizer. These events provide comprehensive visibility into [journey performance](../building-journeys/report-journey.md) and enable powerful analytics capabilities.

## What are journey step events? {#what-are-step-events}

Journey step events are system-generated [XDM (Experience Data Model)](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"} events that Adobe Journey Optimizer automatically creates and sends to [Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/home.html){target="_blank"} whenever a profile moves from one node to another in a journey. Each event corresponds to a specific [journey activity](../building-journeys/about-journey-activities.md) or transition in the customer's journey experience.

There are two main types of journey step events:

- **journeyStepEvent**: Events related to individual profile progression through journey steps
- **journeyStepProfileEvent**: Events that include additional profile context information

### What triggers journey step events? {#event-triggers}

Journey step events are generated automatically for various journey activities:

- **Entry events**: When a profile [enters a journey](../building-journeys/entry-management.md)
- **Action execution**: When [messages are sent](../building-journeys/journeys-message.md) or [custom actions](../building-journeys/using-custom-actions.md) are performed  
- **Condition evaluation**: When profiles pass through [conditions](../building-journeys/condition-activity.md) and decision points
- **Wait activities**: When profiles enter and exit [wait nodes](../building-journeys/wait-activity.md)
- **Exit events**: When profiles complete or [exit a journey](../building-journeys/end-journey.md)
- **Error handling**: When errors occur during journey execution

>[!NOTE]
>
>Journey step events are activated by default on all instances. You cannot modify or update the [schemas and datasets](sharing-overview.md) that have been created during provisioning for step events. These schemas and datasets are in read-only mode.

Learn more about [journey step event schemas](sharing-field-list.md).

## Why journey step events matter {#why-step-events-matter}

Journey step events provide critical value for organizations using Adobe Journey Optimizer:

### Real-time analytics and monitoring {#real-time-analytics}

- **Journey performance tracking**: Monitor how profiles flow through your journeys in real-time using [live reports](live-report.md)
- **Conversion analysis**: Understand drop-off points and successful conversion paths with [journey analytics](journey-global-report-cja.md)
- **Error detection**: Identify and troubleshoot issues as they occur through [monitoring and alerts](alerts.md)

### Data integration and insights {#data-integration}

- **Cross-platform analysis**: Combine journey data with other [Adobe Experience Platform data sources](../datasource/adobe-experience-platform-data-source.md)
- **Customer 360 view**: Create comprehensive [customer profiles](../audience/get-started-profiles.md) that include journey interactions  
- **Attribution modeling**: Connect journey touch points to downstream business outcomes using [Customer Journey Analytics](cja-ajo.md)

### Optimization opportunities {#optimization}

- **A/B testing insights**: Analyze the performance of different journey paths using [experimentation](campaign-global-report-cja-experimentation.md)
- **Personalization enhancement**: Use journey behavior data to improve future experiences with [dynamic content](../personalization/dynamic-content.md)
- **Operational efficiency**: Identify bottlenecks and optimize [journey design](../building-journeys/using-the-journey-designer.md)

## How to use journey step events {#how-to-use-step-events}

### Accessing journey step event data {#accessing-data}

Journey step event data is automatically stored in Adobe Experience Platform and can be accessed through:

1. **Data Lake queries**: Use SQL to query the `journey_step_events` dataset with [Query Service](https://experienceleague.adobe.com/docs/experience-platform/query/home.html){target="_blank"}
2. **Customer Journey Analytics**: Analyze journey data through [advanced analytics tools](cja-ajo.md)
3. **Real-time reporting**: Access data through Journey Optimizer's [built-in reporting capabilities](gs-reports.md)
4. **APIs**: Programmatically access event data for custom applications

Learn more about [accessing datasets](../data/datasets-query-examples.md).

### Key data points available {#key-data-points}

Journey step events capture comprehensive information including:

- **Journey identification**: [Journey ID, version, and name](sharing-journey-fields.md)
- **Profile information**: [Profile ID and associated identities](sharing-identity-fields.md) 
- **Step details**: [Node name, step type, and execution status](sharing-common-fields.md)
- **Timestamps**: Precise timing of each journey step
- **Action results**: [Success/failure status and execution details](sharing-execution-fields.md)
- **Error information**: Detailed [error codes and descriptions](sharing-field-list.md#discarded-events) when issues occur

Explore all [available field definitions](sharing-field-list.md).

### Common use cases {#common-use-cases}

**Performance monitoring**

```sql
-- Example: Count profiles entering a journey in the last 24 hours
SELECT count(distinct _experience.journeyOrchestration.stepEvents.profileID)
FROM journey_step_events 
WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey-id>'
AND _experience.journeyOrchestration.stepEvents.nodeType='start'
AND DATE(timestamp) > (now() - interval '24' hour);
```

**Error analysis**

```sql
-- Example: Identify errors by journey node
SELECT _experience.journeyOrchestration.stepEvents.nodeName,
       count(distinct _experience.journeyOrchestration.stepEvents.profileID)
FROM journey_step_events
WHERE _experience.journeyOrchestration.stepEvents.actionExecutionError IS NOT NULL
GROUP BY _experience.journeyOrchestration.stepEvents.nodeName;
```

**Journey funnel analysis**

- Track conversion rates at each journey step
- Identify where profiles most commonly exit the journey
- Measure time spent in different journey phases

Learn more [query techniques for funnel analysis](query-examples.md#common-queries).

## Samples and resources {#samples-resources}

### Query examples and templates {#query-examples}

Explore comprehensive query examples for common journey step event analysis:

- **[Journey step event query examples](query-examples.md)**: Ready-to-use SQL queries for common analytics scenarios
- **[Dataset query samples](../data/datasets-query-examples.md#journey-step-event)**: Examples of querying journey step event datasets
- **[Profile-based queries](query-examples.md#profile-based-queries)**: Track individual profile journeys and interactions

### Field documentation {#field-documentation}

Understand the complete data structure of journey step events:

- **[Journey step event field list](sharing-field-list.md)**: Comprehensive reference of all available fields
- **[Common fields](sharing-common-fields.md)**: Shared fields across journeyStepEvent and journeyStepProfileEvent
- **[Action execution fields](sharing-execution-fields.md)**: Fields specific to action execution tracking
- **[Journey fields](sharing-journey-fields.md)**: Journey-specific metadata and identifiers

### Best practices and troubleshooting {#best-practices}

**Performance optimization**

- Use `journeyVersionID` instead of `journeyVersionName` for better query performance ([learn more about journey properties](../building-journeys/expression/journey-properties.md))
- Filter by date ranges to improve query speed on large datasets
- Leverage profile identities that match your [journey namespace configuration](../building-journeys/entry-management.md)

**Data quality**

- Regularly monitor for [discarded events](sharing-field-list.md#discarded-events) to identify data issues
- Validate that event schemas match your analysis requirements
- Implement proper error handling in custom queries

**Analytics strategies**

- Combine journey step events with [message feedback data](../data/datasets-query-examples.md#message-feedback-event-dataset) for complete attribution
- Use time-based analysis to understand journey velocity and bottlenecks

### Advanced analytics capabilities {#advanced-analytics}

**Customer Journey Analytics integration**
Journey step events can be analyzed using [Customer Journey Analytics](cja-ajo.md) for:

- Advanced attribution modeling
- Cross-channel journey visualization  
- Predictive analytics on journey outcomes

Learn how to [configure Customer Journey Analytics](report-gs-cja.md) for Journey Optimizer data.

## Additional resources {#additional-resources}

### Documentation links {#documentation-links}

- **[Journey step sharing overview](sharing-overview.md)**: Understanding how journey data flows to Adobe Experience Platform
- **[Built-in schemas dictionary](https://experienceleague.adobe.com/tools/ajo-schemas/schema-dictionary.html){target="_blank"}**: Complete XDM schema reference
- **[Journey Optimizer reporting](report-gs-cja.md)**: Overview of reporting capabilities in Journey Optimizer

### Integration guides {#integration-guides}

- **[Adobe Customer Journey Analytics](cja-ajo.md)**: Analyzing Journey Optimizer data in CJA
- **[Data management](../data/export-datasets.md)**: Exporting and managing journey data
- **[Privacy and governance](../privacy/audit-logs.md)**: Data governance considerations for journey events


**Next steps:**

- Start with [creating your first journey reports](sharing-overview.md)
- Explore [query examples](query-examples.md) for specific use cases  
- Learn about [journey management best practices](../building-journeys/journey.md)
