---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to add a Direct mail message to a journey or a scheduled campaign and how to configure the extraction file that direct mail providers use to send personalized mail to your customers.

**Intents:**

* Add an Action activity from the Actions palette to a journey and select the Direct mail channel
* Choose Direct mail in the Actions section of a Scheduled - Marketing campaign
* Configure the extraction file properties, such as filename, timestamp, and header or footer notes
* Add and format the columns (Data Fields) displayed in the extraction file
* Add decision policies and include decision item attributes as column data
* Preview the extraction file with Simulate content

**Glossary:**

* **Direct mail message**: A message added to a journey or a Scheduled - Marketing campaign, for which you configure the extraction file that your direct mail provider requires to send mail to your customers *(product-specific)*
* **Extraction file**: The file, configured with a filename and columns, that direct mail providers require to send mail to your customers *(product-specific)*
* **Edit content**: The button that opens the editor used to configure the extraction file content *(product-specific)*
* **Data Fields**: The section where columns and the information displayed in the extraction file are added and configured *(product-specific)*
* **Simulate content**: The option used to preview the extraction file once its content has been defined *(product-specific)*
* **Decision policy**: A decision policy inserted through the personalization editor, whose decision item attributes can be used as column data in the extraction file *(product-specific)*

**Guardrails:**

* Before creating a direct mail message, a file routing configuration and a direct mail message configuration must already exist.
* In a campaign, audience selection supports up to 100 million profiles.
* You can add up to 50 columns to the extraction file.
* Direct Mail supports the Holdout functionality but does not currently support Treatments.
* Journey direct mail extraction files are generated according to the file routing frequency; profiles are included in the next export after they reach the Direct mail node. With a frequency shorter than 24 hours, profiles can arrive in different export windows and produce multiple files during a day; a 24-hour routing frequency produces one file per day.
* Campaign direct mail extraction files are generated when the campaign starts; for recurring campaigns, a file is generated for each campaign execution.
* Decision policies in direct mail are a new capability; previously, direct mail extraction files could not use the Decisioning engine.

**Terminology:**

* Canonical name: Direct mail message — Acronym: n/a
* Do not confuse: "Holdout" (supported) ≠ "Treatments" (not currently supported)
* Do not confuse: "file routing configuration" ≠ "direct mail configuration"

**FAQ:**

* **Q: How do I add a direct mail message?** — Add an Action activity to a journey and select the Direct mail channel, or select Direct mail in a Scheduled - Marketing campaign, then choose or create a direct mail configuration.
* **Q: How many columns can the extraction file contain?** — You can add up to 50 columns.
* **Q: Does direct mail support Holdout and Treatments?** — It supports the Holdout functionality but does not currently support Treatments.
* **Q: How do I preview the extraction file?** — Use Simulate content once the content of the extraction file has been defined.
* **Q: Can I use decision policies in the extraction file?** — Yes; select a column in Data Fields, open the personalization editor, create or insert a decision policy, and use decision item attributes as column data.

+++

<!-- ai-section-version: 1 | source-hash: 2d122b4e -->
