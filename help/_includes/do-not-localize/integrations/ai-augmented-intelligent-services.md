---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** This page explains how Journey Optimizer integrates with Adobe Intelligent Services — specifically Customer AI — to leverage machine learning-based propensity scores as profile attributes in journeys.

**Intents:**
- Understand how Adobe Intelligent Services integrates with Journey Optimizer
- Use Customer AI propensity scores as profile attributes in journey conditions or actions
- Enable AI-driven predictions for churn or conversion without requiring data science expertise
- Apply machine learning scores to segment building within Journey Optimizer

**Glossary:**
- **Adobe Intelligent Services**: A suite of AI/ML services built on Adobe Experience Platform that enables customer experience predictions without requiring data science expertise *(product-specific)*
- **Customer AI**: A component of Adobe Intelligent Services that generates machine learning-based churn or conversion propensity scores for customer profiles *(product-specific)*
- **Propensity score**: A machine learning-based score representing the likelihood of a customer performing a specific action (e.g., churn or conversion), stored as a profile attribute *(product-specific)*

**Guardrails:**
- No data science expertise is required, but business-level configuration must be completed by marketing analysts
- Customer AI scores must first be configured in Adobe Experience Platform before they are available as profile attributes in Journey Optimizer

**Terminology:**
- Canonical name: Adobe Intelligent Services — Acronym: none — variants: Intelligent Services, AI services
- Canonical name: Customer AI — Acronym: none — variants: Customer AI scores, propensity scores
- Synonyms: "churn score" = "churn propensity" ; "conversion score" = "conversion propensity"
- Do not confuse: "Adobe Intelligent Services" ≠ "AI Assistant" (Intelligent Services is a predictive ML platform; AI Assistant is a conversational interface)

**FAQ:**
- **Q: What is Customer AI in the context of Journey Optimizer?** — Customer AI is an Adobe Intelligent Services component that creates machine learning-based churn or conversion scores, which become available as profile attributes usable in Journey Optimizer conditions, actions, and segment building.
- **Q: Do I need data science skills to use Adobe Intelligent Services?** — No, marketing analysts can configure predictions using business-level settings without requiring data science expertise.
- **Q: Where are Customer AI scores stored?** — They are stored as profile attributes in Adobe Experience Platform's Real-time Customer Profile, making them accessible like any other profile attribute in Journey Optimizer.
- **Q: How can I use Customer AI scores in a journey?** — Once available as profile attributes, the scores can be used in conditions for decisioning, in action configurations, or for building audience segments.

+++
