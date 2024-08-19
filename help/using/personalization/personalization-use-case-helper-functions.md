---
solution: Journey Optimizer
product: journey optimizer
title: Personalization use case&colon; cart abandonment email
description: Learn how to personalize the body of an email message through a use case.
feature: Personalization
topic: Personalization
role: Data Engineer
level: Intermediate
keywords: expression, editor, helpers,use case, personalization
exl-id: 9c9598c0-6fb1-4e2f-b610-ccd1a80e516e
---
# Personalization use case: cart abandonment email {#personalization-use-case-helper-functions}

In this example, you will personalize the body of an email message. This message targets customers who have left items in their shopping cart, but have not completed their purchase.

You will use these types of helper functions:

* The `upperCase` string function, to insert the customer's first name in capital letters. [Learn more](functions/string.md#upper).
* The `each` helper, to list the items that are in the cart. [Learn more](functions/helpers.md#each).
* The `if` helper, to insert a product-specific note if the related product is in the cart. [Learn more](functions/helpers.md#if-function).
<!-- **Context**: personalization based on contextual data from the journey -->

➡️ [Learn how to use helper functions in this video](#video)

Before you start, ensure you know how to configure these elements:

* A unitary event. [Learn more](../event/about-events.md).
* A journey that starts with an event. [Learn more](../building-journeys/using-the-journey-designer.md).
* An email message in your journey. [Learn more](../email/create-email.md)
* The body of an email. [Learn more](../email/content-from-scratch.md).

Follow these steps:

1. [Create the initial event and the journey](#create-context).
1. [Create an email message](#configure-email).
1. [Insert the customer's first name in capital letters](#uppercase-function).
1. [Add the cart content to the email](#each-helper).
1. [Insert a product-specific note](#if-helper).
1. [Test and publish the journey](#test-and-publish).

## Step 1: Create the initial event and the related journey {#create-context}

The cart content is contextual information from the journey. Therefore, you must add an initial event and the email to a journey before you can add cart-specific information to the email.

1. Create an event whose schema includes the `productListItems` array.
1. Define all the fields from this array as payload fields for this event.

   Learn more about the product list item data type in [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/xdm/data-types/product-list-item.html){target="_blank"}.

1. Create a journey that starts with this event.
1. Add an **Email** activity to the journey.

   ![](assets/personalization-uc-helpers-8.png)

## Step 2: Create the email{#configure-email}

1. In the **Email** activity, click **[!UICONTROL Edit content]**, then click **[!UICONTROL Email Designer]**.

   ![](assets/personalization-uc-helpers-1.png)

1. From the left palette of the Email Designer home page, drag and drop three structure components onto the body of the message.

1. Drag and drop an HTML content component onto each new structure component.

   ![](assets/personalization-uc-helpers-2.png)

## Step 3: Insert the customer's first name in capital letters {#uppercase-function}

1. On the Email Designer home page, click on the HTML component where you want to add the customer's first name.
1. On the contextual toolbar, click **[!UICONTROL Show the source code]**.

   ![](assets/personalization-uc-helpers-3.png)

1. In the **[!UICONTROL Edit HTML]** window, add the `upperCase` string function:
   1. In the left menu, select **[!UICONTROL Helper functions]**.
   1. Use the search field to find "upper case".
   1. From the search results, add the `upperCase` function. To do this, click the Plus (+) sign next to `{%= upperCase(string) %}: string`.

      The Expression editor shows this expression:

      ```handlebars
      {%= upperCase(string) %}
      ``` 

      ![](assets/personalization-uc-helpers-4.png)

1. Remove the "string" placeholder from the expression.
1. Add the first name token:
   1. In the left menu, select **[!UICONTROL Profile attributes]**.
   1. Select **[!UICONTROL Person]** > **[!UICONTROL Full name]**.
   1. Add the **[!UICONTROL First name]** token to the expression.

      The Expression editor shows this expression:

      ```handlebars
      {%= upperCase(profile.person.name.firstName) %}
      ``` 

      ![](assets/personalization-uc-helpers-5.png)

      Learn more about the person name data type in [Adobe Experience Plaform documentation](https://experienceleague.adobe.com/docs/experience-platform/xdm/data-types/person-name.html){target="_blank"}.

1. Click **[!UICONTROL Validate]**, then click **[!UICONTROL Save]**.

   ![](assets/personalization-uc-helpers-6.png)

1. Save the message.

## Step 4: Insert the list of items from the cart {#each-helper}

1. Reopen the message content.

1. On the Email Designer home page, click on the HTML component where you want to list the cart content.
1. On the contextual toolbar, click **[!UICONTROL Show the source code]**.

   ![](assets/personalization-uc-helpers-3.png)

1. In the **[!UICONTROL Edit HTML]** window, add the `each` helper:
   1. In the left menu, select **[!UICONTROL Helper functions]**.
   1. Use the search field to find "each".
   1. From the search results, add the `each` helper.

      The Expression editor shows this expression:

      ```handlebars
      {{#each someArray as |variable|}} {{/each}}
      ```

      ![](assets/personalization-uc-helpers-9.png)

1. Add the `productListItems` array to the expression:

   1. Remove the "someArray" placeholder from the expression.
   1. In the left menu, select **[!UICONTROL Contextual attributes]**.

      **[!UICONTROL Contextual attributes]** are available only after the journey context has been passed to the message.

   1. Select **[!UICONTROL Journey Optimizer]** > **[!UICONTROL Events]** > ***[!UICONTROL event_name]***, then expand the **[!UICONTROL productListItems]** node.

      In this example, *event_name* represents the name of your event.

   1. Add the **[!UICONTROL Product]** token to the expression.

      The Expression editor shows this expression:

      ```handlebars
      {{#each context.journey.events.event_ID.productListItems.product as |variable|}} {{/each}}
      ```
   
      In this example, *event_ID* represents the ID of your event.

      ![](assets/personalization-uc-helpers-10.png)

   1. Modify the expression:
      1. Remove the ".product" string.
      1. Replace the "variable" placeholder with "product".

      This example shows the modified expression:

      ```handlebars
      {{#each context.journey.events.event_ID.productListItems as |product|}}
      ```

1. Paste this code between the opening `{{#each}}` tag and the closing `{/each}}` tag:

   ```html
   <table>
      <tbody>
         <tr>
            <td><b>#name</b></td>
            <td><b>#quantity</b></td>
            <td><b>$#priceTotal</b></td>
         </tr>
      </tbody>
   </table>
   ```

1. Add the personalization tokens for the item name, the quantity, and the price:

   1. Remove the placeholder "#name" from the HTML table.
   1. From the previous search results, add the **[!UICONTROL Name]** token to the expression.

   Repeat these steps twice:

   * Replace the placeholder "#quantity" with the **[!UICONTROL Quantity]** token.
   * Replace the placeholder "#priceTotal" with the **[!UICONTROL Total price]** token.

   This example shows the modified expression:

   ```handlebars
   {{#each context.journey.events.event_ID.productListItems as |product|}}
      <table>
         <tbody>
            <tr>
            <td><b>{{product.name}}</b></td>
            <td><b>{{product.quantity}}</b></td>
            <td><b>${{product.priceTotal}}</b></td>
            </tr>
         </tbody>
      </table>
   {{/each}}
   ```

1. Click **[!UICONTROL Validate]**, then click **[!UICONTROL Save]**.

   ![](assets/personalization-uc-helpers-11.png)

## Step 5: Insert a product-specific note {#if-helper}

1. On the Email Designer home page, click on the HTML component where you want to insert the note.
1. On the contextual toolbar, click **[!UICONTROL Show the source code]**.

   ![](assets/personalization-uc-helpers-3.png)

1. In the **[!UICONTROL Edit HTML]** window, add the `if` helper:
   1. In the left menu, select **[!UICONTROL Helper functions]**.
   1. Use the search field to find "if".
   1. From the search results, add the `if` helper.

      The Expression editor shows this expression:

      ```handlebars
      {%#if condition1%} render_1
         {%else if condition2%} render_2
         {%else%} default_render
      {%/if%}
      ```

      ![](assets/personalization-uc-helpers-12.png)

1. Remove this condition from the expression:

   ```handlebars
   {%else if condition2%} render_2
   ```

   This example shows the modified expression:

   ```handlebars
   {%#if condition1%} render_1
      {%else%} default_render
   {%/if%}
   ```

1. Add the product name token to the condition:
   1. Remove the "condition1" placeholder from the expression.
   1. In the left menu, select **[!UICONTROL Contextual attributes]**.
   1. Select **[!UICONTROL Journey Orchestration]** > **[!UICONTROL Events]** > ***[!UICONTROL event_name]***, then expand the **[!UICONTROL productListItems]** node.

      In this example, *event_name* represents the name of your event.

   1. Add the **[!UICONTROL Name]** token to the expression.

      The Expression editor shows this expression:

      ```handlebars
      {%#if context.journey.events.`event_ID`.productListItems.name%}
         render_1
         {%else%} default_render
      {%/if%}
      ```

      ![](assets/personalization-uc-helpers-13.png)

1. Modify the expression:
   1. In the Expression editor, specify the product name after the `name` token.
         
      Use this syntax, where *product_name* represents the name of your product:

      ```javascript
      = "product_name"
      ```

      In this example, the product name is "Juno Jacket":

      ```handlebars
      {%#if context.journey.events.`event_ID`.productListItems.name = "Juno Jacket" %}
         render_1
         {%else%} default_render
      {%/if%}
      ```

   1. Replace the "render_1" placeholder with the text of the note.

      Example:

      ```handlebars
      {%#if context.journey.events.`event_ID`.productListItems.name = "Juno Jacket" %}
         Due to longer than usual lead times on the Juno Jacket, please expect item to ship two weeks after purchase.
         {%else%} default_render
      {%/if%}
      ```

   1. Remove the "default_render" placeholder from the expression.
1. Click **[!UICONTROL Validate]**, then click **[!UICONTROL Save]**.

   ![](assets/personalization-uc-helpers-14.png)

1.  Save the message.

## Step 6: Test and publish the journey {#test-and-publish}

1. Turn on the **[!UICONTROL Test]** toggle, then click **[!UICONTROL Trigger an event]**.

   ![](assets/personalization-uc-helpers-15.png)

1. In the **[!UICONTROL Event configuration]** window, enter the input values, then click **[!UICONTROL Send]**.

   The test mode works only with test profiles.

   ![](assets/personalization-uc-helpers-16.png)

   The email is sent to the address of the test profile.

   In this example, the email contains the note about the Juno Jacket because this product is in the cart:

   ![](assets/personalization-uc-helpers-17.png)

1. Verify that there is no error, then publish the journey.


## Related topics {#related-topics}

### Handlebars functions {#handlebars}

* [Helpers](functions/helpers.md)

* [String functions](functions/string.md)

### Use cases {#use-case}

* [Personalization with profile information, context, and offer](personalization-use-case.md)

* [Personalization with decision-based offer](../offers/offers-e2e.md)

## How-to video{#video}

Learn how to use helper functions.

>[!VIDEO](https://video.tv.adobe.com/v/334244?quality=12)
