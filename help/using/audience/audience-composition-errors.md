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

## Composition structure {#structure}

These errors occur when you validate or publish a composition and its workflow is not valid.

See also [Create a composition workflow](get-started-audience-orchestration.md#create).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170002-400** | The composition must begin with a single audience. | The composition does not begin with a single audience. Add one audience as the first activity. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170004-400** | The composition must start with a valid dataset or segment. | The first activity is not a valid dataset or segment. Begin the composition with a valid dataset or segment, or with a single audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170006-400** | The composition started without an audience. | The composition has no audience at its start. Add an audience as the first activity. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170005-400** | The composition contains disconnected operations. | An activity is not connected to the workflow. Connect the disconnected activity, or delete it. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170003-400** | The composition must not contain cyclic references. | The workflow loops back on itself. Remove the loop. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170007-400** | The composition must end with a Save operation. | A composition must end with a Save activity. Add a Save activity to each path. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170008-400** | The composition cannot be empty. | The composition is empty. Add the activities. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170001-400** | Invalid references present in the composition. | The composition contains an invalid reference. Fix the activity named in the message. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170039-400** | Invalid Composition. | The composition is empty or contains an invalid reference. Add the activities, or fix the activity named in the message. [Learn more](get-started-audience-orchestration.md#create) |

## Audiences {#audiences}

These errors occur when you select or name the audiences of a composition.

See also [Get started with audience composition](get-started-audience-orchestration.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170011-400** | You need to select at least one audience. | Select at least one audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#add-audience){target="_blank"} |
| **CJMRT-170016-400** | Audience name {label} already exists. Please choose a different name. | An audience with this name already exists. Choose a different audience name. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170025-404** | One or more audience used cannot be found.  Please select another audience. | An audience used in the composition cannot be found. Select another audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170029-400** | One or more selected audiences is using a different merge policy than the one associated with the composition. Please choose a different audience. | A selected audience uses a merge policy different from the one of the composition. Select audiences that use the merge policy of the composition. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170045-400** | One or more of the selected audiences cannot be used in this composition. | A selected audience cannot be used in this composition. Replace it with another audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |

## Activities {#activities}

These errors occur when an activity of a composition is not configured completely.

See also [the audience composition guide](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition){target="_blank"}.

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170015-400** | Sum of all branches should be equal to 100. | The percentages of the branches of a split must add up to 100. Adjust the percentages. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#split-percentage){target="_blank"} |
| **CJMRT-170033-400** | Please select a Target dimension | Select a target dimension. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170013-400** | Limit must be positive. | The limit of the **[!UICONTROL Rank]** activity must be a positive number. Enter a limit greater than 0. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#rank-block){target="_blank"} |
| **CJMRT-170012-400** | Path cannot be empty. | An activity has an empty path. Open the activity named in the message and enter a valid path. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#build-rule){target="_blank"} |
| **CJMRT-170014-400** | Please supply a value for all fields. | A field of an activity is empty. Open the activity and enter a value in every field. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#build-rule){target="_blank"} |
| **CJMRT-170027-400** | Required fields in {param} must not be empty. | A required field of the activity named in the message is empty. Open the activity and fill in the required fields. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#build-rule){target="_blank"} |
| **CJMRT-170023-400** | Excluded values cannot be empty. | The **[!UICONTROL Exclude]** activity has no excluded values. Enter the excluded values. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#exclude-attribute){target="_blank"} |
| **CJMRT-170030-400** | Please provide a filter key. | A filter has no key. Enter the filter key. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#exclude-attribute){target="_blank"} |
| **CJMRT-170031-400** | Please provide a filter value. | A filter has no value. Enter the filter value. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#exclude-attribute){target="_blank"} |

## Enrichment {#enrichment}

These errors occur when you configure an enrichment with a dataset.

See also [Leverage enrichment attributes](enrichment-attributes.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170034-400** | Enrichment dataset not found. | The enrichment dataset cannot be found. Select an existing dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170060-404** | The enrichment dataset was not found. Please use a valid enrichment dataset or try again later. | The enrichment dataset cannot be found. Select a valid dataset, or try again later. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170035-400** | Please select a source join key. | The join key of the audience is not selected. Select it. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170036-400** | Please select an enrichment dataset join key. | The join key of the enrichment dataset is not selected. Select it. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170037-400** | Must select at least one enrichment attribute. | No enrichment attribute is selected. Select at least one attribute of the enrichment dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170050-400** | Please select an audience enrichment attribute. | No audience enrichment attribute is selected. Select at least one attribute of the enrichment dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170040-400** | The selected enrichment dataset is greater than 1 GB. | The enrichment dataset is larger than 1 GB. Select another dataset, or reduce its size. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170041-400** | The selected dataset is empty. Please check and try again. | The enrichment dataset is empty. Select another dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170048-428** | The enrichment dataset must be associated with a schema. | The enrichment dataset is not associated with a schema. Associate it with a schema, or select another dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170058-400** | The selected enrichment dataset must have a primary identity descriptor defined in its schema. | The schema of the enrichment dataset has no primary identity. Update the schema to define one, or select another dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170051-404** | The enrichment attribute schema could not be found. Please verify the schema exists and try again. | The schema of the enrichment attribute cannot be found. Check that the schema exists, then select the attribute again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170052-400** | The enrichment attribute schema properties are missing or empty. Please ensure the properties are defined and try again. | The schema of the enrichment attribute has no properties. Check that the schema defines properties, then select the attribute again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170053-404** | The specified enrichment schema path could not be found. Please verify the path exists and try again. | The path of the enrichment attribute cannot be found in the schema. Check that the schema defines the attribute, then select it again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170054-404** | The source schema for the enrichment attribute was not found. Please verify the schema exists and try again. | The source schema of the enrichment attribute cannot be found. Check that the schema exists, then select the attribute again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170059-424** | There was an error using this enrichment dataset. Please use a valid enrichment dataset or try again later. | The enrichment dataset cannot be used. Select a valid dataset, or try again later. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170061-424** | There was an error using this enrichment dataset. Please use a valid enrichment dataset or try again later. | The enrichment dataset cannot be used. Select a valid dataset, or try again later. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |

## Publication, limits, and permissions {#publication}

These errors occur when you publish or manage compositions.

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170042-400** | You have reached the limitation of 50 active compositions authorized in the inventory. You cannot add a new one. | You reached the limit of 50 published compositions in the sandbox. Compositions created with federated audience composition are not counted. Delete a composition you no longer need, then publish the new one. [Learn more](../start/guardrails.md#audience) |
| **CJMRT-170043-412** | The composition has been modified. Please refresh the page. | The composition was modified by someone else. Refresh the page, then make your change again. [Learn more](get-started-audience-orchestration.md#access) |
| **CJMRT-170046-413** | Publishing this composition may impact system performance. Please consider decreasing the audience size before continuing. | Publishing this composition may affect system performance (warning). Reduce the size of the audience before you continue. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#publish){target="_blank"} |
| **CJMRT-170047-424** | Please ensure associated audience from this composition are not used in any downstream activations or as a building block of another audience. | The audiences of this composition are used in an activation or in another audience. Remove them from there, then delete the composition. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/sandbox/ui/user-guide.html#delete-audience-compositions){target="_blank"} |
| **CJMRT-170056-409** | Only one composition evaluation job can be queued at a time. Please try again later. | Only one composition evaluation can be queued at a time. Wait for the current evaluation to end, then try again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#publish){target="_blank"} |
| **CJMRT-170017-403** | The client is not authorized for access. | Your user does not have the permission needed to publish or manage the composition. Ask your administrator to grant it. [Learn more](../administration/ootb-permissions.md) |
| **CJMRT-170024-403** | You don't have permission to publish this rule.  Please contact your administrator or remove unauthorized settings. | Your user does not have the permission needed to publish or manage the composition. Ask your administrator to grant it, or remove the settings that are not allowed. [Learn more](../administration/ootb-permissions.md) |
| **CJMRT-170028-403** | Missing required permissions. | Your user does not have the permission needed to publish or manage the composition. Ask your administrator to grant it. [Learn more](../administration/ootb-permissions.md) |

## Related topics {#related}

* [Get started with audience composition](get-started-audience-orchestration.md)
* [Leverage enrichment attributes](enrichment-attributes.md)
* [Federated audience composition](federated-audience-composition.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/audience/ai-augmented-audience-composition-errors.md}}
