---
solution: Journey Optimizer
product: journey optimizer
title: Orchestrated campaigns Frequently Asked Questions
description: Frequently Asked Questions about Journey Optimizer Orchestrated campaigns
hide: yes
hidefromtoc: yes
exl-id: 6a660605-5f75-4c0c-af84-9c19d82d30a0
---
# Frequently Asked Questions {#faq-oc}

You will find below Frequently Asked Questions about Adobe Journey Optimizer Orchestrated Campaigns.

Need more details? Use the feedback options at the bottom of this page to raise your question.

## What are Orchestrated Campaigns? {#what-are-oc}

Orchestrated Campaigns in Adobe Journey Optimizer help brands run complex, one-to-many marketing campaigns at scale. They are designed for brand-initiated engagement, such as promotions, seasonal campaigns, or account-based communications.  

Compared with single-send campaigns, they bring **orchestration and sequencing** to outbound marketing: audiences move through a multi-step workflow together, rather than receiving a one-off blast.  

## What can I do with Orchestrated Campaigns? {#what-can-i-do}

Key capabilities include:

* **On-Demand Audiences**: Instantly build and refine target groups using relational queries.  
* **Multi-Entity Segmentation**: Create precise audiences by connecting customer data with related entities (e.g., accounts, purchases, bookings).  
* **Pre-Send Visibility**: See accurate audience counts before launching to optimize targeting.  
* **Multi-Step Workflows**: Run sequenced campaigns such as seasonal promotions, product launches, or loyalty offers.  

>[!BEGINSHADEBOX]

**Best practices**

* Define a **clear campaign objective** before designing workflows.  
* Start with a **pilot audience** to validate counts and logic before scaling.  
* Keep segmentation rules **as simple as possible** to optimize performance and transparency.  
* Use **consistent naming conventions** for audiences and campaigns to make management easier.  

>[!ENDSHADEBOX]


## Which channels are supported? {#channels}

Orchestrated Campaigns support **email, SMS, and push notifications**.  

>[!BEGINSHADEBOX]

**Recommendations**

* Match the channel to the **nature of your message** (e.g., urgent = SMS, personalized offers = email, contextual = push).  
* Always validate consent and subscription preferences before activating a channel.  
* Test message rendering across multiple devices and clients to ensure consistent experience.   

>[!ENDSHADEBOX]

## How are Orchestrated Campaigns different from Journeys? {#oc-vs-journeys}

* **Orchestrated Campaigns**: Best for **batch, one-to-many** campaigns. Entire audiences move through the campaign canvas together.  
* **Journeys**: Best for **real-time, one-to-one** engagement. Each customer moves through the journey at their own pace, triggered by behavior or events.  

>[!BEGINSHADEBOX]

**Tip** - Many organizations use **both together**—Journeys for triggered, reactive experiences, and Orchestrated Campaigns for planned, calendar-based initiatives.  

>[!ENDSHADEBOX]

## How does the data model work? {#data-model}

Campaigns use a **relational database**. This allows you to query across different data sets (e.g., customers, products, subscriptions) and connect them flexibly for advanced segmentation.  

>[!BEGINSHADEBOX]

**Best practices**

* Organize datasets so that **relationships (joins)** reflect business logic.  
* Avoid unnecessary joins to keep queries performant.  
* Validate sample results before running large-scale extractions.  

>[!ENDSHADEBOX]

## Can I personalize messages with this data? {#personalization}

Yes. You can use customer profiles along with linked data (like purchases or subscriptions) to personalize content across all supported channels.  

>[!BEGINSHADEBOX]

**Recommendations**

* Use **transactional and behavioral data** to make offers relevant.  
* Combine **static attributes** (e.g., loyalty tier) with **dynamic ones** (e.g., last purchase date).  
* Keep personalization concise—overloading messages with data can harm readability.  

>[!ENDSHADEBOX]


## Does it integrate with other Adobe solutions? {#integrations}

* **Customer Journey Analytics**: Campaign orchestration reports are available.  
* **Real-Time CDP**: Audiences built in Campaigns can be read in CDP.  
* **Federated Audience Composition (FAC)**: Available as an add-on.  

## What about permissions and consent? {#permissions}

Permissions and consent are centrally managed in Adobe Experience Platform. The same rules apply across both Journeys and Orchestrated Campaigns to ensure compliance and consistent customer experience.  

>[!BEGINSHADEBOX]

**Best practices**

* Apply **centralized governance**—avoid managing consent separately at campaign level.  
* Periodically audit consent data to detect inconsistencies.  
* Respect **channel-specific opt-outs**—do not assume global consent covers all channels.  

>[!ENDSHADEBOX]

## Can I do ad-hoc segmentation? {#ad-hoc}

Yes. With **Live Segmentation**, you can build complex queries on the spot and instantly activate them across outbound channels.  

>[!BEGINSHADEBOX]

**Tips**

* Use ad-hoc segmentation for **time-sensitive needs** (e.g., flash promotions).  
* Save and document useful queries so they can be reused in future campaigns.  
* Validate the audience count before activation to prevent under- or over-sending.  

>[!ENDSHADEBOX]

## Does this support decisioning? {#decisioning}

Currently, decisioning does not use relational data from Orchestrated Campaigns.  

## How does deployment across environments work? {#deployment}

Objects created in Orchestrated Campaigns (e.g., audiences, workflows) are tied to the sandbox in which they are built. Standard packaging and deployment workflows across environments (dev, stage, prod) are not currently available for Orchestrated Campaigns.  

>[!BEGINSHADEBOX]

**Best practices**

* Maintain **separate sandboxes** for experimentation, QA, and production.  
* Document configurations thoroughly to enable manual replication if needed.  
* Align with governance teams to reduce configuration drift between environments.   

>[!ENDSHADEBOX]

## Are there recommended practices for running campaigns at scale? {#scale}

Yes, follow the best practices below:  

* **Plan campaigns around business calendars** (product launches, seasonal peaks) to align volume and resources.  
* Use **audience pre-views** before sending to confirm the expected size and avoid surprises.  
* Where possible, **stagger send times** to avoid overwhelming downstream systems (e.g., call centers, websites).  
* Establish a **monitoring routine**—track delivery logs, error rates, and opt-outs after each send.  
* Run **post-campaign analysis** in Customer Journey Analytics to refine targeting and orchestration for the next cycle.  
