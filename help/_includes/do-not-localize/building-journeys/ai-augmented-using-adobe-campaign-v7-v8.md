---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use Adobe Campaign v7/v8 as an action in Journey Optimizer journeys to send emails, push notifications, and SMS via Campaign Transactional Messaging.

**Intents:**

* Add a Campaign v7/v8 action to a journey to send transactional messages
* Map journey event or datasource fields to the Campaign message payload parameters
* Combine Campaign v7/v8 actions with the native channels of the Action activity in the same journey
* Configure the dedicated action required for the Campaign v7/v8 integration

**Glossary:**

* **Campaign Transactional Messaging**: Adobe Campaign v7/v8 capability used to send emails, push notifications, and SMS from Journey Optimizer through a dedicated action *(product-specific)*
* **Action parameters**: The section where all the fields expected in the message payload are displayed and mapped to fields from the event or the data source *(product-specific)*

**Guardrails:**

* The connection between Journey Optimizer and the Campaign instance is set up by Adobe at provisioning time; contact Adobe to enable it.
* A dedicated action must be configured before Campaign v7/v8 actions are available in the journey palette.
* Campaign v7/v8 actions cannot be used with Read Audience or Audience Qualification activities.
* Access to Campaign Transactional Messaging and the required permissions are prerequisites, along with a Campaign v7/v8 instance provisioned and connected to Journey Optimizer by Adobe.

**Terminology:**

* Canonical name: Adobe Campaign v7/v8 — Acronym: n/a — variants: Campaign v7, Campaign v8
* Do not confuse: "Campaign v7/v8 actions" (can be used alongside the native channels of the Action activity) ≠ "Campaign Standard actions" (cannot be combined with the native channels of the Action activity in the same journey)

**FAQ:**

* **Q: Who sets up the connection between Journey Optimizer and Campaign v7/v8?** — Adobe sets up the connection at provisioning time; you must contact Adobe to have it configured.
* **Q: Can Campaign v7/v8 actions be combined with the native channels of the Action activity in the same journey?** — Yes, Campaign v7/v8 actions can be used alongside the native channels of the Action activity; this is not the case for Campaign Standard actions.
* **Q: Can Campaign v7/v8 actions be used with Read Audience or Audience Qualification activities?** — No, Campaign v7/v8 actions cannot be used with Read Audience or Audience Qualification activities.
* **Q: How do I map journey data to the Campaign message payload?** — In the Action parameters, map each expected payload field to the corresponding field from the journey event or datasource, similar to custom actions.

+++
