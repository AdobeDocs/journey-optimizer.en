---
title: Use decision policies in messages
description: Learn how to use decisions policies in your messages.
feature: Decisioning
topic: Integrations
role: User
level: Experienced
mini-toc-levels: 1
---
# Use decision policies in messages {#create-decision}

Once a decision policy has been created, the policy and the attributes linked to the returned decision items can be used in your content for personalization. To do so, the code associated to the decision policy must first be inserted into your content. Once done, you can leverage its attributes for personalization.

## Insert the decision policy code {#insert-code}

>[!BEGINTABS]

>[!TAB Code-based experience]

1. Open the personalization editor and access the **[!UICONTROL Decision policies]** menu.

1. Select **[!UICONTROL Insert policy]** to add the code corresponding to the decision policy.

    ![](assets/decision-code-based-add-decision.png)

    >[!NOTE]
    >
    >If the code insertion button does not display, a decision policy may already have been configured for the parent component.

1. The code for the decision policy is added. This sequence will be repeated the number of times you want the decision policy to be returned. For example, if you chose to return back 2 items when [creating the decision](#add-decision), the same sequence will be repeated twice.

>[!TAB Email]

1. Open the personalization editor and access the **[!UICONTROL Decision policy]** menu.

1. Select **[!UICONTROL Insert syntax]** to add the code corresponding to the decision policy.

    ![](assets/decision-policy-add.png)

    >[!NOTE]
    >
    >If the code insertion button does not display, a decision policy may already have been configured for the parent component.
    
1. If no placement has been associated to the component beforehand, select one from the list and click **[!UICONTROL Assign]**.

    ![](assets/decision-policy-placement.png)

>[!ENDTABS]

1. The code for the decision policy is added. This sequence will be repeated the number of times you want the decision policy to be returned. For example, if you chose to return back 2 items when [creating the decision](#add-decision), the same sequence will be repeated twice.

## Leverage decision items attributes {#attributes}

Now you can add all the decision attributes you want inside that code. The available attributes are stored in the **[!UICONTROL Offers]** catalog's schema. Custom attributes are stored in the **`_<imsOrg`>** folder and standard attributes in the **`_experience`** folder. [Learn more about the Offers catalog's schema](catalogs.md)

![](assets/decision-code-based-decision-attributes.png)

>[!NOTE]
>
>For decision policy Item tracking, the `trackingToken` attribute needs to be added as following for decision policy content:
>`trackingToken: {{item._experience.decisioning.decisionitem.trackingToken}}`

To add an attribute, click the '+' icon next to it. You can add as many attributes as you want to the code.

![](assets/decision-code-based-add-decision-attributes.png)

Make sure you wrap the `#each` loop inside a pair of square brackets `[ ]`, and add a comma right before the closing `/each`.

![](assets/decision-code-based-wrap-code.png)

You can also add any other attribute available in the personalization editor, such as profile attributes.

![](assets/decision-code-based-decision-profile-attribute.png)

## Leverage fragments {#fragments}

If your decision policy contains decision items including fragments, you can leverage these fragments in the decision policy code. [Learn more on fragments](../content-management/fragments.md)

>[!AVAILABILITY]
>
>This capability is currently only available for a set of organizations (Limited Availability). For more information, contact your Adobe representative.

For example, let's say you want to display different contents for several mobile device models. Make sure you added fragments corresponding to those devices to the decision item that you are using in the decision policy. [Learn how](items.md#attributes).

![](assets/item-fragments.png){width=70%}

Once done, you can use either one of the following methods:

>[!BEGINTABS]

>[!TAB Directly insert the code]

Simply copy-paste the code block below into the decision policy code. Replace `variable` with the fragment ID and `placement` with the fragment reference key:

```
{% let variable =  get(item._experience.decisioning.offeritem.contentReferencesMap, "placement").id %}
{{fragment id = variable}}
```

>[!TAB Follow the detailed steps]

1. Navigate to the **[!UICONTROL Helper functions]** and add the **Let** function `{% let variable = expression %} {{variable}}` to the code pane, where you can declare the variable for your fragment.

    ![](assets/decision-let-function.png)

1. Use the **Map** > **Get** function `{%= get(map, string) %}` to build your expression. The map is the fragment referenced in the decision item and the string can be the device model you entered in the decision item as the **[!UICONTROL Fragment reference key]**.

    ![](assets/decision-map-function.png)

1. You can also use a contextual attribute which would contain this device model ID.

    ![](assets/decision-contextual-attribute.png)

1. Add the variable that you chose for your fragment as the fragment ID.

    ![](assets/decision-fragment-id.png)

>[!ENDTABS]

The fragment ID and reference key will be selected from the decision item's **[!UICONTROL Fragments]** section.

>[!WARNING]
>
>If the fragment key is incorrect or if the fragment content is not valid, rendering will fail causing error in the Edge call.

### Guardrails when using fragments {#fragments-guardrails}

**Decision item and context attributes**

Decision item attributes and contextal attribute are not supported by default in [!DNL Journey Optimizer] fragments. However, you can use global variables instead, such as described below.

Let's say you want to use the *sport* variable in your fragment.

1. Reference this variable in the fragment, for example:

    ```
    Elevate your practice with new {{sport}} gear!
    ```

1. Define the variable with the **Let** function within the decision policy block. In the example below, *sport* is defined with the decision item attribute:

    ```
    {#each decisionPolicy.13e1d23d-b8a7-4f71-a32e-d833c51361e0.items as |item|}}
    {% let sport = item._cjmstage.value %}
    {{fragment id = get(item._experience.decisioning.offeritem.contentReferencesMap, "placement1").id }}
    {{/each}}
    ```

**Decision item fragment content validation**

* Due to the dynamic nature of these fragments, when used in a campaign, the message validation during the campaign content creation is skipped for fragments that are referenced in decision items.

* The validation of the fragment content happens only during the fragment creation and publication.

* In case of JSON fragments, the validity of the JSON object is not ensured. Make sure that the expression fragment content is a valid JSON so that it can be used in decision items.

At runtime, the campaign content (including fragment content from decision items) is validated. In case of a validation failure, the campaign will not get rendered.

## Next steps {#final-steps}

Once that your content is ready, review and publish your campaign or journey:

* [Publish a journey](../building-journeys/publishing-the-journey.md)
* [Review activate a campaign](../campaigns/review-activate-campaign.md)
* [Publish and activate a code-based experience](../code-based/publish-code-based.md)

For code-based experiences, as soon as your developer makes an API or SDK call to fetch content for the surface defined in your channel configuration, the changes will be applied to your web page or app.

>[!NOTE]
>
>Currently you cannot simulate content from the user interface in a [code-based experience](../code-based/create-code-based.md) campaign or journey using decisions. A workaround is available in [this section](../code-based/code-based-decisioning-implementations.md).

To see how your decisions are performing, you can create custom [Customer Journey Analytics reporting dashboards](cja-reporting.md).

