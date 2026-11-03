---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents all list functions available in AJO journey expressions, covering how to filter, sort, deduplicate, check membership, limit, serialize, merge, subtract, and find intersections of lists and arrays.

**Intents:**
* Remove duplicate values from a list using `distinct` (ignoring nulls) or `distinctWithNull` (preserving nulls)
* Filter a listObject to return only objects matching specific key values using `filter`
* Retrieve an element at a specific index from a list using `getListItem`
* Check whether a value exists in a list using `in`
* Find common elements between two lists using `intersect`
* Combine two lists, with or without deduplication, using `mergeLists`
* Subtract one list from another (set difference) using `differenceLists`
* Return the first or last N elements of a list using `limit`
* Count the total number of elements in a list using `listSize`
* Convert a list to a delimited string using `serializeList`
* Sort a list in ascending or descending order using `sort`

**Glossary:**
* **listObject**: A list of complex objects that must be a field reference; cannot contain null objects *(product-specific)*
* **keyAttributeName**: An optional string parameter used with `distinct`, `filter`, and `sort` to identify which object attribute to use for deduplication, filtering, or sorting *(product-specific)*
* **intersect**: A set operation returning only the elements present in both input lists
* **mergeLists**: A set operation returning the union (deduplicated) or concatenation (with duplicates) of two lists, depending on the `deduplicate` parameter *(product-specific)*
* **differenceLists**: A set operation returning the items of the first list that are not present in the second list *(product-specific)*

**Guardrails:**
* `distinctWithNull` does not support the `<listObject>` parameter type
* `filter` requires the listObject parameter to be a field reference, not an inline literal
* `listSize` on a listObject requires the list to be a field reference; a listObject cannot contain null objects
* `serializeList` does not support the `listObject` type
* `mergeLists` and `differenceLists` only support scalar list types (string, integer, decimal, boolean, dateTime, dateTimeOnly, dateOnly, duration); `listObject` is not supported
* `mergeLists`'s `deduplicate` parameter must be a literal `true`/`false`, not a dynamic boolean expression
* `differenceLists` always deduplicates its result; there is no option to keep duplicates

**Terminology:**
* Canonical name: List functions — Acronym: none — variants: collection functions, array functions
* Synonyms: "listSize" = "count list elements"; "serializeList" = "join list to string"
* Do not confuse: "distinct" (ignores nulls) ≠ "distinctWithNull" (preserves null as a distinct value)
* Do not confuse: "limit" with third parameter `true` (returns first N items) ≠ "limit" with `false` (returns last N items)
* Do not confuse: "intersect" (common elements between two lists) ≠ "filter" (elements matching specific key values)
* Do not confuse: "mergeLists" (combines two lists, union or concatenation) ≠ "differenceLists" (subtracts one list from another) ≠ "intersect" (common elements only)

**FAQ:**
* **Q: How do I get the first 3 items of a list?** — Use `limit(myList, 3)` or `limit(myList, 3, true)`; the default is to return the first items.
* **Q: How do I get the last 3 items of a list?** — Use `limit(myList, 3, false)`.
* **Q: What is the difference between `distinct` and `distinctWithNull`?** — `distinct` ignores null values and excludes them from the result; `distinctWithNull` treats null as a distinct value and includes one null entry if any nulls are present.
* **Q: Can I filter a list of strings with `filter`?** — No, `filter` only works on `listObject`; for scalar lists use `in` or `distinct` for deduplication.
* **Q: How do I check if a value is in a list?** — Use `in(value, myList)`, which returns true if the value is found in the list.
* **Q: Can I sort a listObject by a specific attribute?** — Yes, use `sort(@event{...}, "attributeName", true)` where the second parameter is the attribute name and the third is the sort direction (true = ascending).
* **Q: How do I combine two lists and remove duplicates?** — Use `mergeLists(list1, list2, true)`.
* **Q: How do I combine two lists but keep duplicate values?** — Use `mergeLists(list1, list2, false)`.
* **Q: How do I find the items in one list that are not in another?** — Use `differenceLists(list1, list2)`, which returns the items of `list1` not present in `list2`.
* **Q: What is the difference between `intersect` and `differenceLists`?** — `intersect` returns items common to both lists; `differenceLists` returns items in the first list that are absent from the second list.

+++
