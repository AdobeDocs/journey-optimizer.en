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
hide: true
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
| **CJMRT-170002-400**, **CJMRT-170004-400**, **CJMRT-170006-400** | The composition must begin with a single audience.<br/>The composition must start with a valid dataset or segment.<br/>The composition started without an audience. | A composition must begin with a single audience, or with a valid dataset or segment. Add an audience as the first activity. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170005-400**, **CJMRT-170003-400** | The composition contains disconnected operations.<br/>The composition must not contain cyclic references. | Every activity must be connected to the workflow, and the workflow cannot loop back on itself. Connect or delete the disconnected activities, and remove the loop. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170007-400** | The composition must end with a Save operation. | A composition must end with a Save activity. Add a Save activity to each path. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170008-400**, **CJMRT-170001-400**, **CJMRT-170039-400** | The composition cannot be empty.<br/>Invalid references present in the composition.<br/>Invalid Composition. | The composition is empty or contains an invalid reference. Add the activities, or fix the activity named in the message. [Learn more](get-started-audience-orchestration.md#create) |

## Audiences {#audiences}

These errors occur when you select or name the audiences of a composition.

See also [Get started with audience composition](get-started-audience-orchestration.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170011-400** | You need to select at least one audience. | Select at least one audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#add-audience){target="_blank"} |
| **CJMRT-170016-400** | Audience name {label} already exists. Please choose a different name. | An audience with this name already exists. Choose a different audience name. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170025-404** | One or more audience used cannot be found.  Please select another audience. | An audience used in the composition cannot be found. Select another audience. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |
| **CJMRT-170029-400**, **CJMRT-170045-400** | One or more selected audiences is using a different merge policy than the one associated with the composition. Please choose a different audience.<br/>One or more of the selected audiences cannot be used in this composition. | The audiences of a composition must use the merge policy of the composition, and some audiences cannot be used in a composition. Select audiences that use the same merge policy. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#audience-block){target="_blank"} |

## Activities {#activities}

These errors occur when an activity of a composition is not configured completely.

See also [the audience composition guide](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition){target="_blank"}.

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170015-400** | Sum of all branches should be equal to 100. | The percentages of the branches of a split must add up to 100. Adjust the percentages. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#split-percentage){target="_blank"} |
| **CJMRT-170033-400** | Please select a Target dimension | Select a target dimension. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170013-400** | Limit must be positive. | The limit of the **[!UICONTROL Rank]** activity must be a positive number. Enter a limit greater than 0. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#rank-block){target="_blank"} |
| **CJMRT-170012-400**, **CJMRT-170014-400**, **CJMRT-170027-400** | Path cannot be empty.<br/>Please supply a value for all fields.<br/>Required fields in {param} must not be empty. | An activity has an empty or invalid value (path or a required field). Open the activity named in the message and enter a valid value. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#build-rule){target="_blank"} |
| **CJMRT-170023-400**, **CJMRT-170030-400**, **CJMRT-170031-400** | Excluded values cannot be empty.<br/>Please provide a filter key.<br/>Please provide a filter value. | The **[!UICONTROL Exclude]** activity or a filter is incomplete. Enter the excluded values, the filter key, and the filter value. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#exclude-attribute){target="_blank"} |

## Enrichment {#enrichment}

These errors occur when you configure an enrichment with a dataset.

See also [Leverage enrichment attributes](enrichment-attributes.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170034-400**, **CJMRT-170060-404** | Enrichment dataset not found.<br/>The enrichment dataset was not found. Please use a valid enrichment dataset or try again later. | The enrichment dataset cannot be found. Select an existing dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170035-400**, **CJMRT-170036-400** | Please select a source join key.<br/>Please select an enrichment dataset join key. | Select the join key of the audience and the join key of the enrichment dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170037-400**, **CJMRT-170050-400** | Must select at least one enrichment attribute.<br/>Please select an audience enrichment attribute. | Select at least one attribute of the enrichment dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170040-400**, **CJMRT-170041-400** | The selected enrichment dataset is greater than 1 GB.<br/>The selected dataset is empty. Please check and try again. | The enrichment dataset must not be empty, and it must be 1 GB or smaller. Select another dataset, or reduce its size. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170048-428**, **CJMRT-170058-400** | The enrichment dataset must be associated with a schema.<br/>The selected enrichment dataset must have a primary identity descriptor defined in its schema. | The enrichment dataset must be associated with a schema, and the schema must have a primary identity. Update the schema, or select another dataset. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170051-404**, **CJMRT-170052-400**, **CJMRT-170053-404**, **CJMRT-170054-404** | The enrichment attribute schema could not be found. Please verify the schema exists and try again.<br/>The enrichment attribute schema properties are missing or empty. Please ensure the properties are defined and try again.<br/>The specified enrichment schema path could not be found. Please verify the path exists and try again.<br/>The source schema for the enrichment attribute was not found. Please verify the schema exists and try again. | The schema or the path of the enrichment attribute cannot be found, or has no properties. Check that the schema exists and defines the attribute, then select it again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |
| **CJMRT-170059-424**, **CJMRT-170061-424** | There was an error using this enrichment dataset. Please use a valid enrichment dataset or try again later. | The enrichment dataset cannot be used. Select a valid dataset, or try again later. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#enrich-block){target="_blank"} |

## Publication, limits, and permissions {#publication}

These errors occur when you publish or manage compositions.

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-170042-400** | You have reached the limitation of 50 active compositions authorized in the inventory. You cannot add a new one. | You reached the maximum number of compositions that the inventory accepts. Delete a composition you no longer need, then create the new one. [Learn more](get-started-audience-orchestration.md#create) |
| **CJMRT-170043-412** | The composition has been modified. Please refresh the page. | The composition was modified by someone else. Refresh the page, then make your change again. [Learn more](get-started-audience-orchestration.md#access) |
| **CJMRT-170046-413** | Publishing this composition may impact system performance. Please consider decreasing the audience size before continuing. | Publishing this composition may affect system performance (warning). Reduce the size of the audience before you continue. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#publish){target="_blank"} |
| **CJMRT-170047-424** | Please ensure associated audience from this composition are not used in any downstream activations or as a building block of another audience. | The audiences of this composition are used in an activation or in another audience. Remove them from there, then delete the composition. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/sandbox/ui/user-guide.html#delete-audience-compositions){target="_blank"} |
| **CJMRT-170056-409** | Only one composition evaluation job can be queued at a time. Please try again later. | Only one composition evaluation can be queued at a time. Wait for the current evaluation to end, then try again. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition#publish){target="_blank"} |
| **CJMRT-170017-403**, **CJMRT-170024-403**, **CJMRT-170028-403** | The client is not authorized for access.<br/>You don't have permission to publish this rule.  Please contact your administrator or remove unauthorized settings.<br/>Missing required permissions. | Your user does not have the permission needed to publish or manage the composition. Ask your administrator to grant it, or remove the settings that are not allowed. [Learn more](../administration/ootb-permissions.md) |

## Related topics {#related}

* [Get started with audience composition](get-started-audience-orchestration.md)
* [Leverage enrichment attributes](enrichment-attributes.md)
* [Federated audience composition](federated-audience-composition.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)
