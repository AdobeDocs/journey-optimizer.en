---
solution: Journey Optimizer
product: journey optimizer
title: Multi-step campaign event variables
description: Learn how to leverage event variables in your multi-step campaigns
hide: yes
hidefromtoc: yes
exl-id: f86dd262-0209-42f6-a180-736f1de98d78
---
# Multi-step campaign event variables {#event-variables}

Some multi-step campaign activities allow you to edit scripts in the expression editor to perform specific actions such as retrieving data coming from previous activities, building conditions, or computing file names based on event variables.
 
## What are event variables {#scripting}

Scripts executed in the context of a multi-step campaign access a series of additional global **objects** such as the multi-step campaign itself that is being executed (`ìnstance`), its various tasks (`task`), or the events that activated a given task (`event`).

To each type of **object** is associated a category of **variables** that can be leveraged in the expression editor when editing scripts in activities such as **[!UICONTROL JavaScript code]** or **[!UICONTROL Test]**.

* **Instance variables** (`instance.vars.xxx`) are comparable to global variables. They are shared by all activities.
* **Task variables** (`task.vars.xxx`) are comparable to local variables. They are only used by the current task. These variables are used by persistent activities to keep data and are sometimes used to exchange data between the different scripts of a same activity.
* **Event variables** (`vars.xxx`) enable the exchange of data between the elementary tasks of a multi-step campaign process. These variables are passed by the task that activated the task in progress. They are then passed to the following activities. **Event variables** are the most often used variables, and they should be used in preference to instance variables. 

## Leverage event variables in the expression editor {#expression-editor}

Predefined event variables are available for use in the expression editor left-hand side pane. You can also create new ones by initializing a new variable in your code.

![](assets/event-variables.png)

In addition to these event variables, you can also leverage the **[!UICONTROL Conditions]** menu in the left pane to build conditions and the **[!UICONTROL Add current date]** menu to use functions related to date formatting.
