---
solution: Journey Optimizer
product: journey optimizer
title: Iterate over contextual data
description: Learn how to iterate over arrays from various context sources using Handlebars syntax
feature: Personalization
topic: Personalization
role: Developer
level: Intermediate
hide: yes
hidefromtoc: yes
keywords: expression, editor, handlebars, iteration, arrays, context, personalization
---
# Iterate over contextual data {#personalization-contexts}

Learn how to use Handlebars iteration syntax to display dynamic lists of data from various sources in your messages, including events, custom action responses, and other contextual data.

## Overview {#overview}

Journey Optimizer provides access to contextual data from multiple sources during [message personalization](personalize.md). You can iterate over arrays from these sources using Handlebars syntax in native channels ([email](../email/get-started-email-design.md), [push](../push/create-push.md), [SMS](../sms/create-sms.md)) to display dynamic content like product lists, recommendations, or other repeating elements.

**Available context sources:**

* **[Events](#event-data)**: Data from journey events (business events, unitary events)
* **[Custom action responses](#custom-action-responses)**: Data returned from external API calls via custom actions
* **[Dataset lookup](#dataset-lookup)**: Enriched data retrieved from Adobe Experience Platform datasets
* **[Technical properties](#technical-properties)**: Journey metadata such as journey ID and supplemental identifiers
* **[Journey context](#other-contexts)**: Other journey-related data accessible during execution

This guide shows you how to iterate over arrays from each of these sources in your messages, and how to work with arrays when configuring journey activities. Start with [Handlebars iteration syntax](#syntax) to understand message personalization basics, or jump to [Work with arrays in Journey expressions](#arrays-in-journeys) to learn how to pass array data to custom actions and dataset lookups.

## Handlebars iteration syntax {#syntax}

Handlebars provides the `{{#each}}` [helper](functions/helpers.md) to iterate over arrays. The basic syntax is:

```handlebars
{{#each arrayPath as |item|}}
  <!-- Access item properties here -->
  {{item.property}}
{{/each}}
```

**Key points:**

* Replace `arrayPath` with the path to your array data
* Replace `item` with any variable name you prefer (e.g., `product`, `response`, `element`)
* Access properties of each item using `{{item.propertyName}}`
* You can nest multiple `{{#each}}` blocks for multi-level arrays

## Iterate over event data {#event-data}

Event data is available when your journey is triggered by an [event](../event/about-events.md). This is useful for displaying data that was captured at the moment the journey started, such as cart contents, order items, or form submissions.

>[!TIP]
>
>You can combine event data with other sources. See [Combine multiple context sources](#combine-sources) for examples.

### Context path for events

```handlebars
context.journey.events.<event_ID>.<fieldPath>
```

* `<event_ID>`: The unique ID of your event as configured in the journey
* `<fieldPath>`: The path to the field or array within your event schema

### Example: Cart items from an event

If your [event schema](../event/experience-event-schema.md) includes a `productListItems` array (standard [XDM format](https://experienceleague.adobe.com/docs/experience-platform/xdm/data-types/product-list-item.html){target="_blank"}), you can display cart contents like this:

```handlebars
{{#each context.journey.events.event_ID.productListItems as |product|}}
  <div class="product">
    <h3>{{product.name}}</h3>
    <p>Quantity: {{product.quantity}}</p>
    <p>Price: ${{product.priceTotal}}</p>
  </div>
{{/each}}
```

### Example: Nested arrays in events

For nested structures, use nested `{{#each}}` blocks. Learn more about nesting in [Best practices](#best-practices).

```handlebars
{{#each context.journey.events.event_ID.categories as |category|}}
  <h2>{{category.name}}</h2>
  <ul>
    {{#each category.items as |item|}}
      <li>{{item.title}}</li>
    {{/each}}
  </ul>
{{/each}}
```

## Iterate over custom action responses {#custom-action-responses}

[Custom action](../action/about-custom-action-configuration.md) responses contain data returned from external API calls. This is useful for displaying real-time information from your systems, such as loyalty points, product recommendations, inventory status, or personalized offers.

>[!NOTE]
>
>Custom actions must be configured with a response payload to use this feature. Learn more in [this section](../action/action-response.md#config-response). You can also combine custom action responses with event data or dataset lookups - see [Combine multiple context sources](#combine-sources) for examples.

### Context path for custom actions

```handlebars
context.journey.actions.<actionName>.<fieldPath>
```

* `<actionName>`: The name of your [custom action](../action/about-custom-action-configuration.md) as configured in the journey
* `<fieldPath>`: The path to the field or array within the response payload

### Example: Product recommendations from an API

If your custom action returns product recommendations:

**API Response:**

```json
{
  "recommendations": [
    {
      "productId": "12345",
      "productName": "Summer Jacket",
      "price": 89.99,
      "imageUrl": "https://example.com/jacket.jpg"
    },
    {
      "productId": "67890",
      "productName": "Running Shoes",
      "price": 129.99,
      "imageUrl": "https://example.com/shoes.jpg"
    }
  ]
}
```

**Message personalization:**

```handlebars
<h2>Recommended for You</h2>
<div class="recommendations">
  {{#each context.journey.actions.GetRecommendations.recommendations as |item|}}
    <div class="product-card">
      <img src="{{item.imageUrl}}" alt="{{item.productName}}" />
      <h3>{{item.productName}}</h3>
      <p class="price">${{item.price}}</p>
    </div>
  {{/each}}
</div>
```

### Example: Nested arrays from custom actions

If your custom action returns nested arrays (e.g., categories with products). For more complex nesting patterns, see [Best practices](#best-practices).

**API Response:**

```json
{    
  "id": "84632848268632",    
  "responses": [
    { "productIDs": [1111, 2222, 3333] },
    { "productIDs": [4444, 5555, 6666] },
    { "productIDs": [7777, 8888, 9999] }
  ]
}
```

**Message personalization:**

```handlebars
<h2>Product Groups</h2>
{{#each context.journey.actions.GetProducts.responses as |response|}}
  <div class="product-group">
    <ul>
      {{#each response.productIDs as |productID|}}
        <li>Product ID: {{productID}}</li>
      {{/each}}
    </ul>
  </div>
{{/each}}
```

### Example: Loyalty tier benefits

Display dynamic benefits based on loyalty status:

**API Response:**

```json
{
  "loyaltyTier": "gold",
  "benefits": [
    { "name": "Free shipping", "icon": "truck" },
    { "name": "20% discount", "icon": "percent" },
    { "name": "Priority support", "icon": "headset" }
  ]
}
```

**Message personalization:**

```handlebars
<h2>Your {{context.journey.actions.GetLoyaltyInfo.loyaltyTier}} Member Benefits</h2>
<ul class="benefits">
  {{#each context.journey.actions.GetLoyaltyInfo.benefits as |benefit|}}
    <li>
      <span class="icon-{{benefit.icon}}"></span>
      {{benefit.name}}
    </li>
  {{/each}}
</ul>
```

## Iterate over dataset lookup results {#dataset-lookup}

The [Dataset Lookup activity](../building-journeys/dataset-lookup.md) allows you to retrieve data from [Adobe Experience Platform datasets](https://experienceleague.adobe.com/docs/experience-platform/catalog/datasets/overview.html){target="_blank"} during journey runtime. The enriched data is stored as an array and can be iterated over in your messages.

>[!AVAILABILITY]
>
>The Dataset Lookup activity is only available for a limited set of organizations. To gain access, contact your Adobe representative.

Learn more about configuring the Dataset Lookup activity in [this section](../building-journeys/dataset-lookup.md). Dataset lookup is particularly powerful when combined with event data - see [Example: Event data enriched with dataset lookup](#combine-sources) for a practical use case.

### Context path for dataset lookups

```handlebars
context.journey.datasetLookup.<activityID>.entities
```

* `<activityID>`: The unique ID of your Dataset Lookup activity
* `entities`: The array of enriched data retrieved from the dataset

### Example: Product details from a dataset

If you're using a Dataset Lookup activity to retrieve product information based on SKUs:

**Dataset Lookup Configuration:**

* Lookup Keys: `list(@event{purchase_event.products.sku})`
* Fields to Return: `["SKU", "category", "price", "name"]`

**Message personalization:**

```handlebars
<h2>Product Details</h2>
<table>
  <thead>
    <tr>
      <th>Product Name</th>
      <th>Category</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    {{#each context.journey.datasetLookup.3709000.entities as |product|}}
      <tr>
        <td>{{product.name}}</td>
        <td>{{product.category}}</td>
        <td>${{product.price}}</td>
      </tr>
    {{/each}}
  </tbody>
</table>
```

### Example: Filtered iteration with dataset data

Display only products from a specific category. Learn more about conditional filtering in [Best practices](#best-practices).

```handlebars
<h2>Household Products</h2>
{{#each context.journey.datasetLookup.3709000.entities as |product|}}
  {{#if product.category = "household"}}
    <div class="product">
      <h3>{{product.name}}</h3>
      <p>Price: ${{product.price}}</p>
    </div>
  {{/if}}
{{/each}}
```

### Example: Calculate totals from dataset lookup

```handlebars
{% let householdTotal = 0 %}
{{#each context.journey.datasetLookup.3709000.entities as |product|}}
  {%#if product.category = "household"%}
    {% let householdTotal = householdTotal + product.price %}
  {%/if%}
{{/each}}

<p>Your household products total: ${{householdTotal}}</p>
```

## Use journey technical properties {#technical-properties}

Journey technical properties provide access to metadata about the journey execution, such as the journey ID and supplemental identifiers. These can be useful when combined with iteration patterns, especially for filtering arrays based on specific journey instances.

### Available technical properties

```handlebars
context.journey.technicalProperties.journeyUID
context.journey.technicalProperties.supplementalId
```

### Example: Filter array items using supplemental identifier

When using supplemental identifiers in event-triggered journeys with arrays, you can filter to show only the relevant item for the current journey instance. Learn more about supplemental identifiers in [this guide](../building-journeys/supplemental-identifier.md).

**Scenario**: A journey is triggered with multiple bookings, but you want to display information only for the specific booking (identified by supplemental ID) that triggered this journey instance.

```handlebars
{{#each context.journey.events.event_ID.bookingList as |booking|}}
  {%#if booking.bookingInfo.bookingNum = context.journey.technicalProperties.supplementalId%}
    <div class="booking-details">
      <h3>Your Booking: {{booking.bookingInfo.bookingNum}}</h3>
      <p>Destination: {{booking.bookingInfo.bookingCountry}}</p>
      <p>Date: {{booking.bookingInfo.bookingDate}}</p>
    </div>
  {%/if%}
{{/each}}
```

### Example: Include journey ID for tracking

```handlebars
<footer>
  <p>Journey Reference: {{context.journey.technicalProperties.journeyUID}}</p>
</footer>
```

## Combine multiple context sources {#combine-sources}

You can combine data from different sources in the same message to create rich, personalized experiences. This section shows practical examples of using multiple context sources together.

**Context sources you can combine:**

* [Event data](#event-data) + [Custom action responses](#custom-action-responses)
* [Event data](#event-data) + [Dataset lookup](#dataset-lookup)
* [Multiple sources](#combine-sources) + [Technical properties](#technical-properties)

### Example: Cart items with real-time inventory

Combine event data (cart contents) with custom action data (inventory status):

```handlebars
<h2>Your Cart</h2>
{{#each context.journey.events.cartEvent.productListItems as |product|}}
  <div class="cart-item">
    <h3>{{product.name}}</h3>
    <p>Quantity: {{product.quantity}}</p>
    <p>Price: ${{product.priceTotal}}</p>
  </div>
{{/each}}

<h2>We Also Recommend</h2>
{{#each context.journey.actions.GetRecommendations.items as |recommendation|}}
  <div class="recommendation">
    <h4>{{recommendation.name}}</h4>
    <p>${{recommendation.price}}</p>
    {{#if recommendation.inStock}}
      <span class="badge">In Stock</span>
    {{else}}
      <span class="badge out-of-stock">Out of Stock</span>
    {{/if}}
  </div>
{{/each}}
```

### Example: Event data enriched with dataset lookup

Combine [event SKUs](#event-data) with detailed product information from a [dataset lookup](#dataset-lookup):

```handlebars
<h2>Your Order Details</h2>
{{#each context.journey.events.orderEvent.productListItems as |item|}}
  <div class="order-item">
    <p><strong>SKU:</strong> {{item.SKU}}</p>
    <p><strong>Quantity:</strong> {{item.quantity}}</p>
    
    <!-- Enrich with dataset lookup data -->
    {{#each context.journey.datasetLookup.1234567.entities as |enrichedProduct|}}
      {{#if enrichedProduct.SKU = item.SKU}}
        <p><strong>Product Name:</strong> {{enrichedProduct.name}}</p>
        <p><strong>Category:</strong> {{enrichedProduct.category}}</p>
        <img src="{{enrichedProduct.imageUrl}}" alt="{{enrichedProduct.name}}" />
      {{/if}}
    {{/each}}
  </div>
{{/each}}
```

### Example: Combine multiple sources with technical properties

```handlebars
<div class="personalized-content">
  <!-- Profile data -->
  <h1>Hello {{profile.person.name.firstName}},</h1>
  
  <!-- Event data iteration -->
  <h2>Your Recent Purchases</h2>
  {{#each context.journey.events.purchaseEvent.items as |purchase|}}
    <div class="purchase">
      <p>{{purchase.productName}} - ${{purchase.price}}</p>
    </div>
  {{/each}}
  
  <!-- Custom action response iteration -->
  <h2>Recommended for You</h2>
  {{#each context.journey.actions.GetPersonalizedRecs.recommendations as |rec|}}
    <div class="recommendation">
      <h3>{{rec.title}}</h3>
      <p>{{rec.description}}</p>
    </div>
  {{/each}}
  
  <!-- Technical properties -->
  <footer>
    <p class="fine-print">Journey ID: {{context.journey.technicalProperties.journeyUID}}</p>
  </footer>
</div>
```

## Other context types {#other-contexts}

While this guide focuses on iteration over arrays, other context types are available for personalization that typically don't require iteration. These are accessed directly rather than looped over:

* **[Profile attributes](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html){target="_blank"}** (`profile.*`): Individual profile fields from Adobe Experience Platform
* **[Audiences](../audience/about-audiences.md)** (`inAudience()`): Audience membership checks
* **[Offer decisions](../offers/get-started/starting-offer-decisioning.md)**: Decision management offers
* **[Target attributes](../orchestrated/activities/channels.md#add-personalization)** (Orchestrated campaigns only): Attributes calculated in the campaign canvas
* **Token** (`context.token`): Session or authentication tokens

For complete personalization syntax and examples using these sources, refer to:

* [Add personalization](personalization-build-expressions.md)
* [Personalization syntax](personalization-syntax.md)

## Work with arrays in Journey expressions {#arrays-in-journeys}

While the previous sections focus on iterating over arrays in message personalization using Handlebars, you also work with arrays when configuring journey activities. This section explains how to use array data from events in Journey expressions, particularly when passing data to custom actions or using arrays with dataset lookups.

>[!IMPORTANT]
>
>Journey expressions use a different syntax than Handlebars personalization. In journey configuration (such as custom action parameters or conditions), you use the [Journey expression editor](../building-journeys/expression/expressionadvanced.md) with functions like `first`, `all`, and `serializeList`. In message content, you use Handlebars syntax with `{{#each}}` loops.

### Pass array values to custom action parameters {#arrays-to-custom-actions}

When configuring [custom actions](../action/about-custom-action-configuration.md), you often need to extract values from event arrays and pass them as parameters. This section covers common patterns.

Learn more about passing collections in [Pass collections into custom action parameters](../building-journeys/collections.md#passing-collection).

#### Extract a single value from an array

**Use case**: Get a specific field from an event array to pass as a query parameter in a GET request.

**Example scenario**: Extract the first SKU with a price greater than 0 from a product list.

**Event schema example**:

```json
{
  "commerce": {
    "productListItems": [
      { "SKU": "SKU-1", "priceTotal": 10.0 },
      { "SKU": "SKU-2", "priceTotal": 0.0 },
      { "SKU": "SKU-3", "priceTotal": 20.0 }
    ]
  }
}
```

**Custom action configuration**:

1. In your custom action, configure a query parameter (e.g., `sku`) with type `string`
2. Mark it as `Variable` to allow dynamic values

**Journey expression in action parameter**:

```javascript
@event{YourEventName.commerce.productListItems.first(currentEventField.priceTotal > 0).SKU}
```

**Explanation**:

* `@event{YourEventName}`: References your journey event
* `.first(currentEventField.condition)`: Returns the first array item matching the condition
* `currentEventField`: Represents each item in the event array as you loop through it
* `.SKU`: Extracts the SKU field from the matched item
* Result: `"SKU-1"` (a string suitable for the action parameter)

Learn more about the `first` function in [Collection management functions](../building-journeys/expression/collection-management-functions.md).

#### Build a list of values from an array

**Use case**: Create a comma-separated list of IDs to pass as a query parameter (e.g., `/products?ids=sku1,sku2,sku3`).

**Custom action configuration**:

1. Configure a query parameter (e.g., `ids`) with type `string`
2. Mark it as `Variable`

**Journey expression**:

```javascript
serializeList(
  @event{YourEventName.commerce.productListItems.all(currentEventField.priceTotal > 0).SKU},
  ",",
  true
)
```

**Explanation**:

* `.all(currentEventField.condition)`: Returns all array items matching the condition (returns a list)
* `currentEventField`: Represents each item in the event array as you loop through it
* `.SKU`: Projects the list to only include SKU values
* `serializeList(list, delimiter, addQuotes)`: Joins the list into a string
  * `","`: Use comma as delimiter
  * `true`: Add quotes around each string element
* Result: `"SKU-1,SKU-3"` (suitable for a query parameter)

Learn more about:
* [`all` function](../building-journeys/expression/collection-management-functions.md)
* [`serializeList` function](../building-journeys/functions/list-functions.md#serializeList)

Collection handling for custom actions is covered in [Pass collections into custom action parameters](../building-journeys/collections.md#passing-collection).

#### Pass an array of objects to a custom action

**Use case**: Send a complete array of objects in a request body (for POST or GET with body).

**Request body example**:

```json
{
  "ctxt": {
    "products": [
      {
        "id": "productA",
        "name": "Product A",
        "price": 20.1,
        "color": "blue"
      }
    ]
  }
}
```

**Custom action configuration**:

1. In the request body, define `products` as type `listObject`
2. Mark it as `Variable`
3. Define the object fields: `id`, `name`, `price`, `color` (each becomes mappable)

**Journey canvas configuration**:

1. In Advanced mode, set the collection expression:

```javascript
@event{YourEventName.commerce.productListItems.all(currentEventField.priceTotal > 0)}
```

2. In the collection mapping UI:
   * Map `id` → `productListItems.SKU`
   * Map `name` → `productListItems.name`
   * Map `price` → `productListItems.priceTotal`
   * Map `color` → `productListItems.color`

Journey Optimizer constructs the array of objects matching your action payload structure.

>[!NOTE]
>
>When working with event arrays, use `currentEventField` to reference each item. For data source collections (Adobe Experience Platform), use `currentDataPackField`. For custom action response collections, use `currentActionField`.

Learn more in [Pass collections into custom action parameters](../building-journeys/collections.md#passing-collection).

### Use arrays with dataset lookups {#arrays-with-dataset-lookup}

When using the [Dataset Lookup activity](../building-journeys/dataset-lookup.md), you can pass an array of values as lookup keys to retrieve enriched data.

**Example**: Look up product details for all SKUs in an event array.

**Dataset Lookup configuration**:

In the lookup keys field, use `list()` to convert an array path to a list:

```javascript
list(@event{purchaseEvent.productListItems.SKU})
```

This creates a list of all SKU values to look up in the dataset. The results are available as an array at `context.journey.datasetLookup.<activityID>.entities` that you can iterate over in your message (see [Iterate over dataset lookup results](#dataset-lookup)).

### Limitations and patterns {#array-limitations}

Be aware of these limitations when working with arrays in journeys:

#### No dynamic looping over arrays in journey flow

Journeys cannot create dynamic loops where one action node is executed multiple times for each item in an array. This is intentional to prevent runaway performance issues.

**What you cannot do**:

* Execute a custom action once per array item dynamically
* Create multiple journey branches based on array length

**Recommended patterns instead**:

1. **Send all items at once**: Pass the entire array or a serialized list to a single custom action that processes all items. See [Build a list of values from an array](#arrays-to-custom-actions).

2. **Use external aggregation**: Have your external API accept multiple IDs and return combined results in a single call.

3. **Pre-compute in AEP**: Use [computed attributes](../audience/computed-attributes.md) to pre-calculate values from arrays at the profile level.

4. **Single value extraction**: If you only need one value, extract it using `first` or `head`. See [Extract a single value from an array](#arrays-to-custom-actions).

Learn more in [Guardrails and limitations](../start/guardrails.md).

#### Array size considerations

Large arrays can impact journey performance:

* **Event arrays**: Keep event payloads under 50KB total
* **Custom action responses**: Response payloads should be under 100KB
* **Dataset lookup results**: Limit the number of lookup keys and returned entities

### Complete example: Event array to custom action {#complete-example}

Here's a complete workflow showing how to use an event array with a custom action.

**Scenario**: When a user abandons their cart, send cart data to an external recommendation API to get personalized suggestions, then display them in an email.

**Step 1: Configure the custom action**

Create a custom action "GetCartRecommendations":

* **Method**: POST
* **URL**: `https://api.example.com/recommendations`
* **Request body**:

```json
{
  "cartItems": [
    {
      "sku": "string",
      "price": 0,
      "quantity": 0
    }
  ]
}
```

* Mark `cartItems` as type `listObject` and `Variable`
* Define fields: `sku` (string), `price` (number), `quantity` (integer)

Learn more in [Configure a custom action](../action/about-custom-action-configuration.md).

**Step 2: Configure response payload**

In the custom action, configure the response:

```json
{
  "recommendations": [
    {
      "productId": "string",
      "productName": "string",
      "price": 0,
      "imageUrl": "string"
    }
  ]
}
```

Learn more in [Use API call responses](../action/action-response.md).

**Step 3: Wire the action in the journey**

1. After your cart abandonment event, add the custom action
2. In Advanced mode for the `cartItems` collection:

```javascript
@event{cartAbandonment.commerce.productListItems.all(currentEventField.quantity > 0)}
```

3. Map the collection fields:
   * `sku` → `productListItems.SKU`
   * `price` → `productListItems.priceTotal`
   * `quantity` → `productListItems.quantity`

**Step 4: Use the response in your email**

In your email content, iterate over the recommendations:

```handlebars
<h2>We noticed you left these items in your cart</h2>
{{#each context.journey.events.cartAbandonment.productListItems as |item|}}
  <div class="cart-item">
    <p>{{item.name}} - Quantity: {{item.quantity}}</p>
  </div>
{{/each}}

<h2>You might also like</h2>
{{#each context.journey.actions.GetCartRecommendations.recommendations as |rec|}}
  <div class="recommendation">
    <img src="{{rec.imageUrl}}" alt="{{rec.productName}}" />
    <h3>{{rec.productName}}</h3>
    <p>${{rec.price}}</p>
  </div>
{{/each}}
```

**Step 5: Test your configuration**

Before running a live journey, test the custom action using the "Send test request" feature in the action configuration to verify the built request and values.

1. Use [journey test mode](../building-journeys/testing-the-journey.md)
2. Trigger with sample event data including a `productListItems` array
3. Verify the custom action receives the correct array structure
4. Check the [action test logs](../action/action-response.md#test-mode-logs)
5. Preview the email to confirm both arrays display correctly

Learn more in [Troubleshoot your custom actions](../action/troubleshoot-custom-action.md).

## Best practices {#best-practices}

Follow these best practices when iterating over contextual data to create maintainable, performant personalization.

### Use descriptive variable names

Choose variable names that clearly indicate what you're iterating over. This makes your code more readable and easier to maintain. Learn more about [personalization syntax](personalization-syntax.md):

```handlebars
<!-- Good -->
{{#each products as |product|}}
{{#each users as |user|}}
{{#each recommendations as |recommendation|}}

<!-- Less clear -->
{{#each items as |item|}}
{{#each array as |element|}}
```

### Handle empty arrays

Use the `{{else}}` clause to provide fallback content when an array is empty. Learn more about [helper functions](functions/helpers.md):

```handlebars
{{#each context.journey.actions.GetRecommendations.items as |item|}}
  <div>{{item.name}}</div>
{{else}}
  <p>No recommendations available at this time.</p>
{{/each}}
```

### Combine with conditional helpers

Use `{{#if}}` within loops for conditional content. Learn more about [conditional rules](create-conditions.md) and see examples in [Custom action responses](#custom-action-responses) and [Dataset lookup](#dataset-lookup) sections.

```handlebars
{{#each context.journey.actions.GetProducts.items as |product|}}
  <div class="product">
    <h3>{{product.name}}</h3>
    {{#if product.onSale}}
      <span class="badge">On Sale!</span>
    {{/if}}
    {{#if product.newArrival}}
      <span class="badge">New</span>
    {{/if}}
  </div>
{{/each}}
```

### Limit iteration for performance

For large arrays, consider limiting the number of iterations:

```handlebars
<!-- Display only first 5 items -->
{{#each context.journey.actions.GetProducts.items as |product|}}
  {{#if @index < 5}}
    <div>{{product.name}}</div>
  {{/if}}
{{/each}}
```

### Access array metadata

Handlebars provides special variables within loops that help with advanced iteration patterns:

* `@index`: Current iteration index (0-based)
* `@first`: True for the first iteration
* `@last`: True for the last iteration

```handlebars
{{#each products as |product|}}
  <div class="product {{#if @first}}featured{{/if}}">
    {{@index}}. {{product.name}}
  </div>
{{/each}}
```

>[!NOTE]
>
>These Handlebars variables (`@index`, `@first`, `@last`) are only available within `{{#each}}` loops in message personalization. For working with arrays in Journey expressions (such as getting the first item from an array before passing to a custom action), use array functions like [`head`](../personalization/functions/arrays-list.md#head), [`first`](../building-journeys/expression/collection-management-functions.md), or [`all`](../building-journeys/expression/collection-management-functions.md). See [Work with arrays in Journey expressions](#arrays-in-journeys) for more details.

## Troubleshooting {#troubleshooting}

Having issues with iteration? This section covers common problems and solutions.

### Array not displaying

**Issue**: Your array iteration isn't showing any content.

**Possible causes and solutions**:

1. **Incorrect path**: Verify the exact path to your array based on the context source:
   * For [events](#event-data): `context.journey.events.<event_ID>.<fieldPath>`
   * For [custom actions](#custom-action-responses): `context.journey.actions.<actionName>.<fieldPath>`
   * For [dataset lookups](#dataset-lookup): `context.journey.datasetLookup.<activityID>.entities`

2. **Array is empty**: Add an `{{else}}` clause to check if the array has no data. See [Best practices](#best-practices) for examples.

3. **Data not available yet**: Ensure the custom action, event, or dataset lookup activity has been executed before the message activity in your journey flow.

### Syntax errors

**Issue**: Expression validation fails or message doesn't render.

**Common mistakes**:

* Missing closing tags: Every `{{#each}}` must have a `{{/each}}`. Review [Handlebars iteration syntax](#syntax) for proper structure.
* Incorrect variable name: Ensure consistent use of variable name throughout the block. See [Best practices](#best-practices) for naming conventions.
* Incorrect path separators: Use dots (`.`) not slashes or other characters

### Testing your iterations

Use [journey test mode](../building-journeys/testing-the-journey.md) to verify your iterations. This is especially important when using [custom actions](#custom-action-responses) or [dataset lookups](#dataset-lookup):

1. Start your journey in [test mode](../building-journeys/testing-the-journey.md)
2. Trigger the event or custom action with sample data
3. Check the [message preview](../content-management/preview.md) to verify the iteration displays correctly
4. Review test mode logs for any errors (see [Custom action test mode logs](../action/action-response.md#test-mode-logs))

## Related topics {#related-topics}

**Personalization fundamentals:**

* [Get started with personalization](personalize.md)
* [Add personalization](personalization-build-expressions.md)
* [Personalization syntax](personalization-syntax.md)
* [Helper functions](functions/helpers.md)
* [Create conditional rules](create-conditions.md)

**Journey configuration:**

* [About events](../event/about-events.md)
* [Configure custom actions](../action/about-custom-action-configuration.md)
* [Pass collections into custom action parameters](../building-journeys/collections.md#passing-collection)
* [Use API call responses in custom actions](../action/action-response.md)
* [Troubleshoot your custom actions](../action/troubleshoot-custom-action.md)
* [Use Adobe Experience Platform data in journeys](../building-journeys/dataset-lookup.md)
* [Use supplemental identifiers in journeys](../building-journeys/supplemental-identifier.md)
* [Guardrails and limitations](../start/guardrails.md)
* [Test your journey](../building-journeys/testing-the-journey.md)

**Journey expression functions:**

* [Advanced expression editor](../building-journeys/expression/expressionadvanced.md)
* [Collection management functions](../building-journeys/expression/collection-management-functions.md) (first, all, last)
* [List functions](../building-journeys/functions/list-functions.md) (serializeList, filter, sort)
* [Array functions](../personalization/functions/arrays-list.md) (head, tail)

**Personalization use cases:**

* [Cart abandonment email](personalization-use-case-helper-functions.md)
* [Order status notification](personalization-use-case.md)

**Message design:**

* [Get started with email design](../email/get-started-email-design.md)
* [Create push notifications](../push/create-push.md)
* [Create SMS messages](../sms/create-sms.md)
* [Preview and test your content](../content-management/preview-test.md)

