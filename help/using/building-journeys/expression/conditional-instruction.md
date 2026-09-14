---
solution: Journey Optimizer
product: journey optimizer
title: Conditional instruction (if, then, else)
description: Learn about conditional instruction
feature: Journeys
role: Developer
level: Experienced
keywords: advanced, condition, action, journey
exl-id: 5a5b35a7-e3b5-4dc0-8a87-e985956b04a4
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/SObpEvgu0D-pcoLVaKM7iRffLTSP1stp1zcg4Ygs-vQ
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: cce82f05-fc3c-4af7-85ff-8bba603861a7
    internal-label: Condition activities
  - id: d8353d85-5da7-453d-bd68-40ad33fa0ab7
    internal-label: Action activities
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Conditional instruction (if, then, else) {#conditional-instruction}

The conditional instruction (if, then, else) is supported in the advanced editor. It allows to define more complex expressions. It is composed of the following elements:

* **[!UICONTROL if]**: the condition to be evaluated first.
* **[!UICONTROL then]**: the expression to be evaluated in case the result of the condition evaluation is true.
* **[!UICONTROL else]**: the expression to be evaluated in case the result of the condition evaluation is false.

>[!NOTE]
>
>Parentheses are required around all the expressions.

   ```json
   if  (<expression1>)
   then
      (<expression2>)
   else
      (<expression3>)
   ```

`<expression1>` must return a **boolean**.

`<expression2>` and `<expression3>` must have the same type or compatible types. The supported signatures and returned types are:

   ```json
   boolean,boolean : boolean
   dateTime,dateTime : dateTime
   dateTimeOnly,dateTimeOnly : dateTimeOnly
   decimal,integer : decimal
   integer,decimal : integer
   integer,decimal : decimal
   duration,duration : duration
   string,string : string
   listBoolean,listBoolean : listBoolean
   listDateTime,listDateTime : listDateTime
   listDateTimeOnly,listDateTimeOnly : listDateTimeOnly
   listDateOnly,listDateOnly : listDateOnly
   listDecimal,listDecimal : listDecimal
   listInteger,listInteger : listInteger
   listString,listString : listString
   ```

**Usage**

The conditional instruction allows you to optimize the journey workflow by reducing the number of condition activities. For example, within the same action activity, you can specify two alternatives for a field definition using only one condition expression.

Example for an action activity (for a field that expects a string as the result of the conditional instruction):

   ```json
   if (startWithIgnoreCase(@event{eventiOSPushPermissionAllowed.device.model}, 'iPad') or startWithIgnoreCase(@event{eventiOSPushPermissionAllowed.device.model}, 'iOS'))
   then
      ('apns')
   else
      ('fcm')
   ```

{{$include /help/_includes/do-not-localize/building-journeys/ai-augmented-expression-conditional-instruction.md}}
