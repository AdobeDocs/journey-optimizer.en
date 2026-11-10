---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the Load file activity to target an Orchestrated campaign audience from an external CSV or TXT file at execution time, without ingesting the file into Adobe Experience Platform.

**Intents:**

* Target an Orchestrated campaign audience from an external CSV or TXT file without ingesting it into Adobe Experience Platform.
* Define column mappings, data types, NULL handling, and error-processing policies for the file structure.
* Create a File-type target dimension to resolve recipients from an uploaded file.
* Create a channel configuration for file-based delivery.
* Configure the sample file and the target file for the Load file activity.
* Connect the Load file activity to downstream message activities on the campaign canvas.

**Glossary:**

* **Load file activity**: a Data Management activity used to work with profiles and data stored in an external file on the Orchestrated campaign canvas to define the campaign audience *(product-specific)*
* **File-type target dimension**: a Profile Target Dimension with Dimension source set to File, letting Orchestrated campaigns resolve recipients from an uploaded file instead of an Adobe Experience Platform schema *(product-specific)*
* **Sample file**: the file used to configure Columns and Formatting for the Load file activity; its data is not imported as the campaign audience *(product-specific)*
* **Target file**: the CSV or TXT file containing the audience to target, loaded when the campaign runs *(product-specific)*
* **Reject management**: the Load file activity settings that define how the activity behaves when errors occur during file processing *(product-specific)*

**Guardrails:**

* You can upload up to 50 MB per file.
* Only flat-structure CSV and TXT files are supported.
* Uploaded data is used when the campaign runs and is not stored as an Adobe Experience Platform dataset.
* The Load file activity is not meant to be used in a scheduled campaign, because uploaded files have a short data lifetime.
* Standard profile-based channel configurations do not work with a file-based audience; use a channel configuration that targets the File-type dimension for any message activity that follows a Load file activity.
* The identity namespace and identity field path for a File-type target dimension cannot be changed after the target dimension is saved.

**Prerequisites and permissions:**

* Users must be assigned the **Manage File in Orchestrated Campaigns** permission to use the Load file activity in an Orchestrated campaign.
* A **Profile Target Dimension** of type **File** must be created, from **Administration** > **Configurations** > **Campaign Target Dimension**, before the Load file activity can resolve recipients from an uploaded file.
* A channel configuration that uses the File-type target dimension (enabled for Orchestrated campaigns under Execution details) must be created for the message activity that follows the Load file activity.

**Applicability:**

* Does not apply to: Healthcare Shield (the Load file activity is currently not available for use with it).

**Terminology:**

* Canonical name: Load file activity — variants: Load file
* Synonyms: none
* Do not confuse: "sample file" (used to configure columns and formatting; its data is not imported as the campaign audience) ≠ "target file" (the file loaded as the campaign audience when the campaign runs)

**FAQ:**

* **Q: What is the Load file activity used for?** — It is a Data Management activity used to work with profiles and data stored in an external file to define an Orchestrated campaign audience, without ingesting the file into Adobe Experience Platform.
* **Q: Is the uploaded file stored in Adobe Experience Platform?** — No, uploaded data is used when the campaign runs and is not stored as an Adobe Experience Platform dataset.
* **Q: What permission is required to use the Load file activity?** — The Manage File in Orchestrated Campaigns permission.
* **Q: What must be set up before using the Load file activity?** — A File-type Profile Target Dimension and a channel configuration that targets that dimension.
* **Q: Can the Load file activity be used in a scheduled campaign?** — It is not meant to be used in a scheduled campaign, because uploaded files have a short data lifetime.
* **Q: Is the Load file activity available with Healthcare Shield?** — No, it is currently not available for use with Healthcare Shield.

**Examples:**

* Value remapping on a column can replace `True`/`False` with `1`/`0`.
* A Date column can use the date format `yyyy/mm/dd`.
* The identity field path for a File-type target dimension can be `email`, if the uploaded files include an `email` column.

**Best practices:**

* Ensure the target file follows the same format, column structure, and number of columns as the sample file.

**Related pages:**

* For limits on channel and canvas activities: Guardrails and limitations (orchestrated/guardrails.md)
* For assigning the Manage File in Orchestrated Campaigns permission: Manage users and roles (administration/permissions.md)
* For creating the File-type target dimension: Learn more about target dimensions (orchestrated/target-dimension.md)
* For creating the channel configuration used after a Load file activity: Learn more about channel configurations for Orchestrated campaigns (orchestrated/channel-config.md)
* For connecting the Load file activity to downstream activities: Learn how to orchestrate campaign activities (orchestrated/orchestrate-activities.md)

**Personas:**

* **marketer:** Can target an Orchestrated campaign audience from an external CSV or TXT file without ingesting it into Adobe Experience Platform. Can configure column mappings, data types, NULL handling, and error-processing policies, then select the target file to load when the campaign runs. The page states that files can be up to 50 MB and only flat-structure CSV and TXT files are supported. Where: "Configure the Load file activity".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Add a Load file activity to your Orchestrated campaign canvas.
* **Success check:** Rows that fail validation are rejected and logged before the campaign runs.
* **Previous:** Create a File-type target dimension before adding the Load file activity: Create your Targeting dimension (orchestrated/target-dimension.md); Create a channel configuration for file-based delivery before connecting a message activity: Configure your Channel configuration (orchestrated/channel-config.md)
* **Next:** Connect the Load file activity to downstream activities on the campaign canvas: Create Orchestrated campaigns with Adobe Journey Optimizer (orchestrated/orchestrate-activities.md)

+++

<!-- ai-section-version: 1 | source-hash: 916f7b54 -->
