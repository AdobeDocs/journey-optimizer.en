---
solution: Journey Optimizer
product: journey optimizer
title: Journey entry and exit criteria
description: Learn how to effectively manage when profiles enter and exit journeys with real-world examples and best practices
feature: Journeys, Profiles
role: User
level: Intermediate
keywords: entry, exit, criteria, journey, profile, reentrance, best practices
version: Journey Orchestration
---

# Work with journey entry and exit criteria {#entry-exit-criteria-guide}

In customer experience orchestration, delivering the right message at the right time requires precise control over when customers enter and exit your journeys. Understanding and properly configuring entry and exit criteria can make the difference between a successful, engaging campaign and missed opportunities or message fatigue.

This guide provides practical guidance, real-world examples, and best practices for managing journey entry and exit criteria in Adobe Journey Optimizer.

## What are entry and exit criteria? {#what-are-criteria}

**Entry criteria** determine the conditions under which a [customer profile](../audience/get-started-profiles.md) qualifies to enter a specific journey.

| Entry type | Description | Examples |
|------------|-------------|----------|
| [Customer behavior](../event/about-events.md) | Actions taken by customers trigger journey entry | Making a purchase, abandoning a cart, opening an app |
| [Profile attributes](../audience/get-started-profiles.md) | Customer characteristics determine eligibility | Loyalty tier, location, age, preferences |
| [External events](../event/about-creating-business.md) | Business or environmental triggers | Inventory low, weather conditions, price changes |
| [Audience membership](../audience/about-audiences.md) | Belonging to a specific audience segment | High-value customers, inactive users, new subscribers |

**Exit criteria** define when and how a profile leaves or is removed from a journey.

| Exit type | Description | Documentation |
|-----------|-------------|---------------|
| Journey completion | Profile reaches the end of all journey paths | [Learn about journey ending](end-journey.md) |
| Goal achievement | Profile completes the journey objective (e.g., makes a purchase) | [Set up success metrics](success-metrics.md) |
| Condition-based | Specific conditions met (e.g., inactivity over a set period) | [Use conditions](condition-activity.md) |
| Event-based | Specific event occurs (e.g., subscription cancellation) | [Configure events](../event/about-events.md) |
| Audience disqualification | Profile no longer meets audience criteria | [About audiences](../audience/about-audiences.md) |

## Why entry and exit criteria matter {#why-they-matter}

Properly defining entry and exit criteria delivers significant business value:

* **Relevance**: Only the right customers enter the journey, increasing engagement and conversion rates by targeting the most appropriate audience at the optimal time.

* **Efficiency**: Prevents customers from staying in irrelevant journeys, reducing unnecessary communications, operational costs, and customer annoyance.

* **Personalization**: Enables dynamic tailoring of experiences based on real-time data and behavior, creating more meaningful customer interactions.

* **Compliance**: Helps manage frequency capping and avoid over-communication, respecting customer preferences and regulatory requirements while maintaining brand reputation.

* **Resource optimization**: Ensures your marketing resources and system capacity are focused on the profiles most likely to engage and convert.

## Learn through documented use cases {#real-world-use-cases}

The following documented use cases demonstrate how to apply entry and exit criteria in real journey scenarios. Each includes complete implementation guidance and configuration steps.

### Customer onboarding journey {#customer-onboarding}

Build a personalized welcome experience for new customers that adapts based on their engagement and actions.

![Example of exit criteria configuration in journey properties](assets/add-exit-criteria.png){width="50%" align="left"}

**Key concepts demonstrated:**

Event-based journey entry * Exit criteria based on goal achievement * Re-entrance controls * Time-based progression * Conditional paths

**Implementation resources:**

| Resource | Description |
|----------|-------------|
| [Video tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/customer-onboarding) | Complete step-by-step walkthrough |
| [Event-based entry](entry-management.md#entry-unitary) | Set up unitary journey entry |
| [Exit criteria](journey-properties.md#exit-criteria) | Define goal-based exits using **[!UICONTROL Exit criteria]** button |
| [Conditions](condition-activity.md) | Create conditional paths with **[!UICONTROL Condition]** activity |
| [Email design](../email/get-started-email-design.md) | Build welcome messages |

### Abandoned cart recovery {#abandoned-cart}

Recover potentially lost sales by reminding customers about items left in their cart with timely, personalized messages.

![Configuring supplemental identifier in journey properties for cart sessions](assets/supplemental-ID-journey.png){width="50%" align="left"}

**Key concepts demonstrated:**

Event-triggered entry * Event-based exit * Supplemental identifiers * Re-entrance controls * Conditional logic

**Implementation resources:**

| Resource | Description |
|----------|-------------|
| [Video tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/abandoned-cart) | Build complete journey using playbooks |
| [Supplemental identifiers](supplemental-identifier.md) | Enable multiple cart sessions in journey **[!UICONTROL Properties]** |
| [Event-based exits](journey-properties.md#exit-criteria) | Remove converted customers using **[!UICONTROL Exit criteria]** |
| [Personalization](../personalization/personalize.md) | Show cart contents using personalization editor |
| [Conditions](condition-activity.md) | Check for purchase events with **[!UICONTROL Condition]** activity |

### Send messages to subscribers {#send-to-subscribers}

Target specific subscription lists with personalized messages using audience-based entry.

![Journey flow with Read Audience for subscriber list targeting](assets/message-to-subscribers-uc-1.png){width="50%" align="left"}

**Key concepts demonstrated:**

Read audience entry * Subscription list targeting * Email personalization * Journey completion

**Implementation resources:**

| Resource | Description |
|----------|-------------|
| [Complete use case](message-to-subscribers-uc.md) | Step-by-step implementation guide |
| [Read Audience](read-audience.md) | Set up audience-based entry using **[!UICONTROL Read Audience]** activity |
| [Subscriptions](../audience/about-audiences.md) | Manage subscriber lists from **[!UICONTROL Audiences]** menu |
| [Map fields](expression/field-references.md) | Access subscription data in expression editor |

### Send multi-channel messages {#multi-channel-messages}

Combine email and push notifications based on customer reactions and behavior.

![Simple journey flow with Read Audience, Wait, and Email activities](assets/jo-uc1.png){width="70%" align="left"}

**Key concepts demonstrated:**

Read audience entry * Reaction events * Multi-path logic * Goal-based exits

**Implementation resources:**

| Resource | Description |
|----------|-------------|
| [Complete use case](journeys-uc.md) | Full implementation guide |
| [Reaction events](reaction-events.md) | Track interactions after **[!UICONTROL Email]** or **[!UICONTROL Push]** actions |
| [Multi-channel actions](journeys-message.md) | Combine channels from **[!UICONTROL Actions]** palette |
| [Exit criteria](journey-properties.md#exit-criteria) | Define completion conditions using **[!UICONTROL Exit criteria]** |

### Send emails only on weekdays {#weekday-emails}

Schedule email delivery to occur only on business days, with automatic queuing for weekend entries.

![Journey with three condition paths - Saturday, Sunday, and Weekdays](assets/weekday-email-uc-paths.png){width="70%" align="left"}

**Key concepts demonstrated:**

Time-based conditions * Wait formulas * Timezone management * Scheduling logic

**Implementation resources:**

| Resource | Description |
|----------|-------------|
| [Complete use case](weekday-email-uc.md) | Detailed implementation guide |
| [Time conditions](condition-activity.md#time-condition) | Filter by day of week using **[!UICONTROL Time condition]** |
| [Wait activities](wait-activity.md) | Delay until specific time with **[!UICONTROL Wait]** activity |
| [Timezone management](timezone-management.md) | Handle global audiences in journey **[!UICONTROL Properties]** |

### Re-engagement campaigns {#re-engagement}

Win back inactive customers with personalized incentives and relevant content.

![Configuring re-entrance settings in journey properties](assets/journey-re-entrance.png){width="50%" align="left"}

**Key concepts demonstrated:**

Recurring read audience * Inactivity-based targeting * Re-entrance controls * Behavioral conditions * Journey transitions

**Implementation resources:**

| Resource | Description |
|----------|-------------|
| [Video tutorial series](https://experienceleague.adobe.com/en/docs/experience-platform/rtcdp/use-cases/personalization-insights-engagement/use-cases-luma) | Complete implementation walkthrough |
| [Recurring journeys](read-audience.md#read-audience-options) | Schedule using **[!UICONTROL Scheduler]** in **[!UICONTROL Read Audience]** |
| [Re-entrance rules](entry-management.md#entry-read-audience) | Control frequency in **[!UICONTROL Properties]** > **[!UICONTROL Re-entrance]** |
| [Inactivity audiences](../audience/creating-a-segment-definition.md) | Define lapsed customers in **[!UICONTROL Audiences]** menu |
| [Jump activity](jump.md) | Transfer with **[!UICONTROL Jump]** action |

### Additional journey patterns {#additional-patterns}

Explore more specialized journey patterns and techniques.

| Pattern | Description | Key resource |
|---------|-------------|--------------|
| **Ramp up deliveries** ![Profile cap condition](assets/profile-cap-condition.png){width="200px"} | Gradually increase send volume for IP warming using profile cap conditions | [Complete use case](ramp-up-deliveries-uc.md) |
| **Work with experience events** | Patterns for using experience event data including opt-out management, frequency control, and behavioral personalization | [Explore patterns](exp-event-lookup.md) |
| **Remove profiles from live journeys** ![Profiles in paused journey](assets/profiles-in-paused-journeys.png){width="200px"} | Apply exit criteria to paused journeys to remove specific profiles | [Learn how](journey-pause.md#apply-an-exit-criteria-in-a-paused-journey) |

>[!TIP]
>
>Browse all available use cases in the [Journey use cases library](jo-use-cases.md) for more patterns and implementations.

## Configuring entry criteria {#configure-entry}

Adobe Journey Optimizer offers multiple ways to define entry criteria:

### Event-based triggers {#event-triggers}

Use events like "profile creation," "transaction completed," or custom events to kick off a journey in real-time.

**Best for:** Real-time, individual customer actions requiring immediate response (order confirmation, account creation, cart abandonment).

**Configuration steps:**

1. [Configure your event](../event/about-creating.md) in **[!UICONTROL Administration]** > **[!UICONTROL Events]**
1. Define [event schema and fields](../event/experience-event-schema.md)
1. Add event from **[!UICONTROL Events]** palette in [journey designer](using-the-journey-designer.md)
1. Set [timeout](general-events.md) and [wait conditions](wait-activity.md) as needed

Learn more: [About events](../event/about-events.md) * [Event creation](../event/about-creating.md) * [Schemas](../data/get-started-schemas.md)

### Audience-based entry {#audience-entry}

Target journeys to profiles who belong to specific audiences, either as a one-time batch or on a recurring schedule.

**Best for:** Scheduled campaigns, batch communications, segment-based targeting (monthly newsletters, seasonal promotions).

![Read Audience activity configuration with scheduling options](assets/read-segment-schedule.png){width="50%" align="left"}

**Configuration steps:**

1. [Create or select audience](../audience/creating-a-segment-definition.md) in **[!UICONTROL Audiences]** menu
1. Add [Read Audience activity](read-audience.md) from **[!UICONTROL Orchestration]** palette
1. [Configure schedule](journey-properties.md#schedule) in **[!UICONTROL Scheduler]** section
1. Set [recurrence rules](read-audience.md#read-audience-options) if needed

Learn more: [Read audience journeys](read-audience.md) * [Create audiences](../audience/creating-a-segment-definition.md) * [Audience composition](../audience/get-started-audience-orchestration.md)

### Audience qualification entry {#qualification-entry}

Trigger journeys when profiles qualify for or exit from specific audiences in real-time.

**Best for:** Dynamic audience changes requiring immediate response (loyalty tier changes, risk scoring, behavioral segments).

**Configuration steps:**

1. Define [streaming audience](../audience/about-audiences.md) in **[!UICONTROL Audiences]** menu
1. Add [Audience Qualification event](audience-qualification-events.md) from **[!UICONTROL Events]** palette
1. Choose trigger: **[!UICONTROL Entry]**, **[!UICONTROL Exit]**, or both
1. Set [re-entrance rules](entry-management.md#entry-unitary) in journey **[!UICONTROL Properties]**

Learn more: [Audience qualification events](audience-qualification-events.md) * [Streaming segmentation](../audience/about-audiences.md) * [Audience rules](../audience/creating-a-segment-definition.md)

### Attribute filters and combined conditions {#attribute-filters}

Refine entry criteria by combining events or audiences with profile attributes and context.

**Best for:** Precise targeting based on multiple factors (VIP customers in specific regions, high-value carts).

![Condition activity configuration with expression editor](assets/journey-condition.png){width="70%" align="left"}

**Configuration steps:**

1. Start with event or audience entry
1. Add [conditions](condition-activity.md) from **[!UICONTROL Orchestration]** > **[!UICONTROL Condition]**
1. Use [AND/OR logic](conditions.md) in expression editor
1. Reference [profile attributes](../audience/get-started-profiles.md), events, or [external data](../datasource/about-data-sources.md)

Learn more: [Condition activity](condition-activity.md) * [Build conditions](conditions.md) * [Expression editor](expression/expressionadvanced.md) * [Data sources](../datasource/about-data-sources.md)

### Time windows and scheduling {#time-windows}

Set temporal constraints to keep journeys timely and relevant.

**Best for:** Time-bound campaigns, business hours restrictions, seasonal promotions.

**Configuration steps:**

1. Set [schedule on Read Audience activity](read-audience.md) using **[!UICONTROL Scheduler]** section
1. Use [Wait activities](wait-activity.md) from **[!UICONTROL Orchestration]** palette
1. Add [time-based conditions](conditions.md) using **[!UICONTROL Time condition]**
1. Set journey dates in **[!UICONTROL Properties]** > **[!UICONTROL Schedule]**

Learn more: [Journey scheduling](journey-properties.md#schedule) * [Wait activity](wait-activity.md) * [Timezone management](timezone-management.md) * [Weekday email use case](weekday-email-uc.md)

## Configuring exit criteria {#configure-exit}

Exit criteria ensure profiles leave journeys at the appropriate time:

### Journey completion {#journey-completion}

Profiles automatically exit when they reach the end of all paths in the journey.

**Best for:** Linear journeys with clear endpoints, journeys with defined steps.

**Configuration:** Design journey paths to end at **[!UICONTROL End]** activities - no additional configuration needed.

[Learn more about journey ending](end-journey.md)

### Goal achievement {#goal-achievement}

Define business goals and automatically exit profiles when goals are met.

**Best for:** Conversion-focused journeys where continuing communication after goal achievement is unnecessary.

![Exit criteria configuration panel showing event-based exit options](assets/exitcriteria-sample.png){width="70%" align="left"}

**Configuration steps:**

1. Click **[!UICONTROL Show exit criteria]** icon in [journey canvas](using-the-journey-designer.md)
1. Select **[!UICONTROL Add exit criteria]**
1. Choose [Event](../event/about-events.md) or [Audience](../audience/about-audiences.md) as exit trigger
1. Define the goal event (e.g., Purchase Completed)
1. Label the exit criteria clearly using [tags](tags.md)

**Example events for exit:**
* Purchase completed
* Subscription upgraded
* Form submitted
* App downloaded
* Contract signed

[Learn more about exit criteria configuration](journey-properties.md#exit-criteria)

### Inactivity timeouts {#inactivity-timeouts}

Exit profiles if no engagement occurs within a set timeframe.

**Best for:** Nurture campaigns, feedback requests, time-sensitive offers where lack of response indicates disinterest.

**Configuration steps:**

1. Use [Exit Criteria](journey-properties.md#exit-criteria) with [audience](../audience/creating-a-segment-definition.md) that checks last engagement date via **[!UICONTROL Add exit criteria]**
1. Set [Wait activity](wait-activity.md) with defined duration
1. Use [conditions](condition-activity.md) to check for activity using **[!UICONTROL Condition]** activity
1. Route inactive profiles to **[!UICONTROL End]** activity

**Typical timeout periods:**
* Feedback requests: 7-14 days
* Welcome series: 30 days
* Re-engagement: 30-60 days
* Promotional campaigns: 3-7 days

### Profile attribute-based exit {#profile-exit}

Remove profiles based on attribute changes, particularly useful in paused journeys.

**Best for:** Compliance requirements, location-based exclusions, preference changes in paused journeys.

**Configuration steps:**

1. [Pause the journey](journey-pause.md) using **[!UICONTROL Pause]** button
1. Click **[!UICONTROL Show exit criteria]** icon
1. Select **[!UICONTROL Profile Attribute]** as exit type
1. Define [attribute-based rule](conditions.md) (e.g., country = "France")
1. [Resume journey](journey-pause.md#journey-resume-steps) - profiles matching criteria exit at next action

Learn more: [Profile attribute exit criteria](journey-properties.md#profile-exit-criteria) * [Pause and resume journeys](journey-pause.md) * [Profile attributes](../audience/get-started-profiles.md)

### Re-entry rules {#reentry-rules}

Control whether and when profiles can re-enter journeys.

**Best for:** Balancing message persistence with avoiding fatigue, supporting different use cases per journey type.

**Configuration options:**
* **Allow re-entrance**: Enable profiles to enter multiple times after fully exiting (configured in journey **[!UICONTROL Properties]** > **[!UICONTROL Re-entrance]**)
* **Re-entrance wait period**: Set minimum time between entries (5 minutes to [91 days global timeout](journey-properties.md#global_timeout))
* **Force re-entrance on event**: Start new instance even if profile still in journey
* **Block re-entrance**: Prevent any repeat entries (one-time journeys)
* **Supplemental identifiers**: Allow re-entry for different entities (e.g., different orders)

>[!MORELIKETHIS]
>
>
>* [Re-entrance management](entry-management.md) - Configure wait periods and rules for when profiles can re-enter completed journeys.
>* [Supplemental identifiers](supplemental-identifier.md) - Enable context-specific re-entrance for transactional journeys (orders, bookings, sessions).
>* [Journey global timeout](journey-properties.md#global_timeout) - Understand the 91-day maximum duration and what happens when journeys reach timeout.

## Best practices {#best-practices}

### Planning and documentation {#planning-docs}

**Clear definition and mapping**
* Document your entry and exit logic before building in a shared document
* Create flowcharts showing entry points, journey paths, and exit conditions
* Define business rules clearly: "Profiles exit when X happens OR after Y days"
* Include timeout values and re-entrance rules in documentation

**Team alignment**
* Share journey logic with marketing, analytics, and IT teams before launch
* Ensure analytics team can track entry, exit, and conversion metrics
* Align on naming conventions for journeys, events, and criteria
* Review complex journeys in cross-functional meetings

**Clear naming conventions**
* Use descriptive labels: "Exit - Purchase Completed" not "Exit 1"
* Include trigger type in names: "Entry Event - Cart Abandon" or "Entry Audience - Gold Tier"
* [Version journey names](publish-journey.md#journey-versions) when updating: "Welcome Series v2.0"
* [Tag journeys](tags.md) consistently for reporting and filtering

### Avoiding conflicts and overlaps {#avoiding-conflicts}

**Prevent overlapping journeys**
* [Audit active journeys](journey-ui.md) before launching similar ones
* Use exit criteria to remove profiles when they enter higher-priority journeys
* Leverage [conflict management](journey-properties.md#conflict) and [priority scores](../conflict-prioritization/priority-scores.md)
* Design journeys that complement rather than compete

**Example conflict resolution:**
* Profile enters promotional journey → Automatically exit from nurture journey
* Profile in loyalty upgrade journey → Block entry to general loyalty journey
* Holiday campaign active → Pause weekly newsletter journeys

**Use journey prioritization**
* Assign [priority scores](../conflict-prioritization/priority-scores.md) in journey **[!UICONTROL Properties]** > **[!UICONTROL Priority score]** (0-100)
* Higher priority journeys take precedence at [inbound channels](../in-app/get-started-in-app.md)
* Document priority hierarchy: Transactional > Promotional > Nurture
* Review and adjust priorities quarterly

>[!MORELIKETHIS]
>
>
>* [Conflict management](journey-properties.md#conflict) - Set up rules to prevent profiles from being in multiple conflicting journeys simultaneously.
>* [Priority scores](../conflict-prioritization/priority-scores.md) - Assign priority levels (0-100) to determine which journey takes precedence for inbound channels.
>* [View conflicts](../conflict-prioritization/conflicts.md) - Identify potential overlaps between journeys before launching to avoid message fatigue.

**Coordinate with frequency capping**
* Set global frequency caps in addition to journey-level controls
* Configure exit criteria to support frequency limits
* Use capping rules to prevent over-communication across journeys
* Monitor frequency metrics in reporting

[Learn more about frequency capping](../conflict-prioritization/rule-sets.md)

### Optimization and monitoring {#optimization}

**Monitor performance metrics**
* Track entry rate, exit rate, and completion rate for each journey
* Monitor [goal achievement](success-metrics.md): percentage exiting via goal vs. timeout
* Analyze time-to-conversion for profiles in journey
* Review re-entrance patterns and frequency using [journey reports](../reports/journey-global-report.md)

**Key metrics to track:**
* Profiles entered / Eligible profiles (entry rate)
* Profiles exited via goal / Total exits (success rate)
* Average time in journey
* Exit reasons breakdown
* Re-entrance rate and frequency

**A/B test entry and exit criteria**
* Test different entry timing: Immediate vs. 24-hour delay
* Compare audience filters: Broad vs. narrow targeting
* Experiment with exit timing: When to stop nurturing
* Test re-entrance wait periods: 7 days vs. 30 days using [Optimize activity](optimize.md)

**Adjust based on data**
* If high early exits → Review relevance of entry criteria
* If low goal achievement → Analyze journey content and timing
* If high re-entrance with no conversion → Increase wait period or improve targeting
* If low engagement → Tighten entry criteria to more qualified audience

**Regular audits**
* Review all [active journeys](journey-ui.md) quarterly
* [Archive or close outdated journeys](end-journey.md)
* Update entry/exit criteria based on business changes
* [Consolidate similar journeys](copy-to-sandbox.md) to reduce complexity
* Verify [event integrations](../event/about-events.md) are working correctly

>[!MORELIKETHIS]
>
>
>* [Journey reports](../reports/journey-global-report.md) - Analyze overall journey performance including entry rates, completion rates, and goal achievement.
>* [Live reports](../reports/journey-live-report.md) - Monitor real-time journey metrics for profiles currently in flight for immediate optimization.
>* [Query journey step events](../reports/query-examples.md) - Write custom SQL queries to analyze detailed journey execution data and profile behavior.

### Testing and validation {#testing}

**Test before launching**
* Use [test mode](testing-the-journey.md) to validate entry and exit criteria - activate with the **[!UICONTROL Test]** button
* Test with [various profile scenarios](../audience/creating-test-profiles.md): qualified, unqualified, edge cases
* Verify exit criteria trigger correctly with test events
* Check re-entrance logic with [test profiles](../audience/creating-test-profiles.md)

**Validate integrations**
* Confirm [events](../event/about-events.md) fire correctly from source systems
* Test [audience membership](../audience/about-audiences.md) updates in real-time
* Verify [custom actions](using-custom-actions.md) for exit criteria
* Check [supplemental identifier](supplemental-identifier.md) handling

>[!MORELIKETHIS]
>
>
>* [Testing journeys](testing-the-journey.md) - Use test mode to validate entry, exit, and journey logic with test profiles before going live.
>* [Journey dry run](journey-dry-run.md) - Simulate journey execution to identify configuration errors and performance issues without sending messages.
>* [Create test profiles](../audience/creating-test-profiles.md) - Build test profiles representing different customer scenarios for comprehensive journey testing.
>* [Troubleshooting](troubleshooting.md) - Resolve common journey issues including entry problems, message delivery, and performance bottlenecks.

### Common pitfalls to avoid {#common-pitfalls}

❌ **No exit criteria defined**: Profiles stay in journey unnecessarily
✅ **Solution**: Always define at least one exit criteria (goal or timeout)

❌ **Entry criteria too broad**: Irrelevant profiles enter journey
✅ **Solution**: Add attribute filters to refine audience

❌ **Exit criteria too restrictive**: Very few profiles achieve goal
✅ **Solution**: Include timeout-based exits as backup

❌ **No re-entrance controls**: Profiles bombarded with same journey
✅ **Solution**: Set appropriate re-entrance wait periods or disable re-entrance

❌ **Overlapping journeys**: Profiles in multiple competing journeys
✅ **Solution**: Use exit criteria and conflict management to prevent overlap

❌ **Not testing edge cases**: Unexpected profile behaviors cause issues
✅ **Solution**: Test thoroughly including negative and edge case scenarios

❌ **Poor documentation**: Team members can't understand journey logic
✅ **Solution**: Document all entry/exit rules and business logic clearly

## Integration with other Journey Optimizer capabilities {#integration}

Entry and exit criteria work together with other Journey Optimizer features:

**Success metrics and goals**
* Define journey goals aligned with exit criteria
* Track goal achievement as exit reason
* Measure journey ROI based on goal completion
* [Learn more about success metrics](success-metrics.md)

**Frequency capping**
* Coordinate exit criteria with global capping rules
* Use exit criteria to enforce campaign-specific limits
* Balance re-entrance rules with frequency management
* [Learn more about capping](../conflict-prioritization/rule-sets.md)

**Priority and conflict management**
* Set journey priorities in properties
* Configure exit criteria to resolve conflicts
* View potential conflicts before launching
* [Learn more about conflict management](../conflict-prioritization/conflicts.md)

**Supplemental identifiers**
* Enable context-specific re-entrance (e.g., per order, per booking)
* Configure exit criteria with supplemental IDs
* Support multiple journey instances per profile
* [Learn more about supplemental identifiers](supplemental-identifier.md)

**Experiment and optimization**
* Use Optimize activity to test different entry paths
* A/B test exit criteria timing
* Measure impact of entry/exit configurations
* [Learn more about optimization](optimize.md)

## Technical considerations {#technical-considerations}

### Processing rates and throughput {#processing-rates}

Be aware of system limits when designing entry criteria:

* **Read Audience**: Up to 20,000 profiles per second (sandbox level)
* **Unitary Events**: Up to 5,000 events per second (organization level)
* **Audience Qualification**: Up to 5,000 profiles per second (organization level)
* **Business Events**: 5,000 events per second, but Read Audience after has 20,000 TPS limit

[Learn more about processing rates](entry-management.md#journey-processing-rate)

### Exit criteria evaluation timing {#exit-timing}

* **Event-based exit**: Evaluated immediately when event received
* **Audience-based exit**: Can take up to 10 minutes to take effect
* **Profile attribute exit**: Evaluated only at action steps

[Learn more about exit criteria timing](journey-properties.md#exit-criteria-guardrails)

### Namespace coherence {#namespace}

* Entry events and event-based exit criteria must use the same [namespace](../event/selecting-the-namespace.md)
* Ensure consistent [identity management](../audience/get-started-identity.md) across journey
* Test namespace configuration thoroughly

[Learn more about namespaces and identity](../audience/get-started-identity.md)

## Related resources {#related-resources}

### Technical documentation
* [Profile entrance management](entry-management.md) - Detailed technical guide
* [Journey properties and exit criteria](journey-properties.md) - Configuration reference
* [How journeys end](end-journey.md) - Journey lifecycle management
* [Supplemental identifiers](supplemental-identifier.md) - Advanced re-entrance scenarios
* [Journey designer](using-the-journey-designer.md) - Build and design journeys
* [Journey UI](journey-ui.md) - Browse and manage journeys
* [Publish journeys](publish-journey.md) - Go live with your journeys

### Tutorials and examples
* [Journey use cases](jo-use-cases.md) - Complete journey examples
* [Customer onboarding video](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/customer-onboarding)
* [Abandoned cart video](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/abandoned-cart)
* [Community blog: Entry and Exit Criteria](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/mastering-journey-entry-and-exit-criteria-in-adobe-journey/ba-p/760958)

### Related capabilities
* [Audience qualification events](audience-qualification-events.md)
* [Success metrics and goals](success-metrics.md)
* [Conflict management](../conflict-prioritization/conflicts.md)
* [Frequency capping](../conflict-prioritization/rule-sets.md)
* [Testing journeys](testing-the-journey.md)
* [Wait activity](wait-activity.md)
* [Condition activity](condition-activity.md)
* [Reaction events](reaction-events.md)
* [Custom actions](using-custom-actions.md)
* [Update profiles](update-profiles.md)

## Need help? {#need-help}

* **Ask the community**: Join the [Adobe Journey Optimizer Community](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer/ct-p/journey-optimizer) to ask questions and share experiences
* **Watch tutorials**: Browse [Journey Optimizer video tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/overview)
* **Get support**: Contact [Adobe Customer Care](https://experienceleague.adobe.com/?support-solution=Journey+Optimizer#support) for technical assistance

