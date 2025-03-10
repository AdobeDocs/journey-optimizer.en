---
solution: Journey Optimizer
product: journey optimizer
title: Key principles of multi-step campaign creation
description: Learn key principles of multi-step campaigns with Adobe Journey Optimizer
hide: yes
hidefromtoc: yes
exl-id: b04aa15a-71bf-4683-bcbf-f611c189ffe1
---
# Key principles of multi-step campaign creation {#ms-campaign-creation}

With Adobe Journey Optimizer, you can build multi-step campaigns into a visual canvas to design cross-channel processes such as segmentation, campaign execution, file processing.

## What's inside a multi-step campaign? {#gs-ms-campaign-inside}

The multi-step campaign diagram is a representation of what is supposed to happen. It describes the various tasks to be performed and how they are linked together. 

![](assets/workflow-example.png){zoomable="yes"} {zoomable="yes"}

Each multi-step campaign contains:

* **Activities**: An activity is a task to be performed. The various activities are represented on the diagram by icons. Each activity has specific properties and other properties that are common to all activities.

    In a multi-step campaign diagram, a given activity can produce multiple tasks, in particular when there is a loop or recurrent actions.

* **Transitions**: Transitions link a source activity to a destination activity and define their sequence. 

* **Worktables**: The worktable contains all the information carried by the transition. Each multi-step campaign uses several worktables. The data conveyed in these tables can be used throughout the multi-step campaign's life cycle.

## Key steps to create a multi-step campaign {#gs-ms-campaign-steps}
    
Key steps to create multi-step campaign are as follows:

![](assets/workflow-creation-process.png){zoomable="yes"}
