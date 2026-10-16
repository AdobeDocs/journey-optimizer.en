---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains what the errors returned when you create relational schemas (manually, from a DDL file, or from an Excel template) and enable datasets for Orchestrated campaigns mean, and how to fix each family of errors.

**Intents:**

* Find the cause and the fix for a CJMDMS error returned during relational schema creation or dataset enablement
* Identify which error family (files and formats, Excel template, primary key and version descriptor, relationships, identity, dataset enablement, names and permissions) an error belongs to
* Check the file limits that apply to a DDL or Excel upload
* Check what a relational schema needs before a dataset can be enabled for Orchestrated campaigns

**Glossary:**

* **CJMDMS**: Prefix of the schema and dataset error codes; an error code is the prefix, an error number, and an HTTP status (for example CJMDMS-100130-413) *(product-specific)*
* **Primary key**: Field a schema must have; a schema without one returns the primary key errors *(product-specific)*
* **Version descriptor**: Field of a schema that must be selected and marked as required; it must be a field of type datetime, long, or int, and it cannot be the primary key field *(product-specific)*
* **Identity field**: Field of type String that a schema used for targeting needs, mapped to a valid identity namespace *(product-specific)*
* **Relationship**: Link between two schemas, defined by a source schema, a source property, a destination schema, and a cardinality *(product-specific)*
* **Cardinality**: Type of a relationship; the supported cardinalities are 1-1, 1-N, or N-1 *(product-specific)*
* **Customer dataset**: Dataset type required to enable the orchestrated campaign extension; it must not be enabled for Profile *(product-specific)*

**Guardrails:**

* A DDL file larger than 10 MB returns CJMDMS-100130-413. The fix is to reduce its size or split it into several files.
* A file can define up to 200 tables (CJMDMS-100127-400, 100240-400). The fix is to reduce the number of tables or split the file into several uploads.
* The DDL accepts only **[!UICONTROL CREATE TABLE]** statements.
* The Excel template must be in .xlsx format.
* A file name can contain only letters, numbers, underscores, hyphens, or spaces, and a single supported extension.
* A field cannot be both the primary key and the version descriptor.
* The version descriptor must be a field of type datetime, long, or int.
* The source and destination properties of a relationship must have the same type.
* A schema that is already associated with a dataset enabled for Orchestrated campaigns returns CJMDMS-100139-400 or 100166-400. The fix is to use the existing dataset or create another schema.
* Change data capture cannot be enabled when data is already ingested in the dataset. A new dataset with change data capture enabled must be created before ingesting data (CJMDMS-100228-400).

**Terminology:**

* Canonical name: Orchestrated campaigns — variants: orchestrated campaign extension (as in the error messages)
* Do not confuse: "primary key" ≠ "version descriptor" (a field cannot be both)

**FAQ:**

* **Q: How is an error code structured?** — The prefix **CJMDMS**, followed by an error number and an HTTP status, for example CJMDMS-100130-413.
* **Q: Why is my DDL file rejected?** — Depending on the message: the file is larger than 10 MB (CJMDMS-100130-413), defines more than 200 tables (100127-400, 100240-400), has malformed syntax (100126-422, 100186-400, 100187-400), contains a statement other than **[!UICONTROL CREATE TABLE]** (100189-400, 100201-400), defines a table or column twice or a column without a valid data type (100184-400, 100185-400, 100188-400), or refers to a table that is not defined (100256-400, 100258-400).
* **Q: What does a schema need to be used for Orchestrated campaigns?** — A primary key, a version descriptor marked as required, and an identity field of type String mapped to a valid identity namespace.
* **Q: Why can I not enable my dataset for Orchestrated campaigns?** — Common causes: the dataset is not a customer dataset or is enabled for Profile (CJMDMS-100131-400, 100132-400), its schema is not supported (100134-400, 100227-400), or the schema is already associated with a dataset enabled for Orchestrated campaigns (100139-400, 100166-400). If the message says enablement is in progress (100133-400), wait, then try again. If the dataset is already enabled (100169-400), no action is needed.
* **Q: What should I do when I get a 403 error?** — Your user does not have the permission named in the message (CJMDMS-100108-403, 100138-403, 100178-403, 100179-403). Ask your administrator to grant it on your product profile.
* **Q: What does an Excel template error mean?** — The template is not complete or not consistent: a required sheet, structure, or header is missing (100229-400, 100230-400, 100232-400, 100233-400), or the table sheets and the schema summary do not match, a table sheet misses required fields, or a schema name is used twice (100234-400, 100235-400, 100236-400).

**Troubleshooting:**

* **Files and formats**: errors when the uploaded DDL or Excel file is too large, has too many tables, or is not in a supported format. CJMDMS-100129-400 and 100237-400 ("The file format {format} is not supported. Please use a supported file format and try again." and "Invalid file format. Only .xlsx files are supported."): upload a DDL file, or the Excel template in .xlsx format.
* **Excel template**: errors when the template that defines the schemas is not complete or not consistent. Fix: download the template again and check the sheet names, the sheet structure, and the required headers named in the message. Make the sheets consistent with the summary sheet and give each schema a unique name.
* **Primary key and version descriptor**: errors when a schema has no primary key (CJMDMS-100157-400, 100207-400, 100244-400) or no version descriptor (100197-400, 100242-400, 100259-400, 100261-400), when the primary key field is used as the version descriptor (100181-400, 100268-400), or when the version descriptor type is not datetime, long, or int (100182-400, 100260-400). Fix: add a primary key, select one field (for example lastmodified) as the version descriptor and mark it as required, and use another field, for example a datetime column such as lastmodified, when the primary key was selected.
* **Relationships**: CJMDMS-100163-400 (invalid cardinality), 100162-400, 100196-400, 100263-400 (incomplete or inconsistent relationship), 100159-400, 100161-400 (source or destination schema missing from the payload). Fix: use 1-1, 1-N, or N-1; set the source schema and property, the destination schema, and the cardinality; add the missing schema or remove the relationship.
* **Identity**: CJMDMS-100203-400 to 100206-400 (identity field missing, of the wrong type, or without a valid namespace) and 100210-400 ("Identity namespace {namespace} on field {fields} present in schema {schema} is not found."). Fix: add or correct the identity field; for 100210-400, check the namespace in Adobe Experience Platform, then select it again.
* **Names and permissions**: CJMDMS-100146-400, 100168-400 (a schema with this title already exists). Fix: choose a different schema title.

**Related pages:**

* Files and formats and Identity errors, see also: Guardrails and limitations (orchestrated/guardrails.md)
* DDL upload and relationships: Create relational schemas using a DDL file (orchestrated/file-upload-schema.md)
* Primary key, version descriptor, and dataset enablement: Create relational schemas manually (orchestrated/manual-schema.md)
* Change data capture: Ingest data (orchestrated/ingest-data.md)
* Overview of data modeling: Data modeling overview (orchestrated/gs-schemas.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)
* Permissions for 403 errors: Built-in Roles (administration/ootb-permissions.md)

+++

<!-- ai-section-version: 1 | source-hash: ef324bcf -->
