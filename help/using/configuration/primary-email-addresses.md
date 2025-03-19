---
solution: Journey Optimizer
product: journey optimizer
title: Change the execution addresses 
description: Learn how to determine which email address to use from the profile service.
feature: Application Settings
topic: Administration
role: Admin
level: Intermediate
keywords: primary, execution, email, target, profile, optimizer
exl-id: fe2f6516-7790-4501-a3a1-3d7cb94d7874
---
# Change the execution addresses {#change-primary-email}

>[!CONTEXTUALHELP]
>id="ajo_admin_execution_address"
>title="Define which address to use"
>abstract="When several email addresses or phone numbers are available in the database (personal, professional, etc.), you can choose which one to prioritize for sending."

>[!CONTEXTUALHELP]
>id="ajo_admin_execution_address_header"
>title="Define which address to use"
>abstract="Edit the fields used to determine the profile's email address or phone number to prioritize for sending."

When you target a profile, several email addresses or phone numbers may be available in the database (professional email address, personal phone number, etc.).

In that case, [!DNL Journey Optimizer] uses **[!UICONTROL Execution fields]** to determine which email address or phone number to use from the profile service in priority.

To check the fields that are currently used by default, access the **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL General settings]** > **[!UICONTROL Executions fields]** menu.

![](assets/primary-address-execution-fields.png)

The current values are used for all deliveries at the sandbox level. You can update these fields if needed.

In most cases, you will change an execution field globally and define a value that should be used for all email or SMS messages. <!--[Learn how](#admin-settings)-->

<!--In some specific use cases only, you can override the value set globally and define a different value at the journey level. [Learn more](#journey-parameters)-->

## Update the Administration settings {#admin-settings}

To change the execution fields globally at the sandbox level, follow the steps below.

1. Access the  **[!UICONTROL Channels]** > **[!UICONTROL General settings]** > **[!UICONTROL Executions fields]** menu.

1. Click **[!UICONTROL Edit]** to change the default values.

    ![](assets/primary-address.png)

1. Click the current field of your choice or the edit icon to select a new field.

    ![](assets/primary-address-edit.png)

1. The list of available email-type XDM fields displays. Select the field to use.

    ![](assets/primary-address-select-field.png)

1. Click **[!UICONTROL Save]** to confirm your choice.

The execution field is updated and will now be used as the primary address.
    
<!--1. You can also select an additional field to use as secondary email address. This allows you to determine which field to use if the primary field is empty for a profile. -->

## Override the default execution field {#override-default-execution-address}

For specific use cases, you can override the execution field set globally and define a different value at the email configuration level or at the journey level.

Overriding this value may be useful for example to:

* Test an email. You can add your own email address: after you publish the journey, the email is sent to you.
* Send an email to the subscribers of a list. Learn more in [this use case](../building-journeys/message-to-subscribers-uc.md).

### In the email configuration

You can change the default execution field set in the [general settings](#admin-settings) when defining an email channel configuration. [Learn more](../email/email-settings.md#execution-address)

When an execution address is defined in the email configuration, it is used as the primary address and overrides the general setting at the sandbox level.

### In the journey parameters {#journey-parameters}

When adding an **[!UICONTROL Email]** action to a [journey](../email/create-email.md#create-email-journey-campaign), the primary email address is displayed under the journey advanced parameters.

In some specific contexts, you can override this value using the **[!UICONTROL Enable parameter override]** icon to the right of the **[!UICONTROL address]** field.

![](assets/journey-enable-parameter-override.png)

>[!CAUTION]
>
>Email address override should only be used for specific use cases. Most of the time, you do not need to change the email address because the value defined as the primary address in the **[!UICONTROL Execution fields]** is the one that should be used.


