---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create test profiles by uploading a CSV file, using API calls, or the in-product use case, including the schema and dataset prerequisites, so you can preview content and test journeys in Journey Optimizer.

**Intents:**

* Set up the schema (with the Profile test details field group) and dataset prerequisites for test profiles
* Create test profiles by uploading a CSV file using the Map CSV to XDM schema workflow
* Create test profiles using API calls
* Use the in-product use case to generate test profiles from a predefined CSV format
* Flag profiles as test profiles by setting the `testProfile` field to `true`

**Glossary:**

* **Test profile**: A profile flagged with `testProfile = true`, required for using test mode in a journey and for previewing and testing content *(product-specific)*
* **Profile test details**: The field group that must be added to the schema; the `testProfile` flag is part of this field group *(product-specific)*
* **Simulate content**: The action to test content variations with sample input data or AI auto-generation *(product-specific)*
* **Simulate content (AEP profiles)**: The option selected from the Simulate content dropdown to preview content with test profiles *(product-specific)*
* **In-product use case**: A guided card on the Journey Optimizer home page that facilitates test profile creation from a predefined CSV format *(product-specific)*
* **Identity namespace**: The namespace (for example Email or Phone) used to uniquely identify the test profiles *(product-specific)*

**Guardrails:**

* Test profiles are required when using test mode in a journey and to preview and test content.
* To create profiles you must first create a schema and a dataset; the schema must include the Profile test details field group.
* The schema must have the correct identity descriptor applied to the primary identity field for the intended namespace; if it is missing or incorrectly configured, ingested profiles may not be flagged as test profiles (`testProfile = true`) even if ingestion completes successfully.
* When creating a profile via CSV or API, the `testProfile` field must be set to `true`.
* Test profiles may override existing profiles; before running the in-product use case, ensure the CSV contains test profiles only and that it is executed against the correct sandbox.
* The in-product use case expects a predefined CSV format with fields in this order: Person Id, Email Address, First Name, Last Name, City, Country, Gender (available values male, female, non_specified).

**Terminology:**

* Canonical name: Test profile — Acronym: n/a — variants: test profiles
* Synonyms: "`testProfile` flag" = "`testProfile` field"
* Do not confuse: "Simulate content" (sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (preview with test profiles)
* Do not confuse: "Person Id" (unique identifier reflecting the selected identity namespace) ≠ "Email Address" (test profile email address)

**FAQ:**

* **Q: What are the ways to create test profiles?** — By uploading a CSV file, using API calls, or the in-product use case.
* **Q: What must the schema include?** — The Profile test details field group, which contains the `testProfile` flag.
* **Q: Why are my ingested profiles not flagged as test profiles?** — The primary identity field may be missing the correct identity descriptor for your namespace; review the schema, confirm the descriptor, and re-ingest the data.
* **Q: How do I mark a profile as a test profile?** — Set the `testProfile` field to `true` when creating (or updating) the profile.
* **Q: What should I check before running the in-product use case?** — That the CSV contains test profiles only and that it runs against the correct sandbox, since test profiles may override existing profiles.

+++

<!-- ai-section-version: 1 | source-hash: d3e14af3 -->
