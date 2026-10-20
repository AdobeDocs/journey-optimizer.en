---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the errors that [!DNL Adobe Journey Optimizer] returns when you build, enrich, publish, or manage an audience composition, with the cause and the fix for each error family.

**Intents:**

* Find the cause and the fix for an error returned when validating or publishing an audience composition
* Understand the parts of a composition error code: the CJMRT prefix, the error number, and the HTTP status
* Fix an incomplete activity (split, **[!UICONTROL Rank]**, **[!UICONTROL Exclude]**, filter) in a composition
* Fix enrichment dataset errors (dataset, join key, attribute, schema)
* Understand the publication limit, permission, and evaluation errors
* Know what to note and whom to contact when an error persists after the listed steps

**Glossary:**

* **Error code**: Prefix CJMRT, followed by an error number and an HTTP status, for example CJMRT-170042-400 *(product-specific)*
* **Composition**: The audience composition whose workflow is built, enriched, published, and managed *(product-specific)*
* **Enrichment dataset**: The dataset used to enrich a composition; it is configured with a source join key, an enrichment dataset join key, and at least one enrichment attribute
* **Save activity**: The activity a composition must end with
* **Error families, one per section of the page:**
* **Composition structure** (CJMRT-170002, 170004, 170006, 170005, 170003, 170007, 170008, 170001, 170039; status 400): the workflow is not valid when validating or publishing, for example it does not begin with a single audience, has disconnected activities or a loop, does not end with a Save activity, is empty, or has an invalid reference.
* **Audiences** (CJMRT-170011, 170016, 170025, 170029, 170045): no audience selected, audience name that already exists, audience not found, audience with a different merge policy than the composition, audience that cannot be used in the composition.
* **Activities** (CJMRT-170015, 170033, 170013, 170012, 170014, 170027, 170023, 170030, 170031): an activity is not configured completely (split percentages, target dimension, **[!UICONTROL Rank]** limit, empty fields, **[!UICONTROL Exclude]** values, filter key and value).
* **Enrichment** (CJMRT-170034, 170060, 170035, 170036, 170037, 170050, 170040, 170041, 170048, 170058, 170051 to 170054, 170059, 170061): enrichment dataset, join key, attribute, schema, or size problems.
* **Publication, limits, and permissions** (CJMRT-170042, 170043, 170046, 170047, 170056, 170017, 170024, 170028): publication limit, concurrent modification, performance warning, delete restriction, evaluation queue, and permissions.

**Guardrails:**

* A composition must begin with a single audience, or with a valid dataset or segment, and must end with a Save activity (add a Save activity to each path).
* Every activity must be connected to the workflow, and the workflow cannot loop back on itself.
* The percentages of the branches of a split must add up to 100.
* The limit of the **[!UICONTROL Rank]** activity must be a positive number (greater than 0).
* The audiences of a composition must use the merge policy of the composition.
* The enrichment dataset must not be empty, and it must be 1 GB or smaller (hard limit). It must be associated with a schema, and the schema must have a primary identity.
* The limit is 50 active compositions (hard limit; CJMRT-170042-400, "You have reached the limitation of 50 active compositions authorized in the inventory. You cannot add a new one."). Compositions created with federated audience composition are not counted.
* Only one composition evaluation can be queued at a time (CJMRT-170056-409).

**Terminology:**

* Canonical name: Audience composition errors — variants: composition errors

**FAQ:**

* **Q: What do the parts of a composition error code mean?** — Composition errors use the prefix CJMRT, followed by an error number and an HTTP status.
* **Q: Why does "The composition must end with a Save operation." appear?** — CJMRT-170007-400: a composition must end with a Save activity. Add a Save activity to each path.
* **Q: Why does "The composition contains disconnected operations." appear?** — CJMRT-170005-400: an activity is not connected to the workflow. Connect the disconnected activity, or delete it. For a workflow that loops back on itself (CJMRT-170003-400), remove the loop.
* **Q: Why does "Sum of all branches should be equal to 100." appear?** — CJMRT-170015-400: the percentages of the branches of a split must add up to 100. Adjust the percentages.
* **Q: Why can I not publish a new composition ("You have reached the limitation of 50 active compositions authorized in the inventory.")?** — CJMRT-170042-400: you reached the limit of 50 active compositions. Delete a published composition you no longer need, then publish the new one.
* **Q: Why does "The selected enrichment dataset is greater than 1 GB." appear?** — CJMRT-170040-400: the enrichment dataset is larger than 1 GB. Select another dataset, or reduce its size. For an empty dataset (CJMRT-170041-400), select another dataset.
* **Q: What do I do when "The composition has been modified. Please refresh the page." appears?** — CJMRT-170043-412: the composition has been modified. Refresh the page, then make your change again.
* **Q: Why can I not delete a composition (CJMRT-170047-424)?** — The audiences of the composition are used in an activation or in another audience. Remove them from there, then delete the composition.
* **Q: What do I do if the error persists after the listed steps?** — Note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or contact Adobe Support with these details. For all the support options, see the Getting support section of the error codes reference.

**Troubleshooting:**

* CJMRT-170046-413, "Publishing this composition may impact system performance. Please consider decreasing the audience size before continuing." — A warning that publishing may affect system performance. Reduce the size of the audience before you continue.
* CJMRT-170017-403 ("The client is not authorized for access.") and CJMRT-170028-403 ("Missing required permissions.") — Ask your administrator to check the permissions and the sandbox assigned to your role.
* CJMRT-170024-403 ("You don't have permission to publish this rule.  Please contact your administrator or remove unauthorized settings.") — Ask your administrator to check the permissions assigned to your role, or remove the settings your role is not allowed to use, such as audiences or attributes protected by an access label that your role does not include.
* CJMRT-170029-400, "One or more selected audiences is using a different merge policy than the one associated with the composition. Please choose a different audience." — A selected audience uses a merge policy different from the one of the composition. Select audiences that use the merge policy of the composition.
* CJMRT-170048-428 — The enrichment dataset is not associated with a schema. Associate it with a schema, or select another dataset.
* CJMRT-170058-400 — The schema of the enrichment dataset has no primary identity. Update the schema to define one, or select another dataset.
* CJMRT-170059-424 and CJMRT-170061-424 — The enrichment dataset cannot be used. Select a valid dataset, or try again later.

**Related pages:**

* Creating a composition workflow: Create a composition workflow (audience/get-started-audience-orchestration.md)
* Enrichment attributes: Leverage enrichment attributes (audience/enrichment-attributes.md)
* Composition permissions: Built-in Roles (administration/ootb-permissions.md)
* Publication limit: Journey Optimizer guardrails and limitations (start/guardrails.md)
* Compositions created with federated audience composition: Federated audience composition (audience/federated-audience-composition.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)
* Support options when an error persists: Getting support (building-journeys/error-codes-reference.md#getting-support)
* Contacting Adobe Support: Support ticket guidelines (start/user-interface.md#support-ticket-guidelines)

+++

<!-- ai-section-version: 1 | source-hash: 7699f3c5 -->
