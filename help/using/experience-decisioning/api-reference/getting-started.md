---
title: Get started with Decisioning APIs
description: Learn how to start using the Decisioning APIs to programmatically manage decision items and deliver personalized offers.
feature: API, Decisioning
topic: Integrations
role: Developer
level: Experienced
exl-id: 7a4b5d4e-9c1d-4f3a-b8e9-1d5f6e7a8c3a
version: Journey Orchestration
---
# Decisioning API developer guide {#decisioning-api-developer-guide}

Decisioning APIs allow you to programmatically create and manage the components used to deliver personalized offers to your customers. These RESTful APIs provide full CRUD (Create, Read, Update, Delete) operations for decision items, selection strategies, eligibility rules, and other decisioning components.

## Authentication {#authentication}

Before using Decisioning APIs, you must set up authentication to access the API endpoints. You can refer to the [Journey Optimizer authentication guide](https://developer.adobe.com/journey-optimizer-apis/references/authentication/){target="_blank"} for step-by-step instructions.

## Available API operations {#available-operations}

The Decisioning APIs provide comprehensive management capabilities for decisioning components. The following categories of operations are available:

* **Decision items** - Create, read, update, delete, and list decision items that represent the offers or content you want to deliver to customers.

    ➡️ [Learn how to manage decision items](decisions-items/create.md)

* **Item collections** - Organize decision items into collections for easier management and targeting using eligibility rules.

    ➡️ [Learn how to manage item collections](items-collections/create.md)

* **Selection strategies** - Define how decision items are selected and ranked when multiple items qualify for delivery.

    ➡️ [Learn how to manage selection strategies](selection-strategies/create.md)

* **Eligibility rules** - Set conditions that determine which profiles are eligible to receive specific decision items.

    ➡️ [Learn how to manage eligibility rules](eligibility-rules/create.md)

* **Ranking formulas** - Create custom ranking logic to determine the order in which decision items are presented.

    ➡️ [Learn how to manage ranking formulas](ranking-formulas/create.md)

* **Placements** - Define the locations or contexts where decision items can be displayed in your experiences.

    ➡️ [Learn how to manage placements](exd-placements/create.md)

## Next steps {#next-steps}

Now that you understand the basics of the Decisioning APIs, you can proceed to the specific operations:

* [Create decision items](decisions-items/create.md)
* [List decision items](decisions-items/decision-items-list.md)
* [Create selection strategies](selection-strategies/create.md)
* [Create eligibility rules](eligibility-rules/create.md)

For more information about using decisioning in your campaigns and journeys, refer to the [Decisioning documentation](../gs-experience-decisioning.md).
