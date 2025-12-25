---
solution: Journey Optimizer
product: Journey Optimizer
title: Test & approve
description: Test & approve
redpen-status: CREATED_||_2025-08-11_20-30-59
exl-id: a770412f-2f80-459d-8cce-32212154d154
---
# Test & approve{#section-overview}

Quality assurance is critical to delivering exceptional customer experiences. Adobe Journey Optimizer provides comprehensive testing and approval capabilities to help you validate content, verify journey logic, and ensure campaigns meet quality standards before reaching your audience. From previewing personalized messages with test profiles to simulating complex journey flows, these tools empower you to identify and resolve issues early, reduce risk, and maintain brand integrity. Whether you're testing email rendering across devices, validating multi-step journeys, or establishing formal approval workflows, this section guides you through best practices and step-by-step processes to build confidence in your campaigns and journeys. By implementing thorough testing and structured approvals, you'll minimize errors, improve deliverability, and create seamless experiences that resonate with your customers.

## Why testing and approval matter

Testing and approval processes serve as essential quality gates that protect your brand reputation and ensure campaign success. Here's why they matter:

* **Catch errors before they reach customers** - Identify broken links, incorrect personalization, rendering issues, and logic flaws in a controlled environment where fixes are quick and risk-free.

* **Improve deliverability** - Test spam scores, validate email authentication, and check rendering across email clients to maximize inbox placement and engagement rates.

* **Ensure brand consistency** - Preview content with different test profiles to verify that personalization displays correctly for various customer segments and maintains brand standards.

* **Validate complex journeys** - Simulate multi-step journey flows to confirm that triggers fire correctly, conditions evaluate properly, and customers receive the right messages at the right time.

* **Establish accountability** - Implement formal approval workflows that require stakeholder sign-off, creating clear ownership and reducing unauthorized or premature campaign launches.

* **Save time and resources** - Detect issues early in the development cycle when fixes are cheaper and faster, preventing costly post-launch corrections or customer service escalations.

## Testing best practices

To maximize the effectiveness of your testing efforts, follow these recommended practices:

1. **Test early and often** - Don't wait until a campaign is fully built. Test content, personalization, and logic incrementally as you develop.

1. **Use realistic test profiles** - [Create test profiles](../using/audience/creating-test-profiles.md) that accurately represent your target audience segments, including edge cases and different personalization scenarios.

1. **Test across devices and clients** - Verify [email rendering](../using/content-management/rendering.md) on popular email clients (Gmail, Outlook, Apple Mail) and devices (desktop, mobile, tablet) to ensure consistent display.

1. **Validate personalization thoroughly** - Test with multiple [test profiles](../using/content-management/test-profiles.md) that have different attribute values to confirm personalization tokens render correctly and fallback values work.

1. **Simulate journey paths** - For complex journeys with multiple branches, use [test mode](../using/building-journeys/testing-the-journey.md) to test different entry conditions and profile attributes to validate all possible paths.

1. **Check deliverability indicators** - Review [spam scores](../using/content-management/spam-report.md), authentication status, and email health metrics before large sends.

1. **Document test results** - Keep records of test outcomes, issues found, and resolutions to improve future testing processes and share learnings with your team.

1. **Involve stakeholders early** - Share previews and test results with stakeholders before [formal approval](../using/test-approve/gs-approval.md) to gather feedback and align expectations.

## Recommended testing workflow

Follow this systematic approach to ensure thorough testing and smooth approvals:

### 1. Content development and preview

Start by creating your content and using preview capabilities to verify initial design and personalization:

* Design your [email](../using/email/create-email.md), [SMS](../using/sms/create-sms.md), [push notification](../using/push/create-push.md), or other channel content
* Use the **[Simulate content](../using/content-management/preview-test.md)** feature to preview with test profiles
* Check [personalization tokens](../using/personalization/personalization-syntax.md), dynamic content, and fallback values
* Verify [rendering](../using/content-management/rendering.md) across different screen sizes and email clients

### 2. Technical validation

Validate technical aspects that impact deliverability and functionality:

* Run [spam score checks](../using/content-management/spam-report.md) to identify potential deliverability issues
* Test links to ensure they're not broken and track properly
* Validate [email authentication](../using/configuration/dmarc-record.md) (SPF, DKIM, DMARC) configuration
* Review HTML rendering and check for CSS compatibility issues
* Test [responsive design](../using/email/content-from-scratch.md) on mobile and desktop devices

### 3. Journey testing

For journeys, validate the orchestration logic:

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

* **[Send multi-channel messages](../using/building-journeys/journeys-uc.md)** - This use case demonstrates how to test a journey that combines Read Audience, reaction events, and email/push messages. Learn how to validate the entire flow from audience targeting to message delivery, and see testing and publishing steps in action.

* **[Send a message to subscribers](../using/building-journeys/message-to-subscribers-uc.md)** - Discover how to test journeys that target subscription lists with dynamic email addressing. This example shows how to validate personalization expressions and ensure messages reach the correct subscribers.

* **[Send time-bound messages](../using/building-journeys/weekday-email-uc.md)** - Understand how to test journeys with time-based conditions to ensure messages are sent on specific days. See how to validate wait activities and scheduling logic.

* **[Explore more journey use cases](../using/building-journeys/jo-use-cases.md)** - Access a comprehensive collection of practical examples covering experience events, multi-channel messaging, and external system integrations.

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

Validate your journey before publishing by testing it with specific profiles to ensure events, conditions, and actions work as expected.

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

::::

## Additional Resources

### Essential testing and validation guides

* [Live Report in Your Journey](../using/building-journeys/report-journey.md) - Monitor journey metrics in real-time to track performance and identify issues during execution. Access detailed breakdowns of profile progression, event triggers, and action completion rates.

* [Creating Test Profiles](../using/audience/creating-test-profiles.md) - Create and manage test profiles to simulate real customer scenarios and validate personalization. Learn how to flag profiles for testing, set attribute values, and organize test profile segments.

* [Email Spam Report](../using/content-management/spam-report.md) - Check your email spam score before sending to improve deliverability and inbox placement. Understand how spam filters evaluate your content and get recommendations for improvement.

* [Journey FAQ](../using/building-journeys/journey-faq.md) - Find answers to common questions about journey creation, testing, execution, and troubleshooting. Quick reference for resolving frequent issues and understanding journey behavior.

### Related topics

* [Content Management](content-management-landing-page.md) - Learn how to design, preview, and manage content using templates, fragments, and the Email Designer. Master content creation best practices for consistent branding.

* [Reporting & Analytics](reporting-landing-page.md) - Analyze campaign and journey performance with comprehensive reports, dashboards, and metrics. Make data-driven decisions to optimize customer experiences.

* [Journey Configuration](configure-journeys-landing-page.md) - Configure data sources, events, and custom actions to enable sophisticated journey orchestration. Set up the technical foundations for journey creation.

* [Campaign Management](../using/campaigns/get-started-with-campaigns.md) - Explore different campaign types and learn how to create, schedule, and optimize batch and real-time campaigns for maximum impact.
