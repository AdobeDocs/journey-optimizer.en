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

Adobe Journey Optimizer enables brands to deliver connected and contextualized customer journeys throughout the customer lifecycle. It allows teams to personalize interactions at scale and aligns customer expectations with business goals. This documentation explains the key roles in using Journey Optimizer effectively, their responsibilities, and how to get started.

**Important Note:** Adobe Journey Optimizer defines distinct roles with specific responsibilities. A single individual can perform multiple roles or all roles, depending on your organization's structure.

## Role-Based Quick Start Guides

To simplify implementation, Adobe Journey Optimizer organizes tasks into specific roles based on expertise. Each role focuses on essential tasks required to deliver a seamless customer experience.

| Role              | Primary Responsibilities          | Key Skills                      | Typical Tasks                                   |
|-------------------|----------------------------------|--------------------------------|-----------------------------------------------|
| **Administrator** | Environment setup and access management | System configuration, user management, security | Configure sandboxes, manage permissions, set up channel configurations |
| **Data Engineer** | Data foundation and architecture | Data modeling, XDM schemas, data quality | Create schemas and datasets, configure data ingestion, manage data lifecycle |
| **Developer**     | Technical implementation and integrations | Mobile/Web SDK, APIs, event-driven architecture | Integrate SDKs, implement events, build custom action endpoints |
| **Marketer**      | Customer experience design and execution | Journey design, content creation, data analysis | Build journeys, create personalized content, optimize campaigns |

Each role addresses a specific phase of Adobe Journey Optimizer implementation and ensures a structured and efficient deployment process.

## Implementation Order and Role Dependencies

A successful Journey Optimizer implementation typically follows this sequence, which reflects the dependencies between roles:

1. **Administrator**: Sets up the environment  
   The Administrator establishes the foundation by configuring sandboxes, setting up access controls, and preparing channel configurations. This must happen first to enable other teams to work.  
   * Configure development, staging, and production sandboxes  
   * Set up roles, permissions, and object-level access control (OLAC)  
   * Configure channel configurations (email, SMS, push, in-app, web, content cards)
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
   * Implement Web SDK for web experiences  
   * Send events from applications to trigger journeys
   * Build custom action endpoints for external system integrations  
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

Focus on creating personalized customer experiences across all channels.

**Key capabilities you'll use:**

* Create audiences and build segments with multiple methods (segment definitions, CSV upload, audience composition)
* Design content with AI Assistant for text and image generation
* Build multi-channel customer journeys with drag-and-drop designer
* Leverage send-time optimization and conflict management to maximize engagement
* Test content and use approval workflows before publishing
* Monitor performance with integrated reporting dashboards

**Start with:** Create a simple welcome journey or abandoned cart recovery campaign using pre-built templates.

[Get Started as a Marketer →](path/marketer.md)

### For Data Engineers {#for-data-engineers}

Establish the data foundation that powers personalized experiences.

**Key responsibilities:**

* Create identity namespaces and configure identity resolution
* Design XDM schemas for profile and event data (standard and relational)
* Set up datasets and enable them for Real-time Customer Profile
* Configure source connectors for batch and streaming data ingestion
* Create computed attributes to simplify segmentation
* Configure events and data sources for journey execution
* Manage data quality, governance, and lifecycle

**Start with:** Set up identity namespaces and create your first profile schema with the required field groups.

[Get Started as a Data Engineer →](path/data-engineer.md)

### For Administrators {#for-administrators}

Set up and manage the Journey Optimizer environment for your organization.

**Key responsibilities:**

* Create and manage sandboxes for development, testing, and production
* Configure roles and permissions using out-of-the-box or custom roles
* Apply object-level access control (OLAC) to secure resources
* Set up channel configurations for email, SMS, push, in-app, web, and content cards
* Delegate subdomains and create IP pools for email deliverability
* Manage suppression lists and allowed lists
* Configure consent policies and data governance (with Healthcare/Privacy Shield)

**Start with:** Configure sandboxes, set up basic roles and permissions, then work with your team on channel configurations.

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

Successful Journey Optimizer implementations require collaboration across all roles:

* **Administrators** enable other roles by setting up sandboxes, permissions, and channel configurations
* **Data Engineers** provide the data foundation that Developers and Marketers build upon
* **Developers** implement the technical integrations that Marketers use to trigger journeys
* **Marketers** provide feedback to all teams on data quality, feature requests, and user experience

**Best practice:** Hold regular cross-functional meetings to align on priorities, share progress, and address blockers across teams.

## How-to Video {#video}

To learn more about Journey Optimizer's key capabilities and personas, watch the introductory video. The video walks through the user interface and highlights key features based on role-specific workflows.

>[!VIDEO](https://video.tv.adobe.com/v/3424995?quality=12)

## Additional Resources

For more in-depth learning and updates, explore the following resources:

**Learning & Documentation:**

* [Tutorial Videos](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/overview.html){target="_blank"} - Step-by-step video tutorials for all roles
* [Journey Use Cases Library](../building-journeys/jo-use-cases.md) - Practical examples and implementation patterns
* [AI & Intelligent Features](ai-features.md) - Learn about AI Assistant, send-time optimization, and content generation
* [User Interface Guide](user-interface.md) - Navigate Journey Optimizer effectively

**Stay Updated:**

* [Release Notes](../rn/release-notes.md) - Latest features, improvements, and fixes
* [Documentation Updates](../rn/documentation-updates.md) - Track recent documentation changes
* **Product Notifications** - Enable alerts in your [Adobe Experience Cloud profile](https://experience.adobe.com/preferences){target="_blank"} to receive notifications about new releases, maintenance windows, and important announcements. Click your profile icon > Preferences > Notifications to configure.

**Community & Support:**

* [Experience League Community](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer/ct-p/journey-optimizer){target="_blank"} - Connect with other users and experts
* [Product Forum](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer/ct-p/journey-optimizer){target="_blank"} - Ask questions and share knowledge
