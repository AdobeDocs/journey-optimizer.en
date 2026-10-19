---
solution: Journey Optimizer
product: journey optimizer
title: Personalization errors
description: Learn what common errors mean when you build and validate personalization expressions, and when you use URL parameter encryption keys in Adobe Journey Optimizer, and how to fix them
feature: Personalization
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, personalization, expression, helper, handlebars, encryption
---
# Personalization errors {#personalization-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you validate or publish content with personalization expressions, or when you create an encryption key.

>[!ENDSHADEBOX]

Personalization errors use the prefixes **CJMTL** (template rendering) and **CJMRT** (runtime), followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

If the error persists after you follow the steps, note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or [contact Adobe Support](../start/user-interface.md#support-ticket-guidelines) with these details. For all the support options, see [Getting support](../building-journeys/error-codes-reference.md#getting-support).

## Variables and paths {#variables}

These errors occur when an expression refers to a field, a variable, or a namespace that cannot be resolved, or has the wrong type.

See also [Validation mechanisms](personalization-build-expressions.md#validation-mechanisms) and [Available namespaces](personalization-syntax.md#namespaces).

| Error code | Message | How to fix |
|---|---|---|
| **CJMTL-010001-422** | {variable} not found | In the personalization editor, check the name and path of the variable, and replace it with a field defined in the schema. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-010001-422** | Path {variable} not found | In the personalization editor, check the path, and replace it with a field defined in the schema. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-070003-422** | Variable {variable} not found in the execution context. | In the personalization editor, check the name of the variable, and use a field of the schema. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-070008-422** | Path {path} is not supported | In the personalization editor, check the path, and use a field of the schema. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMTL-010008-422** | Namespace not found for {path} | Start the expression with one of the available namespaces: profile, audience, offers, or the contextual attributes. [Learn more](personalization-syntax.md#namespaces) |
| **CJMTL-010002-422** | Type mismatch for variable {variable}. Expected type is {expectedType}, but found {foundType} | Use a variable of the type shown in the message, for example an array in a loop. If a numeric or boolean value is stored as a string, convert it with stringToNumber() or toBool(). [Learn more](personalization-syntax.md#type-coercion) |
| **CJMRT-010002-422** | Type mismatch for variable {variable}. Expected: {expectedType}. Found: {foundType} | Use a variable of the type shown in the message, for example an array in a loop. If a numeric or boolean value is stored as a string, convert it with stringToNumber() or toBool(). [Learn more](personalization-syntax.md#type-coercion) |
| **CJMRT-070007-422** | Variable {variable} is expected to be {expected}. Found {found} instead. | Use a variable of the type shown in the message, or convert the value with stringToNumber() or toBool() if it is stored as a string. [Learn more](personalization-syntax.md#type-coercion) |
| **CJMRT-070002-422** | Variable {variable} is expected to be an array. | Replace the variable with an array variable, or remove the loop. [Learn more](personalization-syntax.md#type-coercion) |
| **CJMTL-010013-422** | Invalid variable name {variableName} | Rename the variable defined with the Let helper: start the name with a letter and use only letters and numbers. [Learn more](functions/helpers.md#let) |
| **CJMTL-010014-422** | Invalid variable name {variableName}. A variable name must start with a letter and only contain alphanumeric characters. | Rename the variable defined with the Let helper: start the name with a letter and use only letters and numbers. [Learn more](functions/helpers.md#let) |
| **CJMRT-070001-422** | {start} is out of bounds. Variable {variable} size is {length} | Use a start position smaller than the size of the variable shown in the message. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMRT-070005-422** | The expression should be a String value. Found : {expression} | Enter a string value surrounded by double quotes, or convert the value to a string. [Learn more](personalization-syntax.md#literal-types) |

## Helpers {#helpers}

These errors occur when a helper is not known or is called with missing parameters.

See also [Helper functions](functions/helpers.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMTL-010012-422** | Invalid helper {command} | Check the helper name against the list of helpers, and correct it. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMTL-010003-422** | Input parameters not defined for helper {helper} | Add the input parameters of the helper named in the message. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMTL-010009-422** | Insufficient parameters for helper {helper}. Undefined {param} | Add the undefined parameter named in the message to the helper. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMRT-010003-422** | Params not defined for helper: {helper} | Add the parameters of the helper named in the message. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMRT-070004-422** | Insufficient arguments for {helperName}. Missing argument {missingArgument} | Add the missing argument named in the message to the helper. [Learn more](personalization-syntax.md#helpers-all) |

## Syntax and content validation {#syntax}

These errors occur when you validate or publish content that has an expression with a syntax error.

See also [Validation mechanisms](personalization-build-expressions.md#validation-mechanisms).

| Error code | Message | How to fix |
|---|---|---|
| **CJMTL-010004-422** | Invalid syntax {reason} | Check the brackets, the quotes, and the helper syntax where the reason in the message points, then click **[!UICONTROL Validate]** in the personalization editor. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMTL-010011-422** | Invalid syntax {message} | Check the brackets, the quotes, and the helper syntax where the message points, then click **[!UICONTROL Validate]** in the personalization editor. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMTL-010015-422** | Invalid assignment syntax. Expression {expression} is invalid. | Check the syntax of the assignment expression named in the message, including the brackets and the quotes, then click **[!UICONTROL Validate]** in the personalization editor. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-010004-422** | Invalid handlebars syntax {reason} | Check the brackets, the quotes, and the helper syntax where the reason in the message points, then click **[!UICONTROL Validate]** in the personalization editor. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-071011-400** | Syntax errors found | Click **[!UICONTROL Validate]** in the personalization editor to find the syntax errors, then check the brackets, the quotes, and the helper syntax. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-130001-400** | The field {fieldName} of {channel} variant is malformed | Open the field named in the message in the content of the variant, and fix its expression. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-130004-400** | The {variable} variable of the field {fieldName} of {channel} variant is malformed: Position: {position} | Open the field named in the message, and fix the variable at the position shown. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-071012-404** | No segment definition found for {segmentId} | Replace the audience in the expression with one that exists in the current sandbox. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-130003-422** | Profile schema does not contain the required field: {fieldName} for channel: {channel} | Add the field to the profile schema, or select another field in the channel configuration. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMRT-000069-400** | The HTML content is not valid: {errorMessage} | Open the content checks in the Email Designer, and fix the HTML issues they detect. [Learn more](../email/content-check.md) |
| **CJMTL-010019-422** | The template rendering size limit of {limit} bytes is exceeded. Please update and try again. | Reduce the content, or the data inserted by the expressions, until the rendered message is under the limit shown in the message. [Learn more](../start/guardrails.md#message-content-size) |

## URL parameter encryption keys {#encryption}

These errors occur when you create or use an encryption key to encrypt URL parameters.

See also [Encrypt URL parameters in tracking links](url-parameter-encryption.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-081601-400** | The key must be 32 bytes (256 bits), but {actualBytes} bytes were provided. Update the key to the correct length and try again. | Generate a key of 32 bytes (256 bits), encode it in base64, and create it again in the **[!UICONTROL Key registry]** (**[!UICONTROL Administration]** > **[!UICONTROL Configurations]** > **[!UICONTROL Manage]**). [Learn more](url-parameter-encryption.md#create-keys) |
| **CJMRT-081602-400** | The key is not base64-encoded. Encode the key in base64 format and try again. | Encode the key (256 bits, 32 bytes) in base64, and create it again in the **[!UICONTROL Key registry]**. [Learn more](url-parameter-encryption.md#create-keys) |
| **CJMRT-081603-400** | The key name can only contain letters, numbers, and hyphens. Update the key name and try again. | Rename the key using only letters, numbers, and hyphens. [Learn more](url-parameter-encryption.md#create-keys) |
| **CJMRT-070011-422** | Encryption / Signing keys could not be resolved | Check that the key used by the encryption helper exists and has the **[!UICONTROL Active]** status in the **[!UICONTROL Key registry]** of the current sandbox. [Learn more](url-parameter-encryption.md#manage-keys) |

## Related topics {#related}

* [Add personalization](personalization-build-expressions.md)
* [Personalization syntax](personalization-syntax.md)
* [Helper functions](functions/helpers.md)
* [Encrypt URL parameters in tracking links](url-parameter-encryption.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/personalization/ai-augmented-personalization-errors.md}}
