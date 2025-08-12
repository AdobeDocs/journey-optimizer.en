---
solution: Journey Optimizer
product: journey optimizer
title: AJO Roles and Responsibilities
description: Learn about the different roles involved in Adobe Journey Optimizer and their responsibilities
feature: Get Started
role: Admin, Data Engineer, Developer, User
level: Beginner
exl-id: 71ab7369-fd84-46eb-95d2-941bd887d565
redpen-status: PASS_||_2025-04-28_15-13-07
---

# AJO Roles and Responsibilities

Adobe Journey Optimizer (AJO) enables brands to deliver connected and contextualized customer journeys throughout the customer lifecycle. It allows teams to personalize interactions at scale and aligns customer expectations with business goals. This documentation explains the key roles in using Journey Optimizer effectively, their responsibilities, and how to get started.

**Important Note:** Adobe Journey Optimizer defines distinct roles with specific responsibilities. A single individual can perform multiple roles or all roles, depending on your organization's structure.

## Role-Based Quick Start Guides

To simplify implementation, AJO organizes tasks into specific roles based on expertise. Each role focuses on essential tasks required to deliver a seamless customer experience.

| Role              | Primary Responsibilities          | Key Skills                      | Typical Tasks                                   |
|-------------------|----------------------------------|--------------------------------|-----------------------------------------------|
| **Administrator** | System setup and permission management | System configuration, user management, security | Configure sandboxes, manage users, set up channels |
| **Data Engineer** | Configure data structure and flows | Data modeling, schema design, API integration | Set up schemas, manage datasets, configure data sources |
| **Developer**     | Technical integrations and customizations | Mobile development, API implementation, coding | Integrate mobile apps, implement APIs, create custom actions |
| **Marketer**      | Design and execute customer journeys | Marketing strategy, content creation, journey design | Create campaigns, design journeys, analyze reports |

Each role addresses a specific phase of AJO implementation and ensures a structured and efficient deployment process.

## Implementation Order and Role Dependencies

A successful Journey Optimizer implementation typically follows this sequence, which reflects the dependencies between roles:

1. **Administrator**: Sets up the environment  
   The Administrator lays the technical foundation for the system and ensures proper access and configuration for all users.  
   * Configure sandboxes and permissions  
   * Set up user access  
   * Configure messaging channels and technical settings  

2. **Data Engineer**: Creates the data foundation  
   Data Engineers define the data structure and flow, which are essential for personalized experiences.  
   * Design and implement schemas  
   * Set up identity namespaces  
   * Configure data ingestion  
   * Create test profiles  

3. **Developer**: Handles technical integrations  
   Developers enable AJO to interact with mobile apps, websites, and external systems by implementing technical integrations. Push notifications, for example, rely on Developer-led configurations.  
   * Integrate mobile applications for push notifications  
   * Implement web SDKs  
   * Develop custom integrations using APIs  
   * Create custom actions for third-party systems  

4. **Marketer**: Creates and launches journeys  
   Marketers use the groundwork laid by other roles to design and deploy customer experiences. They focus on audience segmentation, personalized content, and journey optimization.  
   * Design audience segments  
   * Create personalized content  
   * Build and test journeys  
   * Analyze performance and optimize  

 **Note:** While this sequence is typical, some activities can occur in parallel. For instance, Developers may work on app integrations while Data Engineers configure schemas.

## Getting Started by Role

Each role begins with specific tasks tailored to its focus. Completing these initial steps ensures smoother onboarding and alignment with the overall implementation process:

1. **For Marketers**: Focus on journey creation, message design, and campaign execution.  
   Example: Start by creating a welcome email campaign for new customers.  

2. **For Data Engineers**: Establish the data foundation, configure schemas, and integrate data sources.  
   Example: Set up a schema to track customer purchase history for personalized recommendations.  

3. **For Administrators**: Set up environments, manage permissions, and configure messaging channels.  
   Example: Configure sandbox environments for testing different messaging strategies.  

4. **For Developers**: Integrate mobile apps, implement APIs, and build custom integrations.  
   Example: Use the AJO API to trigger push notifications based on customer actions within your mobile app.  

Click on your role below to access specific guidance tailored to your responsibilities:

* [Get Started as a Marketer](path/marketer.md)  
* [Get Started as a Data Engineer](path/data-engineer.md)  
* [Get Started as an Administrator](path/administrator.md)  

## How-to Video {#video}

To learn more about Journey Optimizer's key capabilities and personas, watch the introductory video. The video walks through the user interface and highlights key features based on role-specific workflows.

>[!VIDEO](https://video.tv.adobe.com/v/3424995?quality=12)

## Additional Resources

For more in-depth learning and updates, explore the following resources:  
* [Release Notes](https://experienceleague.adobe.com/docs/journey-optimizer/using/rn/release-notes.html)  
* [Tutorial Videos](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/overview.html)