---
solution: Journey Optimizer
product: journey optimizer
title: Key terminology
description: Key terminology in AJO
feature: Get Started
role: Admin, Developer, User
level: Beginner
redpen-status: PASS_||_2025-04-28_15-13-07
exl-id: d4c968d2-5eae-4fff-9b67-427ac9d9d74c
hide: yes
---
# Terminology

Welcome to the Adobe Journey Optimizer terminology guide. This resource provides clear and straightforward definitions of key terms you encounter while using the platform. Understanding these terms helps you navigate Adobe Journey Optimizer confidently, implement marketing strategies effectively, and collaborate efficiently with team members and Adobe support.

## Core Platform Terms

| Term | Definition |
|------|------------|
| **Adobe Journey Optimizer (AJO)** | A tool that enables you to create and send personalized messages to customers across channels, such as email, text messages, and mobile app notifications. It allows you to design customer journeys that respond to real-time customer actions. For example, an email confirmation triggers immediately after a customer makes a purchase on your website. |
| **Adobe Experience Platform (AEP)** | The foundation of Adobe Journey Optimizer. It collects and organizes all customer data in one place, creating complete customer profiles that Adobe Journey Optimizer uses to send personalized messages. Consider AEP as the central hub driving customer engagement strategies. |
| **Sandbox** | A separate workspace where you test and experiment without affecting live customer communications. A sandbox functions as a practice area or test environment. Adobe Journey Optimizer provides up to five sandboxes, enabling teams to test scenarios such as onboarding journeys or promotional campaigns. |

## Journey & Campaign Terms

| Term | Definition |
|------|------------|
| **Journey** | A series of connected steps that guide customers through experiences with your brand. For example, a welcome journey includes a welcome email, an app download reminder, and personalized product recommendations. Each step occurs after the previous one completes, enabling sequential, personalized interactions. |
| **Campaign** | A single communication or a set of identical communications sent to a specific group of customers at the same time. Unlike journeys, which unfold over time, campaigns deliver messages simultaneously, either immediately or at a scheduled time. For example, you can schedule a promotional email campaign for a weekend sale. |
| **Channel** | The method used to communicate with customers, such as email, text message (SMS), push notifications (mobile app alerts), in-app messages, or websites. Each channel requires specific setup, such as verifying an email domain or connecting an SMS provider. |
| **Message** | The content sent to customers, including text, images, and personalized elements. You create messages for various formats, such as emails, text messages, and push notifications. For example, a message could be a "thank you" email with dynamically inserted customer names and order details. |
| **Event** | An occurrence that triggers or advances a journey. Events include customer actions, such as making a purchase, or system events, such as a new customer signing up. Events enable journeys to respond to real-time customer actions. For example, a customer’s birthday triggers a special discount email. |

## Customer & Audience Terms

| Term | Definition |
|------|------------|
| **Profile** | A complete view of each customer that combines information such as contact details, purchase history, preferences, and behaviors. An "Engageable Profile" refers to a customer contacted using Adobe Journey Optimizer in the past 12 months. Profiles are essential for creating personalized, data-driven experiences. |
| **Audience** | A group of customers who share common characteristics or behaviors. For example, "customers who purchased in the last 30 days" or "customers interested in outdoor products." Audiences are created in Adobe Experience Platform and used in Adobe Journey Optimizer to target specific segments. |
| **Audience Qualification** | The process that occurs when a customer joins or leaves an audience. Adobe Journey Optimizer triggers actions automatically when someone enters or exits an audience. For example, it sends a welcome message to new loyalty program members, ensuring timely and relevant communications. |
| **Addressable Audience** | The total number of customer profiles you can potentially reach. Your account allows for an Addressable Audience that is 25% larger than your contracted Engageable Audience, providing flexibility as your customer base grows. |
| **Engageable Audience** | The number of customers you actively communicate with through Adobe Journey Optimizer based on your contract. This ensures you stay within licensing limits while focusing on high-value interactions. |
| **Segment Definition** | The rules that determine which customers belong to an audience. These rules are based on attributes, behaviors, or other criteria. For example, a segment definition might include "customers who spent over $500 in the last six months." |

## Decision Management Terms

| Term | Definition |
|------|------------|
| **Decision Management** | A feature that automatically selects the best content or offer for each customer. For example, it recommends a free shipping offer to a customer who frequently abandons their cart. This ensures personalized and relevant interactions. |
| **Offer** | A specific marketing message or promotion presented to customers. Examples include a 20% discount, free shipping offer, or product recommendation. Adobe Journey Optimizer includes up to 10 offers per email, enabling diverse and tailored content. |
| **Decisioning API** | A technical connection that allows other systems to ask Adobe Journey Optimizer, "What’s the best offer for this customer right now?" The selected offer is displayed on websites, apps, or other channels. This integration extends Journey Optimizer's capabilities beyond email and SMS. |
| **Offer Library** | A centralized collection where all marketing offers are stored and managed. This ensures consistency across channels and simplifies updates to promotional strategies. |
| **Eligibility Rules** | Conditions that determine whether a customer can receive a particular offer. For example, "Only show this discount to customers who haven’t purchased in 60 days." These rules help prevent over-messaging or irrelevant offers. |

## Data & Technical Terms

| Term | Definition |
|------|------------|
| **Data Landing Zone** | A temporary storage area where you place data files before moving them into Adobe Experience Platform. Consider it a staging area for your data. For example, you upload a CSV file of customer transactions here before integrating it into the system. |
| **Query Service** | A tool that allows you to run database-style queries to validate data after it is imported into Adobe Journey Optimizer. For example, you query "How many customers signed up in the past week?" to ensure audience segmentation accuracy. |
| **Computed Attribute** | A customer characteristic calculated from their behavior. For example, "average purchase value" or "total website visits this month." These attributes help you personalize messages based on customer patterns, such as targeting high-value customers with exclusive offers. |
| **Personalization Fields** | Placeholders in messages that are replaced with customer-specific information, such as first name, recent purchases, or membership level. Adobe Journey Optimizer supports up to five personalization fields per message. For example, "Hi [First Name], your recent purchase of [Product Name] is on its way!" |
| **Schema** | The blueprint defining how customer data is organized. It maps the types of information stored and their relationships. A clear schema ensures seamless integration and accurate data usage across workflows. |
| **Dataset** | A collection of related data organized according to a schema. For example, you might have separate datasets for purchase history, website activity, and customer service interactions. These datasets allow you to analyze and act on different aspects of customer behavior. |

## Content & Asset Terms

| Term | Definition |
|------|------------|
| **AI Assistant** | A built-in feature that uses artificial intelligence to help create content. It generates text, designs emails, or creates message variations for different channels. For example, you ask it to draft a promotional email based on audience preferences. |
| **Assets Essentials** | A library included with Adobe Journey Optimizer for storing and managing digital files such as images, logos, and documents. It includes storage for marketing assets and supports up to five users with full permissions and 100 users with view access. This simplifies collaboration and ensures brand consistency. |
| **Content Fragment** | A reusable piece of content used in multiple messages. For example, a standard footer with contact information that appears in all emails. This ensures consistency and reduces the time spent recreating shared elements. |
| **Template** | A pre-designed message layout customized with specific content. Templates help maintain a consistent look and feel across communications, such as branded email designs or SMS formats. |

## Reporting & Analysis Terms

| Term | Definition |
|------|------------|
| **Global Report** | A comprehensive overview showing how all journeys and campaigns perform. It helps you understand trends in engagement rates across channels and evaluate overall marketing effectiveness. |
| **Live Report** | Real-time data about currently running journeys and campaigns. This allows immediate adjustments if needed. For example, you pause a campaign with low engagement and revise its messaging. |
| **Journey Report** | Detailed performance insights into a specific journey. It shows how customers move through each step and identifies where they might drop off. This helps optimize customer experiences. |
| **Message Report** | Statistics about a specific message, such as how many were delivered, opened, and clicked. This information helps refine future communications by showing how well customers respond to your content. |

## Related Documentation

* [Get started with Adobe Journey Optimizer](get-started.md)
* [Architecture & Concepts](architecture-concepts-redpen.md)
* [Functional Areas Guide](functional-areas-redpen.md)
