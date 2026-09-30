---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to monitor custom channel delivery performance in Journey Optimizer using out-of-the-box campaign and journey reports and the dedicated custom channel monitoring dashboard, and how to troubleshoot common delivery issues.

**Intents:**

* Monitor custom channel delivery performance through out-of-the-box campaign and journey reports
* Access and use the custom channel monitoring dashboard
* Interpret custom channel metrics such as successful calls, errors, timeouts, and pre-call failures
* Analyze outcomes and latency over time and break them down by endpoint, channel, campaign, and journey
* Troubleshoot common custom channel delivery symptoms and apply recommended resolutions

**Glossary:**

* **Custom channels monitoring dashboard**: A dedicated dashboard accessed from Administration > Channels > Channel Builder > Custom channels monitoring that monitors the reliability and performance of the API calls Journey Optimizer makes to external endpoints *(product-specific)*
* **Pre-call failures**: Custom channel sends that failed before the HTTP call was ever made to the external endpoint; these occur in Journey Optimizer's own infrastructure layer and fall into three categories: authentication failures (`AUTH_*`), request generation errors (`REQUEST_GENERATION_ERROR`), and HTTP parse errors (`HTTP_PARSE_ERROR`) *(product-specific)*
* **Timeout calls**: Number of calls that failed because they exceeded the maximum response time *(product-specific)*
* **Insight Builder**: A tool used to create custom visualizations and dashboards based on custom channel metrics *(product-specific)*
* **Successful deliveries**: Messages for which the endpoint returned an HTTP 2xx response *(product-specific)*

**Guardrails:**

* Clicks metric tracking requires a subdomain delegated for custom channels.
* Pre-call failures indicate a problem on the Journey Optimizer side or in the channel configuration, rather than an issue with your external endpoint; start troubleshooting by reviewing API credentials and required payload fields.
* Average latency is the average end-to-end response time in milliseconds for all HTTP calls, including successful calls, errors, and timeouts.
* Report granularity depends on the selected time range: a 7-day report shows KPIs per day, a 1-day range shows KPIs per hour, and a 1-hour range shows KPIs per minute.
* HTTP 401/403 errors indicate an authentication failure; update the credentials in Administration > Channels > API credentials.
* HTTP 429 errors indicate the external endpoint is throttling requests; review your endpoint's rate limits and reduce the throttling setting in the Channel Builder policy configuration.

**Terminology:**

* Canonical name: Custom channels monitoring dashboard — Acronym: n/a — variants: custom channel monitoring dashboard, Custom channel metrics
* Synonyms: "Attempted deliveries" = total number of messages sent to the external endpoint
* Do not confuse: "Successful deliveries" (report metric: messages for which the endpoint returned an HTTP 2xx response) ≠ "Successful calls" (monitoring metric: total HTTP calls that returned a valid response without error)
* Do not confuse: "4xx/5xx errors" (failed calls due to client-side or server-side errors) ≠ "Timeout calls" (calls that exceeded the maximum response time) ≠ "Pre-call failures" (sends that failed before the HTTP call was made)

**FAQ:**

* **Q: Where can I monitor custom channel performance?** — Through out-of-the-box campaign and journey reports and the dedicated custom channel monitoring dashboard, accessed from Administration > Channels > Channel Builder > Custom channels monitoring.
* **Q: What does the Clicks metric require?** — The Clicks metric counts link clicks tracked in the payload and requires a subdomain delegated for custom channels.
* **Q: What are pre-call failures?** — Custom channel sends that failed before the HTTP call was ever made to the external endpoint; they occur in Journey Optimizer's own infrastructure layer and include authentication failures, request generation errors, and HTTP parse errors.
* **Q: My calls return HTTP 429 errors. What should I do?** — The external endpoint is throttling requests from Journey Optimizer; review your endpoint's rate limits and reduce the throttling setting in the Channel Builder policy configuration.
* **Q: How does the report time granularity change with the time range?** — A 7-day report shows one data point per day, a 1-day range shows KPIs per hour, and a 1-hour range shows KPIs per minute.
* **Q: How do I troubleshoot unresolved personalization tokens?** — Verify the XDM attribute path is correct and add a default value fallback, for example `{{profile.person.name.firstName \| default("Valued Customer")}}`.

+++

<!-- ai-section-version: 1 | source-hash: e6dd6dee -->
