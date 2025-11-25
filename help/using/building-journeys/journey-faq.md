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

Adobe Journey Optimizer supports four types of journeys:

* **Unitary journeys**: Triggered individually by an event (e.g., a purchase, app sign-in). Profiles enter the journey one at a time when the event occurs.
* **Read Audience journeys**: Start with an audience from Adobe Experience Platform and send messages in batch to all profiles in that audience.
* **Audience Qualification journeys**: Triggered when profiles qualify for (or exit from) a specific audience segment. Profiles enter the journey as they meet the audience criteria.
* **Business event journeys**: Triggered by business events (e.g., stock updates, weather alerts) that affect multiple profiles simultaneously.

Learn more about [journey types](entry-management.md#types-of-journeys).

+++

+++ What's the difference between a journey and a campaign?

**[Journeys](journey.md)** are multi-step orchestrations that react to events or target audiences, allowing for complex logic, conditions, wait times, and multiple touch points across the customer lifecycle.

**[Campaigns](../campaigns/get-started-with-campaigns.md)** come in three types:

* **[Action campaigns](../campaigns/create-campaign.md)**: One-time or recurring communications sent to a specific audience, ideal for standalone messages like promotional announcements or newsletters.
* **[API-triggered campaigns](../campaigns/api-triggered-campaigns.md)**: Campaigns triggered via API calls, enabling integration with external systems to send messages based on real-time events or business logic.
* **[Orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md)**: Multi-step, audience-based campaigns built on a canvas that can include conditions, wait times, and multiple actions to create scheduled, coordinated experiences.

**Best practice**: Use [journeys](journey.md) for complex, event-triggered engagement with advanced orchestration; [action campaigns](../campaigns/create-campaign.md) for scheduled, audience-based communications; [API-triggered campaigns](../campaigns/api-triggered-campaigns.md) for programmatic triggering from external systems; and [orchestrated campaigns](../orchestrated/gs-orchestrated-campaigns.md) for multi-step communications with campaign-specific requirements.

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

+++ What types of audiences are supported in journeys and what are their limitations?

Adobe Journey Optimizer supports four types of audiences, each with different characteristics and guardrails:

**1. Streaming audiences**

* **Description**: Audiences that evaluate in real-time as profile data changes
* **Evaluation**: Continuous evaluation when profile attributes or events match segment criteria
* **Journey usage**: Supported in Read Audience, Audience Qualification, and Condition activities
* **Best for**: Real-time engagement based on behavioral changes or profile updates
* **Guardrails**:
  * Maximum audience size depends on your Journey Optimizer license
  * Evaluation latency typically under 5 minutes
  * Complex segment logic may impact evaluation performance

**2. Batch audiences**

* **Description**: Audiences evaluated on a scheduled basis (typically daily)
* **Evaluation**: Processed in batch jobs at scheduled intervals
* **Journey usage**: Supported in Read Audience and Condition activities; limited support in Audience Qualification journeys
* **Best for**: Regular campaigns, newsletters, scheduled communications
* **Guardrails**:
  * Evaluation occurs once per day (default) or at configured schedule
  * Profiles may not reflect real-time changes until next evaluation
  * Read Audience activity can process large batch audiences efficiently

**3. Upload audiences (Custom upload)**

* **Description**: Audiences created by uploading CSV files with profile identifiers
* **Evaluation**: Static list updated only when new files are uploaded
* **Journey usage**: Supported in Read Audience and Condition activities; **not supported** in Audience Qualification journeys
* **Best for**: One-time campaigns, external list imports, targeted communications
* **Guardrails**:
  * CSV file size limits apply (check product documentation for current limits)
  * Audience members are static until refreshed with new upload
  * Identity namespace must match journey namespace
  * Profiles must exist in Adobe Experience Platform

**4. Federated Audience Composition (FAC) audiences**

* **Description**: Audiences created using federated data, allowing you to query and compose audiences from external data warehouses without copying data into Adobe Experience Platform
* **Evaluation**: Static composition updated when the federated audience composition is executed
* **Journey usage**: Supported in Read Audience and Condition activities; **not supported** in Audience Qualification journeys (similar to upload audiences from a backend perspective)
* **Best for**: Enterprise data warehouse integration, audience composition using external data sources, scenarios requiring data to remain in external systems
* **Guardrails**:
  * Audience members are static until next federated composition execution
  * Identity namespace must match journey namespace
  * Performance depends on external data warehouse query capabilities
  * Requires Federated Audience Composition add-on

**Customer Journey Analytics (CJA) audiences**:

While CJA audiences are not directly supported in journeys, you can use a **workaround** by "wrapping" a CJA audience in a segmentation rule. This creates a batch UPS (Unified Profile Service) audience that references the CJA audience, making it available for use in journeys as a batch audience type.

**Journey-specific considerations**:

* **Read Audience journeys**: All four audience types supported; batch export occurs when journey runs
* **Audience Qualification journeys**: Streaming audiences recommended; batch audiences have delayed qualification detection; upload and FAC audiences not supported
* **Condition activities**: All audience types can be used to check membership
* **Namespace alignment**: Audience identity namespace must match the journey's namespace for proper profile identification

**Best practices**:

* Use **streaming audiences** for real-time, event-driven journeys requiring immediate response
* Use **batch audiences** for scheduled communications where daily evaluation is sufficient
* Use **upload audiences** for targeted one-time campaigns with external lists
* Use **FAC audiences** when you need to leverage enterprise data warehouse capabilities without data duplication
* Monitor audience size and evaluation performance in large-scale deployments
* Consider audience refresh rates when designing journey timing and entry conditions

Learn more about [audiences](../audience/about-audiences.md), [creating segments](../audience/creating-a-segment-definition.md), [custom upload audiences](../audience/custom-upload.md), and [Federated Audience Composition](../audience/federated-audience-composition.md).

+++

+++ How do I choose between a unitary journey and a read audience journey?

Use **unitary journeys** when:

* You need to react to individual customer actions in real-time (e.g., purchase confirmation, cart abandonment)
* Each customer should progress at their own pace
* You want to trigger based on specific events

Use **read audience journeys** when:

* You're sending batch communications to a group (e.g., monthly newsletter, promotional campaigns)
* All customers should receive the message around the same time
* You're targeting a pre-defined audience segment

+++

## Building journeys

+++ How do I start building my first journey?

Follow these key steps:

1. **Set up prerequisites**: Configure events, data sources, and actions as needed
2. **Create the journey**: Navigate to the Journeys menu and click "Create Journey"
3. **Define journey properties**: Set the journey name, description, and other settings
4. **Design the journey**: Drag and drop activities from the palette into the canvas
5. **Test the journey**: Use test mode to validate your journey logic
6. **Dry run the journey**: Use Dry run to test the journey using real production data without contacting real customers or updating profile information
7. **Publish the journey**: Activate the journey to make it live

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

Yes, there are several approaches to leverage external data:

**Best practices**:

* **Custom actions**: Call external APIs through custom actions to retrieve or send data to third-party systems. This is the recommended approach for real-time interactions with external systems.
* **Dataset lookup**: If you can load data from external systems into Adobe Experience Platform, use the dataset lookup feature to retrieve information stored in Experience Platform datasets.
* **External data sources**: Configure external data sources to retrieve information from third-party API services (less recommended than the above approaches).

These options allow you to enrich the customer experience with data from your CRM, loyalty systems, weather services, or other external platforms.

Learn more about [custom actions](using-custom-actions.md) and [dataset lookup](dataset-lookup.md).

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

For channels not natively supported, you can use **custom actions** to integrate with external messaging platforms and send messages through any third-party channel.

Learn more about [messages in journeys](journeys-message.md) and [custom actions](using-custom-actions.md).

+++

+++ How do I wait for a specific time or event in a journey?

Use the **Wait activity** to pause the journey for a specified duration or until a specific date/time. Wait activities are useful for:

* Sending follow-up messages after a delay (e.g., 3 days after purchase)
* Creating drip campaigns with timed intervals
* Combining with conditions to create timeout scenarios

Learn more about [wait activities](wait-activity.md).

+++

+++ Can I update profile information within a journey?

Yes. Use the **Update Profile** activity to modify profile attributes in Adobe Experience Platform based on journey events or conditions. This is useful for updating loyalty points, recording journey milestones, changing preference settings, or tracking customer engagement scores.

Learn more about [profile updates](update-profiles.md).

+++

+++ How do I send an email immediately after someone makes a purchase?

Create a **unitary event-triggered journey**:

1. Configure a "Purchase" event with the order details
2. Add the event as your journey entry point
3. Immediately follow with an Email action
4. Design your order confirmation email with personalized order details
5. Publish the journey

The journey will automatically trigger whenever a purchase event is received, sending the confirmation email in real-time.

Learn more about [event configuration](../event/about-events.md) and [email actions](journeys-message.md).

+++

+++ Can I resend a message if someone doesn't open or click it?

Yes. Use a **[!UICONTROL Reaction]** event with a **Timeout**:

1. After sending your message, add a **[!UICONTROL Reaction]** event **immediately** after the channel action (without any **[!UICONTROL Wait]** activity in between)
2. Configure a timeout period (e.g., 3 days) on the **[!UICONTROL Reaction]** event to listen for email opens or clicks
3. Create two paths:
   * **If opened/clicked**: Continue with next steps or end the journey
   * **Timeout path (not opened/clicked)**: Send a reminder email with different subject line

**Best practice**: Limit the number of resends to avoid appearing spammy (typically 1-2 reminders maximum).

>[!IMPORTANT]
>
>Do not place a **[!UICONTROL Wait]** activity between the [channel action](journeys-message.md) and the **[!UICONTROL Reaction]** activity. The **[!UICONTROL Reaction]** must come immediately after the channel action. Use the **[!UICONTROL Reaction]**'s built-in timeout feature to wait for customer responses.

Learn more about [reaction events](reaction-events.md).

+++

+++ How do I create a cart abandonment journey?

Create an event-triggered journey using a **[!UICONTROL Reaction]** event with a Timeout:

1. **Configure a "Cart Abandoned" event**: Triggered when items are added but checkout isn't completed within a timeframe
2. **Send an initial message** (optional): Email acknowledging cart items
3. **Add a [!UICONTROL Reaction] event immediately after the channel action**: Configure it to listen for a Purchase event
4. **Set a timeout period**: Define a timeout (e.g., 1-2 hours) on the **[!UICONTROL Reaction]** event to give the customer time to complete naturally
5. **Create two paths**:
   * **If Purchase event occurs**: End the journey or continue with post-purchase flow
   * **Timeout path (no purchase)**: Send an abandonment reminder email with cart contents
6. **Optional**: Add another **[!UICONTROL Reaction]** event **immediately after** the reminder email with timeout (24 hours) and send a second reminder with an incentive (e.g., 10% discount)

>[!IMPORTANT]
>
>**[!UICONTROL Reaction]** events must be placed immediately after [channel actions](journeys-message.md). Do not place **[!UICONTROL Wait]** activities between the channel action and the **[!UICONTROL Reaction]** activity.

Learn more about [journey use cases](jo-use-cases.md) and [reaction events](reaction-events.md).

+++

+++ How do I split customers into different paths based on their purchase history?

Use a **Condition activity** with audience membership or profile attributes:

1. Add a Condition activity to your journey
2. Create multiple paths based on criteria:
   * **Path 1**: High-value customers (total purchases > $1000)
   * **Path 2**: Regular customers (total purchases $100-$1000)
   * **Path 3**: New customers (total purchases < $100)
3. Add different messages or offers for each path

Learn more about [conditions](condition-activity.md) and [audience qualification](audience-qualification-events.md).

+++

+++ How do I handle different time zones in my journey?

Journey Optimizer provides several options for timezone management:

* **Profile timezone**: Messages are sent based on each individual's timezone stored in their profile
* **Fixed timezone**: All messages use a specific timezone you define

Learn more about [timezone management](timezone-management.md).

+++

+++ How long should I wait between messages in my journey?

**Best practices for wait times**:

* **Transactional messages** (order confirmations): Send immediately
* **Welcome series**: 1-3 days between emails
* **Educational content**: 3-7 days between messages
* **Promotional campaigns**: At least 7 days between offers
* **Re-engagement**: 14-30 days for inactive users

**Factors to consider**:

* Industry standards and customer expectations
* Message urgency and importance
* Your overall messaging frequency across all channels
* Customer engagement patterns

**Tip**: Use journey capping rules to limit the total number of messages a customer receives across all journeys.

Learn more about [wait activities](wait-activity.md) and [journey capping](../conflict-prioritization/journey-capping.md).

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

* The journey becomes **Live** and ready to accept new profiles
* Profiles can enter based on the entry criteria (event or audience)
* Messages and actions start executing for profiles moving through the journey
* You can only edit limited things on a published journey (you must create a new version if you want to edit more)

Learn more about [publishing journeys](publish-journey.md).

+++

+++ Can I modify a journey that is already published?

Yes, but with limitations. You can edit certain elements of a Live journey:

**What you can edit**:

* Journey properties (name, description)
* Message content within existing message activities
* Some journey settings

**What you cannot edit**:

* Journey structure (adding/removing activities)
* Entry conditions
* Journey canvas logic

**To make structural changes**:

1. **Create a new version**: Duplicate the published journey to create a draft version
2. **Make your changes**: Edit the draft version as needed
3. **Test the new version**: Use test mode to validate changes
4. **Publish the new version**: This automatically closes the previous version and activates the new one

Profiles already in the journey will complete the original version, while new profiles will enter the new version.

Learn more about [journey versions](journey-ui.md#journey-filter).

+++

+++ How do I stop a journey?

You can manage journey execution in several ways:

* **Close to new entrances**: Stop new profiles from entering while allowing existing profiles to complete their journey
* **Stop immediately**: End the journey and exit all profiles currently in it
* **Pause**: Temporarily halt the journey and resume it later

Learn more about [ending journeys](end-journey.md).

+++

+++ What's the difference between "Close to new entrances" and "Stop"?

**Close to new entrances**:

* New profiles cannot enter the journey
* Profiles already in the journey continue and complete their path
* Use this when you want to gracefully wind down a journey
* Example: Seasonal campaign that has ended but you want existing customers to complete their experience

**Stop**:

* Immediately ends the journey for all profiles
* All profiles currently in the journey are exited
* Use this for urgent situations or critical errors
* Example: Product recall requiring immediate halt of promotional messages

Learn more about [ending journeys](end-journey.md) and [publishing journeys](publish-journey.md).

+++

## Journey execution and monitoring

+++ How can I track profile progress through a journey?

You can monitor journey execution using:

* **Journey Live Report**: View real-time metrics and KPIs for your journey. You can also review dry run test execution results here.
* **Journey All Time Report**: Analyze journey performance using Customer Journey Analytics. You can also review dry run test execution results here.
* **Journey Step Events**: Access detailed execution data for custom reporting

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
* **Streaming audience qualification timing**: For journeys using Audience Qualification with streaming audiences, profiles may not enter if they were already in the audience before the journey was published, or if the journey hasn't completed its activation period (up to 10 minutes after publishing)

Learn more about [entry management](entry-management.md) and [streaming audience qualification timing considerations](audience-qualification-events.md#streaming-entry-caveats).

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
* **Dry run mode**: Test the journey using real production data without contacting customers to validate targeting and execution
* **Journey reports**: Review execution metrics to find bottlenecks or errors
* **Journey step events**: Analyze detailed execution data to understand profile behavior

**Common issues**:

* Incorrectly configured events or audiences
* Missing data source connections
* Invalid expressions in conditions or personalization
* Timeout settings that are too short

Learn more about [troubleshooting journeys](troubleshooting.md).

+++

<!--
+++ What happens if an action fails in a journey?

When an action fails (e.g., API call timeout, message delivery error), the journey continues by default unless configured otherwise. You can define condition activities to handle failure scenarios, and errors are logged in journey reports and step events for monitoring.

**Best practice**: Set appropriate timeout values for external actions and define alternative paths for critical failure scenarios.

Learn more about [action responses](../action/action-response.md).

+++
-->

+++ Can I see who is currently in my journey right now?

Yes. Use the **Journey Live Report** to view:

* Number of profiles currently in the journey
* Number of profiles at each activity
* Profiles who entered in the last 24 hours
* Real-time execution metrics

To see individual profiles, use **journey step events** in Customer Journey Analytics or query the step event datasets directly.

Learn more about [journey live reporting](report-journey.md).

+++

+++ Why are my messages not being sent in my journey?

**Common reasons and solutions**:

* **Consent issues**: Recipients haven't opted in to receive communications
  Solution: Check consent policies and opt-in status
  
* **Suppression list**: Email addresses are on the suppression list
  Solution: Review the suppression list for bounces or complaints
  
* **Invalid contact information**: Missing or malformed email addresses/phone numbers
  Solution: Validate profile data quality
  
* **Journey not published**: The journey is still in draft mode
  Solution: Publish the journey to activate it
  
 <!-- 
* **Message not approved**: Message content requires approval before sending
  Solution: Submit for approval or check approval status-->
  
* **Channel configuration issue**: Email/SMS configuration is incorrect
  Solution: Verify channel configurations and authentication

Learn more about [troubleshooting](troubleshooting.md) and [consent management](../action/consent.md).

+++

+++ How do I personalize messages in my journey?

You can personalize messages using the **personalization editor**:

**Available personalization data**:

* **Profile attributes**: First name, last name, email, custom fields
* **Event data**: Purchase details, browsing behavior, app activity
* **Contextual data**: Journey variables, external API data
* **Audience membership**: Segment qualifications
* **Computed attributes**: Pre-calculated values

**Example personalization**:

* "Hi `{{profile.firstName}}`, thanks for your purchase of `{{event.productName}}`"
* "Based on your loyalty tier (`{{profile.loyaltyTier}}`), here's a special offer"
* Dynamic content blocks that change based on customer preferences

Learn more about [personalization](../personalization/personalize.md).

+++

+++ Can I send different messages based on preferred channel?

Yes. Use a **[Condition activity](condition-activity.md)** to route profiles based on their preferred channel:

1. Add a [Condition activity](condition-activity.md) in your journey
2. Create a path for each channel by checking the preferred channel profile attribute (e.g., `profile.preferredChannel`)
3. Configure channel-specific paths:
   * **Email path**: Add an [email action](../email/create-email.md) with email-optimized content
   * **SMS path**: Add an [SMS action](../sms/create-sms.md) with concise messaging
   * **Push path**: Add a [push notification action](../push/create-push.md) with short, actionable content
   * **In-app path**: Add an [in-app message action](../in-app/create-in-app.md) for engaged app users
4. Add a default path for profiles without a preference, routing them to your primary channel

**Best practices**:

* Ensure your profile data includes accurate channel preferences
* Design content appropriate for each channel's strengths and limitations
* Use [channel surfaces](../configuration/channel-surfaces.md) to manage channel configurations
* Test all paths to ensure proper message delivery

Learn more about [conditions](condition-activity.md), [message actions](journeys-message.md), and [channel selection](../channels/gs-channels.md).

+++

+++ Can I exclude certain customers from my journey?

Yes, there are several ways to exclude customers:

**At journey entry**:

* Use [audience definitions](../audience/creating-a-segment-definition.md) with exclusion rules
* Add [entry conditions](entry-management.md) that filter out specific profiles
* Configure [profile attribute based exit criteria](journey-properties.md) in journey properties to automatically exclude profiles based on specific attributes

**Within the journey**:

* Add a [Condition activity](condition-activity.md) early in the journey to exit unwanted profiles
* Check for exclusion attributes (e.g., VIP status, test accounts)
* Use [audience qualification](audience-qualification-events.md) to identify profiles to exclude

**Example exclusion scenarios**:

* Exclude customers who recently purchased
* Exclude VIP customers from standard promotions
* Exclude employees and test accounts
* Exclude customers in specific regions

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
* **Supplemental identifier**: Use a supplemental ID to allow profiles to re-enter the journey multiple times for different entities (e.g., different orders, bookings, or transactions), even while they're already in the journey

**Best practice**: Use re-entrance rules to prevent message fatigue and ensure appropriate pacing. Consider using supplemental identifiers for transactional journeys where profiles need to enter multiple times for different transactions.

Learn more about [entry management](entry-management.md) and [supplemental identifiers](supplemental-identifier.md).

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

**Journey capping** allows you to control how profiles interact with journeys, preventing message fatigue and ensuring optimal customer experience:

* **Entry capping**: Limit the number of times a profile can enter journeys within a specified time period
* **Concurrency capping**: Limit the number of journeys a profile can be in simultaneously

You can set maximum entries or concurrency per profile across journeys or specific journeys, define time windows (daily, weekly, monthly), and prioritize journeys when multiple journeys compete for the same profile.

Learn more about [journey capping](../conflict-prioritization/journey-capping.md).

+++

+++ Can I integrate my journey with external systems?

Yes. Use **custom actions** to call third-party APIs (CRM, marketing automation, loyalty systems), send data to external systems, retrieve real-time information for decisioning, and trigger workflows in external platforms. 

Custom actions support authentication (API key, custom authentication), request/response payload customization, error handling and timeouts, and dynamic parameters from journey context.

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

+++ How do I create a welcome series journey?

A typical welcome series includes multiple touchpoints over several days:

**Example structure**:

1. **Entry**: Audience of new subscribers or event when someone signs up
2. **Email 1 - Immediate welcome**: Thank you and introduction
3. **Wait**: 2 days
4. **Email 2 - Getting started**: Tutorial or product guide
5. **Wait**: 3 days
6. **Condition**: Has the customer made a purchase?
   * **Yes**: End or move to customer journey
   * **No**: Continue welcome series
7. **Email 3 - Incentive**: Special first-time buyer discount
8. **Wait**: 5 days
9. **Email 4 - Engagement**: Best-sellers or popular content

**Best practices**:

* Keep it to 3-5 emails over 2-3 weeks
* Each email should have a clear purpose and call-to-action
* Monitor open rates and adjust timing/content accordingly
* Exit customers early if they convert or engage deeply

Learn more about [journey use cases](jo-use-cases.md).

+++

+++ Can I A/B test different paths in my journey?

Yes. Use the **Optimize activity** (Limited Availability) or manually create test splits:

**Using Optimize activity** with the Experiment method:

* Randomly splits traffic between different paths to determine which performs best
* Tests different messages, offers, wait times, or entire journey paths
* Measures performance based on predefined success metrics and declares a winner

**Using Optimize activity** with the Data source condition method:

* Create a condition that randomly splits profiles (e.g., using a random number function)
* Send different experiences to each split
* Measure results using journey reports

**What you can test**:

* Different email subject lines
* Alternative message content
* Different wait times
* Various offers or incentives
* Entirely different journey paths

Learn more about [optimize activity](optimize.md) and [content experiments](../content-management/content-experiment.md).

+++

+++ How do I trigger a journey when inventory is low?

Create a **business event journey**:

1. **Configure a business event**: Set up an event triggered by your inventory system when stock falls below a threshold
2. **Select target audience**: Choose profiles to notify (e.g., customers who viewed the product, subscribers to restock alerts)
3. **Add message action**: Send notification email or push
4. **Personalize content**: Include product details, current inventory level, urgency messaging

**Example business events**:

* Low inventory alert
* Price drop notification
* Product back in stock
* Flash sale announcement
* Weather-based promotions

Learn more about [business events](general-events.md).

+++

+++ What are merge policies and how do they affect journeys?

**Merge policies** determine how Adobe Experience Platform combines data from multiple sources to create a unified profile view. They define rules for data prioritization and identity stitching when profile fragments exist across different datasets.

**Impact on journeys**:

* Journeys use the merge policy associated with the audience or event to determine which profile data is available
  * In Read audience or audience qualification journeys: the merge policy from the audience is used
  * In Unitary event journeys: the default merge policy is used
  * In Business event journeys: the merge policy from the targeted audience in the following Read audience activity is used

* The merge policy affects which attributes are accessible in journey conditions, personalization, and actions
* Different merge policies can result in different profile data being used in the journey

**Best practices**:

* Ensure the merge policy used by your journey aligns with your data governance requirements
* Understand which datasets are included in your merge policy to know what data is available
* Use consistent merge policies across related audiences and journeys for predictable results

Learn more about [merge policies](../audience/get-started-profiles.md) and [identity management](../audience/get-started-identity.md).

+++

+++ What's the difference between a Condition and a Wait activity?

| | **Condition Activity** | **Wait Activity** |
|---|---|---|
| **Purpose** | Creates different paths based on logic (if/then) | Pauses the journey for a period of time |
| **Function** | Evaluates data and routes profiles accordingly | Holds profiles at a specific point before continuing |
| **Use case** | Segment customers, check status, branch based on behavior | Timing between messages, waiting for business hours, creating delays |
| **Example** | If customer is VIP, send premium offer; otherwise send standard offer | Wait 3 days after welcome email before sending next message |

**They work together**:

* Wait for a period, then use a Condition to check if something happened during the wait
* Example: Wait 7 days, then check if customer made a purchase

Learn more about [conditions](condition-activity.md) and [wait activities](wait-activity.md).

+++

## Best practices and limitations

+++ What are the key limitations I should be aware of?

Important guardrails include:

* **Journey complexity**: Maximum activities, paths, and nesting levels
* **Throughput**: Message sending rates and API call limits
* **Time-to-live**: Maximum journey duration (e.g., 91 days)
* **Audience size**: Limits on read audience batch sizes
* **Expression complexity**: Character limits in conditions and personalization

View complete [guardrails and limitations](../start/guardrails.md).

+++

+++ What are best practices for journey design?

**Structure and organization**:

* Keep journeys focused on specific use cases
* Use descriptive naming for activities
* Add descriptions and labels for complex logic
* Group related journeys with tags

**Performance**:

* Optimize wait times to balance engagement and volume
* Limit external API calls to essential use cases
* Use capping rules to prevent message fatigue
* Monitor journey metrics regularly

**Testing**:

* Always test journeys before publishing
* Use test mode to validate journey logic and step through the journey
* Use dry run mode to test with real production data without contacting customers
* Test all conditional paths and scenarios
* Use realistic test profiles
* Validate personalization and dynamic content

**Maintenance**:

* Regularly review journey performance
* Stop or close unused journeys
* Document journey logic and business rules
* Plan for journey versioning

Learn more about [journey design best practices](using-the-journey-designer.md).

+++

+++ How many activities can I add to a journey?

Journeys are limited to a maximum of 50 activities. However, we recommend keeping your journeys simpler for better maintainability and performance.

As journeys approach 50 activities, they can become very complex and difficult to maintain, troubleshoot, and understand. Large journeys with many branches and conditions may also impact processing time, readability, and team collaboration.

**Best practice**: Keep your journeys focused and manageable. If your journey is becoming complex, consider:

* Breaking it into multiple journeys using the Jump activity
* Creating reusable patterns across simpler journeys
* Simplifying logic with more efficient conditions
* Reviewing if all activities are necessary

Learn more about [journey design](using-the-journey-designer.md) and [guardrails and limitations](../start/guardrails.md).

+++

+++ How do I ensure my journey performs well at scale?

**Design considerations**:

* Use [audience-based entry](read-audience.md) for batch communications instead of individual events
* Implement appropriate [wait times](wait-activity.md) to spread message volume
* Leverage [capping rules](../conflict-prioritization/journey-capping.md) to prevent system overload
* Optimize [condition logic](condition-activity.md) to reduce processing complexity

**Monitoring**:

* Track [journey metrics](report-journey.md) regularly
* Monitor API performance for [custom actions](using-custom-actions.md)
* Review error rates and timeout occurrences using [troubleshooting tools](troubleshooting.md)
* Subscribe to [journey alerts](../reports/alerts.md) critical journey failures

**Optimization**:

* Use [test mode](testing-the-journey.md) and [dry run](journey-dry-run.md) to validate performance before publishing
* Minimize external API calls through [custom actions](using-custom-actions.md) to avoid latency and dependency on third-party systems
* Store frequently used data in Adobe Experience Platform using [dataset lookup](dataset-lookup.md) instead of doing external calls, when possible
* Review and optimize [message delivery](journeys-message.md) performance

Learn more about [guardrails and limitations](../start/guardrails.md).

+++

## Additional Resources

For more learning and updates, explore the following resources:

* [Get started with journeys](journey.md)
* [Create your first journey](journey-gs.md)
* [Troubleshooting guides](troubleshooting.md)
* [Journey use cases](jo-use-cases.md)
* [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"}
