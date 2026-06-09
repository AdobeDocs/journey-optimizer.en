---
title: Get started with Decisioning APIs
description: Learn how to start using the Decisioning APIs to programmatically manage decision items and deliver personalized offers.
feature: API, Decisioning
topic: Integrations
role: Developer
level: Experienced
exl-id: 78ed06a3-7787-4aab-8373-df7eb40c1727
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/01NgEXGvNxeb1MNkjeB55VNFZFuSiTfQMKeNahfuHWE
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
---
# Decisioning API developer guide {#decisioning-api-developer-guide}

Decisioning APIs allow you to programmatically create and manage the components used to deliver personalized offers to your customers. These RESTful APIs provide full CRUD (Create, Read, Update, Delete) operations for decision items, selection strategies, eligibility rules, and other decisioning components.

## Authentication {#authentication}

Before using Decisioning APIs, you must set up authentication to access the API endpoints. You can refer to the [Journey Optimizer authentication guide](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"} for step-by-step instructions.

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

>[!NOTE]
>
>If you need to migrate existing Decision management objects to Decisioning, use the dedicated [Decisioning Migration API](../decisioning-migration-api.md). This specialized API provides automated dependency resolution and rollback capabilities specifically designed for decisioning entity migration across sandboxes.
