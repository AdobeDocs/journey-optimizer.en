---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how an administrator generates SMS usage reports in Adobe Journey Optimizer to reconcile mobile-terminated (MT) and mobile-originated (MO) volume with vendor billing, using a Sinch MMS API credential and downloadable CSV output.

**Intents:**

* Generate an SMS usage report to reconcile messaging volume with vendor billing
* Create a Sinch MMS API credential used only to retrieve usage data
* Configure a report with a name, credential, and date range
* Retrieve and view the usage summary and daily SMS volume by short code
* Export the report as a CSV file

**Glossary:**

* **Mobile-terminated (MT)**: Messages counted in the report as sent traffic, broken down by short code *(product-specific)*
* **Mobile-originated (MO)**: Messages counted in the report as received traffic, broken down by short code *(product-specific)*
* **Sinch MMS API credential**: An API credential with SMS vendor set to Sinch MMS, used only to retrieve usage data from Sinch and separate from credentials used to send messages *(product-specific)*
* **Usage summary**: The report section showing total MO and MT messages for the selected dates, broken down by short code *(product-specific)*
* **Daily SMS volume**: The report section showing SMS volume by day, broken down by short code *(product-specific)*

**Guardrails:**

* SMS usage metrics are available when you purchase SMS through Adobe Journey Optimizer.
* Usage data is available only for the last 90 days.
* Reports require an API credential with SMS vendor set to Sinch MMS, which is separate from the Sinch credentials used to send SMS or MMS messages, although the field values come from the same Sinch project.
* Generating usage reports requires the Manage SMS settings permission.
* Reports summarize send and receive traffic by short code or phone number, aggregated by day.

**Terminology:**

* Canonical name: SMS usage report — Acronym: n/a — variants: SMS usage metrics
* Do not confuse: "Mobile-terminated (MT)" (sent traffic) ≠ "Mobile-originated (MO)" (received traffic)
* Do not confuse: "Pending" (report is being generated after Retrieve report) ≠ "Ready" (report can be opened with View)
* Do not confuse: the Sinch MMS API credential used to retrieve usage data ≠ the Sinch credentials used to send SMS or MMS messages

**FAQ:**

* **Q: How far back does usage data go?** — Usage data is available only for the last 90 days.
* **Q: Which credential is required for usage reports?** — An API credential with SMS vendor set to Sinch MMS, which is separate from the credentials used to send messages although the field values come from the same Sinch project.
* **Q: What permission do I need to generate reports?** — The Manage SMS settings permission is required.
* **Q: What does a generated report contain?** — A Usage summary with total MO and MT messages for the selected dates broken down by short code, and a Daily SMS volume section showing SMS volume by day broken down by short code.
* **Q: How do I export the report?** — Click Download CSV to download a CSV file for the report you are viewing.

+++

<!-- ai-section-version: 1 | source-hash: 474f3720 -->
