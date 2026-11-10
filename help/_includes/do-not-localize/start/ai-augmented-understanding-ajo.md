---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how Adobe Journey Optimizer and Adobe Experience Platform work together as a continuous data-to-experience cycle, covering the platform foundation, the orchestration engine, seven key functional areas, and the underlying architecture.

**Intents:**

* Understand how Journey Optimizer builds on Adobe Experience Platform to connect data, content, and journey orchestration
* Identify the Adobe Experience Platform foundation components and the Journey Optimizer orchestration components
* Learn the seven key functional areas, how they map to the orchestration engine stages, and how they operate as a continuous cycle
* Choose between a campaign, a journey, and an Orchestrated campaign
* Understand the sandbox types and how to create a sandbox
* Understand the architecture and the core Adobe Experience Platform services that Journey Optimizer shares
* Locate related privacy and security information

**Glossary:**

* **Continuous optimization cycle**: The flow where data drives customer understanding, which informs personalized content and decisions, orchestrated into journeys, delivered across channels, measured for effectiveness, and refined over time *(product-specific)*
* **Functional area**: One of the seven areas that work together in Journey Optimizer — Data Management, Customer Management, Content Management, Decision Management, Journey Management, Connections, and Administration & Privacy *(product-specific)*
* **Real-Time Customer Profile**: An Adobe Experience Platform core service that creates unified profiles by merging data from multiple sources *(product-specific)*
* **Connections**: The functional area and delivery capability that connects data sources, channels, and external systems *(product-specific)*
* **Orchestrated campaign**: A multi-step batch campaign designed, automated, and delivered across channels from one visual canvas. It personalizes content, channel, and timing using profile attributes and business context from relational, multi-entity data, and builds audiences with exact counts before sending marketing or transactional messages *(product-specific)*
* **Development sandbox / production sandbox**: The two sandbox types. A development sandbox is for building and testing with non-production profiles; a production sandbox is where you send to your real customers. An administrator creates either type in Adobe Experience Platform by selecting Create sandbox and choosing the type *(product-specific)*

**Guardrails:**

* Journey Optimizer is one of four applications natively built on Adobe Experience Platform, alongside Real-Time CDP, Customer Journey Analytics, and Adobe Mix Modeler.
* Because it shares Adobe Experience Platform core services (Real-Time Customer Profile, Identity Graph, data governance, and query services), Journey Optimizer accesses a unified customer data foundation without requiring separate integrations.
* Journey Optimizer can operate as a standalone application or interoperate with other Adobe Experience Platform-native applications.
* Adobe CX Enterprise privacy and security practices apply to Journey Optimizer, supporting compliance with regulations such as GDPR.

**Terminology:**

* Canonical name: Adobe Journey Optimizer — Acronym: AJO — variants: Journey Optimizer
* Canonical name: Adobe Experience Platform — Acronym: AEP — variants: Experience Platform, Platform
* Synonyms: "orchestration engine" = "Adobe Journey Optimizer" (as described on this page)
* Do not confuse: "Data Management" (functional area for organizing customer data) ≠ "Decision Management" (functional area for selecting the best offer in real time)
* Synonyms: "Delivery (Connections)" in the orchestration engine list = "Connections" functional area
* Do not confuse: "development sandbox" (non-production profiles, for building and testing) ≠ "production sandbox" (real customers); "training sandbox" is a development sandbox configured with sample data for the tutorials

**FAQ:**

* **Q: How do Journey Optimizer and Adobe Experience Platform relate?** — Adobe Experience Platform is the foundational data layer, and Journey Optimizer is the orchestration engine built on top of it, applying platform data and insights to deliver personalized experiences.
* **Q: How many functional areas does Journey Optimizer include?** — Seven: Data Management, Customer Management, Content Management, Decision Management, Journey Management, Connections, and Administration & Privacy.
* **Q: Which approach should I use: a campaign, a journey, or an Orchestrated campaign?** — Use a campaign to send a scheduled or API-triggered message to an audience, a journey when customers move at their own pace through a real-time, multi-step, behavior-driven flow, and an Orchestrated campaign to run a complex batch workflow with multi-entity data.
* **Q: What types of sandbox exist, and how do I create one?** — Development and production. An administrator creates a sandbox in Adobe Experience Platform by selecting Create sandbox and choosing the Development or Production type, then adds the new sandbox to a role in Permissions before anyone can use it.
* **Q: Can Journey Optimizer be used on its own?** — Yes, it can operate as a standalone application or interoperate with other Adobe Experience Platform-native applications.
* **Q: What core services does Journey Optimizer share with Adobe Experience Platform?** — Real-Time Customer Profile, Identity Graph, data governance, and query services.

**Personas:**

* **admin:** Can manage users, configure sandboxes, set up channels, and handle privacy requests. The page states that Administration and Privacy controls ensure compliance throughout the continuous cycle. Where: "Key functional areas".
* **developer:** Can structure customer data into schemas and datasets within the Data Platform. Can import data from CRM platforms, websites, mobile apps, and cloud storage using pre-built connectors. Can merge data from multiple sources, such as email interactions, in-store purchases, and web behavior, into unified profiles. Where: "Adobe Experience Platform: the foundation".
* **marketer:** Can author and personalize messages for any channel using a built-in visual designer, reusable templates, and a centralized asset library. Can automate real-time, multi-step sequences of interactions as journeys or send a scheduled or API-triggered message to an audience as campaigns. The page states that real-time decisioning logic selects the best offer for each individual. Where: "Adobe Journey Optimizer: the orchestration engine".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Use the free Journey Optimizer tutorials and a training sandbox to practice the five concepts.
* **Success check:** You can practice the five concepts without touching production data.
* **Previous:** You want to learn about Journey Optimizer's key capabilities first: Journey Optimizer (start/get-started.md); You need definitions of the key terms used on this page: Key terminology (start/terminology.md)
* **Next:** You are not sure who sets up what in Journey Optimizer: Roles and responsibilities | Adobe Journey Optimizer (start/quick-start.md); You need implementation considerations before you build: Journey Optimizer guardrails and limitations (start/guardrails.md)

+++

<!-- ai-section-version: 2 | source-hash: 179e7c42 -->
