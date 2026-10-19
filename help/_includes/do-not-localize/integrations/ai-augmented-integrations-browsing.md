---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Configure a Browsing integration and link it to a Standard integration parameter so marketers can search, browse, and select items returned by an external API during authoring.

**Intents:**

* Configure the items path, search query parameter, and pagination for a Browsing integration.
* Choose how items are displayed to marketers.
* Preview search and pagination behavior with **[!UICONTROL Test browsing]**.
* Link a Browsing integration to a Standard integration parameter.
* Select an item during authoring and insert its **[!UICONTROL Reference path]** value into the integration parameter.

**Glossary:**

* **Browsing integration**: An integration that lets marketers search, browse, and paginate through items returned by an external API, then select a specific item directly in the authoring experience. *(product-specific)*
* **[!UICONTROL Items path]**: The path where the list of items is located. *(product-specific)*
* **[!UICONTROL Offset parameter]**: The request parameter that indicates the number of items to skip. *(product-specific)*
* **[!UICONTROL Page parameter]**: The request parameter that indicates the page number. *(product-specific)*
* **[!UICONTROL Cursor parameter]**: The request parameter that carries the cursor value. *(product-specific)*
* **[!UICONTROL Reference path]**: The value corresponding to the selected entity that is automatically inserted into the integration parameter. *(product-specific)*
* **[!UICONTROL Test browsing]**: A preview of search and pagination behavior with the configured settings. *(product-specific)*

**Guardrails:**

* Browsing integrations are created by an administrator from the **[!UICONTROL Browsing]** tab of the **[!UICONTROL Integrations]** configuration.
* When a parameter is linked to a **[!UICONTROL Browsing]** integration, marketers can pick its value from a selector in the message or journey editor, rather than typing it manually.
* In Page pagination, **[!UICONTROL First page is]** selects whether the first page is numbered 0 or 1; **[!UICONTROL Total pages path]** is optional if the total count path is provided.

**Terminology:**

* Canonical name: Browsing integration.
* Do not confuse: **[!UICONTROL Offset parameter]** indicates the number of items to skip; **[!UICONTROL Page parameter]** indicates the page number; **[!UICONTROL Cursor parameter]** carries the cursor value.
* Do not confuse: **[!UICONTROL Page size]** sets the number of items to request per page; **[!UICONTROL Page size parameter]** specifies the request parameter that indicates the number of items per page in Page pagination.

**FAQ:**

* **Q: Which pagination types can I choose?** Offset, Page, or Cursor.
* **Q: How can items be displayed to marketers?** The **[!UICONTROL Render]** menu provides Table, List, and Avatar.
* **Q: What does Test browsing preview?** **[!UICONTROL Test browsing]** previews the search and pagination behavior with the configured settings.
* **Q: How does a Browsing integration let marketers select a Standard integration parameter value?** Link the Browsing integration to the parameter on the Standard integration so marketers can select values through the Browsing selector instead of entering them manually.
* **Q: What value is inserted after an entity is selected and the selection is confirmed?** The corresponding **[!UICONTROL Reference path]** value is automatically inserted into the integration parameter.

+++

<!-- ai-section-version: 1 | source-hash: 76fdf9e9 -->