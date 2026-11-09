---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to trigger an Orchestrated campaign with a signal from the REST API or from another campaign's End activity, and how to pass payload parameters that become variables for targeting, conditions, and expressions.

**Intents:**

* Schedule an Orchestrated campaign to start on a signal instead of a fixed schedule.
* Define parameters for the signal payload, with test values for use in test mode.
* Build and test the campaign in Draft before publishing, including copying a sample API request.
* Publish the campaign and trigger it from the REST API.
* Chain campaigns by configuring an End activity to send a signal to a downstream campaign.
* Inspect campaign event variables passed in a trigger signal from the campaign logs.

**Glossary:**

* **Triggered by a signal**: the schedule option that makes a campaign wait for a signal instead of running on a schedule *(product-specific)*
* **End activity**: the campaign activity, placed at the end of a branch, that can send a signal to a downstream campaign through its External signal section *(product-specific)*
* **External signal**: the section of the End activity where the downstream campaign to trigger is selected *(product-specific)*
* **Test values**: values defined for signal parameters in the scheduler, used when the campaign is triggered in test mode *(product-specific)*
* **Copy API request**: the scheduler option that copies the orchestrated campaign ID, sandbox name, organization ID, and parameter values, in cURL or HTTP Request format *(product-specific)*

**Guardrails:**

* To trigger an Orchestrated campaign using a signal, you need the Publish orchestrated campaigns permission (`orchestrated-campaign.publish`).
* For a live orchestrated campaign, a throttle guardrail enforces a minimum interval of one hour between two API trigger executions (hard limit); calling the API again before that interval has elapsed returns HTTP 429 (Too many requests). This guardrail is not applied when you trigger a draft version to test it.
* For Orchestrated campaigns triggered by the REST API, if you pass a parameter in the API call that has not been defined in the scheduler, the API call still succeeds and the parameter is propagated and can be used in expressions; however, the orchestrated campaign interface will not help you use it — for example, the Test activity will not list or show parameters that were not defined in the scheduler.
* You cannot run the full chain end-to-end in draft for campaigns triggered by an End activity: once the upstream campaign is published, its End activity only starts a published downstream campaign.
* The downstream campaign must be live before you can publish the upstream campaign that references it in an End activity; if the signal is sent while the target campaign is not published, execution will fail.
* You can use several End activities on the same canvas, each configured to trigger a different downstream campaign.
* Several campaigns can trigger the same downstream campaign, and each call can send a different payload.

**Terminology:**

* Canonical name: Triggered by a signal — variant: signal.
* Do not confuse: "End activity" signal (sent at runtime to a published downstream campaign) ≠ REST API trigger call used to test a draft downstream campaign before both campaigns are published.

**FAQ:**

* **Q: How do I make a campaign start from a signal instead of a schedule?** — Open the schedule configuration and select Triggered by a signal.
* **Q: Where do I define parameters for the signal payload?** — In the campaign scheduler, using Add parameter, where you can also set Test values for test mode.
* **Q: What happens if I pass a parameter in the API call that was not defined in the scheduler?** — The API call still succeeds and the parameter is propagated for use in expressions, but the Test activity will not list or show it.
* **Q: How often can I call the trigger API for a live campaign?** — A throttle guardrail enforces a minimum interval of one hour between two API trigger executions; calling again sooner returns HTTP 429 (Too many requests). This guardrail does not apply when triggering a draft version to test it.
* **Q: Can I test the full chain from an upstream End activity to a downstream campaign before publishing both?** — No; once published, an End activity only starts a published downstream campaign. To test the downstream side first, keep it in Draft, set Test values for its signal parameters, and trigger it directly with the REST API using the same payload the End activity would send.
* **Q: What must be true of the downstream campaign before I publish the upstream campaign's End activity that references it?** — The downstream campaign must be live; if the signal is sent while it is not published, execution will fail.

**Personas:**

* **developer:** Can trigger a published Orchestrated campaign by calling the trigger API, and pass parameters in the payload that become variables for targeting, conditions, and expressions. Can copy a sample cURL or HTTP Request from the campaign scheduler, including the campaign ID, sandbox name, organization ID, and parameter values. The page states that a throttle guardrail enforces a minimum one-hour interval between two API trigger executions for a live campaign. Where: "Send the signal with the REST API".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Open the schedule configuration and select Triggered by a signal.
* **Success check:** In the Tasks tab of the campaign logs, you can access the event variables passed in the trigger signal.
* **Previous:** Opening the schedule configuration to set up the Orchestrated campaign: Create and schedule Orchestrated campaigns with Journey Optimizer (orchestrated/create-orchestrated-campaign.md); Adding and connecting activities on the campaign canvas: Create Orchestrated campaigns with Adobe Journey Optimizer (orchestrated/orchestrate-activities.md)
* **Next:** Using signal parameters as variables in targeting, conditions, or expressions: Use variables in Orchestrated campaigns (orchestrated/variables-orchestrated-campaigns.md); Publishing and monitoring the campaign after testing it: Start and monitor Orchestrated campaigns with Adobe Journey Optimizer (orchestrated/start-monitor-campaigns.md)

+++

<!-- ai-section-version: 1 | source-hash: c0049f36 -->
