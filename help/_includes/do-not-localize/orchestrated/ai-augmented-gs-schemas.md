---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page outlines the key concepts and implementation steps for creating relational schemas and datasets, linking them, and ingesting data to support Orchestrated campaigns.

**Intents:**

* Understand the key concepts of dataset, schema, data model, relational data model, and relational schema in the context of Orchestrated campaigns.
* Create a relational schema either manually or by uploading a DDL file.
* Link schemas to establish relationships between entities.
* Create a dataset based on a schema and enable it for Orchestrated campaigns.
* Ingest data into Adobe Experience Platform from supported sources.

**Glossary:**

* **Dataset**: a storage and management construct for a collection of data, typically a table, that contains a schema (rows) and fields (columns); data successfully ingested into Experience Platform is stored within the data lake as datasets *(product-specific)*
* **Schema**: represents and validates the structure and format of data, providing an abstract definition of a real-world object and outlining what data should be included in each instance of that object *(product-specific)*
* **Data model**: the conceptual blueprint of normalizing your data, describing entities, their attributes, and the relationships between entities; it is logical and conceptual, not tied to a physical implementation in Orchestrated campaigns *(product-specific)*
* **Relational data model**: a data model in which data is organized into tables relating to other tables, where each table has rows (records) and columns (attributes), every table has a primary key to uniquely identify rows, and relationships between tables are expressed using foreign keys *(product-specific)*
* **Relational schema**: the formal definition of the relational data model, specifying the set of tables, the columns in each table, the constraints, and the relationships across tables *(product-specific)*

**Guardrails:**

* Organizing schemas or tables in a relational data model means structuring data into multiple tables, and each table should store one type of entity/schema.
* When creating a schema manually, the dataset must also be created and enabled manually.
* When using a DDL file, dataset creation and enablement are automatic.
* The dataset must be enabled for Orchestrated campaigns to be accessible in Adobe Journey Optimizer.

**Terminology:**

* Do not confuse: "schema" (an abstract definition of a real-world object) ≠ "data model" (the conceptual blueprint describing entities, attributes, and relationships) ≠ "relational schema" (the formal definition of the relational data model, specifying tables, columns, constraints, and relationships)
* Do not confuse: creating a schema "manually" (dataset must also be created and enabled manually) ≠ creating a schema "using a DDL file" (dataset creation and enablement are automatic)

**FAQ:**

* **Q: What is a dataset in the context of Orchestrated campaigns?** — A storage and management construct for a collection of data, typically a table, that contains a schema (rows) and fields (columns).
* **Q: What are the two ways to create a relational schema?** — Create it manually in the user interface, or upload a DDL file for faster setup.
* **Q: Does creating a schema manually also create the dataset automatically?** — No; when creating a schema manually, the dataset must also be created and enabled manually. When using a DDL file, dataset creation and enablement are automatic.
* **Q: Why link schemas?** — To establish relationships between schemas, ensure data consistency, and enable cross-entity queries, for example linking loyalty transactions to recipients or rewards to brands.
* **Q: What are the implementation steps to ingest data and create a relational schema?** — Create the relational schema (manually or using a DDL file), link schemas, create a dataset, enable it for Orchestrated campaigns, and ingest data.
* **Q: Where can data be ingested from?** — Supported sources such as SFTP, cloud storage, or databases.

**Related pages:**

* To create a relational schema in the user interface: relational schema manually (orchestrated/manual-schema.md)
* To create a relational schema by uploading a DDL file: using a DDL file (orchestrated/file-upload-schema.md)
* To establish relationships between schemas: Link schemas (orchestrated/file-upload-schema.md)
* To create a dataset based on a schema: Create Dataset (orchestrated/manual-schema.md)
* To enable the dataset for Orchestrated campaigns: Enable Orchestrated campaigns (orchestrated/manual-schema.md)
* To bring data into Adobe Experience Platform: Ingest Data (orchestrated/ingest-data.md)

**Personas:**

* **developer:** Can create a relational schema manually or by uploading a DDL file, defining tables, attributes, and relationships. Can link schemas to establish relationships between entities, such as linking loyalty transactions to recipients or rewards to brands. Can ingest data into Adobe Experience Platform from sources such as SFTP, cloud storage, or databases. Where: "Implementation steps".
* **admin:** Can create a relational schema manually in the user interface or by uploading a DDL file for faster setup. The page states that creating a schema manually requires manually creating and enabling the dataset, while a DDL file automates dataset creation and enablement. Where: "Guardrails".

**Onboarding:**

* **Level:** Experienced
* **First minimal step:** Create a relational schema manually or by uploading a DDL file.
* **Success check:** The dataset is accessible in Adobe Journey Optimizer.
* **Next:** Create a relational schema manually: Configuration steps (orchestrated/manual-schema.md); Ingest data into Adobe Experience Platform: Configuration steps (orchestrated/ingest-data.md)

+++

<!-- ai-section-version: 1 | source-hash: 70c99c09 -->
