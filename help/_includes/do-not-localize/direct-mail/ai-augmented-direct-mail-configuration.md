---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to set up a file routing configuration and a direct mail channel configuration so that extraction files are exported to the right server for your direct mail provider to retrieve.

**Intents:**

* Create a file routing configuration that defines the export server
* Choose a server type: Amazon S3, SFTP, Azure, or Data Landing Zone
* Encrypt the exported file with a PGP/GPG encryption key
* Generate a Base64-encoded OpenSSH private key for SFTP SSH key authentication
* Create a direct mail configuration that references a file routing configuration
* Select the file format and column separator for the exported file

**Glossary:**

* **File routing configuration**: The configuration that specifies the server where the extraction file is exported and, if needed, encrypts the file *(product-specific)*
* **Direct mail configuration**: The channel configuration that defines the file formatting and references a file routing configuration *(product-specific)*
* **Data Landing Zone**: A supported server type provisioned as one container per sandbox for all Adobe Experience Platform customers *(product-specific)*
* **PGP/GPG encryption key**: The key pasted into the configuration to encrypt the exported file *(product-specific)*
* **Marketing action**: A selection that associates consent policies with messages using the configuration *(product-specific)*

**Guardrails:**

* Creating a file routing configuration requires the Manage file routing built-in permission.
* If no file routing configuration exists, you cannot create a direct mail configuration.
* Supported server types are Amazon S3, SFTP, Azure, and Data Landing Zone.
* SFTP SSH key authentication requires a Base64-encoded OpenSSH private key; a PPK-format key must be converted with PuTTY.
* Configuration names must begin with a letter (A-Z) and can contain only alphanumeric characters plus underscore, dot, and hyphen.
* A file routing configuration cannot be selected in a configuration until it has the Active status; a Save as draft configuration is not selectable.
* Direct mail files are generated only at export time and older exports are not stored indefinitely; configure a file routing option (SFTP or cloud storage) for longer backup.
* Duplicate rows where all values in the row are the same are automatically removed from the file.
* The file split threshold can be set to any value between 1 and 200,000 records per file, after which another file is created for the remaining records.

**Terminology:**

* Canonical name: Direct mail configuration — Acronym: n/a — variants: direct mail channel configuration, direct mail surface
* Synonyms: "file routing configuration" = "file routing config"
* Do not confuse: "file routing configuration" (defines the export server) ≠ "direct mail configuration" (defines file formatting and references the file routing configuration)
* Do not confuse: "Active" (usable status) ≠ "Save as draft" (not selectable in a configuration)

**FAQ:**

* **Q: What must I create before a direct mail configuration?** — A file routing configuration; without one you cannot create a direct mail configuration.
* **Q: Which server types are supported?** — Amazon S3, SFTP, Azure, and Data Landing Zone.
* **Q: What permission do I need to create file routing?** — The Manage file routing built-in permission.
* **Q: How do I encrypt the exported file?** — Paste your encryption key into the PGP/GPG encryption key field.
* **Q: Why can I not select my file routing configuration?** — It is likely saved as a draft; a file routing configuration must have the Active status to be selectable.
* **Q: Which file formats are available?** — CSV or Text delimited, and Text delimited lets you choose a tabulation, semicolon, pipe, or ampersand column separator.

+++

<!-- ai-section-version: 1 | source-hash: 040d4c43 -->
