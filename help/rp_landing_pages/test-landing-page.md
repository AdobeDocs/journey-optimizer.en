---
solution: Journey Optimizer
product: Journey Optimizer
title: Test, validate & approve
description: Discover all testing and approval capabilities in Journey Optimizer. Preview content, simulate journeys, validate emails, run experiments, detect conflicts, and set up approval workflows before launch.
feature: Get Started, Overview
role: User
level: Beginner, Intermediate
keywords: test, validate, approve, approval, quality-assurance, qa, test-profiles, personalization, rendering, spam-check, content-experiment, a/b-test, conflict-detection, seed-list, proofs, sample-data, approval-workflow, email-testing, validation-workflow
redpen-status: CREATED_||_2025-08-11_20-30-59
exl-id: a770412f-2f80-459d-8cce-32212154d154
---
# Test, validate & approve{#section-overview}

This section covers all testing and approval capabilities in Journey Optimizer. You'll find tools to preview content with test profiles, validate journey logic, check email rendering and spam scores, run A/B experiments, detect conflicts, and set up approval workflows.

This landing page helps you choose the right testing approach based on what you're building (campaigns vs. journeys), walks you through recommended testing workflows, and provides quick access to all testing and approval resources. Start with [Choose your testing approach](#choose-your-testing-approach) below to identify which tools apply to your use case.

## Testing capabilities overview

**Testing types available:**

* Content testing: Preview and validate message content before sending → [Testing campaigns](#testing-campaigns), [Testing personalization](#testing-personalization)
* Journey logic testing: Simulate customer progression through journey paths → [Testing journeys](#testing-journeys)
* Technical testing: Validate rendering, deliverability, and authentication → [Technical validation](#2-technical-validation)
* Performance testing: Compare content variations using A/B experiments → [Content experiments](#content-experiments--ab-testing)
* Conflict testing: Detect campaign and journey overlaps → [Conflict detection](#conflict-detection)
* Approval testing: Structured review workflows before activation → [Approval workflows](#approval-workflows-for-journeys-and-campaigns)

**Key capabilities by context:**

| Capability | Applies to | Channel restrictions | Prerequisites | Primary purpose | Documentation |
|------------|-----------|---------------------|--------------|-----------------|---------------|
| [Test profiles](../using/content-management/test-profiles.md) | Campaigns, Journeys | All channels | Test profiles created | Preview personalized content | [Guide](#testing-campaigns) |
| [Sample input data](../test-approve/simulate-sample-input.md) | Campaigns, Journeys | Email, SMS, Push, Web, Code-based, In-app, Content cards | CSV/JSON file | Test multiple personalization variants | [Guide](#simulate-content-variations) |
| [Test mode](../using/building-journeys/testing-the-journey.md) | Journeys only | N/A | Draft journey, namespace configured | Simulate profile progression | [Card](#test-your-journey) |
| [Dry run](../using/building-journeys/journey-dry-run.md) | Journeys only | N/A | Journey created | Analyze execution paths | [Card](#journey-dry-run) |
| [Email rendering](../using/content-management/rendering.md) | Campaigns, Journeys | Email only | Litmus integration | Verify display across clients | [Workflow](#2-technical-validation) |
| [Spam score](../using/content-management/spam-report.md) | Campaigns, Journeys | Email only | None | Deliverability validation | [Workflow](#2-technical-validation) |
| [Seed lists](../using/configuration/seed-lists.md) | Campaigns, Journeys | Email only | Seed list configured | Stakeholder monitoring | [Card](#seed-lists-for-stakeholder-monitoring) |
| [Content experiments](../using/content-management/get-started-experiment.md) | Campaigns only | All channels | None | A/B and multi-armed bandit testing | [Card](#content-experiments--ab-testing) |
| [Conflict detection](../using/conflict-prioritization/conflicts.md) | Campaigns, Journeys (limited) | All channels | None | Prevent customer over-messaging | [Card](#conflict-detection) |
| [Approval workflows](../using/test-approve/gs-approval.md) | Campaigns, Journeys | All channels | Approval policy created | Structured review process | [Card](#approval-workflows-for-journeys-and-campaigns) |
| [Personalization playground](../using/personalization/personalize.md#playground) | All | All channels | None | Learn and test personalization syntax | [Card](#personalization-playground) |

**Common testing workflows:**

1. Pre-development: Use [personalization playground](#testing-personalization) to learn syntax
2. During development: Preview with [test profiles](#testing-campaigns), validate with [sample input data](#simulate-content-variations)
3. Pre-launch: Run [technical tests](#2-technical-validation) (rendering, spam), check [conflicts](#conflict-detection), submit for [approval](#approval-workflows-for-journeys-and-campaigns)
4. Post-launch: Monitor with live reports (see [Monitoring & Troubleshooting](#monitoring--troubleshooting)), iterate based on results


## Why testing and approval matter

Testing and approval processes serve as essential quality gates that protect your brand reputation and ensure campaign success. Here's why they matter:

* **Catch errors before they reach customers** - Identify broken links, incorrect personalization, rendering issues, and logic flaws in a controlled environment where fixes are quick and risk-free.

* **Improve deliverability** - Test spam scores, validate email authentication, and check rendering across email clients to maximize inbox placement and engagement rates.

* **Ensure brand consistency** - Preview content with different test profiles to verify that personalization displays correctly for various customer segments and maintains brand standards.

* **Validate complex journeys** - Simulate multi-step journey flows to confirm that triggers fire correctly, conditions evaluate properly, and customers receive the right messages at the right time.

* **Establish accountability** - Implement formal approval workflows that require stakeholder sign-off, creating clear ownership and reducing unauthorized or premature campaign launches.

* **Save time and resources** - Detect issues early in the development cycle when fixes are cheaper and faster, preventing costly post-launch corrections or customer service escalations.

## Key terminology

**[Test profiles](../using/content-management/test-profiles.md)** = Synthetic customer profiles (not real customers) used to preview personalized content. Flagged in Real-time Customer Profile Service. Required for test mode and content preview. [Learn how to create test profiles](../using/audience/creating-test-profiles.md)

**[Test mode](../using/building-journeys/testing-the-journey.md)** = Journey simulation feature that sends test profiles through journey paths. Limitations: Draft journeys only, requires namespace, test profiles only. [See test mode documentation](../using/building-journeys/testing-the-journey.md)

**[Dry run](../using/building-journeys/journey-dry-run.md)** = Journey execution analysis tool that traces paths without sending messages or making API calls. Use case: Validate logic without consuming resources. [Learn about dry run](../using/building-journeys/journey-dry-run.md)

**[Sample input data](../test-approve/simulate-sample-input.md)** = CSV or JSON files containing profile attribute values for testing personalization. Supports up to 30 variants. Alternative to creating test profiles. [How to simulate content variations](../test-approve/simulate-sample-input.md)

**[Seed lists](../using/configuration/seed-lists.md)** = Email addresses of internal stakeholders automatically included in actual deliveries (not test sends). Email channel only. Use case: Quality monitoring and compliance. [Configure seed lists](../using/configuration/seed-lists.md)

**[Content experiments](../using/content-management/get-started-experiment.md)** = A/B testing or multi-armed bandit experiments comparing content variations. Campaigns only, not available in journeys. [Get started with experiments](../using/content-management/get-started-experiment.md) | [Create experiments](../using/content-management/content-experiment.md)

**[Proofs](../using/content-management/proofs.md)** = Test email deliveries sent to specific email addresses using test profile data. Different from seed lists (proofs are manual test sends, seed lists are automatic stakeholder copies). [Send proofs](../using/content-management/proofs.md)

**[Conflict detection](../using/conflict-prioritization/conflicts.md)** = Tool that identifies overlapping campaigns and journeys targeting same audiences. Limited journey support: unitary, Audience Qualification, and Read Audience types only. [Learn about conflict management](../using/conflict-prioritization/gs-conflict-prioritization.md)

**[Approval workflows](../using/test-approve/gs-approval.md)** = Multi-step review process requiring stakeholder approval before activation. Requires approval policy configuration. [Set up approvals](../using/test-approve/gs-approval.md) | [Create policies](../using/test-approve/approval-policies.md)

**[Rendering tests](../using/content-management/rendering.md)** = Email display validation across email clients (Gmail, Outlook, Apple Mail) and devices. Requires Litmus integration. [Test email rendering](../using/content-management/rendering.md)

**[Personalization playground](../using/personalization/personalize.md#playground)** = Interactive learning environment to experiment with personalization syntax and test expressions with sample data. No live datasets required. [Access the playground](../using/personalization/personalize.md#playground)

## Decision tree for testing method selection

Use this decision tree to quickly identify the right testing tools for your specific scenario. Answer each question based on your context (what you're building, what you need to validate, and which channel you're using) to navigate directly to the relevant capabilities and documentation.

+++ **Question 1: What are you testing?**

* Campaign → [Testing campaigns](#testing-campaigns)
* Journey → [Testing journeys](#testing-journeys)
* Personalization expressions → [Personalization playground](#testing-personalization)
+++

+++**Question 2: What aspect needs validation?**

* Content and personalization → [Test profiles](#testing-campaigns) or [sample input data](#simulate-content-variations)
* Email display → [Email rendering tests](#2-technical-validation)
* Deliverability → [Spam score checks](#2-technical-validation)
* Journey logic and flow → [Test mode](#testing-journeys) or [dry run](#journey-dry-run)
* Performance comparison → [Content experiment](#content-experiments--ab-testing) (campaigns only)
* Timing conflicts → [Conflict detection](#conflict-detection)
* Stakeholder review → [Approval workflow](#approval-workflows-for-journeys-and-campaigns)
+++

+++**Question 3: What channel?**

* Email → All testing methods available (see [Testing campaigns](#testing-campaigns))
* SMS, Push → [Content testing](#testing-campaigns), [sample input data](#simulate-content-variations), [approval workflows](#approval-workflows-for-journeys-and-campaigns)
* Web, In-app, Code-based → [Content testing](#testing-campaigns), [sample input data](#simulate-content-variations), [approval workflows](#approval-workflows-for-journeys-and-campaigns)
* Multiple channels → Test each channel separately
+++

+++**Question 4: When in the workflow?**

* Before building → [Personalization playground](#personalization-playground) for learning
* During building → [Test profiles](#testing-campaigns) and [sample input data](#simulate-content-variations) for validation
* Before launch → [Rendering tests](#2-technical-validation), [spam checks](#email-spam-report), [conflict detection](#conflict-detection), [approvals](#approval-workflows-for-journeys-and-campaigns)
* After launch → [Live reports](../using/building-journeys/report-journey.md) and [monitoring](#monitoring--troubleshooting)
+++


## Choose your testing approach

The right testing approach depends on what you're building and what you need to validate. Use this guide to identify the most relevant testing tools for your scenario.

### Testing campaigns

**For all campaigns:**

* Preview and test content using [test profiles](../using/content-management/test-profiles.md) or [sample input data](../test-approve/simulate-sample-input.md)
* Check [email rendering](../using/content-management/rendering.md) across devices and clients (email channel only)
* Run [spam score checks](../using/content-management/spam-report.md) (email channel only)
* Review [conflicts](../conflict-prioritization/conflicts.md) with other campaigns and journeys
* Set up [seed lists](../configuration/seed-lists.md) for stakeholder monitoring (email channel only)
* Submit for [approval](../using/test-approve/gs-approval.md) before activation

**For A/B testing and optimization:**

* Create [content experiments](../using/content-management/get-started-experiment.md) to test multiple treatments and measure performance

**For API-triggered campaigns:**

* Use the [Campaign Simulation API](https://developer.adobe.com/journey-optimizer-apis/references/simulations/){target="_blank"} to trigger proof jobs programmatically

### Testing journeys

**For all journeys:**

* Use [test mode](../using/building-journeys/testing-the-journey.md) to simulate profile progression (draft journeys only, requires namespace) or [dry run](../using/building-journeys/journey-dry-run.md) to analyze execution paths without sending messages
* Test individual messages using [preview and proofs](../using/content-management/preview-test.md)
* Check [conflicts](../conflict-prioritization/conflicts.md) with other journeys and campaigns
* Submit for [approval](../using/test-approve/gs-approval.md) before publishing

**For complex journeys:**

* Use test mode and dry run together to thoroughly validate branching logic and execution paths
* Test different entry conditions and profile attributes systematically

**Note:** Conflict detection and journey capping are available for unitary, Audience Qualification, and Read Audience journeys only.

### Testing personalization

**Before building content:**

* Experiment in the [personalization playground](../using/personalization/personalize.md#playground) to learn syntax and test expressions with sample data

**During content creation:**

* Preview with [test profiles](../using/content-management/test-profiles.md) to validate personalization renders correctly
* Test multiple scenarios using [sample input data](../test-approve/simulate-sample-input.md) from CSV/JSON files (supports up to 30 variants)

## Testing best practices

To maximize the effectiveness of your testing efforts, follow these recommended practices:

1. **Test early and often** - Don't wait until a campaign is fully built. Test content, personalization, and logic incrementally as you develop.

1. **Use realistic test profiles** - [Create test profiles](../using/audience/creating-test-profiles.md) that accurately represent your target audience segments, including edge cases and different personalization scenarios.

1. **Test across devices and clients** - Verify [email rendering](../using/content-management/rendering.md) on popular email clients (Gmail, Outlook, Apple Mail) and devices (desktop, mobile, tablet) to ensure consistent display (email channel only).

1. **Validate personalization thoroughly** - Test with multiple [test profiles](../using/content-management/test-profiles.md) that have different attribute values to confirm personalization tokens render correctly and fallback values work. Use the [personalization playground](../using/personalization/personalize.md#playground) to experiment with personalization expressions and test code with sample data before applying them to your campaigns.

1. **Test content variations with sample data** - Use [sample input data](../test-approve/simulate-sample-input.md) from CSV or JSON files to test up to 30 personalization scenarios without creating numerous test profiles, saving time while ensuring comprehensive coverage. Supports email, SMS, push, web, code-based experience, in-app, and content cards channels.

1. **Use seed lists for stakeholder monitoring** - Configure [seed lists](../configuration/seed-lists.md) to automatically include internal stakeholders who will receive copies of all deliveries at execution time for quality monitoring and compliance verification (email channel only).

1. **Simulate journey paths** - For complex journeys with multiple branches, use [test mode](../using/building-journeys/testing-the-journey.md) to test different entry conditions and profile attributes to validate all possible paths. Available for draft journeys that use a namespace.

1. **Check deliverability indicators** - Review [spam scores](../using/content-management/spam-report.md), authentication status, and email health metrics before large sends (email channel only).

1. **Document test results** - Keep records of test outcomes, issues found, and resolutions to improve future testing processes and share learnings with your team.

1. **Involve stakeholders early** - Share previews and test results with stakeholders before [formal approval](../using/test-approve/gs-approval.md) to gather feedback and align expectations.

## Recommended testing workflow

Follow this systematic approach to ensure thorough testing and smooth approvals:

### 1. Content development and preview

Start by creating your content and using preview capabilities to verify initial design and personalization:

* Design your [email](../using/email/create-email.md), [SMS](../using/sms/create-sms.md), [push notification](../using/push/create-push.md), or other channel content

* Use the **[Simulate content](../using/content-management/preview-test.md)** feature to preview with test profiles

* Check [personalization tokens](../using/personalization/personalization-syntax.md), dynamic content, and fallback values

* Experiment with personalization expressions in the **[personalization playground](../using/personalization/personalize.md#playground)** to test and refine your code with sample data before applying to live content

* Test multiple variations using **[sample input data](../test-approve/simulate-sample-input.md)** from CSV/JSON files to validate personalization across diverse profile scenarios

* Verify [rendering](../using/content-management/rendering.md) across different screen sizes and email clients

### 2. Technical validation

Validate technical aspects that impact deliverability and functionality:

* Run [spam score checks](../using/content-management/spam-report.md) to identify potential deliverability issues

* Test links to ensure they're not broken and track properly

* Validate [email authentication](../using/configuration/dmarc-record.md) (SPF, DKIM, DMARC) configuration

* Review HTML rendering and check for CSS compatibility issues

* Test [responsive design](../using/email/content-from-scratch.md) on mobile and desktop devices

* Check for [potential conflicts](../conflict-prioritization/conflicts.md) with other campaigns and journeys to prevent customer message fatigue and timing issues

### 3. Journey testing (journeys only)

If you're testing a journey, validate the orchestration logic:

* Activate **[Test mode](../using/building-journeys/testing-the-journey.md)** to simulate profile progression through the journey

* Test different [entry conditions](../using/building-journeys/entry-management.md) and audience qualifications

* Verify [wait activities](../using/building-journeys/wait-activity.md), [conditions](../using/building-journeys/condition-activity.md), and branching logic work correctly

* Use **[Dry run](../using/building-journeys/journey-dry-run.md)** for complex journeys to analyze execution paths without sending messages

* Check that [events](../using/event/about-events.md) trigger correctly and [custom actions](../using/action/about-custom-action-configuration.md) execute as expected

### 4. Approval submission

Once testing is complete and issues are resolved:

* Submit the campaign or journey for approval according to your organization's [approval policy](../using/test-approve/approval-policies.md)

* Include test results and documentation with the [approval request](../using/test-approve/request-approval.md)

* Address any feedback or change requests from [approvers](../using/test-approve/review-approve-request.md)

* Make necessary revisions and retest if changes are significant

### 5. Pre-launch verification

Before activating your campaign or journey:

* Perform a final review of all settings, audiences, and [schedules](../using/building-journeys/journey-properties.md)

* Verify that all approvals are in place and documented

* Confirm send times and [time zones](../using/building-journeys/timezone-management.md) are correct

* Enable [monitoring and alerts](../using/reports/alerts.md) to track performance post-launch

### 6. Monitor and iterate

After launch, continue monitoring to catch any issues early:

* Set up [system alerts](../using/reports/alerts.md) for journey errors, high bounce rates, or low engagement

* Review [live reports](../using/building-journeys/report-journey.md) to track performance against expectations

* Be prepared to [pause or modify](../using/building-journeys/journey-pause.md) journeys if critical issues arise

* Document lessons learned to improve future testing processes

## Testing in action: Use cases

See how testing concepts apply to real-world scenarios:

| Use Case | What You'll Learn | Key Testing Focus |
|----------|-------------------|-------------------|
| **[Send multi-channel messages](../using/building-journeys/journeys-uc.md)** | Test a journey that combines Read Audience, reaction events, and email/push messages. Validate the entire flow from audience targeting to message delivery. | Multi-channel coordination, reaction events, end-to-end flow validation, testing and publishing steps |
| **[Send a message to subscribers](../using/building-journeys/message-to-subscribers-uc.md)** | Test journeys that target subscription lists with dynamic email addressing. Validate personalization expressions for correct subscriber targeting. | Personalization expressions, dynamic addressing, subscription list targeting |
| **[Send time-bound messages](../using/building-journeys/weekday-email-uc.md)** | Test journeys with time-based conditions to ensure messages are sent on specific days. Validate wait activities and scheduling logic. | Time-based conditions, wait activities, scheduling validation |
| **[Explore more journey use cases](../using/building-journeys/jo-use-cases.md)** | Access comprehensive collection of practical examples covering experience events, multi-channel messaging, and external system integrations. | Various scenarios, advanced patterns, integration testing |

## Test & Approve Content

:::: landing-cards-container
:::
![icon](https://cdn.experienceleague.adobe.com/icons/list-check.svg)

Preview, Test, and Validate Content

Learn how to preview, test, and validate personalized content using test profiles, email rendering tests, spam score evaluations, and more.

[Explore Preview & Test Content](preview-test-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/shield-halved.svg)

Approval Workflows for Journeys and Campaigns

Understand how to set up, manage, and execute approval processes to ensure quality control for journeys and campaigns.

[Learn About Approval Workflows](approve-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/bullseye.svg)

Test Your Journey

Validate your journey before publishing by testing it with specific profiles to ensure events, conditions, and actions work as expected. Available for draft journeys that use a namespace.

[Test your journey](../using/building-journeys/testing-the-journey.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/code-branch.svg)

Journey Dry Run

Perform a dry run to simulate and validate your journey's execution path, identifying potential issues before going live.

[Learn about Journey Dry run](../using/building-journeys/journey-dry-run.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/chart-line.svg)

Monitoring & Troubleshooting

Access comprehensive troubleshooting resources, system alerts, and error codes to resolve journey execution and performance issues.

[View Monitoring & Troubleshooting](troubleshoot-journey-landing-page.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/code.svg)

Personalization Playground

Experiment with personalization expressions in a safe environment. Test code with sample data and preview results before applying to your campaigns and journeys.

[Learn About the Personalization Playground](../using/personalization/personalize.md#playground)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/data.svg)

Content Experiments & A/B Testing

Optimize your campaigns by testing multiple content variations and measuring performance to identify the best-performing treatments. Available for campaigns only (supports A/B and multi-armed bandit experiments).

[Learn About Content Experiments](../using/content-management/get-started-experiment.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/envelope.svg)

Seed Lists for Stakeholder Monitoring

Automatically include internal stakeholder addresses in deliveries to monitor actual messages sent to customers for quality assurance and compliance. Available for email channel only.

[Configure Seed Lists](../using/configuration/seed-lists.md)
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/bell.svg)

Conflict Detection

Identify potential overlaps between campaigns and journeys to prevent overwhelming customers with too many simultaneous communications. Available for campaigns and unitary, Audience Qualification, and Read Audience journeys.

[Detect Conflicts](../using/conflict-prioritization/conflicts.md)
:::

::::

## Additional Resources

### Essential testing and validation guides

* [Simulate Content Variations](../test-approve/simulate-sample-input.md) - Test up to 30 personalization scenarios using CSV or JSON files. Ideal for multilingual content testing without creating multiple test profiles. Supports email, SMS, push, web, code-based, in-app, and content cards.

* [Creating Test Profiles](../using/audience/creating-test-profiles.md) - Create and manage test profiles to simulate customer scenarios. Learn how to flag profiles for testing, set attributes, and organize test segments.

* [Email Spam Report](../using/content-management/spam-report.md) - Check spam scores before sending to improve deliverability and inbox placement. Get actionable recommendations for content optimization.

* [Journey FAQ](../using/building-journeys/journey-faq.md) - Quick reference for common questions about journey testing, execution, and troubleshooting.

### Dependencies and relationships

Understand how testing capabilities connect to each other and to your broader Journey Optimizer workflows. This section maps prerequisites, upstream/downstream dependencies, and common capability combinations.

+++**Prerequisites (required before testing)**

* Test profiles must be created before using test mode or content preview
* Approval policies must be configured before submitting for approval
* Seed lists must be created before adding to campaigns/journeys
* Litmus integration required for email rendering tests
* Journey must be in draft status to use test mode
* Journey must have namespace configured to use test mode

+++

+++**What testing depends on (upstream)**

* Content creation: Need campaigns or journeys to test
* Test profiles: Required for test mode and content preview
* Approval policies: Required for approval workflows
* Configuration: Channel configurations, email authentication, domain settings

+++

+++**What depends on testing (downstream)**

* Campaign/journey activation: Cannot activate without resolving errors
* Publishing: Approval may be required before publishing
* Live monitoring: Post-launch monitoring and reporting
* Optimization: Use test results to refine future campaigns

+++

+++**Related capabilities**

* Testing + Approval workflows = Quality assurance process
* Testing + Conflict detection = Preventing customer over-messaging
* Testing + Content experiments = Performance optimization
* Testing + Reporting = Continuous improvement cycle
* Test profiles + Personalization = Content validation
* Dry run + Test mode = Comprehensive journey validation

+++

+++**Common capability combinations**

* Content testing: Test profiles + Sample input data + Personalization playground
* Email validation: Rendering tests + Spam scores + Test profiles + Proofs
* Journey validation: Test mode + Dry run + Test profiles
* Pre-launch checklist: All technical tests + Conflict detection + Approval workflows

+++

### Common questions

+++**Q: What testing is required before launching a campaign?**

**Minimum:** Content preview with test profiles + Spam score check (email)
**Recommended:** + Email rendering + Conflict detection + Approval workflow
**Best practice:** + Sample input data testing + Seed lists + A/B experiment (if optimizing)

+++

+++**Q: How do I test personalization without creating many test profiles?**

**Primary solution:** Use [sample input data](../test-approve/simulate-sample-input.md) with CSV/JSON files (supports up to 30 variants)
**Alternative:** Create 3-5 representative [test profiles](../using/audience/creating-test-profiles.md) covering key segments
**Learning tool:** Experiment first in [personalization playground](../using/personalization/personalize.md#playground)

+++

+++**Q: What's the difference between test mode and dry run for journeys?**

**Test mode:** Sends test profiles through journey, triggers actual actions, generates test messages. Requires draft journey + namespace.
**Dry run:** Traces execution paths without sending anything. Works on any journey status. No messages sent, no actions executed.
**Use together:** Test mode for message testing + Dry run for logic validation = comprehensive coverage.

+++

+++**Q: Can I test journeys in production/live status?**

**Test mode:** No - draft journeys only
**Dry run:** Yes - works on any journey status
**Content preview:** Yes - preview individual messages anytime
**Workaround:** Duplicate live journey to draft for full test mode validation

+++

+++**Q: Which testing capabilities require external integrations?**

**Email rendering:** Requires Litmus integration (separate license)
**All others:** Built-in to Journey Optimizer, no additional integrations required
**Note:** Test profiles require Real-time Customer Profile Service (included)

+++

+++**Q: How do I test API-triggered campaigns?**

**Option 1:** Use [Campaign Simulation API](https://developer.adobe.com/journey-optimizer-apis/references/simulations/){target="_blank"} for programmatic testing
**Option 2:** Preview content with test profiles in UI
**Option 3:** Send proofs to test email addresses
**Best practice:** Combine all three for comprehensive validation

+++


### Related topics

* [Content Management](content-management-landing-page.md) - Learn how to design, preview, and manage content using templates, fragments, and the Email Designer. Master content creation best practices for consistent branding.

* [Reporting & Analytics](reporting-landing-page.md) - Analyze campaign and journey performance with comprehensive reports, dashboards, and metrics. Make data-driven decisions to optimize customer experiences.

* [Journey Configuration](configure-journeys-landing-page.md) - Configure data sources, events, and custom actions to enable sophisticated journey orchestration. Set up the technical foundations for journey creation.

* [Campaign Management](../using/campaigns/get-started-with-campaigns.md) - Explore different campaign types and learn how to create, schedule, and optimize batch and real-time campaigns for maximum impact.
