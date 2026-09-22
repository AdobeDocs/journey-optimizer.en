---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to define email settings in a channel configuration, including email type, subdomain, IP pool, list unsubscribe, header parameters, BCC, seed list, retries, URL tracking, and execution address.

**Intents:**

* Choose the email type (Marketing or Transactional) for a channel configuration
* Select the subdomain and IP pool used to send emails
* Enable list unsubscribe and set header parameters (From, Reply to, Error, optional Sender)
* Enable BCC email and configure sending to suppressed email addresses
* Add a seed list and configure email retry parameters
* Set the execution (delivery) address used to determine which email address to send to

**Glossary:**

* **[!UICONTROL Marketing]** email type: Promotional email that requires user consent *(product-specific)*
* **[!UICONTROL Transactional]** email type: Non-commercial email (for example order confirmation, password reset, delivery information) that can be sent to profiles who unsubscribed from marketing communications, only in specific contexts *(product-specific)*
* **BCC email**: An identical (blind carbon copy) of sent emails delivered to a BCC inbox for compliance or archival purposes *(product-specific)*
* **Seed list**: A list of internal seed addresses automatically included in deliveries at execution time, which receive a copy of the message for assurance purposes *(product-specific)*
* **Suppression list**: The list into which email addresses marked as hard bounces, soft bounces, and spam complaints are automatically collected and excluded from sending *(product-specific)*
* **Execution fields / Delivery address**: The field used to determine which email address to use from the profile service in priority when several addresses are available *(product-specific)*

**Guardrails:**

* Before creating an email channel configuration, set up your sending subdomains and create at least one IP pool.
* Configuration changes: for batch journeys, a change does not apply to batch execution already started and is picked up at the next recurrence or new execution; for transactional messages, the change is picked up immediately for the next communication (up to a five-minute delay).
* You must choose a valid channel configuration matching the email type category you selected.
* You cannot proceed with configuration creation while the selected IP pool is under edition (Processing status) and has never been associated with the selected subdomain; save as draft and retry once the IP pool has the Success status.
* For non-production environments, Adobe does not create out-of-the-box test subdomains nor grant access to a shared sending IP pool.
* The BCC email address must use a subdomain that has a valid MX record configuration, otherwise the email configuration processing will fail.
* Sending to suppressed email addresses is only available for the Transactional email type, is disabled by default, and applies only to addresses suppressed due to spam complaint.
* The seed list feature currently applies to the email channel only, and only one seed list can be selected at a time.
* Email retry period must be an integer value within range: minimum 6 hours for marketing emails, minimum 10 minutes for transactional emails, and a maximum of 84 hours (5040 minutes) for both email types; the default retry time period is 84 hours (3.5 days).

**Terminology:**

* Canonical name: email settings — Acronym: n/a — variants: email channel configuration settings, email configuration
* Synonyms: "BCC email" = "blind carbon copy"; "execution fields" = "delivery address"
* Do not confuse: "[!UICONTROL Marketing]" email type (requires user consent) ≠ "[!UICONTROL Transactional]" email type (non-commercial, sendable to unsubscribed profiles in specific contexts)
* Do not confuse: IP pool "[!UICONTROL Processing]" status (under edition, blocks configuration creation) ≠ "[!UICONTROL Success]" status (ready to use)

**FAQ:**

* **Q: What is the difference between the Marketing and Transactional email types?** — Marketing is for promotional email and requires user consent; Transactional is for non-commercial email, can be sent to profiles who unsubscribed from marketing, and can only be sent in specific contexts.
* **Q: What is the default email retry time period and can I change it?** — The default is 84 hours (3.5 days); you can adjust it within the allowed range (minimum 6 hours for marketing, minimum 10 minutes for transactional, maximum 84 hours / 5040 minutes for both).
* **Q: Can I send emails to addresses on the suppression list?** — Only transactional messages, and only to addresses suppressed due to spam complaint, by enabling the Send to suppressed email addresses option, which is disabled by default.
* **Q: How many seed lists can I select?** — Only one seed list can be selected at a time, and the feature currently applies to the email channel only.
* **Q: Why does my BCC email configuration fail?** — The BCC address must use a subdomain with a valid MX record configuration; if the MX record is not configured, the email configuration processing fails.
* **Q: When do updated configuration settings take effect?** — For batch journeys, at the next recurrence or new execution; for transactional messages, immediately for the next communication (up to a five-minute delay).

+++

<!-- ai-section-version: 1 | source-hash: 2ddfab47 -->
