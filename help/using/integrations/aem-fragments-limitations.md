---
solution: Journey Optimizer
product: journey optimizer
title: Adobe Experience Manager Content Fragments considerations and troubleshooting
description: Considerations and common issues for AEM Content Fragments in Journey Optimizer.
topic: Content Management
role: User
level: Beginner
---
# Considerations and troubleshooting {#aem-fragments-limitations}

## Key considerations {#considerations}

Keep the following in mind when using Content Fragments from [!DNL Adobe Experience Manager] in [!DNL Journey Optimizer]:

* **Content fragment types**
    * Simple Content Fragments, nested Content Fragments, and **Content Fragment variations** are supported. Choose the variation when you insert the fragment in [!DNL Journey Optimizer]. If you do not select a variation, the **Main** variation (the fragment's primary content in [!DNL Adobe Experience Manager]) is used.

* **Multilingual content**
    * Each variation must be authored, tagged, and published in [!DNL Adobe Experience Manager]. In [!DNL Journey Optimizer], select the fragment variation that matches each message language or locale.
    * There is no automatic language resolution or fallback between variations.

* **Repository access**
    * [!DNL Journey Optimizer] integrates with the [!DNL Adobe Experience Manager] **Publish** tier only (Sites, Content Fragments). Content Fragments are available through a public, unauthenticated endpoint.
    * Author repositories may appear in the repository selector, but only fragments published to **Publish** can be used in [!DNL Journey Optimizer].

* **Content Fragment status**
    * Fragments can show **[!UICONTROL Published]** or **[!UICONTROL Modified]** status; [!DNL Journey Optimizer] always uses the **latest published version**.
    * Changes made after publication are not reflected in [!DNL Journey Optimizer] until the fragment is republished in [!DNL Adobe Experience Manager]. There is no automatic version reconciliation between the two products.

* **Personalization**
    * Supported: profile attributes, contextual attributes, static strings, and pre-declared variables.
    * Not supported: derived or computed attributes.

* **Updates and versioning**
    * Updates require manual republication from [!DNL Adobe Experience Manager]. There is no automatic version reconciliation.
    * When a Content Fragment is published or republished in [!DNL Adobe Experience Manager], [!DNL Journey Optimizer] updates that fragment and refreshes **all variations of that fragment that are referenced** in active campaigns or journeys.
    * The [!DNL Adobe Experience Manager] [publish action](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/manage/manage-publication) can be delayed. When it completes, [!DNL Journey Optimizer] receives an event and refreshes the content.
    * After a successful update, changes are typically available within about **5 minutes** for unitary journeys and in the **next batch** for batch use cases.

* **Caching and proofing**
    * When a fragment is first added to a campaign or journey, [!DNL Journey Optimizer] caches it. If you select a fragment that was already used elsewhere through **[!UICONTROL Open AEM CF selector]**, it is loaded from the [!DNL Journey Optimizer] cache.
    * After you republish a modified fragment in [!DNL Adobe Experience Manager], [!DNL Journey Optimizer] listens for the event and updates the cache.
    * Proofs always reflect the **most recently published** version; you cannot lock a historical version for proofing.

## Troubleshooting {#troubleshooting}

If you encounter issues when working with Adobe Experience Manager Content Fragments in Journey Optimizer, refer to the following common problems and resolutions:

| Issue | Cause | Resolution |
|-|-|-|
| **Tag not found** or **Content Fragment not visible in selector** | Adobe Experience Manager tag syntax does not match required format `ajo-enabled:{OrgId}/{SandboxName}` | Validate that the tag ID uses the correct **Organization ID** and **Sandbox Name**. Ensure there are no spaces or incorrect separators. Republish the Content Fragment after correcting the tag. |
| **Content Fragment not appearing in list** | Content Fragment is in draft state or not published | Only approved and published Content Fragments are displayed in the Journey Optimizer selector. Publish the Content Fragment in Adobe Experience Manager and ensure it has the published status. |
| **Variable undefined error** | Personalization placeholder not declared in fragment helper tag | Add all required parameters in the fragment helper tag. Each placeholder used in the Content Fragment must be explicitly declared with its mapping. |
| **Proof displays unexpected content** | Proof uses the latest published version from Adobe Experience Manager | Proofs always reflect the most recent publication of the Content Fragment in Adobe Experience Manager. If you made recent changes in Adobe Experience Manager, republish the fragment and refresh your proof. |
| **Access denied (CPES) error** | User role not authorized to access certain attributes | Contact your system administrator to verify that your role has the appropriate permissions for the profile or contextual attributes used in personalization. |
| **Fragment displays blank or missing content** | Missing required personalization parameters or fallback values | Ensure all required parameters are provided and consider adding fallback values for optional attributes. |
| **Image does not render or appears broken** | Image URL in the Content Fragment is a relative path or not reachable from the channel | Use **absolute** URLs (`https://...`) for image fields. Relative paths from Adobe Experience Manager are not supported. Confirm the URL in a browser or message preview. |
| **Experience League AEM link returns 404** | Stale bookmark, preview build, or unpublished AEM help page | Open the [Content Fragments with Adobe Journey Optimizer](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-with-journey-optimizer){target="_blank"} topic from the live Experience Manager documentation and navigate from the on-page table of contents, or search for the section name (for example **Dispatcher Configuration**). |

If the issue persists, contact your Adobe representative with details about your Content Fragment ID, campaign or journey ID, and any error messages displayed.
