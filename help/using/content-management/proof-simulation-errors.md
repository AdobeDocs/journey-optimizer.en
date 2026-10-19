---
solution: Journey Optimizer
product: journey optimizer
title: Proof and simulation errors
description: Learn what common errors mean when you send proofs and preview content, and when you create simulated users for a journey simulation in Adobe Journey Optimizer, and how to fix them
feature: Proofs, Preview, Test Profiles
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, proof, preview, test profiles, simulation, simulated users
---
# Proof and simulation errors {#proof-simulation-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you send proofs, preview content with test profiles, or create the simulated users of a journey simulation.

>[!ENDSHADEBOX]

Errors use the prefixes **CJMPTS** (proofs and previews), **AJOTDS** (simulated users), and **CJMSAS**, followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Proofs and previews {#proofs}

These errors occur when you send a proof or preview content with test profiles.

See also [Send proofs using test profile data](proofs.md) and [Get started with preview and test](preview-test.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMPTS-1004-400** | Only test profiles are allowed. | Select only profiles that are flagged as test profiles. [Learn more](../audience/creating-test-profiles.md) |
| **CJMPTS-1021-400** | The number of recipient emails in the submit proof post body have exceeded the limit. Please reduce the recipient emails and try again. | Remove recipients until ten or fewer remain, then send the proof again. [Learn more](proofs.md#send-proofs-steps) |
| **CJMPTS-1022-500** | The number of recipient emails in the proof job have exceeded the limit. Please reduce the recipient emails and try again. | Remove recipients until ten or fewer remain, then send the proof again. [Learn more](proofs.md#send-proofs-steps) |
| **CJMPTS-1300-400** | Proof/Rendering failed due to some syntax errors related to personalisations in your content. Please check error details in Alerts section. | Open the alerts to find the expression with the syntax error, then fix it in the personalization editor. [Learn more](../personalization/personalization-syntax.md) |
| **CJMPTS-1023-500** | Couldn't continue proof job processing due to missing IMS user token. Please provide valid IMS user token and try again. | Log out and log in again, then send the proof again. [Learn more](proofs.md#send-proofs-steps) |
| **CJMPTS-1503-400** | Message publishing is in progress. | Wait until the publication completes, then send the proof again. [Learn more](proofs.md) |
| **CJMPTS-1504-400** | Errors during message publication. | Fix the errors reported on the message, then try again. [Learn more](proofs.md) |
| **CJMPTS-1028-403** | You do not have Write permission on this sandbox. Contact your Administrator to get access. | Ask your administrator to grant you the Write permission on this sandbox through your role. [Learn more](../administration/ootb-permissions.md) |
| **CJMPTS-1029-403** | You do not have Read permission on this sandbox. Contact your Administrator to get access. | Ask your administrator to grant you the Read permission on this sandbox through your role. [Learn more](../administration/ootb-permissions.md) |
| **CJMPTS-1042-403** | You do not have Read and Delete permissions on this sandbox. Contact your Administrator to get access. | Ask your administrator to grant you the Read and Delete permissions on this sandbox through your role. [Learn more](../administration/ootb-permissions.md) |
| **CJMPTS-1036-401** | You do not have permissions on this sandbox to perform this action. Contact your Administrator to get proper permissions. | Ask your administrator to grant you the permission needed for this action on this sandbox through your role. [Learn more](../administration/ootb-permissions.md) |
| **CJMPTS-2101-403** | You do not have permissions on this sandbox to perform this action. Contact your Administrator to get proper permissions. | Ask your administrator to grant you the permission needed for this action on this sandbox through your role. [Learn more](../administration/ootb-permissions.md) |
| **CJMPTS-2103-401** | You do not have permissions on this sandbox to perform this action. Contact your Administrator to get proper permissions. | Ask your administrator to grant you the permission needed for this action on this sandbox through your role. [Learn more](../administration/ootb-permissions.md) |

## Simulated users {#simulated-users}

These errors occur when you create or edit simulated users to run a journey simulation.

See also [Create and manage simulated users](../building-journeys/simulate-journey.md#test-users).

| Error code | Message | How to fix |
|---|---|---|
| **AJOTDS-000001-409** | A simulated user already exists with the combination of namespace '{namespace}' and identity value '{identityValue}'. Use the existing user or choose a different identity. | Use the existing user, or enter a different identity value. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000001-404** | Simulated user not found with ID '{simulatedUserId}'. Verify the ID or create a new simulated user. | Check the ID against the simulated users in **[!UICONTROL Browse inventory]**, or create the simulated user. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000002-404** | Simulated user not found with namespace '{namespace}' and identity value '{identityValue}'. Verify the identity or create a new simulated user. | Check the namespace and the identity value against the simulated users in **[!UICONTROL Browse inventory]**, or create the simulated user. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000035-400** | Identity namespace is required but missing for entity type '{entityType}'. Provide the namespace and retry. | Enter a valid identity namespace for the simulated user. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000036-400** | Identity value is required but missing for entity type '{entityType}'. Provide the identity value and retry. | Enter the identity value for the simulated user. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000007-400** | Identity map validation failed: unable to extract identity value from field '{field}' with namespace '{rejectedValue}'. Ensure the identity namespace/value are provided correctly and retry. | Enter the identity namespace and the identity value correctly for the field named in the message. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000009-400** | Data does not conform to XDM schema '{schemaId}'. Validation errors: {validationErrors}. Correct the input data per the validation errors and retry. | Correct the attributes listed in the validation errors, then save the user again. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000011-400** | Entity validation failed against schema for entity type '{entityType}'. Correct the input data to satisfy the schema and retry. | Correct the attributes of the simulated user so that they match the profile schema, then save the user again. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000022-400** | Entity XDM validation failed against schema '{schemaId}' for entity type '{entityType}' at path '{jsonPath}'. Validation errors: {validationErrors}. Error count: {errorCount}. Correct the input data per validation errors and retry. | Correct the attribute at the path given in the message and the other attributes listed in the validation errors, then save the user again. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000010-400** | Cannot modify immutable field '{field}'. Current value: '{rejectedValue}'. You cannot modify immutable fields; please create a new simulated user if needed. | Create a new simulated user with the value you need instead of editing this field. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000013-400** | Number of simulated users in this request exceeds the maximum allowed ({maxBatchSize}); received {actualBatchSize}. Reduce the number of simulated users and retry. | Remove simulated users from the request until it is within the maximum shown in the message. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000014-400** | Batch request cannot be empty. Add at least one user and retry. | Add at least one simulated user to the request. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000037-400** | Simulated user limit exceeded. Current count: {currentCount} exceeds maximum limit: {maxUserLimit}. Archive/delete unused users or contact support. | Delete the simulated users you do not need, then create the new one. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000002-409** | The resource was modified by another operation. Expected version '{expectedVersion}' for operation '{operation}' on user '{simulatedUserId}'. Refresh and retry; if it persists, contact support. | Refresh the page, then make your change again. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000001-412** | Something went wrong, please refresh the page and retry. | Refresh the page, then make your change again. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000007-500** | Something went wrong, please refresh the page and retry. | Refresh the page, then try again. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000025-400** | Only profile schemas are supported for this operation. Provided schema '{rejectedValue}' is not allowed. Use the profile schema option and retry. | Select attributes from the profile schema only. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **CJMSAS-000002-429** | You have reached the request limit for this service. Wait a few moments, then try again. If this continues, reduce how frequently you send requests or contact Adobe Customer Care. | Wait a few moments, then try again. If this continues, reduce how frequently you send requests. [Learn more](../building-journeys/simulate-journey.md) |
| **AJOTDS-000015-400** | Audience ID is required for entity type '{entityType}'. Provide an audience ID and retry. | Select the audience for the simulated user. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000016-400** | Audience type is required for entity type '{entityType}'. Provide an audience type and retry. | Select the audience type for the simulated user. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000019-400** | Duplicate audience found in request for entity type '{entityType}'. Audience ID: {audienceId}, Type: {audienceType}. Remove duplicate entries and retry. | Remove the duplicate entries so that each audience appears once. [Learn more](../building-journeys/simulate-journey.md#test-users) |

## Related topics {#related}

* [Get started with preview and test](preview-test.md)
* [Send proofs using test profile data](proofs.md)
* [Get started with journey simulation](../building-journeys/simulate-journey-gs.md)
* [Simulate your journey](../building-journeys/simulate-journey.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/content-management/ai-augmented-proof-simulation-errors.md}}
