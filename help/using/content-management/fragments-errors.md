---
solution: Journey Optimizer
product: journey optimizer
title: Fragments and AEM content errors
description: Learn what common errors mean when you create, publish, and reference fragments, AEM content fragments, and AEM assets in Adobe Journey Optimizer, and how to fix them
feature: Fragments
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, fragments, AEM, content fragments, assets
---
# Fragments and AEM content errors {#fragments-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you publish fragments, reference them in content, or use Adobe Experience Manager content fragments and assets.

>[!ENDSHADEBOX]

Errors use the prefixes **CJMMAS** (fragments and assets), **AJOCBS** and **AJOAGS** (AEM content), followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

If the error persists after you follow the steps, note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or [contact Adobe Support](../start/user-interface.md#support-ticket-guidelines) with these details. For all the support options, see [Getting support](../building-journeys/error-codes-reference.md#getting-support).

## Permissions and access {#access}

These errors occur when your user does not have the permission or the access needed to manage, simulate, or publish a fragment.

See also [Get started with fragments](fragments.md) and [Built-in permissions](../administration/ootb-permissions.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1120-403** | You do not have permission to simulate content or access this fragment. Please contact your administrator to update your permissions. | Ask your administrator to grant you the **[!DNL Manage library items]** and **[!DNL Manage simulate content]** permissions (included in the Content Library Manager product profile). If an access label restricts the fragment, ask for that label to be added to your role. [Learn more](fragments.md#fragment-prerequisites) |
| **CJMMAS-1121-403** | You do not have permission to manage content or access this fragment. Please contact your administrator to update your permissions. | Ask your administrator to grant you the **[!DNL Manage library items]** permission (included in the Content Library Manager product profile). If an access label restricts the fragment, ask for that label to be added to your role. [Learn more](fragments.md#fragment-prerequisites) |
| **CJMMAS-1131-403** | You do not have permission to manage content or access fragment with id {fragmentId}. Please contact your administrator to update your permissions. | Ask your administrator to grant you the **[!DNL Manage library items]** permission (included in the Content Library Manager product profile). If an access label restricts the fragment whose ID is named in the message, ask for that label to be added to your role. [Learn more](fragments.md#fragment-prerequisites) |
| **CJMMAS-1122-403** | You do not have permission to publish this fragment. Please contact your administrator to update your permissions. | Ask your administrator to grant you the **[!DNL Publish Fragment]** permission (included in the Content Library Manager product profile). [Learn more](fragments.md#fragment-prerequisites) |
| **CJMMAS-1139-403** | You do not have permission on the referenced fragment uris {fragmentUris}. | Ask your administrator for access to the fragments referenced by this fragment. If access cannot be granted, remove the references. [Learn more](fragments.md#fragment-prerequisites) |

## Publishing fragments {#publication}

These errors occur when you publish, edit, or discard changes on a fragment.

See also [Fragments' statuses](manage-fragments.md#fragments-statuses) and [Publish a fragment](create-fragments.md#publish).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1141-400** | The fragment you are trying to publish already has a publication in progress. | Wait until the **[!UICONTROL Publishing]** status clears, then publish again. [Learn more](manage-fragments.md#fragments-statuses) |
| **CJMMAS-1157-400** | Updating fragment while publishing is not allowed. Please try after some time. | Wait until the **[!UICONTROL Publishing]** status clears, then edit the fragment. [Learn more](manage-fragments.md#fragments-statuses) |
| **CJMMAS-1145-400** | Data for fragment whose publication is in progress cannot be requested. | Wait until the **[!UICONTROL Publishing]** status clears, then request the data again. [Learn more](manage-fragments.md#fragments-statuses) |
| **CJMMAS-1160-404** | No data found for fragment whose publication is in progress. Please retry after the publication is complete. | Wait until the **[!UICONTROL Publishing]** status clears, then retry. [Learn more](manage-fragments.md#fragments-statuses) |
| **CJMMAS-1148-400** | Referenced fragment ''{name}'' is not published. Please publish before retrying. | Publish the referenced fragment named in the message, then publish again. [Learn more](create-fragments.md#publish) |
| **CJMMAS-1152-400** | Referenced fragment publication failed. Please fix the fragment and then try again. | Open the referenced fragment, fix it and publish it, then publish this fragment again. [Learn more](create-fragments.md#publish) |
| **CJMMAS-1130-400** | There are error(s) while validating the fragment. | Open the fragment, fix the validation errors, then publish it again. [Learn more](create-fragments.md#publish) |
| **CJMMAS-1149-400** | Validation Error in Fragment to be Published. | Open the fragment, fix the validation errors, then publish it again. [Learn more](create-fragments.md#publish) |
| **CJMMAS-1158-404** | No previous fragment publication found. Please publish fragment before retrying. | Publish the fragment, then retry. [Learn more](create-fragments.md#publish) |
| **CJMMAS-1159-404** | No previous successful fragment publication found. Please publish fragment successfully before retrying. | Publish the fragment, make sure the publication succeeds, then retry. [Learn more](create-fragments.md#publish) |
| **CJMMAS-1142-400** | Fragment should be published for Modify Fragment. | Publish the fragment first, then edit it. [Learn more](manage-fragments.md#edit-fragments) |
| **CJMMAS-1143-400** | Fragment should be in draft to Discard Changes. | Open the draft version of the **[!UICONTROL Live]** fragment that you are editing, then select **[!UICONTROL Discard draft]**. [Learn more](manage-fragments.md#edit-fragments) |
| **CJMMAS-1144-400** | There is no previous version info present. Will not be able to Discard Changes. | Use **[!UICONTROL Discard draft]** only on a fragment that was published before, since a fragment that was never published has no previous version. [Learn more](manage-fragments.md#edit-fragments) |

## References and limits {#references}

These errors occur when the content references fragments that cannot be found, are used in a loop, exceed the limits, or have an invalid syntax.

See also [Fragments guardrails](../start/guardrails.md#fragments-guardrails) and [Use expression fragments](../personalization/use-expression-fragments.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1105-400** | The fragment URI syntax is incorrect. Allowed syntax is {fragmentSyntax}. | Correct the reference to follow the syntax shown in the message, for example ajo:fragmentId/variantId. [Learn more](../personalization/use-expression-fragments.md) |
| **CJMMAS-1164-400** | Invalid fragment URI format. The URI should be in the format 'scheme:fragmentId/optionalVariantId?repoId=optionalRepoId'. | Correct the reference to the format scheme:fragmentId/variantId, for example ajo:fragmentId/variantId. [Learn more](../personalization/use-expression-fragments.md) |
| **CJMMAS-1165-400** | Missing repoId for AEM fragment. The repoId is mandatory for AEM fragments. | Add the repository ID to the fragment URI in the format aem:fragmentId/variantId?repoId=repositoryId. [Learn more](../personalization/use-expression-fragments.md) |
| **CJMMAS-1163-400** | Invalid fragment scheme. Allowed schemes are 'ajo', 'aem' and 'external'. | Use ajo, aem, or external as the scheme. [Learn more](../personalization/use-expression-fragments.md) |
| **CJMMAS-1107-404** | The fragment ID does not exist. Please check and try again. | Check the fragment ID, and that the fragment was not deleted or archived. [Learn more](manage-fragments.md#archive-fragments) |
| **CJMMAS-1132-404** | The fragment with id {fragmentId} does not exist. Please check and try again. | Check the ID named in the message, and that the fragment was not deleted or archived. [Learn more](manage-fragments.md#archive-fragments) |
| **CJMMAS-1140-404** | The fragment ids {fragmentIds} do not exist. | Check the IDs named in the message, and that the fragments were not deleted or archived. [Learn more](manage-fragments.md#archive-fragments) |
| **CJMMAS-1108-400** | The limit of number of fragment URIs passed in the input is reached. You cannot add more than {limit} fragments. | Reduce the number of fragments to the limit named in the message (up to 60 unique fragments per variant, and 120 across the variants of a message). [Learn more](../start/guardrails.md#fragments-guardrails) |
| **CJMMAS-1136-400** | Fragment {fragmentId} cannot be self referenced in itself. | Remove the reference to the fragment from inside the fragment itself. [Learn more](../start/guardrails.md#fragments-guardrails) |
| **CJMMAS-1137-400** | The referenced fragmentIds {fragmentIds} in-turn contain referenced fragments which violates the nested depth level constraint of {depth} depth level nested fragments. | Reduce the nesting: replace a fragment that contains other fragments with a single level of fragments. [Learn more](../start/guardrails.md#fragments-guardrails) |
| **CJMMAS-1138-400** | The fragment is in-turn used inside other fragment(s) and also contains referenced fragments which violates the nested depth level constraint of {depth} depth level nested fragments. | Reduce the nesting to a single level of fragments. [Learn more](../start/guardrails.md#fragments-guardrails) |
| **CJMMAS-1124-400** | Variant references could not be updated as the variant names are not distinct. | Give each variant a distinct name. [Learn more](create-fragments.md#content) |
| **CJMMAS-1125-400** | Variant references could not be updated as at least one variant must be enabled. | Keep at least one variant enabled. [Learn more](create-fragments.md#content) |
| **CJMMAS-1134-400** | The subType is only supported with expression fragment. | Leave the sub type empty for fragments that are not expression fragments. [Learn more](create-fragments.md#properties) |
| **CJMMAS-1135-400** | SubType attribute cannot be null in expression fragment. | Set the sub type of the expression fragment. [Learn more](create-fragments.md#properties) |

## AEM content fragments {#aem-fragments}

These errors occur when [!DNL Adobe Journey Optimizer] fetches or publishes an AEM content fragment.

See also [Considerations and troubleshooting](../integrations/aem-fragments-limitations.md#troubleshooting) for symptoms such as a fragment that is not visible in the selector.

| Error code | Message | How to fix |
|---|---|---|
| **AJOCBS-1101-401** | Unauthorized error occurred while fetching AEM content fragment with id {reqItemId}. Token might be wrong, expired or invalid. | Check the Adobe Experience Manager repository configuration and credentials, then try again. [Learn more](../integrations/aem-fragments.md#aem-add) |
| **CJMMAS-8101-401** | Unauthorized Error while fetching AEM Content Fragments. | Check the Adobe Experience Manager repository configuration and credentials, then try again. [Learn more](../integrations/aem-fragments.md#aem-add) |
| **AJOCBS-1102-403** | You don't have permission to access the AEM content fragment with id {reqItemId}. | Ask your administrator for access to the fragment and its repository. If access cannot be granted, remove the fragment from the content. [Learn more](../integrations/aem-fragments.md#aem-add) |
| **CJMMAS-8102-403** | Forbidden Error while fetching AEM Content Fragments. | Ask your administrator for access to the fragment and its repository. If access cannot be granted, remove the fragment from the content. [Learn more](../integrations/aem-fragments.md#aem-add) |
| **AJOCBS-1103-404** | AEM content fragment resource with id {reqItemId} not found. | Check that the fragment is published to the AEM Publish tier and carries the ajo-enabled tag for your organization and sandbox. [Learn more](../integrations/aem-fragments-limitations.md#troubleshooting) |
| **AJOCBS-1105-504** | Timeout occurred while fetching AEM content fragment with id {reqItemId}. | Check that the fragment is published, then try again. [Learn more](../integrations/aem-fragments-manage.md) |
| **AJOCBS-1108-400** | Bad request for AEM content fragment with id {reqItemId}. | Check that the fragment is published, then try again. [Learn more](../integrations/aem-fragments-manage.md) |
| **CJMMAS-1175-200** | This campaign/journey is using the Adobe Experience Manager fragment {fragmentName} which failed to publish during the last attempt. Republish the fragment on Experience Manager to synchronize it again with Journey Optimizer. | Republish the fragment in Adobe Experience Manager (warning). [Learn more](../integrations/aem-fragments-manage.md) |
| **CJMMAS-1162-500** | Referenced external fragment publication could not be completed in the defined timeframe. | Republish the fragment in Adobe Experience Manager, wait for the synchronization, then publish again. [Learn more](../integrations/aem-fragments-manage.md) |
| **CJMMAS-1161-500** | Referenced external fragment publication failed. Please fix the fragment and then try again. | Fix the fragment in Adobe Experience Manager, republish it, wait for the synchronization, then publish again. [Learn more](../integrations/aem-fragments-manage.md) |
| **CJMMAS-2036-403** | You do not have permission to use one or more AEM repositories referenced in the content: {deniedRepositoryIds}. | Ask your administrator for access to the AEM repositories named in the message. If access cannot be granted, remove the fragments stored in those repositories from the content. [Learn more](../integrations/aem-fragments.md#aem-add) |
| **AJOAGS-1501-422** | Bad Request. Repo Id is missing for AEM Content Fragment. | Select the fragment again so that its repository is recorded. [Learn more](../integrations/aem-fragments.md#aem-add) |

## AEM assets {#aem-assets}

These errors occur when assets from Adobe Experience Manager Assets are published to the CDN for use in your content.

See also [Create and manage assets](../integrations/assets.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1704-400** | Bad Asset ID or Asset not found. | Select a published asset from the right repository. [Learn more](../integrations/assets.md#add-asset) |
| **AJOAGS-1200-500** | AEM asset URL is either empty or not valid. | Select a published asset from the right repository. [Learn more](../integrations/assets.md#add-asset) |
| **AJOAGS-1201-417** | AEM asset has a 'FAILED' status. Please republish the asset and try again. | Republish the asset in Adobe Experience Manager, wait for the sync, then try again. [Learn more](../integrations/assets.md#faq-assets) |
| **CJMMAS-1730-206** | Retrying to check whether Asset is published or not. | Wait for the sync, then try again, and republish the asset in Adobe Experience Manager if it stays unpublished. [Learn more](../integrations/assets.md#faq-assets) |
| **CJMMAS-1732-500** | All assets might not have been published in the defined timeframe. | Republish the assets in Adobe Experience Manager, wait for the sync, then try again. [Learn more](../integrations/assets.md#faq-assets) |
| **CJMMAS-1613-413** | Payload too large for AEM Assets. | Use a smaller version of the asset. [Learn more](../integrations/assets.md#add-asset) |
| **CJMMAS-1713-413** | Asset size is too large to be published on CDN. | Use a smaller version of the asset. [Learn more](../integrations/assets.md#add-asset) |
| **CJMMAS-1657-507** | Org ranout with max storage capacity for storing assets in CDN. | Delete or unpublish assets you do not use, or contact your Adobe representative. [Learn more](../integrations/assets.md#faq-assets) |
| **CJMMAS-1601-401** | Unauthorized Error while accessing AEM Assets, Token might be wrong, expired or invalid. | Check your access to the repository, then try again. [Learn more](../integrations/assets.md#assets-prerequisites) |
| **CJMMAS-1603-403** | Forbidden error while accessing AEM Assets. | Check that you have access to the repository selected under **[!UICONTROL Select Repository]** (account icon, upper right), or switch to a repository you can access, then try again. [Learn more](../integrations/assets.md#assets-prerequisites) |
| **CJMMAS-1629-429** | Exceeded number of request allowed on AEM Assets. | Wait a few minutes, then try again. [Learn more](../integrations/assets.md#assets-prerequisites) |
| **CJMMAS-1653-503** | AEM Assets is currently unavailable. | Wait a few minutes, then try again. [Learn more](../integrations/assets.md#assets-prerequisites) |

## Related topics {#related}

* [Get started with fragments](fragments.md)
* [Create a fragment](create-fragments.md)
* [Manage fragments](manage-fragments.md)
* [Work with Experience Manager Content Fragments](../integrations/aem-fragments.md)
* [Considerations and troubleshooting for AEM Content Fragments](../integrations/aem-fragments-limitations.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/content-management/ai-augmented-fragments-errors.md}}
