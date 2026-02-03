---
solution: Journey Optimizer
product: journey optimizer
title: Create loyalty challenges
description: Learn how to create and configure loyalty challenges in Adobe Journey Optimizer.
feature: Journeys
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Private beta" type="Informative"
---

# Create challenges {#create-challenges}

>[!CONTEXTUALHELP]
>id="ajo_loyalty_create_challenge"
>title="Create a loyalty challenge"
>abstract="Create a loyalty challenge to define the engagement offer, configure content cards for delivery, add tasks, set up rewards, and optionally configure messaging across channels."

Create a loyalty challenge to define the engagement offer, configure content cards, add tasks, set up rewards, and configure messaging across channels.

>[!BEGINSHADEBOX]

**Loyalty Challenges documentation:**

* [Get started with Loyalty Challenges](gs-loyalty-challenges.md) - Quick overview and next steps
* [Understand Loyalty Challenges](get-started.md) - Features, workflow, prerequisites
* **Create challenges** ◀︎ **You are here** - Build and configure challenges
* [Manage challenges](manage-challenges.md) - Edit, monitor, optimize

>[!ENDSHADEBOX]

## Before you start {#before-you-start}

Before creating a challenge, ensure you have:

* Configured and validated data ingestion through source connectors
* Created any required audiences in Experience Platform
* Prepared content assets (images, text, etc.) for your challenge
* Defined the tasks and rewards you want to offer

## Create a challenge {#create-a-challenge}

For detailed steps on creating challenges including:
* Challenge properties configuration
* Challenge types (Standard, Streak, Sequential)
* Audience selection
* Date configuration

## Add tasks {#add-tasks}

Tasks define the specific actions or milestones that customers must complete to earn rewards in a loyalty challenge. You can configure task types, quantities, product requirements, and reward values to create engaging and personalized loyalty experiences.

### Task overview {#task-overview}

Each task represents a measurable action that contributes toward challenge completion. Depending on your challenge type (Standard, Streak, or Sequential), customers complete tasks differently:

* **Standard challenges**: Customers complete any specified number of tasks in any order
* **Streak challenges**: Customers complete the same task multiple times consecutively
* **Sequential challenges**: Customers complete tasks in a defined order

### Add a task {#add-task}

To add a task to your challenge:

1. Open your challenge or create a new one.

2. Navigate to the **[!UICONTROL Tasks]** section.

3. Select **[!UICONTROL Add task]** or **[!UICONTROL Create new task]**.

4. In the task creation screen, configure the following properties.

### Task properties {#task-properties}

#### Basic task information {#basic-info}

**[!UICONTROL Task name]**: Enter a descriptive name for the task. This name is visible to you and your team but may not be shown to customers depending on your content card design.

**[!UICONTROL Task description]**: (Optional) Add details about the task purpose or requirements.

**[!UICONTROL Task type]**: Select the type of action customers must perform. Available task types include:

* **[!UICONTROL Purchase]**: Customer makes a purchase transaction
* **[!UICONTROL Spend amount]**: Customer spends a specified monetary amount
* **[!UICONTROL Visit]**: Customer visits a physical location or digital property
* **[!UICONTROL Engagement]**: Customer engages with content, such as viewing a video or reading an article
* **[!UICONTROL Custom event]**: Customer triggers a custom event tracked through your data ingestion

#### Quantity requirements {#quantity-requirements}

**[!UICONTROL Required quantity]**: Specify how many times the customer must perform the task to complete it.

For example:

* For a Purchase task: "Buy 2 items" (quantity = 2)
* For a Spend amount task: "Spend $50" (quantity = 50)
* For a Visit task: "Visit 5 times" (quantity = 5)

**[!UICONTROL Tracking period]**: (Optional) Define the time window for completing this task:

* Per challenge duration (default)
* Per day
* Per week
* Per month
* Custom date range

### Product and SKU filtering {#product-filtering}

For Purchase and Spend amount tasks, you can specify which products qualify toward task completion.

#### Product inclusions {#product-inclusions}

Define which products or categories count toward the task:

1. Select **[!UICONTROL Add product criteria]**.

2. Choose how to define qualifying products:
   * **[!UICONTROL By SKU]**: Enter specific product SKU codes
   * **[!UICONTROL By category]**: Select product categories from your catalog
   * **[!UICONTROL By attribute]**: Filter by product attributes such as brand, size, color, or custom attributes

3. Enter or select the product identifiers:

   **Example - By SKU**:

   ```text
   SKU001, SKU002, SKU003
   ```

   **Example - By category**:

   * Beverages > Coffee
   * Bakery > Pastries

   **Example - By attribute**:

   * Brand = "Premium Brand"
   * Category = "Seasonal Items"
   * Price > $20

4. Select **[!UICONTROL Add]** to save the product criteria.

#### Product exclusions {#product-exclusions}

Optionally, exclude specific products from counting toward the task:

1. Select **[!UICONTROL Add exclusions]**.

2. Use the same filtering methods as product inclusions to specify which products should be excluded.

3. Common exclusion scenarios:

   * Sale or clearance items
   * Gift cards
   * Promotional or free items
   * Specific brands or categories

>[!NOTE]
>
>**Inclusion and exclusion logic**: When both inclusions and exclusions are defined:
>
>* Products must match inclusion criteria
>* Products matching exclusion criteria are removed, even if they match inclusions
>* If no inclusions are defined, all products qualify except those explicitly excluded

#### Examples of product filtering {#product-filtering-examples}

##### Example 1: Coffee challenge {#example-1}

* Task type: Purchase
* Required quantity: 3
* Inclusions: Category = "Beverages > Coffee"
* Result: Customer must purchase 3 coffee beverages

##### Example 2: Premium spending {#example-2}

* Task type: Spend amount
* Required quantity: $100
* Inclusions: Brand = "Premium Brand"
* Exclusions: Category = "Clearance"
* Result: Customer must spend $100 on Premium Brand items, excluding clearance items

##### Example 3: Specific product purchase {#example-3}

* Task type: Purchase
* Required quantity: 1
* Inclusions: SKU = "NEWPRODUCT2024"
* Result: Customer must purchase the specific product with SKU "NEWPRODUCT2024"

### Configure rewards {#configure-rewards}

Define what customers earn for completing tasks. Rewards can be granted at the task level or at the challenge level after all tasks are complete.

#### Reward timing {#reward-timing}

Choose when customers receive rewards:

**[!UICONTROL After task completion]**: Customers receive a reward immediately after completing this specific task (also called "progressive rewards" or "milestone rewards").

**[!UICONTROL After challenge completion]**: Customers receive a reward only after completing all required tasks in the challenge (also called "final rewards" or "grand prizes").

>[!TIP]
>
>You can combine both reward types in a single challenge to maintain engagement throughout the customer journey. For example:
>
>* Give 10 points after each task completion (progressive rewards)
>* Give an additional 100 points after completing the entire challenge (final reward)

#### Reward types and values {#reward-types}

**[!UICONTROL Points]**: Award loyalty points to the customer's account.

* Enter the number of points (e.g., 100)
* Points are communicated to your external loyalty management system via API

**[!UICONTROL Discount]**: Provide a discount code or value.

* Enter discount type (percentage or fixed amount)
* Enter discount value
* Optionally specify discount code or let the system generate one

**[!UICONTROL Free item]**: Grant a free product or service.

* Specify the item SKU or description
* Indicate how the free item should be claimed

**[!UICONTROL Custom reward]**: Define a custom reward type.

* Enter reward description
* Provide any relevant codes or identifiers
* Configure how the reward is delivered or claimed

## Configure content cards {#configure-content-cards}

For detailed steps on configuring content cards including:
* Content card setup
* Design and personalization
* Preview and testing

## Configure messaging {#configure-messaging}

For detailed steps on configuring multi-channel messaging including:
* Message channels (in-app, email, push)
* Message stages (launch, in-progress, complete)
* Message timing and triggers

## Review and publish {#review-and-publish}

Before publishing your challenge:

1. **Review all components**: Challenge properties, tasks, rewards, content, messaging
2. **Test the experience**: Use test profiles to validate content and task triggers
3. **Publish**: Make the challenge active for your target audience

The auto-generated journey activates on your specified start date.

## Next steps {#next-steps}

* [Manage challenges](manage-challenges.md) - Learn how to edit, monitor, and optimize challenges
* [Understand Loyalty Challenges](get-started.md) - Review features and capabilities
