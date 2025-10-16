---
solution: Journey Optimizer
product: journey optimizer
title: Journeys Frequently Asked Questions
description: Frequently Asked Questions about Journey Optimizer Journeys
feature: Journeys, Get Started
topic: Content Management
role: User
level: Beginner, Intermediate
keywords: journey, questions, answers, troubleshoot, help, guide
version: Journey Orchestration
hide: yes
hidefromtoc: yes
---

# Frequently Asked Questions {#faq-journeys}

You will find below Frequently Asked Questions about Adobe Journey Optimizer Journeys.

Need more details? Use the feedback options at the bottom of this page to raise your question, or connect with [Adobe Journey Optimizer community](https://experienceleaguecommunities.adobe.com/t5/adobe-journey-optimizer/ct-p/journey-optimizer?profile.language=en){target="_blank"}.

## General concepts

+++ What is a journey in Adobe Journey Optimizer?

A journey is a multi-step orchestration that allows you to design and execute real-time customer experiences across multiple channels. Journeys combine events, orchestration activities, actions, and messages to create personalized, contextual experiences based on customer behavior and business events.

Learn more about [journeys](journey.md).

+++

+++ What are the different types of journeys?

Adobe Journey Optimizer supports three types of journeys:

* **Unitary journeys**: Triggered individually by an event (e.g., a purchase, app sign-in). Profiles enter the journey one at a time when the event occurs.
* **Read Audience journeys**: Start with an audience from Adobe Experience Platform and send messages in batch to all profiles in that audience.
* **Business event journeys**: Triggered by business events (e.g., stock updates, weather alerts) that affect multiple profiles simultaneously.

Learn more about [journey types](entry-management.md#types-of-journeys).

+++

+++ What's the difference between a journey and a campaign?

**Journeys** are multi-step orchestrations that react to events or target audiences, allowing for complex logic, conditions, wait times, and multiple touch points across the customer lifecycle.

**Campaigns** are one-time or recurring communications sent to a specific audience, ideal for standalone messages like promotional announcements or newsletters.

**Best practice**: Use journeys for ongoing, multi-step engagement, and campaigns for targeted, standalone communications.

+++

+++ What are the main components of a journey?

A journey consists of:

* **Events**: Entry points that trigger the journey (e.g., profile qualification, business events)
* **Orchestration activities**: Logic components like conditions, wait, read audience, and end
* **Actions**: Activities that perform tasks, such as sending messages, updating profiles, or calling external APIs
* **Built-in channel actions**: Native messaging capabilities for email, SMS, push, and other channels
* **Custom actions**: Integration with third-party systems

Learn more about [journey activities](about-journey-activities.md).

+++

## Building journeys

+++ How do I start building my first journey?

Follow these key steps:

1. **Set up prerequisites**: Configure events, data sources, and actions as needed
2. **Create the journey**: Navigate to the Journeys menu and click "Create Journey"
3. **Define journey properties**: Set the journey name, description, namespace, and other settings
4. **Design the journey**: Drag and drop activities from the palette into the canvas
5. **Test the journey**: Use test mode to validate your journey logic
6. **Publish the journey**: Activate the journey to make it live

Follow the [step-by-step guide](journey-gs.md).

+++

+++ What prerequisites are needed before building a journey?

Prerequisites depend on your journey type:

* **Event-triggered journeys**: Configure events to define when profiles should enter the journey
* **Audience-based journeys**: Create audiences in Adobe Experience Platform
* **Data enrichment**: Set up data sources to retrieve additional information
* **Third-party integrations**: Configure custom actions if using external systems

Learn more about [journey configuration](../configuration/about-data-sources-events-actions.md).

+++

+++ Can I use data from external systems in my journey?

Yes. You can configure **external data sources** to retrieve information from third-party API services and use it in your journey conditions, personalization, or actions. This allows you to enrich the customer experience with real-time data from your CRM, loyalty systems, weather services, or other external platforms. 

Learn more about [external data sources](../datasource/external-data-sources.md).

+++

+++ How do I add conditions to my journey?

You can add conditions using the **Condition activity** from the orchestration palette. Conditions allow you to:

* Create simple or advanced conditions using the expression editor
* Split the journey into multiple paths based on profile attributes, audience membership, events, or contextual data
* Define timeout paths for profiles that don't meet the condition within a specified time

Learn more about [conditions](condition-activity.md).

+++

+++ Can I send messages to profiles in a journey?

Yes. Journey Optimizer includes **built-in channel actions** that allow you to send messages through email, push notifications, SMS/MMS/RCS, in-app messages, web experiences, code-based experiences, direct mail, content cards, WhatsApp, and LINE. You can design message content directly in Journey Optimizer and add them as action activities in your journey. 

Learn more about [messages in journeys](journeys-message.md).

+++

+++ How do I wait for a specific time or event in a journey?

Use the **Wait activity** to pause the journey for a specified duration or until a specific date/time. Wait activities are useful for:

* Sending follow-up messages after a delay (e.g., 3 days after purchase)
* Waiting for business hours before taking action
* Creating drip campaigns with timed intervals
* Combining with conditions to create timeout scenarios

Learn more about [wait activities](wait-activity.md).

+++

+++ Can I update profile information within a journey?

Yes. Use the **Update Profile** activity to modify profile attributes in Adobe Experience Platform based on journey events or conditions. This is useful for updating loyalty points, recording journey milestones, changing preference settings, or tracking customer engagement scores.

Learn more about [profile updates](update-profiles.md).

+++

## Testing and publishing

+++ How do I test my journey before publishing it?

Journey Optimizer offers two testing approaches:

* **Test mode**: Simulate individual profiles moving through the journey step by step, allowing you to verify logic, conditions, and actions before going live.
* **Dry run mode**: Execute your journey using real production data without contacting actual customers or updating profile information. This gives you confidence in audience targeting and journey design.

**Best practice**: Always test journeys before publishing to ensure they work as expected and to identify any issues early.

Learn more about [test mode](testing-the-journey.md) and [dry run](journey-dry-run.md).

+++

+++ What happens when I publish a journey?

When you publish a journey:

* The journey becomes **active** and ready to accept new profiles
* Profiles can enter based on the entry criteria (event or audience)
* Messages and actions start executing for profiles moving through the journey
* You cannot directly edit a published journey (you must create a new version)

Learn more about [publishing journeys](publishing-the-journey.md).

+++

+++ Can I modify a journey that is already published?

You cannot directly edit a live journey. To make changes:

1. **Create a new version**: Duplicate the published journey to create a draft version
2. **Make your changes**: Edit the draft version as needed
3. **Test the new version**: Use test mode to validate changes
4. **Publish the new version**: This automatically closes the previous version and activates the new one

Profiles already in the journey will complete the original version, while new profiles will enter the new version.

Learn more about [journey versions](journey-ui.md#journey-versions).

+++

+++ How do I stop a journey?

You can manage journey execution in several ways:

* **Close to new entrances**: Stop new profiles from entering while allowing existing profiles to complete their journey
* **Stop immediately**: End the journey and exit all profiles currently in it
* **Pause**: Temporarily halt the journey and resume it later (available for specific journey types)

Learn more about [ending journeys](end-journey.md).

+++

## Journey execution and monitoring

+++ How can I track profile progress through a journey?

You can monitor journey execution using:

* **Journey Live Report**: View real-time metrics and KPIs for your journey
* **Journey All Time Report**: Analyze journey performance using Customer Journey Analytics
* **Journey Step Events**: Access detailed execution data for custom reporting
* **Journey Dry Run Dashboard**: Review test execution results before going live

Learn more about [journey reporting](report-journey.md).

+++

+++ Why didn't a profile enter my journey?

Common reasons profiles may not enter a journey:

* **Event not received**: The triggering event was not sent or properly configured
* **Audience criteria not met**: The profile doesn't qualify for the entry audience
* **Re-entrance rules**: The profile recently completed the journey and re-entrance is blocked
* **Journey not published**: The journey is in draft status
* **Invalid namespace**: The journey namespace doesn't match the profile identity
* **Journey closed**: The journey is no longer accepting new entrances

Learn more about [entry management](entry-management.md).

+++

+++ What are journey step events and how can I use them?

Journey step events are automatically generated datasets that capture detailed information about every step a profile takes in a journey. They include entry and exit events, action execution (messages sent, custom actions called), journey transitions (moving between activities), and errors and timeouts.

**Use cases**:

* Build custom reports in Customer Journey Analytics or BI tools
* Debug journey execution issues
* Track detailed profile behavior
* Create advanced analytics and attribution models

Learn more about [journey step events](../reports/sharing-overview.md).

+++

+++ How can I troubleshoot a journey that isn't working as expected?

Journey Optimizer provides several troubleshooting resources:

* **Error indicators**: Visual alerts in the journey canvas highlight configuration issues
* **Test mode**: Step through the journey to identify where problems occur
* **Journey reports**: Review execution metrics to find bottlenecks or errors
* **Journey step events**: Analyze detailed execution data to understand profile behavior

**Common issues**:

* Incorrectly configured events or audiences
* Missing data source connections
* Invalid expressions in conditions or personalization
* Timeout settings that are too short

Learn more about [troubleshooting journeys](troubleshooting.md).

+++

+++ What happens if an action fails in a journey?

When an action fails (e.g., API call timeout, message delivery error), the journey continues by default unless configured otherwise. You can define condition activities to handle failure scenarios, and errors are logged in journey reports and step events for monitoring.

**Best practice**: Set appropriate timeout values for external actions and define alternative paths for critical failure scenarios.

Learn more about [action responses](../action/action-response.md).

+++

## Advanced concepts

+++ What is a journey namespace and why does it matter?

A **namespace** is an identity type (e.g., email, ECID, phone number) that determines how profiles are identified in the journey. The namespace defines which identifier is used to match profiles, must be consistent across events, audiences, and profile data, and affects journey entry and re-entrance behavior.

**Best practice**: Choose a namespace that reliably identifies your customers across all touch points.

Learn more about [identity namespaces](../audience/get-started-identity.md).

+++

+++ Can profiles enter the same journey multiple times?

Yes, depending on the **re-entrance settings**:

* **Allow re-entrance**: Profiles can enter the journey multiple times after completing it
* **Re-entrance wait period**: Define a minimum time between journey entries (e.g., 7 days)
* **Force re-entrance on event**: Trigger a new journey instance even if the profile is already in the journey

**Best practice**: Use re-entrance rules to prevent message fatigue and ensure appropriate pacing.

Learn more about [entry management](entry-management.md).

+++

+++ What is send-time optimization?

**Send-Time Optimization (STO)** uses AI to predict the best time to send a message to each individual profile, maximizing open rates and engagement. STO analyzes historical engagement patterns to determine when each recipient is most likely to interact with your message.

**Benefits**:

* Improved open and click rates
* Better customer experience through optimally-timed messages
* Reduced unsubscribe rates

Learn more about [send-time optimization](send-time-optimization.md).

+++

+++ What are journey capping rules?

**Journey capping** allows you to limit the number of times a profile can enter journeys within a specified time period, preventing message fatigue and ensuring optimal customer experience. You can set maximum entries per profile across journeys or specific journeys, define time windows (daily, weekly, monthly), and prioritize journeys when multiple journeys compete for the same profile.

Learn more about [journey capping](../conflict-prioritization/journey-capping.md).

+++

+++ Can I integrate my journey with external systems?

Yes. Use **custom actions** to call third-party APIs (CRM, marketing automation, loyalty systems), send data to external systems, retrieve real-time information for decisioning, and trigger workflows in external platforms. 

Custom actions support authentication (API key, OAuth 2.0), request/response payload customization, error handling and timeouts, and dynamic parameters from journey context.

Learn more about [custom actions](using-custom-actions.md).

+++

+++ How can I use Adobe Campaign with journeys?

Journey Optimizer integrates natively with Adobe Campaign to leverage its advanced capabilities:

* **Adobe Campaign Standard**: Use Campaign Standard actions to send transactional messages
* **Adobe Campaign v7/v8**: Trigger Campaign workflows and use Campaign's delivery infrastructure

**Best practice**: Use this integration if you have existing Campaign templates, data models, or require Campaign-specific features.

Learn more about [Campaign integration](ajo-ac.md).

+++

+++ What is the Jump activity?

The **Jump activity** allows you to transition profiles from one journey to another, enabling reusable journey patterns, journey orchestration across multiple journeys, simplified journey maintenance, and progressive engagement strategies.

When a profile reaches a Jump activity, they exit the current journey and enter the target journey at its starting point.

Learn more about [the Jump activity](jump.md).

+++

## Best practices and limitations

+++ What are the key limitations I should be aware of?

Important guardrails include:

* **Journey complexity**: Maximum activities, paths, and nesting levels
* **Throughput**: Message sending rates and API call limits
* **Time-to-live**: Maximum journey duration (e.g., 91 days for unitary journeys)
* **Audience size**: Limits on read audience batch sizes
* **Expression complexity**: Character limits in conditions and personalization

View complete [guardrails and limitations](../start/guardrails.md).

+++

+++ What are best practices for journey design?

**Structure and organization**:

* Keep journeys focused on specific use cases
* Use descriptive naming for activities
* Add notes and labels for complex logic
* Group related journeys with tags

**Performance**:

* Optimize wait times to balance engagement and volume
* Limit external API calls to essential use cases
* Use capping rules to prevent message fatigue
* Monitor journey metrics regularly

**Testing**:

* Always test journeys before publishing
* Test all conditional paths and scenarios
* Use realistic test profiles
* Validate personalization and dynamic content

**Maintenance**:

* Regularly review journey performance
* Archive or close unused journeys
* Document journey logic and business rules
* Plan for journey versioning

Learn more about [journey design best practices](using-the-journey-designer.md).

+++

+++ How many activities can I add to a journey?

While there's no strict limit on the number of activities, very complex journeys (50+ activities) can become difficult to maintain and troubleshoot. Large journeys with many branches and conditions may impact processing time and readability.

**Best practice**: If your journey becomes too complex, consider breaking it into multiple journeys using the Jump activity, creating reusable sub-journeys, or simplifying logic with more efficient conditions.

Learn more about [journey design](using-the-journey-designer.md).

+++

+++ How do I ensure my journey performs well at scale?

**Design considerations**:

* Use audience-based entry for batch communications instead of individual events
* Implement appropriate wait times to spread message volume
* Leverage capping rules to prevent system overload
* Optimize condition logic to reduce processing complexity

**Monitoring**:

* Track journey metrics regularly
* Monitor API performance for custom actions
* Review error rates and timeout occurrences
* Set up alerts for critical journey failures

**Optimization**:

* Use test mode and dry run to validate performance before publishing
* Limit external data source calls to essential scenarios
* Cache frequently accessed data when possible
* Review and optimize message delivery performance

Learn more about [journey optimization](../start/guardrails.md).

+++

## Additional Resources

For more learning and updates, explore the following resources:

* [Get started with journeys](journey.md)
* [Create your first journey](journey-gs.md)
* [Troubleshooting guides](troubleshooting.md)
* [Journey use cases](jo-use-cases.md)
* [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"}
