---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create and configure a loyalty challenge, personalize its content, configure lifecycle messaging, publish the challenge, and generate and publish its delivery journey.

**Intents:**

* Create a loyalty challenge and configure its settings
* Configure the challenge structure with tasks and rewards
* Configure challenge content using a content card or code-based experience
* Personalize a content card with challenge metadata
* Configure messaging for the challenge lifecycle
* Publish a challenge and generate and publish its associated journey

**Glossary:**

* **[!UICONTROL Content]**: The tab that controls how the challenge is represented in locations where loyalty members access challenges and track their progress *(product-specific)*
* **[!UICONTROL Content card]**: An action type that displays the challenge as a card-style experience on customer devices *(product-specific)*
* **[!UICONTROL Code-based experience]**: An action type that delivers challenge content through a custom implementation using the code-based channel *(product-specific)*
* **[!UICONTROL Generate Journey]**: An option that automatically publishes the challenge and creates the journey that orchestrates challenge delivery, except for challenges configured with **[!UICONTROL No end date]**, for which no journey is generated *(product-specific)*

**Guardrails:**

* Configuring challenge content and messaging is optional.
* Publishing a challenge without generating a journey does not deliver it to customers. Delivery requires generating and publishing a journey.
* Changes to a challenge must be made in the Loyalty Challenge editor and require generating a new journey. Work done directly on the existing challenge journey is lost if the challenge is changed.
* No journey is generated for challenges configured with **[!UICONTROL No end date]**. The challenge still runs, and members can still opt in and complete tasks.

**Terminology:**

* **[!UICONTROL Content]** controls challenge representation; **[!UICONTROL Messaging]** configures messages at challenge lifecycle stages.
* Do not confuse **[!UICONTROL Publish Challenge]**, which publishes without generating a journey, with **[!UICONTROL Generate Journey]**, which publishes the challenge and creates its delivery journey unless the challenge is configured with **[!UICONTROL No end date]**.
* The generated journey initially has **Draft** status. The challenge appears with **[!UICONTROL Published]** status after publishing.

**FAQ:**

* **Q: How can a challenge be represented to members?** - Use a **[!UICONTROL Content card]** or **[!UICONTROL Code-based experience]** action in the **[!UICONTROL Content]** tab.
* **Q: Can I use challenge metadata in a content card?** - Yes. You can use challenge metadata to personalize the card content.
* **Q: Is challenge content required?** - Configuring challenge content is optional.
* **Q: Does publishing the challenge deliver it to customers?** - Customers do not receive the challenge until its journey is generated and published.
* **Q: What happens when I change a challenge?** - Changes must be made in the Loyalty Challenge editor and require a new journey. Work done directly on the existing challenge journey is lost if the challenge is changed.
* **Q: Can a challenge without an end date generate a journey?** - No journey is generated for challenges configured with **[!UICONTROL No end date]**. Members can still opt in and complete tasks.

+++

<!-- ai-section-version: 3 | source-hash: 31425013 -->