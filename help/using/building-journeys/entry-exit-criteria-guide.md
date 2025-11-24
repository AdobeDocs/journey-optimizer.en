---
solution: Journey Optimizer
product: journey optimizer
title: Journey entry and exit criteria guide
description: Learn how to effectively manage when profiles enter and exit journeys with real-world examples and best practices
feature: Journeys, Profiles
role: User
level: Intermediate
keywords: entry, exit, criteria, journey, profile, reentrance, best practices
version: Journey Orchestration
---

# Mastering journey entry and exit criteria {#entry-exit-criteria-guide}

In customer experience orchestration, delivering the right message at the right time requires precise control over when customers enter and exit your journeys. Understanding and properly configuring entry and exit criteria can make the difference between a successful, engaging campaign and missed opportunities or message fatigue.

This guide provides practical guidance, real-world examples, and best practices for managing journey entry and exit criteria in Adobe Journey Optimizer.

## What are entry and exit criteria? {#what-are-criteria}

**Entry criteria** determine the conditions under which a [customer profile](../audience/get-started-profiles.md) qualifies to enter a specific journey. This can be based on:

* Customer behavior (e.g., making a purchase, abandoning a cart) - [Configure events](../event/about-events.md)
* [Profile attributes](../audience/get-started-profiles.md) (e.g., loyalty tier, location, preferences)
* External events (e.g., inventory low, weather conditions) - [Business events](../event/about-creating-business.md)
* [Audience membership](../audience/about-audiences.md) (e.g., qualifying for a segment)

**Exit criteria** define when and how a profile leaves or is removed from a journey. This includes:

* Journey completion (reaching the end of the path) - [Learn about journey ending](end-journey.md)
* Goal achievement (e.g., making a purchase) - [Set up success metrics](success-metrics.md)
* Specific conditions met (e.g., inactivity over a set period) - [Use conditions](condition-activity.md)
* Event occurrence (e.g., subscription cancellation) - [Configure events](../event/about-events.md)
* Audience disqualification - [About audiences](../audience/about-audiences.md)

## Why entry and exit criteria matter {#why-they-matter}

Properly defining entry and exit criteria delivers significant business value:

* **Relevance**: Only the right customers enter the journey, increasing engagement and conversion rates by targeting the most appropriate audience at the optimal time.

* **Efficiency**: Prevents customers from staying in irrelevant journeys, reducing unnecessary communications, operational costs, and customer annoyance.

* **Personalization**: Enables dynamic tailoring of experiences based on real-time data and behavior, creating more meaningful customer interactions.

* **Compliance**: Helps manage frequency capping and avoid over-communication, respecting customer preferences and regulatory requirements while maintaining brand reputation.

* **Resource optimization**: Ensures your marketing resources and system capacity are focused on the profiles most likely to engage and convert.

## Real-world use cases {#real-world-use-cases}

### Welcome campaign for new subscribers {#welcome-campaign}

Create a personalized onboarding experience for new subscribers that adapts based on engagement.

**Entry criteria:**

* **Trigger**: Profile subscribes to newsletter (event-based)
* **Journey type**: Unitary event journey
* **Additional filters**: None - welcome all new subscribers

**Journey flow:**

1. Immediate [welcome email](../email/create-email.md) with introduction and brand story
1. [Wait 2 days](wait-activity.md)
1. Getting started guide with product tutorials
1. [Wait 3 days](wait-activity.md)
1. [Condition](condition-activity.md): Has customer made a purchase?
   * Yes → Exit journey or [transition to customer engagement journey](jump.md)
   * No → Continue with special offer
1. Send first-time buyer discount
1. [Wait 5 days](wait-activity.md)
1. Best-sellers and popular content email

**Exit criteria:**

* Customer completes first purchase (event-based exit)
* Customer unsubscribes (event-based exit)
* 21 days elapsed with no engagement (timeout)

**Re-entrance settings:**

* Disabled - each subscriber should receive the welcome series only once

**Business benefit:** Ensures new subscribers receive timely onboarding content while avoiding repetitive messaging. Exits early when the goal (first purchase) is achieved, preventing message fatigue.

>[!MORELIKETHIS]
>
>
>* [Configure event-based entry](entry-management.md#entry-unitary) - Learn how to set up unitary and audience qualification journeys with re-entrance controls.
>* [Set up exit criteria](journey-properties.md#exit-criteria) - Define when profiles should automatically leave your journey based on events or audience membership.
>* [Design email content](../email/get-started-email-design.md) - Create engaging email messages using the Email Designer with drag-and-drop components.
>* [Personalize email content](../personalization/personalize.md) - Add dynamic content and personalization tokens to customize messages for each recipient.
>* [Welcome campaign video tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/customer-onboarding) - Watch a step-by-step video showing how to build an effective customer onboarding journey.

### Abandoned cart recovery {#abandoned-cart}

Recover potentially lost sales by reminding customers about items left in their cart.

**Entry criteria:**

* **Trigger**: Items added to cart but no checkout completed within 2 hours (event-based)
* **Journey type**: Unitary event journey
* **Attribute filter**: Cart value > $20 (avoid sending reminders for very low-value carts)

**Journey flow:**

1. [Wait 2 hours](wait-activity.md) after cart abandonment
1. [Email 1](../email/create-email.md): Friendly reminder with [personalized cart contents](../personalization/personalize.md)
1. [Reaction event](reaction-events.md): Wait for purchase (timeout: 24 hours)
   * Purchase made → Exit journey
   * Timeout → Continue
1. [Email 2](../email/create-email.md): Reminder with 10% discount code
1. [Reaction event](reaction-events.md): Wait for purchase (timeout: 48 hours)
   * Purchase made → Exit journey
   * Timeout → End journey

**Exit criteria:**

* Purchase completed (event-based exit) - automatically triggered when checkout event is received
* Cart cleared by customer (event-based exit)
* 7 days elapsed since initial abandonment (timeout)

**Re-entrance settings:**

* Enabled with supplemental identifier (cart session ID)
* Allows same profile to enter for different cart sessions
* Re-entrance wait period: 12 hours

**Business benefit:** Drives conversions through timely reminders without spamming customers who aren't interested. Supplemental identifiers allow the same customer to receive reminders for multiple abandoned carts while preventing duplicate messages for the same cart.

>[!MORELIKETHIS]
>
>
>* [Abandoned cart video tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/use-cases/abandoned-cart) - Watch how to build a complete abandoned cart recovery journey using playbooks.
>* [Configure supplemental identifiers](supplemental-identifier.md) - Enable profiles to enter journeys multiple times for different transactions (e.g., different cart sessions).
>* [Use reaction events](reaction-events.md) - Track customer interactions with messages and create conditional paths based on opens, clicks, or timeouts.
>* [Email design and personalization](../email/get-started-email-design.md) - Build beautiful, responsive emails with product recommendations and cart contents.
>* [Create dynamic content](../personalization/get-started-dynamic-content.md) - Display different content variations based on profile attributes or context.

### Loyalty program engagement {#loyalty-program}

Keep high-value customers engaged with personalized rewards and offers.

**Entry criteria:**

* **Trigger**: Profile reaches Gold tier (1,000 points) in loyalty program
* **Journey type**: Audience qualification journey
* **Audience definition**: Loyalty tier = Gold AND active in last 30 days

**Journey flow:**

1. Congratulations [email](../email/create-email.md) on reaching Gold tier
1. [Wait 7 days](wait-activity.md)
1. Exclusive Gold member [offer](../offers/get-started/starting-offer-decisioning.md)
1. [Wait 14 days](wait-activity.md)
1. [Condition](condition-activity.md): Redeemed offer?
   * Yes → Thank you message and additional rewards
   * No → Reminder email with extended deadline
1. [Wait 30 days](wait-activity.md)
1. Monthly Gold member newsletter

**Exit criteria:**

* Loyalty points drop below Gold threshold (audience disqualification)
* 60 days of inactivity (no purchases or engagement)
* Profile opts out of loyalty communications (event-based)

**Re-entrance settings:**

* Enabled - profiles can re-enter if they drop below Gold tier and then qualify again
* Re-entrance wait period: 30 days

**Business benefit:** Keeps high-value customers engaged with personalized offers while automatically removing inactive members, ensuring communications remain relevant and valued. Avoids communication fatigue through appropriate wait periods and exit criteria.

>[!MORELIKETHIS]
>
>
>* [Audience qualification journeys](audience-qualification-events.md) - Trigger journeys in real-time when profiles join or leave specific audiences.
>* [Exit criteria based on audiences](journey-properties.md#exit-criteria) - Automatically remove profiles when they no longer meet your target audience criteria.
>* [Create and manage audiences](../audience/about-audiences.md) - Build streaming and batch audiences using profile attributes and behaviors.
>* [Work with offers](../offers/offer-library/creating-personalized-offers.md) - Create personalized offers with eligibility rules and content for different customer segments.

### Product feedback collection {#feedback-collection}

Gather valuable customer feedback at the optimal time after product delivery.

**Entry criteria:**

* **Trigger**: Product delivery confirmation event received
* **Journey type**: Event-triggered journey
* **Attribute filters**: Order status = "Delivered" AND order value > $50

**Journey flow:**

1. [Wait 3 days](wait-activity.md) after delivery (gives customer time to use product)
1. [SMS](../sms/create-sms.md) or [email](../email/create-email.md): "How's your [Product Name](../personalization/personalize.md)? Share your thoughts!"
1. [In-app](../in-app/create-in-app.md) or email feedback form
1. [Reaction event](reaction-events.md): Wait for feedback submission (timeout: 7 days)
   * Feedback submitted → Thank you message with loyalty points
   * Timeout → Single reminder
1. [Wait 3 days](wait-activity.md)
1. Final reminder (only if no feedback received)

**Exit criteria:**

* Feedback submitted (event-based exit)
* 10 days elapsed since initial request (timeout)
* Product returned (event-based exit - no need for feedback on returned items)

**Re-entrance settings:**

* Enabled with supplemental identifier (order ID)
* Allows feedback requests for each order
* No re-entrance wait period needed (different orders)

**Business benefit:** Captures valuable feedback promptly without annoying customers with persistent requests. Using supplemental identifiers ensures customers receive appropriate feedback requests for each order without duplication.

>[!MORELIKETHIS]
>
>
>* [Supplemental identifiers for order-level journeys](supplemental-identifier.md) - Allow feedback requests for each order while preventing duplicate messages for the same order.
>* [SMS channel configuration](../sms/create-sms.md) - Set up SMS messages with short, actionable content and personalized links.
>* [In-app messaging](../in-app/get-started-in-app.md) - Display feedback forms directly within your mobile app or website.
>* [Multi-channel journeys](journeys-message.md) - Combine email, SMS, push, and in-app messages in a single customer journey.

### Time-sensitive promotions {#time-sensitive-promo}

Drive urgency with flash sales and limited-time offers.

**Entry criteria:**

* **Trigger**: Read audience activity on scheduled basis
* **Journey type**: Read audience journey (batch)
* **Audience**: High-intent customers (viewed products 3+ times, no purchase in last 7 days)
* **Schedule**: One-time execution

**Journey flow:**

1. [Email](../email/create-email.md): "24-Hour Flash Sale on Items You Love!"
1. [Wait 6 hours](wait-activity.md)
1. [Condition](condition-activity.md): Made purchase?
   * Yes → Exit
   * No → Continue
1. [Push notification](../push/create-push.md): "Only 18 hours left!"
1. [Wait 12 hours](wait-activity.md)
1. [Condition](condition-activity.md): Made purchase?
   * Yes → Exit
   * No → Continue
1. Final reminder: "Last 6 hours!"

**Exit criteria:**

* Purchase made (event-based exit)
* Sale end time reached (24 hours from start)
* Profile opts out during journey

**Re-entrance settings:**

* Disabled for this journey (one-time flash sale)
* Future flash sales would use new journey instances

**Business benefit:** Creates urgency and drives immediate action while respecting customers who have already converted by immediately removing them from reminder communications.

>[!MORELIKETHIS]
>
>
>* [Read audience journeys](read-audience.md) - Target specific audiences with one-time or recurring scheduled campaigns.
>* [Schedule journeys](journey-properties.md#schedule) - Set exact dates, times, and frequencies for when your journey should run.
>* [Push notifications](../push/get-started-push.md) - Send urgent, attention-grabbing messages directly to mobile devices.
>* [Create urgency with countdown timers](../personalization/personalization-use-case.md) - Add dynamic countdown timers to show time remaining in your offers.

### Re-engagement campaign {#re-engagement}

Win back customers who have become inactive with personalized incentives.

**Entry criteria:**

* **Trigger**: Scheduled read audience (weekly)
* **Journey type**: Recurring read audience journey
* **Audience**: No purchase in 90 days AND previously active customer (lifetime purchases > $100)
* **Recurrence**: Weekly

**Journey flow:**

1. [Email](../email/create-email.md): "We miss you! Here's what's new"
1. [Wait 5 days](wait-activity.md)
1. [Condition](condition-activity.md): Visited website?
   * Yes → Continue with [product recommendations](../offers/offer-library/add-representations.md)
   * No → Continue with stronger incentive
1. [Email](../email/create-email.md): 15% off "Welcome back" offer
1. [Wait 7 days](wait-activity.md)
1. [Condition](condition-activity.md): Made purchase?
   * Yes → Exit and move to [active customer journey](jump.md)
   * No → End journey

**Exit criteria:**

* Purchase made (event-based exit)
* Profile qualifies as "active customer" audience (made purchase)
* Explicitly opts out of promotional emails
* 30 days elapsed since journey start

**Re-entrance settings:**

* Enabled - customers can re-enter if they become inactive again
* Re-entrance wait period: 90 days
* Must finish current journey before re-entering

**Business benefit:** Systematically identifies and re-engages lapsed customers while avoiding messaging customers who have already returned to activity. Regular recurrence ensures no inactive customers fall through the cracks.

>[!MORELIKETHIS]
>
>
>* [Recurring read audience journeys](read-audience.md#read-audience-options) - Set up weekly, monthly, or custom recurring campaigns that automatically target your audience.
>* [Re-entrance rules](entry-management.md#entry-read-audience) - Control how often profiles can re-enter journeys to prevent message fatigue.
>* [Jump to another journey](jump.md) - Transfer active customers to different journeys based on their behavior or status.
>* [Create re-engagement audiences](../audience/creating-a-segment-definition.md) - Define audiences based on inactivity periods and past purchase behavior.

## Configuring entry criteria {#configure-entry}

Adobe Journey Optimizer offers multiple ways to define entry criteria:

### Event-based triggers {#event-triggers}

Use events like "profile creation," "transaction completed," or custom events to kick off a journey in real-time.

**Best for:** Real-time, individual customer actions requiring immediate response (e.g., order confirmation, account creation, cart abandonment).

**Configuration:**
1. [Configure your event](../event/about-creating.md) in the Administration menu
1. Define [event schema and fields](../event/experience-event-schema.md)
1. Add event as first activity in [journey designer](using-the-journey-designer.md)
1. Set [timeout](general-events.md) and [wait conditions](wait-activity.md) as needed

**Related documentation:**
* [About events](../event/about-events.md)
* [Event creation steps](../event/about-creating.md)
* [Work with schemas](../data/get-started-schemas.md)

### Audience-based entry {#audience-entry}

Target journeys to profiles who belong to specific audiences, either as a one-time batch or on a recurring schedule.

**Best for:** Scheduled campaigns, batch communications, segment-based targeting (e.g., monthly newsletters, seasonal promotions).

**Configuration:**
1. [Create or select audience](../audience/creating-a-segment-definition.md) in Audiences menu
1. Add [Read Audience activity](read-audience.md) as first step
1. [Configure schedule](journey-properties.md#schedule) (one-time or recurring)
1. Set [recurrence rules](read-audience.md#read-audience-options) if needed

**Related documentation:**
* [Read audience journeys](read-audience.md)
* [Create audiences](../audience/creating-a-segment-definition.md)
* [About audience composition](../audience/get-started-audience-orchestration.md)

### Audience qualification entry {#qualification-entry}

Trigger journeys when profiles qualify for or exit from specific audiences in real-time.

**Best for:** Dynamic audience changes requiring immediate response (e.g., loyalty tier changes, risk scoring, behavioral segments).

**Configuration:**
1. Define [streaming audience](../audience/about-audiences.md) with qualification criteria
1. Add [Audience Qualification event](audience-qualification-events.md) as first activity
1. Choose to trigger on entry, exit, or both
1. Set [re-entrance rules](entry-management.md#entry-unitary)

**Related documentation:**
* [Audience qualification events](audience-qualification-events.md)
* [Streaming segmentation](../audience/about-audiences.md)
* [Build audience rules](../audience/creating-a-segment-definition.md)

### Attribute filters and combined conditions {#attribute-filters}

Refine entry criteria by combining events or audiences with profile attributes and context.

**Best for:** Precise targeting based on multiple factors (e.g., VIP customers in specific regions, high-value carts).

**Configuration:**
1. Start with event or audience entry
1. Add [conditions](condition-activity.md) using journey conditions
1. Use [AND/OR logic](conditions.md) for complex rules
1. Reference [profile attributes](../audience/get-started-profiles.md), event data, or [external data sources](../datasource/about-data-sources.md)

**Related documentation:**
* [Condition activity](condition-activity.md)
* [Build conditions](conditions.md)
* [Use the expression editor](expression/expressionadvanced.md)
* [Data sources](../datasource/about-data-sources.md)

### Time windows and scheduling {#time-windows}

Set temporal constraints to keep journeys timely and relevant.

**Best for:** Time-bound campaigns, business hours restrictions, seasonal promotions.

**Configuration:**
1. Set [schedule on Read Audience activity](read-audience.md)
1. Use [Wait activities](wait-activity.md) for time-based progression
1. Add [time-based conditions](conditions.md) (e.g., "current day is weekday")
1. Set journey start and end dates in [properties](journey-properties.md)

**Related documentation:**
* [Journey scheduling](journey-properties.md#schedule)
* [Wait activity](wait-activity.md)
* [Timezone management](timezone-management.md)
* [Weekday email use case](weekday-email-uc.md)

## Configuring exit criteria {#configure-exit}

Exit criteria ensure profiles leave journeys at the appropriate time:

### Journey completion {#journey-completion}

Profiles automatically exit when they reach the end of all paths in the journey.

**Best for:** Linear journeys with clear endpoints, journeys with defined steps.

**Configuration:** Design journey paths to end at End tags - no additional configuration needed.

[Learn more about journey ending](end-journey.md)

### Goal achievement {#goal-achievement}

Define business goals and automatically exit profiles when goals are met.

**Best for:** Conversion-focused journeys where continuing communication after goal achievement is unnecessary.

**Configuration:**
1. Click Show Exit Criteria icon in [journey canvas](using-the-journey-designer.md)
1. Select Add exit criteria
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

**Configuration:**
1. Use [Exit Criteria](journey-properties.md#exit-criteria) with [audience](../audience/creating-a-segment-definition.md) that checks last engagement date
1. Set [Wait activity](wait-activity.md) with defined duration
1. Use [conditions](condition-activity.md) to check for activity
1. Route inactive profiles to [exit](end-journey.md)

**Typical timeout periods:**
* Feedback requests: 7-14 days
* Welcome series: 30 days
* Re-engagement: 30-60 days
* Promotional campaigns: 3-7 days

### Profile attribute-based exit {#profile-exit}

Remove profiles based on attribute changes, particularly useful in paused journeys.

**Best for:** Compliance requirements, location-based exclusions, preference changes in paused journeys.

**Configuration:**
1. [Pause the journey](journey-pause.md)
1. Click Show Exit Criteria icon
1. Select Profile Attribute as exit type
1. Define [attribute-based rule](conditions.md) (e.g., country = "France")
1. [Resume journey](journey-pause.md#journey-resume-steps) - profiles matching criteria exit at next action

**Related documentation:**
* [Profile attribute exit criteria](journey-properties.md#profile-exit-criteria)
* [Pause and resume journeys](journey-pause.md)
* [Profile attributes](../audience/get-started-profiles.md)

### Re-entry rules {#reentry-rules}

Control whether and when profiles can re-enter journeys.

**Best for:** Balancing message persistence with avoiding fatigue, supporting different use cases per journey type.

**Configuration options:**
* **Allow re-entrance**: Enable profiles to enter multiple times after fully exiting
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
* Assign [priority scores](../conflict-prioritization/priority-scores.md) in journey properties (0-100)
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
* Use [test mode](testing-the-journey.md) to validate entry and exit criteria
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

