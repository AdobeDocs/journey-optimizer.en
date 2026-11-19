---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to migrate email content, journeys, and transactional emails from another marketing platform into Journey Optimizer using a dedicated workspace that converts them into Journey Optimizer content templates, journeys, and API-triggered campaigns.

**Intents:**

* Set up a connection from Journey Optimizer to a source marketing platform for API-based import
* Import email content by uploading HTML files or browsing from a connection
* Import journeys by uploading screenshots or browsing from a connection
* Import transactional emails from a connection to create API-triggered campaigns
* Select the configuration, template, tracking settings, and identity namespace of an imported transactional email before migrating it
* Map personalization placeholders and add a subject line to imported email content
* Track migration progress using KPIs, statuses, and filters in the workspace overview

**Glossary:**

* **Migration workspace**: A dedicated workspace, accessible from the Journey Optimizer homepage, that imports existing email content and journeys and converts them into Journey Optimizer content templates and journeys *(product-specific)*
* **Connection**: A configured link between Journey Optimizer and a source platform's API, used to browse and import content or journeys without exporting files manually *(product-specific)*
* **Authentication Method**: How Journey Optimizer authenticates to the source system, either API Key (a single credential sent with each request) or OAuth 2.0 (a token-based protocol) *(product-specific)*
* **Content template**: The Journey Optimizer object that imported email content is converted into and made available for use in journeys *(product-specific)*
* **Campaigns tab**: The tab of the migration workspace where transactional emails imported from a connection are listed and migrated *(product-specific)*
* **API-triggered campaign**: The Journey Optimizer object that an imported transactional email is converted into, which you can publish and trigger through an API call *(product-specific)*
* **Identity namespace**: The namespace selected in the Audience section of an imported transactional email, used to identify the recipients, for example an email address or a customer ID *(product-specific)*
* **Action items pane**: The pane where each unresolved activity of an imported journey is resolved, such as selecting a channel configuration and content template for message steps, or selecting the audience for Audience activities *(product-specific)*

**Guardrails:**

* This capability is only available for a set of organizations (Limited Availability); to gain access, contact your Adobe representative.
* Migrating content and journeys requires the following permissions: Manage Campaigns, Manage Journeys, Manage Message, Manage Segments, Manage Library items, View and Manage sandboxes, and Manage AJO integration configuration.
* A connection is not required if you upload HTML files or screenshots instead of importing through an API.
* Transactional emails can only be imported by browsing from a connection to your source platform; the Campaigns tab does not support file upload.
* Connection Name must start with a letter and can only contain letters, numbers, underscores, or hyphens, between 4 and 50 characters long (hard limit).
* Client ID, Client Secret, and Token URL are required for OAuth 2.0 connections.
* Email content HTML files must be in .html or .htm format and no larger than 10 MB (hard limit).
* Journey screenshots must be in .png, .jpg, .gif, or .webp format and no larger than 5 MB (hard limit).

**Terminology:**

* Canonical name: Migration workspace — Acronym: n/a — variants: workspace, migration workspace
* Synonyms: "Base API URL" = "root URL of the source system's API"
* Do not confuse: "In Progress" (KPI for items still being reviewed or mapped) ≠ "Needs review" (imported item status and Status filter value) ≠ "Migrated" (successfully converted item) ≠ "Failed" (item that could not be migrated)

**FAQ:**

* **Q: Do I need a connection to import content?** — No. A connection is not required if you upload HTML files or screenshots; a connection is needed only to import content or journeys through an API.
* **Q: What file formats and sizes are accepted?** — Email content must be an .html or .htm file no larger than 10 MB, and journey screenshots must be .png, .jpg, .gif, or .webp no larger than 5 MB.
* **Q: What happens to the source personalization syntax when I import an email?** — The workspace converts the source scripting syntax to Handlebars syntax automatically, and you map each personalization placeholder to the corresponding profile attribute.
* **Q: How do I know which authentication method to choose?** — Choose API Key to send a single credential with each request, or choose OAuth 2.0 to use a token-based protocol better suited to enterprise and third-party APIs; OAuth 2.0 also requires Client ID, Client Secret, and Token URL.
* **Q: What does a transactional email become after migration?** — It becomes an API-triggered campaign in Journey Optimizer, which you can review and publish when you are ready to start sending.
* **Q: What do I need to set before migrating a transactional email?** — Select the configuration, choose a template, review the tracking settings for email opens and clicks, and select the identity namespace under Audience.
* **Q: How can I track the status of imported items?** — The workspace overview shows KPIs for Total emails or Total journeys, In Progress, Migrated, and Failed, and you can combine Status, Created, and Updated filters to narrow the list.

**Personas:**

* **marketer:** Can import email content by uploading HTML files or browsing from a connection to the source platform. Can add a Subject line and map each personalization placeholder to a profile attribute, then select Migrate. The page states that email content HTML files must be in .html or .htm format and no larger than 10 MB. Where: "Import Email content".
* **marketer (transactional emails):** Can import transactional emails by browsing from a connection in the Campaigns tab, then select the configuration, template, tracking settings, and identity namespace, and select Migrate to create an API-triggered campaign. Where: "Import transaction email campaign".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** In the workspace, select Manage connections.
* **Success check:** Once the connection is set up, the advanced menu becomes available to delete it or mark it as default for future imports.
* **Previous:** For the required roles and permissions before using the migration workspace: Manage users and roles (administration/permissions.md)
* **Next:** To learn more about content templates after migrating email content: Use content templates (content-management/use-content-templates.md); To learn more about creating journeys after migrating journeys: Create your first journey (building-journeys/journey-gs.md)

+++

<!-- ai-section-version: 1 | source-hash: ba41d81d -->
