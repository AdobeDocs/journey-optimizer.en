---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to set up a live connection to cloud storage destinations so you can export Journey Optimizer datasets for reporting, archival, and external data analysis.

**Intents:**

* Export Journey Optimizer datasets to a cloud storage destination on a schedule.
* Identify which cloud storage destinations are available.
* Determine which datasets can be exported.
* Obtain the access control permissions required to export datasets.
* Join exported data for custom reporting using documented join keys.

**Glossary:**

* **Dataset export**: establishing a live connection with a cloud storage location to export dataset content *(product-specific)*
* **Cloud storage destination**: an export target such as Amazon S3, Azure Blob, Azure Data Lake Gen 2, Data Landing Zone, Google Cloud Storage, or SFTP
* **AJO Message Export Dataset**: stores sent email and SMS message content marked for export; data is retained for seven calendar days from ingestion *(product-specific)*
* **`scopeDetails.correlationID` / `exdRequestID`**: join keys used to tie interaction or feedback data to the AJO Entity Dataset and to a decision request *(product-specific)*

**Guardrails:**

* Datasets can be exported to the 6 cloud storage destinations listed on the page: Amazon S3, Azure Blob, Azure Data Lake Gen 2, Data Landing Zone, Google Cloud Storage, and SFTP.
* Required access control permissions: **Manage and Activate Dataset Destinations** (Destinations), **View Datasets** (Data Management), and **View Destinations** (Destinations).
* AJO Message Export Dataset data is retained for 7 calendar days from ingestion (hard retention).
* Cloud storage destinations are accessed from the **[!UICONTROL Destinations]** menu, in the **[!UICONTROL Catalog]** tab.

**Terminology:**

* Do not confuse: the **[!UICONTROL Export datasets]** button (dataset export) ≠ the **Activate** button (which, when Real-Time Customer profiles are used, exports datasets and activates audiences)

**FAQ:**

* **Q: Which cloud storage destinations can I export to?** — Amazon S3, Azure Blob, Azure Data Lake Gen 2, Data Landing Zone, Google Cloud Storage, and SFTP.
* **Q: What permissions do I need to export datasets?** — Manage and Activate Dataset Destinations, View Datasets, and View Destinations.
* **Q: How long is AJO Message Export Dataset data kept?** — Seven calendar days from ingestion.
* **Q: Where do I start a dataset export?** — From the Destinations menu, Catalog tab; select Export datasets on the destination card and choose the connection.
* **Q: How do I join exported data for reporting?** — Use `scopeDetails.correlationID` to join to the AJO Entity Dataset, and `exdRequestID` to tie a single decision request to analytics events.

+++

<!-- ai-section-version: 1 | source-hash: 6828f9b3 -->
