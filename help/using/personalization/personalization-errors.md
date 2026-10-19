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

## Variables and paths {#variables}

These errors occur when an expression refers to a field, a variable, or a namespace that cannot be resolved, or has the wrong type.

See also [Validation mechanisms](personalization-build-expressions.md#validation-mechanisms) and [Available namespaces](personalization-syntax.md#namespaces).

| Error code | Message | How to fix |
|---|---|---|
| **CJMTL-010001-422** | {variable} not found | The variable named in the message does not exist in the schema or in the context of the message. Check its name and path in the personalization editor, and use a field of the schema. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-010001-422** | Path {variable} not found | The path named in the message does not exist in the schema or in the context of the message. Check the path in the personalization editor, and use a field of the schema. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-070003-422** | Variable {variable} not found in the execution context. | The variable named in the message is not available in the execution context of the message. Check its name in the personalization editor, and use a field of the schema. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-070008-422** | Path {path} is not supported | The path named in the message is not supported. Check the path in the personalization editor, and use a field of the schema. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMTL-010008-422** | Namespace not found for {path} | The namespace of the expression is not available. Use one of the available namespaces: profile, audience, offers, or the contextual attributes. [Learn more](personalization-syntax.md#namespaces) |
| **CJMTL-010002-422** | Type mismatch for variable {variable}. Expected type is {expectedType}, but found {foundType} | The variable has a different type than the one the expression expects, for example a string used in a loop that needs an array. Use a variable of the expected type. [Learn more](personalization-syntax.md#type-coercion) |
| **CJMRT-010002-422** | Type mismatch for variable {variable}. Expected: {expectedType}. Found: {foundType} | The variable has a different type than the one the expression expects, for example a string used in a loop that needs an array. Use a variable of the expected type. [Learn more](personalization-syntax.md#type-coercion) |
| **CJMRT-070007-422** | Variable {variable} is expected to be {expected}. Found {found} instead. | The variable has a different type than the one the expression expects. Use a variable of the type shown in the message. [Learn more](personalization-syntax.md#type-coercion) |
| **CJMRT-070002-422** | Variable {variable} is expected to be an array. | The expression expects an array, for example in a loop, but the variable has another type. Use an array variable. [Learn more](personalization-syntax.md#type-coercion) |
| **CJMTL-010013-422** | Invalid variable name {variableName} | The name of a variable defined with the Let helper is not valid. Start the name with a letter and use only letters and numbers. [Learn more](functions/helpers.md#let) |
| **CJMTL-010014-422** | Invalid variable name {variableName}. A variable name must start with a letter and only contain alphanumeric characters. | The name of a variable defined with the Let helper is not valid. Start the name with a letter and use only letters and numbers. [Learn more](functions/helpers.md#let) |
| **CJMRT-070001-422** | {start} is out of bounds. Variable {variable} size is {length} | The start position is outside the size of the variable. Use a value smaller than the size shown in the message. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMRT-070005-422** | The expression should be a String value. Found : {expression} | The expression must be a string value. Enter a string, or convert the value to a string. [Learn more](personalization-syntax.md#literal-types) |

## Helpers {#helpers}

These errors occur when a helper is not known or is called with missing parameters.

See also [Helper functions](functions/helpers.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMTL-010012-422** | Invalid helper {command} | The helper is not valid. Check its name in the list of helpers. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMTL-010003-422** | Input parameters not defined for helper {helper} | The helper named in the message is called without its input parameters. Add the parameters of the helper. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMTL-010009-422** | Insufficient parameters for helper {helper}. Undefined {param} | The helper named in the message has too few parameters. Add the undefined parameter named in the message. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMRT-010003-422** | Params not defined for helper: {helper} | The helper named in the message is called without its parameters. Add the parameters of the helper. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMRT-070004-422** | Insufficient arguments for {helperName}. Missing argument {missingArgument} | The helper named in the message has too few arguments. Add the missing argument named in the message. [Learn more](personalization-syntax.md#helpers-all) |

## Syntax and content validation {#syntax}

These errors occur when you validate or publish content that has an expression with a syntax error.

See also [Validation mechanisms](personalization-build-expressions.md#validation-mechanisms).

| Error code | Message | How to fix |
|---|---|---|
| **CJMTL-010004-422** | Invalid syntax {reason} | The expression has a syntax error, described by the reason in the message. Check the brackets, the quotes, and the helper syntax at that place. Use the **[!UICONTROL Validate]** button of the personalization editor. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMTL-010011-422** | Invalid syntax {message} | The expression has a syntax error, described in the message. Check the brackets, the quotes, and the helper syntax at that place. Use the **[!UICONTROL Validate]** button of the personalization editor. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMTL-010015-422** | Invalid assignment syntax. Expression {expression} is invalid. | The assignment expression named in the message is not valid. Check the syntax of the assignment, including the brackets and the quotes. Use the **[!UICONTROL Validate]** button of the personalization editor. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-010004-422** | Invalid handlebars syntax {reason} | The expression has a handlebars syntax error, described by the reason in the message. Check the brackets, the quotes, and the helper syntax at that place. Use the **[!UICONTROL Validate]** button of the personalization editor. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-071011-400** | Syntax errors found | The message does not say where the syntax errors are. Use the **[!UICONTROL Validate]** button of the personalization editor to find them, then check the brackets, the quotes, and the helper syntax. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-130001-400** | The field {fieldName} of {channel} variant is malformed | A field of the message variant is malformed. Open the field named in the message and fix its expression. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-130004-400** | The {variable} variable of the field {fieldName} of {channel} variant is malformed: Position: {position} | A variable of a field of the message variant is malformed. Open the field named in the message and fix the variable at the position shown. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-071012-404** | No segment definition found for {segmentId} | The audience (segment definition) used in the expression cannot be found. Select an audience that exists in the sandbox. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-130003-422** | Profile schema does not contain the required field: {fieldName} for channel: {channel} | The profile schema does not contain the field that the channel configuration needs. Add the field to the schema, or select another field in the channel configuration. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMRT-000069-400** | The HTML content is not valid: {errorMessage} | The HTML content is not valid. Check the HTML for unclosed tags, and use the content checks. [Learn more](../email/content-check.md) |
| **CJMTL-010019-422** | The template rendering size limit of {limit} bytes is exceeded. Please update and try again. | The rendered message is larger than the size limit shown in the message. Reduce the content, or the data inserted by the expressions. [Learn more](../start/guardrails.md#message-content-size) |

## URL parameter encryption keys {#encryption}

These errors occur when you create or use an encryption key to encrypt URL parameters.

See also [Encrypt URL parameters in tracking links](url-parameter-encryption.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-081601-400** | The key must be 32 bytes (256 bits), but {actualBytes} bytes were provided. Update the key to the correct length and try again. | The key does not have the required length of 256 bits (32 bytes). Generate a key of the right length, encode it in base64, and enter it again. [Learn more](url-parameter-encryption.md#create-keys) |
| **CJMRT-081602-400** | The key is not base64-encoded. Encode the key in base64 format and try again. | The key is not encoded in base64. Encode the key in base64, and enter it again. The key must be 256 bits (32 bytes) long. [Learn more](url-parameter-encryption.md#create-keys) |
| **CJMRT-081603-400** | The key name can only contain letters, numbers, and hyphens. Update the key name and try again. | The key name can contain only letters, numbers, and hyphens. Rename the key. [Learn more](url-parameter-encryption.md#create-keys) |
| **CJMRT-070011-422** | Encryption / Signing keys could not be resolved | The encryption or signing key cannot be found. Check that the key used by the encryption helper exists in the key registry of the sandbox. [Learn more](url-parameter-encryption.md#manage-keys) |

## Related topics {#related}

* [Add personalization](personalization-build-expressions.md)
* [Personalization syntax](personalization-syntax.md)
* [Helper functions](functions/helpers.md)
* [Encrypt URL parameters in tracking links](url-parameter-encryption.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/personalization/ai-augmented-personalization-errors.md}}
