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
* A file can define up to 200 tables (CJMDMS-100127-400). For CJMDMS-100240-400, the upload exceeds the schema limit shown in the message. In both cases, the fix is to reduce the number of tables or split the file into several uploads.
* The DDL accepts only **[!UICONTROL CREATE TABLE]** statements.
* The Excel template must be in .xlsx format.
* A file name can contain only letters, numbers, underscores, hyphens, or spaces, and a single extension.
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
* **Q: Why is my DDL file rejected?** — Depending on the message: the file is larger than 10 MB (CJMDMS-100130-413), defines more than 200 tables (100127-400, 100240-400), has malformed content (100126-422), columns that are not properly defined (100186-400), or a table that is not properly defined (100187-400), contains syntax that is not supported (100189-400) or a statement other than **[!UICONTROL CREATE TABLE]** (100201-400), defines tables with the same name (100184-400), columns with the same name in a table (100185-400), or a column with a missing or invalid data type (100188-400), or has a relationship that refers to tables that are not defined in the DDL (100256-400). Each code has its own fix, listed under Troubleshooting.
* **Q: What does a schema need to be used for Orchestrated campaigns?** — A primary key, a version descriptor marked as required, and an identity field of type String mapped to a valid identity namespace.
* **Q: Why can I not enable my dataset for Orchestrated campaigns?** — Common causes: the dataset is not a customer dataset (CJMDMS-100131-400: select or create a customer dataset, then enable it for Orchestrated campaigns from the **[!UICONTROL Datasets]** settings) or is enabled for Profile (100132-400: select or create a customer dataset that is not enabled for Profile, then enable it from the **[!UICONTROL Datasets]** settings), its schema is not supported (100134-400, 100227-400: create a relational schema with a primary key, a version descriptor, and an identity field, then create a new dataset on it), or the schema is already associated with a dataset enabled for Orchestrated campaigns (100139-400) or with datasets (100166-400): use an existing dataset, or create another schema. If the message says enablement is in progress (100133-400), wait a few minutes for the enablement to complete, then try again. If the extension is already enabled on the dataset (100169-400), continue by ingesting data into the dataset.
* **Q: What should I do when I get a 403 error?** — Your user does not have the permission needed to access the resource (CJMDMS-100108-403), or the permission named in the message on a dataset (100138-403), on a schema (100178-403), or on datasets (100179-403). Ask your administrator to grant you the permission named in the message, such as **[!DNL Manage datasets]** or **[!DNL Manage schemas]**, in your product profile.
* **Q: What does an Excel template error mean?** — The template is not complete or not consistent: a required sheet, structure, or header is missing (100229-400, 100230-400, 100232-400, 100233-400), or the table sheets and the schema summary do not match, a table sheet misses required fields, or a schema name is used twice (100234-400, 100235-400, 100236-400).

**Troubleshooting:**

* **Files and formats**:
    * **CJMDMS-100129-400** ("The file format {format} is not supported. Please use a supported file format and try again."): upload a DDL file, or the Excel template in .xlsx format.
    * **CJMDMS-100237-400** ("Invalid file format. Only .xlsx files are supported."): download the provided Excel template, save your schema definitions in it, and upload it in .xlsx format.
    * **CJMDMS-100130-413**: the DDL file is larger than 10 MB. Reduce its size, or split it into several files.
    * **CJMDMS-100127-400**: the file defines more than the 200 tables allowed. Reduce the number of tables, or split the file into several uploads.
    * **CJMDMS-100240-400**: the upload exceeds the schema limit shown in the message. Reduce the number of tables, or split the file into several uploads.
    * **CJMDMS-100126-422**: the DDL content is malformed. Fix the syntax shown in the message, then upload the file again.
    * **CJMDMS-100186-400**: correct the column definitions shown in the message, making sure each column has a name and a data type, then upload the file again.
    * **CJMDMS-100187-400**: check that each table in the DDL is a complete **[!UICONTROL CREATE TABLE]** statement with its columns and at least one primary key, then upload the file again.
    * **CJMDMS-100189-400**: the DDL accepts only **[!UICONTROL CREATE TABLE]** statements, so remove the syntax shown in the message, then upload the file again.
    * **CJMDMS-100201-400**: remove the statements other than **[!UICONTROL CREATE TABLE]**, then upload the file again.
    * **CJMDMS-100184-400**: remove the duplicate tables listed in the message, or give each table a unique name, then upload the file again.
    * **CJMDMS-100185-400**: remove the duplicate columns listed in the message, or give each column of the table a unique name, then upload the file again.
    * **CJMDMS-100188-400**: set a supported data type for the column named in the message.
    * **CJMDMS-100256-400**: add a **[!UICONTROL CREATE TABLE]** statement for each missing table listed in the message.
    * **CJMDMS-100258-400**: add the missing entities listed in the message to the sheet named in the message.
    * **CJMDMS-100265-400**: use only letters, numbers, underscores, hyphens, or spaces, and a single extension in the file name.
    * **CJMDMS-100269-400**: add one of the allowed extensions listed in the message to the file name.
* **Excel template**: download the template again where indicated.
    * **CJMDMS-100229-400**: add the required sheet named in the message.
    * **CJMDMS-100230-400**: the template must have the schema summary sheet and at least one table definition sheet. Add the schema summary sheet and at least one table definition sheet if either is missing.
    * **CJMDMS-100232-400**: check the structure of the sheet named in the message.
    * **CJMDMS-100233-400**: add the header named in the message to the sheet.
    * **CJMDMS-100235-400**: rename the table sheet so it matches a schema name listed in the summary sheet, or correct the schema name in the summary sheet.
    * **CJMDMS-100236-400**: complete all the required columns of the sheet named in the message.
    * **CJMDMS-100234-400**: give each schema a unique name in the schema summary.
* **Primary key and version descriptor**:
    * **CJMDMS-100157-400**: open the schema from the **[!UICONTROL Data Management]** > **[!UICONTROL Schema]** menu, assign a **[!UICONTROL Primary Key]** to a field, and save. Then create the dataset again or upload the file again.
    * **CJMDMS-100207-400**: open the schema from the **[!UICONTROL Data Management]** > **[!UICONTROL Schema]** menu, assign a **[!UICONTROL Primary Key]** to a field, and save. Then create the dataset again.
    * **CJMDMS-100244-400**: define a primary key column in the sheet named in the message, then upload the file again.
    * **CJMDMS-100197-400**, **CJMDMS-100242-400**: open the schema, select one field (for example lastmodified) as the **[!UICONTROL Version Descriptor]**, and mark it as required.
    * **CJMDMS-100259-400**: set the version identifier on exactly one column of the sheet, then upload the file again.
    * **CJMDMS-100261-400**: mark the column named in the message as required in the sheet.
    * **CJMDMS-100181-400**: the primary key field is also used in the version descriptor. Use another field, for example a datetime column such as lastmodified.
    * **CJMDMS-100268-400**: the version identifier is set on the primary key column. Select another column, of one of the allowed types listed in the message.
    * **CJMDMS-100182-400**: select a version descriptor field of type datetime, long, or int.
    * **CJMDMS-100260-400**: select a column of one of the allowed types listed in the message (datetime, long, or int).
* **Relationships**:
    * **CJMDMS-100163-400** (invalid cardinality): use one of the supported cardinalities: 1-1, 1-N, or N-1.
    * **CJMDMS-100162-400** (incomplete relationship): set the source schema, the source property, and the destination schema.
    * **CJMDMS-100196-400**: select source and destination properties that have the same type.
    * **CJMDMS-100263-400**: the source property is a primary key, so update the relationship of the schema named in the message to the 1-1 cardinality.
    * **CJMDMS-100159-400**: add the source schema, or remove the relationship.
    * **CJMDMS-100161-400**: add the destination schema, or remove the relationship.
* **Identity**:
    * **CJMDMS-100203-400**: add an identity field of type String, mapped to a valid identity namespace.
    * **CJMDMS-100204-400**: the identity field is not of the type shown in the message. A schema used for targeting needs an identity field of type String, so correct the type of the field.
    * **CJMDMS-100205-400**: map the identity field named in the message to a valid identity namespace.
    * **CJMDMS-100206-400**: use an identity field of type String, mapped to a valid identity namespace.
    * **CJMDMS-100210-400** ("Identity namespace {namespace} on field {fields} present in schema {schema} is not found."): check in Adobe Experience Platform that the namespace exists, then select an existing identity namespace for the field named in the message.
* **Names and permissions**:
    * **CJMDMS-100146-400**: a schema with this title already exists. Choose a different schema title.
    * **CJMDMS-100168-400**: the request contains several schemas with the same title. Give each schema a unique title.

**Related pages:**

* Files and formats and Identity errors, see also: Guardrails and limitations (orchestrated/guardrails.md)
* DDL upload and relationships: Create relational schemas using a DDL file (orchestrated/file-upload-schema.md)
* Primary key, version descriptor, and dataset enablement: Create relational schemas manually (orchestrated/manual-schema.md)
* Change data capture: Ingest data (orchestrated/ingest-data.md)
* Overview of data modeling: Data modeling overview (orchestrated/gs-schemas.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)
* Permissions for 403 errors: Built-in Roles (administration/ootb-permissions.md)

+++

<!-- ai-section-version: 1 | source-hash: 3b082150 -->
