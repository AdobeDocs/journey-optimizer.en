---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is an overview of the AI and machine learning features across Journey Optimizer, including AI Assistant, AI agents, AI-powered content generation, integrations and tools, Send-Time Optimization, AI decisioning, and content experimentation.

**Intents:**

* Understand what AI Assistant can do and how to access it
* Learn which AI agents are available and what permissions each requires
* Generate content and message variations with AI across supported channels
* Predict the best send time per customer with Send-Time Optimization
* Rank and personalize offers with AI decisioning models
* Optimize Decisioning rules and ranking formulas with AI-suggested simplifications

**Glossary:**

* **AI Assistant**: The conversational guide to Journey Optimizer that answers product-knowledge questions and, in Beta, surfaces operational insights about journeys *(product-specific)*
* **Journey Agent**: An AI agent offering two skills in AI Assistant, Analyze and Create, for optimizing or building journeys from natural language *(product-specific)*
* **Experimentation Agent**: An AI agent that analyzes and manages digital experiments across websites, emails, push messages, and applications *(product-specific)*
* **Generate Content**: AI-powered content generation for subject lines, body text, images, and message variations *(product-specific)*
* **Auto-optimization**: A ranking model type that learns from overall, non-personalized offer performance and retrains roughly every 6 hours *(product-specific)*
* **Personalized optimization**: A ranking model type that uses customer profile attributes, behavior, and audience membership to predict the best offer per individual *(product-specific)*
* **Send-Time Optimization**: An AI capability that predicts the optimal send time per customer from historical engagement data *(product-specific)*
* **Journey Optimizer MCP server**: A Beta capability that connects Journey Optimizer to MCP-compatible AI applications for plain-language queries *(product-specific)*

**Guardrails:**

* AI Assistant requires agreement to the Adobe Experience Cloud Generative AI User Guidelines before use.
* Operational Insights are in Beta, are currently only available for Journeys, and reflect data from your current sandbox.
* Send-Time Optimization is only available for Email and Push actions in journeys; your organization needs at least 30 days of history using those actions before enabling it.
* AI Content Generation is only available for the Email, Push, Web, and SMS channels.
* Brand asset uploads support PDFs, images, or ZIP files (max 50 MB) (hard limit).
* Custom templates support up to 8-10 images.
* Auto-optimization requires at least 2 offers with 100+ display events and 5+ click events each within the last 14 days; offers below this threshold are treated as new and only served through exploration traffic.
* Personalized optimization uses a rolling 30-day window; Adobe recommends at least 1,000 impressions and 100 conversion events per offer per week (recommended); by default, offers with fewer than 1,000 impressions or 50 conversions do not get a model trained for them.
* Up to 5 audiences can be selected to train a single personalized optimization model.
* AI-powered rule and formula optimization analyzes only rules and ranking formulas whose PQL expression is larger than 2 KB (UTF-8 encoded); smaller expressions are not analyzed.
* AI-powered rule and formula optimization requires the Generate Content permission on the AI Assistant resource.
* The Journey Optimizer MCP server is in Beta, and all operations are currently read-only.
* GenStudio for performance marketing integration is in Limited availability and email channel only.
* The Experimentation Agent is available with the Journey Optimizer Experimentation Accelerator license and requires View Experiments and Manage Experiment Metadata permissions.

**Terminology:**

* Canonical name: Send-Time Optimization — Acronym: n/a — variants: send-time optimization
* Synonyms: "Generate Content" = "AI content generation"
* Do not confuse: "Auto-optimization" (learns from overall, non-personalized performance) ≠ "Personalized optimization" (predicts the best offer per individual)
* Do not confuse: "Journey Analyze skill" (optimize existing journeys) ≠ "Journey Create skill" (build new journeys from prompts)
* Do not confuse: "AI Assistant" (conversational guide) ≠ "AI Agents" (specialized agents for deep analysis and recommendations)

**FAQ:**

* **Q: What permissions do I need for AI features?** — Generate Content requires the Generate Content permission; AI Assistant product knowledge requires agreement to the Adobe Generative AI User Guidelines; each agent requires its listed View/Manage permissions.
* **Q: Is AI-generated content always accurate?** — No; always review AI-generated content for accuracy and brand appropriateness, and use the thumbs up/down feedback tools.
* **Q: Which channels support AI Content Generation?** — Only the Email, Push, Web, and SMS channels.
* **Q: What are the requirements for AI ranking models?** — They differ by model type; Auto-optimization and Personalized optimization have distinct minimum interaction-data thresholds described in Requirements.
* **Q: How do I get access to these features?** — Most AI features are included with Journey Optimizer; some capabilities such as Send-Time Optimization or AI Agents may require enablement by Adobe, so contact your Adobe representative.

+++

<!-- ai-section-version: 1 | source-hash: bfd9b49c -->
