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
| **CJMPTS-1004-400** | Only test profiles are allowed. | Proofs and previews use test profiles only. Select profiles that are flagged as test profiles. [Learn more](../audience/creating-test-profiles.md) |
| **CJMPTS-1021-400**, **CJMPTS-1022-500** | The number of recipient emails in the submit proof post body have exceeded the limit. Please reduce the recipient emails and try again.<br/>The number of recipient emails in the proof job have exceeded the limit. Please reduce the recipient emails and try again. | A proof can have up to ten recipients. Remove recipients, then send the proof again. [Learn more](proofs.md#send-proofs-steps) |
| **CJMPTS-1300-400** | Proof/Rendering failed due to some syntax errors related to personalisations in your content. Please check error details in Alerts section. | The proof or the preview failed because of a syntax error in a personalization expression. Open the alerts to find the expression, then fix it in the personalization editor. [Learn more](../personalization/personalization-syntax.md) |
| **CJMPTS-1023-500** | Couldn't continue proof job processing due to missing IMS user token. Please provide valid IMS user token and try again. | Your session is not valid for the proof. Log out and log in again, then send the proof again. [Learn more](proofs.md#send-proofs-steps) |
| **CJMPTS-1503-400**, **CJMPTS-1504-400** | Message publishing is in progress.<br/>Errors during message publication. | The message is being published, or its publication has errors. Wait until the publication completes, and fix the errors reported on the message. [Learn more](proofs.md) |
| **CJMPTS-1028-403**, **CJMPTS-1029-403**, **CJMPTS-1042-403**, **CJMPTS-1036-401**, **CJMPTS-2101-403**, **CJMPTS-2103-401** | You do not have Write permission on this sandbox. Contact your Administrator to get access.<br/>You do not have Read permission on this sandbox. Contact your Administrator to get access.<br/>You do not have Read and Delete permissions on this sandbox. Contact your Administrator to get access.<br/>You do not have permissions on this sandbox to perform this action. Contact your Administrator to get proper permissions. | Your user does not have the permission needed on the sandbox. Ask your administrator to grant it on your product profile. [Learn more](../administration/ootb-permissions.md) |

## Simulated users {#simulated-users}

These errors occur when you create or edit simulated users to run a journey simulation.

See also [Create and manage simulated users](../building-journeys/simulate-journey.md#test-users).

| Error code | Message | How to fix |
|---|---|---|
| **AJOTDS-000001-409** | A simulated user already exists with the combination of namespace '{namespace}' and identity value '{identityValue}'. Use the existing user or choose a different identity. | A simulated user already exists with this identity namespace and identity value. Use the existing user, or enter a different identity value. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000001-404**, **AJOTDS-000002-404** | Simulated user not found with ID '{simulatedUserId}'. Verify the ID or create a new simulated user.<br/>Simulated user not found with namespace '{namespace}' and identity value '{identityValue}'. Verify the identity or create a new simulated user. | The simulated user cannot be found. Check the user in the inventory, or create it. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000035-400**, **AJOTDS-000036-400**, **AJOTDS-000007-400** | Identity namespace is required but missing for entity type '{entityType}'. Provide the namespace and retry.<br/>Identity value is required but missing for entity type '{entityType}'. Provide the identity value and retry.<br/>Identity map validation failed: unable to extract identity value from field '{field}' with namespace '{rejectedValue}'. Ensure the identity namespace/value are provided correctly and retry. | A simulated user needs an identity namespace and an identity value. Enter both, and check that the namespace is valid. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000009-400**, **AJOTDS-000011-400**, **AJOTDS-000022-400** | Data does not conform to XDM schema '{schemaId}'. Validation errors: {validationErrors}. Correct the input data per the validation errors and retry.<br/>Entity validation failed against schema for entity type '{entityType}'. Correct the input data to satisfy the schema and retry.<br/>Entity XDM validation failed against schema '{schemaId}' for entity type '{entityType}' at path '{jsonPath}'. Validation errors: {validationErrors}. Error count: {errorCount}. Correct the input data per validation errors and retry. | The attributes of the simulated user do not match the profile schema. Correct the attributes named in the message, then save the user again. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000010-400** | Cannot modify immutable field '{field}'. Current value: '{rejectedValue}'. You cannot modify immutable fields; please create a new simulated user if needed. | This field cannot be modified after the simulated user is created. Create a new simulated user instead. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000013-400**, **AJOTDS-000014-400** | Number of simulated users in this request exceeds the maximum allowed ({maxBatchSize}); received {actualBatchSize}. Reduce the number of simulated users and retry.<br/>Batch request cannot be empty. Add at least one user and retry. | A simulation takes at least one simulated user, and no more than the maximum shown in the message. Add or remove simulated users. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000037-400** | Simulated user limit exceeded. Current count: {currentCount} exceeds maximum limit: {maxUserLimit}. Archive/delete unused users or contact support. | You reached the maximum number of simulated users. Delete the simulated users you do not need, then create the new one. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000002-409**, **AJOTDS-000001-412**, **AJOTDS-000007-500** | The resource was modified by another operation. Expected version '{expectedVersion}' for operation '{operation}' on user '{simulatedUserId}'. Refresh and retry; if it persists, contact support.<br/>Something went wrong, please refresh the page and retry. | The simulated user was modified by someone else, or by another action. Refresh the page, then make your change again. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **AJOTDS-000025-400** | Only profile schemas are supported for this operation. Provided schema '{rejectedValue}' is not allowed. Use the profile schema option and retry. | Only profile attributes can be used. Select attributes from the profile schema. [Learn more](../building-journeys/simulate-journey.md#test-users) |
| **CJMSAS-000002-429** | You have reached the request limit for this service. Wait a few moments, then try again. If this continues, reduce how frequently you send requests or contact Adobe Customer Care. | You sent too many requests to the service. Wait a few moments, then try again. [Learn more](../building-journeys/simulate-journey.md) |
| **AJOTDS-000015-400**, **AJOTDS-000016-400**, **AJOTDS-000019-400** | Audience ID is required for entity type '{entityType}'. Provide an audience ID and retry.<br/>Audience type is required for entity type '{entityType}'. Provide an audience type and retry.<br/>Duplicate audience found in request for entity type '{entityType}'. Audience ID: {audienceId}, Type: {audienceType}. Remove duplicate entries and retry. | The audience membership of the simulated user is incomplete or duplicated. Select each audience once, with its type. [Learn more](../building-journeys/simulate-journey.md#test-users) |

## Related topics {#related}

* [Get started with preview and test](preview-test.md)
* [Send proofs using test profile data](proofs.md)
* [Get started with journey simulation](../building-journeys/simulate-journey-gs.md)
* [Simulate your journey](../building-journeys/simulate-journey.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/content-management/ai-augmented-proof-simulation-errors.md}}
