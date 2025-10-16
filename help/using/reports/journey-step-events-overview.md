---
solution: Journey Optimizer
product: journey optimizer
title: Work with journey step events
description: Learn how to work with journey step events in Adobe Journey Optimizer - understand what they are, why they matter, and how to use them for analytics and optimization
feature: Journeys, Reporting
topic: Content Management
role: Data Engineer, Data Architect, Admin, User
level: Intermediate, Experienced
keywords: journey, step events, analytics, reporting, monitoring, XDM
hide: yes
hidefromtoc: yes
exl-id: 9f8e7d6c-5b4a-3928-1756-849302a11c2b
---
# Work with journey step events {#work-with-journey-step-events}

Journey step events are automatically generated events that capture detailed information about each step a profile takes as they progress through a journey in Adobe Journey Optimizer. These events provide comprehensive visibility into journey performance and enable powerful analytics capabilities.

## What are journey step events? {#what-are-step-events}

Journey step events are system-generated XDM (Experience Data Model) events that Adobe Journey Optimizer automatically creates and sends to Adobe Experience Platform whenever a profile moves from one node to another in a journey. Each event corresponds to a specific action or transition in the customer's journey experience.

There are two main types of journey step events:

- **journeyStepEvent**: Events related to individual profile progression through journey steps
- **journeyStepProfileEvent**: Events that include additional profile context information

### What triggers journey step events? {#event-triggers}

Journey step events are generated automatically for various journey activities:

- **Entry events**: When a profile enters a journey
- **Action execution**: When messages are sent or custom actions are performed  
- **Condition evaluation**: When profiles pass through decision points
- **Wait activities**: When profiles enter and exit wait nodes
- **Exit events**: When profiles complete or exit a journey
- **Error handling**: When errors occur during journey execution

>[!NOTE]
>
>Journey step events are activated by default on all instances. You cannot modify or update the schemas and datasets that have been created during provisioning for step events. These schemas and datasets are in read-only mode.

## Why journey step events matter {#why-step-events-matter}

Journey step events provide critical value for organizations using Adobe Journey Optimizer:

### Real-time analytics and monitoring {#real-time-analytics}

- **Journey performance tracking**: Monitor how profiles flow through your journeys in real-time
- **Conversion analysis**: Understand drop-off points and successful conversion paths
- **Error detection**: Identify and troubleshoot issues as they occur

### Data integration and insights {#data-integration}

- **Cross-platform analysis**: Combine journey data with other Adobe Experience Platform data sources
- **Customer 360 view**: Create comprehensive customer profiles that include journey interactions
- **Attribution modeling**: Connect journey touch points to downstream business outcomes

### Optimization opportunities {#optimization}

- **A/B testing insights**: Analyze the performance of different journey paths
- **Personalization enhancement**: Use journey behavior data to improve future experiences
- **Operational efficiency**: Identify bottlenecks and optimize journey design

## How to use journey step events {#how-to-use-step-events}

### Accessing journey step event data {#accessing-data}

Journey step event data is automatically stored in Adobe Experience Platform and can be accessed through:

1. **Data Lake queries**: Use SQL to query the `journey_step_events` dataset
2. **Customer Journey Analytics**: Analyze journey data through advanced analytics tools
3. **Real-time reporting**: Access data through Journey Optimizer's built-in reporting capabilities
4. **APIs**: Programmatically access event data for custom applications

### Key data points available {#key-data-points}

Journey step events capture comprehensive information including:

- **Journey identification**: Journey ID, version, and name
- **Profile information**: Profile ID and associated identities
- **Step details**: Node name, step type, and execution status
- **Timestamps**: Precise timing of each journey step
- **Action results**: Success/failure status and execution details
- **Error information**: Detailed error codes and descriptions when issues occur

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

- Use `journeyVersionID` instead of `journeyVersionName` for better query performance
- Filter by date ranges to improve query speed on large datasets
- Leverage profile identities that match your journey namespace configuration

**Data quality**

- Regularly monitor for [discarded events](sharing-field-list.md#discarded-events) to identify data issues
- Validate that event schemas match your analysis requirements
- Implement proper error handling in custom queries

**Analytics strategies**

- Combine journey step events with message feedback data for complete attribution
- Use time-based analysis to understand journey velocity and bottlenecks
- Create cohort analyses to compare different journey variations

### Advanced analytics capabilities {#advanced-analytics}

**Customer Journey Analytics integration**
Journey step events can be analyzed using Customer Journey Analytics for:

- Advanced attribution modeling
- Cross-channel journey visualization  
- Predictive analytics on journey outcomes

**Real-time decisioning**
Use journey step event patterns to:

- Trigger real-time personalization
- Implement dynamic journey optimization
- Enable contextual next-best-action recommendations

## Additional resources {#additional-resources}

### Documentation links {#documentation-links}

- **[Journey step sharing overview](sharing-overview.md)**: Understanding how journey data flows to Adobe Experience Platform
- **[Built-in schemas dictionary](https://experienceleague.adobe.com/tools/ajo-schemas/schema-dictionary.html)**: Complete XDM schema reference
- **[Journey Optimizer reporting](report-gs-cja.md)**: Overview of reporting capabilities in Journey Optimizer

### Integration guides {#integration-guides}

- **[Adobe Customer Journey Analytics](cja-ajo.md)**: Analyzing Journey Optimizer data in CJA
- **[Data management](../data/export-datasets.md)**: Exporting and managing journey data
- **[Privacy and governance](../privacy/audit-logs.md)**: Data governance considerations for journey events

Journey step events form the foundation of advanced journey analytics in Adobe Journey Optimizer. By understanding and leveraging these events effectively, you can gain deep insights into customer behavior, optimize journey performance, and create more personalized experiences for your customers.
