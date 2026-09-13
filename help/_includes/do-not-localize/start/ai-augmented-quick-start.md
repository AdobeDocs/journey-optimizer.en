---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page maps the four Journey Optimizer implementation roles, their responsibilities, and the recommended implementation order so teams can find the right starting point.

**Intents:**

* Identify the four Journey Optimizer implementation roles and their responsibilities
* Understand the recommended implementation order and dependencies between roles
* Prepare for implementation with the "Before you begin" alignment steps
* Find the role-specific getting-started guide and quick-start tasks
* Understand how roles collaborate across an implementation

**Glossary:**

* **Administrator**: The role responsible for environment setup and access management, including sandboxes, permissions, object-level access control (OLAC), channel configurations, and message presets *(product-specific)*
* **Data Engineer**: The role responsible for customer profile data and data sources, including XDM schemas, datasets, identity namespaces, and data ingestion *(product-specific)*
* **Developer**: The role responsible for technical implementation and integrations, including Mobile and Web SDK, events, and custom action endpoints *(product-specific)*
* **Marketer**: The role responsible for journey design and personalized experiences, including journeys, content, offers, decision components, and audiences *(product-specific)*
* **Object-level access control (OLAC)**: An access control the Administrator applies as part of security and governance setup *(product-specific)*

**Guardrails:**

* Adobe Journey Optimizer defines distinct roles, but a single individual can perform multiple roles or all roles depending on your organization's structure.
* Components and capabilities available in your environment depend on your permissions and on your licensing package.
* The Administrator sets up the environment first, because this must happen before other teams can work.
* While the implementation sequence is typical, some activities can occur in parallel, for instance Developers may work on app integrations while Data Engineers configure schemas.
* Adobe CX Enterprise general privacy guidelines and procedures apply to Journey Optimizer.

**Terminology:**

* Canonical name: Roles and responsibilities — Acronym: n/a — variants: role-based quick start, implementation roles
* Synonyms: "Marketer" = "Business Practitioner"; "Data Engineer" = "Data Architect"
* Do not confuse: "Decisioning" (used for push and SMS personalization) ≠ "Decision Management" (offers, eligibility rules, and components in a centralized library)

**FAQ:**

* **Q: What are the four roles in a Journey Optimizer implementation?** — Administrator, Data Engineer, Developer, and Marketer, working in sequence.
* **Q: In what order should implementation proceed?** — The typical sequence is Administrator (sets up the environment), then Data Engineer (creates the data foundation), then Developer (implements technical integrations), then Marketer (designs and executes customer experiences).
* **Q: Can one person hold more than one role?** — Yes. A single individual can perform multiple roles or all roles, depending on your organization's structure.
* **Q: Do all activities have to happen strictly in sequence?** — No. Some activities can occur in parallel, such as Developers working on app integrations while Data Engineers configure schemas.
* **Q: What should teams align on before configuring Journey Optimizer?** — Define your use cases first, involve all teams that touch the customer experience, establish a shared customer identifier, verify data privacy compliance, plan for testing before go-live, and prepare your brand content and asset library.

+++

<!-- ai-section-version: 1 | source-hash: c330cf01 -->
