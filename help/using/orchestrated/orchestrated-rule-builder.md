---
solution: Journey Optimizer
product: journey optimizer
title: Work with the rule builder
description: Learn how to create rules for your Orchestrated campaigns
exl-id: fb7a0eb2-b2ff-49fa-af1f-f1c10f219b00
version: Campaign Orchestration
---

# Work with the rule builder {#orchestrated-rule-builder}

Orchestrated campaigns comes with a rule builder that simplifies the process of filtering the database based on various criteria. The rule builder manages very complex and long queries efficiently, offering enhanced flexibility and precision.

It also supports predefined filters within conditions, empowering you to refine queries with ease while utilizing advanced expressions and operators for comprehensive audience targeting and segmentation strategies.

## Access the rule builder {#access}

The rule builder is available in every context where you need to define rules to filter data.

|Usage|Example|
|  ---  |  ---  |
|**Build audiences**: Specify the population you want to target in your Orchestrated campaigns using a **[!UICONTROL Build audience]** activity, and effortlessly create new audiences tailored to your needs. [Learn how to build audiences](../orchestrated/activities/build-audience.md)|![Image showing how to access the audience creation interface](assets/query-access-audience.png){width="200" align="center" zoomable="yes"}|
|**Create condition in the campaign canvas**: Apply rules within the campaign canvas using a  **[!UICONTROL Split]** activity, to align with your specific requirements. [Learn how to use a Split activity](../orchestrated/activities/split.md)|![Image showing how to access workflow customization options](assets/query-access-split.png){width="200" align="center" zoomable="yes"}|
|**Create advanced filters**: Build rules to filter the data displayed in lists such as campaign logs or targeting dimensions.|![Image showing how to customize list filters](assets/query-access-advanced-filters.png){width="200" align="center" zoomable="yes"}|

## Rule builder interface {#interface}

The rule builder provides a central canvas where you build your query and a properties pane that provides information on the rule.

![Image showing the rule builder interface](assets/rule-builder-interface.png)

*  The **central canvas** is where you add and combine the different components to build your rule. [Learn how to build a rule](../orchestrated/build-query.md)

* The **[!UICONTROL Rule properties]** pane provides information on your rule. It allows you to perform various operations to check the rule and ensure it suits your needs.

    This pane displays when building a query to create an audience. [Learn how to check and validate your query](build-query.md#check-and-validate-your-query)

## Work with predefined filters

Predefined filters let you reuse saved queries in the rule builder, including versions with parameters. For a full walkthrough of saving, applying, and managing predefined filters, see [Work with predefined filters](predefined-filters.md).
