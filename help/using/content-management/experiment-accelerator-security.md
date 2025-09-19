---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer Experimentation Accelerator
description: Data usage in AI with Journey Optimizer Experimentation Accelerator
feature: Experimentation
topic: Content Management
role: User
level: Beginner
keywords: content, experiment, multiple, audience, treatment
hide: yes
hidefromtoc: yes
---
# Data usage in AI with Journey Optimizer Experimentation Accelerator{#experiment-accelerator-security}

>[!BEGINSHADEBOX]

* [Get started with the Journey Optimizer Experimentation Accelerator](experiment-accelerator.md)
* [Data usage in AI with Journey Optimizer Experimentation Accelerator](experiment-accelerator-security.md)
* [Journey Optimizer Experimentation Accelerator best practices](experiment-accelerator-best-practices.md)
* [Monitor Experiments](experiment-accelerator-monitor.md)
* [Experimentation metrics](experiment-accelerator-metrics.md)

>[!ENDSHADEBOX]

**Adobe Journey Optimizer Journey Optimizer Experimentation Accelerator** allows you to automatically discover insights and recommend opportunities to improve your experiments and experimentation program. The solution leverages AI and Machine Learning to provide these recommendations. This statement clarifies how your customers' data is used in **Journey Optimizer Experimentation Accelerator**.

## What data does Journey Optimizer Experimentation Accelerator use?

Currently there are three types of data used by **Journey Optimizer Experimentation Accelerator**:

* **Experiment Metadata**: experiment name, the definition of the audience used in the experiment and the treatments in the experiment, e.g. name, split percentages, location or surface the experiment is served into.

* **Performance of the treatments**: number of people, mean of the success metric and standard deviation for each treatment.

* **Content of the treatment**: the rendered HTML and screenshot of the treatment as it would appear to a user on your website.

## What does Journey Optimizer Experimentation Accelerator do with this data?

**Journey Optimizer Experimentation Accelerator** takes the content for each treatment and creates an embedding, i.e. a mathematical representation of the content, then correlates those embeddings with the performance of the treatments. This process allows extraction of the content attributes that have performed best for future use. Those attributes are then fed into an Adobe hosted large language model, which converts them into human readable statements used to generate insights and suggest opportunities.

## What restrictions does Journey Optimizer Experimentation Accelerator have on the data used?

Each customer is assigned to a specific organization and sandbox. A dedicated model is trained for every sandbox. When a sandbox is deleted, all related data, signals, and models are permanently removed.

* We only use customer data to train or fine-tune the model from that customer.

* We never mix customers to train or fine-tune a model.

## Will Adobe models or AI change a brand's user experience automatically?

No. **Journey Optimizer Experimentation Accelerator** only makeq recommendations of what could be changed and how it could be changed. Only users who have permissions to change the experience using Journey Optimizer or Target will be able to act on these recommendations. All recommendations can be reviewed and edited before being pushed out.

## Is there any risk to their data or system stability?

**Journey Optimizer Experimentation Accelerator** only ingests and analyzes data, producing insights and recommendations for future testing. It does not have access to modify any test settings. All suggestions generated within the tool are sent to Target and Journey Optimizer for implementation, ensuring no impact on a customer's current activities.
