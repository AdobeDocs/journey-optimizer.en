---
title: Leverage fragments in decision policies
description: Learn how to leverage fragments in decision policies
feature: Decisioning
topic: Integrations
role: User
level: Experienced
exl-id: 70f64348-092b-4350-91dc-72c3c07300f9
badge: label="Limited Availability" type="Informative"
---
# Leverage fragments in decision policies {#fragments}

If your decision policy contains decision items including fragments, you can leverage these fragments when authoring a message, within the decision policy. [Learn more on fragments](../content-management/fragments.md)

>[!AVAILABILITY]
>
>This feature is available in Limited Availability for the **Code-based experience** and **Email** channels. To request access, contact your Adobe representative.

For example, let's say you want to display different contents for several mobile device models. Add the specified fragments, each pertaining to a different phone model, to the decision item you are using in the decision policy. [Learn how](items.md#attributes).

![Fragments section of a decision item showing fragment references and placement keys.](assets/item-fragments.png){width=70%}

Once done, you can use either one of the following methods:

>[!BEGINTABS]

>[!TAB Directly insert the code]

Simply copy-paste the code block below into the decision policy code. Replace `variable` with the fragment ID and `placement` with the fragment reference key:

```handlebars
{% let variable =  get(item._experience.decisioning.offeritem.contentReferencesMap, "placement").id %}
{{fragment id = variable required=false}}
```

>[!TAB Follow the detailed steps]

1. Navigate to the **[!UICONTROL Helper functions]** and add the **Let** function `{% let variable = expression %} {{variable}}` to the code pane, where you can declare the variable for your fragment.

    ![Decision policy code editor showing the Let helper function added to the code pane.](assets/decision-let-function.png)

1. Use the **Map** > **Get** function `{%= get(map, string) %}` to build your expression. The map is the fragment referenced in the decision item. The string can be the device model you entered in the decision item as the **[!UICONTROL Fragment reference key]**.

    ![Map and Get functions used to reference the fragment map and fragment reference key.](assets/decision-map-function.png)

1. You can also use a contextual attribute which would contain this device model ID.

    ![Contextual attribute selected for the device model identifier.](assets/decision-contextual-attribute.png)

1. Add the variable that you chose for your fragment as the fragment ID.

    ![Fragment ID variable set from the decision item in the decision policy code.](assets/decision-fragment-id.png)

>[!ENDTABS]

The fragment ID and reference key will be selected from the decision item's **[!UICONTROL Fragments]** section.

>[!WARNING]
>
>If the fragment key is incorrect or if the fragment content is not valid, rendering may fail and cause an error in the Edge call.
>
>To avoid failures when a fragment is temporarily unavailable, the `required=false` flag is used so the fragment is skipped instead. [Learn more](#temporary-unavailable-fragments)

## Usage and guardrails {#fragments-guardrails}

### Simulate content and expression fragments in emails {#simulate-content-expression-fragments}

For the **Email** channel, expression fragments associated with a decision item display correctly when you **[!UICONTROL Send proof]** or when the campaign is activated. However, **[!UICONTROL Simulate content]** does not display the expression fragment from the decision item.

### Visual fragments and decision items in emails {#visual-fragments-decision-items}

You cannot assign a **[!UICONTROL Visual fragment]** to a decision item, only **expression fragments** are supported in this context.

### Decision item and context attributes {#decision-item-context-attributes}

Decision item attributes and contextual attributes are not supported by default in [!DNL Journey Optimizer] fragments. However, you can use global variables instead, such as described below.

Let's say you want to use the *sport* variable in your fragment.

1. Reference this variable in the fragment, for example:

    ```text
    Elevate your practice with new {{sport}} gear!
    ```

1. Define the variable with the **Let** function within the decision policy block. In the example below, *sport* is defined with the decision item attribute:

    ```handlebars
    {#each decisionPolicy.13e1d23d-b8a7-4f71-a32e-d833c51361e0.items as |item|}}
    {% let sport = item._cjmstage.value %}
    {{fragment id = get(item._experience.decisioning.offeritem.contentReferencesMap, "placement1").id }}
    {{/each}}
    ```

### Decision item fragment content validation {#fragment-content-validation}

* Due to the dynamic nature of these fragments, when used in a campaign, message validation during campaign content creation is skipped for fragments referenced in decision items.

* The validation of the fragment content happens only during the fragment creation and publication.

* For JSON-type expression fragments, the content is syntactically validated upon saving the fragment. Validation errors are displayed as alerts.

At runtime, the campaign content (including fragment content from decision items) is validated. In case of a validation failure, the campaign will not get rendered.

### Temporarily unavailable fragments are skipped {#temporary-unavailable-fragments}

When journeys or campaigns reference fragments attached to decision items, there can be short synchronization delays before updated fragments are available on Edge.

To avoid failures when a fragment is temporarily unavailable, fragments now have the `required` flag set to `false` by default so that they are skipped instead of causing the journey or campaign to fail.

This means that if the fragment is temporarily unavailable on Edge, it is simply ignored. If the fragment is available, it renders normally.

**Example**

If your decision policy qualifies for two offers and each has a fragment—for example, "20% off" and "30% off"—and the second fragment is temporarily unavailable, with `required=false` the system renders the available offer (20% off) and skips the other fragment (30% off) instead of failing the journey or campaign. This improves reliability when content is still synchronizing.

>[!NOTE]
>
>You can still mark a fragment as mandatory by setting the `required` flag to `true`. However, if a fragment is temporarily missing, it may cause journey or campaign rendering to fail.