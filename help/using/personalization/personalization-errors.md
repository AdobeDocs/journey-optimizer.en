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
hide: true
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
| **CJMTL-010001-422**, **CJMRT-010001-422**, **CJMRT-070003-422**, **CJMRT-070008-422** | {variable} not found<br/>Path {variable} not found<br/>Variable {variable} not found in the execution context.<br/>Path {path} is not supported | The field or variable named in the message does not exist in the schema or in the context of the message. Check its name and path in the personalization editor, and use a field of the schema. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMTL-010008-422** | Namespace not found for {path} | The namespace of the expression is not available. Use one of the available namespaces: profile, audience, offers, or the contextual attributes. [Learn more](personalization-syntax.md#namespaces) |
| **CJMTL-010002-422**, **CJMRT-010002-422**, **CJMRT-070007-422**, **CJMRT-070002-422** | Type mismatch for variable {variable}. Expected type is {expectedType}, but found {foundType}<br/>Type mismatch for variable {variable}. Expected: {expectedType}. Found: {foundType}<br/>Variable {variable} is expected to be {expected}. Found {found} instead.<br/>Variable {variable} is expected to be an array. | The variable has a different type than the one the expression expects, for example a string used in a loop that needs an array. Use a variable of the expected type. [Learn more](personalization-syntax.md#type-coercion) |
| **CJMTL-010013-422**, **CJMTL-010014-422** | Invalid variable name {variableName}<br/>Invalid variable name {variableName}. A variable name must start with a letter and only contain alphanumeric characters. | The name of a variable defined with the Let helper is not valid. Start the name with a letter and use only letters and numbers. [Learn more](functions/helpers.md#let) |
| **CJMRT-070001-422** | {start} is out of bounds. Variable {variable} size is {length} | The index is outside the size of the array. Use an index smaller than the number of elements. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMRT-070005-422** | The expression should be a String value. Found : {expression} | The helper expects a string value. Enter a string, or convert the value to a string. [Learn more](personalization-syntax.md#literal-types) |

## Helpers {#helpers}

These errors occur when a helper is not known or is called with missing parameters.

See also [Helper functions](functions/helpers.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMTL-010012-422** | Invalid helper {command} | The helper is not valid. Check its name in the list of helpers. [Learn more](personalization-syntax.md#helpers-all) |
| **CJMTL-010003-422**, **CJMTL-010009-422**, **CJMRT-010003-422**, **CJMRT-070004-422** | Input parameters not defined for helper {helper}<br/>Insufficient parameters for helper {helper}. Undefined {param}<br/>Params not defined for helper: {helper}<br/>Insufficient arguments for {helperName}. Missing argument {missingArgument} | The helper is called without its parameters, or with too few. Add the parameters named in the message. [Learn more](personalization-syntax.md#helpers-all) |

## Syntax and content validation {#syntax}

These errors occur when you validate or publish content that has an expression with a syntax error.

See also [Validation mechanisms](personalization-build-expressions.md#validation-mechanisms).

| Error code | Message | How to fix |
|---|---|---|
| **CJMTL-010004-422**, **CJMTL-010011-422**, **CJMTL-010015-422**, **CJMRT-010004-422**, **CJMRT-071011-400** | Invalid syntax {reason}<br/>Invalid syntax {message}<br/>Invalid assignment syntax. Expression {expression} is invalid.<br/>Invalid handlebars syntax {reason}<br/>Syntax errors found | The expression has a syntax error. Check the brackets, the quotes, and the helper syntax at the place named in the message. Use the Validate button of the personalization editor. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-130001-400**, **CJMRT-130004-400** | The field {fieldName} of {channel} variant is malformed<br/>The {variable} variable of the field {fieldName} of {channel} variant is malformed: Position: {position} | A field of the message variant has a malformed expression, at the position named in the message. Open the field and fix the expression. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-071012-404** | No segment definition found for {segmentId} | The audience (segment definition) used in the expression cannot be found. Select an audience that exists in the sandbox. [Learn more](personalization-build-expressions.md#validation-mechanisms) |
| **CJMRT-130003-422** | Profile schema does not contain the required field: {fieldName} for channel: {channel} | The profile schema does not contain the field that the channel configuration needs. Add the field to the schema, or select another field in the channel configuration. [Learn more](../configuration/channel-surfaces.md#create-channel-surface) |
| **CJMRT-000069-400** | The HTML content is not valid: {errorMessage} | The HTML content is not valid. Check the HTML for unclosed tags, and use the content checks. [Learn more](../email/content-check.md) |
| **CJMTL-010019-422** | The template rendering size limit of {limit} bytes is exceeded. Please update and try again. | The rendered message is larger than the size limit shown in the message. Reduce the content, or the data inserted by the expressions. [Learn more](../start/guardrails.md#message-content-size) |

## URL parameter encryption keys {#encryption}

These errors occur when you create or use an encryption key to encrypt URL parameters.

See also [Encrypt URL parameters in tracking links](url-parameter-encryption.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-081601-400**, **CJMRT-081602-400** | The key must be 32 bytes (256 bits), but {actualBytes} bytes were provided. Update the key to the correct length and try again.<br/>The key is not base64-encoded. Encode the key in base64 format and try again. | The key must be 256 bits (32 bytes) long, and encoded in base64. Generate a key of the right length, encode it in base64, and enter it again. [Learn more](url-parameter-encryption.md#create-keys) |
| **CJMRT-081603-400** | The key name can only contain letters, numbers, and hyphens. Update the key name and try again. | The key name can contain only letters, numbers, and hyphens. Rename the key. [Learn more](url-parameter-encryption.md#create-keys) |
| **CJMRT-070011-422** | Encryption / Signing keys could not be resolved | The encryption or signing key cannot be found. Check that the key used by the encryption helper exists in the key registry of the sandbox. [Learn more](url-parameter-encryption.md#manage-keys) |

## Related topics {#related}

* [Add personalization](personalization-build-expressions.md)
* [Personalization syntax](personalization-syntax.md)
* [Helper functions](functions/helpers.md)
* [Encrypt URL parameters in tracking links](url-parameter-encryption.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/personalization/ai-augmented-personalization-errors.md}}
