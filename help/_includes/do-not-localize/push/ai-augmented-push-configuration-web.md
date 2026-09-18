---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the web push notification channel in Journey Optimizer, covering permissions, datasets, the pushNotifications property and VAPID keys, adding Web push credentials, creating a Push channel configuration, the sendPushSubscription command, and testing the setup.

**Intents:**

* Set up the tags user permissions (Property and Company rights) required for web push configuration
* Add Web app push credentials in Journey Optimizer using a VAPID public and private key
* Create a Push channel configuration and associate marketing actions and platforms
* Configure the pushNotifications property and the sendPushSubscription command in the Web SDK
* Test the web push implementation before sending to profiles

**Glossary:**

* **Web push notification channel**: The Journey Optimizer channel used to send push notifications to users' browsers *(product-specific)*
* **Push credential**: The app push credential registered in Journey Optimizer that authorizes Adobe to send push notifications on your behalf *(product-specific)*
* **Channel configuration**: A configuration (i.e. message preset) created so you can send push notifications from Journey Optimizer *(product-specific)*
* **VAPID keys**: The public and private keys required to configure the Web app push credentials *(product-specific)*
* **pushNotifications property**: A Web SDK property that controls how push notifications are handled by your web application *(product-specific)*
* **sendPushSubscription command**: A Web SDK command that registers user push subscriptions with Adobe Experience Platform and maintains their subscription status *(product-specific)*

**Guardrails:**

* Push configuration must be performed by an expert user; you may need to assign the full set of permissions to a single product profile or share permissions between the app developer and the Adobe Journey Optimizer administrator.
* Property rights require the Approve, Develop, Manage Environments, Manage Extensions, and Publish rights; Company rights require Manage App Configurations and Manage Properties.
* Configuration names must begin with a letter (A-Z), can only contain alpha-numeric characters, and may also use underscore, dot, and hyphen characters.
* The pushNotifications property must be configured in the Web SDK, and VAPID keys must be generated, before adding Web app push credentials.
* When selecting the App id in the channel configuration, use the same App id as the push credential configured earlier.
* When push tracking events are ingested into the CJM Push Tracking Experience Event dataset, missing mapped fields cause warnings that appear as 'failed' in batch status but reflect partial ingestion success and do not prevent ingestion of valid data.

**Terminology:**

* Canonical name: Web push notification channel — Acronym: n/a — variants: web push, web push notifications
* Synonyms: "channel configuration" = "message preset"
* Do not confuse: "Push credentials" (authorize Adobe to send push) ≠ "Channel configuration" (message preset used to send push)
* Do not confuse: "Warnings" (logged, do not prevent ingestion) ≠ ingestion failure (valid data is still ingested)

**FAQ:**

* **Q: What keys do I need to add Web push credentials?** — A VAPID public key and private key, along with the App ID; VAPID keys must be generated beforehand.
* **Q: Where do I add Web push credentials?** — Under Channels > Push settings > Push credentials, then Create push credential and select the Web platform.
* **Q: What does the sendPushSubscription command do?** — It registers user push subscriptions with Adobe Experience Platform, tracking which users have opted in and maintaining their subscription status.
* **Q: Which schemas and datasets are used?** — CJM Push Profile Schema/Dataset (Register Push Token) and CJM Push Tracking Experience Event Schema/Dataset (track interactions and provide reporting data).
* **Q: Where can I find the testing workflow for web push?** — Refer to the mobile app push notification configuration documentation, which provides a testing workflow applicable to both mobile and web push channels.

+++

<!-- ai-section-version: 1 | source-hash: dfe98e49 -->
