---
solution: Journey Optimizer
product: journey optimizer
title: Relational schema and dataset errors
description: Learn what common errors mean when you create relational schemas and enable datasets for Orchestrated campaigns in Adobe Journey Optimizer, and how to fix them
feature: Data Model, Datasets
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, orchestrated campaigns, CJMDMS
version: Campaign Orchestration
---
# Relational schema and dataset errors {#relational-schema-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you create relational schemas (manually, from a DDL file, or from an Excel template) and enable datasets for Orchestrated campaigns.

>[!ENDSHADEBOX]

Schema and dataset errors use the prefix **CJMDMS**, followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Files and formats {#files}

These errors occur when you upload a DDL or Excel file to create schemas, and the file is too large, has too many tables, or is not in a supported format.

See also [Guardrails and limitations](guardrails.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100129-400** | The file format {format} is not supported. Please use a supported file format and try again. | Upload a DDL file, or the Excel template in .xlsx format. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100237-400** | Invalid file format. Only .xlsx files are supported. | Download the provided Excel template, save your schema definitions in it, and upload it in .xlsx format. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100130-413** | The DDL content size limit of {limit} has been exceeded. Please reduce the DDL size and try again. | Reduce the DDL file to 10 MB or less, or split it into several files and upload them one by one. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100127-400** | The entity limit of {limit} has been exceeded. Please reduce the number of entities and try again. | Reduce the DDL file to 200 tables or fewer, or split it into several files and upload them one by one. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100240-400** | Schema limit has exceeded {limit} | Reduce the number of tables in the file to stay within the limit shown in the message, or split the file into several uploads. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100126-422** | The DDL content is malformed: {content}. Please fix the DDL and try again. | Correct the DDL syntax shown in the message, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100186-400** | The columns in the DDL are not properly defined, {error}. Please update the DDL and try again. | Correct the column definitions shown in the message, making sure each column has a name and a data type, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100187-400** | The table the the DDL are not properly defined. Please update the DDL and try again. | Check that each table in the DDL is a complete **[!UICONTROL CREATE TABLE]** statement with its columns and at least one primary key, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100189-400** | Unsupported syntax error, {error}. Please update the DDL and try again. | Remove the syntax shown in the message and keep only **[!UICONTROL CREATE TABLE]** statements, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100201-400** | Only 'CREATE TABLE' statements are supported. Please verify your DDL statement type. | Remove the statements other than **[!UICONTROL CREATE TABLE]** from the DDL, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100184-400** | Duplicate table names found in the DDL, {tables}. Please update the DDL and try again. | Remove the duplicate tables listed in the message, or give each table a unique name, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100185-400** | Duplicate column names {columns} found in table {table}. Please update the DDL and try again. | Remove the duplicate columns listed in the message, or give each column of the table a unique name, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100188-400** | The data type for column {column} in table {table} is missing or invalid. Please update the DDL and try again. | Set a supported data type for the column and table named in the message, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100256-400** | Entities referenced in relationships are missing from the DDL: {missingEntities}. Please define CREATE TABLE for them to the DDL and try again. If the problem persists, contact Adobe Customer Care. | Add a **[!UICONTROL CREATE TABLE]** statement for each missing table listed in the message, then upload the file again. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100258-400** | The entities {entities} are missing from the sheet {sheet} but are referenced in the sheet {referencedSheet}. Please correct this in the Excel file and try again. If the problem persists, contact Adobe Customer Care. | Add the missing entities listed in the message to the sheet named in the message, then upload the Excel file again. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100265-400** | File name {filename} is invalid. Filename must contain only letters, numbers, underscores (_), hyphens (-), or spaces, and include a single extension. | Rename the file using only letters, numbers, underscores, hyphens, or spaces, and a single extension, then upload it again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100269-400** | File extension is missing. Please use one of the allowed extensions: {allowedFileExtensions} | Add one of the allowed extensions listed in the message to the file name, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |

## Excel template {#excel}

These errors occur when the Excel template that defines your schemas is not complete or not consistent.

See also [Create relational schemas using a DDL file](file-upload-schema.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100229-400** | The required sheet {name} is missing from the schema upload template. Please check that the file format is correct and try again. | Download the template again, and add the sheet named in the message. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100230-400** | The schema template must include at least one table definition sheet, along with the schema summary sheet. | Download the template again, and add the schema summary sheet and at least one table definition sheet if either is missing. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100232-400** | Invalid structure detected in the sheet: {sheet} | Download the template again, and compare the structure of the sheet named in the message with the template. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100233-400** | Missing required header {header} in sheet {sheet}. Please check all required headers are present and try again. | Add the header named in the message to the sheet named in the message, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100235-400** | The table sheet {sheet} does not match any schema name listed in the summary sheet. Please check for consistency. | Rename the table sheet so it matches a schema name listed in the summary sheet, or correct the schema name in the summary sheet. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100236-400** | Some required fields are missing in the sheet {sheet}. Please review and complete all necessary columns. | Complete all the required columns of the sheet named in the message, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100234-400** | Duplicate schema names found in the schema summary: {schema}. Each schema name must be unique. | Give each schema listed in the schema summary a unique name, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |

## Primary key and version descriptor {#keys}

These errors occur when a schema does not have a primary key and a version descriptor, or when they are not defined as required.

See also [Create relational schemas manually](manual-schema.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100157-400** | The schema {schema} does not contain a primary key. Please update the schema and try again. | Open the schema from the **[!UICONTROL Data Management]** > **[!UICONTROL Schema]** menu, assign a **[!UICONTROL Primary Key]** to a field, and save. Then create the dataset again or upload the file again. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100207-400** | The schema {schema} linked to dataset {dataset} is not supported for orchestrated campaigns due to the absence of a primary key descriptor. Please update schema {schema} and try again. | Open the schema from the **[!UICONTROL Data Management]** > **[!UICONTROL Schema]** menu, assign a **[!UICONTROL Primary Key]** to a field, and save. Then create the dataset again. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100244-400** | No primary key column found in the sheet {sheet} | Define a primary key column in the sheet named in the message, then upload the file again. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100197-400** | The schema {schema} linked to dataset {dataset} is not supported for orchestrated campaigns due to the absence of a version descriptor. | Open the schema, select one field (for example lastmodified) as the **[!UICONTROL Version Descriptor]**, and mark it as required. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100242-400** | The schema {schema} does not have version descriptor. Please update the schema and try again. | Open the schema, select one field (for example lastmodified) as the **[!UICONTROL Version Descriptor]**, and mark it as required. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100259-400** | There must be exactly one column with a non-empty versionIdentifier in sheet {sheet}. Please correct this in the Excel file and try again. If the problem persists, contact Adobe Customer Care. | Set the version identifier on exactly one column of the sheet, then upload the file again. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100261-400** | Please select the required field for the column: {column} as version descriptor is selected for the column in sheet: {sheet} | Mark the column named in the message as required in the sheet. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100181-400** | Primary key field {fields} must not be included in the version descriptor. Please update schema {schema} and try again. | Use another field as the version descriptor, for example a datetime column such as lastmodified. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100268-400** | Version Identifier can't be set on the primary key field {column} in sheet {sheet}, please select other field from one of the allowed types: {allowed} | Select another column, of one of the allowed types listed in the message, as the version identifier. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100182-400** | The version descriptor field {fields} must be of type {type}. Please update schema {schema} and try again. | Select a field of type datetime, long, or int as the version descriptor. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100260-400** | The versionIdentifier column {column} in sheet {sheet} must have one of the allowed types: {allowed}. Found: {xdmType} | Select a column of type datetime, long, or int as the versionIdentifier column of the sheet. [Learn more](manual-schema.md#schema-attributes) |

## Relationships {#relationships}

These errors occur when you define relationships between schemas.

See also [Create relational schemas using a DDL file](file-upload-schema.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100163-400** | The cardinality {cardinality} for one or more relationships is invalid. The supported cardinalities are {allowed}. Please update the relationship and try again. | Set the cardinality of each relationship to 1-1, 1-N, or N-1. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100162-400** | One or more relationships are incomplete. Each relationship must include a sourceSchema, sourceProperty, and destinationSchema. Please update the relationship and try again. | Set the source schema, the source property, and the destination schema of each relationship. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100196-400** | SourceProperty type and destinationProperty type mismatch in relationship in schema {schema}. Please update schema {schema} and try again. | Select a source property and a destination property that have the same type. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100263-400** | Relationships where the source property is a primary key must have a 'one-to-one' type. Please update the relationship(s) in schema {schema} and try again. | Set the relationships of the schema named in the message that have a primary key as source property to the 1-1 cardinality. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100159-400** | The source schema {schema} referenced in the relationship is missing from the payload. Please update the relationship and try again. | Add the source schema to the request, or remove the relationship. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100161-400** | The destination schema {schema} referenced in the relationship is missing from the payload. Please update the relationship and try again. | Add the destination schema to the request, or remove the relationship. [Learn more](file-upload-schema.md#relationships) |

## Identity {#identity}

These errors occur when a schema does not have an identity field mapped to an identity namespace.

See also [Guardrails and limitations](guardrails.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100203-400** | Identity key property {fields} not found for schema {schema}. | Add an identity field of type String to the schema, and map it to a valid identity namespace. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100204-400** | Identity descriptor field {fields} must be of type {type}. Please update schema {schema}. | Set the type of the identity field named in the message to String, the type that a schema used for targeting requires. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100205-400** | Identity descriptor field {fields} must have a valid namespace. Please update schema {schema}. | Map the identity field named in the message to a valid identity namespace. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100206-400** | Identity descriptor field {fields} must be of type {type} only. Please update schema {schema}. | Use an identity field of type String, mapped to a valid identity namespace. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100210-400** | Identity namespace {namespace} on field {fields} present in schema {schema} is not found. | Check in Adobe Experience Platform that the namespace exists, then select an existing identity namespace for the field named in the message. [Learn more](manual-schema.md#schema-attributes) |

## Dataset enablement {#dataset}

These errors occur when you enable a dataset for Orchestrated campaigns.

See also [Enable the dataset for Orchestrated campaigns](manual-schema.md#enable).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100131-400** | The dataset {dataset} is not a customer dataset, so you cannot enable the orchestrated campaign extension. Please select a customer dataset and try again. | Select or create a customer dataset, then enable it for Orchestrated campaigns from the **[!UICONTROL Datasets]** settings. [Learn more](manual-schema.md#enable) |
| **CJMDMS-100132-400** | The dataset {dataset} is enabled for Profile. You can only use orchestrated campaigns on customer datasets that are not Profile enabled. Please select a supported dataset and try again. | Select or create a customer dataset that is not enabled for Profile, then enable it for Orchestrated campaigns from the **[!UICONTROL Datasets]** settings. [Learn more](manual-schema.md#enable) |
| **CJMDMS-100134-400** | The schema for the dataset {dataset} is not supported for orchestrated campaigns. Please use a compatible schema and try again. | Create a relational schema with a primary key, a version descriptor, and an identity field, then create a new dataset on it. [Learn more](manual-schema.md#schema) |
| **CJMDMS-100227-400** | The schema {schema} linked to dataset {dataset} is not supported for orchestrated campaign:  a 'record' type schema is missing. Please add it and try again. | Create a relational schema with a primary key, a version descriptor, and an identity field, then create a new dataset on it. [Learn more](manual-schema.md#schema) |
| **CJMDMS-100139-400** | Schema {schema} is already associated with a orchestrated campaign enabled dataset {dataset}. | Use the existing dataset, or create another schema for the new dataset. [Learn more](manual-schema.md#dataset) |
| **CJMDMS-100166-400** | One or several datasets {dataset} are already associated with the schema {schema}. | Use one of the existing datasets, or create another schema. [Learn more](manual-schema.md#dataset) |
| **CJMDMS-100169-400** | The orchestrated campaign extension is already enabled on dataset {dataset}. | Continue by ingesting data into the dataset. [Learn more](manual-schema.md#enable) |
| **CJMDMS-100133-400** | The orchestrated campaign extension enablement for dataset {dataset} is in progress. Please try again later. | Wait a few minutes for the enablement to complete, then try again. [Learn more](manual-schema.md#enable) |
| **CJMDMS-100228-400** | CDC is not supported on dataset {dataset} because data is already ingested in dataset. | Create a new dataset with change data capture enabled, and ingest your data into it. [Learn more](ingest-data.md#cdc) |

## Names and permissions {#names}

These errors occur when a name is already used, or when your user does not have the permission needed on schemas or datasets.

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100146-400** | Schema with title {schema} already exists. Please update the schema and try again. | Choose a different schema title. [Learn more](manual-schema.md#schema) |
| **CJMDMS-100168-400** | One or several schemas with the title {title} already exist in the request payload. Please update the request payload and try again. | Give each schema in the request a unique title. [Learn more](manual-schema.md#schema) |
| **CJMDMS-100108-403** | You do not have the required permissions to access this resource. Check your permissions or contact your administrator. | Check that your role has the permission for the schema or dataset, such as **[!DNL View schemas]** or **[!DNL View datasets]** to read and **[!DNL Manage schemas]** or **[!DNL Manage datasets]** to change, and that it includes the current sandbox. Ask your administrator to add what is missing. [Learn more](../administration/ootb-permissions.md) |
| **CJMDMS-100138-403** | You do not have {permission} permission on dataset {resource}. Please check your permissions or contact your administrator | Check the permission named in the message against the permissions of your role on datasets, such as **[!DNL Manage datasets]** to change or **[!DNL View datasets]** to read, and ask your administrator to add it. If the dataset carries an access label, your role must also include it. [Learn more](../administration/ootb-permissions.md) |
| **CJMDMS-100178-403** | You do not have {permission} permission on schema {resource}. Please update your permissions or contact your administrator. | Check the permission named in the message against the permissions of your role on schemas, such as **[!DNL Manage schemas]** to change or **[!DNL View schemas]** to read, and ask your administrator to add it. If the schema contains fields with an access label, your role must also include that label. [Learn more](../administration/ootb-permissions.md) |
| **CJMDMS-100179-403** | You do not have {permission} permission on datasets. Please update your permissions or contact your administrator. | Check the permission named in the message against the permissions of your role on datasets, such as **[!DNL Manage datasets]** to change or **[!DNL View datasets]** to read, and ask your administrator to add it. [Learn more](../administration/ootb-permissions.md) |

## Related topics {#related}

* [Data modeling overview](gs-schemas.md)
* [Create relational schemas manually](manual-schema.md)
* [Create relational schemas using a DDL file](file-upload-schema.md)
* [Ingest data](ingest-data.md)
* [Guardrails and limitations](guardrails.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/orchestrated/ai-augmented-relational-schema-errors.md}}
