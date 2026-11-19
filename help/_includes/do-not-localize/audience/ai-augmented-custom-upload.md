---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to import an audience from a CSV file using the Adobe Experience Platform Audience Portal and map its identity attribute to customer profiles.

**Intents:**

* Import an audience from a CSV file using the Audience Portal
* Specify which CSV attribute to use as the identity and the profile identity it maps to
* Understand what happens when a CSV identity value is not found in the profile
* Understand Incremental read behavior for custom upload and other external audiences

**Glossary:**

* **Custom Upload**: Importing an audience into Adobe Experience Platform from a CSV file using the Audience Portal *(product-specific)*
* **Audience Portal**: The Adobe Experience Platform Audience Portal, which allows you to import an audience using a CSV file *(product-specific)*
* **Incremental read**: A recurring option of the Read audience activity that processes only the profiles that entered the audience since the last run; for custom upload and other external audiences it is not functionally supported today *(product-specific)*

**Guardrails:**

* During the custom upload process, you specify the CSV attribute to use as the identity and the profile identity it maps to, establishing a link between the audience data and the profile.
* If the CSV file contains an identity value not found in the profile, a new profile is created with that identity value.
* You select one column as the primary identity and specify its identity namespace; the other columns become attributes of the audience, used for personalization and not connected to the profile.
* The CSV file must have 26 columns or fewer and be 1 GB or smaller, and the column names in the first row cannot contain spaces or dashes.
* A sandbox can contain up to 50 audiences imported from CSV files, not counting Federated Audience Composition audiences.
* By default, an imported audience expires after 30 days, and the expiration is reset if the audience is updated; a custom expiration can be set.
* For custom upload (CSV) and other external audiences, Incremental read is not functionally supported today; on each recurrence the entire audience is retrieved, regardless of the Incremental read toggle setting.

**Terminology:**

* Canonical name: Custom Upload — Acronym: n/a — variants: CSV upload, custom upload audience
* Synonyms: "Custom upload" = "CSV upload"

**FAQ:**

* **Q: How do I import a custom audience?** — Import it from a CSV file using the Adobe Experience Platform Audience Portal.
* **Q: What happens if a CSV identity value is not in the profile?** — A new profile is created with that identity value.
* **Q: Is Incremental read supported for custom upload audiences?** — No; it is not functionally supported today, and the entire audience is retrieved on each recurrence regardless of the toggle setting.

**Personas:**

* **marketer:** Can import an audience from a CSV file using the Adobe Experience Platform Audience Portal. During the custom upload process, specify the CSV attribute to use as the identity and the profile identity it maps to. The page states that custom upload audiences cannot be used to target inbound channel actions, including in-app messages and web or code-based experiences. Where: "Guardrails".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Specify the CSV attribute to use as the identity and the profile identity it maps to.
* **Success check:** A new profile is created when the CSV file contains an identity value not found in the profile.
* **Next:** Learn more about audience guardrails: About Adobe Experience Platform audiences (audience/target-audiences.md)

+++

<!-- ai-section-version: 1 | source-hash: 22efd8e5 -->
