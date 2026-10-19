---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** The page gives the cause and the fix for the personalization errors that [!DNL Adobe Journey Optimizer] returns when you validate or publish content with personalization expressions, or when you create an encryption key, grouped into four families: variables and paths, helpers, syntax and content validation, and URL parameter encryption keys.

**Intents:**

* Identify an error from its code: the prefix (**CJMTL** or **CJMRT**), the error number, and the HTTP status.
* Find why a field, a variable, a path, or a namespace in an expression is reported as not found, or as having the wrong type.
* Fix an error on a helper that is not valid or that is called without enough parameters.
* Fix a syntax error, a malformed field of a message variant, or an HTML content error found when you validate or publish content.
* Fix an error returned when you create or use an encryption key to encrypt URL parameters.

**Glossary:**

* **CJMTL** *(product-specific)*: error code prefix for template rendering errors.
* **CJMRT** *(product-specific)*: error code prefix for runtime errors.
* **Error code**: a prefix, followed by an error number and an HTTP status, for example **CJMTL-010001-422**.
* **Helper**: named in an expression and called with parameters. The Let helper is used to define a variable.
* **Namespace**: the page lists profile, audience, offers, and the contextual attributes as the available namespaces.

**Guardrails:**

* An encryption key for URL parameters must be 256 bits (32 bytes) long and encoded in base64.
* The name of an encryption key can contain only letters, numbers, and hyphens.
* The name of a variable defined with the Let helper must start with a letter and can contain only alphanumeric characters (letters and numbers).
* Template rendering has a size limit: when the rendered message is larger than the limit, error **CJMTL-010019-422** is returned, and the message shows the limit in bytes.

**Terminology:**

* **Canonical name:** Personalization errors
* **Do not confuse:** **CJMTL** (template rendering) ≠ **CJMRT** (runtime). The same kind of problem can return a code with either prefix, for example a variable that is not found returns **CJMTL-010001-422** or **CJMRT-010001-422**.

**FAQ:**

* **Q: What do the prefixes CJMTL and CJMRT mean?** — **CJMTL** is for template rendering and **CJMRT** is for runtime. The prefix is followed by an error number and an HTTP status.
* **Q: Why do I get "Path {variable} not found" or "{variable} not found"?** — For CJMTL-010001-422 ("{variable} not found") and CJMRT-010001-422 ("Path {variable} not found"), the variable or path named in the message does not exist in the schema or in the context of the message. Check its name and path in the personalization editor, and use a field of the schema. CJMRT-070003-422 (variable not found in the execution context) and CJMRT-070008-422 (path not supported) have their own causes, listed under Troubleshooting.
* **Q: Why do I get a type mismatch?** — For CJMTL-010002-422 and CJMRT-010002-422, the variable has a different type than the one the expression expects, for example a string used in a loop that needs an array. Use a variable of the expected type. For CJMRT-070007-422, use a variable of the type shown in the message. For CJMRT-070002-422, the expression expects an array, for example in a loop: use an array variable.
* **Q: Why is the name of my Let variable rejected (CJMTL-010013-422, CJMTL-010014-422)?** — The name is not valid. Start the name with a letter and use only letters and numbers.
* **Q: What do I do when I get "Syntax errors found" or "Invalid syntax"?** — For CJMTL-010004-422, CJMTL-010011-422, and CJMRT-010004-422 (handlebars syntax), the expression has a syntax error described in the message: check the brackets, the quotes, and the helper syntax at that place. For CJMTL-010015-422, the assignment expression named in the message is not valid: check the syntax of the assignment, including the brackets and the quotes. For CJMRT-071011-400 ("Syntax errors found"), the message does not say where the syntax errors are: use the **[!UICONTROL Validate]** button of the personalization editor to find them, then check the brackets, the quotes, and the helper syntax. The **[!UICONTROL Validate]** button also helps for the other syntax errors.
* **Q: Why is my encryption key refused?** — The key must be 256 bits (32 bytes) long and encoded in base64 (**CJMRT-081601-400**, **CJMRT-081602-400**), and the key name can contain only letters, numbers, and hyphens (**CJMRT-081603-400**).
* **Q: What does "Encryption / Signing keys could not be resolved" mean (CJMRT-070011-422)?** — The encryption or signing key cannot be found. Check that the key used by the encryption helper exists in the key registry of the sandbox.

**Troubleshooting:**

* **Variables and paths**: an expression refers to a field, a variable, or a namespace that cannot be resolved, or has the wrong type.
    * "{variable} not found" (**CJMTL-010001-422**) and "Path {variable} not found" (**CJMRT-010001-422**): the variable or path does not exist in the schema or in the context of the message. Check it in the personalization editor, and use a field of the schema.
    * "Variable {variable} not found in the execution context." (**CJMRT-070003-422**): the variable is not available in the execution context of the message. Check its name in the personalization editor, and use a field of the schema.
    * "Path {path} is not supported" (**CJMRT-070008-422**): the path is not supported. Check the path in the personalization editor, and use a field of the schema.
    * "Namespace not found for {path}" (**CJMTL-010008-422**): the namespace is not available. Use one of the available namespaces: profile, audience, offers, or the contextual attributes.
    * Type mismatch (**CJMTL-010002-422**, **CJMRT-010002-422**, **CJMRT-070007-422**): the variable has a different type than the one the expression expects. Use a variable of the expected type (for **CJMRT-070007-422**, the type shown in the message).
    * "Variable {variable} is expected to be an array." (**CJMRT-070002-422**): the expression expects an array, for example in a loop, but the variable has another type. Use an array variable.
    * Invalid variable name (**CJMTL-010013-422**, **CJMTL-010014-422**): see the guardrail on Let variable names.
    * "{start} is out of bounds. Variable {variable} size is {length}" (**CJMRT-070001-422**): the start position is outside the size of the variable. Use a value smaller than the size shown in the message.
    * "The expression should be a String value. Found : {expression}" (**CJMRT-070005-422**): the expression must be a string value. Enter a string, or convert the value to a string.
* **Helpers**: a helper is not known or is called with missing parameters.
    * "Invalid helper {command}" (**CJMTL-010012-422**): the helper is not valid. Check its name in the list of helpers.
    * "Input parameters not defined for helper {helper}" (**CJMTL-010003-422**) and "Params not defined for helper: {helper}" (**CJMRT-010003-422**): the helper is called without its parameters. Add the parameters of the helper.
    * "Insufficient parameters for helper {helper}. Undefined {param}" (**CJMTL-010009-422**): the helper has too few parameters. Add the undefined parameter named in the message.
    * "Insufficient arguments for {helperName}. Missing argument {missingArgument}" (**CJMRT-070004-422**): the helper has too few arguments. Add the missing argument named in the message.
* **Syntax and content validation**: errors when you validate or publish content that has an expression with a syntax error.
    * Syntax error (**CJMTL-010004-422**, **CJMTL-010011-422**, **CJMTL-010015-422**, **CJMRT-010004-422**, **CJMRT-071011-400**): see the FAQ for the fix of each code.
    * "The field {fieldName} of {channel} variant is malformed" (**CJMRT-130001-400**): a field of the message variant is malformed. Open the field named in the message and fix its expression.
    * "The {variable} variable of the field {fieldName} of {channel} variant is malformed: Position: {position}" (**CJMRT-130004-400**): a variable of a field of the message variant is malformed. Open the field named in the message and fix the variable at the position shown.
    * "No segment definition found for {segmentId}" (**CJMRT-071012-404**): the audience (segment definition) used in the expression cannot be found. Select an audience that exists in the sandbox.
    * "Profile schema does not contain the required field: {fieldName} for channel: {channel}" (**CJMRT-130003-422**): the profile schema does not contain the field that the channel configuration needs. Add the field to the schema, or select another field in the channel configuration.
    * "The HTML content is not valid: {errorMessage}" (**CJMRT-000069-400**): check the HTML for unclosed tags, and use the content checks.
    * "The template rendering size limit of {limit} bytes is exceeded. Please update and try again." (**CJMTL-010019-422**): the rendered message is larger than the size limit shown in the message. Reduce the content, or the data inserted by the expressions.
* **URL parameter encryption keys**: errors when you create or use an encryption key to encrypt URL parameters (**CJMRT-081601-400**, **CJMRT-081602-400**, **CJMRT-081603-400**, **CJMRT-070011-422**): see the guardrails and the FAQ.

**Related pages:**

* Validation mechanisms for expressions: Validation mechanisms (personalization/personalization-build-expressions.md)
* Available namespaces: Available namespaces (personalization/personalization-syntax.md)
* Helper functions: Helper functions (personalization/functions/helpers.md)
* Creating and managing encryption keys: Encrypt URL parameters in tracking links (personalization/url-parameter-encryption.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 1 | source-hash: 9e52691f -->
