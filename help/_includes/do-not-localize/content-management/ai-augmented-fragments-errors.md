---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the errors that [!DNL Adobe Journey Optimizer] returns when you publish fragments, reference them in content, or use Adobe Experience Manager content fragments and assets, with the cause and the fix for each error family.

**Intents:**

* Find the cause and the fix for an error returned when publishing a fragment or referencing fragments in content
* Understand the parts of an error code: the prefix (CJMMAS, AJOCBS, AJOAGS), the error number, and the HTTP status
* Resolve permission errors on fragments (simulate, manage, publish, referenced fragments)
* Resolve errors on Adobe Experience Manager content fragments and Adobe Experience Manager assets

**Glossary:**

* **Error code**: Prefix, error number and HTTP status, for example CJMMAS-1122-403 *(product-specific)*
* **CJMMAS**: Prefix of the errors for fragments and assets *(product-specific)*
* **AJOCBS** and **AJOAGS**: Prefixes of the errors for AEM content *(product-specific)*
* **Publication in progress**: A fragment in the **[!UICONTROL Publishing]** status; it cannot be published again or updated until the publication completes
* **Fragment reference syntax**: scheme:fragmentId/variantId; for an AEM fragment, the repository ID is mandatory. Allowed schemes are ajo, aem, and external (for example ajo:fragmentId/variantId)
* **Error families, one per section of the page:**
* **Permissions and access** (CJMMAS-1120, 1121, 1131, 1122, 1139; status 403): the user cannot simulate, manage, or publish a fragment, or lacks access to referenced fragments.
* **Publishing fragments** (CJMMAS-1141, 1157, 1145, 1160, 1148, 1152, 1130, 1149, 1158, 1159, 1142, 1143, 1144): publication already in progress, referenced fragment not published or failed, validation errors, no previous successful publication, editing or discarding changes in the wrong state.
* **References and limits** (CJMMAS-1105, 1164, 1165, 1163, 1107, 1132, 1140, 1108, 1136, 1137, 1138, 1124, 1125, 1134, 1135): invalid reference syntax or scheme, fragment ID that does not exist, too many fragments, self reference, nesting depth, variant names not distinct or no variant enabled, sub type errors.
* **AEM content fragments** (AJOCBS, CJMMAS-8101, 8102, 1175, 1162, 1161, 2036 and AJOAGS-1501): authentication, permission, not found, timeout or bad request when fetching or publishing an AEM content fragment, failed publication, missing repository ID.
* **AEM assets** (CJMMAS-1704, 1730, 1732, 1613, 1713, 1657, 1601, 1603, 1629, 1653 and AJOAGS-1200, 1201): bad asset ID or asset not found, asset not published or publication failed, asset too large, CDN storage capacity reached, access to AEM Assets failed.

**Guardrails:**

* Content can use up to 60 unique fragments per variant, and 120 across the variants of a message (hard limit). Exceeding it returns CJMMAS-1108-400, which names the limit in the message.
* A fragment cannot reference itself (CJMMAS-1136-400).
* Fragments cannot be nested deeper than the allowed depth (CJMMAS-1137-400, CJMMAS-1138-400); the depth is given in the message.
* You can discard changes only from the draft version of a **[!UICONTROL Live]** fragment that you are editing, with **[!UICONTROL Discard draft]** (CJMMAS-1143-400). A fragment that was never published has no previous version, so changes cannot be discarded (CJMMAS-1144-400).
* A sub type is allowed only on expression fragments, and an expression fragment needs one (CJMMAS-1134-400, CJMMAS-1135-400).
* A payload that is too large for AEM Assets is rejected (CJMMAS-1613-413), and an asset that is too large cannot be published to the CDN (CJMMAS-1713-413). In both cases, use a smaller version of the asset.

**Prerequisites and permissions:**

* **[!UICONTROL Manage library items]** permission (included in the Content Library Manager product profile), plus access to the fragment: needed to manage a fragment or simulate content with it
* **[!UICONTROL Publish Fragment]** permission: needed to publish a fragment
* Access to the fragments referenced by a fragment: needed when a fragment references other fragments
* Access to the AEM content fragment and its repository, and to the AEM repositories referenced in the content: needed for AEM content fragments

**Terminology:**

* Canonical name: Fragments and AEM content errors — variants: fragment errors, AEM content fragment errors, AEM asset errors
* Acronym: AEM — Adobe Experience Manager

**FAQ:**

* **Q: What do the parts of an error code mean?** — Errors use the prefixes CJMMAS (fragments and assets), AJOCBS and AJOAGS (AEM content), followed by an error number and an HTTP status.
* **Q: I cannot publish a fragment because of a permission error. What do I do?** — For CJMMAS-1122-403, ask your administrator to grant the **[!UICONTROL Publish Fragment]** permission.
* **Q: I cannot manage a fragment or simulate content with it. What do I do?** — For CJMMAS-1120-403, CJMMAS-1121-403 and CJMMAS-1131-403, ask your administrator to grant the **[!UICONTROL Manage library items]** permission (included in the Content Library Manager product profile) and access to the fragment.
* **Q: Why does publishing fail with "The fragment you are trying to publish already has a publication in progress."?** — The fragment is in the **[!UICONTROL Publishing]** status. Wait until the status clears, then publish again.
* **Q: Why does publishing fail because of a referenced fragment?** — For CJMMAS-1148-400, the referenced fragment named in the message is not published: publish it, then publish again. For CJMMAS-1152-400, the publication of a referenced fragment failed: open the referenced fragment, fix it and publish it, then publish this fragment again.
* **Q: Why does "The limit of number of fragment URIs passed in the input is reached." appear?** — The content uses more fragments than allowed (CJMMAS-1108-400). Content can use up to 60 unique fragments per variant, and 120 across the variants of a message.
* **Q: An AEM content fragment cannot be found (AJOCBS-1103-404). What do I check?** — Check that it is published to the AEM Publish tier and carries the ajo-enabled tag for your organization and sandbox.
* **Q: What do I do when an AEM asset is not published or its publication failed?** — For AJOAGS-1201-417 (the publication of the asset has the FAILED status) and CJMMAS-1732-500 (some assets may not have been published in the defined timeframe), republish the asset or assets in Adobe Experience Manager, wait for the sync, then try again. For CJMMAS-1730-206 (Journey Optimizer is checking again whether the asset is published), wait for the sync, then try again, and republish the asset in Adobe Experience Manager if it stays unpublished.
* **Q: What do I do when the organization reached the CDN storage capacity for assets?** — For CJMMAS-1657-507, delete or unpublish assets you do not use, or contact your Adobe representative.

**Troubleshooting:**

* CJMMAS-1175-200, "This campaign/journey is using the Adobe Experience Manager fragment {fragmentName} which failed to publish during the last attempt. Republish the fragment on Experience Manager to synchronize it again with Journey Optimizer." — A warning. An AEM fragment used in the campaign or journey failed to publish during the last attempt. Republish the fragment in Adobe Experience Manager.
* CJMMAS-1163-400, "Invalid fragment scheme. Allowed schemes are 'ajo', 'aem' and 'external'." — The fragment scheme is not valid. Use ajo, aem, or external.
* CJMMAS-1142-400, "Fragment should be published for Modify Fragment." — The action applies to a published fragment. Publish the fragment first, then edit it.
* AJOAGS-1501-422, "Bad Request. Repo Id is missing for AEM Content Fragment." — The repository ID is missing. Select the fragment again so that its repository is recorded.
* CJMMAS-1629-429, "Exceeded number of request allowed on AEM Assets." — Too many requests were sent to Adobe Experience Manager Assets. Wait a few minutes, then try again.
* CJMMAS-1653-503, "AEM Assets is currently unavailable." — Adobe Experience Manager Assets is unavailable. Wait a few minutes, then try again.
* CJMMAS-1601-401, "Unauthorized Error while accessing AEM Assets, Token might be wrong, expired or invalid." — Authentication to Adobe Experience Manager Assets failed. Check your access to the repository, then try again.
* CJMMAS-1603-403, "Forbidden error while accessing AEM Assets." — You do not have permission to access Adobe Experience Manager Assets. Check your access to the repository, then try again.
* CJMMAS-1704-400, "Bad Asset ID or Asset not found." and AJOAGS-1200-500, "AEM asset URL is either empty or not valid." — The asset ID is wrong or the asset was not found (CJMMAS-1704-400), or the asset has no URL or its URL is not valid (AJOAGS-1200-500). In both cases, select a published asset from the right repository.
* CJMMAS-1139-403, "You do not have permission on the referenced fragment uris {fragmentUris}." — Your user does not have access to the fragments referenced by this fragment. Ask your administrator for access to them, or remove the references.
* CJMMAS-1130-400 and CJMMAS-1149-400 — The fragment has validation errors. Open the fragment, fix the errors, then publish it again.
* CJMMAS-1158-404, "No previous fragment publication found." — The fragment has no publication yet. Publish the fragment before you retry. CJMMAS-1159-404 — The fragment has no successful publication yet. Publish the fragment and make sure the publication succeeds before you retry.
* CJMMAS-1157-400, CJMMAS-1145-400, CJMMAS-1160-404 — The fragment is in the **[!UICONTROL Publishing]** status. Wait until the status clears, then edit the fragment (CJMMAS-1157-400), request the data again (CJMMAS-1145-400), or retry (CJMMAS-1160-404).
* CJMMAS-1143-400, "Fragment should be in draft to Discard Changes." — See Guardrails. CJMMAS-1144-400, "There is no previous version info present. Will not be able to Discard Changes." — The fragment has no previous version, so use **[!UICONTROL Discard draft]** only on a fragment that was published before.
* CJMMAS-1161-500 and CJMMAS-1162-500 — The publication of a referenced AEM fragment failed (CJMMAS-1161-500) or did not complete in time (CJMMAS-1162-500). For CJMMAS-1162-500, republish the fragment in Adobe Experience Manager, wait for the synchronization, then publish again. For CJMMAS-1161-500, fix the fragment in Adobe Experience Manager, republish it, wait for the synchronization, then publish again.
* AJOCBS-1101-401 and CJMMAS-8101-401 — Journey Optimizer cannot authenticate to Adobe Experience Manager. Check the Adobe Experience Manager repository configuration and credentials, then try again.
* AJOCBS-1102-403 and CJMMAS-8102-403 — You do not have permission to use this content fragment. Ask your administrator for access to the fragment and its repository.
* AJOCBS-1105-504 and AJOCBS-1108-400 — The request to Adobe Experience Manager timed out (AJOCBS-1105-504) or was rejected as a bad request (AJOCBS-1108-400). Check that the fragment is published, then try again.
* CJMMAS-1105-400, CJMMAS-1164-400, CJMMAS-1165-400 and CJMMAS-1163-400 — The fragment reference is not valid. Correct it to follow the syntax shown in the message (scheme:fragmentId/variantId); for an AEM fragment, add the repository ID (aem:fragmentId/variantId?repoId=repositoryId).
* CJMMAS-1107-404, CJMMAS-1132-404 and CJMMAS-1140-404 — The fragment ID does not exist. Check the ID, and that the fragment was not deleted or archived.
* CJMMAS-1124-400 and CJMMAS-1125-400 — The variant references cannot be updated: give each variant a distinct name (CJMMAS-1124-400), and keep at least one variant enabled (CJMMAS-1125-400).

**Related pages:**

* Prerequisites for fragment permissions: Get started with fragments (content-management/fragments.md)
* Fragment statuses: Fragments' statuses (content-management/manage-fragments.md)
* Publishing a fragment: Publish a fragment (content-management/create-fragments.md)
* Fragment limits: Fragments guardrails (start/guardrails.md)
* Fragment reference syntax: Use expression fragments (personalization/use-expression-fragments.md)
* AEM content fragment symptoms such as a fragment not visible in the selector: Considerations and troubleshooting (integrations/aem-fragments-limitations.md)
* AEM assets: Create and manage assets (integrations/assets.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 1 | source-hash: d304db4c -->
