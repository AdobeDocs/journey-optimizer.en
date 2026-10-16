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
hide: true
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
| **CJMDMS-100129-400**, **100237-400** | The file format {format} is not supported. Please use a supported file format and try again.<br/>Invalid file format. Only .xlsx files are supported. | Upload a DDL file, or the Excel template in .xlsx format. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100130-413** | The DDL content size limit of {limit} has been exceeded. Please reduce the DDL size and try again. | The DDL file is larger than 10 MB. Reduce its size, or split it into several files. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100127-400**, **100240-400** | The entity limit of {limit} has been exceeded. Please reduce the number of entities and try again.<br/>Schema limit has exceeded {limit} | A file can define up to 200 tables. Reduce the number of tables, or split the file into several uploads. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100126-422**, **100186-400**, **100187-400** | The DDL content is malformed: {content}. Please fix the DDL and try again.<br/>The columns in the DDL are not properly defined, {error}. Please update the DDL and try again.<br/>The table the the DDL are not properly defined. Please update the DDL and try again. | The DDL is not valid. Fix the syntax shown in the message, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100189-400**, **100201-400** | Unsupported syntax error, {error}. Please update the DDL and try again.<br/>Only 'CREATE TABLE' statements are supported. Please verify your DDL statement type. | The DDL accepts only **[!UICONTROL CREATE TABLE]** statements. Remove the other statements, then upload the file again. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100184-400**, **100185-400**, **100188-400** | Duplicate table names found in the DDL, {tables}. Please update the DDL and try again.<br/>Duplicate column names {columns} found in table {table}. Please update the DDL and try again.<br/>The data type for column {column} in table {table} is missing or invalid. Please update the DDL and try again. | A table or a column is defined twice, or a column has no valid data type. Remove the duplicate, or set a supported data type. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100256-400**, **100258-400** | Entities referenced in relationships are missing from the DDL: {missingEntities}. Please define CREATE TABLE for them to the DDL and try again. If the problem persists, contact Adobe Customer Care.<br/>The entities {entities} are missing from the sheet {sheet} but are referenced in the sheet {referencedSheet}. Please correct this in the Excel file and try again. If the problem persists, contact Adobe Customer Care. | A relationship refers to a table that is not defined. Add a CREATE TABLE statement (or a sheet in the Excel template) for the missing table. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100265-400**, **100269-400** | File name {filename} is invalid. Filename must contain only letters, numbers, underscores (_), hyphens (-), or spaces, and include a single extension.<br/>File extension is missing. Please use one of the allowed extensions: {allowedFileExtensions} | The file name is not valid. Use only letters, numbers, underscores, hyphens, or spaces, and a single supported extension. [Learn more](file-upload-schema.md#ddl-upload) |

## Excel template {#excel}

These errors occur when the Excel template that defines your schemas is not complete or not consistent.

See also [Create relational schemas using a DDL file](file-upload-schema.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100229-400**, **100230-400**, **100232-400**, **100233-400** | The required sheet {name} is missing from the schema upload template. Please check that the file format is correct and try again.<br/>The schema template must include at least one table definition sheet, along with the schema summary sheet.<br/>Invalid structure detected in the sheet: {sheet}<br/>Missing required header {header} in sheet {sheet}. Please check all required headers are present and try again. | The Excel template is not valid. Download the template again, and check the sheet names, the sheet structure, and the required headers named in the message. [Learn more](file-upload-schema.md#ddl-upload) |
| **CJMDMS-100235-400**, **100236-400**, **100234-400** | The table sheet {sheet} does not match any schema name listed in the summary sheet. Please check for consistency.<br/>Some required fields are missing in the sheet {sheet}. Please review and complete all necessary columns.<br/>Duplicate schema names found in the schema summary: {schema}. Each schema name must be unique. | The schema summary and the table sheets do not match, a table sheet is missing required fields, or a schema name is used twice. Make the sheets consistent with the summary sheet, and give each schema a unique name. [Learn more](file-upload-schema.md#ddl-upload) |

## Primary key and version descriptor {#keys}

These errors occur when a schema does not have a primary key and a version descriptor, or when they are not defined as required.

See also [Create relational schemas manually](manual-schema.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100157-400**, **100207-400**, **100244-400** | The schema {schema} does not contain a primary key. Please update the schema and try again.<br/>The schema {schema} linked to dataset {dataset} is not supported for orchestrated campaigns due to the absence of a primary key descriptor. Please update schema {schema} and try again.<br/>No primary key column found in the sheet {sheet} | The schema has no primary key. Add a primary key to the schema, then create the dataset again or upload the file again. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100197-400**, **100242-400**, **100259-400**, **100261-400** | The schema {schema} linked to dataset {dataset} is not supported for orchestrated campaigns due to the absence of a version descriptor.<br/>The schema {schema} does not have version descriptor. Please update the schema and try again.<br/>There must be exactly one column with a non-empty versionIdentifier in sheet {sheet}. Please correct this in the Excel file and try again. If the problem persists, contact Adobe Customer Care.<br/>Please select the required field for the column: {column} as version descriptor is selected for the column in sheet: {sheet} | The schema needs a version descriptor. Select one field (for example lastmodified) as the version descriptor, and mark it as required. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100181-400**, **100268-400** | Primary key field {fields} must not be included in the version descriptor. Please update schema {schema} and try again.<br/>Version Identifier can't be set on the primary key field {column} in sheet {sheet}, please select other field from one of the allowed types: {allowed} | A field cannot be both the primary key and the version descriptor. Use another field as the version descriptor, for example a datetime column such as lastmodified. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100182-400**, **100260-400** | The version descriptor field {fields} must be of type {type}. Please update schema {schema} and try again.<br/>The versionIdentifier column {column} in sheet {sheet} must have one of the allowed types: {allowed}. Found: {xdmType} | The version descriptor must be a field of type datetime, long, or int. Select a field of a supported type. [Learn more](manual-schema.md#schema-attributes) |

## Relationships {#relationships}

These errors occur when you define relationships between schemas.

See also [Create relational schemas using a DDL file](file-upload-schema.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100163-400** | The cardinality {cardinality} for one or more relationships is invalid. The supported cardinalities are {allowed}. Please update the relationship and try again. | Use one of the supported cardinalities: 1-1, 1-N, or N-1. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100162-400**, **100196-400**, **100263-400** | One or more relationships are incomplete. Each relationship must include a sourceSchema, sourceProperty, and destinationSchema. Please update the relationship and try again.<br/>SourceProperty type and destinationProperty type mismatch in relationship in schema {schema}. Please update schema {schema} and try again.<br/>Relationships where the source property is a primary key must have a 'one-to-one' type. Please update the relationship(s) in schema {schema} and try again. | The relationship is not complete or not consistent. Set the source schema and property, the destination schema, and the cardinality. The source and destination properties must have the same type. [Learn more](file-upload-schema.md#relationships) |
| **CJMDMS-100159-400**, **100161-400** | The source schema {schema} referenced in the relationship is missing from the payload. Please update the relationship and try again.<br/>The destination schema {schema} referenced in the relationship is missing from the payload. Please update the relationship and try again. | The relationship refers to a schema that is not in the request. Add the missing schema, or remove the relationship. [Learn more](file-upload-schema.md#relationships) |

## Identity {#identity}

These errors occur when a schema does not have an identity field mapped to an identity namespace.

See also [Guardrails and limitations](guardrails.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100203-400**, **100204-400**, **100205-400**, **100206-400** | Identity key property {fields} not found for schema {schema}.<br/>Identity descriptor field {fields} must be of type {type}. Please update schema {schema}.<br/>Identity descriptor field {fields} must have a valid namespace. Please update schema {schema}.<br/>Identity descriptor field {fields} must be of type {type} only. Please update schema {schema}. | A schema used for targeting needs at least one identity field of type String, mapped to a valid identity namespace. Add or correct the identity field. [Learn more](manual-schema.md#schema-attributes) |
| **CJMDMS-100210-400** | Identity namespace {namespace} on field {fields} present in schema {schema} is not found. | The identity namespace named in the message cannot be found. Check the namespace in Adobe Experience Platform, then select it again. [Learn more](manual-schema.md#schema-attributes) |

## Dataset enablement {#dataset}

These errors occur when you enable a dataset for Orchestrated campaigns.

See also [Enable the dataset for Orchestrated campaigns](manual-schema.md#enable).

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100131-400**, **100132-400** | The dataset {dataset} is not a customer dataset, so you cannot enable the orchestrated campaign extension. Please select a customer dataset and try again.<br/>The dataset {dataset} is enabled for Profile. You can only use orchestrated campaigns on customer datasets that are not Profile enabled. Please select a supported dataset and try again. | Orchestrated campaigns need a customer dataset that is not enabled for Profile. Select or create a dataset that meets this condition. [Learn more](manual-schema.md#enable) |
| **CJMDMS-100134-400**, **100227-400** | The schema for the dataset {dataset} is not supported for orchestrated campaigns. Please use a compatible schema and try again.<br/>The schema {schema} linked to dataset {dataset} is not supported for orchestrated campaign:  a 'record' type schema is missing. Please add it and try again. | The schema of the dataset is not supported. Create a relational schema with a primary key, a version descriptor, and an identity field, then create a new dataset on it. [Learn more](manual-schema.md#schema) |
| **CJMDMS-100139-400**, **100166-400** | Schema {schema} is already associated with a orchestrated campaign enabled dataset {dataset}.<br/>One or several datasets {dataset} are already associated with the schema {schema}. | The schema is already associated with a dataset enabled for Orchestrated campaigns. Use the existing dataset, or create another schema. [Learn more](manual-schema.md#dataset) |
| **CJMDMS-100169-400** | The orchestrated campaign extension is already enabled on dataset {dataset}. | The dataset is already enabled. No action is needed. [Learn more](manual-schema.md#enable) |
| **CJMDMS-100133-400** | The orchestrated campaign extension enablement for dataset {dataset} is in progress. Please try again later. | Enablement is still in progress for this dataset. Wait, then try again. [Learn more](manual-schema.md#enable) |
| **CJMDMS-100228-400** | CDC is not supported on dataset {dataset} because data is already ingested in dataset. | Change data capture cannot be enabled because data is already ingested in the dataset. Create a new dataset with change data capture enabled before ingesting data. [Learn more](ingest-data.md#cdc) |

## Names and permissions {#names}

These errors occur when a name is already used, or when your user does not have the permission needed on schemas or datasets.

| Error code | Message | How to fix |
|---|---|---|
| **CJMDMS-100146-400**, **100168-400** | Schema with title {schema} already exists. Please update the schema and try again.<br/>One or several schemas with the title {title} already exist in the request payload. Please update the request payload and try again. | A schema with this title already exists. Choose a different schema title. [Learn more](manual-schema.md#schema) |
| **CJMDMS-100108-403**, **100138-403**, **100178-403**, **100179-403** | You do not have the required permissions to access this resource. Check your permissions or contact your administrator.<br/>You do not have {permission} permission on dataset {resource}. Please check your permissions or contact your administrator<br/>You do not have {permission} permission on schema {resource}. Please update your permissions or contact your administrator.<br/>You do not have {permission} permission on datasets. Please update your permissions or contact your administrator. | Your user does not have the permission named in the message. Ask your administrator to grant it on your product profile. [Learn more](../administration/ootb-permissions.md) |

## Related topics {#related}

* [Data modeling overview](gs-schemas.md)
* [Create relational schemas manually](manual-schema.md)
* [Create relational schemas using a DDL file](file-upload-schema.md)
* [Ingest data](ingest-data.md)
* [Guardrails and limitations](guardrails.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)
