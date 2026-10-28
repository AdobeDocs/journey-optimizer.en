---
solution: Journey Optimizer
product: journey optimizer
title: Audience composition errors
description: Learn what common errors mean when you build, enrich, and publish audience compositions in Adobe Journey Optimizer, and how to fix them
feature: Audiences, Segments
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, audience composition, enrichment, split, rank
---
# Audience composition errors {#audience-composition-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you build, enrich, publish, or manage an audience composition.

>[!ENDSHADEBOX]

Composition errors use the prefix **CJMRT**, followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

If the error persists after you follow the steps, note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or [contact Adobe Support](../start/user-interface.md#support-ticket-guidelines) with these details. For all the support options, see [Getting support](../building-journeys/error-codes-reference.md#getting-support).

## Composition structure {#structure}

These errors occur when you validate or publish a composition and its workflow is not valid.

See also [Create a composition workflow](get-started-audience-orchestration.md#create).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170002-400** | The composition must begin with a single audience. | Add a single audience as the first activity. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170004-400** | The composition must start with a valid dataset or segment. | Make the first activity a valid dataset or segment, or a single audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170006-400** | The composition started without an audience. | Add an audience as the first activity. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170005-400** | The composition contains disconnected operations. | Connect the disconnected activity to the workflow, or delete it. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170003-400** | The composition must not contain cyclic references. | Remove the link that loops the workflow back to an earlier activity. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170007-400** | The composition must end with a Save operation. | Add a Save activity at the end of each path. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170008-400** | The composition cannot be empty. | Add an audience as the first activity, then the activities you need, and end each path with a Save activity. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170001-400** | Invalid references present in the composition. | Open the activity named in the message and correct its reference. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170039-400** | Invalid Composition. | If the composition is empty, add the activities. Otherwise, open the activity named in the message and correct its reference. [Learn more](get-started-audience-orchestration.md#create) |

## Audiences {#audiences}

These errors occur when you select or name the audiences of a composition.

See also [Get started with audience composition](get-started-audience-orchestration.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170011-400** | You need to select at least one audience. | Select at least one audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#add-audience){target="_blank"} |
| **CJMRT-170016-400** | Audience name {label} already exists. Please choose a different name. | Enter a different audience name. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170025-404** | One or more audience used cannot be found.  Please select another audience. | Replace the missing audience with another audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170029-400** | One or more selected audiences is using a different merge policy than the one associated with the composition. Please choose a different audience. | Select audiences that use the merge policy of the composition. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170045-400** | One or more of the selected audiences cannot be used in this composition. | Replace the selected audience with another audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |

## Activities {#activities}

These errors occur when an activity of a composition is not configured completely.

See also [the audience composition guide](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition){target="_blank"}.

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170015-400** | Sum of all branches should be equal to 100. | Adjust the percentages of the branches so that they add up to 100. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#split-percentage){target="_blank"} |
| **CJMRT-170033-400** | Please select a Target dimension | Select a target dimension. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170013-400** | Limit must be positive. | Enter a limit greater than 0 in the **[!UICONTROL Rank]** activity. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#rank-block){target="_blank"} |
| **CJMRT-170012-400** | Path cannot be empty. | Open the activity named in the message and enter a valid path. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#build-rule){target="_blank"} |
| **CJMRT-170014-400** | Please supply a value for all fields. | A field of an activity is empty. Open the activity and enter a value in every field. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#build-rule){target="_blank"} |
| **CJMRT-170027-400** | Required fields in {param} must not be empty. | Open the activity named in the message and fill in its required fields. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#build-rule){target="_blank"} |
| **CJMRT-170023-400** | Excluded values cannot be empty. | Open the **[!UICONTROL Exclude]** activity and enter the excluded values. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#exclude-attribute){target="_blank"} |
| **CJMRT-170030-400** | Please provide a filter key. | A filter has no key. Enter the filter key. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#exclude-attribute){target="_blank"} |
| **CJMRT-170031-400** | Please provide a filter value. | A filter has no value. Enter the filter value. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#exclude-attribute){target="_blank"} |

## Enrichment {#enrichment}

These errors occur when you configure an enrichment with a dataset.

See also [Leverage enrichment attributes](enrichment-attributes.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170034-400** | Enrichment dataset not found. | Select an existing enrichment dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170060-404** | The enrichment dataset was not found. Please use a valid enrichment dataset or try again later. | Select a valid enrichment dataset. If the dataset is valid, try again later. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170035-400** | Please select a source join key. | Select the join key of the audience as the source join key. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170036-400** | Please select an enrichment dataset join key. | Select the join key of the enrichment dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170037-400** | Must select at least one enrichment attribute. | Select at least one attribute of the enrichment dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170050-400** | Please select an audience enrichment attribute. | Select at least one attribute of the enrichment dataset as the audience enrichment attribute. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170040-400** | The selected enrichment dataset is greater than 1 GB. | Select a dataset of 1 GB or less, or reduce the size of the enrichment dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170041-400** | The selected dataset is empty. Please check and try again. | Select a dataset that contains data. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170048-428** | The enrichment dataset must be associated with a schema. | Associate the dataset with a schema, or select another dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170058-400** | The selected enrichment dataset must have a primary identity descriptor defined in its schema. | Define a primary identity in the schema of the dataset, or select another dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170051-404** | The enrichment attribute schema could not be found. Please verify the schema exists and try again. | Check that the schema exists, then select the attribute again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170052-400** | The enrichment attribute schema properties are missing or empty. Please ensure the properties are defined and try again. | Check that the schema defines properties, then select the attribute again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170053-404** | The specified enrichment schema path could not be found. Please verify the path exists and try again. | Check that the schema defines the attribute, then select it again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170054-404** | The source schema for the enrichment attribute was not found. Please verify the schema exists and try again. | Check that the schema exists, then select the attribute again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170059-424** | There was an error using this enrichment dataset. Please use a valid enrichment dataset or try again later. | Select a valid enrichment dataset, or try again later. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170061-424** | There was an error using this enrichment dataset. Please use a valid enrichment dataset or try again later. | Select a valid enrichment dataset, or try again later. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |

## Publication, limits, and permissions {#publication}

These errors occur when you publish or manage compositions.

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170042-400** | You have reached the limitation of 50 active compositions authorized in the inventory. You cannot add a new one. | Delete a published composition you no longer need, then publish the new one. Compositions created with federated audience composition are not counted. [Learn more](../start/guardrails.md#audience) |
| **CJMRT-170043-412** | The composition has been modified. Please refresh the page. | Refresh the page, then make your change again. [Learn more](get-started-audience-orchestration.md#access) |
| **CJMRT-170046-413** | Publishing this composition may impact system performance. Please consider decreasing the audience size before continuing. | Warning. Reduce the size of the audience before you continue. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#publish){target="_blank"} |
| **CJMRT-170047-424** | Please ensure associated audience from this composition are not used in any downstream activations or as a building block of another audience. | Remove the audiences of this composition from the activations and from the audiences that use them, then delete the composition. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/sandbox/ui/user-guide.html#delete-audience-compositions){target="_blank"} |
| **CJMRT-170056-409** | Only one composition evaluation job can be queued at a time. Please try again later. | Wait for the current evaluation to end, then try again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#publish){target="_blank"} |
| **CJMRT-170017-403** | The client is not authorized for access. | Ask your administrator to check the permissions and the sandbox assigned to your role. [Learn more](../administration/ootb-permissions.md) |
| **CJMRT-170024-403** | You don't have permission to publish this rule.  Please contact your administrator or remove unauthorized settings. | Ask your administrator to check the permissions assigned to your role, or remove the settings your role is not allowed to use, such as audiences or attributes protected by an access label that your role does not include. [Learn more](../administration/ootb-permissions.md) |
| **CJMRT-170028-403** | Missing required permissions. | Ask your administrator to check the permissions and the sandbox assigned to your role. [Learn more](../administration/ootb-permissions.md) |

## Related topics {#related}

* [Get started with audience composition](get-started-audience-orchestration.md)
* [Leverage enrichment attributes](enrichment-attributes.md)
* [Federated audience composition](federated-audience-composition.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/audience/ai-augmented-audience-composition-errors.md}}
