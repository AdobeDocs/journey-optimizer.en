---
solution: Journey Optimizer
product: journey optimizer
title: Use the Reconciliation activity
description: Learn how to use the Reconciliation activity in a multi-step campaign
hide: yes
hidefromtoc: yes
exl-id: 0d5cfffe-bc6c-40bc-b3e1-5b44368ac76f
---
# Reconciliation {#reconciliation}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation"
>title="Reconciliation activity"
>abstract="The **Reconciliation** activity is a **Targeting** activity which allows you to define the link between Adobe Journey Optimizer and the data in a work table." 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_field"
>title="Reconciliation select field"
>abstract="Reconciliation select field" 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_condition"
>title="Reconciliation create condition"
>abstract="Reconciliation create condition" 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_complement"
>title="Reconciliation generate complement"
>abstract="Reconciliation generate complement" 

The **Reconciliation** activity is a **Targeting** activity which allows you to define the link between the data in Adobe Journey Optimizer and the data in a work table, for example data loaded from an external file.

## Best practices {#reconciliation-best-practices}

While the **Enrichment** activity allows you to define additional data to process in your multi-step campaign (you can use an **Enrichment** activity to combine data coming from multiple sets, or to create links to a temporary resource), the **Reconciliation** activity allows you to link unidentified data to existing resources. 

>[!NOTE]
>Reconciliation operation implies that the data of the linked dimensions are already in the database.  For example, if you import a file of purchases showing which product was purchased, at what time, by which client, etc., the product as well as the client must already exist in the database.

## Configure the Reconciliation activity {#reconciliation-configuration}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_targeting"
>title="Targeting dimension"
>abstract="Select the new targeting dimension. A dimension lets you define the targeted population: recipients, app subscribers, operators, subscribers, etc. By default, the current targeting dimension is selected." 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_rules"
>title="Reconciliation rules"
>abstract="Select reconciliation rules to use for the deduplication. To use attributes, select the **Simple attributes** option and choose the source and destination fields. To create your own reconciliation condition using the query modeler, select the **Advanced reconciliation conditions** option."
>additional-url="https://experienceleague.adobe.com/en/docs/campaign-web/v8/query-database/query-modeler-overview" text="Work with the query modeler"

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_targeting_selection"
>title="Select the targeting dimension"
>abstract="Select the targeting dimension for your inbound data to reconcile with." 
>additional-url="https://experienceleague.adobe.com/docs/campaign-web/v8/audiences/gs-audiences-recipients.html#targeting-dimensions" text="Targeting dimensions"

>[!CONTEXTUALHELP]
>id="ajo_orchestration_keep_unreconciled_data"
>title="Keep unreconciled data"
>abstract="By default, non reconciled data are kept in the outbound transition and available in the worktable for future use. To remove unreconciled data, desactivate the **Keep unreconciled data** option." 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_attribute"
>title="Reconciliation attribute"
>abstract="Select the attribute to use to reconciliate data, and click Confirm." 

Follow these steps to configure the **Reconciliation** activity:

1. Add a **Reconciliation** activity into your multi-step campaign.

1. Select the new targeting dimension. A dimension lets you define the targeted population: recipients, app subscribers, operators, subscribers, etc.

1. Select the field(s) to use for the reconciliation. You can use one or more reconciliation criteria.

    1. To use attributes to reconcile data, select the **Simple attributes** option. The **Source** field lists the fields available in the input transition, which are to be reconcilied. The **Destination** field corresponds to the fields of the selected targeting dimension. Data are reconcilied when source and destination are equal. For example, select the **Email** fields to deduplicate profiles based on their email address. 
        
        To add another reconciliation criteria, click the **Add rule** button. If several join conditions are specified, they must ALL be verified so that the data can be linked together.    

        ![](../assets/workflow-reconciliation-criteria.png)

    1. To use other attributes to reconcile data, select the **Advanced reconciliation conditions** option. You can then create your own reconciliation condition using the query modeler. 

1. You can filter data to reconciliate using the **Create filter** button. This lets you create a custom condition using the query modeler.

By default, non reconcilied data are kept in the outbound transition and available in the worktable for future use. To remove unreconciled data, desactivate the **Keep unreconciled data** option.

## Example {#reconciliation-example}

The following example demonstrates a multi-step campaign that creates an audience of profiles directly from an imported file containing new clients. It is made up of the following activities:

The multi-step campaign is designed as follows:

![](../assets/workflow-reconciliation-sample-1.0.png)

 
It is built with the following activities:

* A [Load file](load-file.md) activity uploads a file containing profiles data that were extracted from an external tool.

    For example:

    ```
    lastname;firstname;email;birthdate;
    JACKMAN;Megan;megan.jackman@testmail.com;07/08/1975;
    PHILLIPS;Edward;phillips@testmail.com;09/03/1986;
    WEAVER;Justin;justin_w@testmail.com;11/15/1990;
    MARTIN;Babe;babeth_martin@testmail.net;11/25/1964;
    REESE;Richard;rreese@testmail.com;02/08/1987;
    ```

* A **Reconciliation** activity which identifies the incoming data as profiles, by using the **email** and **Date of birth** fields as reconciliation criteria.

    ![](../assets/workflow-reconciliation-sample-1.1.png)

* A [Save audience](save-audience.md) activity to create a new audience based on these updates. You can also replace the **Save audience** activity by an **End** activity if no specific audience needs to be created or updated. Recipient profiles are updated in any case when you run the multi-step campaign.
