---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents all string functions available in AJO journey expressions, covering text search, comparison, transformation, extraction, validation, replacement, splitting, and unique identifier generation.

**Intents:**
* Concatenate two or more strings using `concat`
* Search for a substring within a string (case-sensitive or case-insensitive) using `contain` or `containIgnoreCase`
* Compare two strings while ignoring case using `equalIgnoreCase` or `notEqualIgnoreCase`
* Check whether a string starts or ends with a specific prefix or suffix using `startWith`, `endWith`, and their case-insensitive variants
* Extract a substring by index positions using `substr`
* Replace the first or all occurrences of a pattern in a string using `replace` or `replaceAll`
* Split a string into a list of tokens by a separator using `split`
* Generate a random UUID for unique identifier needs using `uuid`
* Check if a string is empty or non-empty using `isEmpty` or `isNotEmpty`

**Glossary:**
* **RegExp**: A regular expression pattern used as the target parameter in `replace`, `replaceAll`, and `matchRegExp` — special characters must be escaped with `\\`
* **UUID**: Universal Unique IDentifier — a randomly generated string identifier returned by `uuid()`
* **substr**: Extracts a portion of a string by specifying a start index and optional end index (zero-based)

**Guardrails:**
* The `target` parameter in `replace` and `replaceAll` is treated as a RegExp; special characters (e.g., `|`, `.`) must be escaped with `\\`
* `replace` replaces only the first matching occurrence; use `replaceAll` to replace every occurrence
* `isEmpty` returns false for null values (not true); null is not considered an empty string
* `indexOf` and `lastIndexOf` return -1 when no match is found
* String index positions are zero-based (the first character is at position 0)

**Terminology:**
* Canonical name: String functions — Acronym: none — variants: text functions, string manipulation functions
* Synonyms: "contain" = "substring check"; "split" = "tokenize string"; "trim" = "strip whitespace"
* Do not confuse: "replace" (first occurrence only) ≠ "replaceAll" (all occurrences)
* Do not confuse: "indexOf" (first occurrence position) ≠ "lastIndexOf" (last occurrence position)
* Do not confuse: "isEmpty" (true only for zero-length string) ≠ null check (isEmpty returns false for null)
* Do not confuse: "equalIgnoreCase" (returns true when equal ignoring case) ≠ "notEqualIgnoreCase" (returns true when different ignoring case)

**FAQ:**
* **Q: How do I check if a string contains a substring regardless of case?** — Use `containIgnoreCase("myString", "searchTerm")`, which returns true if the search term is found in any case.
* **Q: What is the difference between `replace` and `replaceAll`?** — `replace` substitutes only the first matching occurrence; `replaceAll` substitutes every occurrence in the string.
* **Q: Why do I need to escape the `|` character in `replace`?** — The target parameter is treated as a regular expression; `|` is a special RegExp character and must be escaped as `\\|` to be treated as a literal pipe.
* **Q: Does `isEmpty` return true for null?** — No, `isEmpty` returns false for null; it only returns true for a zero-length string `""`.
* **Q: How do I extract the major version number from a version string like "20.45.2.3434"?** — Use `getListItem(split(@event{event.appVersion}, "\\."), 0)` to split by dot and retrieve the first element.
* **Q: How do I generate a unique identifier in a journey expression?** — Use `uuid()`, which returns a randomly generated UUID string with no parameters required.

+++
