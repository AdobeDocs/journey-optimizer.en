---
solution: Journey Optimizer
product: journey optimizer
title: Build your first query
description: Learn how to create queries for your orchestrated campaigns
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 5e956a6a-0b89-4d78-8f16-fe9fceb25674
---
# Build your first query {#build-query}

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](configuration-steps.md)<br/><br/>[Key steps for orchestrated campaign creation](gs-campaign-creation.md)|[Create an orchestrated campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Send messages with orchestrated campaigns](send-messages.md)<br/><br/>[Start and monitor the campaign](start-monitor-campaigns.md)<br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Split](activities/split.md) -  [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

<br/>

>[!BEGINSHADEBOX]

Documentation in progress

>[!ENDSHADEBOX]

<!--
The main steps to build rules for your orchestrated campaigns are as follows:

1. **Add conditions** - Create custom conditions to filter your query by building your own condition with attributes from the database and advanced expressions.
1. **Combine conditions** - Arrange the conditions in the canvas using groups and logical operators.
1. **Check and validate the rule** - Check the resulting data of your rule before saving it.

## Add a condition {#conditions}

To add conditions in your query, follow these steps:

1. Access the rule builder from a **[!UICONTROL Build audience]** activity.

1. Click the **Add condition** button to create a first condition for your query.

    You can also start your query using a predefined filter. To do so, click the **[!UICONTROL Select or save filter]** button and choose **[!UICONTROL Select predefined filter]**. 

1. Identify the attribute from the dabatase to use as criteria for your condition. The "i" icon next to an attribute provides information on the table where it is store and its data type.

    ![image showing the selection of an attribute](assets/rule-builder-select-attribute.png)

    >[!NOTE]
    >
    >The **Edit expression** button allows you to use the expression editor to manually define an expression using fields from the database and helper functions. [Learn how to edit expressions](expression-editor.md)

1. Click the ![image showing the More actions button](assets/do-not-localize/rule-builder-icon-more.svg) button next to an attribute to access these addititional options:

    +++ Distribution of values

    Analyze the distribution of values for a given attribute within the table. This feature is helpful for understanding the available values, their counts, and percentages. It also helps avoid issues such as inconsistent capitalization or spelling when building queries or creating expressions.

    For attributes with a large number of values, the tool displays only the first twenty. In such cases, a **[!UICONTROL Partial load]** notification appears to indicate this limitation. You can apply advanced filters to refine the displayed results and focus on specific values or subsets of data.

    ![image showing the Distribution of values interface](assets/rule-builder-distribution-values.png)

    +++

    +++ Add to favorites
    
    Adding attributes to your favorites menu provides quick access to your most frequency used attributes. You can add up to 20 attributes to favorites. Favorite and recent attributes are associated with each user within an organization, ensuring accessibility across different machines and providing a seamless experience across devices.
    
    To access attributes you have favorited, use the **[!UICONTROL Favorites and recents]** menu. Favorite attributes appear first, followed by recently used ones, making it easy to locate the required attributes. To remove an attribute from favorites, select the star icon again.

    ![image showing the favorites interface](assets/rule-builder-favorites.png)

    +++

1. Click **[!UICONTROL Confirm]** to add the selected attribute to your condition.

1. A properties pane displays, where you can configure the desired values for the attribute.

    ![image showing the rule builder with a condition added](assets/rule-builder-condition.png)

1. Select the **[!UICONTROL Operator]** to apply from the drop-down list. 
    
    Various operators are available for use. Operators available in the drop-down list depend on the attribute's data type.

   +++List of available operators

    |Operator|Purpose|Example|
    |---|---|---|
    |Equal to|Returns a result identical to the data entered in the second Value column.|Last name (@lastName) equal to 'Jones' will return only recipients whose last name is Jones.|
    |Not equal to|Returns all values not identical to the value entered.|Language (@language) not equal to 'English'.|
    |Greater than|Returns a value greater than the value entered.|Age (@age) greater than 50 will return all values greater than '50', such as '51', '52'.|
    |Less than|Returns a value smaller than the value entered.|Creation date (@created) before 'DaysAgo(100)' will return all recipients created less than 100 days ago.|
    |Greater than or equal to|Returns all values equal to or greater than the value entered.|Age (@age) greater than or equal to '30' will return all recipients aged 30 or more.|
    |Less than or equal to|Returns all values equal to or lower than the value entered.|Age (@age) less than or equal to '60' will return all recipients aged 60 or less.|
    |Included in|Returns results included in the values indicated. These values must be separated by a comma.|Birth date (@birthDate) is included in '12/10/1979,12/10/1984' will return the recipients born between these dates.|
    |Not in|Works like the Is included in operator. Here, recipients are excluded based on the values entered.|Birth date (@birthDate) is not included in '12/10/1979,12/10/1984'. Recipients born within these dates will not be returned.|
    |Is empty|Returns results matching an empty value in the second Value column.|Mobile (@mobilePhone) is empty returns all recipients who do not have a mobile number.|
    |Is not empty|Works in reverse to the Is empty operator. It is not necessary to enter data in the second Value column.|Email (@email) is not empty.|
    |Starts with|Returns results starting with the value entered.|Account # (@account) starts with '32010'.|
    |Does not start with|Returns results not starting with the value entered.|Account # (@account) does not start with '20'.|
    |Contains|Returns results containing at least the value entered.|Email domain (@domain) contains 'mail' will return all domain names that contain 'mail', such as 'gmail.com'.|
    |Does not contain|Returns results not containing the value entered.|Email domain (@domain) does not contain 'vo'. Domain names containing 'vo', such as 'voila.fr', will not appear in the results.|
    |Like|Similar to the Contains operator, it lets you insert a % wildcard character in the value.|Last name (@lastName) like 'Jon%s'. The wildcard character acts as a "joker" to find names like "Jones".|
    |Not like|Similar to the Contains operator, it lets you insert a % wildcard character in the value.|Last name (@lastName) not like 'Smi%h'. Recipients whose last name is 'Smith' will not be returned.|

    +++

1. In the **Value** field, define the expected value. You can also use the expression editor to manually define an expression using fields from the database and helper functions. To do this, click the ![image showing the expression editor icon](assets/do-not-localize/rule-builder-icon-editor.svg) icon. [Learn how to edit expressions](expression-editor.md)

    For date-type attributes, predefined values are available using the **[!UICONTROL Presets]** option.

    +++See example
    
    ![image showing the preset option](assets/rule-builder-attribute-preset.png) 

    +++

### Custom conditions on linked tables (1-1 and 1-N links){#links}

Custom conditions allows you to query tables linked to the table currently used by your rule. This includes tables with a 1-1 cardinality link, or collection tables (1-N link).

For a **1-1 link**, navigate to the linked table, select the desired attribute and define the expected value.

You can also directly select a table link in the **Value** picker and confirm. In that case, values available for the selected table need to be selected using a dedicated picker, as shown in the example below.

+++Query example

Here, the query is targeting brands whose label is "running". 

1. Navigate inside the **Brand** table and select the **Label** attribute.

    ![Screenshot of the Brand table](assets/1-1-attribute.png){zoomable="yes"}{width="85%" align="center"}

1. Define the expected value for the attribute.

    ![Example of a defined expected value](assets/1-1-table.png){zoomable="yes"}{width="85%" align="center"}

Here is a query sample where a table link has been selected directly. Available values for this table must be selected from a dedicated picker.

![Example of a query sample](assets/1-1-table-direct.png){zoomable="yes"}{width="85%" align="center"}

+++ 

For a **1-N link**, you can define sub-conditions to refine your query, as shown in the example below.

+++Query example

Here, the query is targeting recipients who made purchases related to the BrewMaster product, for a total amount of at least 100$.

1. Select the **Purchases** table and confirm.

    ![Screenshot of the Purchase table](assets/1-N-collection.png){zoomable="yes"}{width="50%" align="center"}

1. An outbound transition is added, allowing you to create sub-conditions.

    ![Example of an outbound transition](assets/1-n-subcondition.png){zoomable="yes"}{width="85%" align="center"}

1. Select the **Price** attribute and target purchases of 1000$ or more

    ![Screenshot of the Price attribute](assets/1-n-price.png){zoomable="yes"}{width="85%" align="center"}

1. Add sub-conditions to suit your needs. Here we have added a condition to target profiles who purchased a BrewMaster product.

    ![Example of sub-conditions](assets/custom-condition-1-N.png){zoomable="yes"}{width="85%" align="center"}

+++ 

### Custom conditions with aggregate data {#aggregate}

Custom conditions allow you to perform aggregate operations. To do this, you need to directly select an attribute from a collection table:

1. Navigate inside the desired collection table and select the attribute on which you want to perform an aggregate operation.

    ![Screenshot of the attribute list](assets/aggregate-attribute.png){zoomable="yes"}{width="85%" align="center"}

1. In the properties pane, toggle on the **Aggregate data** option and select the desired aggregate function.







## Combine conditions with groups and operators

Use **Group operators** (AND, OR, EXCEPT) allow you to group filtering components in the diagram. They are added on existing transitions before a filtering component. [Learn how to work with operators](#filtering)

    Example: *Recipients who are Super VIP **AND** VIP to reward **OR** VIP Demo, **EXCEPT** recipients under 21 years old and above 45.










### Copy-paste components {#copy}

The rule builder allows you to copy one or multiple filtering components and paste them at the end of a transition. This operation can be executed within the current query canvas, or in any canvas within your instance.

>[!NOTE]
>
>The copied selection is kept as long as you are working in your instance. If you log off and log back in, your selection will no longer be available for pasting.

>[!IMPORTANT]
>
>It is currently impossible to copy and paste components in the New Rule builder experience. To follow these next steps, please click the **[!UICONTROL Get back to the classic experience]** toggle at the top to use the Classic Rule builder.


To copy-paste filtering components, follow these steps:

1. Select the filtering component that you want to copy by clicking on it in the query canvas. To select multiple components, use the multiple selection tool available in the toolbar located at the upper-right corner of the canvas.

1. Click the **[!UICONTROL Copy]** button in the component's properties pane or in the blue ribbon at the bottom of the screen if you have selected multiple components.

    |Copy a single component|Copy multiple components|
    |  ---  |  ---  |
    |![](assets/copy-single-component.png){zoomable="yes"}{width="200" align="center" zoomable="yes"}|![](assets/copy-multiple-components.png){zoomable="yes"}{width="200" align="center" zoomable="yes"}|

1. To paste the component(s), click the + button at the end of the desired transition and select **Paste n items**.

    ![Example of pasting the components](assets/copy-paste.png){zoomable="yes"}

## Combine filtering components with operators {#operators}

>[!CONTEXTUALHELP]
>id="acw_orchestration_querymodeler_group"
>title="Group"
>abstract="In this pane, you can change the operator used to link filtering conditions together."

Each time you add a new filtering component to your query, it is automatically linked to the other component by an **AND** operator. This means that results from the two filtering components are combined.

In this example, we have added a new audience-type filtering components on the second transition. The component is linked to the predefined filter condition with an **AND** operator, meaning that the query results include recipients targeted by the "Newsletter Subscribers - MADRID" predefined filter AND belonging to the "Purchasers (All time)" audience.

>[!BEGINTABS]

>[!TAB Classic rule builder]

![Example of a query](assets/query-operator.png){zoomable="yes"}

To change the operator used to link filtering conditions together, click on it and select the desired operator in the **Group** pane that opens on the right hand side.

Available operators are:

* **AND (Intersection)**: Combines results matching all the filtering components in the outbound transitions. 
* **OR (Union)**: Includes results matching at least one of the filtering components in the outbound transitions.
* **EXCEPT (Exclusion)**: Excludes results matching all the filtering componentns in the outbound transition. 

![Example of a query](assets/query-operator-change.png){zoomable="yes"}

In addition, you can create intermediate groups of components by grouping components into a same group and linking them together. That way, the AND operator will be put by default, you can then change it to the desired operator.

>[!TAB New rule builder]

![Example of a query](assets/ruleb-9.png){zoomable="yes"}

To change the operator used to link filtering conditions together, click on it, it will change to OR, EXCEPT and then back to AND, and select the desired operator.

Available operators are:

* **AND (Intersection)**: Combines results matching all the filtering components in the outbound transitions. 
* **OR (Union)**: Includes results matching at least one of the filtering components in the outbound transitions.
* **EXCEPT (Exclusion)**: Excludes results matching all the filtering componentns in the outbound transition.

![Example of a query](assets/ruleb-10.gif){zoomable="yes"}

>[!ENDTABS]

In the example below, we have created an intermediate group to include results from either the "VIP to reward" or "Super VIP" audiences.

>[!BEGINTABS]

>[!TAB Classic rule builder]

![Example of a query](assets/query-intermediate-group.png){zoomable="yes"}

>[!TAB New rule builder]

![Example of a query in the new rule builder](assets/ruleb-11.png){zoomable="yes"}

>[!ENDTABS]

## Check and validate your query

>[!CONTEXTUALHELP]
>id="acw_orchestration_querymodeler_ruleproperties"
>title="Rule properties"
>abstract="Once you've built your query in the canvas, you can check it using the **Rule properties** pane located on the right hand side.<br/>This pane allows you to display the resulting data, to retrieve an SQL code version of the query, and check the number of targeted records.<br/>Use the **Select or save filter** button to save your query as a predefined filter, or replace the canvas content with an existing filter."

Once you've built your query in the canvas, you can check it using the **Rule properties** pane located on the right hand side  This pane displays when building a query to create an audience. Available operations are:

* **View results:** Displays the data resulting from your query.
* **Code view**: Displays a code-based version of the query in SQL.
* **Calculate**: Updates and displays the number of records targeted by your query.
* **Select or save filter**: Choose an existing predefined filter to use in the canvas, or save your query as a predefined filter for future reuse. [Learn how to work with predefined filters](../get-started/predefined-filters.md)

    >[!IMPORTANT]
    >
    >Select a predefined filter from the Rule properties pane replaces the query that has been built in the canvas with the selected filter.

When your query is ready, click the **[!UICONTROL Confirm]** button in the upper-right corner to save it.


>[!BEGINTABS]

>[!TAB Classic rule builder]

You can modify your query at any time by opening it. Keep in mind that upon opening an existing query, it displays in a simplified view without the visiblity of  **+** buttons. To add new elements to the query, select a component or operator on the canvas to display the **+** buttons.

![Example of a query](assets/edit-audience.png){zoomable="yes"}

>[!TAB New Rule builder]

You can modify your query at any time by opening it, to do that, click on the **[!UICONTROL Add condition]** button on the top-left corner.

![Example of a query in the new rule builder](assets/ruleb-11.png){zoomable="yes"}

>[!ENDTABS]
-->