---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to set up the email header parameters in a channel configuration — the From, Reply to, Error, and optional Sender fields — and how to manage reply handling and email forwarding.

**Intents:**

* Configure the From name, From email prefix, Reply to name, Reply to email, and Error email prefix in a channel configuration
* Set optional Sender headers when the transmitting entity differs from the From author
* Manage where reply emails, out-of-office notifications, and challenge responses are received
* Set up an email forward process for the delegated subdomain
* Understand the formatting rules for email prefixes

**Glossary:**

* **From name / From email prefix**: The sender name and email address used for communications; the prefix uses the selected delegated subdomain *(product-specific)*
* **Reply to name / Reply to email**: The name and address used when the recipient clicks Reply in their email client *(product-specific)*
* **Error email prefix**: The address that receives asynchronous bounces (ISP errors after a few days), out-of-office notifications, and challenge responses *(product-specific)*
* **Sender headers (Sender name / Sender email)**: Optional fields identifying the party responsible for transmitting the message when it differs from the From author; adds a Sender SMTP header *(product-specific)*
* **Delegated subdomain**: The subdomain used to send the email and used for SPF, DKIM, and DMARC checks *(product-specific)*

**Guardrails:**

* When editing an email configuration, you cannot add new profile attributes to header parameters; you must create a new channel configuration.
* For From email prefix and Error email prefix, values must begin with a letter (A-Z) and can only contain alphanumeric characters, plus underscore `_`, dot `.`, and hyphen `-`.
* Sender name and Sender email must be configured together — both filled in or both empty; filling in only one prevents journeys and campaigns from being published with this channel configuration.
* If both Sender fields are empty, or the resolved Sender is identical to From, no Sender header is added.
* The Sender address is not used for SPF, DKIM, or DMARC alignment (only format validation is performed); those checks continue to rely on the From fields and the delegated subdomain.
* If Sender headers are configured and personalization does not resolve to a value for a recipient, the message is not delivered to that recipient.
* The Reply to email must be a valid, correctly formatted address on a subdomain with a valid MX record, otherwise email configuration processing fails.
* Forwarding is set up by Adobe (contact Adobe Customer Care) and can take 3 to 4 days; the forward email address domain cannot match any subdomain delegated to Adobe.
* There can be only one forward email address per subdomain; configurations sharing a subdomain must use the same forward email address.
* If forwarding is not enabled, emails sent directly to the From email address are discarded by default.

**Terminology:**

* Canonical name: Header parameters — Acronym: n/a — variants: sender headers, header fields
* Synonyms: "From" = "author of the message"; "Sender" = "agent responsible for transmitting the message"
* Do not confuse: "From" (author) ≠ "Sender" (transmitting party) ≠ "Reply to email" (address receiving replies) ≠ "Error email" (address receiving asynchronous bounces, out-of-office notifications, and challenge responses)

**FAQ:**

* **Q: Which address receives asynchronous bounces and out-of-office notifications?** — The Error email prefix address; out-of-office notifications and challenge responses are received there rather than on the Reply to email.
* **Q: Can I fill in only the Sender name or only the Sender email?** — No. Both must be configured together, or both left empty; filling only one prevents publishing journeys and campaigns with the configuration.
* **Q: Does the Sender field affect SPF, DKIM, or DMARC?** — No. Only format validation is performed on the Sender address; SPF, DKIM, and DMARC continue to rely on the From fields and the delegated subdomain.
* **Q: Why did my email configuration fail on submission?** — The MX record is likely not configured for the subdomain of the Reply to email address; contact your administrator or use an address with a valid MX record.
* **Q: How do I forward emails received for the delegated subdomain?** — Contact Adobe Customer Care to set up a forward process, providing the forward email address, sandbox name, and configuration name or subdomain; setup can take 3 to 4 days.

+++

<!-- ai-section-version: 1 | source-hash: 76351813 -->
