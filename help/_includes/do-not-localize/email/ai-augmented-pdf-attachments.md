---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to attach static PDF files to Journey Optimizer emails, and recipient-specific (personalized) PDF files for API-triggered campaigns, along with the applicable format, count, size, and per-profile volume limits.

**Intents:**

* Attach a static PDF file to an email in a journey or campaign
* Attach recipient-specific (personalized) PDF files through an API-triggered campaign
* Understand the PDF attachment count, size, and per-profile volume limits
* Set up the Data Landing Zone container and API payload for personalized attachments
* Raise the attachment size limit with the PDF Attachments add-on

**Glossary:**

* **Static PDF attachment**: A single PDF file attached to an email that is the same for every recipient *(product-specific)*
* **Personalized PDF attachment**: A recipient-specific PDF file (for example an invoice, boarding pass, contract, or shipping label) attached per recipient in an API-triggered campaign *(product-specific)*
* **Data Landing Zone (DLZ)**: The attachment-specific cloud storage container (retrieved with `type=ajoemailattachments`) where personalized PDFs are uploaded and then referenced from the API payload; the only supported storage location for them *(product-specific)*
* **PDF Attachments add-on**: A purchasable add-on that raises the combined personalized-attachment size limit from 5 MB to 10 MB *(product-specific)*

**Guardrails:**

* Up to 6 messages with a PDF attachment per profile per year, whether the attachment is static or personalized.
* Maximum 5 MB per attachment; for emails with personalized attachments, all static and personalized PDFs share a combined 5 MB limit by default. The PDF Attachments add-on raises the combined personalized limit to 10 MB.
* Up to five PDF attachments per email, counting static and personalized together — for example, one static PDF plus up to four personalized PDFs.
* Only the PDF format is allowed for attachments.
* Personalized PDF attachments are supported only for transactional API-triggered email campaigns.
* Personalized PDFs must be uploaded to the attachment-specific Data Landing Zone container; it is currently the only supported storage location for them.
* Data Landing Zone automatically deletes files after seven days — keep the files available until delivery and any retries are complete.
* Personalized PDF attachments are supported for High Throughput campaigns in the primary region and are not supported during regional failover.
* A PDF attachment is not retained when the message is saved as a content template — reattach the file on any new email created from that template.

**Terminology:**

* Canonical name: PDF attachment — Acronym: n/a — variants: static PDF attachment, personalized PDF attachment
* Synonyms: "Data Landing Zone" = "DLZ"
* Do not confuse: "static PDF attachment" (same file for all recipients) ≠ "personalized PDF attachment" (per-recipient file, API-triggered campaigns only)

**FAQ:**

* **Q: How many PDF attachments can one email include?** — Up to five, counting static and personalized together (for example, one static plus up to four personalized).
* **Q: What is the maximum PDF attachment size?** — 5 MB per attachment; with personalized attachments, all static and personalized PDFs share a combined 5 MB limit by default, which the PDF Attachments add-on raises to 10 MB.
* **Q: How many PDF-attachment messages can a single profile receive?** — Up to 6 per profile per year, whether the attachments are static or personalized.
* **Q: Are personalized PDF attachments available for any email?** — No. They are supported only for transactional API-triggered email campaigns, and for High Throughput campaigns in the primary region; they are not supported during regional failover.
* **Q: Where must personalized PDF files be stored?** — In the attachment-specific Data Landing Zone container (retrieved with `type=ajoemailattachments`) and referenced in the API payload; it is the only supported storage location, and files are automatically deleted after seven days.
* **Q: Is the PDF attachment kept when I save the email as a content template?** — No, it is not retained; you must reattach the file on any new email created from the template.

+++

<!-- ai-section-version: 1 | source-hash: a5a74b99 -->
