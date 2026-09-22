---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the system, journey, audience, channel, and content guardrails and limitations of Journey Optimizer, including numeric limits and their scopes, so you can plan deployments that scale without hitting failures.

**Intents:**

* Plan journeys within the activity limit and the concurrent journey limits per sandbox type
* Size event payloads and journey instances within their limits
* Configure custom actions and Read Audience activities within their throughput and concurrency limits
* Keep email, in-app, inbound, and content assets within their size and volume limits
* Understand which limits are hard (enforced) versus recommended

**Glossary:**

* **Journey instance**: The per-profile store of all data gathered during journey execution, which has a maximum size of 1 MB *(product-specific)*
* **Unitary journey**: A journey starting with an event or an audience qualification, subject to specific Select package limitations *(product-specific)*
* **Dry run**: A journey type that counts toward the engageable profile and live journey quotas and is counted in several publication-time guardrail scopes *(product-specific)*
* **Test mode**: A journey state counted in several publication-time guardrail scopes (for events, XDM schemas, and Audience Qualification activities) *(product-specific)*
* **Engageable profile**: A profile counted toward your contractual engageable profile count, which pseudonymous inbound profiles can increase *(product-specific)*

**Guardrails:**

* Datasets Time-To-Live guardrail: 90 days for data in the profile store and 13 months for data in the data lake, rolled out to new sandboxes and new organizations as of February 2025 and enforced on existing customer sandboxes starting October 1, 2026.
* The number of activities in a journey is limited to 50; this activity limit cannot be increased (hard limit).
* The number of live, closed, paused, and dry run journeys active at one time is limited to 200 in production sandboxes and 100 in development sandboxes (hard limit, enforced when you publish a journey).
* A journey instance for a profile has a maximum size of 1 MB (hard limit); it is advised to limit an event payload below 800 KB (recommended); business events and unitary events are subject to a stricter 64 KB limit.
* Any event that starts or enters a journey is limited to a maximum of 64 KB of uncompressed, minified JSON (hard limit); events exceeding this size are dropped and do not trigger the journey.
* The journey runtime keeps an internal queue of up to 10 pending events per profile and journey version; additional events are discarded with the `maxInstanceStackEventsReached` reason.
* A global journey timeout stops the progress of individuals 91 days after they enter; it is not displayed in the interface and cannot be changed (hard limit).
* Journey payload size validation uses a default maximum journey payload size of 2 MB (2,000,000 bytes); the size reflects the serialized journey definition (activity configuration, expressions, conditions, data mappings, parameters) and is not determined by activity count alone; referenced entities such as email content are excluded. A soft warning is shown at 90 to 99 percent of the limit, and at 100 percent or more save or publish is blocked with HTTP 413 Request Entity Too Large (hard limit).
* Events throughput: peak volume of 5,000 inbound journey events per second for unitary events and 5,000 inbound journey events per second for Read Audience based journey events, across all sandboxes.
* A single event can be referenced by a maximum of 25 journeys, and a single XDM schema by a maximum of 100 events, across all live, closed, paused, test mode, and dry run journeys at one time (hard limit; publishing is blocked when reached).
* Profile reentrance into unitary journeys is temporally blocked by default for 5 minutes.
* Custom actions capping: 300,000 calls over one minute per host and per sandbox for endpoints with response times under 0.75 seconds (default cap, sliding window — raisable via the Capping or Throttling APIs); a separate 150,000 calls per 30 seconds applies to endpoints over 0.75 seconds; any targeted endpoint must support at least 200 TPS and throttling cannot go below 200 TPS.
* A sandbox can include a maximum of 300 Audience Qualification activities across all live, closed, paused, test mode, and dry run journeys (hard limit; publishing is blocked when reached).
* You can publish up to 10 audience compositions in a given sandbox.
* Read Audience: each organization can run up to five Read Audience instances concurrently across all sandboxes and journeys; sandbox throughput is a maximum of 20,000 profiles per second shared across all Read Audience activities (individual activities configurable from 500 to 20,000 profiles per second); jobs not processed within 12 hours are cleaned up and will not execute; for supplemental IDs the reading rate is limited to a maximum of 500 profiles per second.
* In-app message content size is limited to 2 MB (hard limit).
* Email message content for journey publication must not exceed 2 MB after backend processing (hard limit; the operation fails); keep authored content well below 2 MB, ideally under 1 MB, to allow a 300 to 400 KB buffer (recommended).
* Inbound: peak volume of 5,000 inbound requests per second across all inbound channels, and a maximum of 500 active inbound actions at any moment in time (hard limit).
* Transactional messages: peak volume of 500 transactional messages per second in campaigns.
* Content authoring recommended size limits: Template 1200 KB, Fragment 700 KB, Message 1200 KB, Landing page 1000 KB (recommended); a warning is surfaced when a variant exceeds its threshold but it does not block saving or publishing.
* Fragments cannot exceed 700 KB (hard limit); up to 60 unique fragments per content variant (warning at 45, publishing blocked at 60) and up to 120 across all variants of a single message (warning at 90, publishing blocked at 120); a fragment must be in Live status to be used.
* For pseudonymous inbound profiles, Adobe recommends setting a Time-To-Live of 14 days to match the current Edge profile TTL (recommended).

**Terminology:**

* Canonical name: Guardrails and limitations — variants: guardrails, limits
* TPS: transactions per second — RPS: requests per second
* Do not confuse: "production sandboxes" (limit of 200 concurrent live, closed, paused, and dry run journeys) ≠ "development sandboxes" (limit of 100)
* Do not confuse: journey status scope "live, closed, paused, and dry run" (the 200/100 concurrent journey limit) ≠ "live, closed, paused, test mode, and dry run" (the event, XDM schema, and Audience Qualification limits)
* Do not confuse: 1 MB journey instance limit ≠ 64 KB event payload limit ≠ 2 MB journey payload (serialized journey definition) limit ≠ 2 MB email message content limit

**FAQ:**

* **Q: Can the 50-activity journey limit be increased?** — No; the activity limit cannot be increased. If you approach it, split the journey into smaller sub-journeys using jump activities or recreate it in a new version.
* **Q: How many journeys can be active at one time?** — Up to 200 live, closed, paused, and dry run journeys in production sandboxes and 100 in development sandboxes, enforced when you publish.
* **Q: What is the maximum event payload size?** — Any event that starts or enters a journey is limited to 64 KB of uncompressed, minified JSON; events exceeding this size are dropped and do not trigger the journey.
* **Q: What is the custom action call cap?** — 300,000 calls over one minute per host and per sandbox for endpoints under 0.75 seconds, or 150,000 calls per 30 seconds for endpoints over 0.75 seconds.
* **Q: What are the size limits for email content when publishing journeys?** — The processed message content must not exceed 2 MB after backend processing or the operation fails; keep authored content ideally under 1 MB to leave a 300 to 400 KB buffer.
* **Q: How many Read Audience instances can run concurrently?** — Each organization can run up to five Read Audience instances concurrently across all sandboxes and journeys, with a sandbox throughput maximum of 20,000 profiles per second shared across all Read Audience activities.

+++

<!-- ai-section-version: 1 | source-hash: 9751576c -->
