---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create a Mobile message channel configuration in Journey Optimizer by setting the message type, mobile configuration, sender number, subdomain, and execution field to send SMS, RCS, and MMS messages.

**Intents:**

* Create a Mobile message channel configuration
* Select the SMS Type (Marketing or Transactional) for the configuration
* Associate a Mobile configuration and a sender number
* Enable URL shortening by selecting a subdomain
* Override the priority phone number with the SMS Execution Field
* Save the channel configuration as draft and resume it later

**Glossary:**

* **Channel configuration**: The Mobile message configuration you create to send SMS, RCS, and MMS messages from Journey Optimizer *(product-specific)*
* **SMS Type**: The message category of the configuration, either Marketing or Transactional *(product-specific)*
* **Marketing**: SMS Type for promotional messages that require user consent *(product-specific)*
* **Transactional**: SMS Type for non-commercial messages such as order confirmations, password resets, or delivery updates *(product-specific)*
* **Mobile configuration**: The provider API credentials association selected for the channel configuration *(product-specific)*
* **Sender number**: The number used for your communications *(product-specific)*
* **Subdomain**: An item selected to use the URL shortening function in Mobile messages *(product-specific)*
* **SMS Execution Field**: A field in the Execution dimension section used to select, among profile attributes, the phone number to use in priority when several numbers are available *(product-specific)*

**Guardrails:**

* Configuration names must begin with a letter (A-Z) and can contain only alpha-numeric characters plus underscore, dot, and hyphen.
* Transactional messages can be sent to profiles who have unsubscribed from marketing communications, but only in specific contexts.
* To select a subdomain, you must have previously configured at least one SMS/RCS/MMS subdomain.
* By default, Journey Optimizer uses the phone number specified in the general settings at the sandbox level; updating the SMS Execution Field overrides the default value for the journeys and campaigns using this configuration.
* The custom dataset for inbound schema must be XDM ExperienceEvent and include at least the Message interaction details, Message Execution Details, and Message Profile Details field groups; the schema and dataset must be enabled for Profile.

**Terminology:**

* Canonical name: Mobile message channel configuration — Acronym: n/a — variants: channel configuration
* Do not confuse: "Marketing" (promotional; requires user consent) ≠ "Transactional" (non-commercial messages)
* Do not confuse: "Processing" (status while checks run) ≠ "Active" (status once checks are successful; ready to deliver messages)
* Do not confuse: "Mobile configuration" (provider API credentials association) ≠ "channel configuration" (the Mobile message configuration created on this page)

**FAQ:**

* **Q: What is the difference between the Marketing and Transactional SMS Type?** — Marketing is for promotional messages that require user consent; Transactional is for non-commercial messages such as order confirmations, password resets, or delivery updates.
* **Q: Can Transactional messages reach profiles who unsubscribed from marketing?** — Yes, but only in specific contexts.
* **Q: Why is no subdomain available to select?** — You must have previously configured at least one SMS/RCS/MMS subdomain before a subdomain can be selected.
* **Q: What does the SMS Execution Field do?** — It selects the phone number to use in priority among profile attributes; updating it overrides the default sandbox-level number for the journeys and campaigns using this configuration.
* **Q: What do the Processing and Active statuses mean?** — After you submit, the configuration displays with the Processing status; once the checks are successful it gets the Active status and is ready to deliver messages.

+++

<!-- ai-section-version: 1 | source-hash: 32fb415b -->
