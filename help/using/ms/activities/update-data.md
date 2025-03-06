---
solution: Journey Optimizer
product: journey optimizer
title: Use the Update data activity in your multi-step campaigns
description: Learn how to use the Update data activity
---
# Update data {#update-data}

The **Update data** activity is a **Data Management** activity. It allows you to perform a mass update on fields in the database. Several options allow you to personalize the data update.

<!--
The **Operation type** field lets you choose the process to be carried out on the data in the database. Select the first option to add data or update (it if it has already been added). You can also only add data, only update data, or delete data. Select the **Update and merge collections** to select a primary record to link duplicates to, and delete those duplicates safely

Specify how to identify the records in the database: if data relate to an existing targeting dimension, select the **Using the targeting dimension** option and select the targeting dimension and fields to update. Otherwise, specify one or more custom links to identify the data in the database, or direct use of reconciliation keys.

Select the fields to update and reconciliation settings. You can use the **Auto-mapping** option to automatically identify the fields to be updated.

The **Advanced options** section let you specify additional settings to manage data and duplicates.

Toggle the **Generate an outbound transition** option to add an outbound transition that will be activated at the end of the execution of the **Update data** activity. The update generally marks the end of a targeting workflow and therefore the option is not activated by default.

Toggle the **Generate an outbound transition for rejects** option to add an outbound transition containing records that have not been correctly processed after the update (for example if there is a duplicate). The update generally marks the end of a targeting workflow and therefore the option is not activated by default.
-->

## Configure the Update data activity{#update-data-configuration}

To configure the **Update data** activity, start by adding the activity to your multi-step campaign and define a label.

![](../assets/workflow-update-data.png)

### Operation type

The **Operation type** field lets you choose the process to be carried out on the data in the database:

* **Insert or update**: insert data or update it if the records already exist in the database.
* **Insert**: insert data only. The records that already exist are not updated. If reconciliation criteria are defined, only the non-reconciled records will be added.
* **Update**: update data of the records that already exist in the database only.
* **Delete**: delete data.

The **Batch size** field lets you select the number of inbound transition elements to be updated. For example, if you state 500, the first 500 records dealt with will be updated.

### Record identification

This section allows you to specify how to identify the records in the database:

* If data entries relate to an existing targeting dimension, select the **Using the targeting dimension** option and select it from in the **Targeting dimension to update** field.
* You can also select the **Using custom links** and specify one or more links which will enable identification of the data in the database 
* If the operation type selected requires an update, you must use the **Using reconciliation rules** option.

### Fields to update

In the **Fields to update** section, add the fields on which the update will be applied and, if necessary, add conditions so that this update is carried out. To do this, use the **Taken into account if** field. The conditions are applied one after the other in list order. Use the arrows on the right to change the order of the updates. You can use the same destination field multiple times.

You can automatically link fields using the **Auto-mapping** button. Automatic linking detects fields with the same name.

During an **Insert or update** operation type, you can individually select the operation to apply for each field. To do this, select the value you would like in the **Operation type** field.

### Advanced options

The **Advanced options** lets you specify additional options to deal with updating data as well as managing duplicates.

<!--
* **Disable automatic key management**
* **Disable audit**
* **Empty the destination value if the source value is empty**
* **Update all columns with matching names**
* **Ignore records which concern the same target**: only the first in the list of expressions will be considered
-->

The last two options allow you to perform specific actions:

* **Generate an outbound transition**: creates an outbound transition that will be activated at the end of execution. Updating usually signals the end of a targeting workflow, and the option is therefore not activated by default.

* **Generate an outbound transition for the rejects**: creates an outbound transition containing records that have not been correctly processed after the update (for example if there is a duplicate). The update generally marks the end of a targeting multi-step campaign and therefore the option is not activated by default.
