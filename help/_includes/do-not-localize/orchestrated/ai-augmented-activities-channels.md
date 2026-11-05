---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to add, configure, and send channel activities (Email, Mobile message, Push, Direct mail, Line, and Custom channel) within an Orchestrated campaign, including targeting, channel configuration, content creation, testing, sending confirmation, and rate control.

**Intents:**

* Add a channel activity (Email, Mobile message, Push, Direct mail, Line, or Custom channel) to an Orchestrated campaign canvas.
* Choose a Marketing or Transactional category for a channel activity and configure its target dimension.
* Select a channel configuration and apply rule set capping rules, content experiments, and multilingual content to a channel activity.
* Create and personalize the message content for a channel activity.
* Simulate and test channel activity content before publishing.
* Confirm or disable confirmation for message sending, and set rate control for outbound channel activities.

**Glossary:**

* **Channel activity** *(product-specific)*: an activity added to an Orchestrated campaign canvas that sends a message through a specific channel.
* **Category (Marketing or Transactional)** *(product-specific)*: field on a channel activity used to choose Marketing or Transactional handling for the message.
* **Target dimension** *(product-specific)*: the dimension selected in the Target section of a channel activity to determine the delivery target.
* **One message per profile / One message per secondary dimension** *(product-specific)*: options that determine how many messages are sent when a secondary dimension (related rows linked to a profile) applies.
* **Channel configuration** *(product-specific)*: defined by a System Administrator; contains technical sending parameters (header parameters, subdomain, mobile apps, etc.) for a channel activity.
* **Rule set** *(product-specific)*: applied to a channel activity to set capping rules such as frequency capping and quiet hours.
* **Simulate content** *(product-specific)*: tests content variations using sample input data or AI auto-generation.
* **Simulate content (AEP profiles)** *(product-specific)*: previews and tests content using test profiles.
* **Send without confirmation**: a Properties setting that disables the default pause, which by default requires explicit approval before message delivery for non-recurring Orchestrated campaigns.
* **Throttle delivery** *(product-specific)*: a Schedule tab option that enables rate control (a delivery rate per second) for Email, Mobile message, and Push channel activities.
* **Rapid delivery mode** *(product-specific)*: a Journey Optimizer add-on that enables very fast, large-volume push message sending through campaigns, used when delay in message delivery is business-critical (for example, an urgent breaking-news push alert).

**Guardrails:**

* Supported channels in Orchestrated campaigns: only Mobile message, Push, Email, and Direct mail channels are supported (hard limit). Note: the page's contextual help also describes a Line activity and a Custom channel activity for Orchestrated campaigns, so this guardrail and that description are in conflict in the source page.
* Channel activities limit: an Orchestrated campaign supports a maximum of 10 channel activities (Email, Mobile message, Push, or Direct mail) (hard limit). Only channel activities count toward this limit; targeting and flow control activities do not.
* Exceeding the channel activities limit when saving or publishing causes the operation to fail.
* Transactional messages bypass business rules and do not require opt-in.
* Simulating content with test profiles requires that execution has reached the channel activity in test: in test mode the workflow pauses at the channel activity, so a channel activity located after another channel activity is never reached, and Simulate Content cannot be used for those downstream channel activities.
* Simulating content with test profiles requires a test profile that belongs to the audience targeted by that channel activity; otherwise selecting it does not render a preview of the content.
* By default, for non-recurring Orchestrated campaigns, message delivery is paused until the send is explicitly confirmed.
* Wave sending (splitting delivery into scheduled batches before confirming) applies only to outbound channel activities (Email, Mobile, Push, or Direct mail).
* Rate control (Throttle delivery) minimum supported delivery rate, per channel activity: 1 per second (hard limit).
* Rate control (Throttle delivery) maximum supported delivery rate, per channel activity, when Throttle delivery is enabled: 2000 per second (hard limit).
* When setting a delivery rate, the maximum timeframe for which a campaign audience can execute is 12 hours (hard limit). If the delivery rate does not allow the full audience to be sent within that timeframe, the remaining profiles are excluded from the campaign and counted in the campaign report.

**Prerequisites and permissions:**

* Before adding a channel activity, define the target audience using a Build audience or a Read audience activity.
* Email header personalization (Email) is available only for a set of organizations (Limited Availability); access requires contacting an Adobe representative.
* Rapid delivery mode (Push) is a Journey Optimizer add-on.

**Terminology:**

* Canonical name: channel activity — variants: Email activity, Mobile message activity, Push activity, Direct mail activity, Line activity, Custom channel activity.
* Canonical name: Adobe Experience Platform — Acronym: AEP.
* Synonyms: none.
* Do not confuse: "Simulate content" (tests content variations with sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (previews and tests content with test profiles).
* Do not confuse: "One message per profile" (one message regardless of how many secondary dimension rows qualify) ≠ "One message per secondary dimension" (one message per qualifying secondary dimension row, so a profile can receive multiple messages).
* Do not confuse: "Marketing" category (opt-in required, business rules applied) ≠ "Transactional" category (opt-in not required, business rules bypassed).

**FAQ:**

* **Q: Which channels are supported in Orchestrated campaigns?** — The Guardrails and limitations section states that only Mobile message, Push, Email, and Direct mail are supported; the page's contextual help also documents Line and Custom channel activities for Orchestrated campaigns.
* **Q: How many channel activities can an Orchestrated campaign contain?** — A maximum of 10 channel activities (Email, Mobile message, Push, or Direct mail); targeting and flow control activities do not count toward this limit.
* **Q: What is the difference between Marketing and Transactional categories?** — Marketing requires opt-in and applies business rules; Transactional does not require opt-in and bypasses business rules.
* **Q: What is the difference between Simulate content and Simulate content (AEP profiles)?** — Simulate content tests content variations with sample input data or AI auto-generation; Simulate content (AEP profiles) previews and tests content with test profiles.
* **Q: Why can I not simulate content for some channel activities using test profiles?** — In test mode, the workflow pauses at the channel activity, so a channel activity located after another channel activity is never reached, and the selected test profile must belong to the audience targeted by that channel activity.
* **Q: What happens if message delivery cannot complete within the rate control timeframe?** — The maximum timeframe for a campaign audience to execute is 12 hours; if the delivery rate does not allow the full audience to be sent within that timeframe, the remaining profiles are excluded from the campaign and counted in the campaign report.

**Examples:**

* Welcome series: sending a welcome series through email, Mobile messages, push, and direct mail.
* Post-purchase follow-up: delivering a follow-up email after a purchase.
* Birthday greeting: sending personalized birthday greetings via Mobile messages.
* Cart abandonment: triggering a message through a custom channel when a customer abandons their shopping cart.
* Rate control: setting a delivery rate of 165 messages per second to ensure steady delivery without overwhelming downstream systems (an illustrative value within the 1–2000 per second supported range).

**Best practices:**

* Use Transactional only for operational or time-sensitive communications; misclassifying a promotional message as Transactional bypasses consent and business rules, which may violate regulatory requirements.

**Related pages:**

* To define the target audience before adding a channel activity: Build audience (orchestrated/activities/build-audience.md)
* To define the target audience before adding a channel activity: Read audience (orchestrated/activities/read-audience.md)
* For more information on targeting dimensions and how to configure them: Configure a Targeting dimension (orchestrated/target-dimension.md)
* For who defines a channel configuration: System Administrator (start/path/administrator.md)
* To learn how to set up channel configurations: Learn how to set up channel configurations (configuration/channel-surfaces.md)
* To apply capping rules using channel rule sets: Learn how to work with rule sets (conflict-prioritization/rule-sets.md)
* To create a content experiment for a channel activity: Create a content experiment (content-management/content-experiment.md)
* To add multilingual content to a channel activity: Get started with multilingual content (content-management/multilingual-gs.md)
* To view action tracking results for Email and Mobile deliveries: Learn more about campaign reports (reports/campaign-global-report-cja.md)
* To enable Rapid delivery mode for Push notifications: on this page (push/create-push.md)
* To add personalization in Orchestrated campaigns: Learn how to add personalization in Orchestrated campaigns (orchestrated/add-personalization.md)
* To create conditional content in the Email Designer: Learn how to create conditional content in the Email Designer (personalization/dynamic-content.md)
* To simulate content variations with sample input data or AI auto-generation: Learn how to simulate content variations (test-approve/simulate-sample-input.md)
* To preview and test content with test profiles: Preview and test your content (content-management/preview-test.md)
* To run a campaign in test before simulating content: Test your campaign before publishing (orchestrated/start-monitor-campaigns.md)
* To select a test profile matching the channel activity's target audience: Select test profiles (content-management/test-profiles.md)
* To split delivery into scheduled batches before confirming sending: Learn how to send using waves (delivery/send-using-waves.md)
* To complete activities orchestration and publish the campaign: Learn how to start and monitor Orchestrated campaigns (orchestrated/start-monitor-campaigns.md)

**Personas:**

* **marketer:** Can add a channel activity to an Orchestrated campaign canvas, choosing Email, Mobile message, Push, Direct mail, or Line. Can set the Category field to Marketing or Transactional, then select a Target dimension for the delivery in the Target section. The page states that transactional messages do not require opt-in and bypass business rules. Where: "Add a channel activity and define its properties".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Add a channel activity into the canvas.
* **Success check:** The list of channel configurations is filtered according to the target set for the delivery, and only compatible configurations appear.
* **Previous:** Define the target audience before adding a channel activity: Use the Build audience activity (orchestrated/activities/build-audience.md); Define the target audience before adding a channel activity: Use the Read audience activity (orchestrated/activities/read-audience.md)
* **Next:** Complete the activities orchestration in the canvas and publish the campaign: Start and monitor Orchestrated campaigns with Adobe Journey Optimizer (orchestrated/start-monitor-campaigns.md)

+++

<!-- ai-section-version: 1 | source-hash: d92ac7ea -->
