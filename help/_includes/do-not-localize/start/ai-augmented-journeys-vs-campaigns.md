---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Choose between Journeys, Action campaigns, and API-triggered campaigns based on whether you need real-time 1:1 orchestration, scheduled or inbound batch delivery, or on-demand API-triggered execution.

**Intents:**
* Understand the key differences between Journeys, Action campaigns, and API-triggered campaigns
* Select the right approach for a given marketing use case using the decision guide and comparison tables
* Understand when Action campaigns support inbound channel activations vs. outbound broadcasts
* Know when to escalate to Orchestrated campaigns (ad-hoc composition, federated data, multi-entity)
* Combine multiple approaches effectively in a marketing strategy

**Glossary:**
* **Journey**: A multi-step, real-time orchestration flow where each profile progresses at their own pace based on behavior and events. *(product-specific)*
* **Action campaign**: A campaign delivering scheduled or recurring activations to audiences — outbound broadcast or inbound channel activations to the edge for low-latency personalization. *(product-specific)*
* **API-triggered campaign**: A campaign initiated by an external system via API call, delivering a single on-demand message with payload-driven personalization. *(product-specific)*
* **Orchestrated campaign**: A Hub-side batch campaign supporting multi-entity relational data, ad-hoc audience composition, and federated data sources; not covered by the comparison tables on this page. *(product-specific)*
* **Unitary event journey**: A journey triggered by a single profile action in real time; use when multi-step orchestration is needed after an API-sent event. *(product-specific)*
* **Inbound channel activation**: Delivering personalized experiences to the edge (Code-based experience, In-app, Content Card, Web) for low-latency rendering, supported in Action campaigns. *(product-specific)*

**Guardrails:**
* Up to 10 inbound channel actions per Action campaign (hard limit) — applies to inbound channels only: Code-based experience, In-app, Content Card, Web
* Orchestrated campaigns are excluded from the comparison tables on this page to avoid oversimplification; see dedicated Orchestrated campaigns documentation for architectural details

**Terminology:**
* Canonical name: Action campaigns — variants: "scheduled campaigns", "broadcast campaigns"
* Canonical name: API-triggered campaigns — variants: "transactional campaigns", "event-driven campaigns"
* Do not confuse: "Action campaigns" (scheduled/inbound delivery to audiences) ≠ "API-triggered campaigns" (on-demand, payload-driven, no pre-built audience) ≠ "Orchestrated campaigns" (Hub-side batch with relational data)
* Do not confuse: "Unitary event journey" (triggered by a profile's real-time action) ≠ "Business event journey" (triggered by a non-profile event affecting multiple people via an internal Read Audience step)
* Synonyms: "inbound channel activation" = "inbound channel action" (used interchangeably on this page for edge-delivered experiences in Action campaigns)

**FAQ:**
* **Q: When should I use a Journey instead of an Action campaign?** — Use Journeys when customers need to move at their own pace with real-time conditional logic across multiple touchpoints; use Action campaigns for scheduled or inbound delivery to a pre-defined audience.
* **Q: Can Action campaigns deliver to inbound channels?** — Yes. Action campaigns support inbound channel activation (Code-based experience, In-app, Content Card, Web) to the edge for low-latency personalization, with up to 10 inbound actions per campaign and targeting rules for message variants.
* **Q: What distinguishes Orchestrated campaigns from Action campaigns?** — Orchestrated campaigns run Hub-side batch execution with multi-entity relational data, exact pre-send counts, ad-hoc audience composition, and federated data support; Action campaigns are stateless single-execution deliveries to Experience Platform audiences.
* **Q: When should I use an API-triggered campaign vs. a Unitary event journey?** — Use an API-triggered campaign when an external system needs to trigger a single message immediately with payload data; use a Unitary event journey when multi-step orchestration is needed after the API-sent event.
* **Q: Can I combine Journeys and campaigns in the same marketing strategy?** — Yes. Use Journeys for behavioral real-time engagement, Action campaigns for scheduled broadcasts or inbound activations, API-triggered campaigns for transactional messages, and Orchestrated campaigns for complex batch workflows.

+++
<!-- ai-accordion-version: 1 | source-hash: 873097f5 -->
