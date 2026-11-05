---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to build rules for Orchestrated campaigns using the rule builder, by adding conditions from database attributes and expressions, combining them with logical operators, and checking and validating the results.

**Intents:**

* Add a custom condition to a query by selecting an attribute from the database and defining an operator and value.
* Start a query from a predefined filter instead of building a condition from scratch.
* Use the Distribution of values tool to review available attribute values before building a condition.
* Add attributes to a favorites menu for quicker access when building conditions.
* Build conditions on 1-1 linked tables by navigating to the linked table and selecting an attribute, or by selecting the table link directly.
* Build conditions on 1-N (collection) linked tables by selecting the collection itself to create an exists such as condition with sub-conditions, or by selecting an attribute from the collection and choosing the Default, Aggregate, or Advanced option.
* Combine conditions with AND, OR, or EXCEPT operators and group conditions using the canvas toolbar.
* Check the resulting data, view the SQL code, or calculate the number of targeted records before confirming the rule.

**Glossary:**

* **Rule builder**: the interface accessed from a Build audience activity used to create targeted queries for Orchestrated campaigns *(product-specific)*
* **Custom condition**: a filtering component that lets you filter a query by building a condition with attributes from the database and advanced expressions *(product-specific)*
* **Distribution of values**: a tool that shows how values are used within the database, including their counts and percentages, to help avoid issues such as inconsistent capitalization or spelling *(product-specific)*
* **1-1 link**: a table link with one-to-one cardinality, where an attribute from the linked table can be selected directly *(product-specific)*
* **1-N link (collection table)**: a table link with one-to-many cardinality, where conditions can target the collection itself or an attribute within it *(product-specific)*
* **Exists such as condition**: a condition created when selecting a collection itself (or, with the Default option, an attribute from the collection), which allows sub-conditions to be added *(product-specific)*
* **Default**: the recommended option for a collection attribute condition; it automatically creates an exists such as condition for the collection and produces the same result as selecting the collection directly *(product-specific)*
* **Aggregate**: an option that applies an aggregate function, such as Count, to the selected collection attribute *(product-specific)*
* **Advanced**: an option that uses a direct join to the collection element, evaluating the selected attribute directly, for a single condition on the collection element *(product-specific)*
* **AND (Intersection)**: an operator that combines results matching all the filtering components in the outbound transitions *(product-specific)*
* **OR (Union)**: an operator that includes results matching at least one of the filtering components in the outbound transitions *(product-specific)*
* **EXCEPT (Exclusion)**: an operator that excludes results matching all the filtering components in the outbound transition *(product-specific)*
* **Rule properties pane**: the pane used to check a built query, offering View results, Code view, Calculate, and Select or save filter operations *(product-specific)*

**Guardrails:**

* For attributes with a large number of values, the Distribution of values tool displays only the first twenty; a Partial load notification appears to indicate this limitation.
* Up to 20 attributes can be added to favorites.
* Each new condition added to a rule is automatically linked to the existing condition by an AND operator.
* Selecting a predefined filter from the Rule properties pane replaces the rule that has been built in the canvas with the selected filter.

**Terminology:**

* Canonical name: rule builder

**FAQ:**

* **Q: What is a custom condition?** — A filtering component that lets you filter a query by building your own condition with attributes from the database and advanced expressions.
* **Q: How many attributes can I add to favorites?** — Up to 20 attributes.
* **Q: What operator links a newly added condition to an existing one?** — An AND operator, by default.
* **Q: What is the difference between selecting a collection itself and selecting an attribute from the collection with the Default option?** — Both create an exists such as condition and produce the same result; the Default option is the recommended choice for most use cases.
* **Q: What does the Aggregate option do?** — It applies an aggregate function, such as Count, to the selected collection attribute.
* **Q: What happens if I select a predefined filter from the Rule properties pane?** — It replaces the rule built in the canvas with the selected filter.

**Related pages:**

* To start a query from a predefined filter, or to save a query as one: Work with predefined filters (orchestrated/predefined-filters.md)
* To manually define an expression using fields from the database and helper functions: Learn how to edit expressions (orchestrated/edit-expressions.md)

**Personas:**

* **marketer:** Can build rules for Orchestrated campaigns by adding conditions with database attributes, operators, and values in the rule builder. Can combine conditions using AND, OR, and EXCEPT operators, and check results before confirming. The page states that each new condition is automatically linked to the existing condition by an AND operator. Where: "Combine conditions using operators".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Access the rule builder from a Build audience activity.
* **Success check:** You can view the resulting data, view the SQL code, and calculate the number of records targeted by your rule.
* **Previous:** Starting a query from a predefined filter instead of building a condition from scratch: Work with predefined filters (orchestrated/predefined-filters.md)
* **Next:** Manually defining an expression using fields from the database and helper functions: Edit expressions (orchestrated/edit-expressions.md)

+++

<!-- ai-section-version: 1 | source-hash: 5aa5fd6c -->
