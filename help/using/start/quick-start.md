---
solution: Journey Optimizer
product: journey optimizer
title: Roles and Responsibilities
description: Learn about the different roles involved in Adobe Journey Optimizer and their responsibilities
feature: Get Started
role: Admin, Developer, User
level: Beginner
exl-id: 71ab7369-fd84-46eb-95d2-941bd887d565
redpen-status: PASS_||_2025-04-28_15-13-07
---

# Roles and Responsibilities

Adobe Journey Optimizer enables brands to deliver connected, contextual, and personalized experiences throughout the customer journey. Built with an end-to-end focus on scale, speed, and flexibility, Journey Optimizer combines three main value drivers in a unified application:

* **Real-time customer insights and engagement** powered by Adobe's real-time customer profile
* **Modern omnichannel orchestration** through unified canvases for both real-time journeys and batch campaigns, plus a modern message designer
* **Intelligent decisioning and personalization** through decision management and AI/ML capabilities

Journey Optimizer offers two orchestration approaches to meet different marketing needs:

* **Journeys**: Best for real-time, one-to-one engagement where each customer moves through at their own pace, triggered by behavior or events
* **Orchestrated Campaigns**: Best for batch, one-to-many campaigns where audiences progress together through multi-step workflows on a schedule—ideal for seasonal promotions, product launches, and account-based communications

This unified experience allows you to implement entire use cases in one place, from defining audiences and designing journeys to creating personalized content and analyzing results. This documentation explains the key roles in using Journey Optimizer effectively, their responsibilities, and how to get started.

**Important Note:** Adobe Journey Optimizer defines distinct roles with specific responsibilities. A single individual can perform multiple roles or all roles, depending on your organization's structure.

## Role-Based Quick Start Guides

To simplify implementation, Adobe Journey Optimizer organizes tasks into specific roles based on expertise. Each role focuses on essential tasks required to deliver a seamless customer experience.

| Role              | Primary Responsibilities          | Key Skills                      | Typical Tasks                                   |
|-------------------|----------------------------------|--------------------------------|-----------------------------------------------|
| **Administrator** | Environment setup and access management | System configuration, user management, security | Set up sandboxes, manage user permissions, configure channels and message presets |
| **Data Engineer** | Customer profile data and data sources | Data modeling, XDM schemas, source connectors | Model profile and business data into schemas, configure source connectors, monitor data ingestion |
| **Developer**     | Technical implementation and integrations | Mobile/Web SDK, APIs, event-driven architecture | Integrate SDKs, implement events, build custom action endpoints |
| **Marketer**      | Journey design and personalized experiences | Journey orchestration, content creation, audience targeting | Design customer journeys, create and personalize messages, manage offers and decision components, define audiences |

Each role addresses a specific phase of Adobe Journey Optimizer implementation and ensures a structured and efficient deployment process.

## Implementation Order and Role Dependencies

A successful Journey Optimizer implementation typically follows this sequence, which reflects the dependencies between roles:

1. **Administrator**: Sets up the environment  
   The Administrator establishes the foundation by configuring sandboxes, setting up access controls, and preparing channel configurations. This must happen first to enable other teams to work.  
   * Configure development, staging, and production sandboxes  
   * Set up roles, permissions, and object-level access control (OLAC)  
   * Configure channel configurations (email, SMS, push, web push, in-app, web, direct mail, content cards)
   * Delegate subdomains and set up IP pools  
   * Configure suppression lists and consent policies

2. **Data Engineer**: Creates the data foundation  
   Data Engineers build the data infrastructure that powers personalization, defining how customer data flows into and through the system.  
   * Create identity namespaces for customer identification  
   * Design XDM schemas (profile, experience events, relational)
   * Set up datasets and enable them for Real-time Customer Profile  
   * Configure data ingestion (batch and streaming)
   * Create computed attributes for complex calculations
   * Configure events and data sources for journeys

3. **Developer**: Implements technical integrations  
   Developers connect applications to Journey Optimizer by integrating SDKs, sending events, and building API endpoints. These implementations enable journeys to trigger and execute.  
   * Integrate Mobile SDK (iOS/Android) with push notification setup  
   * Implement Web SDK for web experiences and web push notifications
   * Send events from applications to trigger journeys
   * Build custom action endpoints for external system integrations  
   * Monitor custom action health and performance
   * Test implementations using Adobe Experience Platform Assurance

4. **Marketer**: Designs and executes customer experiences  
   Marketers leverage all the foundational work to build journeys, create content, and optimize customer experiences across all channels.  
   * Build audiences using segmentation, CSV upload, or audience composition  
   * Design personalized content with AI Assistant and templates  
   * Create multi-channel journeys with event and audience triggers
   * Test with approval workflows before launch
   * Monitor performance and optimize based on reporting insights  

 **Note:** While this sequence is typical, some activities can occur in parallel. For instance, Developers may work on app integrations while Data Engineers configure schemas.

## Getting Started by Role

Each role begins with specific tasks tailored to its focus. Completing these initial steps ensures smoother onboarding and alignment with the overall implementation process:

### For Marketers {#for-marketers}

As a Marketer or Business Practitioner, you design customer journeys to deliver personal, contextual experiences across all touchpoints. You'll work in a unified interface to implement entire use cases from start to finish.

**Key capabilities you'll use:**

* **Journey Orchestration**: Create real-time, one-to-one customer engagement where each person moves through at their own pace, triggered by behavior or events across channels. Use the unified Action activity for all channel actions, the Content decision activity to integrate offers into journeys, and Journey Agent to create journeys from natural language prompts
* **Campaign Orchestration**: Design and automate complex, multi-step batch campaigns at scale using a visual canvas. Perfect for brand-initiated campaigns like seasonal promotions, product launches, and account-based communications. Leverage multi-entity segmentation to create precise audiences by connecting customer data with related entities (accounts, purchases, bookings). Use wave sending to deliver messages in controlled batches
* **Modern Message Designer**: Design and personalize email and mobile messages with a drag-and-drop interface. Edit out-of-the-box templates to accelerate time to market
* **Decision Management**: Create and manage offers, eligibility rules, and other components in a centralized library that can be embedded in emails and customer touchpoints. Use Decisioning for push and SMS personalization
* **Asset Management**: Access Adobe Experience Manager Assets Essentials fully embedded into Journey Optimizer for streamlined asset access and delivery
* **Audience Definition**: Build on-demand audiences with instant refinement using relational queries, with pre-send visibility for accurate audience counts
* **AI/ML Services**: Leverage send-time optimization and predictive engagement scores to target high-value customers and minimize churn risk
* **Delivery Control**: Use quiet hours (time-based exclusions) and conflict management to respect customer preferences and prevent over-communication

**Start with:** Use case templates and wizards to easily create and deploy new customer journeys. Use Journey Agent to create journeys from natural language prompts.

[Get Started as a Marketer →](path/marketer.md)

### For Data Engineers {#for-data-engineers}

As a Data Architect or Engineer, you set up and maintain the customer profile data and other data sources that power the experiences orchestrated by Journey Optimizer.

**Key responsibilities:**

* **Customer Profile Data**: Model customer profile data and business data into schemas to create a unified 360-degree view of the customer
* **Relational Data Modeling**: For Orchestrated campaigns, design relational schemas to enable multi-entity segmentation—connecting customer data with related entities like accounts, purchases, subscriptions, and bookings for flexible audience creation
* **Source Connectors**: Configure source connectors to ingest data from web, CRM, offline data, and other sources into Adobe Experience Platform
* **Identity Resolution**: Set up identity namespaces to continuously update profiles and move customers in and out of segments and journeys in real-time
* **Data Sources**: Configure data sources to listen in real-time to external signals across the customer journey
* **Profile Management**: Enable datasets for Real-time Customer Profile to power personalized experiences
* **Data Quality**: Monitor data ingestion to ensure everything flows smoothly into Journey Optimizer

**Start with:** Review the [Get started with data management](../data/gs-data.md) overview to understand schemas, datasets, identities, and the full data setup checklist. Then model your first customer profile schema and configure a source connector to begin ingesting data.

[Get Started as a Data Engineer →](path/data-engineer.md)

### For Administrators {#for-administrators}

As an Administrator, you set up the Journey Optimizer environment to enable your teams to work efficiently and securely.

**Key responsibilities:**

* **Sandboxes**: Create and manage sandboxes to partition data and journeys for different user groups (development, testing, production)
* **User Management**: Set up user groups and permissions to control access to different functionality
* **Channel Setup**: Configure delivery channels and message presets to ensure consistent branding across messages and assets delivered through Journey Optimizer
* **Security & Governance**: Apply object-level access control (OLAC), configure consent policies, and implement data governance policies
* **Deliverability**: Delegate subdomains, migrate subdomains to custom delegation when needed, create IP pools, and manage suppression lists and allowed lists
* **Journey Configuration**: Set up journey elements and configurations for your teams
* **Channel Configuration**: Configure web push notifications, direct mail, and message export (email/SMS) when required

**Start with:** Configure sandboxes and user permissions, then set up your first channel configurations and message presets.

[Get Started as an Administrator →](path/administrator.md)

### For Developers {#for-developers}

Implement technical integrations that connect Journey Optimizer to your applications.

**Key responsibilities:**

* Integrate Adobe Experience Platform Mobile SDK (iOS/Android)
* Implement Web SDK for web experiences and web push notifications
* Configure push notification credentials and certificates
* Send events from applications to trigger journeys
* Build API endpoints that Journey Optimizer calls via custom actions
* Implement code-based experiences for web, mobile, and other surfaces
* Test and debug implementations with Adobe Experience Platform Assurance
* Work with Journey Optimizer APIs for programmatic access

**Start with:** Integrate the Mobile or Web SDK, then implement your first event to trigger a journey.

[Get Started as a Developer →](path/developer.md)  

## Cross-Role Collaboration

Successful Journey Optimizer implementations require collaboration across all roles. Each role works with others to deliver seamless customer experiences:

>[!BEGINTABS]

>[!TAB Administrators]

**Administrators** enable all teams by managing access and configurations. They work with:

* **Data Engineers**: Grant permissions for data management, approve sandbox access, coordinate on governance policies
* **Developers**: Provide API credentials, set up testing environments, approve channel configurations
* **Marketers**: Assign permissions for journeys/campaigns, configure channels, support testing environments

>[!TAB Data Engineers]

**Data Engineers** provide the data foundation for everyone. They work with:

* **Administrators**: Request permissions for data management, coordinate on governance and retention policies
* **Developers**: Provide XDM schemas and event structures, define event payload formats, test data ingestion
* **Marketers**: Create computed attributes for personalization, build audiences, configure relational schemas

>[!TAB Developers]

**Developers** implement technical integrations that power journeys. They work with:

* **Data Engineers**: Get XDM schemas and event structures, align on data collection requirements, test event delivery
* **Administrators**: Provide API specifications, request permissions and credentials, coordinate on testing strategy
* **Marketers**: Understand event triggers, implement tracking, support journey testing, troubleshoot issues

>[!TAB Marketers]

**Marketers** design customer experiences and provide feedback. They work with:

* **Data Engineers**: Request computed attributes, coordinate on audience requirements, provide feedback on data quality
* **Developers**: Align on event triggers, test implementations, validate tracking
* **Administrators**: Request channel configurations, confirm feature access, coordinate on enablement

>[!ENDTABS]

**Best practice:** Hold regular cross-functional meetings to align on priorities, share progress, and address blockers across teams.

## How-to Video {#video}

To learn more about Journey Optimizer's key capabilities and personas, watch the introductory video. The video walks through the user interface and highlights key features based on role-specific workflows.

>[!VIDEO](https://video.tv.adobe.com/v/3424995?quality=12)

## Additional Resources

For more in-depth learning and updates, explore the following resources:

>[!BEGINTABS]

>[!TAB Learning & Documentation]

* [Tutorial Videos](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/overview.html){target="_blank"} - Step-by-step video tutorials for all roles
* [Get started with data management](../data/gs-data.md) - Schemas, datasets, identities, and the data readiness checklist for Journey Optimizer
* [Journey Use Cases Library](../building-journeys/jo-use-cases.md) - Practical examples and implementation patterns
* [AI & Intelligent Features](ai-features.md) - Learn about AI Assistant, send-time optimization, and content generation
* [User Interface Guide](user-interface.md) - Navigate Journey Optimizer effectively

>[!TAB Stay Updated]

* [Release Notes](../rn/release-notes.md) - Latest features, improvements, and fixes
* [Documentation Updates](../rn/documentation-updates.md) - Track recent documentation changes
* [Product Notifications](../rn/releases.md#staying-informed) - Learn how to subscribe to email and in-product alerts for Journey Optimizer updates

>[!TAB Community & Support]

* [Experience League Community](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer/ct-p/journey-optimizer){target="_blank"} - Connect with other users and experts
* [Product Forum](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer/ct-p/journey-optimizer){target="_blank"} - Ask questions and share knowledge

>[!ENDTABS]
