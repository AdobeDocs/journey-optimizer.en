---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the errors that [!DNL Adobe Journey Optimizer] returns when you send proofs, preview content with test profiles, or create the simulated users of a journey simulation, with the cause and the fix of each.

**Intents:**

* Fix errors returned when sending a proof or previewing content with test profiles
* Fix sandbox permission errors returned for proofs and previews
* Fix errors returned when creating or editing simulated users for a journey simulation
* Recognize which error prefix belongs to proofs and previews, and which to simulated users

**Glossary:**

* **Error code**: Prefix, error number, and HTTP status, for example CJMPTS-1004-400 *(product-specific)*
* **CJMPTS**: Error prefix for proofs and previews *(product-specific)*
* **AJOTDS**: Error prefix for simulated users *(product-specific)*
* **CJMSAS**: Error prefix listed on the page; its documented error (CJMSAS-000002-429) concerns the request limit of the service *(product-specific)*
* **Test profile**: Profile flagged as a test profile; proofs and previews use test profiles only *(product-specific)*
* **Simulated user**: User created to run a journey simulation, identified by an identity namespace and an identity value *(product-specific)*

**Guardrails:**

* A proof can have up to ten recipients (hard limit). Errors CJMPTS-1021-400 and CJMPTS-1022-500 are returned when the number of recipient emails is exceeded.
* Proofs and previews use test profiles only (CJMPTS-1004-400).
* A simulation takes at least one simulated user, and no more than the maximum shown in the message (AJOTDS-000013-400, AJOTDS-000014-400).
* There is a maximum number of simulated users, given in the message of AJOTDS-000037-400.
* A simulated user needs an identity namespace and an identity value.
* Some fields cannot be modified after the simulated user is created (AJOTDS-000010-400): create a new simulated user instead.
* Only profile attributes can be used for simulated users; select attributes from the profile schema (AJOTDS-000025-400).
* The attributes of a simulated user must match the profile schema.

**Prerequisites and permissions:**

* Write permission, Read permission, or Read and Delete permissions on the sandbox, depending on the action. The errors CJMPTS-1028-403, CJMPTS-1029-403, CJMPTS-1042-403, CJMPTS-1036-401, CJMPTS-2101-403, and CJMPTS-2103-401 are returned when your user lacks the permission. Ask your administrator to grant it on your product profile.

**Applicability:**

* Proof and preview errors (CJMPTS): apply when you send a proof or preview content with test profiles.
* Simulated user errors (AJOTDS, CJMSAS): apply when you create or edit simulated users to run a journey simulation.

**Terminology:**

* Canonical name: Proof and simulation errors — variants: proof errors, preview errors, simulated user errors
* Do not confuse: CJMPTS (proofs and previews) ≠ AJOTDS (simulated users)

**FAQ:**

* **Q: How is an error code structured on this page?** — It is a prefix (CJMPTS for proofs and previews, AJOTDS for simulated users, CJMSAS), an error number, and an HTTP status. For the other error code prefixes, see the error codes reference.
* **Q: Why does my proof fail with a recipients error?** — CJMPTS-1021-400 or CJMPTS-1022-500: a proof can have up to ten recipients. Remove recipients, then send the proof again.
* **Q: Why does my proof or preview fail with a syntax error?** — CJMPTS-1300-400: a personalization expression has a syntax error. Open the alerts to find the expression, then fix it in the personalization editor.
* **Q: Why is only test profiles allowed?** — CJMPTS-1004-400: proofs and previews use test profiles only. Select profiles that are flagged as test profiles.
* **Q: What do I do on a permission error on a sandbox?** — Ask your administrator to grant the permission needed on your product profile (CJMPTS-1028-403 and related codes).
* **Q: Why can I not create a simulated user?** — Possible causes: a simulated user already exists with the combination of identity namespace and identity value (AJOTDS-000001-409), the identity namespace or value is missing (AJOTDS-000035-400, AJOTDS-000036-400, AJOTDS-000007-400), the attributes do not match the profile schema (AJOTDS-000009-400, AJOTDS-000011-400, AJOTDS-000022-400), or the maximum number of simulated users is reached (AJOTDS-000037-400).
* **Q: What do I do when a simulated user was modified by another operation?** — Refresh the page, then make your change again (AJOTDS-000002-409, AJOTDS-000001-412, AJOTDS-000007-500).

**Troubleshooting:**

* **CJMPTS-1023-500** — The message says the proof job could not continue because of a missing IMS user token. Your session is not valid for the proof. Log out and log in again, then send the proof again.
* **CJMPTS-1503-400**, **CJMPTS-1504-400** — "Message publishing is in progress." and "Errors during message publication." Wait until the publication completes, and fix the errors reported on the message.
* **AJOTDS-000001-404**, **AJOTDS-000002-404** — The simulated user cannot be found. Check the user in the inventory, or create it.
* **AJOTDS-000015-400**, **AJOTDS-000016-400**, **AJOTDS-000019-400** — The audience membership of the simulated user is incomplete or duplicated. Select each audience once, with its type.
* **CJMSAS-000002-429** — "You have reached the request limit for this service. Wait a few moments, then try again. If this continues, reduce how frequently you send requests or contact Adobe Customer Care."

**Related pages:**

* Proofs: Send proofs using test profile data (content-management/proofs.md)
* Preview and test: Get started with preview and test (content-management/preview-test.md)
* Journey simulation overview: Get started with journey simulation (building-journeys/simulate-journey-gs.md)
* Simulated users: Create and manage simulated users (building-journeys/simulate-journey.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 1 | source-hash: 462167df -->
