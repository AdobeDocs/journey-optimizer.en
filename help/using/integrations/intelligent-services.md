---
solution: Journey Optimizer
product: journey optimizer
title: Integrate with Intelligent Services
description: Learn how to leverage Adobe Intelligent Services and Customer AI predictions in Journey Optimizer
feature: Journeys, Integrations
topic: Artificial Intelligence
role: User
level: Intermediate
keywords: artificial, AI, intelligent, journey, service
exl-id: 20da09e1-0611-4d27-a589-30552011e06c
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/rTKcWHwfwleQtD68fcdeqYK2AMQHVaknKtsNDFsOldI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: bbbea26f-9621-49eb-9ab8-e06fb3bbce8c
    internal-label: Artificial intelligence
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: eb30f47f-d87a-400f-8f78-63ce7979ff56
    internal-label: Machine learning
subfeature_v2: []
---
# Integrate with intelligent services {#ai-overview}

The integration with **[!DNL Adobe Intelligent Services]** enables you to leverage artificial intelligence and machine learning for customer experience use cases. This allows marketing analysts to set up predictions tailored to a company's needs using business-level configurations without requiring data science expertise.

[!DNL Intelligent Services], built on [!DNL Adobe Experience Platform], provides AI-as-a-service for customer experience teams. It helps predict customer behavior, measure campaign impact, and improve returns on investment. For more details, refer to the [[!DNL Adobe Experience Platform] documentation](https://experienceleague.adobe.com/docs/experience-platform/intelligent-services/home.html){target="_blank"}.  

Integration between [!DNL Journey Optimizer] and [!DNL Intelligent Services] allows you to leverage customer predictions.

Customer AI, a component of [!DNL Adobe Intelligent Services], predicts likely customer actions. See the [[!DNL Adobe Experience Platform] documentation](https://experienceleague.adobe.com/docs/experience-platform/intelligent-services/customer-ai/overview.html){target="_blank"}.  

Customer AI allows brands to create churn or conversion machine learning-based scores. These scores are available as profile attributes in [!DNL Adobe Experience Platform] profiles (Real-time Customer Profile).

As a result, these attributes can be used like any other profile attributes in Journey Optimizer. Use them in conditions for decisioning, actions, or segment building.

![Customer AI integration showing propensity scores and predictions](assets/customer-ai.png)

+++AI Assistant — Page context

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
