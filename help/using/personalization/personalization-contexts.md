---
solution: Journey Optimizer
product: journey optimizer
title: Iterate over contextual data with Handlebars
description: Learn how to iterate over arrays from various context sources using Handlebars syntax
feature: Personalization
topic: Personalization
role: Developer
level: Intermediate
keywords: expression, editor, handlebars, iteration, arrays, context, personalization
exl-id: TBD
---
# Iterate over contextual data with Handlebars {#personalization-contexts}

Learn how to use Handlebars iteration syntax to display dynamic lists of data from various sources in your messages, including events, custom action responses, and other contextual data.

## Overview {#overview}

Journey Optimizer provides access to contextual data from multiple sources during message personalization. You can iterate over arrays from these sources using Handlebars syntax in native channels (email, push, SMS) to display dynamic content like product lists, recommendations, or other repeating elements.

**Available context sources:**

* **Events**: Data from journey events (business events, unitary events)
* **Custom action responses**: Data returned from external API calls via custom actions
* **Journey context**: Other journey-related data accessible during execution

This guide shows you how to iterate over arrays from each of these sources.

## Handlebars iteration syntax {#syntax}

Handlebars provides the `{{#each}}` helper to iterate over arrays. The basic syntax is:

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

Event data is available when your journey is triggered by an event. This is useful for displaying data that was captured at the moment the journey started, such as cart contents, order items, or form submissions.

### Context path for events

```handlebars
context.journey.events.<event_ID>.<fieldPath>
```

* `<event_ID>`: The unique ID of your event as configured in the journey
* `<fieldPath>`: The path to the field or array within your event schema

### Example: Cart items from an event

If your event schema includes a `productListItems` array (standard XDM format), you can display cart contents like this:

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

For nested structures, use nested `{{#each}}` blocks:

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

Custom action responses contain data returned from external API calls. This is useful for displaying real-time information from your systems, such as loyalty points, product recommendations, inventory status, or personalized offers.

>[!NOTE]
>
>Custom actions must be configured with a response payload to use this feature. Learn more in [this section](../action/action-response.md#config-response).

### Context path for custom actions

```handlebars
context.journey.actions.<actionName>.<fieldPath>
```

* `<actionName>`: The name of your custom action as configured in the journey
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

If your custom action returns nested arrays (e.g., categories with products):

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

## Combine multiple context sources {#combine-sources}

You can combine data from different sources in the same message to create rich, personalized experiences.

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

## Best practices {#best-practices}

### Use descriptive variable names

Choose variable names that clearly indicate what you're iterating over:

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

Use the `{{else}}` clause to provide fallback content when an array is empty:

```handlebars
{{#each context.journey.actions.GetRecommendations.items as |item|}}
  <div>{{item.name}}</div>
{{else}}
  <p>No recommendations available at this time.</p>
{{/each}}
```

### Combine with conditional helpers

Use `{{#if}}` within loops for conditional content:

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

Handlebars provides special variables within loops:

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

## Troubleshooting {#troubleshooting}

### Array not displaying

**Issue**: Your array iteration isn't showing any content.

**Possible causes and solutions**:

1. **Incorrect path**: Verify the exact path to your array
   * For events: `context.journey.events.<event_ID>.<fieldPath>`
   * For custom actions: `context.journey.actions.<actionName>.<fieldPath>`

2. **Array is empty**: Add an `{{else}}` clause to check if the array has no data

3. **Data not available yet**: Ensure the custom action or event has been executed before the message activity

### Syntax errors

**Issue**: Expression validation fails or message doesn't render.

**Common mistakes**:

* Missing closing tags: Every `{{#each}}` must have a `{{/each}}`
* Incorrect variable name: Ensure consistent use of variable name throughout the block
* Incorrect path separators: Use dots (`.`) not slashes or other characters

### Testing your iterations

Use journey test mode to verify your iterations:

1. Start your journey in test mode
2. Trigger the event or custom action with sample data
3. Check the message preview to verify the iteration displays correctly
4. Review test mode logs for any errors

## Related topics {#related-topics}

* [Get started with personalization](personalize.md)
* [Personalization syntax](personalization-syntax.md)
* [Helper functions](functions/helpers.md)
* [Use API call responses in custom actions](../action/action-response.md)
* [Cart abandonment email use case](personalization-use-case-helper-functions.md)

