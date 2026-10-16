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
hide: true
---
# Fragments and AEM content errors {#fragments-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you publish fragments, reference them in content, or use Adobe Experience Manager content fragments and assets.

>[!ENDSHADEBOX]

Errors use the prefixes **CJMMAS** (fragments and assets), **AJOCBS** and **AJOAGS** (AEM content), followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Permissions and access {#access}

These errors occur when your user does not have the permission or the access needed to manage, simulate, or publish a fragment.

See also [Get started with fragments](fragments.md) and [Built-in permissions](../administration/ootb-permissions.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1120-403**, **CJMMAS-1121-403**, **CJMMAS-1131-403** | You do not have permission to simulate content or access this fragment. Please contact your administrator to update your permissions.<br/>You do not have permission to manage content or access this fragment. Please contact your administrator to update your permissions.<br/>You do not have permission to manage content or access fragment with id {fragmentId}. Please contact your administrator to update your permissions. | Your user cannot access or manage this fragment, or simulate content with it. Ask your administrator to grant the **[!UICONTROL Manage library items]** permission (included in the Content Library Manager product profile), and access to the fragment. [Learn more](fragments.md#fragment-prerequisites) |
| **CJMMAS-1122-403** | You do not have permission to publish this fragment. Please contact your administrator to update your permissions. | Your user cannot publish this fragment. Ask your administrator to grant the **[!UICONTROL Publish Fragment]** permission. [Learn more](fragments.md#fragment-prerequisites) |
| **CJMMAS-1139-403** | You do not have permission on the referenced fragment uris {fragmentUris}. | Your user does not have access to the fragments referenced by this fragment. Ask your administrator for access to them, or remove the references. [Learn more](fragments.md#fragment-prerequisites) |

## Publishing fragments {#publication}

These errors occur when you publish, edit, or discard changes on a fragment.

See also [Fragments' statuses](manage-fragments.md#fragments-statuses) and [Publish a fragment](create-fragments.md#publish).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1141-400**, **CJMMAS-1157-400**, **CJMMAS-1145-400**, **CJMMAS-1160-404** | The fragment you are trying to publish already has a publication in progress.<br/>Updating fragment while publishing is not allowed. Please try after some time.<br/>Data for fragment whose publication is in progress cannot be requested.<br/>No data found for fragment whose publication is in progress. Please retry after the publication is complete. | The fragment is being published (**[!UICONTROL Publishing]** status). Wait until the publication completes, then try again. [Learn more](manage-fragments.md#fragments-statuses) |
| **CJMMAS-1148-400**, **CJMMAS-1152-400** | Referenced fragment ''{name}'' is not published. Please publish before retrying.<br/>Referenced fragment publication failed. Please fix the fragment and then try again. | A fragment that is referenced in this fragment or in the content is not published, or its publication failed. Fix and publish the referenced fragment first, then publish again. [Learn more](create-fragments.md#publish) |
| **CJMMAS-1130-400**, **CJMMAS-1149-400** | There are error(s) while validating the fragment.<br/>Validation Error in Fragment to be Published. | The fragment has validation errors. Open the fragment, fix the errors, then publish it again. [Learn more](create-fragments.md#publish) |
| **CJMMAS-1158-404**, **CJMMAS-1159-404** | No previous fragment publication found. Please publish fragment before retrying.<br/>No previous successful fragment publication found. Please publish fragment successfully before retrying. | The fragment has no successful publication yet. Publish the fragment, and make sure the publication succeeds, before you retry. [Learn more](create-fragments.md#publish) |
| **CJMMAS-1142-400** | Fragment should be published for Modify Fragment. | This action applies to a published fragment. Publish the fragment first, then edit it. [Learn more](manage-fragments.md#edit-fragments) |
| **CJMMAS-1143-400**, **CJMMAS-1144-400** | Fragment should be in draft to Discard Changes.<br/>There is no previous version info present. Will not be able to Discard Changes. | You can discard a draft only when the fragment is **[!UICONTROL Live]** and is being edited, so that a published version exists to go back to. A fragment that was never published has no previous version. [Learn more](manage-fragments.md#edit-fragments) |

## References and limits {#references}

These errors occur when the content references fragments that cannot be found, are used in a loop, exceed the limits, or have an invalid syntax.

See also [Fragments guardrails](../start/guardrails.md#fragments-guardrails) and [Use expression fragments](../personalization/use-expression-fragments.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1105-400**, **CJMMAS-1164-400**, **CJMMAS-1165-400** | The fragment URI syntax is incorrect. Allowed syntax is {fragmentSyntax}.<br/>Invalid fragment URI format. The URI should be in the format 'scheme:fragmentId/optionalVariantId?repoId=optionalRepoId'.<br/>Missing repoId for AEM fragment. The repoId is mandatory for AEM fragments. | The fragment reference does not follow the required syntax: scheme:fragmentId/variantId. For an AEM fragment, the repository ID is mandatory. Correct the reference, for example ajo:fragmentId/variantId. [Learn more](../personalization/use-expression-fragments.md) |
| **CJMMAS-1163-400** | Invalid fragment scheme. Allowed schemes are 'ajo', 'aem' and 'external'. | The fragment scheme is not valid. Use ajo, aem, or external. [Learn more](../personalization/use-expression-fragments.md) |
| **CJMMAS-1107-404**, **CJMMAS-1132-404**, **CJMMAS-1140-404** | The fragment ID does not exist. Please check and try again.<br/>The fragment with id {fragmentId} does not exist. Please check and try again.<br/>The fragment ids {fragmentIds} do not exist. | The fragment does not exist. Check the fragment ID, and that the fragment was not deleted or archived. [Learn more](manage-fragments.md#archive-fragments) |
| **CJMMAS-1108-400** | The limit of number of fragment URIs passed in the input is reached. You cannot add more than {limit} fragments. | The content uses more fragments than allowed. Reduce the number of fragments to the limit named in the message. Content can use up to 60 unique fragments per variant, and 120 across the variants of a message. [Learn more](../start/guardrails.md#fragments-guardrails) |
| **CJMMAS-1136-400** | Fragment {fragmentId} cannot be self referenced in itself. | A fragment cannot reference itself. Remove the reference. [Learn more](../start/guardrails.md#fragments-guardrails) |
| **CJMMAS-1137-400**, **CJMMAS-1138-400** | The referenced fragmentIds {fragmentIds} in-turn contain referenced fragments which violates the nested depth level constraint of {depth} depth level nested fragments.<br/>The fragment is in-turn used inside other fragment(s) and also contains referenced fragments which violates the nested depth level constraint of {depth} depth level nested fragments. | The fragments are nested deeper than the allowed depth. Reduce the nesting: replace a fragment that contains other fragments with a single level of fragments. [Learn more](../start/guardrails.md#fragments-guardrails) |
| **CJMMAS-1124-400**, **CJMMAS-1125-400** | Variant references could not be updated as the variant names are not distinct.<br/>Variant references could not be updated as at least one variant must be enabled. | The variant references cannot be updated. Give each variant a distinct name, and keep at least one variant enabled. [Learn more](create-fragments.md#content) |
| **CJMMAS-1134-400**, **CJMMAS-1135-400** | The subType is only supported with expression fragment.<br/>SubType attribute cannot be null in expression fragment. | A sub type is allowed only on expression fragments, and an expression fragment needs one. Set the sub type of the expression fragment, or leave it empty for other fragments. [Learn more](create-fragments.md#properties) |

## AEM content fragments {#aem-fragments}

These errors occur when [!DNL Adobe Journey Optimizer] fetches or publishes an AEM content fragment.

See also [Considerations and troubleshooting](../integrations/aem-fragments-limitations.md#troubleshooting) for symptoms such as a fragment that is not visible in the selector.

| Error code | Message | How to fix |
|---|---|---|
| **AJOCBS-1101-401**, **CJMMAS-8101-401** | Unauthorized error occurred while fetching AEM content fragment with id {reqItemId}. Token might be wrong, expired or invalid.<br/>Unauthorized Error while fetching AEM Content Fragments. | Journey Optimizer cannot authenticate to Adobe Experience Manager. Check the AEM connection and the access token, then try again. [Learn more](../integrations/aem-fragments.md#aem-add) |
| **AJOCBS-1102-403**, **CJMMAS-8102-403** | You don't have permission to access the AEM content fragment with id {reqItemId}.<br/>Forbidden Error while fetching AEM Content Fragments. | You do not have permission to use this content fragment. Ask your administrator for access to the fragment and its repository. [Learn more](../integrations/aem-fragments.md#aem-add) |
| **AJOCBS-1103-404** | AEM content fragment resource with id {reqItemId} not found. | The content fragment cannot be found. Check that it is published to the AEM Publish tier and carries the ajo-enabled tag for your organization and sandbox. [Learn more](../integrations/aem-fragments-limitations.md#troubleshooting) |
| **AJOCBS-1105-504**, **AJOCBS-1108-400** | Timeout occurred while fetching AEM content fragment with id {reqItemId}.<br/>Bad request for AEM content fragment with id {reqItemId}. | The request to Adobe Experience Manager timed out or was rejected. Check that the fragment is published, then try again. [Learn more](../integrations/aem-fragments-manage.md) |
| **CJMMAS-1175-200** | This campaign/journey is using the Adobe Experience Manager fragment {fragmentName} which failed to publish during the last attempt. Republish the fragment on Experience Manager to synchronize it again with Journey Optimizer. | An AEM fragment used in this campaign or journey failed to publish during the last attempt (warning). Republish the fragment in Adobe Experience Manager. [Learn more](../integrations/aem-fragments-manage.md) |
| **CJMMAS-1162-500**, **CJMMAS-1161-500** | Referenced external fragment publication could not be completed in the defined timeframe.<br/>Referenced external fragment publication failed. Please fix the fragment and then try again. | The publication of a referenced AEM fragment failed or did not complete in time. Fix the fragment in Adobe Experience Manager and republish it, then publish again. [Learn more](../integrations/aem-fragments-manage.md) |
| **CJMMAS-2036-403** | You do not have permission to use one or more AEM repositories referenced in the content: {deniedRepositoryIds}. | You do not have permission on the AEM repositories used in the content. Ask your administrator for access to the repositories named in the message. [Learn more](../integrations/aem-fragments.md#aem-add) |
| **AJOAGS-1501-422** | Bad Request. Repo Id is missing for AEM Content Fragment. | The repository ID of the AEM content fragment is missing. Select the fragment again so that its repository is recorded. [Learn more](../integrations/aem-fragments.md#aem-add) |

## AEM assets {#aem-assets}

These errors occur when assets from Adobe Experience Manager Assets are published to the CDN for use in your content.

See also [Create and manage assets](../integrations/assets.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1704-400**, **AJOAGS-1200-500** | Bad Asset ID or Asset not found.<br/>AEM asset URL is either empty or not valid. | The asset ID is wrong, or the asset was not found or has no valid URL. Select a published asset from the right repository. [Learn more](../integrations/assets.md#add-asset) |
| **AJOAGS-1201-417**, **CJMMAS-1730-206**, **CJMMAS-1732-500** | AEM asset has a 'FAILED' status. Please republish the asset and try again.<br/>Retrying to check whether Asset is published or not.<br/>All assets might not have been published in the defined timeframe. | The asset is not published yet, its publication failed, or it did not complete in time. Republish the asset in Adobe Experience Manager, wait for the sync, then try again. [Learn more](../integrations/assets.md#faq-assets) |
| **CJMMAS-1613-413**, **CJMMAS-1713-413** | Payload too large for AEM Assets.<br/>Asset size is too large to be published on CDN. | The asset is too large to be published to the CDN. Use a smaller version of the asset. [Learn more](../integrations/assets.md#add-asset) |
| **CJMMAS-1657-507** | Org ranout with max storage capacity for storing assets in CDN. | Your organization reached the storage capacity for assets in the CDN. Delete or unpublish assets you do not use, or contact your Adobe representative. [Learn more](../integrations/assets.md#faq-assets) |
| **CJMMAS-1601-401**, **CJMMAS-1603-403**, **CJMMAS-1629-429**, **CJMMAS-1653-503** | Unauthorized Error while accessing AEM Assets, Token might be wrong, expired or invalid.<br/>Forbidden error while accessing AEM Assets.<br/>Exceeded number of request allowed on AEM Assets.<br/>AEM Assets is currently unavailable. | Journey Optimizer cannot access Adobe Experience Manager Assets: authentication or permission failure, too many requests, or the service is unavailable. Check your access to the repository, wait a few minutes, then try again. [Learn more](../integrations/assets.md#assets-prerequisites) |

## Related topics {#related}

* [Get started with fragments](fragments.md)
* [Create a fragment](create-fragments.md)
* [Manage fragments](manage-fragments.md)
* [Work with Experience Manager Content Fragments](../integrations/aem-fragments.md)
* [Considerations and troubleshooting for AEM Content Fragments](../integrations/aem-fragments-limitations.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)
