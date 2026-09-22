---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the mobile app push notification channel in Journey Optimizer, covering permissions, datasets, adding iOS and Android push credentials, creating a Push channel configuration (with optional App id personalization), configuring the Adobe Journey Optimizer extension, and testing with a journey and event.

**Intents:**

* Set up the tags user permissions (Property and Company rights) required for push configuration
* Add mobile app push credentials in Journey Optimizer for iOS and Android
* Create a Push channel configuration and associate marketing actions and platforms
* Personalize the App id to drive multiple apps from a single channel configuration
* Configure the Adobe Journey Optimizer extension in the mobile property
* Test the mobile app by creating a schema, event, and journey that triggers a push notification

**Glossary:**

* **Push credential**: The mobile app push credential registered in Journey Optimizer that authorizes Adobe to send push notifications on your behalf *(product-specific)*
* **Channel configuration**: A configuration (i.e. message preset) created so you can send push notifications from Journey Optimizer *(product-specific)*
* **Apply to all sandboxes**: A push credential option that makes the credentials available across all sandboxes; sandbox-specific credentials for the same Platform and App ID pair take precedence *(product-specific)*
* **App id personalization**: Storing each App id on the profile and using a single channel configuration, with a Handlebars expression evaluated per recipient at send time *(product-specific)*
* **Adobe Journey Optimizer extension**: The Adobe Experience Platform Mobile SDK extension that powers push notifications, collects user push tokens, and manages interaction measurement *(product-specific)*

**Guardrails:**

* Push configuration must be performed by an expert user; you may need to assign the full set of permissions to a single product profile or share permissions between the app developer and the Adobe Journey Optimizer administrator.
* Property rights require the Approve, Develop, Manage Environments, Manage Extensions, and Publish rights; Company rights require Manage App Configurations and Manage Properties.
* Only .p8 Apple Push Notification keys are supported; use another Apple Developer account if you reach the .p8 key limit.
* The iOS Key ID is a 10 character string assigned during creation of the p8 auth key.
* Configuration names must begin with a letter (A-Z), can only contain alpha-numeric characters, and may also use underscore, dot, and hyphen characters.
* When personalizing the App id, Journey Optimizer does not check that push credentials exist for every value the expression may return; ensure credentials exist for every possible app id and test with representative profiles, or recipients whose resolved app id has no matching credentials will not be delivered as expected.
* When push tracking events are ingested into the CJM Push Tracking Experience Event dataset, missing mapped fields cause warnings that appear as 'failed' in batch status but reflect partial ingestion success and do not prevent ingestion of valid data.

**Terminology:**

* Canonical name: Mobile app push notification channel — Acronym: n/a — variants: push channel, mobile push
* Synonyms: "channel configuration" = "message preset"
* Do not confuse: "Push credentials" (authorize Adobe to send push) ≠ "Channel configuration" (message preset used to send push)
* Do not confuse: "APNs" (Apple, iOS) ≠ "FCM" (Firebase Cloud Messaging, Android)

**FAQ:**

* **Q: What credentials do I provide for iOS?** — A .p8 Apple Push Notification Authentication Key file, the Key ID (a 10 character string), and the Team ID; only .p8 keys are supported.
* **Q: What do I provide for Android?** — The App ID (usually the package name from your build.gradle file) and the FCM push credentials.
* **Q: How can one channel configuration serve multiple apps?** — Store each App id on the profile and use App id personalization; the Handlebars expression is evaluated per recipient at send time, and you must ensure push credentials exist for every possible app id.
* **Q: What does the Apply to all sandboxes option do?** — It makes the push credentials available across all sandboxes; sandbox-specific credentials for the same Platform and App ID pair take precedence.
* **Q: How do I test the push setup?** — Create an XDM Experience Event schema, set up a Rule Based event, build a journey with the event and a Push activity, then use the Test toggle to trigger an event and send the notification.

+++

<!-- ai-section-version: 1 | source-hash: de791ae7 -->
